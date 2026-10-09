## 2026-10-08 — 주수빈 Half+coarse QS performance test ready (PROPOSED)

- Existing accelerated SDE half+selective-coarse mesh PASS: 138,194 elements / 65,513 points; SWB SDE done.
- Half+coarse 0→0.3 V *Transient* smoke actually running/accepted at about 0.0083 V; one step wallclock 109.74 s (solve 90.20 s), so runtime blocker persists despite smaller mesh.
- Separate `Quasistationary` 0→0.3 V test deck generated and statically audited PASS (SHA256 `a7281c79e7e440c6192726f4ce6edefb58f8d76ed30ec921900fee5ff5a5ec01`). Solver execution not started; correctness/runtime unverified.
- New branch only; original full FAST_C1 reference protected. Next: old half-transient smoke clean stop/backup if switching → QS preprocess → QS short run → compare time/convergence/current.

## 2026-10-08 — cmp216 FAST_C1_ACCOUNT_TEST n6 logging stopped during new BE-step (OBSERVED / TERMINATION CAUSE UNRESOLVED)

- cmp216 ssudisu2 cross-account Node6 test shows successful step at 0.9534V then `n6_des.log` ends after next BE-step iteration header; no normal termination/fatal/killed signature found in log. Log/PLT last modified Oct 7 ~17:47/17:45; current date Oct 8. Local `sdevice` process absent as separately observed. Status: **not currently progressing on checked host**, reason **UNRESOLVED** (session hangup/job termination/remote host etc not evidenced).
- No final TDR; cross-account runtime improvement cannot be confirmed at <1V. Verify process/session/job history before rerun.

## 2026-10-08 — cmp216 FAST_C1 cross-account benchmark: local run apparently inactive near 0.9534 V

- 작업자: 이택규; 상태: OBSERVED / TERMINATION CAUSE UNRESOLVED.
- `cmp216@ssudisu2` in `~/FAST_C1_ACCOUNT_TEST`: last accepted Node6 anode voltage 0.9534 V at 2026-10-07 file mtime; next BE-step starts in `n6_des.log` but no completion shown in terminal tail.
- `n6_des.log` last modified 2026-10-07 17:47, `n6_des.plt` 17:45; no local cmp216 `sdevice` process observed on ssudisu2 on Oct 8; no `n*_des.tdr` found.
- Cannot identify interruption cause or conclude cross-account performance. Do not restart until output/status review; original `semi437` reference run is separate and must not be stopped.
- Evidence: user supplied `ls -lhtr`, `tail -n 80 n6_des.log`, earlier `ps` output.

## 2026-10-07 — Project A/B production pre-run audit: Baseline parent OK, broad A/B run NO-GO

- 작업자: 주수빈
- 상태: REVIEWED / PRE-RUN GATE
- FAST_C1/Common Baseline은 Project A/B parent로 유지 가능. physical baseline 재구축 사유 없음.
- 다만 broad multi-day A/B run은 다음이 끝날 때까지 NO-GO:
  - actual active preprocessed deck/output dataset audit
  - tested spatial integration/extraction workflow
  - current-density normalization
  - A Cedge parameterized geometry/mesh/physics/null-control
  - B vertical-span decision + parameterized AlBarrier/mesh/null-control
  - Save/Load smoke
  - one representative pilot per project
- detailed audit: `CMP/PROJECT_AB_PRE_RUN_AUDIT.md`.

## 2026-10-06 — Revised C2 smoke started; premature duplicate Load tests detected

- 작업자: 이택규
- 상태: OBSERVED / SMOKE RUNNING
- revised C2 smoke generator hash matched expected `c39925d5...030c`.
- generated smoke deck shows D2-approved policy: segment1 Iterations=15, Increment=1.2; Save at 0.2 V; segment2 Iterations=15, Increment=1.05.
- smoke SDevice PID 13881 started successfully and was still in the initial Poisson solve at the captured log; no checkpoint file had yet been created in the shown listing.
- before smoke completion/checkpoint creation, two restart-check jobs were accidentally launched from the shell: PIDs 14179 and 14180.
- these duplicate Load tests must not be used as evidence; stop/ignore them if still alive, then wait for smoke Save checkpoint creation before performing a single Load check.
- next: verify only c2smk_des process remains, monitor c2smk.out, confirm c2smk_ckpt_0p2V* exists, then launch exactly one restart check.

## 2026-10-06 — D6 complete: current C1 intermediate restart rejected

- 작업자: 이택규
- 상태: OBSERVED / D6 COMPLETE / OPTION 3 REJECTED
- scratch Load test used Node 6 `n6_inter_0004_des.tdr` (~4.7 V) with copied mesh/pp files and a check-only restart deck.
- SDevice parsed `Load(FilePrefix="n6_inter_0004")`, found and read `n6_inter_0004_des.tdr`, then terminated with `contains no SLP information !` and exit code 5.
- conclusion: the existing C1 `Plot(-Loadable)` intermediate is not a restart checkpoint. Option 3 is closed for the current Node 6 run.
- live Node 6/12 reference runs were not stopped and were unaffected.
- the D6 job successfully checked out SDevice/hetero/parallel/trap licenses before the load failure, so the test was not blocked by license availability at that moment.
- next strategy: Option 2 only — keep C1 references running and validate a new C2 smoke that prospectively creates a real `Save` checkpoint, then tests `Load` from that Save-generated file.
- D2 policy remains: first common C2 keeps `Iterations=15`; `Increment=1.05` is the first high-bias runtime lever.
- new public helper added: `CMP/tcad/tools/make_c2_smoke_deck.py` (PROPOSED; Python syntax/synthetic text transformation tested). Full proprietary deck remains off GitHub.

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

## 2026-10-06 — D2 complete: Iterations=8/10 rejected as a universal C2 cap

- 작업자: 이택규
- 상태: OBSERVED / DECISION
- current log snapshots audited with `sdevice_newton_audit.py`.

### Node 6 (NtSide=0)
- attempts=3957, accepted=3311, rejected=645.
- accepted Newton histogram:
  - 2 iters: 2378
  - 3 iters: 778
  - 4 iters: 155
- accepted max = 4.
- predicted false rejections:
  - N=5/6/8/10: 0
  - N=15: 0
- measured attempt wallclock in parsed snapshot:
  - total 190868 s
  - accepted 87377 s
  - rejected 103491 s
  - rejected fraction ≈54.2%.

### Node 12 (NtSide=1e18)
- attempts=1325, accepted=1223, rejected=101.
- accepted Newton histogram:
  - 2: 329
  - 3: 815
  - 4: 60
  - 5: 13
  - 7: 4
  - 13: 1
  - 15: 1
- accepted max = 15.
- predicted false rejections:
  - N=5: 6
  - N=6: 6
  - N=8: 2
  - N=10: 2
  - N=15: 0
- first cap-induced trajectory divergence for N<=10 appears around 4.195 V.
- parsed attempt wallclock:
  - total 44143 s
  - accepted 31939 s
  - rejected 12204 s
  - rejected fraction ≈27.6%.

### Decision
- Claude C2 proposal `Iterations=8` is NOT accepted as a universal/common-baseline high-bias cap.
- `Iterations=10` is also not evidence-safe for Node 12.
- first publication-oriented C2 candidate should keep `Iterations=15` for both NtSide=0 and NtSide=1e18, while testing `Increment=1.05` as the first high-bias runtime lever.
- the previously recorded full C2 deck SHA-256 `b876f614424202e6deaf0655411d7bc15733095da297c1df9ca5ebaacbb578d1` contains Iterations=8 in high-bias segments and is therefore **REJECTED FOR EXECUTION AS-IS**; retain only as provenance.
- optional later optimization: NtSide=0-specific cap=8 branch may be benchmarked separately, but it must not be treated as the common C2 numerical policy without separate validation.
- next: inspect the two Node 12 accepted attempts requiring >8 iterations, then proceed to D3 current normalization / J-window gate.

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

## 2026-10-06 — Node 6 reached 4.703 V; 4.7 V intermediate TDR confirmed

- 작업자: 이택규
- 상태: OBSERVED / RUNTIME EVIDENCE
- direct terminal evidence from active FAST_C1 Node 6:
  - intermediate snapshots written successfully at pseudo-times 0.80, 0.84, 0.88, 0.92, 0.94, corresponding to 4.0, 4.2, 4.4, 4.6, 4.7 V.
  - newest confirmed snapshot: n6_inter_0004_des.tdr at 4.700 V.
  - current log tail advanced to pseudo-time 0.940668 = 4.70334 V.
  - recent accepted steps: 7.2336e-06 and 8.6804e-06 pseudo-time, equivalent to about 36.2 and 43.4 microvolts per accepted voltage step.
  - each accepted solve converged in 2 Newton iterations after the initial row and took about 22.6 s wallclock.
  - RHS converged below 1e-3; the run is not stalled.
- important provenance: n6_des.tdr has timestamp 2026-09-24 and is stale relative to the current FAST_C1 run; current spatial evidence is in n6_inter_*.tdr.
- interpretation: dominant blocker remains timestep collapse / poor timestep recovery, not per-step Newton cost.
- if the current 7.2e-6 to 8.7e-6 step scale never recovers, a no-rejection constant-step extrapolation alone would require roughly 43-52 additional hours to 5 V; this is not a completion ETA, only a bottleneck-scale estimate.

## 2026-10-06 — Node 6 / Node 12 actual runtime paths confirmed

- 작업자: 이택규
- 상태: OBSERVED / DIRECT PROCESS EVIDENCE
- ps -fu semi437에서 두 SDevice run의 실제 경로와 process chain을 직접 확인.
- Node 6 (NtSide=0):
  - project: /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1
  - gsub PID 69166
  - gjob PID 69396
  - sdevice PID 69457
  - command: sdevice --max_threads 4 pp6_des.cmd
- Node 12 (NtSide=1e18):
  - project: /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1_Copy
  - gsub PID 93737
  - gjob PID 93864
  - sdevice PID 93915
  - command: sdevice --max_threads 4 pp12_des.cmd
- 두 SDevice process 모두 CPU 99%로 active.
- Node 12 exact project path가 이제 확인되었으므로 기존 VERIFY NEEDED path blocker는 해소.
- 다음: 각 project에서 source/preprocessed cmd/par/mesh/log provenance를 실제 파일 기준으로 확인.

## 2026-10-06 — CRITICAL DEADLINE: abstract due Oct 23; runtime is now primary blocker

- 작업자: 이택규
- 상태: DECISION / BLOCKER
- 사용자 명시: 논문 초록 제출 마감은 2026-10-23.
- 현재 primary blocker는 node failure 자체가 아니라 multi-day runtime/high-bias timestep collapse로 인해 Common Baseline 및 A/B 결과 확보가 일정에 맞지 않을 위험이 큰 것.
- FAST_C1 Node 6과 별도 Node 12는 가능한 한 reference evidence로 계속 보존하되, 완주만 기다리는 전략은 중단.
- 오늘부터 병행: exact same physics/mesh를 유지한 numerical-only acceleration branch를 short benchmark로 검증.
- 우선 후보: DC sweep용 Quasistationary 또는 staged continuation, existing converged state 재사용/Save-Load, bias segmentation, thread/I/O benchmark. T-2022.03 지원 syntax는 공식 자료와 실제 preprocess/log로 검증 후 사용.
- 금지: 논문 일정 때문에 SRH/trap/polarization/geometry를 임의 제거하거나 convergence criterion을 검증 없이 완화.

## 2026-10-06 — Node 12 appears to be running normally by Workbench F7 check

- 작업자: 이택규
- 상태: USER-REPORTED / OBSERVED VIA WORKBENCH
- 사용자가 Workbench에서 F7로 확인했을 때 별도 Node 12 run이 정상적으로 돌아가는 것으로 보인다고 보고함.
- 현재 계획:
  - Node 6 (NtSide=0): 기존 FAST_C1 run 계속 유지
  - Node 12 (NtSide=1e18): 별도 병렬 run 계속 유지
- 아직 Node 12의 solver log/process output은 직접 검증하지 않았으므로 CONFIRMED running으로 승격하지 않음.
- baseline 두 run이 진행 중인 동안 physics/numerical settings를 추가 변경하지 않음.
- 다음 검증 시점: Node 12 n12_des.out/process 확인 또는 어느 한 node 완료 시점.

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

## 2026-10-06 — Node 12 separate parallel run started by user

- 작업자: 이택규
- 상태: USER-REPORTED / VERIFY NEEDED
- User reports that a separate copied project/file for Node 12 (NtSide=1e18) has been started in parallel while FAST_C1 Node 6 continues.
- Exact new project path, source hash, pp12_des.cmd/par provenance, and initialization success are not yet directly verified.
- Do not mark Node 12 as CONFIRMED running until process/log evidence is checked.
- Intended purpose: reduce wall-clock schedule by parallelizing the two Common Baseline branches.
- Publication-grade baseline conditions remain unchanged; no physics/convergence relaxation is authorized by this action.

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


## 2026-10-09 11:30 KST update
- OBSERVED (user report): `JUSUBIN_FAST_HALF_SWB` run completed overnight.
- Previous blocker "half+coarse transient still running" is cleared at report level.
- Verification gate remains: confirm final 0.3 V, no fatal termination, output artifacts, and extract runtime/I-V before treating the run as a validated result.


## 2026-10-09 — Half transient completed, QS Copy MinStep failure
- OBSERVED: `JUSUBIN_FAST_HALF_SWB` original transient completed `Curve trace finished` at 0.300 V, wallclock 25019.43 s, and wrote n2_des.plt/tdr/sav. I-V 0.3 V very low current; full LED turn-on/IQE/reference equivalence not yet validated.
- UNRESOLVED: distinct `JUSUBIN_FAST_HALF_SWB_Copy` QS run ended with `Step-size less than MinStep (step-size = 8.3986e-07)` after 18417.09 s (5:06:57); wrote sav/tdr and `Good Bye`, but goal 0.3 V is NOT verified. Do not call it successful or faster than transient.
- Current blocker: obtain last accepted QS bias and diagnose rejected steps/Newton using QS n2_des.plt/log/err.


## 2026-10-09 — QS Copy last accepted bias determined
- 작업자: 이택규. OBSERVED from user-provided `JUSUBIN_FAST_HALF_SWB_Copy/n2_des.plt` tail and `n2_des.log` grep.
- Last recorded QS pseudo-time: 6.43487876313307E-02; last anode OuterVoltage: 1.93046362893992E-02 V (0.0193046363 V; 19.3 mV, only ~6.435% of requested 0.3 V).
- Last log attempts at t=0.0643488 to 0.0643505 then terminated `Step-size less than MinStep (step-size = 8.3986e-07)`.
- QS runtime 18417.09 s but did NOT reach goal. Cannot compare as speedup to original transient that reached 0.3 V in 25019.43 s.
- Root numerical/physics trigger not yet established. Next: inspect QS log around lines 6900-7000 and `n2_des.err`; no blind MinStep or baseline modification.


## 2026-10-09 — QS Copy nonlinear convergence failure mechanism
- OBSERVED: last QS Copy step failed after 15 iterations, with large oscillating Newton residuals (RHS up to ~1.26e8); following cutback 8.3986e-7 below min 1e-6. Hence QS stopped near 0.0193046363V; this is not a valid 0.3V runtime result. Underlying numeric/physical cause UNRESOLVED. E0 material model mismatch warning appears but direct causal connection unproven. Original half transient completed 0.3V; baseline equivalence not validated.


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


## 2026-10-09 — Half 5V test directory copied; SWB recognition pending
- 작업자: 이택규 / 상태: OBSERVED (terminal), UNRESOLVED (SWB project opened)
- User running shell appears C-shell-like: earlier provided Bash `if [ ! -e ... ]; then` led to `if: Expression Syntax.` and `then/fi: Command not found.` No basis to treat those syntax errors as file copy failure.
- A standalone `cp -a JUSUBIN_FAST_HALF_SWB JUSUBIN_FAST_HALF_5V_TEST` was issued. `ls -ld JUSUBIN_FAST_HALF_5V_TEST` confirms copied folder exists. `cmp JUSUBIN_FAST_HALF_SWB/sdevice_des.cmd JUSUBIN_FAST_HALF_5V_TEST/sdevice_des.cmd` produced no output, verifying those two files are byte-identical.
- This is NOT yet verified as a SWB-opened project. SWB project recognition depends on copy of hidden `.project` metadata (described in Sentaurus Workbench User Guide, N-2017.09); check `ls -la` and `.project` in original/copy. If project metadata present, use SWB Projects browser to open or `swb /path/to/project &` for a separate view; no simulation launch.
- Preserve original smoke and QS Copy; copied test must remain separate and unmodified until SWB registration and inputs validated.


## 2026-10-09 — SWB `.project` files verified in original and 5V test copy
- 작업자: 이택규; OBSERVED in user terminal `ls -la JUSUBIN_FAST_HALF_SWB/.project JUSUBIN_FAST_HALF_5V_TEST/.project` from `myproject`.
- Both `.project` files exist, zero bytes, each mode `-rw-r--r--`, timestamp Oct 8 16:58; the 5V test is an actual copy with SDevice source previously compared identical.
- This supports SWB project marker preservation, but SWB GUI successful open, flow nodes, and project paths are NOT yet confirmed.
- Next: in existing SWB GUI locate/open `JUSUBIN_FAST_HALF_5V_TEST`, screenshot the project flow and verify independent folder before any source edits, preprocessing or Run/F7. Original smoke project remains preserved.


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


## 2026-10-09 — Concept-study focus: Baseline qualification and Project A Carbon implementation
- 작업자: 이택규; USER says hands-on TCAD temporarily unavailable and requests conceptual study. Existing 5V_TEST SWB Node2 launch was observed earlier, but no new log/process evidence of current progress; do NOT assume run stopped or completed.
- CONFIRMED from CMP/PROJECT_AB_PRE_RUN_AUDIT.md and JuSubin/TIMELINE.md: 5V arrival alone is NOT a publication-ready Common Baseline. Half+coarse NtSide=0 is trap-off control; final validation requires consistent NtSide=1e18 nominal damaged reference, full-vs-half mesh/geometry and convergence checks, unbiased same-current I/Vf, MQW Rrad/RSRH/RAuger, integrated sidewall SRH and IQE/injection/current-crowding, and 2D current normalization. Common baseline parent FAST_C1 usable candidate, Project A/B production still NO-GO until gates.
- Project A 1st-stage TCAD is NOT carbon implantation process simulation. Geometry defines GaN `Cedge_L/R` immediately inside preexisting 5nm Dmg_L/R region, first test upper n-GaN under MQW; SDevice implements distinct C-related deep acceptor/trap/compensation physics (nominal literature anchor C_N approx Ev+0.9eV with variable capture cross sections), donor/compensation slot, explicit GaN region boundary meshing, A-null carbon-off control. Half domain retains one physical sidewall and one center symmetry boundary, not two Cedge regions in half representation.
- Carbon ion implantation is a possible physical fabrication option BUT not decided as exact process route and requires separate depth/lateral profile, implantation damage/activation/recovery study; don't call current Stage1 model simulated implantation or proven fabrication. Hypothesis is steering current away from sidewall to reduce SRH and improve IQE; may also increase Vf/reduce injection, not demonstrated.
- NEXT while user studies: explain C incorporation vs ion implantation and electrically compensated semi-insulating GaN:C, distinguish A mechanism-screen from future SProcess/process-realistic study; no TCAD changes requested. Once TCAD accessible review actual 5V_TEST log and baseline comparator, not rerun/cancel based on conversational assumption.

## 2026-10-09 — Half+Coarse NtSide=0 5V simulation completed; publication Baseline validation pending

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

## 2026-10-09 — 5V Half+Coarse SVisual RadiativeRecombination field visible, QW attribution pending (OBSERVED)

- 작업자: 이택규. User shared Sentaurus Visual T-2022.03 screenshot, project title `JUSUBIN_FAST_HALF_5V_TEST`, data `n2_des`, selected scalar `RadiativeRecombination` (not only an output-deck declaration). Colorbar displays max `7.483e+19 cm^-3*s^-1` and minimum `-7.512e-34 cm^-3*s^-1` (numerically ~0). Therefore the **displayed spatial field includes nonzero positive radiative recombination** at the plotted state. Note values are 3D volume-rate density and do not imply integrated photon rate or EQE.
- Spatial map shows high rate in several thin **top** layers and near-zero deep bulk. Individual colored layers are not yet labelled as Clean_QW1–Clean_QW4. Screenshot top Data Selection was `Lines/Particles`, not a visible region-isolation of each InGaN QW. Hence precise QW rate, total QW-integrated radiative recombination, meaningful LED optical emission, efficiency/IQE, material coefficient C, and carrier balance are **not yet verified**.
- Bottom status: `Elements=138194`, `Points=65513`, consistent with accelerated Half+Coarse SDE mesh provenance. The screenshot is direct evidence for field visualization, not a quantitative integration of MQWs or a comparison against reference Full/fine.
- NEXT: in SVisual, open `Regions` tab and identify/visually isolate `Clean_QW1`–`Clean_QW4` while keeping RadiativeRecombination selected; zoom near top quantum-well stack, verify region names and use Probe to obtain numerical QW values. After check, inspect SRH/Auger spatial distributions and integrated rates. Preserve current saved data/other active jobs; do not launch new run. Material radiative coefficient and 2D current normalization remain unresolved.

## 2026-10-09 — 5V_TEST four InGaN Clean_QW local RadiativeRecombination Probe measurements (OBSERVED; IQE NOT YET)

- 작업자: 이택규. User supplied four direct Sentaurus Visual Probe screenshots in `JUSUBIN_FAST_HALF_5V_TEST` / `n2_des`, with scalar `RadiativeRecombination`, explicit zone label, x/y coordinates and Magnitude (cm^-3 s^-1, unit grounded in preceding SVisual legend).
- `Clean_QW1(InGaN)`: x=0.169818746552, y=0.560459877538, z=0, `Rrad=1.836010164996e+13`.
- `Clean_QW2(InGaN)`: x=0.194326754006, y=0.556958733616, z=0, `Rrad=3.558921779790e+12`.
- `Clean_QW3(InGaN)`: x=0.22058533342, y=0.56571159342, z=0, `Rrad=8.395713573050e+14`.
- `Clean_QW4(InGaN)`: x=0.245093340874, y=0.58321731303, z=0, `Rrad=7.094266327897e+18`.
- Result: **each of four named InGaN QWs contains a positive local Rrad point**, beyond mere output declaration or plot-wide maximum. The QW4 sampled point exceeds sampled other QW values by several orders of magnitude. HOWEVER: points differ in both vertical and lateral coordinates (x/y), so local values are **NOT** region-integrated emission, per-well averages or a verified QW4 total-emission dominance. Do not treat local peak, photon escape, IQE or material radiative coefficient as validated.
- Remaining: check SRH and Auger at the *same probe coordinates*, map Rrad spatially through each QW and perform mesh/region correct integrals, confirm 2D current normalization, injection/current plausibility and half-vs-full correspondence; NtSide=0 branch only. No new solver or source changes.

## 2026-10-09 — 5V_TEST local SRH Probe in Clean_QW4 (OBSERVED; not co-located with earlier Rrad)

- 이택규 supplied SVisual Probe screenshot for `n2_des` 5V test: Zone `Clean_QW4(InGaN)`; selected field `srhRecombination`; (x,y,z)=(0.244864017914, 0.599783903626, 0); SRH = `1.681637512936e+22` cm^-3 s^-1 (field units refer to same SVisual recombination output convention).
- The previous QW4 local `RadiativeRecombination=7.094266327897e+18` was probed at (x,y,z)=(0.245093340874, 0.58321731303, 0). They are in the same named region but have **different coordinates**, especially lateral y. It is invalid to form a local loss ratio or IQE from the two values without co-locating them. The high SRH number is a measured point, not evidence of whole-QW dominance.
- NEXT: in SVisual use Probe At or coordinate entry to probe `SRHRecombination` at the exact earlier QW4 Rrad coordinates and verify zone. Then measure Auger at that same point; subsequently validate spatial integrals for IQE. Preserve outputs; no solver/source modifications.

## 2026-10-09 OBSERVED: 5V half/coarse NtSide=0 SVisual same-position QW4 Probe yields Rrad 7.103015017104e18, SRH 1.681575471039e22, Auger 1.238545872618e15, Total 1.682285896396e22 cm^-3 s^-1. Local radiative fraction around 0.0422%, SRH dominant at this single point. Device IQE and SRH cause UNRESOLVED. Need region integrated rates, material lifetime and J normalization. No new simulation.

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

## 2026-10-09 — QW3 whole-well 2D recombination integrals and derived recombination fraction (OBSERVED + DERIVED)

- Worker: 이택규. User screenshots of Sentaurus Visual Field Integration from successful 5V `JUSUBIN_FAST_HALF_5V_TEST/n2_des`. Newly OBSERVED `Clean_QW3(InGaN)`, Region of Dimension 2: `srhRecombination Integral=5.841611e+05 [s^-1 um^-1]` and `AugerRecombination Integral=1.265704e+01 [s^-1 um^-1]`; both Domain `5.985012e-03 um^2`. Earlier standalone Clean_QW3 Rrad=265.711; DmgL_QW3 Rrad=0.526818, SRH=1655.249, Auger=0.05774334 [s^-1 um^-1], Dmg Domain=1.500002e-05 um^2.
- Independent nonoverlapping **Half-domain QW3 Clean+DmgL** 2D area integral sums [s^-1 um^-1]: Rrad=**266.237818**; SRH=**585816.349**; Auger=**12.71478334**; sum all 3=**586095.30160134**. Derived recombination-based **QW3-only, 5V, NtSide=0 ratio** = 100*266.237818/586095.30160134 = **0.0454256871%**. SRH fraction ≈99.9524049%, Auger fraction≈0.0021694054%.
- Fraction of QW3 SRH integral from Clean region = 584161.1/585816.349 ≈99.71745%; DmgL contribution ~0.28255%. This matters for Project A sidewall-loss hypothesis: high QW3 SRH is not dominated by Dmg region under NtSide=0 in this output. It does NOT diagnose causes; Clean area is also ~99.75% of total QW3 physical cross-section. Generic SRH remains active even when NtSide=0. Need verify effective SRH lifetimes, material radiative coefficients, carrier density, local recombination maps and current normalization before claiming physical LED model is valid.
- **Strict scope**: QW3 recombination-ratio from spatial integrals, NOT whole-MQW/device IQE, EQE, measured experimental light, or proof that damaged NtSide=1e18 device behaves similarly. 2D integrals are per out-of-plane micrometer per SVisual display, common thickness factors cancel in within-device ratios. Full/fine vs Half/coarse and mesh convergence still unverified.
- NEXT: integrate Rrad/SRH/Auger in standalone Clean_QW1 + DmgL_QW1, QW2, QW4; record Region Dimension 2/Domain and compute 4-QW summed IQE. In parallel physical parameter and J-normalization audit; no modifications/re-run now.

## 2026-10-09 — Physical plausibility review after very low QW3 radiative share (OBSERVED vs HYPOTHESES)

- Worker: 이택규 asks whether real LED IQE is similarly low, whether device is incorrectly configured, and whether recombination can occur at QW/barrier interfaces or mesa edge instead of QW interiors. This is an interpretation/audit response, **not a new TCAD measurement**.
- Actual 5V_TEST `NtSide=0` Half/Coarse **QW3 only** Clean+DmgL spatially integrated Rrad=266.237818, SRH=585816.349, Auger=12.71478334 s^-1 um^-1, recombination radiative ratio 0.0454256871%. Device-wide IQE and electrical injection efficiency NOT verified. Rad >0 in all four QWs locally, so physically modeled radiative recombination occurs in InGaN wells; NOT equivalent to confirmed practical LED electroluminescence.
- Of QW3 SRH, 584161.1/585816.349≈99.717% integrated over **Clean_QW3** versus DmgL_QW3≈0.283%. Crucial area context: Clean area 0.005985012/0.00600001202≈99.75%, Dmg≈0.25%; cannot infer defects strongly favor clean core or sidewall merely from integrated shares. NtSide=0 means parametric Dmg trap off, but global SRH() remains active.
- Earlier co-located QW3 Probe x=0.219173763524 y=0.555622585194 has electron density 1.385821616728e14, hole density 4.507709343047e11 cm^-3 (from user panel), a strong local n/p imbalance (single-point only); one working mechanism to investigate is weak hole injection and/or QW polarization overlap. Others: very small 5V terminal current raw 1.44801646079583e-11 with 2D unit/AreaFactor unverified, excessive effective SRH rates / lifetimes, insufficient radiative coefficient/overlap, transient vs quasistationary solver output and mesh sensitivity. Hypotheses only; no cause established.
- Actual user-supplied `pp2_des.cmd` declares `SRH()`, `Auger()`, `Radiative`, and output recombination fields. `FASTC1_pp6_des.par` showed only lattice/Thermionic/Mg active ionization and no explicit Rrad coefficient/lifetime; active SDevice material database or effective parameter paths not checked. Legacy GitHub `CMP/tcad/CURRENT/sdevice2_defect_on.cmd` is NOT source of truth for live 5V_TEST pp2 (avoid confusing).
- Physics: desirable radiative e/h recombination inside InGaN QWs; QW/barrier boundary can exhibit radiative or non-radiative recombination, but interfacial SRH requires corresponding interface traps / relevant bulk SRH near boundary; screenshots cannot attribute to interfaces. DmgL_QW3 is the existing etched mesa-sidewall strip and only one area. Published low-current density InGaN microLED study (PMCID PMC8175512) explains SRH can dominate at low injection; published Nature Communications 2023 10×10 um2 blue microLED reports EQE 3.0% at J=0.1 A/cm2 (DOI 10.1038/s41467-023-36773-w) and IEEE TED 2024 reports passivated device EQE≈25% (DOI 10.1109/TED.2024.3449829). Comparisons are EQE vs *only QW3 recombination fraction*, not apples-to-apples benchmarks.
- DECISION / PRIORITY: Do not freeze baseline, alter SRH lifetimes, or conclude failure solely from 0.0454%; FIRST inspect active pp2 physics, actual InGaN effective radiative/SRH material parameters, 2D current normalization & J(V), QW carrier distribution, and 5V final-state quasi-static consistency. Continue four-QW integrals for true recombination-based IQE, then matched-current NtSide1e18 damaged and Full/fine mesh comparisons; Project A/B production still NO-GO.

## 2026-10-09 — QW4 full Half 2D recombination integrals, Clean+DmgL (OBSERVED + DERIVED)

- Worker 이택규 submitted SVisual Field Integration screenshots from completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des` 5V, NtSide=0. 2D `Clean_QW4(InGaN)` (domain 5.985012e-03 um²), values s^-1 um^-1: Radiative=3.874696e+04 (=38746.96), srh=3.561769e+07 (=35617690), Auger=1.327983e+03 (=1327.983).
- Same field, separately integrated 2D `DmgL_QW4(InGaN)` (domain 1.500002e-05 um²): Radiative=9.876800e+01 (=98.768), srh=2.264962e+05 (=226496.2), Auger=2.414354e+00 (=2.414354). Repeated DmgL Rad screenshot is duplicate, not independent new sample.
- **Derived QW4 complete Half Clean+DmgL integral sums** [s^-1 um^-1]: Rrad=**38845.728**, SRH=**35844186.2**, Auger=**1330.397354**, sum=**35884362.325354**. Recombination-based QW4-only ratio `100*38845.728/35884362.325354=0.1082525242%`. SRH fraction = 99.8880400%; Auger=0.00370746%. Comparatively prior QW3-only same type ratio 0.0454256871%; QW4 is ~2.383 times QW3's ratio, yet SRH dominates both.
- Of QW4 integrated SRH, clean 35617690/35844186.2≈99.3681%, but clean area is ~99.75% of total area; area ratio matters and no defect or sidewall cause can be inferred solely from total shares. All values are modeled 2D normalized integrals at 5V and NtSide0. QW4 ratio is **NOT** the 4-QW/device IQE, EQE, or experimental device efficiency. Physical validity still needs carrier injection, 2D current normalizations, effective radiative/SRH material parameters and mesh/reference comparison.
- NEXT: independently integrate Radiative, SRH, Auger in standalone 2D `Clean_QW1` / `DmgL_QW1` and `Clean_QW2` / `DmgL_QW2` and combine four-QW totals. No source changes, solver rerun, or cleanup. Continue physics audit (live pp2 and material database) before declaring baseline valid.

## 2026-10-09 — QW2 complete 2D Clean/DmgL radiative, SRH, Auger integrals + active physics grep (OBSERVED / DERIVED)

- Worker 이택규 shared six Sentaurus Visual T-2022.03 Field Integration screenshots from the completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des` dataset at 5V, NtSide=0, Half+Coarse. Right pane confirms Regions of Dimension 2 for every selected independent region/field, and common per-region 2D Domains. Units for rate area-integrals [s^-1 um^-1].
- **Clean_QW2(InGaN)** (Domain=5.984982e-03 um²): Radiative=8.331490e+01 (=83.3149), srh=5.464576e+04 (=54645.76), Auger=1.736316e+00 (=1.736316).
- **DmgL_QW2(InGaN)** (Domain=1.499994e-05 um²): Radiative=1.672872e-01 (=0.1672872), srh=1.416049e+02 (=141.6049), Auger=3.800247e-03 (=0.003800247).
- Derived nonoverlapping **full QW2 Half-domain** sums: Rrad=**83.4821872**; SRH=**54787.3649**; Auger=**1.740116247**; All=**54872.587203447** [s^-1 um^-1], Total Area=0.00599998194 um². Derived `IQE_rec,QW2=100*Rrad/(Rrad+SRH+Auger)=0.1521382378%`; SRH share=99.8446906%, Auger share=0.00317119%. IMPORTANT: **QW2-only**, not device IQE/EQE; QW1 pending and physics unvalidated. Comparators QW3=0.0454256871%, QW4=0.1082525242%, all QW-only.
- Same user terminal ran read-only `grep -niE 'Lifetime|Tau|Radiative|SRH|Auger|DefaultParametersFromFile|AreaFactor' pp2_des.cmd FASTC1_pp6_des.par | head -n 90`: `pp2_des.cmd:68 DefaultParametersFromFile`, lines 80/82/84 `SRH()`, `Auger()`, `Radiative`; lines 398–406 desired output fields; NO explicit lifetime/Tau/Radiative coefficient/AreaFactor matched in these two files. This proves model declarations and default-parameter flag but **NOT** the numerical effective lifetime/radiative coefficients; material DB and log remain to be checked. No right to conclude unphysical defaults or that Radiative coefficient is zero without material model verification.
- Next: run QW1 six standalone 2D region integrations (Clean_QW1 and DmgL_QW1, each Radiative/srh/Auger); sum four QW integrals to compute recombination-based full MQW fraction. In parallel inspect actual effective SDevice material SRH/radiative coefficients and 2D terminal J/AreaFactor; do not modify source or rerun, Common Baseline still not frozen, A/B NO-GO.

## 2026-10-09 — Four MQW 5V half-device area-integrated recombination ratios completed (OBSERVED + DERIVED)

- Worker: 이택규. Six direct SVisual `n2_des` Field Integration screenshots completed Clean_QW1 and DmgL_QW1 2D regions at 5V on `JUSUBIN_FAST_HALF_5V_TEST` NtSide=0 Half+Coarse. Clean_QW1, domain=5.985012e-3 um²: Radiative=8.579041e2, srh=7.765839e4, Auger=2.525448e2 [s^-1 um^-1]. DmgL_QW1, domain=1.500002e-5 um²: Radiative=1.946374e1, srh=4.966036e2, Auger=2.309115e0 [s^-1 um^-1]. All six corresponding fields and 2D region names verified from screenshots.
- Derived QW1 complete Half-domain Clean+DmgL: Rrad=877.36784; SRH=78154.9936; Auger=254.853915; Total=79287.215355 [s^-1 um^-1], recombination-based well radiative fraction 1.1065691185%.
- Prior QW2 totals: Rrad 83.4821872, SRH 54787.3649, Auger 1.740116247, well fraction 0.1521382378%; QW3 totals Rrad 266.237818, SRH 585816.349, Auger 12.71478334, well fraction 0.0454256871%; QW4 totals Rrad 38845.728, SRH 35844186.2, Auger 1330.397354, well fraction 0.1082525242%. All original user SVisual screenshots already separately logged.
- **NEW derived four-QW total** (independent Clean and DmgL 2D area integral sums in same units s^-1 um^-1): Rrad=40072.8158452; SRH=36562944.9075; Auger=1599.706168587; total three-rate recombination=36604617.4295138. **MQW recombination-based radiative share = 100*Rrad/Total=0.1094747566%**; SRH share=99.8861550%; Auger share=0.00437023%. QW4 contributed 96.9378547% of measured integrated MQW Rrad. The single-well 1.10657% QW1 ratio must NOT be averaged with other well ratios to get this total.
- **Scope/limitations**: This is only the 4-InGaN-QW recombination-based ratio at one simulated 5V step in the Half+Coarse NtSide=0 2D deck; it is NOT experimental LED IQE/EQE nor complete optical output, injection efficiency, or proof of sound reference physics. SVisual reports 2D integration [s^-1 um^-1], so true absolute total requires depth/current-area normalization. Presence of `DefaultParametersFromFile`, `SRH()`, `Auger()`, `Radiative` in pp2 does NOT establish numerical lifetimes or radiative coefficients. Existing reported endpoint current 1.44801646079583e-11 in n2_des.plt requires dimension/unit validation. High SRH under NtSide=0 and QW4 dominance require material model, hole injection/polarization, steady-state and current normalization audit BEFORE baseline freeze or A/B operation. No 5V data or source modified, no rerun.

## 2026-10-09 — Paper provenance cross-check and MaterialDB load log (OBSERVED / QUALIFIED)

- 이택규 asked whether dimensions and QW stack are all paper-based and supplied fresh read-only `grep -niE 'Radiative|SRH|Auger|Lifetime|Tau|material|parameter|AreaFactor' n2_des.log | head -n 100` for `JUSUBIN_FAST_HALF_5V_TEST`.
- Repository `CMP/COMMON_BASELINE.md` documents a **literature-based representative hybrid TCAD model, not JBD exact pixel/mesa replica**. Documented nominal full geometry: 2D Cartesian planar, mesa width 4.0 um **modeling choice**, computational domain 5 um, numerically defined 0.3um n-base and 0.1um nitride, each sidewall Dmg width 5nm modeled from Wu; n-GaN 4um, p-GaN 120nm, p-Al0.15Ga0.85N EBL 26nm, four In0.15Ga0.85N QWs each 3nm and five GaN barriers each 22nm from Kou 2019. It does **not** claim all settings direct from same publication. The current 5V_TEST Half+Coarse geometry/source was NOT freshly inspected here; do not equate stated nominal to exact current coordinate boundaries without comparing live pp1_dvs.cmd or n1_msh.tdr.
- Primary sources externally confirmed: Kou et al., `Impact of the surface recombination on InGaN/GaN-based blue micro-light emitting diodes`, Optics Express 2019 DOI 10.1364/OE.27.00A643 documents ~445nm emission, four-period In0.15Ga0.85N/GaN with QW 3nm/barrier 22nm, 4um nGaN, 26nm p-Al0.15 EBL, 120nm pGaN; full original paper also includes a 20nm highly doped pGaN contact cap beyond documented baseline vertical stack—verify if full deck implements this before saying exact Kou copy. Wu et al. `Physical mechanisms on the size-effect in GaN-based Micro-LEDs`, Micro and Nanostructures 2023 DOI 10.1016/j.micrna.2023.207542 sets acceptor-like sidewall traps in 5nm damaged strip; Wu's own epitaxy differs (In fraction 0.08, barrier 8nm, nGaN 3.9um), so our baseline intentionally does NOT mix that epi. Chen et al. 2024 DOI 10.1021/acsaelm.4c01540 has an experimental 4x4um mesa, supporting size relevance, but does not establish that JBD's mesa is 4um. JBD official 0.13inch 640x480 documentation explicitly has pixel pitch 4um, **not mesa width** (https://www.jb-display.com/product_des/3.html).
- User `n2_des.log` grep actually showed 338 With SRH-Recombination, 345 With Auger, 346 With Radiative and 417 With default parameters from file; `DefaultParametersFromFile: material GaN: .../MaterialDB/GaN.par` around 804 and `InGaN: .../MaterialDB/InGaN.par` around 951 (also Silicon, InN). Thus material files **were opened/parsed**. No effective numeric SRH lifetime or Radiative/Auger coefficients were established by this grep. `Use Si parameters` at log ~336 requires context; cannot conclude InGaN uses Si because the log separately reads GaN/InGaN material DB. Potential library parameter fallback/interpolation needs direct material file and log context inspection.
- Important physical caveat: numerical trap NtSide=1e18, Et=Ev+0.75 eV and capture sigma 1e-15 cm² were calibration/modeling assumptions in COMMON_BASELINE, NOT direct measured JBD or Wu parameters. Same goes for p active concentration ~3e17 approximations and barrier background doping. 5V Half/Coarse model's MQW integrated recombination radiative share ~0.10947% is observed/derived but low; geometry being literature-motivated does NOT validate material coefficients, current injection, or IQE.
- NEXT read-only terminal gate: inspect `sed -n '264,355p' n2_des.log` around default/Use Si context; read exact material database `InGaN.par`, `GaN.par`, `InN.par` SRH/Radiative/Auger sections and *effective parameter interpolation* or material overrides; inspect live `pp1_dvs.cmd` SDE geometry against literature documented nominal; leave solver/source and baseline unchanged.

## 2026-10-09 — CRITICAL OBSERVED InGaN MaterialDB warning: GaAs-derived recombination parameters require calibration

- 작업자 이택규 provided direct terminal `sed -n '855,925p' /user/tools/synopsys/sentaurus/T-2022.03/tcad/current/lib/sdevice/MaterialDB/InGaN.par` for actual Sentaurus T-2022.03 environment. **Direct vendor material file warning** immediately before Scharfetter SRH / Auger / Radiative sections: `Parameters for the recombination models below were taken from GaAs and require calibration for accurate simulations`.
- The InGaN.par values documented in actual file: `Scharfetter taumin=0,0 [s]`; `taumax=1.0e-9,1.0e-9 [s]`; `Nref=1.0e16,1.0e16 cm^-3`; `gamma=1,1`; `Talpha=Tcoeff=0`; `Etrap=0`. `Auger A=1.0e-30,1.0e-30 cm^6/s`, `B=C=H=0`; `RadiativeRecombination C=2.0e-10 cm^3/s`. The radiative coefficient symbol in par is C (commonly referred to as B in LED ABC notation).
- This is ACTUAL MATERIAL FILE evidence, **not yet complete proof of effective per-In0.15Ga0.85N parameters at the active QWs** (material mixing/overrides and file-precedence audit pending). `n2_des.log` previously observed `DefaultParametersFromFile` for InGaN.par, and SRH/Rad/Auger enabled, without field/doping/temperature-dependent lifetimes. Never automatically infer effective SRH lifetime everywhere equals 1ns without inspecting enabled model and resolved coefficients.
- SCIENTIFIC STATUS: Existing 5V Half+Coarse NtSide=0 recombination-only 4-QW ratio=0.1094747566% with SRH 99.886155%. The GaAs-derived uncalibrated InGaN recombination parameters make physical validity an **explicit calibration blocker**, not proof of a geometrically incorrect Mesa/MQW or sole proven cause of low efficiency. NtSide=0 removes parameterized edge traps, but global SRH() persists. Deep-electrical injection/J normalization, polarization, band profiles, material mixing may also matter.
- DECISION / NEXT: preserve baseline and measured simulation outputs (do not silently tune lifetime to increase efficiency); first verify active log/model parameter precedence `sed -n '945,970p' n2_des.log` and `sed -n '270,310p' n2_des.log`, determine proper In0.15Ga0.85N interpolated/overridden Rrad/SRH/Auger coefficients, verify 2D current injection. Then establish literature-backed parameter calibration and sensitivity with unchanged geometry and documented alternate physics branch only after team approval. No TCAD source edited or rerun in this check.

## 2026-10-09 — Literature cross-check & Baseline rerun GO/NO-GO after 5V_TEST low MQW efficiency (REVIEWED, not new simulation)

- Worker 이택규 supplied actual n2_des.log sections. Observed DefaultParametersFromFile loads T-2022.03 MaterialDB/InGaN.par and InN.par, and ModelParameters FASTC1_pp6_des.par, Grid n1_msh.tdr, Current n2_des.plt; log says no separate Lifetime file. This does NOT mean SRH is off or there is no lifetime: active MaterialDB Scharfetter section provides it. The global default block 'Use Si parameters' / 'Without incomplete ionization' cannot be assigned to active InGaN wells or Mg settings without region context. No override coefficients or final mole-fraction interpolation verified yet.
- **Peer-reviewed basis**: Kou et al. Optics Express 2019 DOI 10.1364/OE.27.00A643 uses Auger 1e-30 cm6/s, SRH numerical lifetime 1e-7 (paper displays unit s^-1, which is inconsistent with lifetime and must be flagged as a likely notation error, not ignored); Baek et al. Nature Communications 2023 DOI 10.1038/s41467-023-36773-w simulation uses SRH 100ns, Radiative 1e-10 cm3/s, Auger 1e-31 cm6/s, with a DIFFERENT 6-QW epitaxy and fitted polarization/interface assumptions. Low-current SRH dominance also discussed in Nanoscale Research Letters 2021 https://pmc.ncbi.nlm.nih.gov/articles/PMC8175512/. None uniquely fixes our model values without calibration.
- **Existing vendor file**: InGaN.par explicitly warns GaAs-derived SRH/Auger/Radiative parameters require calibration; Scharfetter taumax 1e-9 s; Rrad C=2e-10; Auger A=1e-30. File values are not yet proven to be final effective xIn=0.15 parameters. Relative to published 100ns example the file taumax is 100 times shorter, potentially explaining large SRH but not a proved sole root cause.
- Existing 5V NtSide0 Half+Coarse integrated 4 QWs Clean+DmgL: Rrad 40072.8158452, SRH 36562944.9075, Auger 1599.706168587 [s^-1 um^-1], fraction 0.1094747566%. Source no user code changes. QW4 ~96.94% of Rrad integral. 2D PLT terminal current raw =1.44801646079583e-11, dimension and AreaFactor still unresolved. From 2D QW3 area 0.00600001202um2 and QW thickness 0.003um, inferred Half width approximately 2um: **CONDITIONAL** on no scaling and A/um terminal current, J_5V ≈ 1.448e-11 / 2 × 1e8 ≈ 7.24e-4 A/cm2, much less than literature 0.1 A/cm2 low-current example; this is NOT verified operating J.
- **Verdict**: No evidence the nominal four-QW Kou-based geometry itself must be rebuilt; no validation of a publishable absolute IQE/optical LED baseline. Need to resolve active material parameters, low current density, carrier injection/polarization, steady-state validity and Half-vs-Full reference. Current IQE issue **must be addressed or clearly bounded** before using baseline for credible Project A/B SRH/IQE improvement conclusions. Causality not established. No new long run now; original finished files protected.
- **Stage plan** (proposal only): (1) read-only pp2/log/material model precedence and QW In mole interpolation, 2D J and equivalent 2D Half area, carrier/hole density and interface traps; (2) literature-supported calibrated parameter *separate branch* including tau sensitivity 1ns/10ns/100ns as exploratory, not automatic performance tuning; compare at same J and keep nominal sidewall Trap; (3) Short NtSide0 QS/steady + checkpoint pilot, electrical/optical checks; (4) NtSide1e18 matched-current sidewall contrast; (5) Mesh convergence and Full-vs-Half, 4/10/20um and Nt sensitivity for paper; (6) only then freeze revised physical Baseline, Project A/B null-control/pilot and broader DOE. Must not silently alter original source.

## 2026-10-09 — Live pp2_des.cmd partial physics grep: region incomplete-ionization + traps, BE transient (OBSERVED)

- Worker 이택규 sent live read-only terminal output from `JUSUBIN_FAST_HALF_5V_TEST`. `sed -n '55,110p' pp2_des.cmd` confirms `Fermi`, `Thermionic`, `Piezoelectric_Polarization(strain)`, `DefaultParametersFromFile`, `EffectiveIntrinsicDensity(NoBandgapNarrowing)`, `Recombination(SRH(),Auger(),Radiative)`, Masetti/CaugheyThomas/Lombardi mobility, `Aniso`.
- `grep -niE 'IncompleteIonization|MoleFraction|Piezoelectric|Traps|AreaFactor|Quasistationary|Transient' pp2_des.cmd FASTC1_pp6_des.par` finds **IncompleteIonization on pp2 lines 128 and 137**, many **Traps declarations lines 141–361**, `xMolefraction/yMolefraction` plot fields lines 486/488, `Transient=BE` line 515 and `Transient(` line 585. **No visible AreaFactor or Quasistationary in the two scanned files.**
- Interpret conservatively: previous global-default `Without incomplete ionization` log entry does not prove region-specific Mg ionization disabled; need inspect actual Physics scope lines 115–170 and region parameter settings. The presence of Trap statements even for `NtSide=0` does not prove finite active traps; inspect real `Conc`, trap types, region names and possible `0` concentration in actual pp2. `Transient=BE` confirms time-dependent solver, so having reached 5 V and produced normal termination is NOT proof of steady DC equilibrium; compare same-bias QS/hold only after confirming physics and numerical convergence. xMolefraction plot declaration is NOT evidence the actual alloy composition assignment has been checked; verify SDE mesh/material.
- Existing InGaN.par is GaAs-derived and warns lifetime/Rad/Auger need calibration; actual QW effective alloy values, 2D current normalization and SRH model remain unverified. Existing 4-QW recombination share 0.1094747566% cannot be used as validated experimental IQE/EQE. No source edits or rerun in this turn.
- NEXT csh-safe read-only: `sed -n '112,175p' pp2_des.cmd` to confirm ionization and first sidewall trap region/Conc and `sed -n '505,615p' pp2_des.cmd` to confirm bias ramp, final time/goal, BE step and possible hold. If Trap conc is zero in n2 confirm explicitly; do not infer solely from label `NtSide=0`. Preserve completed 5V outputs/full references.

## 2026-10-09 — SWB Create Parameter File dialog and silicon-vs-GaN misconception; controlled baseline calibration plan (OBSERVED + REVIEWED)

- Worker 이택규 screenshot: SWB title shows **/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_SWB** (the *original branch*, NOT already-completed `JUSUBIN_FAST_HALF_5V_TEST`). Dialog `Create Parameter File`: **`Parameter file sdevice.par does not exist`**, radio choices `Silicon` default selected, `Choose Materials`, `Create Empty File`; scenario `NtSide=0`, SDE→SDEVICE.
- This is an **input-generation dialog** not an SDevice error or proof the existing 5V simulation used Silicon physics. Actual completed 5V_TEST n2_des.log lists `ModelParameters file: FASTC1_pp6_des.par`, `DefaultParametersFromFile` loading GaN/InGaN/InN MaterialDB, and a working 5V curve trace; that branch's `pp2_des.cmd` has region-specific incomplete ionization and `NtSide=0` ALL 12 sidewall `Conc=0` entries preprocessed (already earlier recorded in LIVE_STATE JSON). Do not confuse same old SWB input-file workflow with 5V_TEST source.
- Synopsys SWB User Guide (publicly accessible N-2017.09 pages 65–68, https://studylib.net/doc/28266667/swb-ug) documents `Tool > Edit Input > Parameter` then `Choose Materials` and selection, copies chosen release MaterialDB files into project and includes `Material="GaN" { #includeext ... }` etc in sdevice.par; Silicon default merely generates Silicon material file; `Create Empty File` possible. Tool properties can use common `sdevice.par` or per-tool .par. Sentaurus Device default physical parameters have builtin/material DB/custom parameter file precedence; blindly generating/using a new sdevice.par can overwrite working FASTC1_pp6_des.par customization (e.g., lattice/polarization/thermionic and Magnesium ionization), and merely copying the uncalibrated GaAs-derived InGaN.par does NOT improve recombination IQE.
- Intended mesh materials in Common Baseline: GaN, InGaN, AlGaN, Nitride (Si3N4); InN relevant as InGaN constituent and file-loader but not necessarily an explicitly meshed domain. Confirm exact mesh material names before choosing in a NEW clone. Danger: picking only GaN does not set all InGaN/AlGaN regions to GaN; material assignment is in SDE/TDR.
- **Immediate safe recommendation**: Cancel current parameter creation in original JUSUBIN_FAST_HALF_SWB, do NOT hit OK with Silicon or generate any .par there, do NOT rerun there yet. Clone known 5V_TEST to separate calibration sandbox after backing up existing source and results, audit `File{Parameters}` of active sdevice source and actual pp2_des.par/FASTC1_pp6_des.par before integrating a region/material-specific calibration par.
- As of 2026-10-08 JuSubin timeline (documented, not necessarily new actions today): Half+coarse mesh 138,194 elements/65,513 points versus Full 290,814; half+coarse equivalence to Full unverified; Mg/n-GaN doping-profile physical validation not complete; QS 0.3V pilot proposed; later LeeTaekGyu Oct9 run of QS Copy failed at **0.019304636 V** with Newton 15 iterations then MinStep; physical cause unresolved. Additional sidewall trap-ON NtSide=1e18 in accelerated Half branch unverified. C2 save/load reference gating remains separate.
- New blocker classification: P0 preserve original proven 5V_TEST source and metadata, establish exact active materials and .par custom overrides; P1 check doping/currents/2D AreaFactor and material B/SRH lifetime, NtSide0 region trap status; P2 conditional calibration branch and short smoke/QS/Transient checks; P3 NtSide1e18 at matched J; P4 Half+Coarse vs Full/mesh and no-project modification without explicit approval. Issue #7 append only.
