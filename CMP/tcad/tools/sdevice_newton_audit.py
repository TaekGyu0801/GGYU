#!/usr/bin/env python3
"""
sdevice_newton_audit.py  --  CMP FAST_BASELINE Newton / cutback audit

Status : PROPOSED tool (parser tested only on a synthetic log, see --selftest).
Author : Claude for worker Lee Taek Gyu, 2026-10-04

Purpose
  Read-only analysis of a Sentaurus Device transient log (nX_des.out / .log)
  to quantify, per BE step attempt:
    pseudo-time t0 -> t1, stepsize, anode voltage (V = vscale * t),
    Newton iteration count, final |Rhs|, accepted / rejected, wallclock.
  and to predict what an inner-Coupled "Iterations = N" cap would change.

  Two-log mode (--cand) compares a FAST candidate log with the reference
  log: identical-step check, first divergence, wallclock to voltage
  milestones, and bottleneck-window cost.

It never modifies any file.  Copy the live log first, e.g.
    cp n6_des.out ~/x8_n6_des_$(date +%Y%m%d_%H%M).out

Usage
  python3 sdevice_newton_audit.py REF.out
  python3 sdevice_newton_audit.py REF.out --cand FAST.out --window 4.55 4.75
  python3 sdevice_newton_audit.py REF.out --csv ref_attempts.csv --raw 1
  python3 sdevice_newton_audit.py --selftest

Parsing rules (format-tolerant, verify with --raw):
  * an attempt starts at either "Computing BE-step from <a> s to <b> s" (T-2022.03 observed format)\n    or "Computing step from t=<a> to t=<b>"
  * Newton rows are lines starting with an integer index followed by numbers
    (with or without '|' separators); the column header line containing
    "Rhs" is used to locate the Rhs / error / time columns when present
  * an attempt is REJECTED when the next attempt starts at the same t0,
    ACCEPTED when the next attempt starts at this attempt's t1
  * wallclock: "Total ... <seconds>" (or "wallclock ... <seconds>") lines
    inside the attempt; if those values only grow, they are treated as
    cumulative and differenced.  The mode used is printed.
"""
import argparse
import csv
import math
import re
import statistics
import sys

FLOAT = r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?'
RE_STEP = re.compile(
    r'(?:Computing\\s+BE-step\\s+from\\s+|Computing\\s+step\\s+from\\s+t\\s*=\\s*)'
    + '(' + FLOAT + ')'
    + r'(?:\\s*s)?\\s+to\\s+(?:t\\s*=\\s*)?'
    + '(' + FLOAT + ')'
    + r'(?:\\s*s)?'
    + r'(?:\\s*\\(Stepsize:\\s*(' + FLOAT + r')\\s*s\\))?',
    re.I
)
RE_ROW = re.compile(r'^\s*(\d+)\s*(?:\|)?\s*(' + FLOAT + r')')
RE_TOTAL = re.compile(r'\bTotal\b[^0-9\n]*(' + FLOAT + r')', re.I)
RE_WALL = re.compile(r'wall\s*-?clock[^0-9\n]*(' + FLOAT + r')', re.I)
RE_FINISHED = re.compile(r'Finished,?\s*because', re.I)


class Attempt:
    __slots__ = ('idx', 't0', 't1', 'rows', 'reason', 'raw', 'tot', 'wall',
                 'status', 'cols', 'time_s')

    def __init__(self, idx, t0, t1):
        self.idx, self.t0, self.t1 = idx, t0, t1
        self.rows = []
        self.reason = ''
        self.raw = []
        self.tot = None
        self.wall = None
        self.status = 'unknown'
        self.cols = None
        self.time_s = None

    @property
    def dt(self):
        return self.t1 - self.t0

    @property
    def iters(self):
        return max((r['k'] for r in self.rows), default=-1)

    @property
    def final_rhs(self):
        return self.rows[-1]['rhs'] if self.rows else float('nan')


def _floats(s):
    out = []
    for tok in re.findall(FLOAT, s):
        try:
            out.append(float(tok))
        except ValueError:
            pass
    return out


def parse(path, keep_raw=60):
    atts, cur, cols = [], None, None
    reason_pending = 0
    with open(path, errors='replace') as fh:
        for line in fh:
            m = RE_STEP.search(line)
            if m:
                cur = Attempt(len(atts), float(m.group(1)), float(m.group(2)))
                cur.cols = cols
                atts.append(cur)
                cur.raw.append(line.rstrip('\n'))
                reason_pending = 0
                continue
            if cur is None:
                continue
            if len(cur.raw) < keep_raw:
                cur.raw.append(line.rstrip('\n'))
            if 'Rhs' in line and '|' in line:
                cols = [c.strip().lower() for c in line.split('|')]
                cur.cols = cols
                continue
            if reason_pending and line.strip():
                reason_pending -= 1
                if not (RE_TOTAL.search(line) or RE_WALL.search(line) or RE_ROW.match(line)):
                    cur.reason = (cur.reason + ' ' + line.strip()).strip()
                    continue
            if RE_FINISHED.search(line):
                cur.reason = line.strip()
                reason_pending = 2
                continue
            mr = RE_ROW.match(line)
            if mr and not RE_TOTAL.search(line):
                k = int(mr.group(1))
                rhs = err = tcol = None
                if '|' in line and cur.cols:
                    cells = [c.strip() for c in line.split('|')]
                    for name, cell in zip(cur.cols, cells):
                        v = _floats(cell)
                        if not v:
                            continue
                        if name == 'rhs':
                            rhs = v[0]
                        elif name.startswith('error'):
                            err = v[0]
                        elif name.startswith('time'):
                            tcol = v[0]
                    if rhs is None:
                        v = _floats(cells[1]) if len(cells) > 1 else []
                        rhs = v[0] if v else None
                else:
                    v = _floats(line)
                    rhs = v[1] if len(v) > 1 else None
                    tcol = v[-1] if len(v) > 2 else None
                if rhs is None:
                    continue
                if cur.rows and k <= cur.rows[-1]['k']:
                    continue
                cur.rows.append({'k': k, 'rhs': rhs, 'error': err, 'time': tcol})
                continue
            mt = RE_TOTAL.search(line)
            if mt:
                cur.tot = float(mt.group(1))
            mw = RE_WALL.search(line)
            if mw:
                cur.wall = float(mw.group(1))
    _classify(atts)
    mode = _assign_time(atts)
    return atts, mode


def _same(a, b):
    return abs(a - b) <= 1e-12 + 1e-9 * max(abs(a), abs(b))


def _classify(atts):
    for i, a in enumerate(atts):
        if i + 1 == len(atts):
            a.status = 'last'
            continue
        nxt = atts[i + 1]
        if _same(nxt.t0, a.t0):
            a.status = 'rejected'
        elif _same(nxt.t0, a.t1):
            a.status = 'accepted'
        else:
            a.status = 'unknown'


def _assign_time(atts):
    for key in ('tot', 'wall'):
        vals = [getattr(a, key) for a in atts]
        have = [v for v in vals if v is not None]
        if len(have) < max(3, 0.5 * len(atts)):
            continue
        nondec = sum(1 for x, y in zip(have, have[1:]) if y >= x)
        cumulative = len(have) > 3 and nondec >= 0.95 * (len(have) - 1) and have[-1] > 20 * have[0] + 1
        prev = None
        for a in atts:
            v = getattr(a, key)
            if v is None:
                continue
            if cumulative:
                a.time_s = v - prev if prev is not None else v
                prev = v
            else:
                a.time_s = v
        return f'"{key}" lines, {"cumulative -> differenced" if cumulative else "per-attempt"}'
    tv = [a.rows[-1]['time'] if a.rows and a.rows[-1]['time'] is not None else None for a in atts]
    if sum(v is not None for v in tv) >= 0.5 * max(1, len(atts)):
        for a, v in zip(atts, tv):
            a.time_s = v
        return 'Newton-table time column (last row) -- VERIFY: may be cumulative or CPU time'
    return 'no wallclock found'


def vol(a, vs):
    return vs * a.t0


def fmt(x, p=3):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return '-'
    return f'{x:.{p}g}'


def report(atts, mode, args, label='REF'):
    vs = args.vscale
    acc = [a for a in atts if a.status == 'accepted']
    rej = [a for a in atts if a.status == 'rejected']
    print(f'\n=== {label}: {args.ref if label == "REF" else args.cand}')
    print(f'attempts={len(atts)} accepted={len(acc)} rejected={len(rej)} '
          f'unknown={sum(a.status == "unknown" for a in atts)}  time source: {mode}')
    if not atts:
        print('NO supported step-start lines found -- check the file / send a raw excerpt.')
        return
    last = atts[-1]
    print(f'last attempt: t0={last.t0:.8g} (V~{vol(last, vs):.5f}) dt={last.dt:.3g} iters={last.iters} '
          f'status={last.status}')
    tt = [a.time_s for a in atts if a.time_s is not None]
    if tt:
        print(f'sum wallclock over attempts = {sum(tt):.0f} s ({sum(tt)/3600:.1f} h); '
              f'accepted {sum(a.time_s or 0 for a in acc):.0f} s, rejected {sum(a.time_s or 0 for a in rej):.0f} s')

    print('\n-- per 0.25 V bin (V = vscale * t0) --')
    print(f'{"V bin":>11} {"acc":>5} {"rej":>4} {"accIt med/max":>13} {"rejIt mean":>10} '
          f'{"t_acc[s]":>9} {"t_rej[s]":>9} {"min dt":>9}')
    bins = {}
    for a in atts:
        b = math.floor(vol(a, vs) / 0.25) * 0.25
        bins.setdefault(b, []).append(a)
    for b in sorted(bins):
        L = bins[b]
        A = [a for a in L if a.status == 'accepted']
        R = [a for a in L if a.status == 'rejected']
        ai = [a.iters for a in A]
        print(f'{b:5.2f}-{b+0.25:4.2f} {len(A):5d} {len(R):4d} '
              f'{(str(int(statistics.median(ai)))+"/"+str(max(ai))) if ai else "-":>13} '
              f'{fmt(statistics.mean([a.iters for a in R])) if R else "-":>10} '
              f'{sum(a.time_s or 0 for a in A):9.0f} {sum(a.time_s or 0 for a in R):9.0f} '
              f'{min(a.dt for a in L):9.2e}')

    print('\n-- accepted-step Newton iteration histogram --')
    h = {}
    for a in acc:
        h[a.iters] = h.get(a.iters, 0) + 1
    for k in sorted(h):
        print(f'  {k:3d} iters : {h[k]}')

    print('\n-- rejected attempts (stall diagnostics) --')
    print(f'{"#":>6} {"V":>9} {"dt":>9} {"iters":>5} {"rhs_min(last10)":>15} {"rhs_med(last10)":>15} '
          f'{"err<1?":>6} {"time[s]":>8}  reason')
    for a in rej[-args.maxlist:]:
        tail = [r['rhs'] for r in a.rows[-10:]] or [float('nan')]
        errs = [r['error'] for r in a.rows if r['error'] is not None]
        e1 = ('yes' if any(e < 1 for e in errs) else 'no') if errs else '-'
        print(f'{a.idx:6d} {vol(a, vs):9.5f} {a.dt:9.2e} {a.iters:5d} {min(tail):15.4e} '
              f'{statistics.median(tail):15.4e} {e1:>6} {fmt(a.time_s, 5):>8}  {a.reason[:70]}')
    if len(rej) > args.maxlist:
        print(f'  ... ({len(rej) - args.maxlist} earlier rejected attempts not listed)')

    print('\n-- predicted effect of an inner-Coupled "Iterations = N" cap --')
    print('  (false_rej = accepted x8 steps that needed > N iterations; these would be')
    print('   rejected + cut back under the cap.  first_div = first attempt where the cap')
    print('   changes the trajectory, i.e. where the FAST log may start to differ.)')
    print(f'{"N":>4} {"false_rej":>9} {"first_div V":>11} {"rej>N":>6} {"saved iters":>11} {"saved time[s]":>13}')
    for N in args.caps:
        fr = [a for a in acc if a.iters > N]
        rr = [a for a in rej if a.iters > N]
        first = next((a for a in atts if a.iters > N), None)
        si = sum(a.iters - N for a in rr)
        st = sum((a.time_s or 0) * (a.iters - N) / max(a.iters, 1) for a in rr)
        print(f'{N:4d} {len(fr):9d} {fmt(vol(first, vs), 6) if first else "none":>11} {len(rr):6d} '
              f'{si:11d} {st:13.0f}')
    print('  NOTE: saved time ignores extra cutback/recovery steps that false rejections add,')
    print('        and assumes time per Newton iteration is uniform within an attempt.')

    print('\n-- cutback recovery after each rejection --')
    rec = []
    for i, a in enumerate(atts):
        if a.status != 'rejected':
            continue
        target = a.dt
        n = 0
        for b in atts[i + 1:]:
            if b.status == 'accepted':
                n += 1
                if b.dt >= 0.999 * target:
                    break
        rec.append(n)
    if rec:
        print(f'  accepted steps needed to regain the pre-rejection dt: median {statistics.median(rec)}, '
              f'max {max(rec)} (n={len(rec)})')

    if args.raw:
        print('\n-- RAW excerpt of first rejected and first accepted attempt (verify the parser) --')
        for a in ([x for x in rej[:args.raw]] + [x for x in acc[:args.raw]]):
            print(f'---- attempt {a.idx} status={a.status} parsed iters={a.iters} '
                  f'final_rhs={a.final_rhs:.4e} time={a.time_s}')
            for ln in a.raw:
                print('    ' + ln)


def compare(ref, cand, args):
    vs = args.vscale
    print('\n=== REF vs CAND step-sequence identity check ===')
    n = min(len(ref), len(cand))
    div = None
    for i in range(n):
        r, c = ref[i], cand[i]
        if not (_same(r.t0, c.t0) and _same(r.t1, c.t1) and r.iters == c.iters):
            div = i
            break
    if div is None:
        print(f'first {n} attempts identical in (t0, t1, Newton iterations).')
    else:
        r, c = ref[div], cand[div]
        print(f'first divergence at attempt #{div}: REF t0={r.t0:.8g} dt={r.dt:.3g} it={r.iters} ({r.status}) | '
              f'CAND t0={c.t0:.8g} dt={c.dt:.3g} it={c.iters} ({c.status})  V~{vs*r.t0:.5f}')
        expected = r.iters > args.cap
        print('  -> EXPECTED (REF attempt exceeded the cap)' if expected else
              '  -> UNEXPECTED: REF attempt did not exceed the cap. Stop and investigate '
              '(input diff, mesh, threads/nondeterminism).')

    print('\n=== wallclock to reach anode voltage (accepted steps, cumulative attempt time) ===')
    def milestones(atts):
        out, cum = {}, 0.0
        marks = sorted(args.milestones)
        j = 0
        for a in atts:
            cum += a.time_s or 0.0
            if a.status == 'accepted':
                v1 = vs * a.t1
                while j < len(marks) and v1 >= marks[j]:
                    out[marks[j]] = cum
                    j += 1
        return out
    mr, mc = milestones(ref), milestones(cand)
    print(f'{"V":>6} {"REF [h]":>9} {"CAND [h]":>9} {"ratio":>7}')
    for v in sorted(args.milestones):
        a, b = mr.get(v), mc.get(v)
        print(f'{v:6.3f} {fmt(a/3600 if a else None, 4):>9} {fmt(b/3600 if b else None, 4):>9} '
              f'{fmt(a/b if a and b else None, 3):>7}')

    lo, hi = args.window
    print(f'\n=== bottleneck window {lo:.3f}-{hi:.3f} V ===')
    for name, atts in (('REF', ref), ('CAND', cand)):
        W = [a for a in atts if lo <= vs * a.t0 < hi]
        if not W:
            print(f'{name}: no attempts in window'); continue
        A = [a for a in W if a.status == 'accepted']
        R = [a for a in W if a.status == 'rejected']
        vmax = max(vs * a.t1 for a in A) if A else float('nan')
        t = sum(a.time_s or 0 for a in W)
        it = sum(max(a.iters, 0) for a in W)
        span = (vmax - lo) if A else 0
        print(f'{name}: acc={len(A)} rej={len(R)} newton_iters={it} wallclock={t:.0f} s '
              f'reached V={fmt(vmax, 6)}  ->  {fmt(span*1000/(t/3600) if t else None, 4)} mV/h')


def write_csv(atts, path, vs):
    with open(path, 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['idx', 't0', 't1', 'dt', 'V0', 'V1', 'iters', 'final_rhs', 'status', 'time_s', 'reason'])
        for a in atts:
            w.writerow([a.idx, a.t0, a.t1, a.dt, vs * a.t0, vs * a.t1, a.iters, a.final_rhs,
                        a.status, a.time_s, a.reason])


SYNTH = """SYNTHETIC TEST LOG -- NOT SENTAURUS OUTPUT -- parser self-test only
Computing step from t=0.0000E+00 to t=1.0000E-05 (stepsize 1.0000E-05) :
           | Rhs       | factor    | |step|    | error     | #inner | #iterative | time      |
     0     | 1.20E+01  |           |           |           |        |            |   1.00    |
     1     | 3.00E-01  | 1.00E+00  | 2.00E-02  | 2.00E+01  |   1    |    30      |  20.00    |
     2     | 5.00E-04  | 1.00E+00  | 1.00E-04  | 1.00E-01  |   1    |    30      |  40.00    |
 Finished, because...
    |Rhs| < 1.0000E-03
 Total: 40.00 s
Computing step from t=1.0000E-05 to t=2.2000E-05 (stepsize 1.2000E-05) :
           | Rhs       | factor    | |step|    | error     | #inner | #iterative | time      |
     0     | 1.20E+01  |           |           |           |        |            |   1.00    |
""" + ''.join(f"    {k:2d}     | 1.4{k%3}E-03  | 1.00E+00  | 1.00E-06  | 3.00E+00  |   1    |    30      |  {20*k:.2f}    |\n" for k in range(1, 51)) + """ Finished, because...
    Max. number of iterations reached
 Total: 1000.00 s
Computing step from t=1.0000E-05 to t=1.6000E-05 (stepsize 6.0000E-06) :
           | Rhs       | factor    | |step|    | error     | #inner | #iterative | time      |
     0     | 2.00E-03  |           |           |           |        |            |   1.00    |
     1     | 8.00E-04  | 1.00E+00  | 1.00E-06  | 5.00E-01  |   1    |    30      |  20.00    |
 Finished, because...
    |Rhs| < 1.0000E-03
 Total: 20.00 s
Computing step from t=1.6000E-05 to t=2.3200E-05 (stepsize 7.2000E-06) :
"""


def selftest():
    import os
    import tempfile
    # Regression test for the actual Copy x8 T-2022.03 log syntax.
    probe = "Computing BE-step from 0.928243 s to 0.928266 s (Stepsize: 2.2968e-05 s)"
    m = RE_STEP.search(probe)
    assert m is not None, "RE_STEP does not match real T-2022.03 BE-step syntax"
    assert abs(float(m.group(1)) - 0.928243) < 1e-12
    assert abs(float(m.group(2)) - 0.928266) < 1e-12
    assert abs(float(m.group(3)) - 2.2968e-05) < 1e-12
    fd, p = tempfile.mkstemp(suffix='.out')
    with os.fdopen(fd, 'w') as fh:
        fh.write(SYNTH)
    atts, mode = parse(p)
    os.unlink(p)
    assert [a.status for a in atts] == ['accepted', 'rejected', 'accepted', 'last'], [a.status for a in atts]
    assert [a.iters for a in atts[:3]] == [2, 50, 1], [a.iters for a in atts]
    assert abs(atts[1].final_rhs - 1.42e-3) < 1e-9 or abs(atts[1].final_rhs - 1.40e-3) < 1e-9 \
        or abs(atts[1].final_rhs - 1.41e-3) < 1e-9
    assert atts[1].time_s == 1000.0, (atts[1].time_s, mode)
    print('selftest OK (synthetic format only; real SDevice format must be checked with --raw).', mode)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('ref', nargs='?')
    ap.add_argument('--cand')
    ap.add_argument('--vscale', type=float, default=5.0, help='V_anode = vscale * t (default 5.0 for 0->5 V)')
    ap.add_argument('--caps', type=lambda s: [int(x) for x in s.split(',')], default=[8, 10, 12, 15, 20, 25, 30])
    ap.add_argument('--cap', type=int, default=15, help='cap used by the candidate (for divergence check)')
    ap.add_argument('--window', type=float, nargs=2, default=[4.55, 4.75])
    ap.add_argument('--milestones', type=float, nargs='+',
                    default=[1.0, 2.0, 2.5, 3.0, 3.5, 4.0, 4.2, 4.4, 4.5, 4.6, 4.65, 4.7, 4.8, 4.9, 5.0])
    ap.add_argument('--csv')
    ap.add_argument('--raw', type=int, default=0, help='print raw text of first N rejected/accepted attempts')
    ap.add_argument('--maxlist', type=int, default=40)
    ap.add_argument('--selftest', action='store_true')
    args = ap.parse_args()
    if args.selftest:
        selftest(); return
    if not args.ref:
        ap.error('REF log required')
    ref, mode = parse(args.ref)
    report(ref, mode, args, 'REF')
    if args.csv:
        write_csv(ref, args.csv, args.vscale)
        print(f'\nCSV written: {args.csv}')
    if args.cand:
        cand, cmode = parse(args.cand)
        report(cand, cmode, args, 'CAND')
        compare(ref, cand, args)


if __name__ == '__main__':
    main()
