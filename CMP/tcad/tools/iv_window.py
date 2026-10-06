#!/usr/bin/env python3
"""
iv_window.py  --  current-density window of the running baseline (CMP).  Status: PROPOSED.
Author: Claude for worker Lee Taek Gyu, 2026-10-06.   Read-only; copy live files first.

Prints anode V, I and J at chosen voltages from one or two DF-ISE .plt files
(e.g. Node 6 NtSide=0 and Node 12 NtSide=1e18), and, for two files, the
same-current voltage shift and same-voltage current ratio.

  J [A/cm^2] = I [A per um depth] / (W_mesa[um] * 1 um * 1e-8 cm^2/um^2)
  default W_mesa = 4 um (Common Baseline representative mesa).  ASSUMPTION:
  2D SDevice current is per 1 um depth (AreaFactor not set) and the relevant area
  is the mesa width; check both before quoting J in the abstract.

Usage (tcsh-safe):
  python3 iv_window.py n6_copy.plt
  python3 iv_window.py n6_copy.plt n12_copy.plt --v 3.0 3.5 4.0 4.2 4.4 4.6 4.7
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
        sys.exit(f'{path}: no datasets block')
    names = re.findall(r'"([^"]*)"', m.group(1))
    d = re.search(r'\bData\s*\{(.*)', txt, re.S)          # tolerate a file still being written
    if not d:
        sys.exit(f'{path}: no Data block')
    body = d.group(1).split('}')[0]
    vals = [float(x) for x in re.findall(FLOAT, body)]
    n = len(names); rows = len(vals) // n
    cols = {nm: vals[i::n][:rows] for i, nm in enumerate(names)}
    v = next((c for c in names if re.fullmatch(r'anode\s+OuterVoltage', c, re.I)), None) \
        or next((c for c in names if re.search(r'anode.*Voltage', c, re.I)), None)
    i = next((c for c in names if re.fullmatch(r'anode\s+TotalCurrent', c, re.I)), None)
    if not v or not i:
        sys.exit(f'{path}: anode voltage/current columns not found: {names}')
    pv, pi = [], []
    for a, b in zip(cols[v], cols[i]):
        if not pv or a > pv[-1]:
            pv.append(a); pi.append(b)
    return pv, pi


def at(xs, ys, x):
    j = bisect.bisect_left(xs, x)
    if j <= 0 or j >= len(xs):
        return None
    f = (x - xs[j - 1]) / (xs[j] - xs[j - 1])
    y0, y1 = ys[j - 1], ys[j]
    if y0 and y1 and (y0 > 0) == (y1 > 0):
        return math.copysign(math.exp(math.log(abs(y0)) + f * (math.log(abs(y1)) - math.log(abs(y0)))), y0)
    return y0 + f * (y1 - y0)


def v_at(xs, ys, target):
    t = abs(target)
    for k in range(1, len(xs)):
        a, b = abs(ys[k - 1]), abs(ys[k])
        if a < t <= b and a > 0:
            return xs[k - 1] + (math.log(t) - math.log(a)) / (math.log(b) - math.log(a)) * (xs[k] - xs[k - 1])
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('plt', nargs='+')
    ap.add_argument('--v', type=float, nargs='+', default=[2.5, 3.0, 3.5, 4.0, 4.2, 4.4, 4.6, 4.7])
    ap.add_argument('--wmesa', type=float, default=4.0, help='mesa width in um')
    ap.add_argument('--j', type=float, nargs='+', default=[0.1, 1, 10, 100, 1000],
                    help='current densities [A/cm2] for the V-at-J table')
    a = ap.parse_args()
    k = 1.0 / (a.wmesa * 1e-8)
    data = [read_plt(p) for p in a.plt[:2]]
    for p, (v, i) in zip(a.plt, data):
        print(f'{p}: {len(v)} points, V {v[0]:.4f} .. {v[-1]:.4f} V, I_max {max(abs(x) for x in i):.4e}')
    print('\nV [V] ' + ''.join(f'| {p[:22]:>22} I [A/um]   J [A/cm2] ' for p in a.plt[:2]))
    for x in a.v:
        row = f'{x:5.3f} '
        for v, i in data:
            y = at(v, i, x)
            row += f'| {y:>22.4e} {abs(y)*k:>10.3e} ' if y is not None else '|  (beyond range)                   '
        if len(data) == 2:
            y0, y1 = at(*data[0], x), at(*data[1], x)
            if y0 and y1:
                row += f'| I2/I1 = {y1/y0:.4f}'
        print(row)
    print('\nJ [A/cm2] -> V at that current density')
    for jj in a.j:
        row = f'{jj:9.3g} '
        vs = []
        for v, i in data:
            vv = v_at(v, i, jj / k)
            vs.append(vv)
            row += f'| V = {vv:.4f} ' if vv is not None else '| not reached '
        if len(vs) == 2 and None not in vs:
            row += f'| dV (file2 - file1) = {1e3*(vs[1]-vs[0]):+.2f} mV'
        print(row)


if __name__ == '__main__':
    main()
