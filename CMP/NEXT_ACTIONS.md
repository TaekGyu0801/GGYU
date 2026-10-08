## 2026-10-08 — 주수빈 accelerated Baseline QS smoke (PROPOSED)

1. Keep original full FAST_C1 reference runs untouched. For JUSUBIN_FAST_HALF_SWB, capture current n2 transient smoke output and if switching, stop **only** the old Node2 job in SWB.
2. Install private `sdevice_des_JUSUBIN_HALF_COARSE_QS_SMOKE.cmd` as `sdevice_des.cmd` after backup (QS anode 0→0.3 V; source SHA256 `a7281c79e7e440c6192726f4ce6edefb58f8d76ed30ec921900fee5ff5a5ec01`).
3. SWB preprocess only; verify pp2_des.cmd has `Quasistationary(`, Goal=0.3, Grid=n1_msh.tdr, NtSide=0, no executable DmgR, RHSMin=1e-3, Iterations=15.
4. Run QS 0.3V smoke; report normal completion, current consistency and wallclock. Source/static test does NOT guarantee convergence.
5. Only if QS speed/convergence are favorable, design validated staged 0→5V QS candidate and compare against full transient reference at identical bias/current including sidewall/QW recombination and trap state. Do not presume QS/transient numerical equivalence for non-equilibrium effects.

## 2026-10-08 — cmp216 Node6 terminal/runtime diagnosis (READ ONLY)

1. Verify process on current host (`ps -ef | grep '[s]device'`) and inspect relevant login history (`last -n 10 cmp216`); if SWB spawned remotely check its host/job details separately.
2. Inspect how the separate `FAST_C1_ACCOUNT_TEST` SDevice test was launched (`history | tail -n 25` where available) and logs for non-standard exit. Avoid asserting interruption cause without exit code/system evidence.
3. Do not overwrite existing log/PLT; do not stop semi437 reference runs. Decide on detached batch run only after root cause/provenance analysis.

## 2026-10-08 — 이택규 urgent optional half+bulk-coarse pilot (PROPOSED, parallel branch)

1. Without disturbing full/fine FAST_C1 references, obtain exact active SDE source (or pp1_dvs.cmd) plus copied active SDevice source / pp6_des.cmd and pp6_des.par from Workbench. Public CURRENT source may be stale.
2. Verify left/right symmetry of actual electrodes/doping/material/geometry and identify physical mesa center, full domain edge and DmgL/DmgR regions; do not guess the half-plane coordinate.
3. Create separate half-domain SDE, retaining **one intact 5nm damaged edge** and placing symmetry plane at center. Change only far-remote homogeneous n-GaN bulk/numerical n-base mesh spacing moderately (~1.5–2x candidate) while preserving MQW/EBL/heterointerface/damaged 5nm refinement.
4. SDE-only mesh + region/contact geometry check; compare current mesh element/point statistics (reference 290814 elements, 137831 points) and confirm all surviving SDevice region physics blocks are valid after removed-side region deletion.
5. Use copied baseline physics and numerical tolerances (Iterations=15, RHSMin unmodified). Run preprocess-only then short low-bias smoke; compare I_half×2 against full I at identical bias using the same depth convention, plus representative QW and edge fields. Note that combined domain/mesh branch is an exploratory speed experiment, NOT a proven numerical/physical equivalence.
6. Only if smoke is valid, run a longer pilot. Existing unresolved very-low-J and Save/Load/region-integration gates still must be resolved before publication-grade A/B production.

## 2026-10-07 — Before any Project A/B multi-day production run

1. Finish/freeze the FAST_C1 Common Baseline reference evidence.
2. Audit the exact active `pp1_dvs.cmd`, `ppN_des.cmd`, `ppN_des.par` that will be inherited by A/B; do not use stale public CURRENT as proof.
3. On an existing intermediate TDR, prove all required datasets and extraction: sidewall SRH, MQW Rrad/RAuger/IQE, carrier/current, crowding, lateral Ec/Ev, trap/polarization.
4. Confirm 2D current -> current-density normalization and freeze full-mesa area convention.
5. Project A: implement parameterized `Cedge_L/R`, explicit Cedge mesh, carbon parameters (with optional compensation slot), and a carbon-off null control.
6. Project B: decide exact AlBarrier vertical span first; then implement parameterized `AlBarrier_L/R`, xAl/wAl, lateral-interface mesh, and a clean null control.
7. Complete Save/Load smoke before relying on checkpoints.
8. Preprocess-only + short smoke for A and B.
9. Run exactly one representative pilot A and one representative pilot B; verify runtime, convergence, V(I), saved-state coverage and postprocessing.
10. Only then launch the broader DOE. See `CMP/PROJECT_AB_PRE_RUN_AUDIT.md`.

## 2026-10-06 — C2 smoke immediate handling

1. Check whether premature restart PIDs 14179/14180 are still alive; terminate them if so.
2. Keep smoke PID 13881 running.
3. Do not run Load test until smoke reaches the 0.2 V Save point and `c2smk_ckpt_0p2V*` exists.
4. Then launch exactly one check-only Load test and inspect its log.

## 2026-10-06 — D6 이후 다음 단계

1. 기존 C1 intermediate TDR restart 시도는 종료.
2. Node 6/12 reference run 유지.
3. `make_c2_smoke_deck.py`로 copied `pp6_des.cmd`에서 short smoke deck 생성.
4. smoke 조건: segment1 0→0.2 V, Increment=1.2, Iterations=15; Save checkpoint 생성; segment2 0.2→0.3 V, Increment=1.05, Iterations=15.
5. smoke 완료 후 Save-generated checkpoint 파일 존재 확인.
6. 그 checkpoint를 `make_restart_deck.py --mode check`로 Load-test.
7. Save/Load smoke가 통과한 뒤에만 production C2 preprocess/launch.

## 2026-10-06 — Next: D6 Node 6 4.7 V Load gate

1. Keep Node 6/12 running.
2. CPU headroom PASS; license headroom still unknown.
3. Run D6 only in a separate scratch directory using copies of n1_msh.tdr, pp6_des.par/cmd and n6_inter_0004_des.tdr.
4. Generate a check-only restart deck; do not continue bias yet.
5. Launch as a third short SDevice job and inspect immediately for license wait or Load syntax/data error.
6. If Load succeeds, compare steady re-solve anode current at 4.7 V with the reference current around 4.7 V before allowing Option 3.
7. Decision 0 J-window remains pending; current provisional J values are far below 0.1 A/cm2.

## 2026-10-06 — D3 next: extract I(V) / provisional J(V)

1. D2 exception check CLOSED: Node 12 13/15-iteration accepted steps are real and barely meet RHSMin.
2. D3 structural gate PASS: live .plt files exist, are current, contain anode TotalCurrent, and no explicit AreaFactor is present in pp cmd/par.
3. Copy live .plt files and run iv_window.py read-only.
4. Treat J values as provisional until exact T-2022.03 2D current normalization is verified; I(V) itself is directly usable.
5. Keep Decision 0 pending until I(V)/J(V) window is inspected.
6. In parallel, perform D4 progress snapshot and D5 resource check.

## 2026-10-06 — D2 complete; inspect Node 12 exceptions, then D3

1. D2 CLOSED: cap 8 and cap 10 are not safe universal C2 settings because Node 12 has accepted 13- and 15-iteration steps.
2. Extract the exact Node 12 accepted attempts with iterations >8 from the audit CSV and confirm their bias/time/final RHS.
3. First common C2 candidate: Iterations=15 retained; Increment=1.05 is the first runtime lever.
4. Do not execute the original cap-8 C2 deck as-is.
5. Then D3: verify .plt update plus AreaFactor/2D current normalization before using current-density windows.

## 2026-10-06 — D1 complete; D2 is next

1. D1 CLOSED: current Node 6 failure is not a GMRES maxit stall; keep linear solver unchanged for first C2 candidate.
2. D2 NOW: audit full current Node 6 and Node 12 logs for accepted Newton-iteration distribution and cap-8 false rejection risk.
3. Keep both live C1 reference runs running during the audit.
4. Only if D2 shows sufficient accepted-iteration margin may FAST_C2 retain high-bias Iterations=8; otherwise use 10 or keep 15.
5. After D2 proceed to D3 current-density normalization/window check.

## 2026-10-06 — FAST_C2 immediate validation sequence (PROPOSED)

1. Keep current FAST_C1 Node 6 and FAST_C1_Copy Node 12 running; do not stop for C2.
2. D1: inspect failed/success Newton table columns to diagnose dt* mechanism.
3. D2: audit current Node 6/12 accepted-iteration distribution; Iterations=8 is allowed as a candidate only if the observed accepted-step margin remains sufficient.
4. D3: inspect .plt update and verify AreaFactor/2D normalization before using current-density values.
5. D4: measure Node 6/12 progress over fixed 1–2 h windows.
6. D5: verify CPU/license headroom before launching smoke/C2 parallel work.
7. D6: test whether existing intermediate TDR can be loaded; Option 3 is blocked unless this passes.
8. Run C2 smoke test to verify segmented global time/Goal and Save/Load syntax.
9. Only after smoke/preprocess gates pass: launch NtSide=1e18 C2 first, then NtSide=0 if resources allow.
10. Validate C2 against C1 at matched bias/current including I-V/Vf, trap charge/occupancy, sidewall SRH, QW radiative/Auger and carrier distributions.
11. Decision 0 remains TEAM DECISION PENDING: J-window analysis endpoint. Do not change the protected 5 V baseline endpoint yet.

## 2026-10-06 — Immediate runtime-first branch: half + coarse mesh

1. Keep existing FAST_C1 full Node 6/12 untouched as reference evidence.
2. Create a separate half-domain candidate centered at the mirror plane; retain one physical sidewall and matching one-sided SDevice region references.
3. Coarsen only remote/global homogeneous bulk first; preserve MQW/EBL/heterointerface/5 nm damage refinement near current resolution.
4. Build SDE mesh before any long SDevice solve and record Elements/Points plus mesh screenshots around MQW, EBL, sidewall damage, and n-GaN bulk.
5. Runtime-oriented engineering target: reduce mesh substantially from 290,814 elements; do not claim a fixed target as validated physics.
6. If only one accelerated electrical case is launched first, prioritize the nominal damaged baseline NtSide=1e18 for mechanism-relevant preliminary A/B comparisons; keep NtSide=0 as control/reference when resources allow.
7. For half-domain comparison, compare 2×half terminal current with full current (or current density); IQE itself should not be multiplied by 2.
8. Treat this branch as preliminary/screening until full-vs-half/coarse equivalence is checked at matched bias/current.

## 2026-10-06 — Deadline triage for Oct 23 abstract

1. 현재 FAST_C1 Node 6/Node 12는 자원 충돌이 없으면 계속 유지하여 full-reference evidence를 확보한다.
2. 동시에 별도 copy에서 numerical-only accelerated C2 pilot를 만든다. 기존 physics/mesh/trap/contacts는 고정한다.
3. 첫 benchmark는 full 0→5 V가 아니라 동일 초기상태/대표 bias 구간에서 Transient C1 vs DC-oriented Quasistationary/staged sweep의 convergence/runtime/I-V equivalence를 비교한다.
4. PASS 기준을 먼저 정의: matched-bias I-V, Vf, carrier distribution, SRH/radiative/Auger 및 spatial profile이 reference와 허용오차 내 일치해야 한다.
5. accelerated method가 PASS하면 Common Baseline과 A/B screening에 사용하고, 최종 대표 case만 full validation한다.
6. 초록 제출 전 목표는 모든 parameter sweep 완료가 아니라, 검증된 Common Baseline + mechanism을 보여줄 최소 preliminary A/B evidence 확보로 설정한다.

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

## 2026-10-06 — Deadline-aware publication plan

1. Keep FAST_C1 Node 6 running as the full-reference NtSide=0 case.
2. Check server capacity; if sufficient, launch NtSide=1e18 in a separate clean FAST_C1 project in parallel.
3. Do not loosen RHSMin for the publication baseline without a dedicated sensitivity study.
4. Build the next acceleration test around safer numerical levers first: staged step-growth policy / thread count / checkpointing.
5. Define the scientific operating-current window from the validated baseline.
6. Use that reduced window for broad Project A/B screening.
7. Full 0–5 V validation only for baseline, best/representative/worst A/B cases, and cases needed to establish Vf/I–V limits.
8. Perform mesh-convergence on a small representative set, not every sweep point.
9. Final paper plots/tables must come only from validated full or explicitly convergence-checked runs.

## 2026-10-06 — Quantify FAST_C1 high-bias progress rate

1. Keep FAST_C1 Node 6 running for now; it is confirmed alive at ~4.682 V and C1 Iterations=15 is active.
2. Do not infer completion ETA from the 0→4.682 V average.
3. Use a fixed recent log window to measure:
   - pseudo-time / anode-voltage advance,
   - accepted attempts,
   - rejected attempts,
   - average accepted-step wallclock,
   - average rejected-step wallclock.
4. Recalculate mV/hour from that recent high-bias window.
5. Decide whether to continue to 5 V or redesign the numerical schedule based on the measured tail rate.
6. Preserve the current run and logs; no physics changes.

## 2026-10-06 — Immediate runtime check before waiting longer

1. FAST_C1 Node 6 has been running ~41 h 48 min without a completed node by user report.
2. Before simply waiting longer, inspect current process state and the tail of FAST_C1 n6_des.out.
3. Record latest pseudo-time/anode voltage and compare with the last known point to prove forward progress.
4. Confirm C1 rejected attempts report the 15-iteration cap; if 50 still appears, stop because the intended C1 cap is not active.
5. If progress is real, estimate mV/hour from recent log intervals rather than extrapolating from the old 65.4 h run.
6. If progress has stopped or repeated cutbacks dominate with no meaningful voltage advance, reassess numerics before investing another multi-day run.
7. Keep staged A/B screening strategy; do not brute-force every parameter case over full 0→5 V.

## 2026-10-04 — Revised immediate action and staged production plan

1. Do NOT discard the currently running FAST_C1 Node 6 yet.
2. While it runs, execute read-only preprocess equivalence gate on existing pp6_des.cmd/par.
3. PASS -> continue current Node 6 as B1; FAIL -> stop and correct.
4. After one full/validated FAST reference, define the matched-current operating window used for A/B scientific comparison.
5. Use reduced-window screening for broad A/B parameter exploration.
6. Full 0→5 V runs are reserved for baseline/final representative cases and any case needed to establish I–V/Vf limits.
7. Evaluate adding true `Save` checkpoints for long runs; current `Plot(-Loadable)` snapshots cannot be used as restart checkpoints.

## 2026-10-04 — Runtime-aware A/B rollout after baseline freeze

1. Freeze FAST C1 common baseline only after NtSide=0 and NtSide=1e18 validation.
2. Project A: run one representative GaN:C case first; measure runtime, cutbacks, convergence, I-V/Vf/SRH behavior before launching a parameter sweep.
3. Project B: same approach with one representative AlGaN barrier case.
4. Only after pilot runtime is known, launch independent parameter points in parallel where resources permit.
5. Do not reduce physical validation scope solely to meet runtime; optimize numerics and scheduling instead.

## 2026-10-04 — Baseline freeze criteria

1. Stop/hold any pre-gate FAST_C1 solve.
2. Run preprocess equivalence gate.
3. Run and validate NtSide=0 B1.
4. Then run NtSide=1e18 with the same frozen C1 setup.
5. Freeze FAST_C1 as common baseline only after both cases pass.
6. Use NtSide=0 as defect-free control and NtSide=1e18 as nominal defect baseline for subsequent Project A/B comparisons.

## 2026-10-04 — Stop accidental FAST_C1 solve and audit generated deck

1. In Workbench, stop only FAST_C1 Node 6 (NtSide=0) that launched at 15:46.
2. Do not kill/modify unrelated processes.
3. After stop, confirm no FAST_C1 `sdevice` remains.
4. Preserve generated `pp6_des.cmd` and `pp6_des.par`; they are the preprocess products needed for the gate.
5. Run read-only preprocess equivalence checks against Copy x8.
6. Restart NtSide=0 B1 only after gate PASS.

## 2026-10-04 — FAST_C1 preprocess-only next

1. 원래 Copy x8 live process PID 78941은 건드리지 않는다.
2. Workbench에서 FAST_C1 프로젝트를 별도로 열고 Node 6 (NtSide=0)만 Preprocess한다.
3. Run/Solve는 누르지 않는다.
4. preprocess 완료 후 `pp6_des.cmd`, `pp6_des.par` timestamp/hash를 확인한다.
5. `fast_preprocess_check.py`로 golden-vs-C1 gate 수행.
6. PASS 후에만 NtSide=0 B1 solve를 시작한다.

## 2026-10-04 — FAST_C1 source installed; inspect Workbench status before preprocess

1. Read `.status` and `gtree.dat` in FAST_C1.
2. Confirm Node 6 is NtSide=0 and Node 12 is NtSide=1e18.
3. Confirm copied execution state will not accidentally launch/resume a solve.
4. Then preprocess Node 6 only; do not run SDevice.
5. Run `fast_preprocess_check.py`.
6. Only after gate PASS start NtSide=0 B1.

## 2026-10-04 — B0 CLOSED; begin separate FAST C1 preprocess

1. Keep live x6/x7/x8 untouched.
2. Create a separate FAST C1 Workbench project/copy.
3. Generate/install the exact C1 source from the frozen x8 source with only the transient inner Coupled `Iterations=15` change.
4. Verify C1 source SHA-256 = `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`.
5. Preprocess only.
6. Run the preprocess gate:
   - golden mesh/parameter provenance preserved
   - exactly one intended executable change in SDevice: `Iterations=15`
   - no physics/trap/geometry/step-control drift
7. Only after preprocess PASS: run NtSide=0 B1 benchmark with A1'/A1''.

## 2026-10-04 — Regenerate B0 CSV using explicit Stepsize

1. Download current `sdevice_newton_audit.py` from GitHub main.
2. Run `--selftest`.
3. Rerun the copied x8 log audit to regenerate `~/CMP_B0/x8_attempts.csv`.
4. Recompute `retry_dt / rejected_dt` across all 285 rejection/retry pairs.
5. Treat a tight cluster around 0.5 as confirmation of the fixed cutback rule; do not use the old 0.478–0.522 spread.

## 2026-10-04 — FAST C1 next action after B0 PASS

1. Claude B0 review complete: C1 source unchanged; `Iterations=15` retained.
2. Before/alongside B1, verify the full B0 CSV cutback ratio `retry dt / rejected dt` across all rejection pairs. Existing raw excerpts show ~0.5, but full-CSV constancy is still pending.
3. Create a **separate** Workbench project/copy for FAST C1. Do not modify/stop live x6/x7/x8.
4. Install the exact Claude C1 source locally and verify SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`.
5. Preprocess only and run `fast_preprocess_check.py`.
6. Require: golden SDE/parameter equivalence + exactly one intended executable change (`Iterations=15`).
7. Run NtSide=0 C1 first.
8. Compare against Copy x8 using A1'/A1'':
   - accepted steps `(t0,t1,Newton count)` and rejection points `(t0,dt)` should match over the overlap
   - ~4.33 V is the first rejected attempt where Newton count is expected to change 50 -> 15, **not** a trajectory divergence
   - every C1 rejection must report `#iterations larger than 15.`; a 50-cap message means stop
   - I-V / matched-current Vf and available snapshots should match printed precision on the observed overlap; 1e-3 / 1 mV are outer limits
   - wallclock / mV-per-hour in the high-bias bottleneck
9. Do not declare FAST baseline CONFIRMED until numerical/physical equivalence and runtime criteria pass.

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


## Lee Taek Gyu — FAST_C2 geometry/mesh acceleration candidate (2026-10-06)

1. 현재 Node 6/12 full-reference run은 중단하지 않는다.
2. 실제 실행 중인 SDE source를 확보하여 reflect 사용 여부, centerline 좌표, contacts, trap 적용 sidewall, refinement windows를 확인한다.
3. 좌우 대칭이 확인되면 별도 FAST_C2 branch에서 half-domain을 구성한다.
4. 5 nm sidewall damage, active/heterointerface/junction, depletion/high-field 및 relevant contact edge는 fine mesh를 유지한다.
5. 이 영역에서 충분히 떨어진 homogeneous bulk만 단계적으로 coarsen한다. abrupt mesh jump는 피한다.
6. short benchmark에서 full/fine vs half/selective mesh의 element/point count, wallclock/step, I-V/current normalization, SRH/radiative/carrier/field spatial metrics를 동일 bias/physics로 비교한다.
7. equivalence를 확인하기 전에는 Common Baseline final mesh로 교체하지 않는다.


## Project B — half-domain/selective mesh constraint (2026-10-06)

- symmetric AlBarrier_L/R 구조가 유지되면 B에도 half-domain 적용 가능.
- 계산 영역 가운데 mesh를 없애지 말고, remote homogeneous bulk만 coarsen.
- B 전용 fine zones: GaN/AlGaN lateral interfaces, MQW stack, sidewall 5 nm damage, barrier/MQW corner, high-field/contact edges.
- center MQW는 radiative recombination/current crowding 평가 때문에 fine/adequate resolution 유지.
- full/fine reference 대비 lateral Ec/Ev, I-V, SRH, Rrad, Jmax/Javg equivalence 검증 필수.


## Baseline half-domain validation path (2026-10-06)

1. Physical baseline definition remains W_mesa = 4.0 µm.
2. Recover actual running SDE source and confirm mirror symmetry of geometry, doping, contacts, sidewall traps, BCs, and reflect/centerline handling.
3. Build a separate half-domain candidate representing 2.0 µm of the 4.0 µm physical mesa.
4. First keep mesh philosophy as close as possible to the full reference; validate symmetry-only change.
5. Then apply selective coarsening only to remote homogeneous bulk.
6. Compare full/fine vs half candidate: I-V/Vf, IQE, integrated SRH/Radiative/Auger, current normalization, e/h density, current density, E-field; Project B additionally lateral Ec/Ev barrier.
7. If equivalent, use the half-domain model as the common production baseline for Baseline/A/B. Keep one full/fine model as publication/reference validation evidence.
