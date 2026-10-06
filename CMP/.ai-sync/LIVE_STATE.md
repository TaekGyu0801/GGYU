## 2026-10-06 — Node 6 and Node 12 SDevice processes confirmed alive at evening check

- 작업자: 이택규
- 상태: OBSERVED / RUNTIME
- user-provided process listing at ~2026-10-06 21:43 KST shows both baseline runs have live SDevice processes:
  - FAST_C1 Node 6: PID 69457, command `sdevice --max_threads 4 pp6_des.cmd`
  - FAST_C1_Copy Node 12: PID 93915, command `sdevice --max_threads 4 pp12_des.cmd`
- both processes showed active CPU usage in the provided `ps` output.
- a solver line `Computing BE-step from 0.845455 s to 0.845473 s (Stepsize: 1.7909e-05 s)` was also provided, but the originating project/node is not yet attributable from the pasted context alone.
- `ls n6_des.out` failed only because it was run from the home directory (`~`), not from the FAST_C1 project directory; this is not evidence that the log file is missing.
- next: inspect timestamp and tail of `n6_des.out` and `n12_des.out` from their respective project directories to determine whether accepted pseudo-time is still advancing or a convergence retry loop is occurring.

## 2026-10-06 — Runtime-first half + coarse-mesh candidate prioritized

- 작업자: 이택규
- 상태: DECISION / DEADLINE ACCELERATION
- 기존 FAST_C1 full Node 6/12는 reference로 유지.
- 새 accelerated branch는 half-domain + coarse remote/global bulk mesh를 동시에 적용하여 10/23 전 preliminary result 확보를 우선.
- active physics/critical mesh는 유지: MQW, EBL, GaN/InGaN and GaN/AlGaN interfaces, 5 nm sidewall damage.
- first gate before long solve: SDE mesh build only -> element/point count + visual mesh sanity.
- half-domain current normalization: full-device total current 비교 시 2×I_half 또는 current density 사용; IQE ratio 자체는 ×2 하지 않음.
- branch classification: preliminary/screening until full-reference equivalence/mesh-convergence is demonstrated.

## 2026-10-06 — Oct 23 abstract deadline: runtime-first triage

- 작업자: 이택규
- 상태: CRITICAL DEADLINE / DECISION
- 논문 초록 마감: 2026-10-23.
- primary blocker: FAST_C1 Node 6/12가 multi-day runtime을 요구하고 Node 6은 ~4.68 V 부근 high-bias timestep collapse가 관찰됨.
- current full-reference runs는 가능하면 유지하되, 이들의 완주를 기다리는 것을 critical path에서 제거.
- immediate parallel task: same physics/mesh의 numerical-only accelerated branch short benchmark.
- first methods to audit: Quasistationary DC sweep vs current Transient ramp, staged continuation, Save/Load/restart, bias segmentation, thread/output overhead.
- publication constraint: physics/trap/geometry를 runtime 때문에 완화하지 않으며 acceleration은 reference-equivalence validation을 통과해야 함.
- abstract strategy: 10/23 전 모든 sweep 완료가 아니라 defensible baseline + 최소 mechanism-relevant preliminary result를 확보.

## 2026-10-06 — Priority reset: finish and validate Common Baseline before Project A/B

- 작업자: 이택규
- 상태: DECISION / PRIORITY
- 사용자가 연구 우선순위를 Common Baseline 완성으로 재확정.
- 즉시 우선순위:
  1. FAST_C1 Node 6 (NtSide=0) 현재 run 유지 및 완주.
  2. 별도 프로젝트로 시작한 Node 12 (NtSide=1e18)의 실제 정상 실행 여부를 process/log로 확인.
  3. 두 run의 source/mesh/parameter/numerical provenance를 확인.
  4. 완주 후 I-V, convergence, key output sanity를 검증.
  5. 두 조건이 모두 통과한 뒤에만 FAST_C1 Common Baseline을 freeze.
- Project A/B 설계 및 sweep은 baseline freeze 이후로 보류.
- publication-grade 기준 유지: physics/trap/geometry/convergence criterion을 일정 때문에 임의 완화하지 않음.

## 2026-10-06 — Deadline-aware publication-grade simulation strategy

- 작업자: 이택규
- 상태: DECISION / RESEARCH STRATEGY
- 사용자 요구: 결과는 논문에 사용할 수 있을 정도로 수치적으로 타당해야 하지만, 전체 연구 일정도 맞춰야 함.
- 결정:
  1. publication-grade reference/final cases와 screening cases를 분리한다.
  2. Common Baseline 및 최종 대표 A/B case는 full validation(0–5 V, same physics, mesh/convergence checks)으로 유지한다.
  3. broad parameter exploration은 operating-current/bias window 중심의 reduced-window screening으로 수행한다.
  4. screening winner/representative/worst case만 full 0–5 V로 최종 검증한다.
  5. C1 Iterations=15은 numerical-only candidate로 유지; full-range equivalence validation 후에만 baseline freeze.
  6. RHSMin 완화 같은 convergence-criterion 변경은 publication baseline에 바로 적용하지 않는다. 별도 sensitivity/convergence study로 결과 불변성이 입증될 때만 고려한다.
  7. 우선순위 높은 시간 단축 수단: parallel independent runs, staged bias schedule, thread benchmark, checkpoint/restart, mesh coarsening only after mesh-convergence evidence.
- 논문 방어 원칙:
  - physics/geometry/trap model을 runtime 때문에 임의 완화하지 않는다.
  - numerical acceleration은 reference와 I–V/Vf/spatial metrics equivalence를 검증한다.
  - 최종 논문 figures/tables는 validated runs에서만 생성한다.
- 현재 실행:
  - FAST_C1 Node 6은 C1 full-reference evidence로 유지.
  - Node 12는 자원 확인 후 separate clean project에서 병렬 실행 고려.
  - A/B full brute-force sweep은 하지 않는다.

## 2026-10-06 — FAST_C1 Node 6 confirmed progressing after 41 h 05 min wall time

- 작업자: 이택규
- 상태: OBSERVED / RUNTIME
- direct process evidence at 2026-10-06 08:51 KST:
  - sdevice PID 69457
  - ELAPSED = 1-17:05:26 (~41 h 05 min wall time)
  - CPU = 280%, consistent with multithreaded activity
  - process state SNl
- n6_des.out modification time = 2026-10-06 08:51:49 KST, proving the log was actively updating.
- recent accepted pseudo-time advanced to at least ~0.936443; current attempted endpoint ~0.936458.
- mapped anode bias remains ~4.682 V.
- C1 cap is active: repeated '#iterations larger than 15.'
- recent successful attempts still converge in ~21 s with 2–3 Newton iterations, but occasional attempts sit just above RHSMin and run toward the 15-iteration cap.
- high-bias timestep remains ~7e-6 to 1.45e-5 pseudo-time, so the remaining ~0.318 V can still take a long time.
- conclusion: Node 6 is not hung; current blocker is high-bias timestep collapse, not process death.
- planning implication: two-node sequential completion can plausibly take multiple additional days; Node 12 runtime cannot be assumed equal without evidence and may be similar or worse.
- do not launch broad A/B full-sweep brute force from this runtime pattern.

## 2026-10-06 — FAST_C1 Node 6 confirmed alive at ~4.682 V; Iterations=15 active

- 작업자: 이택규
- 상태: OBSERVED / RUNTIME EVIDENCE
- process evidence:
  - gsub PID 69166
  - gjob PID 69396
  - sdevice PID 69457 at ~99% CPU
  - FAST_C1 project path confirmed
- `n6_des.out` timestamp observed: 2026-10-06 08:49 KST, size ~3.5 MB.
- latest accepted pseudo-time observed: approximately 0.936405.
- 0→5 V ramp mapping gives latest accepted anode target ≈ 4.682025 V; current attempted step to 0.936419 corresponds ≈ 4.682095 V.
- solver output directly shows anode voltage 4.682E+00 V on recent accepted steps.
- C1 cap is definitely active: repeated `#iterations larger than 15.` followed by timestep retry.
- recent accepted steps converge in 2–3 Newton iterations and ~21–22 s wallclock.
- current difficult attempt at 0.936405→0.936419 reached iteration 14 with RHS ~1.03e-3, just above RHSMin=1e-3; likely near rejection unless the next iteration converges.
- recent timestep scale is ~7.8e-6 to 1.6e-5 pseudo-time, showing severe high-bias timestep contraction.
- interpretation:
  - run is NOT hung at the captured time.
  - C1 successfully removes the old 50-iteration cap behavior, but the dominant remaining bottleneck is now very small high-bias timesteps and repeated 15-iteration rejections.
  - latest accepted bias exceeds the prior copied x8 audit endpoint (~4.643 V) by ~39 mV.
- remaining voltage from 4.682025 V to 5.0 V is ~0.317975 V.
- do not estimate finish time from full-run average; high-bias tail is strongly nonlinear.
- next: quantify recent progress rate over a longer fixed window (e.g. 30–60 min of log) and count accepted/rejected attempts to estimate remaining runtime more defensibly.

## 2026-10-06 — FAST_C1 Node 6 still unfinished after ~41 h 48 min

- 작업자: 이택규
- 상태: USER-REPORTED / RUNTIME BLOCKER
- FAST_C1 Node 6 recorded start: 2026-10-04 15:46 KST.
- Current checked time: 2026-10-06 09:34 KST.
- Elapsed since recorded start: approximately 41 h 48 min.
- User reports that no node has completed yet.
- For comparison, the historical NtSide=0 run completed in ~65.4 h; current elapsed time is already ~64% of that historical full-run wallclock.
- The prior ~2.11x C1 speedup number was an idealized estimate from the observed x8 path, not a completion-time prediction; the current run has not yet demonstrated that speedup.
- This observation alone does not distinguish slow progress from a stall. Do not infer hang/failure without current n6_des.out/process evidence.
- Next: read current FAST_C1 n6_des.out tail + process state, determine latest pseudo-time/anode voltage, confirm rejected attempts cap at 15, and measure progress rate before deciding whether to continue/stop.
- Research strategy remains staged: do not plan brute-force full 0→5 V for every Project A/B parameter point.

# 2026-10-04 — FAST_C1 exact source install PASS

- exact C1 source SHA-256 f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93 confirmed in separate FAST_C1 project.
- golden backup preserved.
- next: inspect copied Workbench status metadata, then preprocess only.
- no SDevice solve yet; live x6/x7/x8 untouched.

---

# 2026-10-04 — B0 COMPLETE; FAST C1 ready for preprocess

- updated Stepsize-based x8 CSV verified all 285 retry/rejection pairs.
- retry_dt / rejected_dt: min 0.499975805, max 0.500023337, mean 0.499999621.
- cutback factor = 0.5 to log-print precision.
- B0 is closed.
- C1 unchanged: Iterations=15, source SHA-256 f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93.
- next: separate FAST C1 project/copy -> source hash -> preprocess gate -> NtSide=0 B1.
- live x6/x7/x8 untouched.

---

# 2026-10-04 — Claude B0 review: C1 unchanged, A1'/A1'' added

- C1 source unchanged: SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`; `Iterations=15`.
- correction: ~4.33 V is the first rejected attempt where Newton count changes 50->15, not a trajectory divergence.
- A1': accepted-step sequence + rejection points should match over the observed overlap; unexplained mismatch = UNEXPECTED.
- A1'': every C1 rejection must show `#iterations larger than 15.`; 50 means cap not applied -> stop.
- A3/A4: printed-precision identity expected on observed overlap; 1e-3 / 1 mV are outer limits.
- new audit tool SHA-256 `9a935633e92bc55fa86849b6988b60a8a8ee55f637387ced62721d9f6267d281`; synthetic selftest passed.
- observed raw retry/rejected dt examples are ~0.5; full 285-event CSV ratio verification remains pending because the CSV was not included in the review package.
- patch-equivalent commit: `ace056fcb01d2e6e785dbee08a213e1148d6be35`.
- next: separate FAST C1 preprocess gate, then NtSide=0 B1 benchmark; live x6/x7/x8 untouched.

---

# 2026-10-04 — B0 PASS for C1 Iterations=15

- 1950 accepted x8 attempts, accepted max Newton=4.
- 285 rejected attempts, all 50 iterations.
- N=15 false_rej=0 through observed x8 progress (~4.643 V).
- rejected attempt wallclock fraction ~75%; idealized observed-path speedup estimate ~2.11x.
- next: separate FAST C1 preprocess gate -> NtSide=0 benchmark.
- live x6/x7/x8 untouched.

---

# 2026-10-04 — B0 parser patched for actual BE-step log format

- real T-2022.03 x8 step syntax identified and parser patched.
- next: re-download tool and rerun B0 audit; Iterations=15 remains unconfirmed until real accepted-step distribution is parsed.

---

# 2026-10-04 — B0-1 passed: no explicit transient Iterations in x8 pp6

- observed x8 pp6_des.cmd:
  - RHSMin=1e-3
  - CheckRhsAfterUpdate
  - Iterations=500 (initial Poisson)
  - Iterations=100 (equilibrium)
  - no transient Iterations
  - no NotDamped
- remaining blocker: interpret raw x8 n6_des.out and accepted/rejected Newton iteration distribution before confirming C1 Iterations=15.

---

# 2026-10-04 — FAST C1 reviewed; B0 audit required

- Claude C1 SHA: `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`
- golden Copy x8 SHA: `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`
- executable change: transient inner Coupled `Iterations=15` only
- C1 and prior ChatGPT v0.1 are executable-statement equivalent
- status: PROPOSED / REVIEWED / NOT EXECUTED
- blocker: B0 must resolve documented default 20 vs project-recorded ~50-iteration failures and verify no accepted x8 step needs >15
- Claude tools are synthetic-tested only; actual x8 format validation pending
- live x6/x7/x8 remain untouched
- guide: `CMP/FAST_BASELINE_C1.md`

---

# 2026-10-04 sequence correction — FAST coding starts now

Copy x8 golden reference has been frozen. The next task is to build a separate numerical-only FAST_BASELINE and benchmark the first solver change against Copy x8.

Clean-account reproduction remains mandatory before final FAST baseline freeze / Project A-B production, but it is not a blocker for writing and short-benchmarking the FAST code.

Priority:
1. obtain/use exact Copy x8 editable source
2. create separate FAST_BASELINE
3. first candidate = Newton iteration/cutback policy only
4. short benchmark against Copy x8
5. accept/reject by runtime + physical/numerical equivalence
6. reproduce the accepted FAST deck on both accounts before production

---

# 2026-10-04 Copy x8 golden reference frozen

Golden local snapshot completed and core hashes fixed.

- n1_msh.tdr: 762d2d57a352a00bb030b968985cbf3b71d53118c68e5c53b7586e613f392ea3
- pp1_dvs.cmd: 5685528bc3ec338ce104040b0503be43ef032094976d69995529eb5d6fb4e658
- pp6_des.cmd: 2dfcc98effe145ec944fb8ee5d6914f5f098e54d1bf2319c69acc76afe1692e6
- pp6_des.par: 60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039
- sd_fdiv_des.cmd: 56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c

Immediate next task: reproduce preprocessing in Lee Taek Gyu clean account before any full FAST solve.

---

# 2026-10-04 FAST baseline handoff

**Current task:** freeze Copy x8 as the golden local reference, then reproduce preprocessing in Lee Taek Gyu's clean account before any full FAST solve.

**Newest confirmed repository action:**
- `CMP/FAST_BASELINE_REPRO_PROTOCOL.md` added.
- `CMP/tcad/capture_reference_snapshot.sh` added.
- Public GitHub `CMP/tcad/CURRENT` is still not the authoritative Copy x8 running source.

**Immediate blocker:**
Existing local reference package `~/CMP_REFERENCE_20261004.tgz` is recorded as missing the exact editable SDevice source `sd_fdiv_des.cmd`. This source must be added locally and hashed before clean-account reproduction.

**Next:**
1. Complete Copy x8 local snapshot with exact source.
2. Generate SHA-256 manifest.
3. In clean account, preprocess only / early initialization.
4. Diff `pp1_dvs.cmd`, `pp6_des.cmd`, `pp6_des.par`; compare mesh hash/statistics.
5. Only after reproducibility gate passes, create numerical-only FAST branch.

**Do not change:** Common Baseline geometry, Nt/Et/sigma, 5 nm sidewall damage width, common A/B physics.

---

## 2026-09-29 — JuSubin active run direct evidence: Node 6 alive, high-bias convergence slowdown

- Direct file evidence: active output is `n6_des.out` (Node 6), superseding the earlier Node-19 inference.
- pseudo-time ≈0.93254, equivalent to ≈4.66 V on the known 0→5 V transient ramp.
- A BE step exceeded 50 Newton iterations, was rejected, then automatically retried with a smaller timestep (~8.67e-06).
- One failed attempt cost ~1244 s wallclock, dominated by solve time (~999 s).
- Status: RUNNING, not hung at the captured moment; repeated high-bias cutbacks are the present runtime bottleneck.
- Next check: confirm continued pseudo-time advance and timestep recovery before considering any restart or solver change.

## 2026-09-29 — JuSubin 3-day Workbench status screenshot

- OBSERVED: selected upper SDevice node reports `Status: waiting`; it has not started solving.
- Lower branch Node 19 appears running in Workbench, but actual solver progress is not proven from topology alone.
- Runtime blocker is now split into (1) scheduler/resource waiting for one branch and (2) unknown progress/hang status for the active branch.
- Next evidence: Node 19 Job Log + last lines/timestamps of `n19_des.out`.
- Do not abort/restart or modify baseline physics solely from this screenshot.

# LIVE AI STATE

## 2026-09-28 — CRITICAL SOURCE SYNC GAP FOUND

- GitHub Issue #7 and JuSubin timeline contain Final SDevice v1.2 progress.
- Actual `CMP/tcad/CURRENT/sdevice2_defect_on.cmd` is still an older stale deck and does NOT contain the v1.2 intermediate TDR save workflow.
- Gmail notifications are GitHub Issue #7 notifications and are consistent with the logged progress; they do not prove the actual code file was synchronized.
- Do NOT overwrite CURRENT from snippets or memory.
- Blocker: recover exact full user-provided Final SDevice v1.1/v1.2 source, then synchronize it.
- Current final-code provenance is therefore UNRESOLVED until that exact source is committed.



## 2026-09-26 — deadline mode

- User needs baseline + PPT today.
- Full 5 V NtSide=1e18 completion is not expected today based on historical multi-day runtime.
- Today deliverable: source/parameter freeze, clean preprocess comparison, successful trap-on initialization/early solve, and presentation-ready baseline evidence.
- Full same-revision NtSide=0 vs 1e18 electrical comparison remains pending and must not be presented as completed.


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


## 2026-10-06 — FAST_C2 half-domain / selective-mesh direction accepted

- 작업자: 이택규
- 상태: DECISION / IMPLEMENTATION CANDIDATE
- user accepted a runtime-optimization branch using half-domain symmetry plus localized fine mesh.
- keep current Node 6/12 full-device runs as reference evidence.
- candidate only: half-domain is allowed only after confirming left-right symmetry of geometry, doping, contacts, traps and BCs in the actual SDE source.
- preserve fine resolution at the 5 nm sidewall-damage region and other solution-critical interfaces/high-field zones; coarsen only remote homogeneous bulk with graded transitions.
- publication gate: compare against full/fine reference at identical physics/bias, including current normalization and key spatial metrics, before adopting.
- immediate next step: recover/inspect exact running SDE source, then create separate FAST_C2 short benchmark.


## 2026-10-06 — Project B compatible with half-domain, but center active region remains mesh-critical

- Project B symmetric AlBarrier_L/R concept is compatible with half-domain if the actual SDE/contact/BC setup is mirror-symmetric.
- do not remove mesh from the retained center domain; only coarsen remote homogeneous bulk.
- Project B requires additional refinement at GaN/AlGaN lateral interfaces and barrier/MQW intersections, while the center MQW must remain adequately resolved for radiative/current-crowding metrics.
- adoption still gated by full/fine equivalence validation.


## 2026-10-06 — A/B half-domain + selective mesh formally recommended as validated candidate

- 작업자: 이택규
- 상태: REVIEWED / RECOMMENDED CANDIDATE
- A/B 모두 mirror symmetry가 actual SDE/contact/BC에서 확인되면 half-domain 적용 가능.
- retained center domain의 mesh는 제거하지 않고 remote homogeneous bulk만 graded coarsening.
- common fine zones: 5 nm sidewall damage, MQW, junction/heterointerfaces, high-field/depletion/contact edges.
- A-specific: refine Cedge/GaN:C boundary.
- B-specific: refine lateral AlGaN/GaN interface and barrier-MQW intersections; B has stricter interface-mesh need because band offsets/fields are primary mechanism.
- final adoption requires full/fine equivalence validation; current Node 6/12 reference runs remain preserved.


## 2026-10-06 — Half-domain preserves IQE ratio under mirror symmetry

- current CMP IQE metric: integrated Rrad / (Rrad + RSRH + RAuger) over an identical physical integration region.
- for an exactly mirror-symmetric device, each full-domain integrated recombination term is twice the half-domain term, so the factor of 2 cancels in IQE.
- half-domain is therefore valid for IQE comparison, provided symmetry and identical integration-region definitions hold.
- do not multiply IQE by 2; only absolute total current/recombination/power may require full-device symmetry scaling/2D normalization checks.


## 2026-10-06 — Recommended baseline strategy: physical 4 µm device, validated half-domain production model

- physical Common Baseline remains a 4.0 µm mesa.
- recommended computational representation, after validation: simulate only the 2.0 µm half-domain with centerline symmetry.
- retain full/fine runs as reference evidence; do not delete the full model from the methodology.
- validate symmetry-only change before mesh coarsening, then use the same validated half-domain mesh policy for Baseline/A/B production comparisons.
- IQE is compatible with the half-domain under exact symmetry; absolute totals still need normalization/symmetry scaling checks.
