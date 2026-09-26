# LIVE AI STATE

## 2026-09-26 — exact fix selected

- Proposed minimal edit: move Mg incomplete ionization from global Physics to p-GaN regions only.
- Do not alter Thermionic, trap parameters, Plot, Math, Solve, or geometry.
- After edit, rerun both NtSide=0 and 1e18 from the same frozen source/PAR revision for final comparison.


## 2026-09-26 — fair-comparison correction

- Node6 pp6_des.par and Node12 pp12_des.par are different revisions.
- Node6 uses generic P/N dopant ionization species; Node12 uses pMagnesiumActiveConcentration.
- Existing Node6 vs current/fixed Node12 is not a valid final NtSide-only comparison.
- Final baseline must freeze one source + parameter-file revision and rerun both NtSide=0 and 1e18.
- Node12-only fix remains diagnostic only.


## 2026-09-26 — Mg incomplete-ionization mismatch found

- pp12_des.par has Mg ionization parameters only under Material=GaN for pMagnesiumActiveConcentration.
- No InGaN ionization parameters are present.
- Node12 fails immediately after missing Mg incomplete-ionization parameter messages in InGaN QWs.
- Current source activates Mg incomplete ionization globally.
- Strong root-cause candidate: model/parameter material-scope mismatch.
- Proposed minimal fix: region-scope IncompleteIonization to Clean/DmgL/DmgR pGaN only; keep traps/Thermionic/Plot unchanged.
- Confirmation requires Node12 re-preprocess + initialization rerun.


## 2026-09-26 — full source inspection result

- Current SDevice source has no NtSide-dependent conditional preprocessing.
- NtSide only controls trap Conc.
- Current source always includes Thermionic + species-selected Mg IncompleteIonization + expanded Plot.
- Successful Node6 pp6 lacks those items, so Node6 is historical/stale relative to current source revision.
- Existing Node6 and current Node12 are not a clean same-source NtSide-only comparison.
- Node12 failure remains strongly tied to Mg incomplete-ionization initialization in InGaN.
- Next: inspect pp12_des.par Ionization/Magnesium/InGaN blocks before editing or rerunning.


## 2026-09-26 — Node 12 failure reproduced

- Node 12-only rerun fails again.
- Failure is reproducible.
- Same-source NtSide split is user-confirmed.
- Most likely next discriminators: NtSide-dependent preprocessing vs stale/cached Node 6 preprocess from an older source revision.
- Do not rerun or edit baseline physics until original source conditional logic/provenance is inspected.


## 2026-09-26 — correction: same source, NtSide-only split confirmed by user

- User states Node 6 and Node 12 used the same source; only NtSide=0 vs 1e18 was split.
- Prior proposed physics cleanup is retracted pending source inspection.
- pp6/pp12 differences may come from NtSide-dependent preprocessing or node/input version behavior.
- Do not edit Thermionic/IncompleteIonization/Plot yet.
- Next: inspect original sd_fdiv_des.cmd for parameter-dependent conditionals and source provenance.


## 2026-09-26 — Node 6/12 exact diff found

- Successful Node 6 and failed Node 12 are not NtSide-only decks.
- Extra Node12-only changes: `Thermionic`, species-selected `IncompleteIonization`, and four extra Plot fields.
- Intended difference: trap Conc 0 vs 1e18.
- Current failure therefore cannot yet be blamed on NtSide=1e18 alone.
- Proposed next: restore Node 6 Physics/Plot in original SDevice source, keep only NtSide=1e18, verify preprocessed diff, rerun.
- Status: PROPOSED FIX / UNCONFIRMED until rerun.


## 2026-09-26 — failed Node 12 deck captured

- Node 12 has `Thermionic` and `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`.
- Sidewall traps are 1e18 across pGaN/EBL/barriers/QWs/nGaN.
- Plot block is expanded with trap/SRH/Mg outputs.
- This differs from synchronized baseline record; possible deck drift beyond NtSide.
- Next: exact successful Node 6 pp6_des.cmd diff before any correction.


## 2026-09-26 — baseline branch comparison status

- NtSide=0 Node 6: CONFIRMED normal completion to 5 V; TDR written; wallclock ~65.4 h.
- NtSide=1e18 Node 12: SDevice exit(1) during initialization.
- Success log has no `mMagnesiumActiveConcentration` warning; failed log does.
- Strong correlated difference, but root cause not yet proven.
- Next action: diff `pp6_des.cmd/par` vs `pp12_des.cmd/par` before any physics change.


## 2026-09-26 — Node 12 des.log comparison needed

- Failed `n12_des.log` terminates immediately after InGaN Mg incomplete-ionization parameter messages, then returns licenses.
- No normal solver start is visible.
- Causality is unresolved.
- Highest-priority discriminator: compare the successful NtSide=0 node log for the exact same message.
- Do not alter baseline physics until this comparison is done.


## 2026-09-26 — Node 12 Find Error exhausted

- Find Error output reaches `**** End` with warnings only; no explicit fatal/root cause visible.
- The warnings concern E0 anisotropy and missing Mg incomplete-ionization parameters in InGaN.
- Their causal role is unproven.
- Highest-priority next evidence: `n12_des.log` bottom, then `n12_des.sta`.
- Status remains UNRESOLVED.


## 2026-09-26 — Node 12 failure location narrowed further

- Workbench preprocessing: successful.
- `pp12_des.cmd` / `pp12_des.par`: generated.
- SDevice command launched: `sdevice --max_threads 4 pp12_des.cmd`.
- SDevice returned `exit(1)` shortly after launch.
- Failure is therefore inside SDevice initialization/model setup, not SWB preprocessing/dependency.
- Root cause still UNRESOLVED.
- Next: use **Find Error** / explicit error search in `n12_des.err`.


## 2026-09-26 — Node 12 local.err result

- `n12_local.err`: `Job failed` / `child process exited abnormally` / `gjob exits with status 1`.
- This is a generic wrapper-level failure, not the root cause.
- Root cause remains UNRESOLVED.
- Next evidence: Node 12 Job Log bottom; then `n12_des.job` / `n12_des.sta`.
- Do not alter Common Baseline physics yet.


## 2026-09-26 — Ju Subin Node 12 failure narrowed

- `NtSide=1e18` failed Node = 12.
- `n12_des.err` visible messages are warnings; no fatal cause yet observed.
- `n12_des.out` ends during initialization/license return, without normal SDevice completion text.
- No TDR/PLT visible in Node 12 output list.
- Priority next evidence: `n12_local.err`, then Workbench Job Log.
- Status: UNRESOLVED; do not change baseline physical parameters yet.


## 2026-09-26 — 주수빈 baseline split-run 확인

- OBSERVED: `NtSide=0` run 정상 완료.
- OBSERVED: `NtSide=1e18` run failed.
- Cause: 아직 UNRESOLVED.
- Immediate next action: failed 1e18 SDevice node의 `*.err`와 `*.out` 마지막 구간을 확인해 최초 실패 원인을 식별.
- Do not change Common Baseline physical parameters before log-based diagnosis.


Last update: 2026-09-21
Primary worker: 이택규
Current phase: Phase 0 — Common Baseline validation
Current task: SDevice2 → SVisual2 TDR output/linkage debugging

## Parallel worker — 주수빈

**OBSERVED from shared project conversation:** 주수빈은 Common Baseline 관련 메인 SDevice 및 관련 코드를 최종 수정했다고 보고했고, 장시간 simulation 전에 Project A/B 공통 baseline 적합성을 마지막으로 검토 중이다.

Planned first runs:
- `NtSide=0`
- `NtSide=1e18`

Reported compute cost:
- 약 3일 / run

Verification boundary:
- 주수빈 측 최신 전체 코드와 새 simulation 결과는 이 sync 시점에 GitHub에서 직접 확인되지 않음.
- 따라서 코드 정확성/성공 여부는 아직 CONFIRMED 아님.

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
JuSubin latest modified full code is also NOT yet synchronized.

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


## 2026-09-22 parallel update — 주수빈 runtime

- Node 6 SDevice NtSide split run이 18시간 이상 실행 중.
- OBSERVED: 직전 BE step은 정상 수렴 완료, total wallclock 약 3563.68 s (~59 min/step).
- 다음 BE step은 약 0.0766738 → 0.0776738, Stepsize=1e-3로 계속 진행 중.
- 현재 증거만으로는 hang/fatal이 아니라 매우 느린 진행으로 판단.
- 주수빈 다음 우선 확인: pp6_des.cmd Solve block의 최종 목표와 step-control 설정을 읽어 총 step 수/예상 runtime 산정.


### 2026-09-22 runtime diagnosis confirmed
- pp6_des.cmd Transient: InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Goal anode=5.0 V.
- Log cross-check: pseudo-time ~0.0766738 corresponds to anode ~0.3834 V, matching 5*time.
- Therefore MaxStep=1e-3 corresponds to ~5 mV maximum bias increment.
- Current point leaves roughly 923–924 accepted steps minimum to reach 5 V.
- Using the latest observed ~3564 s/step as a crude extrapolation gives ~38 days remaining; actual cost can vary with bias.
- Treat current JuSubin blocker as numerical step strategy/computational cost, not SDE/SDevice dependency failure.


### Runtime diagnosis refinement
- User reports the pre-final-edit version of nearly the same deck completed in ~3 days.
- Therefore MaxStep=1e-3 explains a large step count but is not established as the new slowdown cause.
- If old/new step-control is the same, prioritize comparing per-step solve cost and rejected/cutback steps, then mesh size, Physics/Traps application scope, and Math solver settings.
- The prior ~38-day estimate is only a crude extrapolation from one slow step, not a reliable ETA.


### 2026-09-22 identical-bias comparison
- Old run at anode ~0.3834 V: Total 177.47 s (Assembly 64.84 s, Solve 108.74 s).
- Current run at same accepted anode ~0.3834 V: Total 3563.68 s (Assembly 598.77 s, Solve 2928.83 s).
- Current accepted-step cost is ~20.1x old at the same bias.
- Root cause is therefore narrowed to per-step computational cost, not merely MaxStep/step count.
- Next: compare mesh/grid/unknown statistics, Physics/Traps scope, and Math/solver settings old vs current.


### 2026-09-22 correction — same-file early vs late stage
- The 123–177 s logs around 0.30–0.3834 V are NOT verified as an old 3-day run; they are from the current Node 6 `n6_des.out` early section.
- Current run early: 0.0756738→0.0766738 reached ~0.3834 V in Total 177.47 s.
- A later screen from the same current run showed ~0.3834 V with Total 3563.68 s.
- Therefore prior "old vs current 20.1x" conclusion is invalid.
- Highest priority: determine whether the same pseudo-time/voltage ramp occurs in multiple Transient/Solve stages. Search all `Transient(` in pp6_des.cmd and locate `3563.68` / repeated `0.0766738` in n6_des.out.


### 2026-09-22 re-correction — old run confirmed by user
- User explicitly confirmed the 177.47 s / ~0.3834 V screenshot was from the older node that completed in ~3 days.
- Restore valid comparison:
  - old: Total 177.47 s (Assembly 64.84 s, Solve 108.74 s)
  - current: Total 3563.68 s (Assembly 598.77 s, Solve 2928.83 s)
  - current is ~20.1x slower per accepted step at the same anode voltage.
- Prior "same current run repeated stage" correction is retracted.
- Next: diff old vs current Math/solver, Physics/Traps scope, and mesh/unknown statistics.


### 2026-09-22 old 3-day full deck captured
- Old preprocessed `pp6_des.cmd` provided in full.
- All DmgL/R trap blocks have `Conc=0`; this is an NtSide=0 case.
- Old numerical stepping: InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Goal anode=5 V — same as the slow current Solve block already observed.
- Old Math signature: 4 threads, Digits=5, ErrRef=1e4, RHSMin=1e-3, BE, ExtendedPrecision(80), Blocked + ILS(22), gmres(100), tolrel=1e-10, ilut(1e-8,-1).
- Priority: verify current slow node's actual trap Conc. Only compare runtime directly if current is also NtSide=0.
