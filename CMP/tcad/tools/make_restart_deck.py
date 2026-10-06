#!/usr/bin/env python3
"""
make_restart_deck.py  --  build a standalone SDevice restart deck from an
already-preprocessed ppN_des.cmd (CMP FAST baseline).   Status: PROPOSED.
Author: Claude for worker Lee Taek Gyu, 2026-10-06.

It copies Physics / trap blocks / Plot variables / Math VERBATIM from the
preprocessed deck and replaces only:
  * File { Plot / Current / Output }  -> new names (never overwrites the source run)
  * Electrode { anode Voltage }        -> the bias of the loaded state
  * Solve { ... }                      -> Load + steady re-solve [+ optional continuation]

Modes
  --mode check     Load the state, then one steady Coupled solve at that bias.
                   Use it to test whether a file is loadable at all and whether the
                   steady (DC) solution reproduces the reference current there.
  --mode continue  check + continue the 5 V/s ramp on the SAME global time axis with the
                   C2 high-bias step policy (Increment 1.05, Iterations 8), with
                   intermediate snapshots at the C1/x8 times and Save checkpoints.

The output deck uses literal file names (no Workbench macros) so it can be run
from a scratch directory:   sdevice --max_threads 4 <out>.cmd

Example (tcsh-safe, one line each):
  python3 make_restart_deck.py --pp pp6_des.cmd --load n6_inter_0004 --volt 4.7 --mode check --tag ld47 --out ld47_des.cmd
  python3 make_restart_deck.py --pp pp6_des.cmd --load n6_inter_0004 --volt 4.7 --t0 0.94 --mode continue --tag rs47 --out rs47_des.cmd

NOTE: "Load ( FilePrefix = ... )" / "Save ( FilePrefix = ... )" syntax and whether a
Plot(-Loadable) TDR can be loaded are NOT confirmed against the T-2022.03 manual.
The first run of a generated deck is itself the test.
"""
import argparse
import re
import sys


def find_block(text, keyword):
    """return (start, end) of 'keyword { ... }' at top level (brace matched)."""
    m = re.search(r'(^|\n)\s*' + keyword + r'\s*\{', text)
    if not m:
        sys.exit(f'block "{keyword} {{" not found')
    start = m.start() if m.group(1) == '' else m.start() + 1
    i = text.index('{', m.start())
    depth = 0
    for j in range(i, len(text)):
        if text[j] == '{':
            depth += 1
        elif text[j] == '}':
            depth -= 1
            if depth == 0:
                return start, j + 1
    sys.exit(f'unbalanced braces in "{keyword}" block')


def file_block(text, tag):
    s, e = find_block(text, 'File')
    blk = text[s:e]
    def keep(key):
        m = re.search(key + r'\s*=\s*"([^"]+)"', blk)
        if not m:
            sys.exit(f'File block has no {key}')
        return m.group(1)
    grid, par = keep('Grid'), keep('Parameters')
    new = (f'File {{\n  Grid       = "{grid}"\n  Parameters = "{par}"\n'
           f'  Plot       = "{tag}_des.tdr"\n  Current    = "{tag}_des.plt"\n'
           f'  Output     = "{tag}_des.log"\n}}')
    return text[:s] + new + text[e:]


def electrode_block(text, volt):
    s, e = find_block(text, 'Electrode')
    blk = text[s:e]
    m = re.search(r'(Name\s*=\s*"anode"[^}]*?Voltage\s*=\s*)([-+0-9.eE]+)', blk, re.S)
    if not m:
        sys.exit('anode Voltage not found in Electrode block')
    blk = blk[:m.start(2)] + repr(float(volt)) + blk[m.end(2):]
    return text[:s] + blk + text[e:]


COUPLED = '{\n      Poisson\n      Electron\n      Hole\n    }'

# C1/x8 snapshot times on the global axis (V = 5 t)
SNAP = [0.80, 0.84, 0.88, 0.92, 0.94, 0.96, 0.97, 0.98, 0.985, 0.99, 0.995]
# C2 segment ends and InitialStep per segment (same as FAST_C2 deck)
SEG = [(0.88, 1e-4), (0.92, 5e-5), (0.96, 2e-5), (1.00, 1e-5)]


def solve_block(load, mode, t0, tag, iters, inc):
    s = ['Solve {', '',
         f'  Load ( FilePrefix = "{load}" )', '',
         '  # steady re-solve at the loaded bias (no time derivative): the anode current',
         '  # printed here must match the reference run at the same bias',
         f'  Coupled ( Iterations = 15 ) {COUPLED}', '']
    if mode == 'continue':
        if t0 is None:
            sys.exit('--t0 is required for --mode continue')
        ends = [(t, st) for (t, st) in SEG if t > t0 + 1e-12]
        start = t0
        for k, (t1, st) in enumerate(ends):
            snaps = [x for x in SNAP if start < x <= t1 + 1e-12]
            s += ['  Transient(',
                  f'    InitialTime = {start}', f'    FinalTime   = {t1}',
                  f'    InitialStep = {st}', '    MinStep = 1e-9', '    MaxStep = 1e-3',
                  f'    Increment = {inc}',
                  f'    Goal {{ Name = "anode" Voltage = {round(5.0 * t1, 6)} }}',
                  '  ) {',
                  f'    Coupled ( Iterations = {iters} ) {COUPLED}']
            if snaps:
                s += ['    Plot ( -Loadable FilePrefix = "%s_inter_s%d" NoOverWrite' % (tag, k + 1),
                      '           Time = ( ' + '; '.join(str(x) for x in snaps) + ' ) )']
            s += ['  }']
            if t1 < 1.0 - 1e-12:
                s += [f'  Save ( FilePrefix = "{tag}_ckpt_{str(round(5.0 * t1, 3)).replace(".", "p")}V" )']
            s += ['']
            start = t1
    s += ['}', '']
    return '\n'.join(s)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pp', required=True, help='preprocessed source deck, e.g. pp6_des.cmd')
    ap.add_argument('--load', required=True, help='FilePrefix of the state to load')
    ap.add_argument('--volt', required=True, type=float, help='anode bias of the loaded state [V]')
    ap.add_argument('--t0', type=float, help='global pseudo-time of the loaded state (V = 5 t)')
    ap.add_argument('--mode', choices=['check', 'continue'], default='check')
    ap.add_argument('--tag', required=True, help='prefix for all new output files')
    ap.add_argument('--iters', type=int, default=8)
    ap.add_argument('--inc', type=float, default=1.05)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    if a.t0 is not None and abs(5.0 * a.t0 - a.volt) > 1e-6:
        sys.exit(f'--volt {a.volt} inconsistent with --t0 {a.t0} on the V = 5 t axis')
    text = open(a.pp).read()
    text = file_block(text, a.tag)
    text = electrode_block(text, a.volt)
    s, _ = find_block(text, 'Solve')
    text = text[:s] + solve_block(a.load, a.mode, a.t0, a.tag, a.iters, a.inc)
    hdr = (f'# RESTART DECK (PROPOSED) generated by make_restart_deck.py from {a.pp}\n'
           f'# load={a.load} anode={a.volt} V mode={a.mode} t0={a.t0} iters={a.iters} inc={a.inc}\n')
    open(a.out, 'w').write(hdr + text)
    print(f'written {a.out}')


if __name__ == '__main__':
    main()
