#!/usr/bin/env python3
"""
fast_preprocess_check.py  --  CMP FAST_BASELINE C1 preprocess gate

Status : PROPOSED tool.  Author: Claude for worker Lee Taek Gyu, 2026-10-04
Read-only.  Run after Workbench "Preprocess" (and the SDE node) in the NEW
FAST project, BEFORE any SDevice solve is started.

Compares the new project against the frozen Copy x8 golden snapshot and
classifies every difference as INTENDED or UNEXPECTED.

Usage
  python3 fast_preprocess_check.py \
      --ref  ~/CMP_REFERENCE_SNAPSHOTS/Copy_x8_20261004_124024/files \
      --new  <FAST project dir> \
      --ref-node 6 --new-node <node with NtSide=0> \
      [--new-node-1e18 <node with NtSide=1e18>]

Exit code 0 = gate PASS, 1 = at least one UNEXPECTED item.
"""
import argparse
import difflib
import hashlib
import os
import re
import sys

GOLD = {
    'sd_fdiv_des.cmd(golden x8)': '56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c',
    'pp1_dvs.cmd': '5685528bc3ec338ce104040b0503be43ef032094976d69995529eb5d6fb4e658',
    'n1_msh.tdr': '762d2d57a352a00bb030b968985cbf3b71d53118c68e5c53b7586e613f392ea3',
    'pp6_des.cmd': '2dfcc98effe145ec944fb8ee5d6914f5f098e54d1bf2319c69acc76afe1692e6',
    'pp6_des.par': '60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039',
}
FAST_C1_SRC = 'f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93'

bad = 0


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def say(status, msg):
    global bad
    if status == 'UNEXPECTED':
        bad += 1
    print(f'[{status:10s}] {msg}')


def norm_node(lines, node):
    # neutralise node-specific file names so only content differences remain
    out = []
    for ln in lines:
        ln = re.sub(r'\b(pp|n)%d_' % node, r'\1NODE_', ln)
        ln = re.sub(r'"n%d_inter"' % node, '"nNODE_inter"', ln)
        out.append(ln.rstrip())
    return out


def strip_c(ln):
    return ln.split('#', 1)[0].strip()


def classify_cmd_diff(ref_lines, new_lines):
    d = list(difflib.unified_diff(ref_lines, new_lines, 'REF pp_des.cmd', 'NEW pp_des.cmd', lineterm='', n=0))
    changed = [l for l in d if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    intended, comment, unexpected = [], [], []
    for l in changed:
        body = strip_c(l[1:])
        if not body:
            comment.append(l)
        elif re.fullmatch(r'Coupled\s*(\{|\()', body) or re.fullmatch(r'Iterations\s*=\s*15', body) \
                or body in (') {', '){'):
            intended.append(l)
        else:
            unexpected.append(l)
    return d, intended, comment, unexpected


def trap_concs(lines):
    return [strip_c(l) for l in lines if re.match(r'\s*Conc\s*=', strip_c(l))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ref', required=True, help='golden snapshot "files" directory (Copy x8)')
    ap.add_argument('--new', required=True, help='new FAST project directory')
    ap.add_argument('--ref-node', type=int, default=6)
    ap.add_argument('--new-node', type=int, required=True, help='new node with NtSide=0')
    ap.add_argument('--new-node-1e18', type=int)
    ap.add_argument('--sde-node', type=int, default=1)
    a = ap.parse_args()
    R, N = os.path.expanduser(a.ref), os.path.expanduser(a.new)

    print('== 1. source revision')
    p = os.path.join(N, 'sd_fdiv_des.cmd')
    if os.path.exists(p):
        h = sha(p)
        say('OK' if h == FAST_C1_SRC else 'UNEXPECTED',
            f'sd_fdiv_des.cmd sha256 {h[:16]}... (FAST C1 expected {FAST_C1_SRC[:16]}...)')
    else:
        say('UNEXPECTED', 'sd_fdiv_des.cmd not found in new project')

    print('== 2. SDE input and mesh')
    p = os.path.join(N, 'pp%d_dvs.cmd' % a.sde_node)
    if os.path.exists(p):
        h = sha(p)
        say('OK' if h == GOLD['pp1_dvs.cmd'] else 'UNEXPECTED', f'pp{a.sde_node}_dvs.cmd sha256 {h[:16]}...')
        if h != GOLD['pp1_dvs.cmd'] and os.path.exists(os.path.join(R, 'pp1_dvs.cmd')):
            for l in difflib.unified_diff(open(os.path.join(R, 'pp1_dvs.cmd')).read().splitlines(),
                                          open(p).read().splitlines(), lineterm='', n=0):
                print('    ' + l)
    else:
        say('UNEXPECTED', f'pp{a.sde_node}_dvs.cmd missing (run Preprocess)')
    p = os.path.join(N, 'n%d_msh.tdr' % a.sde_node)
    if os.path.exists(p):
        h = sha(p)
        if h == GOLD['n1_msh.tdr']:
            say('OK', 'mesh TDR byte-identical to golden')
        else:
            say('CHECK', f'mesh TDR hash differs ({h[:16]}...). Binary TDR may differ by metadata; '
                         'require 138137 vertices / 274946 elements / 41 regions in the SDevice log '
                         '(see guide step P5) before accepting.')
    else:
        say('CHECK', f'n{a.sde_node}_msh.tdr not present yet (SDE node not run?)')

    for node, nt in ((a.new_node, '0'), (a.new_node_1e18, '1e18')):
        if node is None:
            continue
        print(f'== 3. SDevice node {node} (NtSide={nt})')
        par = os.path.join(N, 'pp%d_des.par' % node)
        if os.path.exists(par):
            h = sha(par)
            say('OK' if h == GOLD['pp6_des.par'] else 'UNEXPECTED', f'pp{node}_des.par sha256 {h[:16]}...')
        else:
            say('UNEXPECTED', f'pp{node}_des.par missing')
        cmd = os.path.join(N, 'pp%d_des.cmd' % node)
        refcmd = os.path.join(R, 'pp%d_des.cmd' % a.ref_node)
        if not os.path.exists(cmd):
            say('UNEXPECTED', f'pp{node}_des.cmd missing'); continue
        new_lines = open(cmd).read().splitlines()
        concs = trap_concs(new_lines)
        vals = sorted(set(re.sub(r'\s+', '', c) for c in concs))
        want = 'Conc=0' if nt == '0' else 'Conc=1e18'
        ok = len(concs) == 24 and len(vals) == 1 and vals[0].lower() in (want.lower(), want.lower().replace('1e18', '1e+18'))
        say('OK' if ok else 'UNEXPECTED', f'{len(concs)} trap Conc lines, values {vals} (expect 24 x {want})')
        it = [l for l in new_lines if re.fullmatch(r'Iterations\s*=\s*15', strip_c(l))]
        say('OK' if len(it) == 1 else 'UNEXPECTED', f'transient "Iterations = 15" occurrences: {len(it)} (expect 1)')
        if nt == '0' and os.path.exists(refcmd):
            # compare statement streams: comments, blank lines and indentation removed,
            # so the gate does not depend on whether Workbench keeps comments in pp files
            rl = [re.sub(r'\s+', ' ', strip_c(l)) for l in norm_node(open(refcmd).read().splitlines(), a.ref_node)]
            nl = [re.sub(r'\s+', ' ', strip_c(l)) for l in norm_node(new_lines, node)]
            rl, nl = [l for l in rl if l], [l for l in nl if l]
            d, intended, comment, unexpected = classify_cmd_diff(rl, nl)
            print(f'    statement-level diff vs golden pp{a.ref_node}_des.cmd (comments/blank/indent ignored): '
                  f'{len(intended)} intended, {len(unexpected)} unexpected changed lines')
            for l in intended:
                print('      INTENDED   ' + l)
            for l in unexpected:
                print('      UNEXPECTED ' + l)
            say('OK' if not unexpected and intended else 'UNEXPECTED', 'pp_des.cmd content gate')
        elif nt == '0':
            say('CHECK', f'golden {refcmd} not found; cannot diff')

    print('\nGATE:', 'PASS' if bad == 0 else f'FAIL ({bad} unexpected item(s)) -- do not start the solve')
    sys.exit(0 if bad == 0 else 1)


if __name__ == '__main__':
    main()
