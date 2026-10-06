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

## 2026-10-04 — Runtime strategy re-evaluation: do not brute-force full 0–5 V for every A/B case

- 작업자: 이택규
- 상태: DECISION / PROPOSED IMPLEMENTATION
- 냉정한 재평가 결과, 모든 baseline/A/B parameter case를 동일한 0→5 V full sweep으로 순차 실행하는 방식은 총 연구시간 관점에서 비효율적임.
- validation scope는 유지하되 계산 전략을 staged 방식으로 변경한다.
- 즉시 수정:
  - 현재 FAST_C1 Node 6은 이미 실제 SDevice solve 중이고 generated pp6_des.cmd/par가 존재함.
  - 먼저 running 상태에서 read-only preprocess equivalence gate를 수행한다.
  - gate PASS이면 현재 진행분을 버리지 않고 B1 run으로 계속 인정한다.
  - gate FAIL일 때만 FAST_C1 Node 6을 중지한다.
- production 전략:
  1. numerical FAST validation용 full reference sweep는 소수의 대표 case에만 수행.
  2. Project A/B parameter screening은 실제 연구 지표가 필요한 operating-current/bias window를 먼저 정의한 후 그 구간 중심으로 수행.
  3. screening winner/representative/worst case만 full 0→5 V sweep으로 최종 검증.
  4. independent parameter points는 가능한 자원 범위에서 병렬화.
  5. future long runs에는 loadable Save checkpoint를 별도 검토하여 crash/restart 손실을 줄인다. 현재 x8 intermediate Plot은 `-Loadable`이라 restart checkpoint가 아님.
- 근거:
  - x8 B0에서 rejected attempts가 관측 attempt wallclock의 약 75%를 차지했고, high-bias가 주요 병목.
  - Sentaurus 공식 training은 ramped solve에서 Newton 15–20회 이후에는 timestep을 줄이는 편이 더 효율적일 수 있다고 설명함.
- 이 전략은 physics/validation을 생략하는 것이 아니라, screening과 final validation을 분리하는 방식임.

## 2026-10-04 — Runtime planning implication for Project A/B

- 작업자: 이택규
- 연구 판단: FAST common baseline optimization은 단순 baseline 편의가 아니라 이후 Project A/B parameter study의 총 계산시간을 줄이기 위한 필수 단계.
- Project A의 localized GaN:C high-resistance 영역은 carrier transport를 더 강하게 제한하고 수치 stiffness/cutback을 증가시킬 수 있어 baseline보다 느려질 가능성이 있음. 단, 실제 slowdown magnitude는 아직 미측정이며 추측하지 않음.
- 따라서 production A/B sweep 전에 representative single-case pilot를 먼저 실행해 runtime/convergence를 측정하고, 그 결과로 parameter grid/parallelization 계획을 확정해야 함.
- baseline C1 검증 후 동일 numerical framework를 A/B에 유지하고, physics shortcut 대신 numerical efficiency + independent parallel runs로 시간을 단축한다.

## 2026-10-04 — FAST C1 baseline acceptance sequence clarified

- 작업자: 이택규
- 연구 판단: FAST_C1은 단순히 Node 6/12가 완주했다는 이유만으로 baseline으로 확정하지 않는다.
- 최종 공통 baseline은 두 조건을 포함한다:
  - NtSide=0: defect-free control
  - NtSide=1e18: nominal sidewall-defect baseline
- acceptance sequence:
  1. FAST_C1 preprocess equivalence gate PASS.
  2. NtSide=0 B1 run: golden x8 overlap에서 accepted/rejected trajectory, Iterations=15 적용, I-V/Vf/출력 등가성 검증.
  3. NtSide=1e18 run: 동일한 C1 source/mesh/physics 유지, trap concentration만 1e18로 변경되었는지 확인하고 완주/물리 sanity 검증.
  4. 두 조건이 모두 통과하면 FAST_C1을 Project A/B 공통 baseline numerical implementation으로 freeze.
- Project A/B는 이후 이 frozen common baseline 위에서 각각 GaN:C high-resistance 영역과 AlGaN barrier를 추가한다.

## 2026-10-04 — FAST_C1 Node 6 solve accidentally launched before preprocess gate

- 작업자: 이택규
- 상태: OBSERVED / BLOCKER
- process check shows FAST_C1 Node 6 was actually launched, not preprocess-only:
  - gsub PID 69166: `-e 6 .../GaN_PiN_Diode_FAST_C1`
  - gjob PID 69396
  - sdevice PID 69457: `sdevice --max_threads 4 pp6_des.cmd`
  - start time 15:46, active at ~99% CPU.
- therefore the ~3 h delay is real SDevice solve runtime, not preprocess delay.
- since SDevice is running from `pp6_des.cmd`, preprocessing has already produced the generated deck.
- this run began before the mandatory preprocess equivalence gate, so it must not be accepted as B1 evidence unless the generated deck is validated.
- immediate action: stop only the FAST_C1 Node 6 job via Workbench (do not kill unrelated jobs), then audit `pp6_des.cmd/par` before any restart.
- the current process list showed no other user-owned x8 gsub/sdevice process; user had reported stopping other runs.

## 2026-10-04 — FAST_C1 preprocess appears stalled >3 h

- 작업자: 이택규
- 상태: USER-REPORTED / BLOCKER
- 사용자가 FAST_C1 단계가 약 3시간째 완료되지 않았다고 보고함.
- preprocess-only라면 비정상적으로 긴 시간이며, 실제 SDevice solve가 시작되었거나 Workbench 상태/queue 문제일 가능성 확인 필요.
- 아직 원인 확정 전. 임의 종료하지 말고 프로세스와 최근 로그를 먼저 확인한다.

## 2026-10-04 — FAST_C1 copied .status ownership resolved

- 작업자: 이택규
- 상태: OBSERVED / RESOLVED
- FAST_C1 `.status`에 남아 있던 PID 78941을 `/proc/78941/cwd`와 cmdline으로 확인함.
- PID 78941의 실제 cwd와 gsub 대상은 원래 live Copy x8:
  `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_Copy_Copy_Copy_Copy_Copy_Copy_Copy_Copy`
- 따라서 FAST_C1의 `.status`는 Save As 과정에서 복사된 stale metadata이고, live process ownership은 x8에 있음.
- PID 78941은 절대 종료/수정하지 않음.
- FAST_C1 source는 exact C1 SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`.
- 다음: Workbench에서 FAST_C1 프로젝트만 열고 Node 6(NtSide=0)을 preprocess-only. SDevice solve는 시작하지 않음.

## 2026-10-04 — FAST_C1 exact source installation PASS

- 작업자: 이택규
- 상태: OBSERVED / SOURCE-INSTALL PASS
- separate project: `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1`
- exact patch applied successfully to `sd_fdiv_des.cmd`.
- resulting SHA-256:
  `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`
- this matches the canonical Claude C1 source hash exactly.
- golden backup remains `sd_fdiv_des.cmd.golden_x8`.
- live x6/x7/x8 untouched.
- next: inspect copied Workbench node/status metadata before preprocess; do not launch SDevice yet.

## 2026-10-04 — FAST_C1 patch dry-run PASS

- 작업자: 이택규
- 상태: OBSERVED
- separate FAST_C1 directory에서 `patch --dry-run -p0 < ~/CMP_B0/FAST_C1_exact_source.patch` 실행.
- 출력: `checking file sd_fdiv_des.cmd`; reject/error 없음.
- 아직 실제 patch 적용 전.
- 다음: actual patch apply 후 `sd_fdiv_des.cmd` SHA-256이 exact C1 hash와 일치하는지 확인.

## 2026-10-04 — B0 cutback-rule validation CLOSED

- 작업자: 이택규
- 상태: OBSERVED / B0 COMPLETE
- regenerated x8 CSV with the updated audit tool using explicit `Stepsize`.
- all 285 rejection/retry pairs were checked.
- `retry_dt / rejected_dt`:
  - pairs = 285
  - min = 0.499975805
  - max = 0.500023337
  - mean = 0.499999621
- interpretation: the retry timestep is effectively exactly 0.5 of the rejected timestep; remaining spread is consistent with printed Stepsize precision.
- this closes the B0 assumption that the transient cutback factor is independent of whether the rejected Newton attempt ran to 50 or is capped at 15.
- therefore C1 should preserve the x8 rejection points/accepted-step trajectory over the observed overlap; only the rejected-attempt Newton count changes 50 -> 15.
- C1 source remains unchanged: SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`, `Iterations=15`.
- next: separate FAST C1 Workbench project/copy -> source hash -> preprocess gate.
- live x6/x7/x8 untouched.

## 2026-10-04 — Old B0 CSV ratio spread is a rounding artifact, not a physics/cutback result

- 작업자: 이택규
- 상태: OBSERVED / VALIDATION PENDING
- old CSV ratio check over all 285 rejection/retry pairs: min 0.47826087, max 0.52173913, mean 0.499405569.
- old audit CSV computed dt from rounded t0/t1, so these values cannot be used to test whether the cutback factor is constant.
- updated Claude audit tool reads the explicit `Stepsize` field and must regenerate the CSV before the cutback-ratio assumption is closed.
- existing raw log examples using printed Stepsize are ~0.5.
- C1 `Iterations=15` decision is unchanged; this affects only the auxiliary validation of the timestep-reduction rule.

## 2026-10-04 — Full CSV cutback-ratio check exposed old-dt rounding artifact

- 작업자: 이택규
- 상태: OBSERVED / TOOLING INTERPRETATION
- old B0 CSV ratio check across all 285 rejection/retry pairs returned:
  - pairs = 285
  - min = 0.47826087
  - max = 0.52173913
  - mean = 0.499405569
- This CSV was produced by the older audit parser whose `dt` was computed from printed `t1-t0`.
- T-2022.03 prints t0/t1 with limited decimal precision, so small high-bias timesteps are distorted when subtracting the rounded endpoints.
- Therefore the 0.478–0.522 spread is **not valid evidence that the cutback factor varies**.
- Claude's updated audit tool specifically fixes this by reading the explicit `(Stepsize: ... s)` value from each log line.
- Existing raw examples using printed Stepsize show exact/near-exact 0.5 cutback.
- Next: regenerate x8_attempts.csv with the updated audit tool and repeat the 285-pair ratio check using the explicit Stepsize-derived dt.

## 2026-10-04 — Claude B0 review accepted; C1 source unchanged

- 작업자: 이택규
- 상태: PROPOSED / CLAUDE-REVIEWED / READY FOR SEPARATE PREPROCESS
- Claude review package verified:
  - C1 source unchanged
  - C1 SHA-256 = `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`
  - `Iterations = 15` retained
- B0 interpretation correction accepted:
  - ~4.33 V is **not** a trajectory divergence.
  - It is the first observed rejected attempt where the Newton count is expected to differ: x8 50 -> C1 15.
  - Over the overlapping observed path, C1 is expected to preserve the accepted-step sequence and rejection points; any unexplained mismatch is UNEXPECTED and must be investigated.
- Acceptance additions:
  - A1': accepted steps (t0,t1,Newton count) + rejection points (t0,dt) should match over the overlap.
  - A1'': every C1 rejected attempt must report `#iterations larger than 15.`; seeing 50 means the cap did not apply and the run must stop.
  - A3/A4: identical-to-printed-precision is the expectation on the observed overlap; 1e-3 / 1 mV remain outer limits, not automatic acceptance bands.
- Updated audit tool package SHA-256:
  - `9a935633e92bc55fa86849b6988b60a8a8ee55f637387ced62721d9f6267d281`
  - package selftest independently rerun by ChatGPT and passed.
- Cutback-ratio evidence:
  - actual x8 excerpts already observed show retry/rejected dt ratios approximately 0.5 (e.g. 2.2968e-05->1.1484e-05, 2.3813e-05->1.1907e-05, 2.4690e-05->1.2345e-05).
  - the full B0 CSV itself was not included in the Claude review ZIP, so constancy across all 285 rejections is still **PENDING FULL-CSV VERIFICATION**.
- Patch-equivalent review changes applied at commit `ace056fcb01d2e6e785dbee08a213e1148d6be35`.
- live x6/x7/x8 remain untouched.

## 2026-10-04 — FAST C1 cleared by B0 for separate-project benchmark

- 작업자: 이택규
- 상태: PROPOSED / B0-PASSED / NOT YET EXECUTED
- raw Copy x8 audit: 1950 accepted steps, max accepted Newton iterations = 4; 285 rejected attempts, each reaching 50 iterations.
- N=15 false rejection count on observed x8 trajectory = 0.
- raw log confirms effective failed-attempt cap behavior of >50 iterations even though transient inner Coupled has no explicit Iterations in pp6_des.cmd.
- rejected attempts account for ~75% of observed attempt wallclock; under the observed fixed-cutback pattern and approximately uniform per-iteration cost, N=15 predicts ~2.1x speedup over the observed path.
- B0 evidence currently covers x8 only to ~4.643 V.
- next: create/preprocess separate FAST C1 project, run preprocess gate, then NtSide=0 benchmark. Keep live x6/x7/x8 untouched.
- C1 remains PROPOSED until execution/equivalence checks pass.

## 2026-10-04 — Real T-2022.03 BE-step syntax identified; B0 parser patched

- 작업자: 이택규
- 상태: OBSERVED / TOOL FIXED
- real x8 log uses:
  - `Computing BE-step from <t0> s to <t1> s (Stepsize: <dt> s)`
  - `Iteration |Rhs| factor |step| error #inner #iterative time`
  - rejected attempt message: `Newton didn't converge, trying again with smaller timestep...`
  - accepted attempt message: `|RHS| less than 1.0000E-03.`
- repeated retry at the same t0 with a smaller dt is directly visible, validating the high-level accepted/rejected classification rule.
- `CMP/tcad/tools/sdevice_newton_audit.py` patched to recognize the actual T-2022.03 BE-step start format while preserving the previous synthetic format.
- B0 statistics must be rerun with the updated parser before any Iterations=15 decision.

## 2026-10-04 — B0-1: Copy x8 preprocessed Iterations check

- 작업자: 이택규
- 상태: OBSERVED
- active Copy x8 `pp6_des.cmd`에서:
  - `RHSMin = 1e-3`
  - `CheckRhsAfterUpdate`
  - `Iterations = 500` (initial Poisson)
  - `Iterations = 100` (equilibrium Coupled)
  - transient inner Coupled에 explicit `Iterations` 없음
  - `NotDamped` 없음
- 따라서 프로젝트 기록의 ~50-row/iteration failure는 preprocessed deck에 명시된 `Iterations=50` 때문이 아님.
- 다음: exact x8 `n6_des.out` raw audit으로 50의 의미를 확인하고 accepted-step iteration 분포를 측정.

## 2026-10-04 — FAST_BASELINE C1 reviewed; B0 required before execution

- 작업자: 이택규
- 상태: PROPOSED / REVIEWED / NOT EXECUTED
- Claude C1 golden/FAST hashes verified.
- executable change vs Copy x8: transient inner `Coupled` only → `Iterations=15`.
- C1 and prior ChatGPT FAST v0.1 are executable-statement equivalent; C1 is now the canonical provenance candidate.
- Synopsys 2022 training documents default 20 Newton iterations for ramped solves and recommends roughly 15–20 before timestep reduction. This supports 15 as a first candidate but conflicts with the project record of ~50-iteration failed attempts.
- Current blocker: B0 read-only audit of exact x8 `pp6_des.cmd` and raw `n6_des.out` to resolve the 20-vs-50 discrepancy, verify parser correctness, and ensure no accepted x8 step needs >15.
- Do not launch C1 until B0 passes.
- live Copy x6/x7/x8 remain untouched.
- reviewed record: `CMP/FAST_BASELINE_C1.md`.

## 2026-10-04 — Current Copy x8 Node12 pending location narrowed to Workbench/gsub dispatch queue

- 작업자: 이택규
- 상태: OBSERVED / NARROWED
- Current Copy x8 gexec.cmd:
  - Node6: `job 6 -d "1" ... sdevice pp6_des.cmd`
  - Node12: `job 12 -d "1" ... sdevice pp12_des.cmd`
  - therefore both depend on Node1 and Node12 does not depend on Node6 at graph level.
- Current Node12 status: `pending`, `local:-1`.
- No current `n12_des.job` exists.
- No current Node12 `gjob` or `sdevice` process exists.
- Sep26 n12 out/log/err/local.err are stale historical artifacts.
- Current x8 gsub0 process was launched with `-q local:default -e remaining`, while only Node6 has been dispatched to gjob/sdevice.
- Three separate project copies currently each have one active Node6 SDevice process.
- Therefore current Node12 is waiting before SDevice launch, inside Workbench/gsub scheduling/dispatch, not failing inside the current SDevice deck.
- Most plausible explanation is local queue/resource/concurrency serialization while three SDevice jobs are already active, but exact queue limit is not yet proven.
- If immediate Node12 execution is desired, first retire one duplicate active run (prefer x7), then observe whether x8 gsub dispatches Node12 automatically. If not, inspect Workbench local queue/concurrency settings before manually relaunching.


## 2026-10-04 — Why Node12 is not running: separate old solver failure from current pending state

- 작업자: 이택규
- 상태: CONFIRMED BOUNDARY
- Two different events must not be conflated.
1. OLD Sep26 Node12 execution:
   - actually launched and terminated during SDevice initialization.
   - logs show Mg incomplete-ionization parameter mismatch in InGaN while global/species ionization handling was active.
   - this is the historical solver-initialization failure.
2. CURRENT Sep28 Copy x8 Node12:
   - pp12_des.cmd/par were freshly preprocessed at Sep28 18:43.
   - n12_des.sta = pending, local:-1.
   - there is no current n12 gjob/sdevice process and no current Sep28 n12 output/log.
   - gexec.cmd shows Node12 depends only on Node1, not on Node6.
   - therefore the current Node12 has not failed in SDevice; it has not been launched yet.
- Current cause of pending is outside the SDevice numerical solve. Possible causes include Workbench launch selection / project execution policy / job concurrency-resource scheduling, but the exact scheduler reason is not proven by the captured package.
- Three separate project copies currently consume active SDevice jobs on the same account/host, so resource/concurrency pressure is plausible, but not yet proven as the exact pending cause.
- Do not attribute current Node12 pending to the stale Sep26 Mg error.


## 2026-10-04 — Golden baseline pair confirmed at preprocess level

- 작업자: 이택규
- 상태: CONFIRMED
- Copy x8 current preprocess:
  - Node 6 = NtSide 0 control
  - Node 12 = NtSide 1e18 damaged branch
- pp6_des.par SHA256 = 60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039
- pp12_des.par SHA256 = 60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039
- diff pp6_des.par vs pp12_des.par = no differences.
- Current pp6_des.cmd vs pp12_des.cmd differences are node-specific filenames/intermediate-output prefix plus trap Conc 0 -> 1e18 in the intended sidewall trap regions; no parameter-file difference.
- Therefore the current Copy x8 Node6/Node12 pair is a valid NtSide-only validation pair at preprocess/parameter level.
- Important: current Node12 remains pending; current Sep28 pp12 has not yet been executed. Sep26 Node12 failure logs are stale and must not be used to judge this pair.
- Next:
  1. re-upload the refreshed CMP_REFERENCE_20261004.tgz containing pp12 files/diffs/timestamps;
  2. sync exact reference bundle metadata and safe source files to GitHub;
  3. generate Claude FAST_BASELINE prompt against this exact pair;
  4. require clean-account preprocess/hash equivalence before any multi-day full run.


## 2026-10-04 — Copy x8 Node12 current preprocess is NtSide-only pair; visible Node12 failure logs are stale

- 작업자: 이택규
- 상태: CONFIRMED
- Evidence from current Copy x8 directory:
  - pp6_des.cmd timestamp: 2026-09-28 18:43
  - pp12_des.cmd / pp12_des.par timestamp: 2026-09-28 18:43
  - n12_des.out / log / err timestamp: 2026-09-26 14:24
  - n12_des.sta: pending, local -1
- Exact diff pp6_des.cmd vs pp12_des.cmd shows:
  - node-specific Parameters/Plot/Current/Output filenames
  - trap Conc 0 -> 1e18 in all intended sidewall regions
  - intermediate FilePrefix n6_inter -> n12_inter
  - no shown Physics/Math/Solve differences in the captured diff
- Therefore the current Copy x8 Node6/Node12 command pair is consistent with an NtSide-only validation pair at cmd level.
- Critical provenance correction:
  - the visible Node12 Mg-incomplete-ionization failure logs are from Sep26 and do NOT correspond to the current Sep28 pp12_des.cmd/par.
  - current Node12 has not yet executed; status is pending.
- Do not use stale n12 logs to judge the current v1.2 Node12 deck.
- Next discriminator:
  1. exact SHA/diff pp6_des.par vs pp12_des.par
  2. if identical, current Node12 should be launched in a clean execution context and initialization checked before full run.
  3. clean-account reproduction must avoid inheriting stale outputs from copied Workbench directories.


## 2026-10-04 — Copy x8 exact reference package audited: active Node 6 is NtSide=0 control, not nominal damaged baseline

- 작업자: 이택규
- 상태: CONFIRMED FROM UPLOADED ACTIVE PACKAGE
- 근거: user-uploaded `CMP_REFERENCE_20261004.tgz` extracted and inspected.
- Exact hashes:
  - sd_fdiv_des.cmd: `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`
  - pp1_dvs.cmd: `5685528bc3ec338ce104040b0503be43ef032094976d69995529eb5d6fb4e658`
  - pp6_des.cmd: `2dfcc98effe145ec944fb8ee5d6914f5f098e54d1bf2319c69acc76afe1692e6`
  - pp6_des.par: `60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039`
  - n1_msh.tdr reference hash: `762d2d57a352a00bb030b968985cbf3b71d53118c68e5c53b7586e613f392ea3`
- Critical correction:
  - gtree.dat maps Node 6 to NtSide=0 and Node 12 to NtSide=1e18.
  - pp6_des.cmd contains `Conc = 0` in all sidewall trap regions.
  - Therefore the currently inspected/running Copy x8 Node 6 is the pristine validation control, NOT the nominal NtSide=1e18 damaged baseline.
  - The Workbench tree currently contains only NtSide={0,1e18}; the source comments list 1e17/1e19 but those sweep points are not in the captured tree.
- Runtime:
  - Math: Digits=5, ErrRef(e/h)=1e4, RHSMin=1e-3, Transient=BE, ExtendedPrecision(80), Blocked + ILS(set=22).
  - Transient: InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2; transient Coupled has no explicit Iterations setting.
  - Logs show repeated high-bias residual stagnation slightly above RHSMin with long rejected steps.
- External runtime event:
  - n6_des.err records license-server outage/suspension from 2026-09-30 23:02 to 2026-10-01 13:02, roughly 14 hours, so calendar runtime is inflated by infrastructure downtime in addition to solver convergence cost.
- Mesh:
  - 138137 vertices, 274946 elements, 41 regions, max connectivity 9.
- Immediate consequence:
  - FAST optimization should first benchmark against this exact NtSide=0 control for numerical equivalence, but a scientifically valid Common Baseline still requires the NtSide=1e18 branch (Node 12) to be independently recovered/run from the same frozen source and parameter revision.


## 2026-10-04 — overnight active-run progress confirms severe high-bias runtime bottleneck

- 작업자: 이택규
- 상태: OBSERVED
- 2026-10-04 11:52 KST 터미널 확인:
  - Copy x6: still running; latest visible pseudo-time ~0.942317, anode ~4.712 V.
  - Copy x8: still running; latest visible pseudo-time ~0.928460, anode ~4.642 V.
  - Copy x7 is also still running despite being previously identified as a duplicate v1.1 active calculation.
- Compared with the 2026-10-03 evening captures, overnight progress is only a few to ~10 mV while repeated Newton stagnation persists near RHS ~1e-3.
- Copy x6 again shows a step spending >1000 s while residual stalls around 1.42–1.43e-3.
- Copy x8 is entering the same pattern.
- Conclusion: do not wait for current decks to reach 5 V before starting runtime optimization. Preserve x8 as reference, retire duplicate x7, and begin a separate FAST_BASELINE benchmark today.

## 2026-09-29 — Active baseline run confirmed alive; severe Newton cutback near 4.66 V

**OBSERVED:** direct `n6_des.out` output shows the active job is Node 6. It has reached pseudo-time ≈0.93254, corresponding to ≈4.66 V for the 0→5 V linear transient ramp.

A BE step exceeded 50 Newton iterations, was rejected, and SDevice immediately retried with a smaller timestep of about 8.67e-06. The failed attempt consumed about 1244 s wallclock (~20.7 min), including about 999 s solve time.

Therefore the job is not hung at the captured moment. The current blocker is poor high-bias convergence causing repeated timestep cutbacks and potentially very long completion time. Do not abort or change baseline physics based on this screenshot alone.

## 2026-09-29 — Ju Subin current run: one branch waiting, active branch progress unverified

**OBSERVED from user screenshot:** the selected upper SDevice branch shows `Status: waiting` in Workbench Properties, so that branch has not begun SDevice computation. The lower branch's Node 19 visually appears active/running, but the graph view alone does not prove that SDevice is still advancing after three days.

**Current blocker:** determine whether Node 19 is actively advancing or stalled, and why the other branch remains queued. Highest-value evidence is Node 19 Job Log bottom plus the last 30–50 lines and modification time of `n19_des.out`.

Do not restart the run or change Nt/Et/sigma/geometry/solver physics until that evidence is checked.

# Current Status

## 2026-09-28 — CRITICAL SYNC GAP: Ju Subin Final SDevice v1.2 is NOT in tcad/CURRENT

**OBSERVED by Lee Taek Gyu session:** GitHub Issue #7 and JuSubin timeline record that Final SDevice v1.2 was prepared with intermediate visualization TDR saves, while preserving physics/traps/solver/0→5 V ramp.

However, the actual source-of-truth file `CMP/tcad/CURRENT/sdevice2_defect_on.cmd` is still an older deck:
- sidewall trap concentration is hard-coded as `Conc = 1e18`
- global `IncompleteIonization` is still present
- no v1.2 intermediate `Plot(... Time=(...))` saves are present
- therefore this file is not the recorded Final SDevice v1.2 and should not be treated as current final code

**BLOCKER:** the exact full user-provided Final SDevice v1.1/v1.2 source is not present in GitHub CURRENT. Do not reconstruct or overwrite it from Issue snippets. The exact full source must be recovered from the JuSubin chat/user file or re-uploaded, then synchronized verbatim/minimally patched.

**Data status:** Issue #7 / Gmail notifications correctly reflect JuSubin's progress, but the executable CURRENT source file is stale.

---


## 2026-09-26 — Presentation-ready baseline scope

For today's deadline, the baseline can be considered **implementation-frozen / structurally validated** once the corrected current source preprocesses cleanly and the NtSide=1e18 branch passes initialization/early solve. It is **not yet fully electrically validated** until same-revision NtSide=0 and 1e18 full runs complete.

Presentation wording should preserve this distinction.


## 2026-09-26 — Fair comparison requirement updated

Successful Node6 and current Node12 differ in both generated command and parameter files.

Node6 `pp6_des.par`:
- PDopantActiveConcentration
- NDopantActiveConcentration

Node12 `pp12_des.par`:
- pMagnesiumActiveConcentration

Therefore the existing Node6 result cannot serve as the final control for a modified/current Node12. A valid baseline comparison requires both NtSide=0 and NtSide=1e18 to be regenerated from the same frozen SDevice source and same parameter-file revision, with NtSide as the only intentional difference.


## 2026-09-26 — Mg incomplete-ionization scope mismatch identified

Node 12 `pp12_des.par` contains incomplete-ionization parameters only for `Material="GaN"` and `Species("pMagnesiumActiveConcentration")`. It contains no InGaN ionization block.

The failed Node 12 log terminates after reporting that an Mg-related active-concentration species in InGaN QW regions has no incomplete-ionization parameters. The current SDevice source activates Mg incomplete ionization globally.

This establishes a strong configuration mismatch: the model is globally active where the parameter file does not provide the corresponding InGaN ionization parameters.

Proposed minimal fix: scope Mg incomplete ionization to the p-GaN regions only (`Clean_pGaN`, `DmgL_pGaN`, `DmgR_pGaN`) rather than globally. Keep Thermionic, sidewall trap Nt/Et/sigma, geometry, and Plot unchanged for this diagnostic.


## 2026-09-26 — Full source resolves the Node 6/12 preprocessing discrepancy

The current full SDevice source contains no NtSide-dependent conditional preprocessing. `@NtSide@` appears in trap concentration only. The current source always includes `Thermionic`, species-selected Mg incomplete ionization, and the expanded Mg/quasi-Fermi Plot fields.

Therefore the successful Node 6 generated deck (which lacked these lines) is almost certainly from an earlier source revision and was not regenerated when Node 12 was rerun. Existing Node 6 output remains a valid result for its historical deck, but it is not a clean same-source control for the current Node 12.

The current Node 12 initialization failure remains strongly correlated with Mg incomplete-ionization setup in InGaN. Next evidence required: `pp12_des.par` Ionization/Magnesium/InGaN definitions.


## 2026-09-26 — Node 12 failure reproducible on rerun

The NtSide=1e18 Node 12 was rerun alone and failed again in the same manner. This makes a transient scheduler/license glitch less likely and points to a reproducible input/configuration problem for Node 12.

Because the user confirms a single source with only NtSide split, the observed pp6/pp12 differences most plausibly come from either:
1. NtSide-dependent preprocessing in the source, or
2. stale/cached Node 6 generated files from an earlier source revision while Node 12 was re-preprocessed from the current source.

No physics change should be made until the original source conditional logic/provenance is checked.


## 2026-09-26 — Correction: Node 6/12 came from the same source split

User explicitly confirmed that Node 6 and Node 12 were generated from the same SDevice source and only `NtSide` was split (0 vs 1e18).

Therefore the observed pp6/pp12 differences must not be interpreted as proven manual/source-deck drift. Plausible mechanisms now include:
- NtSide-dependent preprocessor conditionals in the source,
- parameter-dependent macro expansion,
- or node/input version/cache differences.

No physics/model line should be removed yet. The next diagnostic is to inspect the original `sd_fdiv_des.cmd` around NtSide and any conditional preprocessing.


## 2026-09-26 — Ju Subin Node 6/12 deck diff resolved a major confounder

Direct comparison of the successful Node 6 and failed Node 12 preprocessed Physics/Plot blocks confirms that the two runs differ by more than NtSide:

- Node 6: no `Thermionic`; plain `IncompleteIonization`; no Mg-specific/quasi-Fermi-energy Plot fields.
- Node 12: `Thermionic`; `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`; extra `eQuasiFermiEnergy`, `hQuasiFermiEnergy`, `pMagnesiumActiveConcentration`, `pMagnesiumMinusConcentration` Plot fields.
- Trap concentration: 0 vs 1e18 as intended.

Therefore the failed Node 12 is **not a clean NtSide-only comparison**. The immediate recovery plan is to restore the successful Node 6 Physics/Plot configuration in the original SDevice source and vary only the trap concentration for the 1e18 rerun. No claim is made yet that Thermionic or species-selected incomplete ionization is intrinsically invalid.


## 2026-09-26 — Failed Node 12 preprocessed deck differs from synchronized baseline

User supplied the failed Node 12 preprocessed Physics/Plot section. It contains:
- `Thermionic`
- `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`
- sidewall trap Conc=1e18 in DmgL/R pGaN, EBL, Barrier0~4, QW1~4, nGaN
- expanded Plot keywords for SRH subcomponents, trap fields, and Mg species

The synchronized baseline deck currently in GitHub has plain `IncompleteIonization`, no `Thermionic`, and a simpler Plot list. Therefore the failed Node 12 cannot yet be treated as a proven NtSide-only split until it is directly diffed against successful Node 6.


## 2026-09-26 — Ju Subin baseline result strengthened

**CONFIRMED:** successful `NtSide=0` Node 6 reached 5.0 V, finished the curve trace, wrote `n6_des.tdr`, and ended with normal SDevice completion text. Wallclock ≈235312 s (~65.4 h, ~2.7 days).

**FAILED:** `NtSide=1e18` Node 12 exits during initialization with SDevice `exit(1)`, before normal solve/output completion.

Key branch difference observed in logs:
- Node 6 success: no `mMagnesiumActiveConcentration` message found by user search.
- Node 12 fail: repeated InGaN incomplete-ionization parameter messages immediately before termination.

This is a strong diagnostic difference but not yet sufficient to change physics. First verify preprocessed CMD/PAR files differ only by intended NtSide trap concentration.


## 2026-09-26 — Ju Subin baseline split-run result

**OBSERVED:** 주수빈이 학교에서 이전에 실행해 둔 Common Baseline split run을 확인함.

- `NtSide=0`: 정상 완료
- `NtSide=1e18`: failed

현재는 1e18 실패 원인이 아직 식별되지 않았다. 0 조건이 완료됐다는 사실은 동일 flow가 최소한 trap-off 조건에서 실행 가능함을 보여주지만, 이것만으로 1e18 실패가 trap physics 자체 때문이라고 확정할 수는 없다.

**Immediate diagnostic:** 실패한 1e18 node의 `*.err` 전체와 `*.out` 마지막 50~100줄에서 최초 error/fatal/convergence failure를 확인한다. 원인 확인 전 Common Baseline의 Nt/Et/sigma/5 nm damage width/epitaxy를 변경하지 않는다.


Last synchronized: 2026-09-21

## Current stage

**Common Baseline v1 validation — geometry mostly validated; SVisual2 output-file linkage currently unresolved.**

## Parallel work — Ju Subin

**Status: OBSERVED — shared project conversation / user report**

주수빈은 별도 채팅에서 Common Baseline 관련 메인 SDevice 및 앞서 검토한 관련 코드를 최종 수정했다고 보고했으며, 장시간 simulation을 시작하기 전에 Project A와 Project B 모두에 적합한 baseline인지 마지막 정적/논리 검토를 진행 중이다.

현재 계획:
- 우선 `NtSide=0`
- 우선 `NtSide=1e18`

두 조건만 먼저 실행해 baseline 동작을 확인.

주수빈 보고 기준으로 한 run이 약 3일 걸릴 수 있어 전체 sweep 전에 코드 검증을 우선한다.

**중요:** 이 기록 시점에는 주수빈 측 최신 전체 코드 원문 및 새 simulation 결과가 GitHub에서 직접 검증되지 않았다. 따라서 코드 정확성이나 실행 성공을 CONFIRMED로 간주하지 않는다.

## Confirmed

### Geometry / Regions
Sentaurus Visual에서 다음 region들이 실제로 존재함을 확인:
- Clean_Barrier0~4
- Clean_EBL
- Clean_QW1~4
- Clean_nGaN
- Clean_pGaN
- DmgL_Barrier0~4
- DmgL_EBL
- DmgL_QW1~4
- DmgL_nGaN
- DmgL_pGaN
- DmgR_Barrier0~4
- DmgR_EBL
- DmgR_QW1~4
- DmgR_nGaN
- DmgR_pGaN
- Nitride_L / Nitride_R

따라서 `DmgL | Clean | DmgR` partition은 구조적으로 구현됨.

### Doping visual check
DopingConcentration map에서:
- p-side 약 -3×10^17 cm^-3 scale
- n-GaN 약 +5×10^18 cm^-3 scale
확인됨.

### Vertical stack visual check
- MQW 층이 존재
- n-GaN 시작 위치가 p-GaN 0.120 µm + EBL 0.026 µm + MQW 0.122 µm ≈ 0.268 µm와 시각적으로 일치
- Nitride_R 폭이 약 0.1 µm scale로 보임

### SVisual1
초기 오류 수정:
1. `"Anode Voltage [V]"`의 Tcl command substitution 문제
   - 수정: `{Anode Voltage [V]}`
2. `fit_plot` unsupported
   - 수정/제거 후 실행 가능 상태 확보

### SDevice2
Node 9 `n9_des.out`에서:
- `Sentaurus Device simulation finished`
- `Good Bye !`
확인.
즉 SDevice2 solver 자체는 정상 종료한 실행 이력이 있음.

## Current blocker

SVisual2(Node 10)가 다음 파일을 읽도록 되어 있음:

```text
n9_des.tdr
```

현재 SVisual2 오류:

```text
Error: File 'n9_des.tdr' could not be loaded.
```

Node 9 Explorer의 Output Files 화면에서는 당시:
- n9_des.err
- n9_des.job
- n9_des.out
- n9_des.sta
- n9_local.err
- pp9_des.cmd
- pp9_des.par

가 보였으며 `n9_des.tdr`은 목록에서 확인되지 않았음.

따라서 현재 핵심 질문은:

**SDevice2가 실제 Plot/TDR output을 어떤 파일명으로 생성하도록 preprocessing 되었는가, 또는 왜 TDR이 생성되지 않았는가?**

## Important: do not change yet

이 blocker를 해결하기 위해 아래 baseline parameter를 바꾸지 말 것:
- Nt
- Et
- sigma_n / sigma_p
- 5 nm damage width
- Kou epitaxy
- mesa width
- doping

현재 문제는 우선 output/dependency/file-linkage 문제로 취급한다.

## Files synchronized to GitHub

- `CMP/tcad/CURRENT/sdevice2_defect_on.cmd`
- `CMP/tcad/CURRENT/svisual1_iv.tcl`
- `CMP/tcad/CURRENT/svisual2_maps.tcl`

아직 최신 전체 원문이 GitHub에 없는 것:
- SDE
- SDevice1
- 주수빈 측 최신 수정 코드 전체 원문

이들은 연구자가 실제 최신 코드를 동기화하기 전까지 추정 생성 금지.


## Parallel blocker update — Ju Subin runtime

**OBSERVED 2026-09-22:** Node 6 SDevice는 18시간 이상 실행 중이지만 현재 출력상 멈춘 것이 아니라 BE stepping을 계속 수행하고 있다. 공유 화면에서 직전 step은 수렴 완료됐고 총 wallclock 약 3563.68 s(약 59분), 다음 step은 `0.0766738 → 0.0776738` with `Stepsize=1e-3`로 진행 중이다.

현재 주수빈 트랙의 즉시 blocker는 **실패가 아니라 과도한 per-step runtime / 총 run time 불확실성**이다. 다음 판단에는 `pp6_des.cmd` Solve block의 최종 목표와 step-control 값 확인이 필요하다. Baseline physics parameter는 이 진단 때문에 임의 변경하지 않는다.


## Ju Subin runtime blocker — cause identified

**CONFIRMED 2026-09-22:** Node 6의 장시간 실행은 현재 `Transient` bias ramp의 매우 작은 `MaxStep=1e-3`와 큰 per-step solve cost가 결합된 결과다. Goal은 anode 5.0 V이며, 로그의 pseudo-time 0.0766738에서 anode ≈0.3834 V가 `5×time`과 일치한다. 따라서 MaxStep 1e-3은 약 5 mV/bias step에 해당하며 5 V까지 약 1000 accepted steps 규모가 필요하다. 현재 지점에서만 최소 약 923~924 steps가 남는다.

최근 약 3564 s/step을 그대로 외삽하면 남은 시간이 약 38일 수준이 될 수 있으므로, 현재 blocker는 **numerical step strategy / computational cost**로 갱신한다. 물리 baseline parameter는 이 문제 해결을 위해 변경하지 않는다.


## Ju Subin runtime diagnosis refinement

사용자가 **최종 수정 전 거의 같은 deck이 약 3일 내 완료**되었다고 보고했다. 따라서 현재 확인된 `MaxStep=1e-3`은 긴 총 step 수를 설명하지만, **이번 run이 과거보다 느려진 원인을 단독으로 설명하지는 못한다.** 이전 run과 step-control이 같았다면 핵심 차이는 per-step 계산비용 또는 step rejection/cutback 증가다.

현재 우선 비교 대상은 old vs current의 mesh 규모, Physics/Trap 적용 범위, Math/linear solver 설정, 그리고 n*_des.out의 rejected/repeated step 이력이다. 최근 3564 s 한 step으로 산출한 ~38일 값은 실제 총시간 예측이 아니라 단순 외삽 참고치로 강등한다.


## Ju Subin runtime evidence — old run around 0.30 V

과거 약 3일 내 완료된 run에서 anode 약 0.3034 V step의 Total time은 172.57 s, 약 0.3084 V step은 123.94 s였고 각각 5 Newton iterations로 수렴했다. 현재 run의 약 0.3834 V step은 Total 약 3563.68 s가 관찰됐다. bias가 완전히 같지는 않지만, **현재 run의 accepted step 비용이 과거 run보다 크게 증가한 정황이 강해졌다.** 최종 비교를 위해 과거 0.38 V 부근 로그 확인이 필요하다.


## Ju Subin runtime root cause narrowed at identical bias

Old/current를 **동일 accepted anode ≈0.3834 V**에서 직접 비교했다. old run은 Total 177.47 s (Assembly 64.84 s, Solve 108.74 s), current run은 Total 3563.68 s (Assembly 598.77 s, Solve 2928.83 s)였다. 현재 step은 old 대비 약 **20.1× 느림**. 따라서 현재 장시간 문제는 MaxStep/step 개수보다 per-step computational cost 증가가 핵심이다.


## Correction — Ju Subin runtime interpretation (2026-09-22)

앞서 'old run 0.3834 V = 177.47 s vs current = 3563.68 s'로 기록한 비교는 **무효**다. 177.47 s 로그도 현재 Node 6의 동일 `n6_des.out` 초기 구간임이 확인됐다.

현재 확인된 사실:
- 현재 run 초기 구간: 0.0756738→0.0766738, accepted anode ≈0.3834 V, Total 177.47 s.
- 같은 현재 run의 더 뒤쪽 화면: accepted anode ≈0.3834 V 직후 Total 3563.68 s.
- 따라서 현재 핵심 질문은 **한 run 안에서 같은 ramp coordinate가 왜 다시 나타나는지 / 서로 다른 Transient or Solve stage인지**이다.

old-vs-current 20.1× slowdown 결론은 철회하고, stage identification 전까지 원인을 mesh/physics/solver 변화로 확정하지 않는다.


## Re-correction — old/current runtime comparison restored

사용자가 직전 스크린샷이 **예전에 약 3일 만에 완료된 노드의 `n6_des.out`**이라고 명확히 확인했다. 따라서 앞서 추가한 "같은 current run 내부 초기 구간" 해석은 철회한다.

유효한 동일-bias 비교:
- old run, anode ≈0.3834 V: Assembly 64.84 s, Solve 108.74 s, Total 177.47 s
- current run, anode ≈0.3834 V: Assembly 598.77 s, Solve 2928.83 s, Total 3563.68 s
- current/old Total ≈ 20.1×

따라서 현재 장시간 문제는 **per-step solve cost 증가**가 핵심이며, old/current deck 차이 비교가 우선이다.


## Ju Subin old 3-day deck captured

과거 약 3일 완료된 preprocessed SDevice deck의 전체 설정을 확보했다. 이 old deck은 모든 sidewall damage trap의 `Conc=0`인 **NtSide=0 케이스**다. 또한 Transient 설정은 `1e-5 / 1e-9 / 1e-3 / Increment 1.2 / Goal 5 V`로 현재 slow run에서 확인한 step-control과 동일하다.

따라서 다음 판정의 핵심은 현재 slow Node 6도 `Conc=0`인지 여부다. current가 1e18이면 old 0과 runtime을 직접 비교하면 안 된다. current도 0이면 Math/Physics/mesh 차이로 바로 좁힌다.
