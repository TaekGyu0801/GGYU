#!/usr/bin/env python3
"""
plt_compare.py  --  CMP FAST_BASELINE I-V equivalence check (reference vs candidate)

Status : PROPOSED tool (tested on a synthetic DF-ISE xyplot file only).
Author : Claude for worker Lee Taek Gyu, 2026-10-04

Reads two Sentaurus Device current files (the File{ Current = ... } output,
DF-ISE text "xyplot", e.g. n6_des.plt) and compares the anode I-V on the
overlapping voltage range:

  1. same-voltage relative current difference  |Ic - Ir| / |Ir|
  2. same-current voltage shift (Delta Vf) at the reference current
     reached at chosen voltages (default 3.0 3.5 4.0 4.2 4.4 4.5 4.6 V)

Read-only.  Copy the live file first.

Usage
  python3 plt_compare.py --list REF.plt
  python3 plt_compare.py REF.plt CAND.plt
  python3 plt_compare.py REF.plt CAND.plt --vcol "anode OuterVoltage" \
                         --icol "anode TotalCurrent" --floor 1e-14
  python3 plt_compare.py --selftest
"""
import argparse
import bisect
import math
import re
import sys

FLOAT = r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?'


def read_plt(path):
    txt = open(path, errors='replace').read()
    m = re.search(r'datasets\s*=\s*\[(.*?)\]', txt, re.S)
    if not m:
        sys.exit(f'{path}: no "datasets = [ ... ]" block found (not a DF-ISE xyplot?)')
    names = re.findall(r'"([^"]*)"', m.group(1))
    d = re.search(r'\bData\s*\{(.*?)\}', txt, re.S)
    if not d:
        sys.exit(f'{path}: no "Data {{ ... }}" block found')
    vals = [float(x) for x in re.findall(FLOAT, d.group(1))]
    n = len(names)
    if n == 0 or len(vals) % n:
        print(f'WARNING {path}: {len(vals)} numbers not a multiple of {n} datasets; '
              f'truncating to the last complete row (file may still be being written)')
    rows = len(vals) // n
    cols = {name: vals[i::n][:rows] for i, name in enumerate(names)}
    return names, cols


def pick(names, want, patterns):
    if want:
        if want not in names:
            sys.exit(f'column "{want}" not found. Available: {names}')
        return want
    for p in patterns:
        for nm in names:
            if re.fullmatch(p, nm, re.I):
                return nm
    sys.exit(f'could not auto-detect a column for {patterns}; use --vcol/--icol. Available: {names}')


def monotone(v, i):
    """keep the accepted, strictly increasing-voltage part (transient ramp)."""
    pv, pi = [], []
    for a, b in zip(v, i):
        if not pv or a > pv[-1]:
            pv.append(a); pi.append(b)
    return pv, pi


def interp(xs, ys, x):
    j = bisect.bisect_left(xs, x)
    if j <= 0:
        return ys[0] if xs and x == xs[0] else None
    if j >= len(xs):
        return None
    x0, x1, y0, y1 = xs[j - 1], xs[j], ys[j - 1], ys[j]
    f = (x - x0) / (x1 - x0)
    if y0 != 0 and y1 != 0 and (y0 > 0) == (y1 > 0):
        s = 1.0 if y0 > 0 else -1.0
        return s * math.exp(math.log(abs(y0)) + f * (math.log(abs(y1)) - math.log(abs(y0))))
    return y0 + (y1 - y0) * f


def v_at_current(v, i, target):
    """first voltage where |I| reaches |target| (log-linear interpolation)."""
    t = abs(target)
    for k in range(1, len(v)):
        a, b = abs(i[k - 1]), abs(i[k])
        if a < t <= b and a > 0:
            f = (math.log(t) - math.log(a)) / (math.log(b) - math.log(a))
            return v[k - 1] + f * (v[k] - v[k - 1])
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('ref', nargs='?')
    ap.add_argument('cand', nargs='?')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--vcol')
    ap.add_argument('--icol')
    ap.add_argument('--floor', type=float, default=0.0,
                    help='ignore points with |I_ref| below this (noise floor), same units as the file')
    ap.add_argument('--vf', type=float, nargs='+', default=[3.0, 3.5, 4.0, 4.2, 4.4, 4.5, 4.6])
    ap.add_argument('--tol-rel', type=float, default=1e-3, help='acceptance: max same-V relative diff')
    ap.add_argument('--tol-dvf', type=float, default=1e-3, help='acceptance: max |Delta Vf| in V')
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.ref:
        ap.error('REF required')
    names, R = read_plt(a.ref)
    if a.list or not a.cand:
        print('\n'.join(names)); return
    names_c, C = read_plt(a.cand)
    vpat = [r'anode\s+OuterVoltage', r'anode\s+InnerVoltage', r'anode.*Voltage']
    ipat = [r'anode\s+TotalCurrent', r'anode.*TotalCurrent']
    vc = pick(names, a.vcol, vpat); ic = pick(names, a.icol, ipat)
    vc2 = pick(names_c, vc if vc in names_c else None, vpat); ic2 = pick(names_c, ic if ic in names_c else None, ipat)
    rv, ri = monotone(R[vc], R[ic]); cv, ci = monotone(C[vc2], C[ic2])
    print(f'REF : {len(rv)} pts, V {rv[0]:.4f}..{rv[-1]:.4f}  [{vc} / {ic}]')
    print(f'CAND: {len(cv)} pts, V {cv[0]:.4f}..{cv[-1]:.4f}  [{vc2} / {ic2}]')
    vmax = min(rv[-1], cv[-1])
    print(f'overlap up to {vmax:.4f} V\n')

    worst, wv, bins = 0.0, None, {}
    for v, i in zip(rv, ri):
        if v > vmax or abs(i) <= a.floor or i == 0:
            continue
        c = interp(cv, ci, v)
        if c is None:
            continue
        rel = abs(c - i) / abs(i)
        b = math.floor(v / 0.5) * 0.5
        bins[b] = max(bins.get(b, 0.0), rel)
        if rel > worst:
            worst, wv = rel, v
    print('same-voltage max relative current difference per 0.5 V bin')
    for b in sorted(bins):
        print(f'  {b:4.1f}-{b+0.5:3.1f} V : {bins[b]:.3e}')
    print(f'  WORST {worst:.3e} at {wv} V   (tol {a.tol_rel:g})\n')
    print('NOTE: linear interpolation between ramp points adds error where the')
    print('      current changes fast (turn-on); judge the high-bias bins primarily.\n')

    print('same-current Delta Vf (cand - ref) at I_ref(V)')
    dmax = 0.0
    for v in a.vf:
        if v > vmax:
            print(f'  {v:.3f} V : beyond overlap'); continue
        it = interp(rv, ri, v)
        vc_ = v_at_current(cv, ci, it) if it else None
        vr_ = v_at_current(rv, ri, it) if it else None
        if vc_ is None or vr_ is None:
            print(f'  {v:.3f} V : n/a'); continue
        d = vc_ - vr_
        dmax = max(dmax, abs(d))
        print(f'  I_ref={it:.4e} : V_ref={vr_:.5f}  V_cand={vc_:.5f}  dVf={d*1e3:+.3f} mV')
    ok = worst <= a.tol_rel and dmax <= a.tol_dvf
    print(f'\nVERDICT (I-V only, overlap range): {"PASS" if ok else "FAIL"}  '
          f'(worst rel {worst:.2e} vs {a.tol_rel:g}; max |dVf| {dmax*1e3:.3f} mV vs {a.tol_dvf*1e3:g} mV)')


def selftest():
    import os, tempfile
    def mk(scale, n):
        v = [5.0 * k / n for k in range(n + 1)]
        i = [1e-20 * (math.exp(x / 0.1) - 1) * scale for x in v]
        t = [x / 5 for x in v]
        hdr = 'DF-ISE text\n\nInfo {\n  version = 1.0\n  type = xyplot\n  datasets = [\n' \
              '    "time" "anode OuterVoltage" "anode TotalCurrent"\n  ]\n}\n\nData {\n'
        body = '\n'.join(f'  {a:.10e} {b:.10e} {c:.10e}' for a, b, c in zip(t, v, i))
        fd, p = tempfile.mkstemp(suffix='.plt'); os.write(fd, (hdr + body + '\n}\n').encode()); os.close(fd)
        return p
    p1, p2 = mk(1.0, 1000), mk(1.0005, 777)
    sys.argv = ['x', p1, p2, '--floor', '1e-18']
    main()
    os.unlink(p1); os.unlink(p2)
    print('\nselftest done (synthetic ideal diode; expected dVf ~ +0.1*ln(1/1.0005) V = -0.05 mV).')


if __name__ == '__main__':
    main()
