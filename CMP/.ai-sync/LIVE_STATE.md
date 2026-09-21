# LIVE AI STATE

Last update: 2026-09-21
Primary worker: 이택규
Current phase: Phase 0 — Common Baseline validation
Current task: SDevice2 → SVisual2 TDR output/linkage debugging

## One-line handoff

**SDevice2(Node 9)는 solver 종료까지 갔지만 SVisual2(Node 10)가 기대하는 `n9_des.tdr`이 Node 9 Output Files에서 보이지 않아 로드에 실패한 상태다. 다음 AI는 trap physics를 건드리지 말고 실제 preprocessed Plot filename부터 확인해야 한다.**

## Current blocker

SVisual2 error:

```text
File 'n9_des.tdr' could not be loaded.
```

SVisual2 currently constructs:

```tcl
set tdrfile n@previous@_des.tdr
load_file $tdrfile -name $dname2
```

Node 10 previous node = 9.

## OBSERVED evidence

1. Node 9 `n9_des.out` ends with:

```text
Sentaurus Device simulation finished
Good Bye !
```

Therefore the observed Node 9 run did not terminate with a solver fatal error.

2. Node 9 Explorer Output Files screenshot showed:

```text
n9_des.err
n9_des.job
n9_des.out
n9_des.sta
n9_local.err
pp9_des.cmd
pp9_des.par
```

`n9_des.tdr` was not visible in that screenshot.

3. The Node 9 output also displayed the Plot variable list, including:
- SRHRecombination
- RadiativeRecombination
- AugerRecombination
- TotalRecombination
- Current / eCurrent / hCurrent
- ElectricField
- DopingConcentration
- ConductionBandEnergy / ValenceBandEnergy
- xMoleFraction / yMoleFraction

4. Earlier SVisual2 Tcl mistakes already resolved:
- `create_plot -2d` invalid
- `@node|sdevice@` invalid in this flow
- SVisual2 must not contain an SDevice `Plot { ... }` block

## CURRENT GitHub code

Read these exact files before proposing edits:

- `CMP/tcad/CURRENT/sdevice2_defect_on.cmd`
- `CMP/tcad/CURRENT/svisual2_maps.tcl`
- `CMP/tcad/CURRENT/svisual1_iv.tcl`

SDE and SDevice1 latest full source are NOT yet synchronized.

## Next diagnostic — highest priority

Open `pp9_des.cmd` and inspect the preprocessed `File { ... }` block.

Need exact values of:

```text
Grid =
Parameters =
Plot =
Current =
Output =
```

Then compare the actual preprocessed `Plot = "..."` filename against Node 9 Output Files.

### Decision logic

- If a TDR exists under a different name → fix SVisual2 filename/reference only.
- If `Plot=` points to expected TDR but no TDR exists → diagnose why the SDevice run did not emit the device plot file.
- Do not modify Nt/Et/sigma/damage width while diagnosing this.

## Do NOT change

- Nt = 1e18 cm^-3 nominal Defect ON
- Et = Ev + 0.75 eV
- sigma_n = sigma_p = 1e-15 cm^2
- damage width = 5 nm
- Kou-based vertical epitaxy
- mesa = 4 µm representative modeling choice
- common contacts/physics for A/B comparison

## Known caution from previous ChatGPT attempts

Several trap-output keywords were previously proposed in bulk without confirming T-2022.03 support. Do not reintroduce unverified keywords by guess.

The original synchronized SDevice2 deck contains `SRHRecombination`; the fact that it was not visible in one SVisual scalar list does NOT by itself prove that the keyword is invalid.

## Goal after blocker is solved

1. Load Defect-ON TDR in SVisual2
2. Inspect actual available scalar names
3. Validate sidewall-localized recombination/trap effect
4. Compare Defect OFF vs ON
5. Continue Nt / mesa-size / mesh convergence validation
