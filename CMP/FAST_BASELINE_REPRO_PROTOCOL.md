# FAST Baseline Reproducibility Gate

Status: PROPOSED / execution pending  
Worker: Lee Taek Gyu  
Reference run: semi437 Copy x8

## Purpose

Before any runtime optimization is accepted, prove that the same baseline can be reproduced from the same source in a clean account/project.

The current public GitHub `CMP/tcad/CURRENT` directory is not the authoritative source for the active Copy x8 run. Do not overwrite the running/reference deck from that stale file.

## Immutable physics boundary

Do not change these while establishing reproducibility:

- Kou-based vertical epitaxy
- representative mesa = 4 um modeling choice
- sidewall damage width = 5 nm
- nominal defect-on Nt = 1e18 cm^-3
- Et = Ev + 0.75 eV
- sigma_n = sigma_p = 1e-15 cm^2
- common contacts / physical models used for A/B comparison

## Gate A — freeze working reference locally

On the working semi437 account, run:

```bash
bash capture_reference_snapshot.sh "<Copy x8 project directory>"
```

This creates a local snapshot directory only. Do not upload licensed Synopsys example-derived source/output files to the public repository.

Required evidence:

- original editable SDE/SDevice/SVisual source files present in the project directory
- `gtree.dat`
- `pp1_dvs.cmd`
- `pp6_des.cmd`
- `pp6_des.par`
- `n1_msh.tdr`
- `n6_des.job`, `n6_des.sta`, `n6_des.err`, `n6_des.out` when present
- SHA-256 manifest
- executable paths / runtime context

## Gate B — clean-account preprocess comparison

In the clean account:

1. Import/copy the exact frozen editable source files.
2. Create a fresh Workbench project.
3. Run only far enough to generate SDE mesh and SDevice preprocessed inputs.
4. Before starting a multi-day full solve, compare:

```bash
sha256sum pp1_dvs.cmd pp6_des.cmd pp6_des.par n1_msh.tdr
```

Then run exact diffs for text inputs:

```bash
diff -u REF/pp1_dvs.cmd NEW/pp1_dvs.cmd
diff -u REF/pp6_des.cmd NEW/pp6_des.cmd
diff -u REF/pp6_des.par NEW/pp6_des.par
```

Binary `n1_msh.tdr` is compared by SHA-256 plus mesh statistics from SDevice output, not by text diff.

## Gate C — acceptance criteria

The clean-account reproduction passes only when:

- intended editable source is the same revision
- preprocessed SDE/SDevice command and parameter files are identical, except for explicitly documented path/node substitutions that do not alter physics
- reference mesh identity is established by hash, or any unavoidable binary difference is explained and mesh statistics/geometry are proven equivalent
- Sentaurus release/path and thread count are documented
- no hidden Workbench variable/scenario difference remains

If any unexplained difference exists, stop before a long run and resolve the difference first.

## Gate D — FAST branch

Only after Gate C passes:

- clone the verified baseline into a separate numerical-only FAST branch
- change one numerical factor at a time
- compare against the reference at matched bias/current
- reject any speedup that changes the physical result beyond the agreed tolerance

Initial candidates:

1. bias stepping / staged ramp
2. Newton iteration policy and high-bias cutback behavior
3. ErrRef / numerical tolerances, only with result validation
4. far-field mesh coarsening, preserving sidewall/MQW critical mesh
5. Quasistationary as a controlled acceleration experiment, not as an assumed equivalent replacement

## Current blocker

The exact Copy x8 editable source and generated preprocess/output files are not stored in the public GitHub repository. They must first be frozen locally and their non-proprietary hashes/metadata recorded before the FAST branch can be safely created.
