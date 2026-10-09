## 2026-10-09 — 5V Half SWB preflight done, archive integrity pending (이택규)
- OBSERVED user terminal: copied `JUSUBIN_FAST_HALF_5V_TEST` 12M snapshot archive `../JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz` exists (Oct9 11:25); `tar -tzf` integrity test not yet run.
- Executable pp2: `Grid=n1_msh.tdr`, 12 printed `Conc=0` entries, RHSMin=1e-3, Coupled iterations startup=500/100, sweep=15. Prior pp2 confirmed Transient FinalTime=1.0 Goal anode=5.0 Save=n2_5V_ckpt. No 5V run observed yet.
- First next: `tar -tzf ../JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz > /dev/null` and C-shell `echo $status` expecting 0; launch only copied SWB SDevice Node2 after that; inspect fresh n2 log/error. Never claim completed simulation until 5V trace and physical outputs are checked.
- Keep original 0.3V project/outputs and separate failed QS Copy unchanged. Do not use inherited copied n2 files as evidence for 5V.

---

## 2026-10-09 — 5V copied half SDevice source edited (이택규 / ChatGPT)
- OBSERVED user terminal in `JUSUBIN_FAST_HALF_5V_TEST`: original source backup command executed, then sed replaced Transient FinalTime 0.06->1.0, Goal anode 0.3->5.0, Save prefix from smoke 0p3V to 5V. Grep returned edited lines 587, 597, 608 and untouched initial electrodes 0V at 38/43.
- Actual changed source is on remote semi437, NOT uploaded as full GitHub source. New 5V run not started. Existing original 0.3V smoke and separate QS Copy remain protected.
- NEXT: SWB copied project SDevice node 2 Ctrl+P preprocess ONLY, then verify `pp2_des.cmd` has FinalTime 1.0, Goal anode 5.0 and intended save; confirm correct grid/NtSide and no stale output. Do not F7 until reviewed. Original 0.3V smoke comment may still be in source.
- WARNING: 5V at FinalTime 1.0 preserves previous voltage ramp ratio, not proof of high-voltage convergence or steady-state LED validity.

---

## 2026-10-09 — Half 5V test copy marker check passed (이택규 / ChatGPT)
- OBSERVED `JUSUBIN_FAST_HALF_SWB/.project` and `JUSUBIN_FAST_HALF_5V_TEST/.project` both exist as zero-byte files (Oct 8 16:58) per user terminal. Copy's SDevice source previously matched original with `cmp`.
- SWB GUI open, tool-flow nodes, and independent project path remain UNVERIFIED; marker alone is not full recognition proof.
- NEXT: open `JUSUBIN_FAST_HALF_5V_TEST` from SWB Projects list or project open menu, check screenshot. No Run/F7 or code edits. Preserve original.

---



## 2026-10-09 — Filesystem copy exists; SWB open not yet checked
- 이택규 executed `cp -a JUSUBIN_FAST_HALF_SWB JUSUBIN_FAST_HALF_5V_TEST`, subsequent ls confirmed target directory and `cmp` between original/copied SDevice source produced no differences.
- Bash-style conditional produced `if: Expression Syntax.` in current C-shell-like terminal; standalone copy command worked.
- Next verify original/copied hidden `.project` file and project directory content, then open copied project in SWB Projects browser; preserve original, do not run simulations or edit high-bias deck yet.
## 2026-10-09 Original Transient endpoint verified
- 이택규 verified executable original Node2 Transient: FinalTime 0.06, Goal anode 0.3V, Inner Coupled Iterations 15. Header 0–4/4–5 V comments are stale for the smoke.
- Original Transient 0.3V smoke complete; QS Copy failed at 0.019304636V. Neither proves the 3–5V LED baseline or full/fine equivalence.
- Preserve original, QS Copy and outputs. Next review separate higher-bias transient branch without changing Common Baseline. No SDevice sources were modified.

---

## 2026-10-09 — Transient versus QS settings checked (이택규 / ChatGPT)
- OBSERVED original `JUSUBIN_FAST_HALF_SWB/pp2_des.cmd` and QS Copy pp2: both startup Poisson Coupled 500 with LineSearchDamping=1e-2, initial carriers Coupled 100, sweep inner Coupled Iterations=15; ErrRef e/h 1e4, RHSMin=1e-3. So lack of QS sweep damping is NOT a unique QS-vs-original difference.
- Original Transient controls InitialStep 1e-5, MinStep 1e-9, MaxStep 1e-3, Increment 1.2; QS InitialStep .03, MinStep 1e-6, MaxStep .15, Increment 1.5, Decrement 2.0. Different time semantics; direct numerical comparison invalid.
- QS stopped Newton nonconvergence near 0.019304636V; original transient completed 0.3V. No change applied to TCAD sources.
- Noted discrepancy: header comments in original preprocessed deck mention 0–4.0V and 4.0–5.0V; actual completed smoke log was 0.3V. Inspect executable original Goal and full Solve in pp2 lines 583–615 instead of extrapolating from comments.
- Underlying root cause still unresolved; preserve baseline and both branches. Next: verify original Goal/step block, then design an isolated QS stability test only if justified.

---

## 2026-10-09 — QS Copy actual Math/Solve controls inspected (이택규 / ChatGPT)
- Exact preprocessed QS deck (user terminal): `ErrRef(e/h)=1e4, RHSMin=1e-3, CheckRhsAfterUpdate, Transient=BE, ExtendedPrecision(80), Blocked/ILS(set=22)`; initialization Poisson 500 iterations + `LineSearchDamping=1e-2`, startup carrier coupled 100 iterations; QS Goal 0.3V, `InitialStep=.03, MinStep=1e-6, MaxStep=.15, Increment=1.5, Decrement=2`, inner coupled Poisson/Electron/Hole `Iterations=15` (no explicit damping).
- Observed failure: Newton 15 iter, nonconvergent RHS at 0.019304636V; step cutback below MinStep. Underlying root cause UNRESOLVED. Damping within QS is a **proposal**, not yet verified fix.
- WARNING: `Save(n2_qs0p3_ckpt)` executed after QS failed, despite code comment saying only after 0.3V completed. This checkpoint must not be interpreted as verified 0.3V.
- Next: inspect/compare original transient pp2_des.cmd Math/Solve numeric controls and physics; no code changed; preserve original full/common baseline and both results.

---

## 2026-10-09 — Final QS Copy convergence diagnostic (이택규 / ChatGPT)
- Source log user provided `n2_des.log` 6900-6997: on t=0.0643488→0.0643505 (step 1.6797e-6), Poisson/electron/hole Bank/Rose Newton with factor 1.0 oscillates strongly, Rhs up to 1.26e8; after 15 iterations final Rhs 1.85e6 → `#iterations larger than 15`. Retry 8.3986e-7 violates MinStep 1e-6; sweep stops, last accepted V=0.0193046363 V of 0.3 V.
- `.err`: repeated vanOverstraetendeMan E0 isotropic/anisotropic difference; direct link to failure not established. DOS mass interpolation is logged.
- Already tried: actual QS Copy started and completed process but not bias sweep; separate original transient 0.3V completed.
- Next: inspect actual QS pp2_des.cmd Math/Solve settings for controlled numerical-only remedy; preserve physical Common Baseline, both branches. Do not blindly lower MinStep or claim QS speedup.

---

## 2026-10-09 — QS Copy last voltage clarified (이택규 / ChatGPT)
- OBSERVED: last saved `.plt` time 0.0643487876313307 and `anode OuterVoltage` 0.0193046362893992 V, only 6.435% of 0.3V goal.
- UNRESOLVED blocker: SDevice QS reports `Step-size less than MinStep (8.3986e-07)` near t=0.06435; exact underlying solver issue unknown.
- Read `sed -n '6900,7010p' n2_des.log` and `tail -n 40 n2_des.err` before editing or restarting.
- Preserve original 0.3V transient and Common Baseline; QS elapsed time is not a fair speedup benchmark.

---

## 2026-10-09 — QS Copy MinStep blocker (Lee Taekgyu; ChatGPT)
- Project: `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_SWB_Copy`; distinct from completed transient original.
- User-shared `n2_des.log`: `Finished, because... Step-size less than MinStep (step-size = 8.3986e-07)`; SDevice final `Good Bye !`, save + plot written, 18417.09 s (5:06:57), max memory 2.96 GB.
- Failure: QS goal 0.3 V NOT verified. Saved checkpoint is not convergence evidence.
- Already tried: SWB Copy QS source and pp2 preprocess validated on Oct 8; QS SDevice actually ran. Original transient reached 0.3 V normally in 25019.43 s.
- First next: extract final accepted anode bias from QS `n2_des.plt` tail, cutback/step attempts in `n2_des.log`, and relevant `.err`; diagnose before changing solver settings.
- Preserve: Common Baseline geometry/physics/traps, original transient & full reference results. Do not blindly reduce MinStep or claim QS speed gain.

---

## 2026-10-06 — 이택규 → 주수빈/다음 작업자 인수인계

오늘은 FAST_C1 Node 6(NtSide=0)·Node 12(NtSide=1e18)가 실제로 멈춘 게 아니라 high-bias에서 timestep을 키웠다가 Newton 실패 → 약 1/2 cutback → 다시 수렴하는 패턴 때문에 매우 느리다는 것을 로그로 확인했다. D1에서 linear solver maxit 문제가 아니라 RHS가 1e-3 바로 위에서 정체되는 timestep-dependent nonlinear bottleneck임을 확인했고, D2에서 Node 6은 accepted Newton max=4였지만 Node 12는 13·15 iteration에서 실제 accepted된 step이 있어 Claude가 제안했던 공통 C2 Iterations=8/10은 폐기했다. 따라서 첫 공통 FAST_C2는 Iterations=15를 유지하고, high-bias Increment만 1.2→1.05로 낮추는 방향으로 간다. D3에서 live .plt로 I(V)를 뽑았고, provisional J는 아직 너무 낮아 '5 V 대신 current-density window에서 분석 종료' 결정은 보류했다. D6에서는 기존 n6_inter_0004_des.tdr을 Load해보았지만 'contains no SLP information'으로 실패해, 현재 C1 intermediate TDR로 restart하는 Option 3은 폐기했다. Node 6/12 기존 run은 reference로 계속 유지하는 것이 원칙이다.

현재는 Option 2만 남겨서 새 C2 smoke를 별도 scratch에서 검증 중이다. 새 smoke deck은 segment1 0→0.2 V에서 Increment=1.2/Iterations=15, 0.2 V에서 Save checkpoint, segment2 0.2→0.3 V에서 Increment=1.05/Iterations=15로 구성했고 syntax/preprocess 없이 실제 sdevice가 초기 Poisson solve까지 정상 진입했다. 다만 checkpoint가 생기기 전에 restart test를 실수로 두 번 실행해 PID 14179/14180이 생겼으므로, 내일 시작하면 먼저 `ps -u semi437 -o pid,etime,pcpu,args | grep -E '13881|14179|14180|c2smk|sdevice'`로 확인하고 14179/14180이 살아 있으면 그 둘만 종료한다. smoke PID 13881은 계속 두고 `tail -n 80 ~/CMP_C2_SMOKE/c2smk.out`와 `ls -lh ~/CMP_C2_SMOKE/c2smk_ckpt_0p2V*`로 0.2 V Save checkpoint 생성 여부를 확인한다. checkpoint가 실제 생성된 뒤에만 `c2smk_ld02_des.cmd`를 딱 한 번 실행해 Save-generated checkpoint가 Load되는지 검증하면 된다. 이 Load가 성공하면 그 다음이 production C2 preprocess/launch 단계다.

---

## 2026-10-06 — FAST_C2 handoff after Claude runtime analysis review

- 작업자: 이택규
- 사용 AI: Claude analysis reviewed by ChatGPT
- 상태: PROPOSED / NOT EXECUTED
- exact problem: Node 6/12 are alive but high-bias runtime is dominated by repeated timestep growth/rejection/cutback cycles.
- evidence: Node 6 dt=1.1842e-5 rejects after RHS ~1.41e-3 stagnation to Iteration 15; half-step retry 5.9211e-6 converges in 2 iterations. Node 12 shows repeated near-half cutbacks too.
- reviewed strategy: `CMP/FAST_BASELINE_C2.md`.
- proposed tools: `CMP/tcad/tools/make_restart_deck.py`, `CMP/tcad/tools/iv_window.py`; synthetic-only tested.
- do not change: current running Node 6/12, Common Baseline physics/geometry/traps/RHSMin, protected 5 V endpoint.
- unresolved: InitialTime/FinalTime+Goal segmented semantics, Save/Load syntax, existing -Loadable TDR restartability, actual J normalization.
- important validation caveat: changing transient timestep sequence can alter trap state; NtSide=1e18 C2 equivalence must include trap/SRH/radiative/carrier metrics, not only I-V.
- next first action: D1–D6; then C2 smoke gate. Decision 0 (J-window endpoint) requires team approval.

---

## 2026-10-04 — B0 COMPLETE; handoff to FAST C1 preprocess

- 285/285 rejection/retry pairs checked with explicit Stepsize-derived dt.
- ratio min=0.499975805, max=0.500023337, mean=0.499999621 -> fixed 0.5 cutback confirmed.
- C1 source unchanged, Iterations=15.
- next: separate project/copy -> exact C1 source SHA -> preprocess gate.
- live x6/x7/x8 untouched.

---

## 2026-10-04 — Claude B0 review accepted: C1 unchanged

- 작업자: 이택규
- C1 source unchanged; SHA `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`; `Iterations=15`.
- correction: ~4.33 V is not trajectory divergence; it is the first rejected attempt where x8/C1 Newton count is expected to differ 50->15.
- A1': accepted-step sequence and rejection points should match over overlap; unexplained mismatch = UNEXPECTED.
- A1'': all C1 rejections must show `#iterations larger than 15.`; 50 => cap not applied, stop.
- new audit tool SHA-256: `9a935633e92bc55fa86849b6988b60a8a8ee55f637387ced62721d9f6267d281`.
- package selftest independently passed by ChatGPT.
- raw observed cutback ratios are ~0.5; full 285-rejection CSV constancy is pending because CSV was not included in package.
- patch-equivalent commit: `ace056fcb01d2e6e785dbee08a213e1148d6be35`.
- next: separate-project preprocess -> NtSide=0 B1 benchmark.
- live x6/x7/x8 untouched.

---

## 2026-10-04 — B0 result: C1 Iterations=15 cleared for first benchmark

- worker: 이택규
- x8 raw audit parsed 2236 attempts: 1950 accepted / 285 rejected.
- accepted Newton iterations: 2–4 only; max=4.
- all 285 rejected attempts reached 50 iterations; raw log explicitly says `#iterations larger than 50.`
- predicted N=15 false rejection = 0 on observed path through ~4.643 V.
- rejected attempts consume ~75% of observed attempt wallclock.
- idealized saved time for cap 15 ≈72.3 h over the copied trajectory; simple idealized speedup ≈2.11x, before extra recovery overhead.
- C1 is therefore cleared as PROPOSED first numerical candidate for separate-project preprocess + NtSide=0 benchmark.
- limitations: no evidence yet for 4.643→5.0 V; parser does not yet parse real-log `error` column; current recovery-step metric should be ignored.
- do not modify live x6/x7/x8.

---

## 2026-10-04 — B0 preprocessed check result

- active Copy x8 `pp6_des.cmd`: transient inner Coupled has no explicit `Iterations`; only initial 500 and equilibrium 100 are present.
- `RHSMin=1e-3`, `CheckRhsAfterUpdate`; no `NotDamped`.
- The recorded ~50 failed Newton rows therefore cannot be attributed to an explicit `Iterations=50` in pp6_des.cmd.
- Next evidence needed: raw x8 `n6_des.out` + parser-verified B0 audit.
- Claude should receive this observation and the B0 output before C1 is executed.

---

## 2026-10-04 — ChatGPT review of Claude FAST C1

- 작업자: 이택규
- Claude C1 status: PROPOSED / REVIEWED / NOT EXECUTED.
- golden SHA: `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`.
- C1 SHA: `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`.
- only executable change: transient inner Coupled `Iterations=15`.
- C1 and ChatGPT v0.1 are executable-statement equivalent.
- first-candidate logic is supported by Synopsys 2022 training (default 20; 15–20 recommended before timestep reduction).
- blocker: project record of ~50-iteration failures conflicts with documented default 20. B0 must inspect exact x8 `pp6_des.cmd` + raw `n6_des.out` and validate the parser.
- Claude tools passed syntax/synthetic selftests only; actual Sentaurus log/PLT formats unverified.
- raw patch was not applied verbatim: stale `sd_fdiv_des.cmd missing` state and “stop x7” recommendation were rejected/corrected.
- live x6/x7/x8 remain untouched.
- canonical reviewed record: `CMP/FAST_BASELINE_C1.md`.

---

## 2026-10-04 — Claude GitHub permission clarification

- 작업자: 이택규
- 이택규의 Claude는 GitHub READ 가능, WRITE/EDIT 불가.
- Claude는 구현/분석 결과를 채팅에 반환하고 GitHub 저장 성공을 주장하지 않는다.
- 실제 GitHub 기록/수정은 ChatGPT가 Claude 결과를 검토한 뒤 수행한다.
- `CMP/prompts/CLAUDE_FAST_BASELINE_IMPLEMENTATION.md`도 이 권한 구조로 정정됨.

---

## 2026-10-04 — Claude implementation package is ready

- 구현 담당: Claude
- GitHub handoff/prompt: `CMP/prompts/CLAUDE_FAST_BASELINE_IMPLEMENTATION.md`
- user must attach exact source: `Copy_x8_sd_fdiv_des.cmd`
- expected source SHA-256: `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`
- Claude must read project instructions/state before coding.
- public `CMP/tcad/CURRENT` SDevice is stale and must not be used as the base.
- previous ChatGPT `Iterations=15` is PROPOSED only, not a required patch.
- Claude must produce complete code, unified diff, Workbench steps, preprocess checks, short benchmark, acceptance and rollback criteria.
- do not commit proprietary full source to public GitHub.

---

## 2026-10-04 — sequence correction: FAST coding precedes final clean-account freeze gate

- 작업자: 이택규
- Copy x8 golden reference freeze는 완료.
- 지금부터 separate numerical-only FAST_BASELINE 코드를 작성하고 short benchmark한다.
- clean-account reproduction은 최종 FAST deck freeze 및 Project A/B production 전에 반드시 수행하되, FAST 코드 작성 자체의 선행 blocker로 두지 않는다.
- 첫 benchmark 변수는 Newton iteration/cutback policy.
- x8 live directory는 수정 금지.

---

## 2026-10-04 — clean-account reproducibility requirement before FAST baseline freeze

- 작업자: 이택규
- 사용자 목표: 최종 baseline은 주수빈 계정과 이택규 계정에서 동일 source로 독립 재현되어야 함.
- 과거 경험: 동일 코드/파라미터를 다른 계정에 복사했을 때 실행되지 않은 사례가 있었음. 원인을 단순한 "계정에 축적된 상태"로 확정하지 않음.
- Claude/ChatGPT는 working account의 exact source뿐 아니라 preprocessed outputs와 project/runtime context를 함께 비교해야 함.
- 필수 비교 대상:
  - original SDE/SDevice source
  - pp1_dvs.cmd
  - pp6_des.cmd / pp6_des.par
  - mesh statistics and reference n1_msh.tdr hash
  - Workbench variables/tree/scenario files where relevant
  - n6_des.job/sta/err/out/log
  - Sentaurus version/path and thread settings
- 재현 절차:
  1. working semi437 Copy x8를 immutable reference로 보존.
  2. new account에서 source를 새 project로 import.
  3. full solve 전에 preprocess only / early initialization 단계까지 실행.
  4. pp1_dvs.cmd, pp6_des.cmd, pp6_des.par를 working account와 exact diff.
  5. mesh vertex/element statistics 비교.
  6. 차이가 있으면 full multi-day solve를 시작하지 않고 먼저 원인을 해결.
- FAST_BASELINE은 이 clean-account reproducibility gate를 통과할 수 있게 설계한다.

---

## 2026-10-03 — baseline execution split plan

- 최종 baseline 구현 단계에서는 동일한 검증 baseline을 주수빈 계정 1개, 이택규 계정 1개에 각각 실행할 계획.
- 두 계정에서 동일 조건을 재현한 뒤, 각자 맡은 후속 작업을 병렬로 진행.
- 향후 실행/코드 인수인계 시 이 병렬 운용 계획을 전제로 한다.

---

## 2026-10-03 — Claude handoff: active baseline runtime source needed

작업자: 이택규
상태: PROPOSED

현재 약 7일간 실행 중인 baseline run의 runtime 최적화 전에 주수빈 측에서 실제 실행 자료를 GitHub에 동기화해야 한다.

필요 자료:
- 실제 실행에 사용한 원본 SDevice 전체
- active node의 pp*_des.cmd
- active node의 pp*_des.par
- 최신 *_des.out 마지막 구간
- 가능하면 node 번호, NtSide 조건, pseudo-time, timestep, elapsed time, log/sta

Claude 작업 원칙:
- GitHub CURRENT의 기존 sdevice2_defect_on.cmd를 현재 active run과 동일하다고 가정하지 않는다.
- 실제 실행 원문을 기준으로 lineage를 확인한다.
- Common Baseline geometry/physics/Nt/Et/sigma는 유지한다.
- runtime 최적화는 numerical-only branch에서 수행한다.
- MaxStep/staged bias, Newton iteration, ErrRef, high-bias cutback, far-field mesh를 우선 검토한다.
- full multi-day run 전에 short benchmark로 기존 설정과 비교한다.

---

# AI RELAY

## 2026-09-28 — Lee Taek Gyu session: Final SDevice source-sync blocker

### Exact problem
JuSubin's Issue #7 / timeline say Final SDevice v1.2 was prepared, but `CMP/tcad/CURRENT/sdevice2_defect_on.cmd` is still an older deck and lacks the v1.2 intermediate TDR saves.

### Confirmed evidence
The current GitHub file still has hard-coded `Conc=1e18`, global `IncompleteIonization`, and no intermediate transient Plot/Time saves.

### Do next
Recover the exact full user-provided Final SDevice v1.1/v1.2 source from the JuSubin chat/file and sync that exact source to CURRENT.

### Do not do
Do not reconstruct v1.2 from Issue #7 snippets or from memory. The stale CURRENT deck is not a safe base for a final-code overwrite.

---



## 2026-09-21 — ChatGPT → Claude

### Context
이택규와 Common Baseline Defect-ON flow를 디버깅 중.

### Exact blocker
Node 9 SDevice2의 solver output은 `Good Bye !`까지 정상 종료했지만, Node 10 SVisual2가 찾는 `n9_des.tdr`이 Node 9 Output Files screenshot에서 보이지 않았다.

### What has already been tried / learned
- SVisual2의 `create_plot -2d`는 T-2022.03에서 invalid.
- `@node|sdevice@` reference는 현재 Workbench flow에서 invalid.
- SDevice의 `Plot { ... }` block을 SVisual Tcl에 붙이면 `invalid command name "Plot"`가 난다.
- SVisual2 자체는 현재 최소한의 `@previous@` 기반 loader로 복구됨.
- Node 9 SDevice2 output에는 Plot variable list가 출력되고 solver는 종료됨.

### Please do next
코드를 바로 다시 쓰기 전에 `pp9_des.cmd`의 preprocessed `File { ... }`에서 실제 `Plot=` 경로를 확인하라.
그 파일명과 Node 9 Output Files를 비교한 뒤 원인을 분기하라.

### Do not do
- trap physics parameter 변경
- unverified Plot variable 대량 추가
- JBD 4 µm pitch를 exact mesa로 해석
- SDE/SDevice1 full source를 추정 생성

### Relevant files
- `CMP/.ai-sync/LIVE_STATE.md`
- `CMP/tcad/CURRENT/sdevice2_defect_on.cmd`
- `CMP/tcad/CURRENT/svisual2_maps.tcl`
- `CMP/ERROR_LOG.md`

---

새 AI 메시지는 이 문서의 맨 위에 추가한다.
