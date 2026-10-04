## 2026-10-04 — FAST C1 next action after B0 PASS

1. Send B0 summary to Claude for independent review; no code change is required unless Claude identifies a concrete issue.
2. Create a **separate** Workbench project/copy for FAST C1. Do not modify/stop live x6/x7/x8.
3. Install the exact Claude C1 source locally and verify SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`.
4. Preprocess only and run `fast_preprocess_check.py`.
5. Require: golden SDE/parameter equivalence + exactly one intended executable change (`Iterations=15`).
6. Run NtSide=0 C1 first.
7. Compare against Copy x8:
   - first divergence should occur only when the reference attempt exceeds 15 iterations (~4.33 V on current evidence)
   - I-V / matched-current Vf
   - accepted/rejected attempts
   - timestep trajectory
   - wallclock / mV-per-hour in the high-bias bottleneck
8. Do not declare FAST baseline CONFIRMED until numerical/physical equivalence and runtime criteria pass.

## 2026-10-04 — Rerun B0 with patched real-log parser

1. Re-download `CMP/tcad/tools/sdevice_newton_audit.py` from GitHub to `~/CMP_B0/`.
2. Run `--selftest`.
3. Re-run the x8 copied-log audit with `--raw 1` and CSV output.
4. Verify parsed first rejected/accepted attempt against raw log text.
5. Use the real accepted-step iteration distribution to decide whether C1 `Iterations=15` is safe.

## 2026-10-04 — Immediate B0 action: identify real x8 log syntax

1. Do not use the current audit statistics; parser matched zero attempts.
2. Inspect the raw x8 log for the exact transient step-start wording.
3. Patch `sdevice_newton_audit.py` to the actual T-2022.03 format.
4. Validate the patched parser by comparing parsed fields against raw log rows.
5. Only then evaluate accepted-step max iterations / false rejection for N=15.

## 2026-10-04 — B0 next: raw x8 n6_des.out audit

1. Copy live x8 `n6_des.out` to a safe home/bench location.
2. Download/run `CMP/tcad/tools/sdevice_newton_audit.py`.
3. First run `--selftest`.
4. Run x8 audit with `--raw 1` and CSV output.
5. Manually compare parser output with the raw Newton table.
6. Determine accepted-step max iteration and whether N=15 would create false rejections.
7. Send B0 output to Claude for independent interpretation before C1 execution.

## 2026-10-04 — FAST C1 immediate next action: B0 read-only audit

1. Do **not** launch FAST C1 yet.
2. Copy the active/reference x8 `pp6_des.cmd` and `n6_des.out` to a safe analysis location.
3. Inspect preprocessed settings:
   `grep -n -i "Iterations\\|RHSMin\\|CheckRhsAfterUpdate\\|NotDamped" pp6_des.cmd`
4. Run Claude `sdevice_newton_audit.py` on the copied x8 log with `--raw 1`.
5. Manually verify parser output against the raw Newton table before trusting any statistics.
6. Resolve why project records show ~50 Newton iterations while Synopsys 2022 training documents a default cap of 20 for ramped solves.
7. Confirm that no accepted x8 step requires >15 iterations.
8. Only after B0 passes: create/preprocess separate `GaN_PiN_Diode_FAST_C1`; keep live x6/x7/x8 untouched.
9. Acceptance targets remain provisional until baseline repeatability / actual A-B effect scale is known.

## 2026-10-04 — Immediate: hand golden source to Claude

1. Claude project에서 작업자 `이택규`로 시작.
2. exact file `Copy_x8_sd_fdiv_des.cmd` 첨부.
3. Claude에게 `CMP/prompts/CLAUDE_FAST_BASELINE_IMPLEMENTATION.md`를 읽고 그대로 구현 업무를 수행하도록 지시.
4. Claude는 attached source hash를 golden SHA-256과 확인.
5. Claude가 complete FAST_BASELINE source + diff + Workbench 적용법 + short benchmark plan을 작성.
6. live Copy x8은 수정하지 않음.
7. full proprietary source는 public GitHub에 commit하지 않음.

## 2026-10-04 — FAST v0.1 short benchmark

- Copy x8 live directory는 수정하지 않는다.
- 별도 Workbench copy/project에서 FAST v0.1을 시험한다.
- 첫 후보의 유일한 solver change는 transient inner Coupled `Iterations=15`.
- full DOE 전에 short benchmark로 다음을 비교:
  1. accepted/rejected Newton iterations
  2. high-bias timestep cutback pattern
  3. wallclock per accepted/rejected step
  4. I-V/current at matched bias
  5. spatial result availability
- 결과가 numerical tolerance 내에서 reference와 일치하면서 runtime이 개선될 때만 다음 후보로 채택.

## 2026-10-04 — CORRECTION: begin FAST code now; clean-account reproduction is a later freeze gate

- 작업자: 이택규
- 상태: DECISION / CORRECTION
- Copy x8 golden reference source/hash freeze가 완료되었으므로 numerical-only FAST_BASELINE 코드 작성과 short benchmark를 지금 시작한다.
- clean-account reproduction을 FAST 코드 작성 전 blocker로 두지 않는다.
- 올바른 순서:
  1. Copy x8 exact source/reference freeze
  2. separate FAST_BASELINE code/project 생성
  3. Newton iteration/cutback policy를 첫 numerical-only change로 short benchmark
  4. Copy x8과 결과 등가성 확인
  5. 필요 시 staged bias/MaxStep, ErrRef, far-field mesh를 하나씩 추가 benchmark
  6. 최종 FAST deck 후보가 확정되면 JuSubin/LeeTaekGyu clean-account reproduction gate 수행
  7. 그 뒤 Project A/B production runs 시작
- 기존 x6/x7/x8 live directories는 수정하지 않는다.
- Common Baseline physics/Nt/Et/sigma/5 nm damage width는 변경하지 않는다.

## 2026-10-04 — Next: clean-account reproduction gate

- Copy x8 golden snapshot/hash freeze 완료.
- 이제 이택규 clean account에서 새 Workbench project를 생성하고 exact frozen source를 가져온다.
- full multi-day solve는 아직 시작하지 않는다.
- preprocess / early initialization까지만 실행 후 golden reference와 비교:
  - sd_fdiv_des.cmd revision
  - pp1_dvs.cmd
  - pp6_des.cmd
  - pp6_des.par
  - n1_msh.tdr hash + mesh statistics
- unexplained difference가 하나라도 있으면 long run 시작 금지.
- 모두 일치/설명 가능할 때 numerical-only FAST baseline branch로 이동.

## 2026-10-04 — Immediate next action: finish Copy x8 golden reference package

- 작업자: 이택규
- 상태: ACTION READY
- 기존 local package `~/CMP_REFERENCE_20261004.tgz`에는 핵심 editable SDevice source `sd_fdiv_des.cmd`가 빠져 있음.
- 먼저 Copy x8 active directory에서 exact `sd_fdiv_des.cmd`를 reference snapshot에 포함하고 SHA-256 manifest를 다시 생성한다.
- 이후에만 이택규 clean account에서 새 Workbench project를 만들고 preprocess/init 단계까지만 실행한다.
- full multi-day solve 시작 전 필수 비교:
  - original editable source revision
  - `pp1_dvs.cmd`
  - `pp6_des.cmd`
  - `pp6_des.par`
  - `n1_msh.tdr` hash + mesh statistics
  - Workbench variables/tree/scenario context
  - Sentaurus executable path / 4-thread setting
- helper: `CMP/tcad/capture_reference_snapshot.sh`
- protocol: `CMP/FAST_BASELINE_REPRO_PROTOCOL.md`
- physics baseline은 이 단계에서 수정하지 않는다.

## 2026-10-04 — Decision: leave legacy runs untouched and build a new clean FAST baseline

- 작업자: 이택규
- 상태: DECISION
- 기존 Copy x6/x7/x8 active runs은 당장 중단하지 않고 reference/history 확보용으로 그대로 둔다.
- 새 baseline은 기존 live project를 수정하지 않고, exact Copy x8 golden pair를 기준으로 새 Workbench project에서 cleanly 재구성한다.
- 새 baseline 목표:
  1. Node6 NtSide=0 / Node12 NtSide=1e18 pair 유지
  2. 동일 geometry/physics/parameter/mesh intent 유지
  3. generated/stale/cached files에 의존하지 않는 clean reproduction
  4. numerical-only runtime optimization
  5. short preprocess/init benchmark 통과 후 full run
- Claude는 이 clean FAST_BASELINE branch/project만 수정 대상으로 삼고, 기존 Copy x6/x7/x8 live directories는 건드리지 않는다.

## 2026-10-03 — overnight execution plan

### Tonight
- Keep Copy x6 running as the historical v1.1 reference because it is currently the farthest progressed.
- Keep Copy x8 running as the preferred v1.2 reference with intermediate spatial TDR saves.
- Stop/retire Copy x7 through Workbench because it is semantically duplicate with x6 for the active v1.1 calculation and less progressed.
- Do not start a new full FAST baseline tonight before the exact x8 bundle is reviewed.
- Preserve/upload `CMP_Copy8_active_20261003.tgz` for tomorrow's code audit.

### Tomorrow
1. Review exact x8 source/preprocessed cmd/par/log.
2. Create a separate FAST_BASELINE branch/copy; never edit x8 live directory.
3. First benchmark only the highest-value numerical change: Newton iteration/cutback policy.
4. Then test staged bias/MaxStep and ErrRef one at a time.
5. Only after short benchmark equivalence is confirmed, launch full 0→5 V FAST baseline.
6. Split subsequent validated runs across JuSubin and LeeTaekGyu accounts.

## 2026-10-03 — CORRECTION: abstract deadline does NOT reduce baseline validation scope

- 작업자: 이택규
- 상태: DECISION
- 사용자 결정: 초록 마감이 있어도 Common Baseline 자체의 검증 강도는 낮추지 않는다.
- 따라서 abstract fast-track은 validation 항목 삭제가 아니라 runtime 최적화, 중복 run 제거, dual-account 병렬화로 시간을 줄이는 전략으로 수정한다.

### Baseline must-have before Project A/B main sweep
1. Exact baseline source freeze and provenance.
2. FAST numerical deck validated against Copy x8 reference.
3. Defect OFF vs nominal Defect ON physical trend.
4. NtSide sensitivity: 0 / 1e17 / 1e18 / 1e19.
5. Mesa-size sensitivity: 4 / 10 / 20 um.
6. Same-current comparison for I-V/Vf, sidewall SRH, MQW radiative/IQE proxy, spatial carrier/current distribution.
7. Mesh-convergence check around the chosen production mesh.
8. Reproducibility on JuSubin and LeeTaekGyu accounts using the same frozen baseline.

### Time compression strategy
- Stop duplicate runs.
- Optimize numerics without changing physics.
- Run short convergence benchmarks before full sweeps.
- Split independent validation cases across two accounts in parallel.
- Reuse already-completed trustworthy reference outputs where provenance is exact.

### Abstract strategy
Do not claim Project A/B final optimization until baseline gate is passed. If needed, submit an abstract centered on the validated baseline + initial mechanism results while full DOE continues, but baseline itself remains fully validated.

## 2026-10-03 — ABSTRACT-DEADLINE FAST TRACK

### Deadline context
논문 초록을 2026-10 내 제출해야 하므로 validation scope를 단계화한다.

### Phase 1 — Minimum defensible baseline (immediate priority)
Goal: scientific baseline + runtime reduction sufficient to start Project A/B.
Required before A/B:
- Copy x8 exact source bundle frozen.
- Duplicate x7 retired to free resources.
- One FAST numerical candidate benchmarked against Copy x8.
- Defect OFF vs nominal Defect ON trend confirmed.
- Same-current I-V / sidewall-SRH / MQW-radiative comparison available at representative bias/current.
Not required before abstract:
- full NtSide sweep 0/1e17/1e18/1e19
- mesa 4/10/20 um sweep
- full mesh-convergence campaign
- exhaustive A/B DOE

### Phase 2 — Abstract-supporting preliminary A/B
After FAST baseline freeze:
- Run one nominal Project A condition and one nominal Project B condition.
- Compare against Defect-ON baseline at same injected current.
- Minimum evidence: Vf, integrated sidewall SRH, MQW radiative/IQE proxy, spatial current/carrier redistribution.
- If one project is delayed, abstract can be framed around baseline + one demonstrated edge-access mechanism and the second as ongoing comparative extension only if wording is accurate.

### Phase 3 — Full paper validation after abstract
Perform NtSide, mesa scaling, A/B DOE, mesh convergence, robustness, dual-account reproduction.

### Operational principle
Do not spend the abstract window on exhaustive validation. Freeze a defensible baseline quickly, collect one clear mechanism result per project, then expand after abstract submission.

## 2026-10-03 — PROPOSED fast-baseline acceptance protocol

Runtime optimization must not be accepted solely because it is faster. Compare each candidate against the Copy x8 reference with frozen physics.

Proposed numerical-equivalence checks:
- same I-V / total current trend at matched bias/current
- target-current Vf difference preferably within ~10 mV
- integrated sidewall SRH difference preferably within ~2%
- MQW radiative/IQE-proxy difference preferably within ~2%
- no qualitative change in carrier/current spatial distribution
- identical conclusions for Defect OFF vs nominal Defect ON

These are project acceptance targets, not literature-standard universal tolerances, and may be tightened after the first benchmark.

First runtime target:
- reduce week-scale runs to <=24 h if possible without losing numerical equivalence.
- observed normal accepted steps are often ~25 s while rejected high-bias steps can exceed 1000 s, so Newton-failure handling is the highest-priority lever.

## 2026-10-03 — Baseline freeze + runtime acceleration plan

### Goal
Create a baseline that is both scientifically defensible and fast enough for repeated DOE/sweeps.

### Baseline reference
- Use Copy x8 as the preferred latest reference.
- Preserve its exact running source/preprocessed input before any edits.
- Keep geometry, epitaxy, contacts, trap model, Nt/Et/sigma, recombination models, Mg incomplete-ionization setup, heterojunction physics, and output definitions frozen during runtime optimization.

### Immediate actions
1. Stop/retire Copy x7 after preserving provenance, because x6/x7 are semantically duplicate active calculations.
2. Keep one v1.1 historical reference if desired (x6) and keep x8 as the latest v1.2 reference.
3. Build a separate FAST_BASELINE branch cloned from x8; never edit the live x8 directory.
4. Optimize numerics in controlled short benchmarks, one group at a time:
   A. Newton iteration/cutback policy
   B. bias-step strategy and staged ramp
   C. ErrRef / convergence tolerance sensitivity
   D. mesh reduction only outside MQW, 5 nm sidewall damage, and heterointerfaces
5. For each candidate, compare against x8 at the same bias/current:
   - I-V / Vf
   - total current
   - integrated sidewall SRH
   - MQW radiative recombination / IQE proxy
   - spatial carrier/current distribution
   - convergence failures / cutbacks
   - wallclock per accepted step
6. Accept a faster deck only if electrical/physical outputs remain within a predefined tolerance versus the reference.
7. Once accepted, run the frozen FAST_BASELINE independently on JuSubin and LeeTaekGyu accounts before Project A/B divergence.

### Current observed runtime bottleneck
- High-bias Newton stagnation near RHS ~1e-3 causes 40–50 iteration failures, >1000 s wasted per rejected step, followed by timestep cutback.
- This is the first optimization target; output TDR saving is secondary.

## 2026-10-03 — next actions after identifying Copy x8 as latest useful baseline revision

1. Preserve the exact Copy x8 active-run bundle before any edits:
   - sd_fdiv_des.cmd
   - pp6_des.cmd / pp6_des.par
   - n1_msh.tdr hash
   - n6_des.out/log/sta/err
   - intermediate n6_inter_*.tdr inventory
2. Confirm Copy x6 vs Copy x7 source differences to document prior-revision changes.
3. Treat Copy x8 as the preferred latest reference because x7/x8 have identical source/grid/par and x8 differs only by intermediate TDR saves.
4. Copy x7 is numerically redundant with x8 for device physics; after preserving provenance, consider stopping x7 to free compute/license resources while keeping x8 running.
5. Do not stop Copy x6 until its source/grid differences vs x7 are documented and its value as historical reference is decided.
6. Create a separate numerical-optimization branch from Copy x8 exact source; do not edit the running directory in place.
7. Benchmark runtime changes with frozen physics/geometry/traps before launching another multi-day full run.

## Lee Taek Gyu — runtime optimization before another full-week baseline run (2026-10-03)

1. Recover the exact SDevice source currently/routinely used by JuSubin (Final v1.1/v1.2); do not optimize the stale GitHub CURRENT deck.
2. Capture the latest active solver output: pseudo-time, accepted/rejected steps, Newton iteration counts, timestep and wallclock per step.
3. Keep physics/geometry/trap parameters frozen.
4. Make a numerical-only benchmark branch and test, one change group at a time:
   - bias step strategy / MaxStep and staged high-bias refinement,
   - Newton iteration limit around the documented 15–20 range where applicable,
   - III-nitride ErrRef sensitivity (current stale deck 1e4 vs Synopsys example scale 1e8),
   - mesh node-count reduction only away from MQW / 5 nm sidewall / heterointerfaces.
5. Use transient as the robustness reference; test Quasistationary as an acceleration branch and accept it only if final DC observables agree within a predefined tolerance.
6. Before committing to a multi-day full run, benchmark to an intermediate bias and compare wallclock/accepted-step/convergence behavior.

## 2026-09-29 — Ju Subin next check for active Node 6

1. Leave Node 6 running for now.
2. Reopen `n6_des.out` after additional runtime and confirm pseudo-time advances beyond ~0.93255.
3. Check whether timestep recovers after successful steps or continues shrinking toward `MinStep`.
4. If pseudo-time continues increasing, keep the run; this is slow convergence, not a hang.
5. If the same pseudo-time persists for many hours or timestep repeatedly collapses without accepted progress, then diagnose solver settings/resource state before restarting.
6. Do not change NtSide, Et, sigma, geometry, or other Common Baseline physics for this runtime symptom alone.

## 2026-09-29 — Ju Subin immediate run-status check

1. Select Node 19 (the branch that appears active) in Workbench.
2. Open **Job Log** and inspect the bottom for current state, host/job ID, exit/wait messages, or continuing SDevice output.
3. Open `n19_des.out` and inspect the last 30–50 lines; note the last BE-step/time/bias and whether the file timestamp is still updating.
4. If the log is still updating and BE-step/bias increases, leave it running; the other SDevice branch can remain `waiting` until resources free.
5. If the log timestamp has not changed for many hours and the same solve line is frozen, then diagnose scheduler/license/memory/hang before any restart.
6. Do not change baseline physics or abort both branches based only on the Workbench graph.

# Next Actions

## 2026-09-28 — Highest priority sync repair

1. Recover the exact full Final SDevice v1.1/v1.2 source from JuSubin's actual user-provided file/chat.
2. Re-read `CMP/tcad/CURRENT/sdevice2_defect_on.cmd` immediately before write.
3. Replace/update CURRENT only from that exact source; do not reconstruct from Issue summaries.
4. Verify v1.2 contains intermediate visualization TDR saves near 4.0–4.975 V while leaving physics/trap/solver/0→5 V ramp unchanged relative to v1.1.
5. Then preprocess both NtSide branches and confirm fair-comparison provenance.
6. Until step 3 is complete, treat `tcad/CURRENT/sdevice2_defect_on.cmd` as stale and not authoritative for the latest JuSubin run.

---


## Ju Subin — CES2027 selection presentation priority

1. Build the presentation around the weakness identified in week 1: make the TCAD implementation path for Project A/B concrete and testable.
2. Show only verified Common Baseline evidence as completed; label full same-revision NtSide=0 vs 1e18 electrical comparison as ongoing unless it actually finishes.
3. For Project A, specify the exact structural modification, TCAD region/material/doping/trap implementation, sweep variables, and expected observables.
4. For Project B, specify the exact localized AlGaN region, composition/width sweep, heterointerface physics, and expected band/carrier/recombination observables.
5. Define shared evaluation metrics before claiming improvement: same-current comparison, sidewall SRH, MQW radiative/Auger, IQE, Vf, current crowding, carrier/current maps.
6. Use the 1주차 발표 as context only; spend presentation time on progress, implementation specificity, evidence, and next-stage experiment design.

## Ju Subin — deadline-driven plan for today

1. Apply the final SDevice fix and preprocess both NtSide=0 and 1e18.
2. Verify generated PAR files are identical and CMD differs only in NtSide-controlled trap Conc.
3. Run NtSide=1e18 only long enough to verify initialization/initial Poisson-Coupled solve proceeds without the prior immediate exit.
4. Preserve historical completed NtSide=0 as reference evidence, but do not use it as final quantitative control against the new revision.
5. Build PPT today around:
   - baseline structure/parameter provenance
   - verified geometry/doping
   - finalized common SDevice model
   - historical successful 5 V control as implementation reference
   - current-revision NtSide=1e18 startup validation
   - full same-revision NtSide=0 vs 1e18 transient comparison marked ongoing.
6. Schedule full same-revision 0/1e18 runs after the presentation deadline.


## Ju Subin — exact code edit for Mg incomplete ionization

- Delete global:
```
IncompleteIonization(
  Dopants = "pMagnesiumActiveConcentration"
)
```
- Add region-scoped activation to `Clean_pGaN`, `DmgL_pGaN`, `DmgR_pGaN` only.
- Change nothing else before rerun.


## Ju Subin — freeze one baseline revision, then rerun both branches

1. Keep historical Node6 as a reference result only; do not treat it as the final control for current Node12.
2. Decide/freeze the intended final Mg incomplete-ionization formulation and parameter file.
3. Ensure the same SDevice source and same source parameter file generate both branches.
4. Preprocess NtSide=0 and NtSide=1e18 and diff CMD/PAR:
   - CMD should differ only in NtSide-controlled trap Conc.
   - PAR should be identical.
5. Then run both full simulations for the final baseline comparison.
6. A short Node12-only diagnostic run may still be used to test a crash fix, but it is not the final comparison dataset.


## Ju Subin — apply region-scoped Mg incomplete ionization

In the original SDevice source:

1. Remove from global `Physics`:
```
IncompleteIonization(
  Dopants = "pMagnesiumActiveConcentration"
)
```

2. Add to `Clean_pGaN`:
```
Physics (Region="Clean_pGaN") {
  IncompleteIonization(
    Dopants = "pMagnesiumActiveConcentration"
  )
}
```

3. In existing `DmgL_pGaN` and `DmgR_pGaN` Physics blocks, add the same `IncompleteIonization(...)` alongside the existing Traps block.

4. Do not change:
- NtSide
- Et=Ev+0.75 eV
- sigma_n=sigma_p=1e-15
- 5 nm damage geometry
- Thermionic
- Plot list

5. Re-preprocess Node12 and verify:
- no InGaN Mg incomplete-ionization missing-parameter messages
- SDevice enters initial Poisson solve.

6. If initialization succeeds, continue the 1e18 run. Final fair comparison still requires NtSide=0 and 1e18 from the same frozen source revision.


## Ju Subin — inspect Mg ionization parameter file before rerun

1. Do not rerun Node 12 again yet.
2. Open `pp12_des.par`.
3. Search for:
   - `Ionization`
   - `Magnesium`
   - `InGaN`
   - `GaN`
   - `AlGaN`
4. Capture every `Ionization { Species(...) { ... } }` block involving Mg and the material header above it.
5. Verify whether the species name is `MagnesiumActiveConcentration`, `pMagnesiumActiveConcentration`, or another internal species.
6. Verify whether InGaN has an Mg ionization parameter block.
7. Only after this, choose between:
   - correcting the selected Mg species name,
   - restricting incomplete ionization to materials with calibrated Mg parameters,
   - or adding a justified InGaN Mg ionization parameter if literature/source supports it.
8. For fair baseline comparison, once the physics deck is frozen, regenerate/rerun both NtSide=0 and 1e18 from that same source revision (or explicitly use the historical Node6 deck and reproduce its source exactly).


## Ju Subin — immediate action after reproducible Node 12 failure

1. Do not rerun Node 12 again yet.
2. Open original SDevice source `sd_fdiv_des.cmd` (not `pp12_des.cmd`).
3. Search for `NtSide`.
4. Around every match, capture any `#if/#else/#endif`, Tcl/preprocessor expression, or conditional insertion of:
   - `Thermionic`
   - `IncompleteIonization(Dopants=...)`
   - Mg Plot fields
5. Compare Node 6/12 Job Log preprocessing timestamps/source path to determine whether Node 6 is stale from an older source revision.
6. Once provenance is known, make the two branches truly identical except for trap `Conc`.


## Ju Subin — verify parameter-dependent preprocessing before any edit

1. Do **not** edit the physics yet.
2. Open the original SDevice source `sd_fdiv_des.cmd`.
3. Search for:
   - `NtSide`
   - `Thermionic`
   - `IncompleteIonization`
   - `Dopants`
   - `eQuasiFermiEnergy`
   - `pMagnesiumActiveConcentration`
   - `#if`, `#else`, `#endif` or other Workbench preprocessing expressions
4. Capture the relevant source block(s).
5. Confirm Node 6 and Node 12 Job Logs both preprocess the same source path and compare timestamps.
6. Only after identifying why NtSide changes unrelated preprocessed lines should a minimal fix be considered.


## Ju Subin — clean NtSide-only rerun (2026-09-26)

1. Edit the original SDevice source (not generated `pp12_des.cmd`).
2. Make global Physics identical to successful Node 6:
   - remove Node12-only `Thermionic` for this diagnostic rerun
   - replace `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")` with plain `IncompleteIonization`
3. Make Plot identical to Node 6 by removing Node12-only:
   - `eQuasiFermiEnergy`
   - `hQuasiFermiEnergy`
   - `pMagnesiumActiveConcentration`
   - `pMagnesiumMinusConcentration`
4. Preserve trap model and keep the Workbench NtSide-controlled concentration at 1e18.
5. Re-preprocess and confirm the new 1e18 preprocessed deck differs from Node 6 only in trap `Conc`.
6. Rerun only the 1e18 branch.
7. If it still fails, then diagnose the nonzero trap interaction itself.


## Ju Subin — exact Node 6 vs Node 12 deck diff next

After capturing failed Node 12:
1. Obtain successful Node 6 corresponding sections from `pp6_des.cmd`.
2. Compare line-by-line:
   - global Physics (`Thermionic`, `IncompleteIonization` syntax)
   - every trap block and Conc
   - Plot block
3. Expected fair split: only NtSide-controlled trap concentration should differ.
4. If additional differences exist, restore a true NtSide-only split before rerunning.
5. Do not change Nt/Et/sigma based solely on the incomplete-ionization warning.


## Ju Subin — highest-priority deck diff (2026-09-26)

Before changing `IncompleteIonization`, trap parameters, or solver settings:

1. Compare `pp6_des.cmd` and `pp12_des.cmd`.
2. Compare `pp6_des.par` and `pp12_des.par`.
3. Expected fair-split difference: only `NtSide`-controlled trap `Conc` values (0 vs 1e18).
4. Pay special attention to:
   - global `IncompleteIonization`
   - QW/InGaN region-specific Physics blocks
   - Mg doping species references
   - parameter-file includes/overrides
   - trap blocks for DmgL/R_QW1~QW4
5. If CMD/PAR are otherwise identical, investigate why nonzero traps activate the InGaN incomplete-ionization failure path.
6. If additional differences exist, fix deck drift first.


## Ju Subin — compare failed Node 12 against successful NtSide=0 log (2026-09-26)

1. Open the successful `NtSide=0` SDevice node.
2. Open its `*_des.log`.
3. Search for `mMagnesiumActiveConcentration`.
4. Report whether the same incomplete-ionization messages for InGaN QW regions appear.
5. If they do, capture the lines immediately after them showing the successful run proceeding.
6. If they do not, compare failed/successful preprocessed parameter and command files around IncompleteIonization/material setup.
7. Use `n12_des.sta` only if the successful-log comparison is inconclusive.


## Ju Subin — after Find Error shows warnings only (2026-09-26)

1. Open Node 12 output file `n12_des.log`.
2. Go to the very bottom and capture the final 50–100 lines.
3. Search for `Error`, `Fatal`, `abort`, `exception`, `signal`, `trap`, `memory`.
4. If `n12_des.log` also ends without a clear cause, open `n12_des.sta`.
5. Keep Nt/Et/sigma/geometry unchanged until the first actual failure message is identified.


## Ju Subin — Node 12 SDevice exit(1) next step (2026-09-26)

Preprocessing succeeded and SDevice itself returned `exit(1)`.

Immediate diagnostic:
1. In Node 12 Job Log, click **Find Error**.
2. Capture the exact file/line/message Workbench jumps to.
3. If it does not jump to a useful line, search `n12_des.err` for: `Error:`, `Fatal`, `Unsupported`, `invalid`, `not found`, `cannot`.
4. Only after the first explicit error line is identified should code be changed.


## Ju Subin — Node 12 wrapper exit follow-up (2026-09-26)

`n12_local.err` only reports a generic child-process abnormal exit with status 1.

Next diagnostic order:
1. Node 12 **Job Log** tab → capture bottom ~30–50 lines including exit status/command.
2. If still generic, open `n12_des.job`.
3. Check `n12_des.sta` for last stage/status.
4. Search `n12_des.err` and `n12_des.out` for: `Fatal`, `Error`, `Segmentation`, `Killed`, `signal`, `memory`, `license`, `abort`.
5. Do not rerun or change baseline physics until the actual process-exit reason is found.


## Ju Subin — Node 12 immediate diagnostic refinement (2026-09-26)

The provided `n12_des.err` view contains warnings but no explicit fatal cause, while `n12_des.out` terminates before normal completion and no TDR/PLT is visible.

Immediate order:
1. Open `n12_local.err` and capture all contents.
2. If empty/non-diagnostic, open the Node 12 **Job Log** tab and capture the bottom section with exit status.
3. If still unclear, open `n12_des.job` and inspect wrapper/exit code.
4. Only after the exact exit reason is identified, modify the minimum necessary numerical/model setting.


## Priority 0 — Ju Subin NtSide=1e18 failure diagnosis (2026-09-26)

1. Workbench에서 `NtSide=1e18` failed scenario의 SDevice node를 선택.
2. 해당 node의 `*.err`를 열어 전체 또는 첫 error/fatal message를 확보.
3. `*.out` 맨 아래 50~100줄을 확보.
4. error가 convergence인지 syntax/parameter인지 resource/solver인지 분류.
5. 실제 원인에 맞는 최소 수정만 적용.
6. 수정 전 `NtSide=0` 성공 조건과 동일한 geometry/physics baseline은 유지.


## Priority 0 — 현재 blocker 해결

### Goal
SDevice2(Node 9)의 실제 TDR output을 확인하고 SVisual2(Node 10)가 정확히 그 파일을 읽도록 연결한다.

### Steps
1. Node 9 Explorer에서 `pp9_des.cmd` 열기
2. 맨 위 `File { ... }` 블록 확인
3. 특히 preprocessed:
   - `Grid =`
   - `Plot =`
   - `Current =`
   - `Output =`
   값 기록
4. Node 9 Output Files 전체 목록에서 `.tdr` 파일명 확인
5. 실제 TDR이 존재하면 `svisual2_maps.tcl`의 `tdrfile`을 그 이름에 맞춤
6. 실제 TDR이 없다면 SDevice2의 output 생성 조건을 별도로 진단

## Parallel track — Ju Subin Common Baseline pre-run validation

### Current state
공유 프로젝트의 주수빈 채팅에서, 메인 SDevice와 관련 코드를 최종 수정했다고 사용자 보고가 있었음. 아직 최신 전체 코드 및 실행 결과는 GitHub에서 직접 검증되지 않음.

### Next steps
1. 주수빈 측 최신 전체 코드 원문을 CMP에 동기화
2. Project A/B 공통 baseline 조건에 맞는지 정적/논리 검토
3. 계산 비용을 고려해 우선 `NtSide=0` 실행
4. 우선 `NtSide=1e18` 실행
5. 두 run의 로그/결과를 비교하고 GitHub에 기록
6. 이후에만 더 넓은 Nt sweep 여부 결정

## Priority 1 — mechanism validation

TDR linkage 해결 후 SVisual2에서:
- SRH / trap-assisted recombination 관련 실제 available scalar 확인
- RadiativeRecombination
- AugerRecombination
- eDensity
- hDensity
- Current / TotalCurrentDensity
- ConductionBandEnergy
- ValenceBandEnergy
- trap occupation / concentration 관련 실제 available field 확인

**필드 이름은 SVisual 실제 목록을 기준으로 사용. 추측 금지.**

## Priority 2 — Defect OFF vs ON

동일 bias에서:
- edge recombination OFF vs ON
- radiative recombination OFF vs ON
- carrier distribution OFF vs ON
비교.

## Priority 3 — Baseline validation completion

- Nt sweep: 0 / 1e17 / 1e18 / 1e19
- mesa sweep: 4 / 10 / 20 µm
- mesh convergence
- IQE definition/volume integration 검증
- 2D Cartesian current-density normalization 확인

## Priority 4 — Freeze then branch

Common Baseline Final 통과 후에만:
- Project A Carbon High-R Edge
- Project B Localized AlGaN Lateral Heterobarrier
로 분기.


## Ju Subin immediate runtime diagnostic

1. 현재 Node 6은 화면상 진행 중이므로 18시간 경과만으로 hang으로 판정하지 않음.
2. `pp6_des.cmd`의 `Solve { ... }`에서 현재 BE/transient 구간의:
   - 최종 목표 시간 또는 ramp goal
   - `InitialStep`
   - `MinStep`
   - `MaxStep`
   - `Increment`
   - 해당 구간의 bias/ramp 설정
   을 확인.
3. 현재 관찰된 약 3564 s/step과 실제 남은 step 수로 예상 총 runtime 계산.
4. 코드 최적화/step 조정은 전체 최신 deck 확인 뒤에만 제안. Nt/Et/sigma/5 nm damage width 등 Common Baseline physics는 runtime 문제 때문에 임의 변경하지 않음.


## Ju Subin — next numerical action after runtime diagnosis

1. 현재 `pp6_des.cmd` 자체를 수정하지 말고 원본 SDevice deck의 `Transient` block을 확인한다.
2. DC baseline I–V가 목적이라면, 5 mV 고정 수준의 최대 bias increment가 실제로 필요한지 검토한다.
3. `MaxStep` 확대 또는 DC용 `Quasistationary` 전환 여부는 최신 전체 deck과 원하는 I–V 해상도/수렴 안정성을 함께 검토한 뒤 결정한다.
4. numerical stepping을 바꾸면 NtSide=0/1e18 및 이후 Project A/B 모두에 동일하게 적용하고, coarse/fine step 비교로 결과 민감도를 검증한다.
5. Nt/Et/sigma/damage width/epitaxy/doping 등 Common Baseline physics는 runtime 때문에 변경하지 않는다.


## Ju Subin — compare against prior 3-day run

현재 코드를 바로 바꾸기 전에 과거 3일 run과 아래를 1:1 비교한다.
1. old/new `Transient`: InitialStep / MinStep / MaxStep / Increment / Goal
2. old/new mesh statistics: vertices/elements 또는 total grid points/unknowns
3. old/new Physics 및 Traps: 추가 모델, 적용 region, trap density/cross section 자체가 아니라 **적용 범위와 coupling 변화**
4. old/new Math: linear solver, Iterations, Method, damping/derivative 관련 옵션
5. old/new `.out`: accepted step 당 Newton iteration 수와 failed/retry/cutback 횟수

이 비교 전에는 MaxStep 확대를 확정 조치로 적용하지 않는다.


## Ju Subin — identical-bias slowdown follow-up

1. old/current `.out` 시작부의 mesh/grid/unknown statistics를 비교.
2. old/current `pp*_des.cmd`에서 Physics/Traps와 Math/Solver block을 diff.
3. 동일 0.3834 V step의 Newton iteration 수 및 linear iterative count/time을 비교.
4. 차이가 확인되기 전 numerical step size를 먼저 변경하지 않음.


## Ju Subin — identify slow stage inside current run

1. `pp6_des.cmd` 하단 검색창에서 `Transient(`를 검색하고 Search Fwd를 반복해 등장 횟수를 센다.
2. `n6_des.out`에서 `3563.68`을 검색해 느린 step 위치로 이동한다.
3. 그 위치에서 위로 20~40줄 정도 올려 다음을 함께 확인한다:
   - `Computing BE-step from ... to ...`
   - 직전/다음 contact voltage
   - 해당 solve stage 시작을 알리는 문구
   - `NewCurrentPrefix`, `Set`, `Load`, 다른 ramp/Transient 전환 여부
4. `0.0766738`을 검색해 같은 숫자가 output에 여러 번 등장하는지도 확인한다.
5. 이 stage 식별 전에는 MaxStep, mesh, physics를 변경하지 않는다.


## Ju Subin — corrected next action after old/current confirmation

1. 과거 3일 완료 run과 현재 run의 `pp*_des.cmd`를 1:1 비교한다.
2. 우선순위:
   - Math / linear solver block
   - Physics / Traps 적용 범위
   - mesh/grid/unknown statistics
   - 동일 0.3834 V step의 Newton/linear iteration 세부 비용
3. step-control 자체는 두 run에서 동일한지 확인하되, 현재 20.1× 차이는 per-step 비용 차이로 먼저 설명해야 한다.
4. 기존 "same-run repeated Transient stage" 확인은 우선순위에서 제외.


## Ju Subin — immediate old/current deck comparison

1. 현재 slow Node 6의 `pp6_des.cmd`에서 `Conc =`를 검색해 실제 NtSide가 0인지 1e18인지 확인.
2. current도 Conc=0이면 old/current full `pp6_des.cmd`를 diff:
   - Math / ILS
   - Physics / Mobility / Recombination
   - trap region list 및 syntax
3. old/current `.out` 시작부의 grid/vertex/element/equation/unknown 통계를 비교해 mesh 변화 여부 확인.
4. current가 Conc=1e18이면 old fast deck과 직접 속도 비교를 중단하고, current NtSide=0 node와 old NtSide=0을 비교.
