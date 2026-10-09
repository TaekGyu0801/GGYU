## 2026-10-08 — 주수빈 accelerated Half+coarse QS smoke deck prepared (PROPOSED)

- Half+coarse SDE mesh actually built successfully; 138,194 elements, 65,513 points.
- Current 0→0.3 V transient smoke is accepted but slow (~109.74s/step with ~90.20s linear solve).
- Private SWB SDevice alternative generated: `sdevice_des_JUSUBIN_HALF_COARSE_QS_SMOKE.cmd`, SHA256 `a7281c79e7e440c6192726f4ce6edefb58f8d76ed30ec921900fee5ff5a5ec01`.
- Steady QS anode 0→0.3 V; InitialStep=.03, MaxStep=.15, Increment=1.5, MinStep=1e-6, Decrement=2; original full device physics/traps and Math/ILS preserved.
- Static syntax/region checks PASS, actual QS preprocess/run NOT DONE. Original full FAST_C1 reference untouched.
- NEXT: user installs file in SWB after stopping only old Node2 smoke if desired; preprocess `pp2_des.cmd` and run QS 0.3V test.

## 2026-10-08 — cmp216 FAST_C1 test: apparent interruption, cause unresolved

- OBSERVED (user shell outputs): separate `cmp216@ssudisu2` run in `~/FAST_C1_ACCOUNT_TEST`. Last accepted Node6 0.9534 V; next BE-step logged header only. Log last modified Oct 7 17:47; PLT Oct 7 17:45; no `n*_des.tdr` found; no active `cmp216` SDevice process on checked host.
- `grep` search found license checkouts but no explicit fatal/killed/aborted/normal-completion marker.
- UNRESOLVED: why the run stopped producing output, including login/session termination or process failure. Cross-account performance effect beyond low bias unverified.
- NEXT: read-only process/session/job/launch history check; retain files and ongoing `semi437` references untouched.

## 2026-10-07 — Project A/B pre-run audit: Baseline parent OK; production A/B NO-GO until gates pass

- 작업자: 주수빈
- 상태: REVIEWED / PRE-RUN GATE
- FAST_C1/Common Baseline은 A/B parent로 유지 가능; physical baseline 재구축 필요 없음.
- same-current I-V + intermediate spatial TDR 기반은 유지되고 실제 FAST_C1 Node 6에서 intermediate TDR 생성 확인.
- broad multi-day A/B production은 아직 NO-GO.
- 필수 gate: active pp-deck audit, dataset/extraction test, J normalization, A Cedge geometry/mesh/physics/null control, B exact vertical span + AlBarrier geometry/mesh/null control, Save/Load smoke, representative A/B pilots.
- Project B가 QW edge를 AlGaN으로 치환하면 active QW volume이 달라질 수 있으므로 total recombination뿐 아니라 QW-volume normalization 및 injection/leakage metric을 함께 사용.
- 상세: `CMP/PROJECT_AB_PRE_RUN_AUDIT.md`.

## 2026-10-06 — D6 complete; Save-based C2 smoke next

- 기존 C1 `Plot(-Loadable)` intermediate는 restart state 정보가 없어 current Node 6 restart에 사용 불가.
- Option 3 폐기, Option 2만 유지.
- Node 6/12 reference run 계속.
- 다음: revised C2 smoke에서 `Save` checkpoint를 생성하고, 그 Save 파일에 대한 `Load` check 수행.
- 첫 common C2 정책: Iterations=15 유지, Increment=1.05 시험.

## 2026-10-06 — D3 IV extraction and D5 CPU headroom check

- 작업자: 이택규
- 상태: OBSERVED / VALIDATION

### D3 I(V) extraction
- copied live current files parsed successfully with proposed `iv_window.py`.
- Node 6: 3323 points, V range 0 -> 4.7128 V, I_max = 2.8954e-12 A/um (under standard 2D no-AreaFactor interpretation).
- Node 12: 1236 points, V range 0 -> 4.2474 V, I_max = 7.9816e-14 A/um.
- selected same-voltage Node12/Node6 total-current ratios:
  - 3.0 V: 0.9566
  - 3.5 V: 0.9562
  - 4.0 V: 0.9252
  - 4.1 V: 0.8150
  - 4.2 V: 0.5829
  - 4.23 V: 0.5276
  - 4.24 V: 0.5125
- provisional current-density conversion with 4 um mesa gives values only ~1.5e-6 to 3.8e-6 A/cm2 in the shared 3.0-4.24 V range; default target list 0.1-1000 A/cm2 is not reached.
- therefore Decision 0 (truncate production range based on already-reached J window) is NOT supported by current data and remains pending.
- explicit AreaFactor is absent in pp6/pp12 cmd/par. Older Sentaurus documentation states default 2D width 1 um / current unit A/um, but exact T-2022.03 manual confirmation is still pending before publication use of J.
- the extremely low extracted current density should be treated as a model/result sanity-check item, not automatically as a valid LED operating-current range.

### D4 current snapshot
- 21:52 KST:
  - Node 6 latest attempt t0=0.942564 -> ~4.71282 V.
  - Node 12 latest attempt t0=0.849478 -> ~4.24739 V.
- both runs remain live and progressing.
- fixed 1-2 h progress-rate measurement is not yet complete from this snapshot alone.

### D5 CPU resource
- nproc=128.
- load average ~7.46 / 7.70 / 7.81.
- active SDevice CPU: Node6 ~280%, Node12 ~268%.
- CPU headroom is ample for a short third smoke/load test.
- Sentaurus license headroom remains unverified.

- next: D6 scratch Load test using Node 6 4.7 V intermediate TDR without stopping Node 6/12; if license unavailable, the test must not disturb reference runs.

## 2026-10-06 — D2 exception check confirmed; D3 structural gate passed

- 작업자: 이택규
- 상태: OBSERVED / VALIDATION
- Node 12 accepted >8-iteration exceptions are real accepted transient steps, not parser artifacts:
  - idx 1103: V0=4.233805 V -> V1=4.233915 V, dt=2.1351e-5, 15 iterations, final RHS=9.98e-4, wallclock=121.55 s.
  - idx 1165: V0=4.237610 V -> V1=4.237710 V, dt=1.9766e-5, 13 iterations, final RHS=9.98e-4, wallclock=104.02 s.
- both barely satisfy RHSMin=1e-3, confirming that universal C2 caps 8/10 would create genuine false rejections.
- common C2 Iterations=15 decision is strengthened.

### D3 structural checks
- Node 6 current file: n6_des.plt, 1.4 MB, mtime 2026-10-06 21:45.
- Node 12 current file: n12_des.plt, 496 KB, mtime 2026-10-06 21:46.
- both preprocessed File blocks point Current to the corresponding .plt.
- both .plt datasets include time, anode OuterVoltage/InnerVoltage, eCurrent, hCurrent, TotalCurrent, Charge.
- no explicit AreaFactor string found in pp6_des.cmd/par or pp12_des.cmd/par.
- therefore .plt files are suitable for I(V) extraction.
- absolute current-density normalization remains provisional until exact T-2022.03 default 2D current/AreaFactor semantics are verified; older Sentaurus documentation indicates default 2D current units A/um when no AreaFactor is specified.
- next: run iv_window.py on copied live .plt files to obtain I(V) and provisional J(V), while keeping Decision 0 pending.

## 2026-10-06 — D2 complete: cap 8/10 not safe for common C2

- Node 6 accepted max Newton=4; cap 8 false_rej=0.
- Node 12 accepted max Newton=15; accepted 13-iteration and 15-iteration steps exist.
- Node 12 cap 8/10 each predict 2 false rejections; first divergence ~4.195 V.
- Decision: first common C2 keeps Iterations=15; test Increment=1.05 first.
- Original cap-8 C2 deck is provenance only and must not be executed as-is.
- Next: inspect Node 12 >8 accepted exceptions, then D3 current normalization/J-window.

## 2026-10-06 — D1 complete: high-bias failure is not a GMRES-maxit stall

- 작업자: 이택규
- 상태: OBSERVED / DIAGNOSIS
- Node 6 representative failed step (0.942217 -> 0.942229, dt=1.1842e-5):
  - nonlinear factor remains 1.00e+00.
  - |step| remains about 1.33e-2 to 1.34e-2 instead of collapsing toward zero.
  - #iterative is typically ~48-54, far below configured linear-solver maxit=200.
  - RHS drops rapidly to ~1.41e-3 by Newton iteration 2 and then remains essentially flat through iteration 15.
- half-step retry (dt=5.9211e-6):
  - #iterative remains similar (~50-52), yet RHS reaches 4.58e-4 at Newton iteration 2 and converges.
- therefore the observed failure is NOT explained by the inner GMRES reaching maxit, and the linear-solver iteration count itself does not distinguish failure from success.
- the logged error column alternates between values similar to those also seen on the successful retry, so its semantic meaning must not be over-interpreted without the T-2022.03 manual.
- working interpretation: a timestep-dependent nonlinear residual floor just above RHSMin is the immediate bottleneck; this supports testing safer high-bias timestep growth before changing the linear solver.
- implication for FAST_C2: keep linear solver unchanged for the first C2 candidate. Proceed to D2 accepted-iteration audit before approving Iterations=8.

## 2026-10-06 — Claude high-bias runtime analysis reviewed; FAST_C2 proposed

- 작업자: 이택규
- 상태: REVIEWED / PROPOSED / NOT EXECUTED
- Claude package `FAST_C2_strategy_for_GPT.zip` reviewed by ChatGPT.
- central diagnosis accepted as a working numerical model:
  - high-bias runtime is dominated by a local convergent-timestep ceiling (`dt*`) plus `Increment=1.2` growth -> expensive rejection -> ~0.5 cutback cycling.
  - Node 6 representative failure: dt=1.1842e-5, RHS ~1.41e-3 stagnates through Iteration 15; retry dt=5.9211e-6 converges in 2 iterations.
  - idealized cycle model reproduces current Node 6 speed (~2.24 mV/h model vs ~2.2 mV/h observed).
  - under the same idealized assumptions, Increment=1.05 + Iterations=8 gives ~5.24 mV/h; this is a model prediction, not measured C2 performance.
- FAST_C2 remains numerical-only PROPOSED:
  - staged global-time Transient
  - 4 V+ Increment 1.05
  - candidate Iterations 8 subject to D2 accepted-iteration audit
  - checkpoints at 4.0/4.4/4.6/4.8 V
  - RHSMin/physics/mesh/5 V endpoint unchanged
- important ChatGPT caveat:
  - changing iteration cap/timestep growth changes the transient step sequence; identical convergence criteria do not by themselves guarantee identical trap/transient state.
  - NtSide=1e18 C2 validation must include trap charge/occupancy, SRH, radiative/Auger and carrier distributions, not I-V alone.
  - Claude trap-emission estimate uses generic GaN assumptions and is not a confirmed active-deck timescale.
- current Node 6/12 runs MUST continue as reference evidence.
- syntax/manual gates remain unresolved: segmented InitialTime/FinalTime+Goal semantics, Save/Load syntax, and whether existing Plot(-Loadable) TDR can be loaded.
- Decision 0 is separate and pending team approval: whether production analysis endpoint may be defined by a validated current-density window instead of always requiring 5 V. Baseline 5 V endpoint is not changed.
- `iv_window.py` J values are provisional until AreaFactor/2D current normalization is verified.
- public files added:
  - `CMP/FAST_BASELINE_C2.md`
  - `CMP/tcad/tools/make_restart_deck.py`
  - `CMP/tcad/tools/iv_window.py`
- proprietary full C2 deck was NOT uploaded; recorded production deck SHA-256 = `b876f614424202e6deaf0655411d7bc15733095da297c1df9ca5ebaacbb578d1`.
- helper scripts passed Python syntax and synthetic-only tests; no live Sentaurus test yet.
- next: D1–D6 in order, then C2 smoke gate before any production C2 run.

## 2026-10-06 — Node 6/12 logs confirm forward progress with repeated timestep cutback, not a hard stall

- 작업자: 이택규
- 상태: OBSERVED / RUNTIME DIAGNOSIS
- user-provided logs show both SDevice runs are advancing in accepted pseudo-time.
- Node 6 (FAST_C1):
  - recent BE-step attempts progress through ~0.942147 -> 0.942238.
  - representative failed attempt: 0.942217 -> 0.942229, dt=1.1842e-05, reaches Iteration 15 with RHS ~1.41e-3 and is rejected.
  - automatic retry halves the step to 5.9211e-06 and converges in 2 iterations with RHS 4.58e-4.
  - subsequent accepted steps increase again (7.1054e-06, then 8.5265e-06).
  - mapped bias is ~4.711 V at pseudo-time ~0.9422 for the known 0->5 V ramp.
  - diagnosis: not hung; local nonlinear convergence causes periodic reject -> ~0.5 cutback -> quick recovery.
- Node 12 (FAST_C1_Copy):
  - recent BE-step attempts progress through ~0.848534 -> 0.848697.
  - repeated pattern visible: larger attempt rejected, then step approximately halved (e.g. 2.1922e-05 -> 1.0961e-05; 1.8941e-05 -> 9.4703e-06; 1.9638e-05 -> 9.8188e-06), followed by renewed growth.
  - accepted steps generally converge in 2 iterations around 18-19 s in the provided tail.
  - mapped bias is ~4.243 V around pseudo-time ~0.8486 for the known 0->5 V ramp.
  - current last shown attempt at dt=2.0360e-05 had RHS ~1.17e-3 by iteration 3, so its eventual accept/reject outcome is not yet shown.
- conclusion:
  - no evidence of syntax error or frozen solver in these logs.
  - dominant runtime cost is repeated high-bias step rejection/cutback, especially Node 6.
  - do not terminate current runs solely on suspicion of a stall.
- next:
  - keep current runs as reference evidence.
  - accelerated branch should target numerical continuation / sweep strategy and/or reduced mesh, while preserving physics.
  - any solver-policy change must be validated against these reference trajectories.

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


## 2026-10-09 11:30 KST update
- OBSERVED (user report): `JUSUBIN_FAST_HALF_SWB` run completed overnight.
- Previous blocker "half+coarse transient still running" is cleared at report level.
- Verification gate remains: confirm final 0.3 V, no fatal termination, output artifacts, and extract runtime/I-V before treating the run as a validated result.


## 2026-10-09 11:30 KST priority
1. Verify completed `JUSUBIN_FAST_HALF_SWB` terminal/log evidence: final 0.3 V, normal completion, no fatal/error, output files.
2. Extract total wallclock/runtime and I-V points from the completed half+coarse transient.
3. Check the `JUSUBIN_FAST_HALF_SWB_Copy` QS smoke status/result separately.
4. Compare Half+coarse transient vs QS Copy, then against full FAST_C1 reference before adopting the fast branch for production A/B.


## 2026-10-09 — QS Copy early termination verified; original transient complete
- Original `JUSUBIN_FAST_HALF_SWB` transient: CONFIRMED 0.300 V trace completion, 25019.43 s, 412K PLT / 15M TDR / 3.1M SAV. 0.3 V I-V examined but physically validated baseline not yet established.
- Separate `JUSUBIN_FAST_HALF_SWB_Copy` QS: UNRESOLVED — SDevice `Step-size less than MinStep (step-size = 8.3986e-07)`; 18417.09 s and `Good Bye`, SAV/TDR written. Goal 0.3 V NOT confirmed. No comparable QS speedup conclusion.
- Next: QS n2_des.plt last accepted anode bias + last log step/retries/err; do not modify baseline or solver yet.


## 2026-10-09 — QS Copy last accepted bias determined
- 작업자: 이택규. OBSERVED from user-provided `JUSUBIN_FAST_HALF_SWB_Copy/n2_des.plt` tail and `n2_des.log` grep.
- Last recorded QS pseudo-time: 6.43487876313307E-02; last anode OuterVoltage: 1.93046362893992E-02 V (0.0193046363 V; 19.3 mV, only ~6.435% of requested 0.3 V).
- Last log attempts at t=0.0643488 to 0.0643505 then terminated `Step-size less than MinStep (step-size = 8.3986e-07)`.
- QS runtime 18417.09 s but did NOT reach goal. Cannot compare as speedup to original transient that reached 0.3 V in 25019.43 s.
- Root numerical/physics trigger not yet established. Next: inspect QS log around lines 6900-7000 and `n2_des.err`; no blind MinStep or baseline modification.


## 2026-10-09 — QS Newton failure isolated
- Final attempted QS step `t=0.0643488→0.0643505`, Newton Poisson+electron+hole Bank/Rose hit Coupled limit 15, residual oscillated to ~1.26e8, final ~1.85e6; retry step 8.3986e-7 below MinStep 1e-6. Root numerical/physical trigger unresolved. Preserve completed transient and baseline. Next inspect actual active QS Math/Solve deck before any numerical-only pilot.


## 2026-10-09 — QS Copy active preprocess settings checked
- OBSERVED from semi437 `JUSUBIN_FAST_HALF_SWB_Copy/pp2_des.cmd` grep supplied by Lee Taekgyu: Quasistationary begins line 589 (InitialStep=0.03, MinStep=1e-6, MaxStep=0.15). QS Coupled has `Iterations=15` line 601; Math `RHSMin=1e-3` line 510. Earlier `Coupled(Iterations=500, LineSearchDamping=1e-2)` around 570-572 appears in initial solve, another initial Coupled Iterations=100 at line 578.
- OBSERVED final QS failed Newton after 15 iterations and rejected halved step below MinStep; 0.0193046363 V last accepted. Specific nonlinear divergence trigger remains UNRESOLVED.
- Need inspect full surrounding Math/Solve 505-610 before attributing nonconvergence to damping, iteration cap, or other solver options. Avoid changing frozen Common Baseline, preserved transient results, or rerunning blindly.


## 2026-10-09 — QS Math/Solve complete context inspected
- 작업자: 이택규; OBSERVED from `JUSUBIN_FAST_HALF_SWB_Copy/pp2_des.cmd` lines 505–530 and 565–610 supplied in chat.
- Math: `ErrRef(electron/hole)=1e4`, `RHSMin=1e-3`, `CheckRhsAfterUpdate`, `Transient=BE`, `ExtendedPrecision(80)`, `TensorGridAniso(aniso)`, `ComputeDopingConcentration`, `Method=Blocked`, `SubMethod=ILS(set=22)`.
- Solve initialization: Poisson `Coupled(Iterations=500 LineSearchDamping=1e-2)`; carrier-coupled zero-bias `Coupled(Iterations=100)`.
- QS: `InitialStep=0.03 MinStep=1e-6 MaxStep=0.15 Increment=1.5 Decrement=2.0 Goal(anode)=0.3 V`, inner `Coupled(Iterations=15)` over Poisson/Electron/Hole with NO explicit LineSearchDamping.
- The initial Poisson damping does not imply the QS inner Coupled has damping. Hypothesis to test: QS Newton stabilization numerics may improve convergence; no direct causal verification yet. Math `Transient=BE` does not replace QS Solve command.
- IMPORTANT discrepancy: code comment says 0.3V checkpoint written only after sweep completed, but actual logs prove Save ran after QS `Step-size less than MinStep` termination at last accepted V=0.019304636 V. Thus `n2_qs0p3_ckpt` is NOT a verified 0.3V checkpoint; never use filename as endpoint evidence.
- Next before code edits: compare numeric & physics control lines of original transient `JUSUBIN_FAST_HALF_SWB/pp2_des.cmd` with QS Copy actual deck. No solver setting modified yet.


## 2026-10-09 — Original transient vs QS Copy settings compared
- 작업자: 이택규; 상태: OBSERVED from user-shared original `JUSUBIN_FAST_HALF_SWB/pp2_des.cmd` grep and previous QS Copy preprocessed deck.
- Both original transient and QS Copy: `ErrRef(electron/hole)=1e4`, `RHSMin=1e-3`, `CheckRhsAfterUpdate`, startup Poisson `Coupled(Iterations=500, LineSearchDamping=1e-2)`, startup carrier `Coupled(Iterations=100)`, sweep inner `Coupled(Iterations=15)` without explicit sweep-local damping.
- Original transient: `Transient` with InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2 (actual final 0.3V result was confirmed earlier). QS Copy: `Quasistationary` InitialStep=0.03, MinStep=1e-6, MaxStep=0.15, Increment=1.5, Decrement=2.0, Goal(anode)=0.3V. Time coordinates have different meanings and cannot be compared directly as numerical step sizes.
- Correction: lack of explicit sweep-local LineSearchDamping is NOT a unique QS setting and cannot by itself explain the divergent convergence. Underlying cause still UNRESOLVED. Other Physics settings and actual complete original Goal/Decrement block not yet side-by-side audited.
- The original source header comments say 0-4.0V/4.0-5.0V, whereas current observed result was a 0.3V smoke; must read executable original Goal in `pp2_des.cmd` to resolve the potentially stale header comment.
- Next: inspect original `pp2_des.cmd` lines 583–615 for actual executable voltage Goal and step-control; preserve both results and Common Baseline. No code changes.


## 2026-10-09 — Original transient executable Goal confirmed (smoke only)
- 작업자: 이택규. OBSERVED from user terminal `../JUSUBIN_FAST_HALF_SWB/pp2_des.cmd` lines 580–615 (actual executable block): `Transient(InitialTime=0.0, FinalTime=0.06, InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Goal{Name="anode", Voltage=0.3})` and inner `Coupled(Iterations=15){Poisson Electron Hole}`, followed by `Save(FilePrefix="n2_smoke_ckpt_0p3V")`.
- Therefore full 0.3 V endpoint was explicitly intended for this short syntax/mesh/physics smoke; earlier header comments describing 0–4.0 V/4.0–5.0 V are NOT the executable sweep configuration for Node 2. Previous comment/Goal discrepancy resolved.
- Original Transient smoke successfully finished 0.3 V; does not establish 3–5 V forward I–V, IQE or half+coarse equivalence to full/fine reference. QS Copy stalled at 0.019304636 V and remains an experimental numerical branch.
- Decision: preserve both existing projects and all outputs; prioritize preparing a separate, reviewed high-bias Transient branch for actual LED operation, only after source/provenance, bias plan, solver stability and half-vs-full validation gates. Do NOT modify original 0.3 V smoke or automatically launch 5 V.


## 2026-10-09 — Filesystem copy exists; SWB open not yet checked
- 이택규 executed `cp -a JUSUBIN_FAST_HALF_SWB JUSUBIN_FAST_HALF_5V_TEST`, subsequent ls confirmed target directory and `cmp` between original/copied SDevice source produced no differences.
- Bash-style conditional produced `if: Expression Syntax.` in current C-shell-like terminal; standalone copy command worked.
- Next verify original/copied hidden `.project` file and project directory content, then open copied project in SWB Projects browser; preserve original, do not run simulations or edit high-bias deck yet.


## 2026-10-09 — SWB `.project` files verified in original and 5V test copy
- 작업자: 이택규; OBSERVED in user terminal `ls -la JUSUBIN_FAST_HALF_SWB/.project JUSUBIN_FAST_HALF_5V_TEST/.project` from `myproject`.
- Both `.project` files exist, zero bytes, each mode `-rw-r--r--`, timestamp Oct 8 16:58; the 5V test is an actual copy with SDevice source previously compared identical.
- This supports SWB project marker preservation, but SWB GUI successful open, flow nodes, and project paths are NOT yet confirmed.
- Next: in existing SWB GUI locate/open `JUSUBIN_FAST_HALF_5V_TEST`, screenshot the project flow and verify independent folder before any source edits, preprocessing or Run/F7. Original smoke project remains preserved.


## 2026-10-09 — 5V test SWB flow screenshot inspected
- 작업자: 이택규; status OBSERVED from screenshot of SWB project table.
- Screenshot visibly contains SDE and SDEVICE tool columns, one scenario row, parameter NtSide=0, and `No Variables` section. SVisual node is not visible in the cropped image.
- Project name/title bar is not shown in this crop, so cannot yet independently verify screenshot refers to `JUSUBIN_FAST_HALF_5V_TEST`, despite user's prior report that copied project opened.
- No evidence of 5V code modifications or new node execution. Next: read copied `JUSUBIN_FAST_HALF_5V_TEST/sdevice_des.cmd` lines 565-620 from user's terminal, check the editable original Solve block and bias/ramp before safe separate 5V branch changes. Do not press F7 before verified preprocess.


## 2026-10-09 — Copied 5V_TEST SDevice source Solve confirmed (OBSERVED; 5V change PROPOSED)
- Worker 이택규 provided terminal `sed -n '565,620p' sdevice_des.cmd` from `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST`.
- Actual copied editable Solve source is still original 0.3V transient smoke: initial Poisson Coupled 500 iterations with `LineSearchDamping=1e-2`; initial Poisson/Electron/Hole Coupled 100; `Transient(InitialTime=0.0, FinalTime=0.06, InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Goal{Name=anode Voltage=0.3})` and inner `Coupled(Iterations=15)`; `Save(FilePrefix="n@node@_smoke_ckpt_0p3V")`.
- PROPOSED minimal 5V feasibility trial in copy only: preserve 5V/time-unit ramp (original 0.3/0.06=5) by considering FinalTime=1.0 alongside Goal=5.0 and distinct save suffix, leaving physics/mesh and numerical controls unchanged initially. This is not an approved or executed code modification or a demonstrated solver convergence strategy.
- Must back up copy source and preflight SWB re-preprocess before Run; high-voltage numerical and physical validation remain open. Original and separate QS Copy results protected. Important: Save can occur after unsuccessful sweep, so checkpoint name alone cannot confirm 5V.


## 2026-10-09 — Half 5V test SDevice edit performed in copied SWB project
- 작업자: 이택규. OBSERVED from terminal in `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST`: user ran `cp -p sdevice_des.cmd sdevice_des_0p3V_backup.cmd`, then `sed -i` replacing `FinalTime = 0.06` with `1.0`, `Goal Voltage = 0.3` with `5.0`, and `Save FilePrefix n@node@_smoke_ckpt_0p3V` with `n@node@_5V_ckpt`.
- Follow-up `grep -nE 'FinalTime|Voltage =|FilePrefix =' sdevice_des.cmd` confirmed line 587 FinalTime=1.0, line 597 Goal Voltage=5.0, line 608 new 5V Save prefix; initial electrode Voltage=0.0 appears at lines 38 and 43.
- Code modification is OBSERVED in the user's remote copied project, NOT yet synced as full source to GitHub. Backup command executed but exact backup-byte equality not independently checked. Original `JUSUBIN_FAST_HALF_SWB` and QS Copy were not targeted.
- Numerical intent: preserve the old 5 V per time-unit voltage ramp by adjusting 0.3/0.06 to 5/1; note `Transient` time is physical simulation time and this is not a steady-state QS. Not yet validated for high-bias convergence/current/IQE. The old 0.3V smoke comment in source may remain stale.
- NEXT: in the copied SWB project select SDevice Node 2 and run Ctrl+P preprocessing only; check generated `pp2_des.cmd` for actual FinalTime=1.0, anode Goal Voltage=5.0, Save prefix and expected mesh/physics/NtSide before F7. Do NOT run 5V yet; check that copied project prep is independent from original.


## 2026-10-09 — 5V_TEST SDevice preprocess output verified
- 작업자: 이택규. OBSERVED from terminal `JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd` grep: executable `Transient(` line 585, `FinalTime=1.0` line 587, `Goal Voltage=5.0` line 597, generated Save prefix `n2_5V_ckpt` line 608. Initial anode/cathode electrode voltages remain 0.0 at lines 38/43.
- This confirms 5V edits propagated into a generated preprocessed deck. However, this grep alone does NOT verify output Grid file, effective `NtSide=0` trap substitution, preexisting copied results safety, full physics/solver correctness, or high-bias convergence. 5V SDevice run is NOT yet confirmed launched.
- NEXT before F7: check Grid and parameter/trap substitutions in `pp2_des.cmd`, check `n1_msh.tdr` and existing n2 outputs in copied project (preserve old results if present), then decide whether to start prolonged high-bias 5V transient. If future result Save executes after failed sweep, `n2_5V_ckpt` name alone does not establish 5 V reached.


## 2026-10-09 — Copied 5V test contains old 0.3 V node2 outputs: protect before Run
- 작업자: 이택규. OBSERVED user `ls -lh` in `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST`: `n1_msh.tdr` 1.6M (Oct 8 18:08), `n2_des.log` 1.1M (Oct 9 01:39), `n2_des.plt` 412K (Oct 9 01:39), `n2_des.tdr` 15M (Oct 9 01:39).
- These outputs are inherited from the original 0.3V smoke folder by `cp -a`; they are NOT evidence that 5V has run. A new Node2 Run may overwrite/clear outputs. The original source 0.3V project exists separately.
- User did not include requested grep of preprocessed Grid/Parameter/Conc/RHSMin/Iterations in this message; settings not yet verified for 5V run.
- Next proposed: create a timestamped tar.gz snapshot of entire 5V_TEST directory from parent folder and confirm archive exists; then retrieve missing `pp2_des.cmd` Grid/trap/solver grep before deciding F7. Do not claim backup succeeded until terminal verifies. Preserve original smoke/QS branches.


## 2026-10-09 — 5V copied Half/Coarse transient backup and Grid/Trap preflight observed
- 작업자: 이택규; 상태: OBSERVED from user's terminal (archive integrity check pending; 5V run NOT YET observed).
- At `/user/semi/semi437/tmp/myproject`, user executed `tar -czf JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz JUSUBIN_FAST_HALF_5V_TEST`; `ls -lh` confirms archive 12M, timestamp Oct 9 11:25. This is an existing compressed project snapshot made *after* 5V source edits, containing copied old 0.3V outputs; not a verified successful 5V result. Archive contents/integrity have not yet been independently checked with `tar -tzf`.
- In copied project `pp2_des.cmd` grep: Grid=`n1_msh.tdr` line20; 12 displayed region-level `Conc=0` lines145–365; RHSMin=1e-3 line510; startup Coupled Iterations=500 and 100; sweep `Coupled(Iterations=15)` line600. Earlier pp2 verification showed executable Transient, FinalTime=1.0, Goal anode=5.0, Save prefix `n2_5V_ckpt`.
- Original 0.3V smoke and separate QS Copy preserved. Current blocker: archive integrity check and launching SDevice Node2 only in copied SWB; don't launch SDE or modify original. 5V high-bias numerical/physical validity, IQE, I-V, mesh/symmetry equivalence are not established. Allow initial run only as exploratory independent branch, with output/log monitoring and no runtime/accuracy promise.
- NEXT: `tar -tzf ../JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz > /dev/null` and `echo $status` (C-shell-compatible; 0 expected); then copied SWB Node2 SDevice Run F7 only; inspect new n2_des.log/err after startup, verify no immediate failure and logs no longer Oct 9 01:39 copied outputs.


### 2026-10-09 archive check
- 이택규 verified tar listing of JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz: C-shell status 0.
- 5V SDevice Node2 startup is now next; F7 launch not yet observed. Original projects preserved.


## 2026-10-09 — SWB copied 5V project GUI state ambiguous; do NOT clean node yet
- 작업자 이택규. OBSERVED screenshot: SWB title/path `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST` (T-2022.03), copied project selected in tree, SDE and SDEVICE stages present, NtSide=0, SDE/SDEVICE cells show `--` (no unambiguous running/completed status).
- User asks whether a job is already running and whether to Clean Up Node. No actual SDevice active-process, new log, or scheduler run evidence supplied. Inherited n2_des.* files are old 0.3V smoke results copied earlier.
- Guidance: hold Clean Up Node and F7 until check; cleanup can remove copied node outputs, possibly mesh/dependency and confuse active jobs. Ask user to run `ps -fu semi437 | grep '[s]device'`, `ls -lh --full-time n2_des.log`, `tail -n 12 n2_des.log` in 5V_TEST, then decide. Also if no sdevice process, SWB Scheduler could still have queued job; inspect scheduler status before cleanup.
- Archive tar integrity was confirmed (`tar -tzf`, status 0) and 5V preprocessed source verified, but run status currently UNKNOWN, not started claim.


## 2026-10-09 — 5V copied project Node2 not running; old 0.3V log confirmed
- 작업자: 이택규; OBSERVED user terminal from `JUSUBIN_FAST_HALF_5V_TEST`.
- `ps -fu semi437 | grep '[s]device'` showed ONLY two old active sdevice processes: PID 69457 running `pp6_des.cmd` since Oct04, and PID 93915 running `pp12_des.cmd` since Oct06 (both 99% CPU). No `pp2_des.cmd` SDevice process present in this observed process list. A queued SWB job, if any, was not separately checked.
- `n2_des.log` mtime Oct 9 01:39:13 +0900; its tail says the *old original 0.3V smoke* completed with `Good Bye` Oct9 01:39:13, wallclock 25019.43 s and 2.61GB peak memory. This log was inherited by directory copy and is NOT a 5V result.
- Therefore no indication 5V SDevice Node2 has launched; do NOT Clean Up Node merely to start. Existing pre5V archive readable (tar listing status 0), pp2_des.cmd preprocessed 5V parameters confirmed earlier.
- NEXT: if concurrent machine/license resources are acceptable, select **only** SDevice Node2 in the SWB copied `JUSUBIN_FAST_HALF_5V_TEST` and run F7. Avoid SDE re-run. Monitor fresh `n2_des.log` timestamp and View Output; check convergence and actual attained anode voltage. CPU contention from pp6/pp12 may prolong 5V run. Do not mark 5V started/completed before evidence.


## 2026-10-09 11:33 KST — Copied Half 5V SDevice Node2 launched via SWB
- 작업자: 이택규. OBSERVED in user-supplied SWB Project Log screenshot for `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST`: preprocessor successfully initialized, dependency on node 1 recognized, local submit for job 2, status changed ready -> pending -> running, `11:33:14 Oct 09 2026 job '2' <sdevice> started on host ...`.
- Correct project title/path visible and scenario NtSide=0. This establishes SWB submitted/launched Node2 at the recorded instant, but DOES NOT establish process still alive, solver convergence, 5V reached, I-V or IQE. No new `n2_des.log` contents received since launch.
- Preflight had verified pp2 Transient FinalTime=1.0 Goal anode=5.0V, Grid=n1_msh.tdr, 12 displayed Conc=0, RHSMin=1e-3, inner Coupled Iterations=15, and readable 12MB pre5V archive. Existing unrelated pp6 and pp12 SDevice jobs observed on the same account immediately prior.
- NEXT: do not Clean Up Node or press F7 again. In copied test directory check `ps -fu semi437 | grep '[s]device'`, `ls -lh --full-time n2_des.log`, `tail -n 20 n2_des.log` to confirm fresh process/log and whether simulation is progressing. Avoid interrupting unrelated pp6/pp12 and original smoke/QS projects.

## 2026-10-09 14:29:52 KST — Half+Coarse 5V TEST Node2 COMPLETE (OBSERVED)

- OBSERVED source: user-provided terminal in `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST`, `tail -n 40 n2_des.log` after run. Final anode voltage `5.000E+00 V`, anode electron `2.781E-13`, hole `1.420E-11`, total current `1.448E-11` (terminal output units require current-normalization audit). `Finished, because... Curve trace finished.`, `Sentaurus Device simulation finished`, `Good Bye !` at 2026-10-09 14:29:52 KST.
- OBSERVED files written per log: `n2_5V_ckpt_des.sav`, `n2_5V_ckpt_circuit_des.sav`, `n2_des.tdr`. `wallclock=10596.76 s` (2 h 56 m 36.76 s), total CPU 30641.23 s, peak memory 2.97 GB. `ps` showed only pp6 PID 69457 and pp12 PID 93915; no active pp2 at check.
- Proven: copied **Half+Coarse NtSide=0** Transient Node2 reached 5V and terminated normally. Not proven: publication-grade/common damaged NtSide=1e18 baseline, physical I-V/current-density validity, full-vs-half equivalence, IQE/optical emission, extracted current units, or A/B improvements. Do not treat save filename alone as 5V evidence; here independently supported by final 5V terminal row + normal curve trace.
- Previous 116h extrapolated runtime and 3–7+day planning range are superseded by the **measured 10596.76 s** for this run; reason for fast runtime relative to old 0.3V smoke remains unverified. Do not infer speedup or solver equivalence without source/deck/log comparison.
- NEXT: preserve 5V outputs/checkpoints and current reference pp6/pp12 jobs; inspect `n2_des.plt` for full I-V, ensure actual postprocess unit/AreaFactor/2D symmetry normalization, compare intermediate MQW Rrad/SRH/Auger and carrier/injection with full/fine at matched bias/current; then separate nominal `NtSide=1e18` damage case after controlled preprocess/short-run gate. Project A/B production remains NO-GO pending existing audit.

## 2026-10-09 — Half+Coarse 5V_TEST output artifact and PLT schema gate (OBSERVED / partial PASS)

- 이택규 user terminal in `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST`: `ls -lh --full-time` confirms `n2_des.plt` 412K (mtime 14:29:52), `n2_des.tdr` 16M (14:29:53), `n2_5V_ckpt_des.sav` 3.2M (14:29:50), and `n2_5V_ckpt_circuit_des.sav` 306B (14:29:50). Artifacts correspond temporally to observed normal 5V finish at 14:29:52; contents of .tdr/.sav not independently decoded.
- `head -n 30 n2_des.plt` confirms `DF-ISE text` and 17 datasets: time, cathode/anode outer/inner voltage, quasi-Fermi, displacement current, electron/hole/total current, and charge. Full PLT data trajectory/last row NOT YET PARSED; do not confuse schema presence with verified IV physical correctness.
- `grep -ni 'AreaFactor' pp2_des.cmd pp2_des.par` returns `grep: pp2_des.par: No such file or directory`; no `AreaFactor` match printed for `pp2_des.cmd`. Missing `pp2_des.par` is a parameter-path audit item, not evidence of SDevice failure. Actual parameter reference and 2D area/current normalization still UNRESOLVED.
- NEXT (read-only): parse PLT as 17-field data records, report first/last V and current, full I–V and voltage monotonicity; inspect `Parameters` reference from `pp2_des.cmd` and actual `*.par` files before any A/cm2 normalization. Preserve outputs and other pp6/pp12 jobs.

## 2026-10-09 — Half+Coarse 5V_TEST PLT 1023-point I–V readout and Parameters path confirmed (OBSERVED)

- 작업자: 이택규. User ran read-only awk across `n2_des.plt` DF-ISE Data with 17 fields per record: `ROWS=1023`, `REMAINDER=0`, first anode OuterVoltage 0 V, last exactly 5.00000000000000E+00 V; last anode TotalCurrent (raw printed) 1.44801646079583E-11. This confirms a fully parsed 17-column series from 0 to 5V but not yet its physical current units or validity.
- Sampled voltage/raw total current pairs: (0 V, -9.34556980161972E-27), (0.503368865 V, 5.81275673304787E-15), (1.003368865 V, 6.13100514338505E-15), (1.503368865 V, 7.84214693612489E-15), (2.003368865 V, 1.31567117783539E-14), (2.503368865 V, 2.84645414227297E-14), (3.003368865 V, 3.17582117791696E-14), (3.503368865 V, 3.28516927136479E-14), (4.003368865 V, 3.50552134304176E-14), (4.503368865 V, 3.69335070901735E-13), (5V, 1.44801646079583E-11). Sample points show pronounced rise above ~4V, not evidence of confirmed LED emission or normal operating current; full 1023-point monotonicity not checked.
- `pp2_des.cmd` File block points to `Grid="n1_msh.tdr"`, `Parameters="FASTC1_pp6_des.par"`, `Plot="n2_des.tdr"`, `Current="n2_des.plt"`, `Output="n2_des.log"`. User `find . -maxdepth 1 -type f -name '*.par'` returned `./FASTC1_pp6_des.par`. Therefore absent `pp2_des.par` is explained by correct alternate parameter filename. Parameter *contents*, AreaFactor absence across all active sources, radiative coefficient and steady-state-vs-transient interpretation not yet verified.
- Source header comments claim staged 0–4 / 4–5V with multiple checkpoint saves, but previous actual executable Solve was a single 0–5V transient and log showed end Save only; comments cannot substitute for active code. Do not assert multi-stage operation from comments.
- NEXT: read-only inspect `FASTC1_pp6_des.par`, actual `pp2_des.cmd` Physics/Plot and any AreaFactor; establish semiconductor radiative coefficient/output fields, 2D width and current scaling; then evaluate MQW Rrad/SRH/Auger and terminal carrier-current consistency using `n2_des.tdr`. Do not modify working code, clean up, or rerun as part of audit. NtSide=0 endpoint success does not validate damaged NtSide=1e18 or final common baseline.

## 2026-10-09 — Half+Coarse 5V endpoint contact-current components and recombination declarations (OBSERVED / emission UNRESOLVED)

- 작업자: 이택규. User provided direct terminal outputs from `JUSUBIN_FAST_HALF_5V_TEST`: last DF-ISE PLT record `time=1.00000000000000E+00, V=5.00000000000000E+00`. Anode raw `DisplacementCurrent=3.29132361382365E-18`, `eCurrent=2.78143237811134E-13`, `hCurrent=1.42020180788235E-11`, `TotalCurrent=1.44801646079583E-11`. At final step, terminal displacement contribution is negligible relative to total; anode hole current dominates. This does NOT establish MQW hole injection or steady-state across complete device.
- Actual parameter linkage confirmed: `pp2_des.cmd` uses `Parameters="FASTC1_pp6_des.par"` and `find` locates that exact file. User `cat FASTC1_pp6_des.par` shows only `LatticeParameters`, `Thermionic Formula=1`, and GaN Mg active-species `Ionization`; **no explicit Radiative coefficient in this parameter file**. Material database / other effective settings may still supply parameters: do not infer radiative coefficient=0 from this absence.
- User `grep -niE 'AreaFactor|Radiative|SRH|Auger|Recombination|CurrentPlot' pp2_des.cmd FASTC1_pp6_des.par` shows SDevice Physics `Recombination(SRH(), Auger(), Radiative)` at pp2 lines ~78–84, and Plot datasets `SRHRecombination`, `RadiativeRecombination`, `AugerRecombination` ~398–408. No AreaFactor match in these two files. These are code/model/output declarations, **not proof that any MQW Rrad is positive, integrated, or emitted light**.
- Prior Synopsys T-2022.03 UG audit recorded in `LeeTaekGyu/TIMELINE.md` (2026-10-08; Device UG §16 pp.488–489) cautions non-GaAs radiative-coefficient default may be zero without override; need verify effective GaN/InGaN material coefficients instead of claiming emission. Material database not reviewed in this turn.
- Next: read-only inspect `pp2_des.cmd` Physics/Plot context and `n2_des.log` radiative/material parameter clues, then open final `n2_des.tdr` in SVisual and confirm fully visible `RadiativeRecombination` values inside `Clean_QW1`–`Clean_QW4`; compare SRH/Auger and carrier maps and, when validated, perform spatial integration. Current-density normalization/AreaFactor still unresolved; no code modified, no rerun.

## 2026-10-09 — 5V SVisual radiative field (OBSERVED)

- 이택규 screenshot shows positive RadiativeRecombination in final n2_des.tdr; plot max 7.483e19 cm^-3 s^-1, min about zero (-7.512e-34). Mesh 138194 elements / 65513 points.
- The high-rate thin layers have not been mapped to named Clean_QW1-4, so MQW emission, integrated rates and IQE remain unverified.
- NEXT: SVisual Regions tab identify QWs and probe rates; then SRH/Auger and material radiative coefficient. Preserve results.

## 2026-10-09 — 5V_TEST four InGaN Clean_QW local RadiativeRecombination Probe measurements (OBSERVED; IQE NOT YET)

- 작업자: 이택규. User supplied four direct Sentaurus Visual Probe screenshots in `JUSUBIN_FAST_HALF_5V_TEST` / `n2_des`, with scalar `RadiativeRecombination`, explicit zone label, x/y coordinates and Magnitude (cm^-3 s^-1, unit grounded in preceding SVisual legend).
- `Clean_QW1(InGaN)`: x=0.169818746552, y=0.560459877538, z=0, `Rrad=1.836010164996e+13`.
- `Clean_QW2(InGaN)`: x=0.194326754006, y=0.556958733616, z=0, `Rrad=3.558921779790e+12`.
- `Clean_QW3(InGaN)`: x=0.22058533342, y=0.56571159342, z=0, `Rrad=8.395713573050e+14`.
- `Clean_QW4(InGaN)`: x=0.245093340874, y=0.58321731303, z=0, `Rrad=7.094266327897e+18`.
- Result: **each of four named InGaN QWs contains a positive local Rrad point**, beyond mere output declaration or plot-wide maximum. The QW4 sampled point exceeds sampled other QW values by several orders of magnitude. HOWEVER: points differ in both vertical and lateral coordinates (x/y), so local values are **NOT** region-integrated emission, per-well averages or a verified QW4 total-emission dominance. Do not treat local peak, photon escape, IQE or material radiative coefficient as validated.
- Remaining: check SRH and Auger at the *same probe coordinates*, map Rrad spatially through each QW and perform mesh/region correct integrals, confirm 2D current normalization, injection/current plausibility and half-vs-full correspondence; NtSide=0 branch only. No new solver or source changes.

## 2026-10-09 — QW4 SRH point confirmed; coordinate mismatch with Rrad

- User SVisual Probe: Clean_QW4(InGaN), srhRecombination = 1.681637512936e22 cm^-3 s^-1 at (x,y)=(0.244864017914, 0.599783903626).
- Previous Clean_QW4 Rrad=7.094266327897e18 was at (0.245093340874, 0.58321731303). Same region, different position; direct pointwise SRH/Rrad comparison and IQE are not valid.
- NEXT: Probe SRH and Auger at the exact previous Rrad coordinate and validate integrated QW rates before estimating IQE. No code or model change.

## 2026-10-09 — 5V_TEST co-located Clean_QW4 Probe shows dominant local SRH (OBSERVED; device IQE UNRESOLVED)

- Worker 이택규 provided three SVisual Probe screenshots on the completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des` final TDR. All three are the **same point**: zone `Clean_QW4(InGaN)`, x=`0.244864017914`, y=`0.651958341615`, z=0. This differs from earlier SRH y=0.599783903626 and initial Rrad y=0.58321731303; do not mix old and new point values.
- Same-point fields in cm^-3 s^-1 (screen values): `RadiativeRecombination=7.103015017104e18`; `srhRecombination=1.681575471039e22`; `AugerRecombination=1.238545872618e15`; `TotalRecombination=1.682285896396e22`. Sum agrees with displayed TotalRecombination within screenshot precision.
- Derived **LOCAL radiative fraction only**: `100*Rrad/(Rrad+Rsrh+RAuger)≈0.0422%`; local nonradiative fraction ≈99.9578%; SRH dominates at this sampled point. This is **NOT** full-QW or full-device IQE, nor proof of overall LED performance/failure. QW1–QW3 require corresponding SRH/Auger samples and integrated full-QW volumes for recombination-based IQE.
- Importantly `NtSide=0` disables parameterized damaged-edge traps in this reference branch but does NOT disable the generic `SRH()` bulk nonradiative recombination physics; high QW local SRH does not by itself prove sidewall damage or carbon-project effect. Need inspect active carrier lifetime, material parameters and field/region distribution before root-cause claims.
- NEXT: preserve outputs and avoid rerun; use read-only SVisual integrated QW Rrad/SRH/Auger workflow and compare QW1–4, inspect actual active SRH lifetime and material database, 2D current normalization/physical injection. Use same-bias/current full vs half/fine check before declaring Common Baseline. No TCAD code modified.

## 2026-10-09 — Corrected measurement priority: QW3 probes confirmed, per-region integration needed (OBSERVED / SCIENTIFIC DECISION)

- Worker: 이택규. User submitted SVisual Probe screenshots in the successful `JUSUBIN_FAST_HALF_5V_TEST/n2_des` 5V result. Clean_QW3(InGaN) same location x=0.219173763524, y=0.555622585194, z=0: `RadiativeRecombination=8.333611568957e14`, `srhRecombination=5.390114530106e19`, `AugerRecombination=5.79338765299e8` cm^-3 s^-1. Other captured fields include electron density 1.385821616728e14 and hole density 4.507709343047e11 (units of densities expected cm^-3, panel exact unit not shown). Numerical point checks are local only, no physical IQE claim.
- User correctly identified that publication analysis requires **integrating the recombination rate over each entire QW**, not further collecting isolated probes. Adopt `CMP/PROJECT_AB_PRE_RUN_AUDIT.md` G5 and metric definition: integrate Rrad, SRH, Auger over each QW region, sum integrals, THEN compute recombination-based IQE. Do not average or sum local fractional IQEs. The local QW3 and QW4 probes suggest large SRH at those sampled points but are not representative of whole-well rates.
- First non-destructive operational check: SVisual Tools > Integrate (∫dr right toolbar), field RadiativeRecombination, Region/Material filter Clean_QW3 only, complete spatial domain and Start Integration. Save/report raw integral AND domain units displayed; then integrate same QW's srhRecombination and AugerRecombination and expand QW1..4. Include DmgL_QW regions as appropriate for complete active-QW physical volume and matched full/half comparisons, explicitly avoid counting Clean-only as total QW losses. Two-dimensional SVisual integration produces an area integral with native geometrical units; out-of-plane depth/2D normalization and actual physical cm unit conversion MUST be verified for absolute recombination counts; a ratio of comparably normalized integrals cancels common factors.
- Older and newer Sentaurus Visual User Guides document Field Integration GUI and `integrate_field -field ... -regions {Clean_QW3}`; current environment T-2022.03-specific GUI behavior and output units still require a user screenshot before scripting/automation is treated as validated. No TCAD source or baseline changes or new solver runs.

## 2026-10-09 — 5V SVisual Clean_QW3 Rad field integral and '+' label correction (OBSERVED / UNRESOLVED)

- Worker 이택규 supplied `Field Integration` screenshot for `JUSUBIN_FAST_HALF_5V_TEST/n2_des`: field `RadiativeRecombination`, right pane `Regions of Dimension 2` shows ONLY `Clean_QW3 (InGaN)` with `Integral = 2.657110e+02 [s^-1*um^-1]`, `Domain=5.985012e-03 [um^2]`. This is **Clean_QW3-only 2D area integral**, not full QW3 or total photon output, and NOT IQE. Left list highlights both `Clean_QW3` and `Clean_QW3+DmgL_QW3` but only Clean_QW3 appears in right output, possibly stale result until Start Integration; do not interpret highlighted items as proven integrated.
- **Correction of previous GPT claim:** `Clean_QW3+DmgL_QW3` should NOT be assumed to denote union of bulk regions or selected as sole full-well ROI. Its structure and lack of inclusion in the dimension-2 output indicate it is likely a lower-dimensional boundary/interface label. Exact T-2022.03 metadata for '+' label has not been independently inspected, so interface interpretation remains PROVISIONAL. Safest method: select standalone region `DmgL_QW3` (not '+' named item), click `Start Integration`, verify `Regions of Dimension 2: DmgL_QW3`, record its Integral/Domain, then **sum independent Clean_QW3 and DmgL_QW3** integrals for whole QW3 (or choose both standalone 2D regions and verify both appear in output). Do not double-count interface or mix old results.
- The physical measured rate is 2D area-integrated per out-of-plane unit; raw SVisual [s^-1 um^-1] is NOT absolute 3D photon rate without explicit effective thickness. Same geometric normalization cancels for recombination fraction ratios when all wells are treated consistently; continue SRH/Auger over same 2D set and four QWs before IQE.
- Source: user screenshot Oct9 and earlier GitHub `PROJECT_AB_PRE_RUN_AUDIT.md`, SVisual manual Integration Tool general region-filter procedure. No code or TCAD source modified, no new run.

## 2026-10-09 — QW3 full 2D Radiative integration obtained from separate Clean/Dmg regions (OBSERVED)

- Worker 이택규; user SVisual Field Integration screenshot of completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des`, field `RadiativeRecombination`, `Regions of Dimension 2` explicitly lists **DmgL_QW3 (InGaN)**: `Integral=5.268180e-01 [s^-1*um^-1]`, `Domain=1.500002e-05 [um^2]`.
- Previously directly observed **Clean_QW3 (InGaN)**: `Integral=2.657110e+02 [s^-1*um^-1]`, `Domain=5.985012e-03 [um^2]`.
- These are separate disjoint **2D area region** integrals, so the full QW3 half-device measured raw regional sum = **266.237818 s^-1 um^-1**; total measured 2D domain area = **0.00600001202 um^2**. Arithmetic: 265.711 + 0.526818; 0.005985012 + 0.00001500002. **Derived**, not direct SVisual combined group output.
- This supersedes earlier incorrect idea that '+' item is a merged area. The `Clean_QW3+DmgL_QW3` entry should not be used as integrated 2D union without proof (likely lower-dimensional interface). Not full device IQE/absolute 3D photon rate. At NtSide=0, parametric damaged-edge traps are off, while DmgL_QW3 geometry exists.
- NEXT READ-ONLY: Integrate `srhRecombination` for standalone Clean_QW3 and DmgL_QW3 (or both as explicitly distinct 2D regions with actual Total Integral verification), then `AugerRecombination` same region scope. Keep units and voltage fixed; after all four QWs, compute recombination-based IQE from summed Rrad/SRH/Auger integrals; confirm normalization, full-vs-half equivalence and current physics before declaring baseline.
- No TCAD source edit, no new run; original files and checkpoints retained.

## 2026-10-09 — 5V half TEST DmgL_QW3 spatial SRH integral measured (OBSERVED)

- Worker 이택규 sent direct Sentaurus Visual Field Integration screenshot, Dataset=n2_des, field=srhRecombination, Regions of Dimension 2: **DmgL_QW3 (InGaN)**. Integral `1.655249e+03 [s^-1*um^-1]`, Domain `1.500002e-05 [um^2]`, Total Integral same. This is a verified **2D area-region** integral (per out-of-plane um), not a local Probe point and not combined whole-QW SRH.
- Prior independent DmgL_QW3 Radiative 2D area integral `5.268180e-01 [s^-1*um^-1]` on same region and domain. Observed DmgL segment SRH substantially exceeds Radiative; Auger integral for that area still unknown, so no exact regional radiative share or IQE claim. NtSide=0 does not eliminate generic SRH() bulk recombination; causal attribution to sidewall trap or Project A carbon NOT supported.
- Other prior independent 2D area result Clean_QW3 Radiative 265.711 [s^-1*um^-1]. Current full QW3 total Radiative Clean + DmgL = 266.237818 [s^-1*um^-1]. **Clean_QW3 SRH integral still missing**, so no total QW3 SRH or IQE.
- NEXT read-only GUI: choose `srhRecombination`, select **standalone `Clean_QW3`** (not plus-named 1D interface), press Start Integration and capture result and Domain. Then integrate AugerRecombination over both standalone Clean_QW3 and DmgL_QW3. Verify corresponding area and results before summing for QW3 radiative-recombination ratio. Preserve saved 5V_TEST outputs, no solver/code changes.

## 2026-10-09 — QW3 DmgL Auger spatial integral measured (OBSERVED)

- 이택규 supplied direct SVisual Field Integration screenshot for completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des`: `AugerRecombination` `Regions of Dimension 2: DmgL_QW3 (InGaN)`; `Integral=5.774334e-02 [s^-1*um^-1]`, `Domain=1.500002e-05 [um^2]`.
- Prior directly observed same-region 2D Radiative `0.526818`, SRH `1655.249` [s^-1 um^-1] and same Domain. Therefore DmgL_QW3 has all 3 regional integrals and SRH dominates *this segment*. At `NtSide=0`, generic SRH remains active; do NOT attribute to parameterized edge traps or infer full QW/device IQE.
- The earlier request was `Clean_QW3` SRH; user instead measured DmgL_QW3 Auger, which is useful and preserved. Still missing standalone `Clean_QW3` SRH and Auger for full QW3 radiative-vs-nonradiative integration. Clean_QW3 Radiative=265.711 [s^-1 um^-1]. NEXT: switch field `srhRecombination` + select only standalone `Clean_QW3` + Start Integration, screenshot. Then `AugerRecombination` + standalone `Clean_QW3`, repeat. No code edits or rerun.
