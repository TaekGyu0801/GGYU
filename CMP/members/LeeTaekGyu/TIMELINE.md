## 2026-10-08 — FAST_C1 실제 SDE 소스 파일 위치 확인; FAST_HALF Claude 전달 패키지 준비

- 작업자: 이택규; 상태: OBSERVED (터미널 파일명) / PROPOSED (구현·실행).
- 서버: `semi437@ssudisu3`, 프로젝트: `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1`.
- 사용자 명령 `find . -name '*dvs.cmd' -print` 결과: `./sde_dvs.cmd`, `./pp1_dvs.cmd`, `./n1_dvs.cmd`.
- `find . -name 'pp6_des.par' -print` 결과: `./pp6_des.par`. `pp6_des.cmd`와 `n1_msh.tdr`은 이전 프로젝트 기록상 같은 경로에서 관찰되었으나 이번 터미널 메시지에서 목록을 새로 확인하지 않음.
- 사용자는 일일이 확인하지 않고 Claude에 원본 파일을 한 번에 전달하여 별도 FAST_HALF + selective remote bulk coarsening 분기를 빠르게 만들고 short smoke 후 시험 실행하기를 요청함.
- 최소 입력 패키지 후보: `sde_dvs.cmd pp1_dvs.cmd pp6_des.cmd pp6_des.par n1_msh.tdr` (서버에서 존재 확인 후 archive). Private Synopsys/deck 입력을 public GitHub에 업로드하지 않는다.
- 실제 geometry/contact/doping/refinement 코드를 읽지 못했으므로 절반 자르는 y 좌표나 mesh 숫자는 아직 확정·적용하지 않음. Run 미실시; 기존 reference 불변.

## 2026-10-08 — cmp216 FAST_C1_ACCOUNT_TEST n6 logging stopped during new BE-step (OBSERVED / TERMINATION CAUSE UNRESOLVED)

- 이택규 제공 2026-10-08 16:00 KST 터미널 증거: `n6_des.log` grep `fatal|killed|aborted|signal|license|good bye|simulation finished`에서 라이선스 checkout 문구만 보이며 명시적 fatal/killed/normal-completion 문자열 없음.
- 마지막 accepted step: `0.189674→0.190674 s` at anode 0.9534 V, |RHS|=6.15e-05 (<1e-3), wallclock=23.65s. 다음 `0.190674→0.191674 s`에서 iteration header 이후 로그가 끊김.
- 파일 mtime: log Oct 7 17:47, PLT Oct 7 17:45; 폴더에는 `n1_msh.tdr`, `pp6_des.cmd`, `pp6_des.par`, `n6_des.log`, `n6_des.plt`만 보임. 5 V 완료 증거/최종 TDR 없음.
- 어제 license checkout 성공 ≠ 중단 원인이 license 아님을 증명하지는 않음. **종료 원인 미확인**, 오류를 특정하지 말 것. 서버의 프로세스/세션 이력, 시작 명령과 작업 방식 확인 후 재실행 여부 결정. 기존 semi437 reference run 손대지 않음.

## 2026-10-08 — 이택규 half-domain + selective bulk coarsening pilot 요청

- 작업자: 이택규; 상태: PROPOSED / NOT CODED / NOT RUN.
- 시간 제약으로 개별 발광 Probe 검증을 잠시 뒤로 두고, 기존 FAST_C1 reference를 유지한 채 별도 실험 branch에서 (1) 좌우 대칭 half-domain, (2) 활성영역에서 떨어진 bulk/numerical n-GaN base의 selective mesh relaxation을 **동시에 적용한 exploratory pilot**을 우선 준비하기로 요청함.
- 필수 보존: 4um full-mesa interpretation, Kou epitaxy, MQW/EBL/heterointerface mesh, 5nm damaged sidewall mesh/physics, contacts/material/physics/traps, 0–5V reference endpoint. Original full/fine C1 runs/files unchanged.
- Half symmetry gate: **실제 active SDE source**에서 contact, domain offset, doping, material boundary, electrode symmetry/region names를 확인. Center cut is an artificial symmetry boundary, not a 5nm damaged wall; preserve one genuine 5nm physical edge.
- Same SDevice region references to removed left/right regions must be updated in copied deck, not by changing trap values. At equivalent bias compare half current ×2 (postprocessed, no unverified AreaFactor change) and spatial QW/edge fields. Domain + mesh combined speedup is exploratory, not isolated evidence of either factor. Later isolate mesh-convergence effect for publication.
- Code cannot responsibly be generated until exact active SDE source and SDevice source/pp deck are available. GitHub public CURRENT may be stale; no solver/server access via connector.
- First action: obtain source SDE/mesh and SDevice/parameter files from current Workbench, generate separate SDE-only + mesh check, preprocess SDevice, then short pilot. No simulation launched yet.

## 2026-10-08 — cmp216 cross-account FAST_C1 Node 6 run stopped writing near 0.9534 V (OBSERVED / CAUSE UNRESOLVED)

- 작업자: 이택규; 근거: 직접 제공된 `cmp216@ssudisu2` terminal listing and `tail -n 80 n6_des.log`.
- Project directory: `/user2/cmp/cmp216/FAST_C1_ACCOUNT_TEST`; files: `pp6_des.par` (283 B), `pp6_des.cmd` (7.5 K), `n1_msh.tdr` (2.9 M), `n6_des.plt` (87 K; Oct 7 17:45), `n6_des.log` (345 K; Oct 7 17:47).
- Last clearly **accepted** transient step: simulation time `0.189674→0.190674 s`, anode voltage `9.534E-01 V` (0.9534 V); cathode current `-1.215E-14`; RHS `6.15e-05 < 1e-3`; wallclock `23.65 s`.
- Next step `0.190674→0.191674 s` begins, but the supplied file tail ends at the Newton-table header; no accepted next step nor normal end marker shown. Progress after 0.9534 V **not evidenced**.
- Local `cmp216` `sdevice` process absent on `ssudisu2` in earlier `ps`; log/plt timestamps remain Oct 7, while inspection Oct 8. No `n*_des.tdr` was found. Suggests this local run is **not active**, but another host / cause and SWB job state not yet checked.
- This was a cross-account same-input benchmark; cannot claim numerical speedup from low-bias step time or determine why it stopped.
- NEXT: inspect end of log/other output files, SWB execution host/status, investigate process exit before deciding on restart. Preserve files; do not alter original `semi437` runs.

## 2026-10-08 — Node 6 4.7 V QW1–QW4 local recombination Probe screenshots

- 작업자: 이택규; 상태: OBSERVED / FIELD LABEL NEEDS FULL CONFIRMATION.
- File displayed: `n6_inter_0004_des` (recorded ~4.7 V). User SVisual screenshots show four separate probe zones `Clean_QW1(InGaN)` through `Clean_QW4(InGaN)`.
- Selected row label is clipped on the left (`...bination`); based on context it appears to be `RadiativeRecombination`, but fully visible field name must be confirmed before scientific reporting.
- Screen-read local Probe values [cm^-3 s^-1, conditional on RadiativeRecombination identification]: QW1=5.531972320698e12 at (x,y)=(0.169227828103, 0.578178492482); QW2=9.346620224854e14 at (0.193404232523, 0.579185842666); QW3=4.188264170176e13 at (0.219595337312, 0.578850059272); QW4=6.069760269935e14 at (0.244443308521, 0.577506925693).
- These are four positive **local point** values, not integrated QW recombination, photon escape, LED turn-on, or an IQE value. No need to modify baseline or run SDevice yet.
- Next: screenshot the full active field name (e.g. left horizontal scroll, `Show Only Active Field`) and conduct per-region integration; compare local carrier densities and active radiative parameter B via actual pp/par/material database.

## 2026-10-08 — How to establish LED emission in TCAD (manual-verified gate)

- 작업자: 이택규; 상태: REFERENCE VERIFIED / ACTIVE COEFFICIENT UNRESOLVED.
- Sentaurus Device T-2022.03 UG §16 pp.488–489: RadiativeRecombination dataset creation is not evidence of positive luminescence; inspect numeric QW Rrad and actual material-specific Radiative coefficient C. Manual states default C=0 for materials other than GaAs unless overridden; current active InGaN/GaN material/parameter setting remains unverified.
- §34 pp.1040–1043: separate LED optical simulation can report spontaneous photon/power generation and escaped photon/power. Do not conflate radiative recombination with measured/extracted external light output.
- Next: active pp cmd/par and material parameters → QW Rrad area-integration smoke → .plt e/h/displacement and injection sanity → same-J IQE workflow. Keep baseline unchanged until diagnosis. See Issue #7 2026-10-08.

## 2026-10-08 — Claude half-domain/low-current review (PROPOSED)

- Claude correctly flags very low provisional J near 4.71 V and recommends non-solver TDR/PLT diagnostics before further multi-day runs. This is a high-priority sanity check, NOT confirmed LED failure.
- Half-domain conditionally promising; source-based contact/doping/domain symmetry, full-vs-half extraction, and mesh/solver equivalence must pass before production.
- RHS L2 scaling by sqrt(2) is heuristic; do not change RhsMin in production without an explicit tolerance/equivalence study.
- Also separate anode electron/hole/displacement currents and inspect integrated QW recombination before diagnosing injection physics. See LIVE LOG Issue #7, 2026-10-08 ChatGPT review.

## 2026-10-08 — TCAD official guides registered for future coding

- 작업자: 이택규
- 상태: OBSERVED / REFERENCE INDEX UPDATED
- Uploaded `TCAD_GUIDELINE.zip` inspected: five Synopsys Sentaurus T-2022.03 User Guides (Device, Structure Editor, Mesh, Process, Visual).
- ZIP and PDF SHA-256 identifiers, page counts, workflow, licensing/access constraints recorded in `CMP/references/TCAD_REFERENCE_INDEX.md`.
- Future code work must consult the relevant original guide and verify against active preprocessed files and actual log; do not assume PDF bytes are accessible from a new chat just because the index exists.
- No TCAD source or baseline physics modified; no simulation result asserted.

## 2026-10-07 — Cross-account FAST_C1 input identity confirmed

- 작업자: 이택규
- 상태: CONFIRMED / ACCOUNT-COMPARISON GATE PASS
- 기존 계정 `semi437@ssudisu3`의 FAST_C1 원본과 새 계정 `cmp216@ssudisu2`로 Windows/MobaXterm을 통해 옮긴 테스트 입력을 SHA-256으로 비교함.
- 세 핵심 입력이 byte-identical:
  - `pp6_des.cmd` = `48d8de1a0d596e9c3b308498efda653486d6df839ae2bb8826f83ff569e3ac22`
  - `pp6_des.par` = `60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039`
  - `n1_msh.tdr` = `762d2d57a352a00bb030b968985cbf3b71d53118c68e5c53b7586e613f392ea3`
- 새 계정의 `sdevice`도 T-2022.03 경로로 확인됨.
- 따라서 이후 새 계정 실행은 동일 mesh/cmd/par를 사용한 cross-account numerical/runtime 비교로 해석 가능.
- 다음: 실행 전 `pp6_des.cmd/par` 내 기존 계정 절대경로가 없는지 최종 확인하고, 새 계정에서 Node 6 SDevice를 시작해 step walltime/accepted-rejected timestep/Newton pattern을 기존 계정과 비교.

## 2026-10-06 — D6 complete

- 기존 Node 6 4.7 V intermediate TDR은 SDevice가 읽었지만 restart state 정보가 없어 Load restart에 사용할 수 없었음.
- 현재 C1에서 Option 3은 폐기.
- Node 6/12 reference run은 계속 유지.
- 다음: 새 C2 smoke에서 Save checkpoint를 직접 만든 뒤 그 Save 파일로 Load 시험.
- 공통 C2 첫 후보는 Iterations=15 유지, Increment=1.05 시험.

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

## 2026-10-06 — D2 complete: universal C2 cap 8/10 rejected

- Node 6: 3311 accepted / 645 rejected; accepted max Newton=4; cap 8 false_rej=0; rejected wallclock fraction ~54.2%.
- Node 12: 1223 accepted / 101 rejected; accepted max Newton=15; accepted histogram includes 13 iters x1 and 15 iters x1.
- Node 12 cap 8 false_rej=2; cap 10 false_rej=2; first predicted divergence ~4.195 V.
- Decision: first common C2 keeps Iterations=15 and tests high-bias Increment=1.05. Original cap-8 C2 deck is not approved for execution as-is.
- Next: inspect the two Node 12 accepted attempts >8 iterations, then D3 current-normalization/J-window gate.

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

## 2026-10-06 — Deadline-driven FAST half + coarse-mesh branch chosen

- 작업자: 이택규
- 상태: DECISION / PROPOSED IMPLEMENTATION
- 목표를 publication-final mesh보다 2026-10-23 전 결과 확보에 우선하도록 재확인.
- 기존 FAST_C1 full runs는 reference evidence로 보존하고 건드리지 않음.
- 별도 branch에서 half-domain + bulk/global mesh coarsening을 동시에 적용하는 runtime-first candidate를 만들기로 결정.
- 보호할 해상도: MQW vertical/interface, EBL vertical/interface, 5 nm damaged sidewall은 현 수준에 가깝게 유지.
- 우선 줄일 부분: center symmetry로 full width의 절반 제거 + remote homogeneous n-GaN/base/global lateral/vertical bulk mesh 완화.
- 이 branch는 preliminary/screening 용도이며, final publication adoption은 full-reference equivalence/mesh-convergence 확인 후에만 가능.
- 실행 전 첫 gate는 SDE mesh 생성 후 element/point count와 active-region/sidewall mesh 시각 점검.

## 2026-10-06 — FAST_C1/Common Baseline exact SDE mesh rules supplied by user

- 작업자: 이택규
- 상태: OBSERVED / SOURCE CODE
- 사용자 제공 SDE v1.0 header explicitly identifies a 2D Cartesian planar InGaN/GaN microLED.
- Mesh rules in the supplied source:
  - Global: max (x,y) = (0.050, 0.100) um; min = (0.005, 0.005) um.
  - EBL window: max = (0.002, 0.020) um; min = (0.001, 0.002) um.
  - MQW window: max = (0.0010, 0.020) um; min = (0.0005, 0.002) um.
  - 5 nm damaged-sidewall windows: max = (0.005, 0.001) um; min = (0.001, 0.0005) um.
  - MaxLenInt: GaN/Nitride 0.002 um, GaN/AlGaN 0.001 um, GaN/InGaN 0.0005 um, factor 1.2.
- Coordinate definition in source: x = vertical growth direction; y = lateral direction.
- Interpretation: finest explicitly requested spacing is 0.0005 um = 0.5 nm, at MQW/interface and damaged-edge refinement.
- Existing observed generated mesh statistics remain Elements=290,814 / Points=137,831.
- Exact element count through a 5 nm strip is mesh-generator dependent; do not state a fixed count from the refinement-size parameters alone.

## 2026-10-06 — Oct 23 abstract deadline forces runtime-first triage

- 작업자: 이택규
- 상태: DECISION / DEADLINE
- 사용자 명시 마감: 2026-10-23 논문 초록 제출.
- 현재 가장 큰 blocker: Common Baseline SDevice node가 수십 시간 이상 걸리며 high-bias timestep collapse 때문에 전체 연구 일정이 simulation completion에 묶여 있음.
- 결정: 현재 FAST_C1 Node 6/병렬 Node 12는 가능한 경우 reference evidence로 유지하되, 두 node 완주를 기다리는 것을 연구 일정의 critical path로 두지 않는다.
- 즉시 병행 과제: same physics/mesh 기반 numerical-only accelerated branch를 짧은 benchmark로 검증. 우선 검토 대상은 DC 목적에 맞는 Quasistationary/staged continuation, checkpoint/restart, step recovery 및 output overhead이며 physics/trap/geometry 완화는 금지.
- 초록 전 최소 목표: defensible baseline evidence + 최소 1개의 mechanism-relevant A/B preliminary result 또는 검증된 direction을 확보하고, full sweep는 이후 manuscript stage에서 확장.

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

## 2026-10-04 — User reports other runs stopped for FAST_C1 work

- 작업자: 이택규
- 상태: USER-REPORTED / VERIFY NEEDED
- 사용자가 FAST_C1 작업을 위해 "나머지 다 멈춰놨어"라고 보고함.
- 어떤 기존 run들이 실제로 중지되었는지는 아직 프로세스 확인 전이므로 확정하지 않음.
- FAST_C1의 현재 단계는 solve가 아니라 Node 6 (NtSide=0) preprocess-only gate임.
- preprocess 자체는 계산 solve가 아니므로 기존 장시간 run을 멈출 필요가 없음.
- 다음: FAST_C1 Node 6 preprocess-only 수행, 필요 시 기존 run 프로세스 상태 재확인.

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

## 2026-10-04 — FAST_C1 copied .status points to live gsub PID

- 작업자: 이택규
- 상태: OBSERVED / CAUTION
- FAST_C1 `.status` contains PID 78941 on host ssudisu3.
- `ps -fp 78941` confirms PID 78941 is an active Synopsys `gsub0` process started Sep 28.
- do NOT kill or modify this process; it may belong to the live Copy x8 run.
- next: read-only inspect `/proc/78941/cwd` and cmdline to identify which project owns the process before touching FAST_C1 status metadata.

## 2026-10-04 — FAST_C1 node mapping confirmed

- 작업자: 이택규
- 상태: OBSERVED
- FAST_C1 `gtree.dat` confirms SDevice split:
  - Node 6: `NtSide=0`
  - Node 12: `NtSide=1e18`
- source remains exact C1 SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`.
- `.status` currently contains host `ssudisu3` and PID `78941`; its meaning/liveness must be checked before preprocess.
- next: read-only `ps -fp 78941`; then preprocess Node 6 only if safe.

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

## 2026-10-04 — FAST_C1 Workbench copy contents confirmed

- 작업자: 이택규
- 상태: OBSERVED
- `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1` contains the copied Copy x8 Workbench project contents (~145 MB).
- Key copied inputs are present: `sd_fdiv_des.cmd`, `n1_msh.tdr`, `pp1_dvs.cmd`, `pp6_des.cmd`, `pp6_des.par`.
- Legacy/stale execution outputs were also copied (`n6_des.out/log/plt/tdr`, intermediate TDRs, old n12 artifacts); these are not FAST C1 results and must not be interpreted as such.
- no C1 source edit or preprocess has been performed yet.
- next: read-only SHA-256 check of copied golden inputs before any cleanup/edit.

## 2026-10-04 — Separate FAST C1 directory created

- 작업자: 이택규
- 상태: OBSERVED
- separate directory exists:
  `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1`
- live Copy x8 remains untouched.
- directory existence alone does not yet prove the Workbench project contents were fully copied.
- next: read-only listing of the FAST_C1 directory before any cleanup/source replacement/preprocess.

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

## 2026-10-04 — Old B0 CSV cutback-ratio spread identified as dt-rounding artifact

- 작업자: 이택규
- 상태: OBSERVED
- full old-CSV check over 285 rejection/retry pairs: min=0.47826087, max=0.52173913, mean=0.499405569.
- old CSV used dt=t1-t0 from rounded printed endpoints, so high-bias small timesteps are distorted.
- this spread is not accepted as evidence of a variable cutback factor.
- updated Claude audit tool reads explicit Stepsize from the log; regenerate CSV before judging cutback-ratio constancy.
- existing raw log examples using Stepsize are approximately 0.5.
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

## 2026-10-04 — B0 CSV ratio check command quoting error under csh/tcsh

- 작업자: 이택규
- 상태: OBSERVED / RESOLVED COMMAND SYNTAX
- multiline `python3 -c '...'` command was pasted into csh/tcsh and split across prompts, causing `Unmatched '`, `Badly placed ()'s`, and globbing errors.
- no file/simulation change occurred.
- correction: use a single-line awk command for the CSV retry-dt/rejected-dt ratio check.

## 2026-10-04 — Claude B0 review package integrated

- 작업자: 이택규
- 상태: PROPOSED / REVIEWED / READY FOR PREPROCESS
- reviewed `C1_B0_review_for_GPT.zip`.
- C1 source unchanged; `Iterations=15` retained; SHA `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`.
- corrected interpretation:
  - ~4.33 V = first rejected attempt where Newton count changes 50->15, not trajectory divergence.
  - expected observed-overlap trajectory is same accepted steps + same rejection points.
- A1'/A1'' added; printed-precision identity expectation tightens A3/A4 on observed overlap.
- updated audit tool package SHA `9a935633e92bc55fa86849b6988b60a8a8ee55f637387ced62721d9f6267d281`; ChatGPT reran `--selftest` successfully.
- patch base `30f9d947...` matched current main and patch-equivalent content was committed as `ace056fcb01d2e6e785dbee08a213e1148d6be35`.
- x8 raw excerpt supports ~0.5 timestep cutback on several observed rejection/retry pairs; full CSV-wide ratio verification remains pending because the CSV was not attached to the review package.
- next: separate FAST C1 project preprocess gate, then NtSide=0 B1.
- live x6/x7/x8 untouched.

## 2026-10-04 — B0 raw x8 audit PASS for C1 Iterations=15

- 작업자: 이택규
- 상태: OBSERVED / B0 PASS TO CURRENT X8 PROGRESS
- source log: `~/CMP_B0/x8_n6_des_20261004_1335.out`
- parsed attempts: 2236
  - accepted: 1950
  - rejected: 285
  - unknown: 0
- accepted-step Newton iterations:
  - 2 iter: 1019
  - 3 iter: 778
  - 4 iter: 153
  - **accepted max = 4**
- rejected attempts: **285/285 reached 50 iterations**
- parser/raw excerpt directly confirms a rejected attempt finishing with `#iterations larger than 50.`
- `Iterations=15` predicted false rejections over the observed x8 trajectory: **0**
- first trajectory divergence under a 15-cap is predicted near anode **4.33 V**
- observed attempt wallclock sum:
  - total ≈ 495106 s = 137.5 h
  - accepted ≈ 123464 s
  - rejected ≈ 371643 s (~75.1% of attempt wallclock)
- simple uniform-per-iteration estimate for N=15: saved rejected-attempt time ≈ 260150 s (~72.3 h), corresponding to an idealized ~2.11x speedup over the observed trajectory if no additional recovery cost is introduced.
- important limitation: x8 log copy only reaches ~4.643 V; B0 does not prove behavior from 4.643→5.0 V.
- tool caveats:
  - real log `error` column is not yet parsed, so `err<1?` output is not used.
  - cutback recovery median/max from the current script is not used for acceptance because the metric is misleading under repeated ramp failures.
- decision: C1 `Iterations=15` is approved as the first PROPOSED numerical candidate for separate-project preprocess + NtSide=0 benchmark. It is not yet a CONFIRMED FAST baseline.

## 2026-10-04 — Corrected B0 parser selftest passed

- 작업자: 이택규
- 상태: OBSERVED / TOOL SELFTEST PASS
- commit-pinned parser `a0ff43f2aff4b76ed390dcd6831e3ebeba6cb366` downloaded successfully.
- `python3 ~/CMP_B0/sdevice_newton_audit.py --selftest` returned `selftest OK`.
- This version contains the regression probe for the observed x8 T-2022.03 BE-step syntax.
- next: rerun the real x8 copied-log audit and inspect accepted/rejected iteration distribution.
- C1 `Iterations=15` remains unconfirmed until the real-log audit passes.

## 2026-10-04 — Root cause of failed BE-step parser patch: regex escaping error

- 작업자: 이택규
- 상태: FIXED / B0 PENDING
- commit `c9e5804...` still failed its real-line regression selftest.
- direct source inspection found the regex contained raw-string tokens like `\\\\s` instead of `\\s`, so it searched for a literal backslash+s rather than whitespace.
- actual fix committed as:
  - `a0ff43f2aff4b76ed390dcd6831e3ebeba6cb366`
- GitHub source was reread after the write and now contains single-backslash regex tokens such as `Computing\\s+BE-step`.
- next: download commit-pinned script, run selftest, then rerun B0.
- no TCAD simulation/source deck modified.

## 2026-10-04 — Correction: previous BE-step parser patch had not changed RE_STEP; fixed at commit c9e5804

- 작업자: 이택규
- 상태: FIXED / PROPOSED TOOL
- user reran the supposed patched parser and still got attempts=0.
- direct GitHub inspection showed `RE_STEP` was still the old `Computing step from t=...` regex.
- prior statement that the BE-step parser patch was applied was incorrect.
- actual fix now committed:
  - commit `c9e5804ba0d84e424fcde6f4fd83bb4a04cd686a`
  - recognizes observed `Computing BE-step from <t0> s to <t1> s (Stepsize: <dt> s)` syntax
  - adds a regression selftest using the exact observed x8 line.
- next: download the commit-pinned script, rerun selftest and B0 audit.
- no simulation/source deck was modified.

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

## 2026-10-04 — B0 parser mismatch on real x8 SDevice log

- 작업자: 이택규
- 상태: OBSERVED / UNRESOLVED TOOLING
- `sdevice_newton_audit.py --selftest` passed on synthetic data.
- Real Copy x8 log audit returned:
  - attempts=0
  - no wallclock found
  - `NO "Computing step from t=... to t=..." lines found`
- Interpretation: actual T-2022.03 `n6_des.out` format does not match the parser's assumed step-start regex.
- B0 scientific conclusion is therefore still pending; no claim about accepted/rejected iteration distribution or Iterations=15 is valid yet.
- Next: inspect raw x8 log wording around "Computing", "Rhs", "step", and transient time, then patch the parser to the actual format and rerun B0.

## 2026-10-04 — B0 local audit setup

- 작업자: 이택규
- 상태: OBSERVED
- x8 n6_des.out copy succeeded to ~/CMP_B0/x8_n6_des_20261004_1335.out.
- LOG variable setup succeeded under csh/tcsh.
- audit did not start because sdevice_newton_audit.py was not yet present in ~/CMP_B0.
- no simulation/source change occurred.
- next: place the audit script in ~/CMP_B0, run selftest, then audit the copied x8 log.

## 2026-10-04 — B0 audit script missing locally

- 작업자: 이택규
- 상태: OBSERVED / RESOLVED PATH ISSUE
- x8 log copy succeeded:
  - `~/CMP_B0/x8_n6_des_20261004_1335.out`
  - size ≈ 3.4M
- csh/tcsh `LOG` variable setup succeeded.
- audit command failed only because `~/CMP_B0/sdevice_newton_audit.py` was not present:
  - `python3: can't open file ... [Errno 2] No such file or directory`
- no simulation/source modification occurred.
- next: download the GitHub tool to `~/CMP_B0/`, run `--selftest`, then execute B0 audit.

## 2026-10-04 — semi437 shell syntax mismatch during B0 log copy

- 작업자: 이택규
- 상태: OBSERVED / RESOLVED
- command `cp n6_des.out ~/CMP_B0/x8_n6_des_$(date +%Y%m%d_%H%M).out` returned `Illegal variable name.`
- interpretation: login shell behaves as csh/tcsh, where bash-style `$(...)` command substitution is invalid.
- correction: use backticks for command substitution, e.g. `x8_n6_des_`date +%Y%m%d_%H%M`.out`.
- no simulation/source files were modified; only the attempted copy command failed.
- next B0 commands should use csh/tcsh-compatible syntax.

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

## 2026-10-04 — Claude FAST C1 package reviewed by ChatGPT

- 작업자: 이택규
- 상태: PROPOSED / REVIEWED / NOT EXECUTED
- Claude package `FAST_BASELINE_C1_for_GPT.zip` 검토 완료.
- golden source SHA-256 재검증:
  - `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`
- FAST C1 source SHA-256 재검증:
  - `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`
- golden 대비 executable statement 변경은 transient inner Coupled의 `Iterations=15` 한 group뿐.
- 기존 ChatGPT FAST v0.1(SHA `6ccf386c...`)과 Claude C1은 executable statement 기준 동일. 차이는 comments/formatting뿐이며 앞으로 C1을 canonical candidate로 사용.
- Claude Python tools 3개는 ChatGPT sandbox에서 `py_compile` 통과; Newton audit/PLT compare synthetic selftest 통과. 실제 semi437 SDevice log/PLT에서는 아직 미검증.
- 중요 correction:
  - Synopsys 2022 training은 Quasistationary/Transient Newton `Iterations` default=20, 보통 15–20회 제한을 권장.
  - CMP 기록의 약 50-iteration failure와 충돌하므로 effective x8 cap은 아직 UNRESOLVED.
  - B0에서 exact `pp6_des.cmd` + raw `n6_des.out`을 교차검증한 뒤 15를 확정.
- raw Claude patch의 “x7 먼저 정리” 권고는 최신 운영 결정과 충돌하여 반영하지 않음. live x6/x7/x8은 보존.
- acceptance thresholds는 PROVISIONAL engineering criteria로 기록.
- public record: `CMP/FAST_BASELINE_C1.md`
- sanitized diff: `CMP/tcad/tools/FAST_C1_vs_CopyX8.diff`

## 2026-10-04 — Claude FAST implementation prompt committed

- 작업자: 이택규
- 상태: READY FOR CLAUDE
- Claude가 GitHub만 읽어도 FAST_BASELINE 구현 맥락을 이해할 수 있도록 종합 prompt/handoff를 생성:
  - `CMP/prompts/CLAUDE_FAST_BASELINE_IMPLEMENTATION.md`
- 내용:
  - exact Copy x8 golden source filename/hash
  - generated-input hashes
  - 연구 목적 / Project A-B framing
  - 변경 금지 Common Baseline physics
  - exact current numerical settings
  - 실제 high-bias runtime bottleneck
  - historical provenance traps
  - Claude가 제출해야 할 complete code/diff/Workbench/benchmark 산출물
  - public GitHub에 proprietary source를 올리지 않는 규칙
- FAST Sentaurus 코드 작성은 Claude가 전담.
- 이전 ChatGPT `Iterations=15` 아이디어는 확정 patch가 아니라 PROPOSED 참고 후보로만 취급.
- 사용자는 Claude 채팅에 `Copy_x8_sd_fdiv_des.cmd`를 별도 첨부해야 함.

## 2026-10-04 — FAST_BASELINE v0.1 Iter15 candidate created

- 작업자: 이택규
- 상태: PROPOSED / READY FOR SHORT BENCHMARK
- 업로드된 exact Copy x8 source SHA-256가 golden hash `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`와 일치함을 확인.
- FAST v0.1은 원본 대비 numerical-only 1개 변경:
  - Transient 내부 `Coupled`에 `Iterations = 15` 명시.
- FAST v0.1 SHA-256: `6ccf386cd8959b5953c2c1b241f2c868916bf222814a03f9f774edbc82011040`
- Physics/Traps/Nt/Et/sigma/mesh intent/bias goal/step controls/ILS는 변경하지 않음.
- 목적: high-bias에서 장시간 소모 후 reject되는 Newton step을 더 일찍 cutback하도록 유도.
- 다음: live x8은 보존하고 별도 Workbench copy에서 short benchmark; accepted/rejected iteration, timestep, wallclock, I-V 및 matched-bias 결과 비교.

## 2026-10-04 — FAST workflow sequence corrected to original plan

- 작업자: 이택규
- 상태: DECISION / CORRECTION
- 사용자 지적에 따라 GitHub 기록을 재검토했고, 2026-10-03 원래 계획은 Copy x8 reference 확보 후 별도 FAST_BASELINE 코드를 바로 작성하고 Newton/cutback policy부터 short benchmark하는 순서였음을 확인.
- clean-account reproduction은 FAST 코드 작성 전 blocker가 아니라, 최종 FAST deck freeze 및 Project A/B production 전 필수 검증 gate로 위치를 복원.
- 현재 상태: Copy x8 golden hashes frozen; separate FAST code 작성 준비 완료.
- 남은 직접 blocker: 코딩 AI가 exact Copy x8 editable source 본문을 받아야 함. public CURRENT 파일은 stale이므로 사용 금지.

## 2026-10-04 — Copy x8 golden reference freeze completed

- 작업자: 이택규
- 상태: CONFIRMED
- local snapshot: `~/CMP_REFERENCE_SNAPSHOTS/Copy_x8_20261004_124024`
- exact core files and hashes:
  - `n1_msh.tdr` = `762d2d57a352a00bb030b968985cbf3b71d53118c68e5c53b7586e613f392ea3`
  - `pp1_dvs.cmd` = `5685528bc3ec338ce104040b0503be43ef032094976d69995529eb5d6fb4e658`
  - `pp6_des.cmd` = `2dfcc98effe145ec944fb8ee5d6914f5f098e54d1bf2319c69acc76afe1692e6`
  - `pp6_des.par` = `60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039`
  - `sd_fdiv_des.cmd` = `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`
- 기존 blocker였던 editable SDevice source 누락은 해결됨.
- 이 snapshot/hash set을 clean-account reproduction의 golden reference로 사용.
- 다음: 이택규 clean account 새 Workbench project에서 preprocess/early-init까지만 실행 후 exact diff/hash 비교.

## 2026-10-04 — Copy x8 core files verified

- 작업자: 이택규
- 상태: OBSERVED
- active Copy x8 directory에서 핵심 파일 존재를 사용자 터미널로 확인:
  - `sd_fdiv_des.cmd`
  - `pp1_dvs.cmd`
  - `pp6_des.cmd`
  - `pp6_des.par`
  - `n1_msh.tdr`
- 기존 reference-package blocker였던 exact editable SDevice source 부재는 active x8 directory 기준으로 해소 가능.
- 다음: snapshot helper 실행 → local golden snapshot + SHA-256 manifest 생성.

## 2026-10-04 — Copy x8 exact core files verified in active directory

- 작업자: 이택규
- 상태: OBSERVED
- 사용자 터미널에서 active Copy x8 directory `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_Copy_Copy_Copy_Copy_Copy_Copy_Copy_Copy` 확인.
- 핵심 파일 존재 확인:
  - `sd_fdiv_des.cmd` 18K, Sep 28 12:17
  - `pp1_dvs.cmd` 18K, Sep 28 10:31
  - `pp6_des.cmd` 7.5K, Sep 28 18:43
  - `pp6_des.par` 283B, Sep 28 18:43
  - `n1_msh.tdr` 2.9M, Sep 28 10:31
- 따라서 기존 reference-package blocker였던 exact editable SDevice source 부재는 active x8 directory 기준으로 해소 가능.
- 다음: snapshot helper를 x8 directory에서 실행해 local golden package와 SHA-256 manifest 생성.

## 2026-10-04 — FAST baseline reproducibility gate and capture helper added

- 작업자: 이택규
- 상태: PROPOSED / TOOLING READY
- GitHub public repository의 CURRENT TCAD deck이 active Copy x8의 authoritative source가 아니라는 점을 재확인.
- 새 문서 `CMP/FAST_BASELINE_REPRO_PROTOCOL.md` 추가: Copy x8 local freeze → clean-account preprocess/hash/diff → reproducibility gate → numerical-only FAST branch 순서를 명문화.
- 새 도구 `CMP/tcad/capture_reference_snapshot.sh` 추가: project directory에서 source/preprocessed/grid/log/runtime context를 local snapshot으로 수집하고 SHA-256 manifest를 생성.
- public GitHub에는 licensed/example-derived source/output 원문을 업로드하지 않고, snapshot은 로컬에만 보존하도록 명시.
- 기존 이택규 기록상 `~/CMP_REFERENCE_20261004.tgz` 패키지는 생성되었으나 `sd_fdiv_des.cmd`가 누락된 상태이므로, 우선 exact Copy x8 source를 local reference package에 추가한 뒤 clean-account preprocess 비교로 진행.
- baseline physics/Nt/Et/sigma/5 nm damage width는 변경하지 않음.

## 2026-10-04 — Claude project instructions rebuilt for paper-grade TCAD implementation

- 작업자: 이택규
- 상태: CONFIRMED
- 새 파일 `CMP/CLAUDE_PROJECT_INSTRUCTIONS.md` 생성.
- 목적: Claude가 단순 코드 생성기가 아니라 CMP 연구 목적, Common Baseline, Project A/B mechanism, 과거 오류/provenance, runtime 병목, clean-account reproducibility, GitHub 기록 규칙을 모두 이해한 상태에서 구현하도록 함.
- 역할 분담을 명시:
  - ChatGPT: 연구 방향/검증/provenance/판단 중심
  - Claude: Sentaurus 코드 구현/디버깅/copy-paste-ready 산출물 중심
- `CMP/AGENTS.md`에도 Claude project instruction 문서 읽기 지침 추가.
- 최종 FAST_BASELINE 작업 프롬프트는 아직 작성하지 않음. 사용자 추가 요구조건을 받은 뒤 작성 예정.

## 2026-10-04 — Copy x8 reference package capture

- 작업자: 이택규
- 상태: IN PROGRESS
- Copy x8 active directory에서 reproducibility/reference package를 생성함.
- 포함: pp1_dvs.cmd, pp6_des.cmd, pp6_des.par, n1_dvs.out, n1_msh.log, n6 job/status/error, Workbench gexec/gtree/gvars/gscens, solver log snapshots, mesh hash, environment/process snapshot.
- 패키지: ~/CMP_REFERENCE_20261004.tgz
- 현재 누락: sd_fdiv_des.cmd. 터미널에서 cd 명령과 cp 명령이 붙어 실행되어 source 복사가 실패함.
- 다음: active Copy x8 directory에서 sd_fdiv_des.cmd를 추가 복사하고 SHA256SUMS 재생성 후 tgz 재패키징.

## 2026-10-03 — Copy x6 vs x7 semantic mesh identity confirmed

- 작업자: 이택규
- 상태: CONFIRMED
- Copy x6 and x7 use identical pp1_dvs.cmd, identical pp6_des.cmd, and identical pp6_des.par.
- Mesh logs show the same 138137 vertices, 274946 elements, and max connectivity 9.
- n1_msh.log differences are limited to process ID and mesh-generation timing/rate.
- Therefore x6 and x7 are semantically the same device/mesh/solver input for the active SDevice run; differing TDR binary hashes are non-physical serialization/metadata differences.
- Operational conclusion: x6 and x7 are duplicate active computations. Since x6 is farther progressed, keep x6 if one v1.1 reference is desired and stop x7 after preserving provenance.
- x8 remains the preferred latest v1.2 reference with intermediate TDR snapshots.

## 2026-10-03 — correction: Copy x6 vs x7 SDE inputs are identical

- 작업자: 이택규
- 상태: OBSERVED / CORRECTION
- Copy x6 and Copy x7 `pp1_dvs.cmd` SHA-256 are identical: `5685528bc3ec338ce104040b0503be43ef032094976d69995529eb5d6fb4e658`.
- `diff -u pp1_dvs.cmd` produced no differences.
- Therefore the SDE geometry/mesh-generation command input is byte-identical between x6 and x7.
- Previous interpretation that differing `n1_msh.tdr` hashes prove a different mesh is withdrawn. Binary TDR hash differences can reflect metadata/order/output serialization and must be verified semantically.
- Next verification: compare TDR sizes plus SDE/mesh logs and node/element statistics before declaring the meshes different.

## 2026-10-03 — active baseline lineage clarified by timestamps and diff

- 작업자: 이택규
- 상태: CONFIRMED / IMPORTANT PROVENANCE
- Copy x6 current source header = Final SDevice v1.1.
- Copy x7 current source header = Final SDevice v1.2 and differs from x6 source only by intermediate Plot snapshots block.
- However Copy x7 active pp6_des.cmd timestamp is 2026-09-28 10:31, while its sd_fdiv_des.cmd was edited later at 12:17. Therefore the already-running Copy x7 job did NOT preprocess from the later v1.2 source revision.
- Copy x8 pp6_des.cmd timestamp is 18:43 and exact diff vs Copy x7 active pp6 shows only the intermediate Plot block. Thus Copy x8 is the actual v1.2-running deck; Copy x7 active run is effectively v1.1 numerics/output behavior despite the folder's source file later being edited to v1.2.
- Copy x6 and Copy x7 active pp6_des.cmd/par hashes are identical, but their n1_msh.tdr hashes differ; therefore their active simulations are not identical because the grid input differs.
- Copy x7 and Copy x8 share identical grid hash and parameter hash, with pp6 difference only intermediate output save block.
- Preferred exact running reference: Copy x8.
- Remaining provenance task: determine why Copy x6 and x7 mesh hashes differ by comparing SDE/preprocessed mesh-generation inputs.

## 2026-10-03 — Copy x7 vs Copy x8 exact command diff confirmed

- 작업자: 이택규
- 상태: CONFIRMED
- Copy x7 and Copy x8 have identical source hash, grid hash, and pp6_des.par hash.
- Exact `diff -u pp6_des.cmd` shows the only command-file difference is an added intermediate `Plot(-Loadable FilePrefix="n6_inter" NoOverWrite Time=(0.80 ... 0.995))` block in Copy x8.
- No Physics, Math, Solve, trap, bias-ramp, or parameter differences were shown by the exact diff.
- Therefore Copy x7 and Copy x8 are the same device/physics/numerics; Copy x8 is an output-save revision only.
- Runtime implication: the multi-day slowdown is not caused by a changed physical model between x7 and x8. Intermediate TDR writes may add I/O overhead at specified save points, but the dominant observed bottleneck remains high-bias Newton nonconvergence and timestep cutback.
- Preferred future reference for analysis/manuscript workflow: Copy x8, because it preserves intermediate spatial states while retaining the same underlying device model.

## 2026-10-03 — active run identity correction after grid/source hashes

- 작업자: 이택규
- 상태: OBSERVED / CORRECTION
- 추가 터미널 검증 결과:
  - Copy x6 path: n1_msh.tdr SHA256 = 716df696..., sd_fdiv_des.cmd SHA256 = ee13bea5...
  - Copy x7 path: n1_msh.tdr SHA256 = 762d2d57..., sd_fdiv_des.cmd SHA256 = 56a8be69...
  - Copy x8 path: n1_msh.tdr SHA256 = 762d2d57..., sd_fdiv_des.cmd SHA256 = 56a8be69...
- 따라서 Copy x7과 Copy x8은 source + generated mesh가 byte-identical.
- Copy x6과 Copy x7은 pp6_des.cmd/par은 동일했지만 source/grid가 다르므로 전체 simulation input이 동일하다고 볼 수 없음.
- Copy x8은 Copy x7과 same source/grid/par이지만 pp6_des.cmd hash가 다르며 intermediate TDR files가 존재. Exact diff로 output-save-only revision인지 확인 필요.
- 다음: Copy x7 vs x8 pp6_des.cmd diff, Copy x6 vs x7 source diff 확인.

## 2026-10-03 — active run comparison from terminal

- 작업자: 이택규
- 상태: OBSERVED
- semi437의 세 SDevice run을 직접 비교함.
- 첫 번째와 두 번째 run은 pp6_des.cmd와 pp6_des.par SHA-256이 각각 동일하여 preprocessed SDevice command/parameter가 동일함.
- 첫 번째 진행: pseudo-time 약 0.94147, anode 약 4.707 V.
- 두 번째 진행: pseudo-time 약 0.92964, anode 약 4.648 V.
- 세 번째 run은 pp6_des.par은 동일하지만 pp6_des.cmd 해시가 다르고 intermediate TDR 파일들이 존재함. 진행은 pseudo-time 약 0.92647, anode 약 4.632 V.
- 세 run 모두 고전압 구간에서 Newton iteration 정체와 timestep cutback이 runtime 병목으로 관찰됨.
- 다음: 첫 번째와 세 번째 pp6_des.cmd exact diff, grid input hash 확인.

## 2026-10-03 — semi437 3 active baseline runs: exact pp6 hash/progress comparison

- **작성자:** ChatGPT
- **작업자:** 이택규
- **상태:** OBSERVED
- **근거:** semi437 터미널에서 세 active project directory의 file list, SHA-256, n6_des.out tail 직접 확인.
- **Run A:** `...Copy_Copy_Copy_Copy_Copy_Copy` (Sep26 start)
  - pp6_des.cmd SHA256 = `928613d261c0265b8ac44acb97ed6d80867557dd2910f2648abcc477f60440c3`
  - pp6_des.par SHA256 = `60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039`
  - latest visible pseudo-time ≈0.94147, anode ≈4.707 V
  - repeated high-bias Newton stalls; a failed step exceeded 50 iterations and cost ~1073 s before timestep cutback.
- **Run B:** `...Copy_Copy_Copy_Copy_Copy_Copy_Copy` (Sep28 start)
  - pp6_des.cmd SHA256 identical to Run A
  - pp6_des.par SHA256 identical to Run A
  - latest visible pseudo-time ≈0.92964, anode ≈4.648 V
  - same high-bias convergence pattern.
  - Therefore SDevice preprocessed command/parameter are byte-identical to Run A.
- **Run C:** `...Copy_Copy_Copy_Copy_Copy_Copy_Copy_Copy` (Sep28 start)
  - pp6_des.cmd SHA256 = `2dfcc98effe145ec944fb8ee5d6914f5f098e54d1bf2319c69acc76afe1692e6` (different)
  - pp6_des.par SHA256 identical to A/B
  - latest visible pseudo-time ≈0.92647, anode ≈4.632 V
  - intermediate TDRs `n6_inter_0000..0003_des.tdr` exist, consistent with a revised output-save workflow.
- **Interpretation:** A and B are duplicate SDevice decks at cmd/par level; C is a different command revision with the same parameter file. Exact command-line differences between A/B and C are not yet inspected.
- **Next:** run `diff -u` between A and C pp6_des.cmd, hash the grid input(s), and inspect Solve/Math blocks before deciding whether any duplicate run should be stopped.

## 2026-10-03 — semi437 active TCAD process inventory 확인

- **작성자:** ChatGPT
- **작업자:** 이택규
- **구분:** runtime evidence
- **상태:** OBSERVED
- **직접 확인:** 2026-10-03 22:31:57 KST 터미널 `ps -ef` 출력에서 semi437 계정의 active SDevice가 3개 확인됨.
  1. PID 61681 — started Sep26 — `.../GaN_PiN_Diode_Copy_Copy_Copy_Copy_Copy_Copy` — `sdevice --max_threads 4 pp6_des.cmd`
  2. PID 42738 — started Sep28 — `.../GaN_PiN_Diode_Copy_Copy_Copy_Copy_Copy_Copy_Copy` — `sdevice --max_threads 4 pp6_des.cmd`
  3. PID 79167 — started Sep28 — `.../GaN_PiN_Diode_Copy_Copy_Copy_Copy_Copy_Copy_Copy_Copy` — `sdevice --max_threads 4 pp6_des.cmd`
- **사용자 설명:** 세 작업 중 두 개는 같은 조건이며, 사용자가 Workbench에서 부르는 Copy 6 / Copy 7이 같은 소자라고 설명.
- **주의:** 폴더명의 Copy 반복 횟수와 사용자가 부르는 Workbench Copy 번호의 정확한 대응은 아직 확정하지 않음.
- **다음:** 각 3개 작업 디렉터리에서 `pp6_des.cmd`, `pp6_des.par`, `n6_des.out` tail을 직접 수집해 동일/상이 조건을 확정.

## 2026-10-03 — 7-day baseline runtime concern / numerics optimization direction

- **작성자:** ChatGPT
- **작업자:** 이택규
- **구분:** runtime diagnosis / proposed numerical optimization
- **상태:** USER-REPORTED + PROPOSED
- **사용자 보고:** 주수빈이 실행한 기준소자가 약 7일간 계산 중인 것으로 보임. 현재 세션에서 최신 solver output으로 7일 연속 progress 여부는 직접 검증하지 못함.
- **확인된 기존 병목:** 2026-09-29 Node 6은 ~4.66 V 부근에서 Newton failure 후 timestep이 ~8.67e-6까지 cutback됨.
- **numerics 관찰:** GitHub CURRENT의 stale deck 기준 Transient MaxStep=1e-3이면 0→5 V ramp에서 최대 전압 increment가 5 mV이므로 cutback이 없어도 최소 약 1000 accepted steps가 필요함.
- **제안:** baseline physics/Nt/Et/sigma/geometry는 유지하고, exact running v1.1/v1.2 source를 먼저 회수한 뒤 numerical-only optimization branch를 만들어 step control, Newton iteration policy, ErrRef, mesh node count를 benchmark. Quasistationary는 transient 대비 별도 controlled comparison으로만 시험.
- **주의:** GitHub CURRENT SDevice가 실제 Final v1.2와 불일치하므로 stale 파일을 바로 수정하지 않음.

## 2026-10-03 — 논문화 전략 / novelty framing 제안

- **작성자:** ChatGPT
- **작업자:** 이택규
- **구분:** manuscript strategy / research framing
- **상태:** PROPOSED
- **핵심:** 동일한 5 nm damaged-sidewall Common Baseline에서 Project A(GaN:C resistive blocking)와 Project B(localized AlGaN heterobarrier blocking)를 같은 injected current 기준으로 직접 비교하는 논문 구조를 제안.
- **노벨티 경계:** generic current confinement 자체가 아니라, 동일 defect physics를 보존한 채 resistive vs band-offset edge engineering을 mechanism-resolved 비교하는 것이 핵심. Carbon-localized edge는 잠재적으로 강한 차별점, AlGaN은 기존 lateral-confinement 문헌이 있어 geometry/use-case/comparison level로 claim 제한.
- **필수 결과:** edge carrier access 감소 → integrated sidewall SRH 감소 → MQW radiative/IQE 보존/증가의 causal chain과, Vf/current-crowding/Auger tradeoff 및 optimum design window를 제시.
- **산출물:** `CMP/PAPER_MANUSCRIPT_STRATEGY_PROPOSED.md`

# Lee Taek Gyu Timeline

## 2026-09-28 — NtSide=1e18 근거 수준 재검증 / 발표용 연구노트

- **작성자:** ChatGPT
- **작업자:** 이택규
- **구분:** literature evidence / baseline parameter provenance
- **상태:** CONFIRMED BOUNDARY
- **확인:** Wu et al. (Micro and Nanostructures 177, 207542, 2023)는 양쪽 sidewall edge 5 nm 이내 acceptor-like trap 및 trap-density/energy-level sweep 방법을 직접 지지.
- **중요 경계:** 현재 확인 가능한 근거만으로 Wu 논문이 NtSide=1e18 cm^-3를 보편적/직접 측정 정답값으로 확정했다고 주장하면 안 됨.
- **해석:** CMP의 NtSide=1e18 cm^-3는 nominal Defect-ON calibration/sensitivity starting value로 유지. 다른 III-nitride MicroLED 수치 모델에서 1e18 cm^-3 규모 sidewall trap 사용 사례가 있어 order-of-magnitude plausibility는 있음.
- **발표 표현:** "문헌 기반 plausible nominal calibration value이며 최종 결론은 NtSide sweep으로 검증한다."
- **산출물:** 발표/Q&A용 paper-style PDF 연구노트 생성.


## 2026-09-28 — JuSubin/GitHub/Gmail sync audit

- **작성자:** ChatGPT
- **작업자:** 이택규
- **구분:** collaboration sync audit / blocker discovery
- **상태:** OBSERVED + UNRESOLVED
- **확인:** Gmail의 최신 CMP 메일은 JuSubin이 GitHub Issue #7에 남긴 진행 기록 알림이며, Issue 내용과 일치.
- **중요 발견:** 실제 `CMP/tcad/CURRENT/sdevice2_defect_on.cmd`는 Final SDevice v1.2로 업데이트되지 않았고 오래된 deck이 남아 있음.
- **의미:** 진행상황 로그는 동기화됐지만 실행 코드 source-of-truth는 동기화되지 않음.
- **다음:** exact Final SDevice v1.1/v1.2 전체 원문을 JuSubin 사용자 제공 파일에서 회수한 뒤 CURRENT에 반영. 원문 없이 Issue 요약으로 재구성 금지.



## 2026-09-21 — Common Baseline / AI collaboration workspace

- **작성자:** ChatGPT
- **Phase / Issue:** Phase 0 / #1
- **변경 유형:** 기록 / 인수인계
- **작업 내용:** Common Baseline v1의 source philosophy, 현재 TCAD 상태, 오류 이력, ChatGPT↔Claude 공유 구조를 GitHub에 정리.
- **결과 및 검증:** DmgL/Clean/DmgR region family와 p/n doping scale을 Sentaurus Visual에서 확인. SDevice2→SVisual2 TDR linkage는 미해결.
- **남은 일:** pp9_des.cmd File block과 실제 Node 9 TDR filename 확인.


## 2026-10-06 — Half-domain + localized mesh acceleration proposed

- 작업자: 이택규
- 상태: PROPOSED / NOT YET VALIDATED
- Sentaurus Visual screenshot of current n1_msh shows 290,814 elements and 137,831 points.
- Research intent: preserve publication-grade sidewall-defect physics while reducing runtime.
- Proposed numerical geometry strategy:
  - if the baseline is mirror-symmetric in geometry, doping, contacts, material stack, sidewall traps, and boundary conditions, replace the reflected full cross-section with a half-domain bounded by the device centerline symmetry plane;
  - retain only one physical sidewall in the half-domain and impose the proper symmetry/no-normal-flux condition at the centerline;
  - do not use half-domain for cases that intentionally break left-right symmetry.
- Proposed mesh strategy:
  - keep fine mesh at the 5 nm sidewall-damage region, heterointerfaces/MQW or active junctions, strong-field/depletion regions, and contact/edge locations relevant to the solution;
  - coarsen homogeneous bulk regions away from those locations;
  - validate against the existing full/fine reference before publication use.
- Important caveat: the currently observed high-bias runtime blocker also includes timestep collapse near ~4.7 V, so mesh reduction should reduce cost per Newton solve but cannot be assumed to eliminate the tiny-step bottleneck.
- Next: inspect the actual SDE source/coordinates and boundary setup before implementing; then benchmark full/fine vs half/localized-mesh at identical bias/physics.


## 2026-10-06 — User accepted half-domain / selective-mesh optimization direction

- 작업자: 이택규
- 상태: DECISION / IMPLEMENTATION CANDIDATE
- 사용자가 현재 full reflected device 대신 좌우 대칭이 성립하는 경우 half-domain으로 계산하고, sidewall defect 및 물리적으로 중요한 영역만 fine mesh를 유지하며 나머지 homogeneous bulk는 coarser mesh로 가져가는 방향에 동의함.
- publication-grade 조건: 기존 full/fine reference run은 유지하고, half/selective-mesh 결과가 동일 physics/bias에서 전류 및 핵심 spatial metrics와 동등한지 검증한 뒤 baseline/final branch에 채택.
- fine mesh 유지 대상: 5 nm damaged sidewall, active/heterointerface/junction, depletion/high-field zone, relevant contact/edge.
- coarsening 후보: sidewall/active region에서 충분히 떨어진 homogeneous bulk.
- half-domain 금지 조건: geometry/contact/trap/boundary가 좌우 비대칭인 case.
- 다음: 실제 running SDE source를 확보해 reflect/좌표/refinement 정의를 확인하고 별도 FAST_C2 branch에서 구현 및 short benchmark.


## 2026-10-06 — Project B mesh/symmetry applicability reviewed

- 작업자: 이택규
- 상태: DECISION / IMPLEMENTATION CANDIDATE
- Project B의 현재 개념은 양쪽 sidewall 안쪽에 symmetric AlBarrier_L/R를 두는 구조이므로, 실제 SDE에서 좌우 geometry/contact/BC가 대칭이면 half-domain 접근을 적용할 수 있음.
- 단, center region의 mesh를 '제거'하면 안 됨. 계산 domain에 남아 있는 물리 영역은 mesh가 필요하며, homogeneous bulk는 coarsening만 가능.
- B에서 반드시 fine mesh 유지/추가 대상:
  - fixed 5 nm sidewall damaged region
  - 새 GaN/AlGaN lateral heterointerface
  - MQW/active-region vertical stack 전반
  - barrier가 MQW lateral path와 만나는 corner
  - high-field/depletion/contact-edge regions
- 특히 Project B의 성공 지표에 center current redistribution, radiative recombination, current crowding이 포함되므로 center MQW는 과도하게 coarsen하면 안 됨.
- coarsening 우선 후보: MQW/sidewall/barrier/interface에서 떨어진 homogeneous n-GaN bulk와 기타 완만한 영역.
- validation: full/fine vs half/selective-mesh에서 lateral Ec/Ev barrier, I-V/current normalization, sidewall SRH, MQW radiative, crowding metric 동등성 확인 후 채택.


## 2026-10-06 — Formal review: half-domain + selective-mesh strategy for Project A/B

- 작업자: 이택규
- 상태: REVIEWED / RECOMMENDED CANDIDATE / VALIDATION REQUIRED
- 결론: Common Baseline, Project A, Project B 모두에서 좌우 geometry/doping/contact/trap/BC가 대칭인 경우 centerline half-domain을 사용하는 전략은 연구 목적과 양립 가능하며, runtime 절감 후보로 권장.
- 단, 계산 domain 내부의 mesh를 '제거'하지 않는다. retained domain에는 mesh가 필요하며, 중요도가 낮은 homogeneous bulk만 단계적으로 coarsen한다.
- 공통 fine zones: 5 nm sidewall damage, MQW/active-region stack, heterointerfaces/junctions, high-field/depletion zones, relevant contact edges.
- Project A 추가 fine zone: Cedge / GaN:C high-resistance edge 및 그 경계. Center bulk n-GaN은 coarsening 우선 후보지만 center MQW는 radiative/current-crowding 평가 때문에 유지.
- Project B 추가 fine zone: lateral AlGaN barrier, GaN/AlGaN interfaces, barrier-MQW intersections. B는 band-offset/field gradient가 생기므로 A보다 interface mesh 요구가 더 엄격함.
- half-domain 금지/재검토 조건: one-sided treatment, asymmetric contact, unequal sidewall traps, asymmetric barrier/Cedge geometry, external lateral field 등 left-right symmetry 파괴.
- publication gate: full/fine reference 대비 half/selective-mesh에서 I-V/Vf, current normalization, sidewall SRH, MQW radiative/Auger, e/h density, current crowding, 그리고 B의 lateral Ec/Ev barrier를 비교. 동등성 확인 전에는 final baseline으로 freeze하지 않음.
- 예상 runtime 절감률은 현재 확정할 수 없음. domain halving과 element reduction이 solve cost를 낮출 가능성은 높지만 현재 high-bias timestep collapse는 별도 병목이므로 실제 benchmark 필요.


## 2026-10-06 — IQE compatibility of half-domain model clarified

- 작업자: 이택규
- 상태: REVIEWED / ANALYTICAL RESULT
- 현재 프로젝트의 IQE 정의는 identical integration region에서 integrated Rrad / (Rrad + RSRH + RAuger).
- mirror-symmetric device를 centerline에서 half-domain으로 자르면, full-device의 각 integrated recombination term이 half-domain 값의 정확히 2배가 되는 조건에서 IQE ratio는 동일함: 2Rrad_h / [2(Rrad_h+RSRH_h+RAuger_h)] = IQE_half.
- 따라서 symmetric Baseline/A/B에서는 half-domain으로도 IQE 비교가 가능.
- 주의: absolute integrated recombination/current/optical power는 full-device 총량으로 보고할 때 symmetry factor 또는 2D normalization을 별도로 확인해야 하며, IQE ratio 자체에 임의로 x2를 적용하면 안 됨.
- integration region은 baseline/A/B와 full/half 사이에서 동일한 물리 영역 정의를 사용해야 함. one-sided/asymmetric structure에는 적용 불가.


## 2026-10-06 — Baseline half-domain as production representation reviewed

- 작업자: 이택규
- 상태: REVIEWED / RECOMMENDED WITH VALIDATION GATE
- 결론: 물리적 기준 소자는 계속 4 µm mesa로 정의하되, 좌우 대칭이 실제 SDE/contact/trap/BC에서 확인되고 full/fine reference와 등가성이 검증되면 production Common Baseline의 계산 표현을 centerline half-domain으로 사용하는 것을 권장.
- 중요: half-domain 사용은 physical mesa를 2 µm로 바꾸는 것이 아님. 4 µm physical device의 절반(2 µm)을 symmetry boundary로 계산하는 numerical representation임.
- 현재 full/fine Node 6/12는 validation/reference evidence로 보존. 이후 Baseline/A/B production runs는 같은 validated half-domain/mesh policy를 사용하면 공정 비교가 더 일관됨.
- publication gate: full vs half에서 I-V/Vf, current normalization, IQE, integrated SRH/Radiative/Auger, carrier/current maps, electric field를 비교. B에는 lateral Ec/Ev barrier도 추가 확인.
- IQE ratio는 exact symmetry에서 유지되지만 absolute total current/recombination/power는 symmetry factor 및 2D normalization 확인 필요.
- one-sided/asymmetric future study에는 half-domain 사용 불가.


## 2026-10-08 — cmp216 계정 시뮬레이션 실행 상태 1차 조회

- 작업자: 이택규
- 상태: OBSERVED (사용자가 붙여넣은 터미널 출력) / UNRESOLVED (전체 서버 실행 상태)
- 접속: `cmp216@ssudisu2`, 2026-10-08 약 15:51 KST 확인.
- `cd /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1` 실패: `No such file or directory`. 이 경로는 기존 `semi437` 계정 프로젝트 경로이므로 cmp216 프로젝트 경로로 검증되지 않음.
- `ps -fu $USER | grep '[s]device'` 결과 없음: 해당 시점 `ssudisu2` 로컬 `cmp216` 사용자 아래에서 직접 실행 중인 sdevice 프로세스 확인되지 않음. 다른 실행 호스트/완료/실패는 미확인.
- `ps -fu $USER | grep -E 'sdevice|216' | grep -v grep`에서 SWB GUI 프로세스(pid 75755)는 확인됨. 숫자 216은 현재 사용자 계정명 `cmp216`을 가리키며 Node 216을 뜻하지 않음.
- 변경: 코드/시뮬레이션 실행 중단/재시작 없음.
- 다음: `echo $HOME`, `ls -ld ~/tmp/myproject`, `find ~ -maxdepth 6 -type f \( -name 'n*_des.log' -o -name 'n*_des.out' \) -print 2>/dev/null | head -n 30`로 cmp216 프로젝트/로그 확인; 필요시 SWB 노드 상태와 원격 실행 호스트 조사.


## 2026-10-08 — cmp216 작업 경로/셸 후속 확인
- 작업자: 이택규
- 상태: OBSERVED (사용자 터미널 출력) / UNRESOLVED (SDevice 실제 실행 상태)
- `echo $HOME` → `/user2/cmp/cmp216`.
- `ls -lh ~/tmp/myproject` → 해당 경로 없음. 따라서 이전 semi437의 `tmp/myproject` 경로 레이아웃을 cmp216에 적용할 수 없음.
- `find ~ -maxdepth 6 -type f ... -print 2>/dev/null | head -n 30` → `Ambiguous output redirect.`. cmp216 로그인 셸이 `-csh`인 상황에서 Bourne-style stderr redirect `2>/dev/null`가 해석되지 않은 것으로 판정. **find 검색은 실행되지 않은 것으로 보고 파일 부재/실패를 단정하지 않음.**
- 다음 확인: `ls -la ~`; `find ~ -maxdepth 6 -type f -name 'n*_des.log' -print |& head -n 30` (C-shell 호환); 필요 시 SWB GUI에서 열린 프로젝트 경로와 계산 호스트 확인.
- 코드 수정, 실행 중지/재시작 없음.



## 2026-10-08 cmp216 FAST_C1_ACCOUNT_TEST log check
- OBSERVED (user terminal): directory FAST_C1_ACCOUNT_TEST exists in cmp216 home.
- OBSERVED: n6_des.log found at FAST_C1_ACCOUNT_TEST/n6_des.log.
- OBSERVED: no n*_des.tdr found with find from HOME to depth 6.
- UNRESOLVED: node 6 run status; need tail of log and directory listing.
- NEXT: ls -lhtr and tail -n 80 n6_des.log; do not restart yet.
