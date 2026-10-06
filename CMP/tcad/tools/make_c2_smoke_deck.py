#!/usr/bin/env python3
"""
make_c2_smoke_deck.py -- generate a short FAST_C2 smoke deck from an already-
preprocessed C1 ppN_des.cmd without publishing the proprietary full source.

Status: PROPOSED.  Purpose: syntax/mechanics smoke only, NOT research output.

Smoke path on the same global V=5*t axis:
  segment 1: t 0.00 -> 0.04, 0.0 -> 0.2 V, Increment=1.2, Iterations=15
  Save checkpoint at 0.2 V
  segment 2: t 0.04 -> 0.06, 0.2 -> 0.3 V, Increment=1.05, Iterations=15

Unchanged from the input pp deck: Grid, Parameters, Electrode names, Physics,
Plot variables, Math, and all physical parameters.  File outputs and Solve are
replaced so the smoke run cannot overwrite the reference run.
"""
import argparse
import re
import sys


def find_block(text, keyword):
    m = re.search(r'(^|\n)\s*' + re.escape(keyword) + r'\s*\{', text)
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
    sys.exit(f'unbalanced braces in {keyword} block')


def replace_file_block(text, tag):
    s, e = find_block(text, 'File')
    blk = text[s:e]
    def get(key):
        m = re.search(re.escape(key) + r'\s*=\s*"([^"]+)"', blk)
        if not m:
            sys.exit(f'File block has no {key}')
        return m.group(1)
    grid = get('Grid')
    par = get('Parameters')
    new = f'''File {{
  Grid       = "{grid}"
  Parameters = "{par}"
  Plot       = "{tag}_des.tdr"
  Current    = "{tag}_des.plt"
  Output     = "{tag}_des.log"
}}'''
    return text[:s] + new + text[e:]


def smoke_solve(tag):
    return f'''Solve {{

  Coupled(
    Iterations = 500
    LineSearchDamping = 1e-2
  ) {{
    Poisson
  }}

  Coupled(
    Iterations = 100
  ) {{
    Poisson
    Electron
    Hole
  }}

  # Smoke segment 1: same global axis V=5*t, 0.0 -> 0.2 V
  Transient(
    InitialTime = 0.0
    FinalTime   = 0.04
    InitialStep = 1e-5
    MinStep = 1e-9
    MaxStep = 1e-3
    Increment = 1.2
    Goal {{
      Name = "anode"
      Voltage = 0.2
    }}
  ) {{
    Coupled ( Iterations = 15 ) {{
      Poisson
      Electron
      Hole
    }}
    Plot(
      -Loadable
      FilePrefix = "{tag}_s1"
      NoOverWrite
      Time = ( 0.04 )
    )
  }}

  # Prospective restart checkpoint; Save syntax is intentionally being tested.
  Save (
    FilePrefix = "{tag}_ckpt_0p2V"
  )

  # Smoke segment 2: 0.2 -> 0.3 V; D2-approved common cap remains 15.
  Transient(
    InitialTime = 0.04
    FinalTime   = 0.06
    InitialStep = 1e-4
    MinStep = 1e-9
    MaxStep = 1e-3
    Increment = 1.05
    Goal {{
      Name = "anode"
      Voltage = 0.3
    }}
  ) {{
    Coupled ( Iterations = 15 ) {{
      Poisson
      Electron
      Hole
    }}
    Plot(
      -Loadable
      FilePrefix = "{tag}_s2"
      NoOverWrite
      Time = ( 0.05; 0.06 )
    )
  }}
}}
'''


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--pp', required=True, help='preprocessed C1 deck, e.g. pp6_des.cmd')
    ap.add_argument('--tag', default='c2smk', help='new output prefix')
    ap.add_argument('--out', required=True, help='output smoke .cmd')
    a = ap.parse_args()

    text = open(a.pp, errors='replace').read()
    text = replace_file_block(text, a.tag)
    s, e = find_block(text, 'Solve')
    text = text[:s] + smoke_solve(a.tag) + text[e:]
    hdr = ('# FAST_C2 SMOKE deck generated from ' + a.pp + '\n'
           '# PROPOSED / syntax-mechanics test only / not research output\n'
           '# D2 policy: Iterations=15 in both transient segments; segment2 Increment=1.05\n')
    open(a.out, 'w').write(hdr + text)
    print(f'written {a.out}')


if __name__ == '__main__':
    main()
