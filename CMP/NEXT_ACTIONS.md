## 2026-10-10 (latest terminal result; exact capture time not given) — FAST_C1 n6 active MinStep/Iterations/RHSMin confirmed (OBSERVED)

- 이택규가 서버의 **실제 전처리 입력** `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1/pp6_des.cmd`에서 `grep -nE 'MinStep|Iterations|RHSMin'` 출력 제공. Line 766 `RHSMin=1e-3`, line 828 `Iterations=500`, line 839 `Iterations=100`, line 856 `MinStep=1e-9`, line 875 `Iterations=15`. Iterations=500/100은 별도 Solve 블록에 있으나 전체 문맥은 이번 grep만으로 직접 확인 불가. Transient BE step Newton 반복은 실제 실패 로그에서 15회 초과 후 cutback.
- FAST_C1 n6의 최종 시도 `Stepsize: 1.2174e-09 s`에 대해 Newton 실패 후 기존 로그 패턴상 0.5× cutback은 `6.087e-10 s`이며, 이는 확인된 `MinStep=1e-9 s`보다 작음. 따라서 `Step-size is too small` **수치 종료 조건은 확인됨**. 단 Newton 불안정의 근본 원인이 물성, 메쉬, Mg, 파라미터, 경계 조건 중 무엇인지는 여전히 UNRESOLVED.
- 종료 전 마지막 표기 anode=4.801E+00 V, target 5V 미도달, 2026-10-10 17:39:07 process exit. `n6_des.tdr` 생성됨에도 정상 목표 달성/재시작 checkpoint 아님. 이미 완료된 `JUSUBIN_FAST_HALF_5V_TEST` 별도 소자와 혼동 금지. CAL n2 최신 직접 기록 약 4.142V, 후속 결과 미확인.
- 다음: READ ONLY `sed -n '815,885p' /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1/pp6_des.cmd`로 실제 Solve의 MinStep/Increment/Decrement/Iterations/Goal/Save를 정확히 구분하고, 후보 수정이나 재실행 이전에 전처리 입력과 실패 위치를 점검. 기존 FAST 및 CAL 계산파일 보존. 서버 변경 없음.

## 2026-10-10 (last log time unspecified) — FAST_C1 n6 tiny BE-steps oscillate near 4.801V; final minimum step failure (OBSERVED)

- Worker 이택규 supplied filtered **actual** `GaN_PiN_Diode_FAST_C1/n6_des.log` tail. Pseudo-time printed `0.960247 s` on successive BE attempts (6 decimal digits only), corresponding to ~4.801235 V at unchanged 0→5V ramp. Last repeated anode printed `4.801E+00V`, not proof exact zero time advancement.
- Seen rejected timestep trials: `9.0176e-08, 4.5088e-08, 2.2544e-08` s; some intervening **accepted** attempts printed with anode current (e.g. following `1.1272e-08, 6.7632e-09, 1.0145e-09` s). Newton alternated failures and very small accepted progress. Last rejected attempt `1.2174e-09 s` immediately followed by `Step-size is too small.`
- If the previously documented `MinStep=1e-9 s` is indeed active in **this actual pp6 deck**, next 0.5× cutback = `6.087e-10s`, explaining stopping threshold. This must be verified against `GaN_PiN_Diode_FAST_C1/pp6_des.cmd` (not yet shown).
- Earlier detailed n6 Newton tail alternated electron C-norm errors ~0.966 and ~74.4 at adjacent x=0.119–0.120um, y=2.617188um; Poisson and hole errors small there. **Electron-equation instability seen, underlying physics/material/mesh root cause unproven**; cannot blame Mg/traps without regional/model checks.
- Prior process end: 2026-10-10 17:39:07 KST after 525152.85s wallclock, n6_des.tdr written at failure. No successful 5V. Last 4.801V/5V≈96.02% *voltage* sweep only.
- CAL n2 separate: latest direct observed ~4.142 V accepted, 5V/100ns override unresolved; no new CAL evidence in this turn. Preserve active CAL and prior completed 5V_TEST parent.
- NEXT READ-ONLY: inspect exact preprocessed FAST_C1 pp6 `MinStep`, `Iterations`, `RHSMin`, and solving block; save logs/tdr; do not merely lower MinStep, rerun 145h or claim saved TDR is restart checkpoint. No school-server changes.

## 2026-10-10 (after ~19:02 KST, exact capture time unknown) — FAST_C1 n6 last printed V 4.801, MinStep failure before 5V (OBSERVED)

- 작업자 이택규 제공 `grep -n 'anode ' /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1/n6_des.log | tail -n 5` 실제 로그: lines 239133, 239222, 239344, 239400, 239532 모두 `anode 4.801E+00`, electron 4.594E-14, hole 5.318E-12, total 5.364E-12 (raw SDevice output units). 로그는 3-decimal V이므로 마지막 다섯 로그 행의 정확한 t/V 동일성은 미증명.
- 앞서 캡처한 동일 n6 전체 종료 로그: 15 Newton iterations exceeded → `Newton didn't converge, trying again with smaller timestep` → `Step-size is too small` → wrote n6_des.tdr, process exited 2026-10-10 17:39:07, wallclock=525152.85s. `simulation finished / Good Bye`는 성공 의미 아님.
- 마지막 **표시 전압** 4.801V / 목표 5V = 96.02% of sweep, 0.199V remaining; NOT runtime completion, and last exact accepted BE step/time, checkpoint validity and fundamental divergence cause unresolved. No confirmed 5V in this FAST_C1 node. Do not infer 4.801 V is exact last converged to >3 decimals from grep alone.
- Separate CAL n2 latest user log ~4.142V accepted; no new CAL observation in this turn. Completed JUSUBIN_FAST_HALF_5V_TEST parent preserved.
- NEXT READ ONLY: `grep -E 'Computing BE-step|Finished, because|Step-size is too small|Newton didn.t converge|anode ' /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1/n6_des.log | tail -n 35` to see last BE transitions/timestep/rejections/accepted contact; optional `n6_des.sta`. Preserve current TDR/log, do not rerun nor change MinStep/iterations yet. Current chat made no simulator changes.

## 2026-10-10 — FAST_C1 min-step failure and CAL slow accepted steps (NEXT READ-ONLY)

- 작업자 이택규가 학교 서버 실제 터미널 로그 두 개 제공. FAST_C1 `GaN_PiN_Diode_FAST_C1/n6_des.log` (NtSide=0)는 반복 Newton 15회 초과 후 `Newton didn't converge, trying again with smaller timestep...` 그리고 `Finished, because... Step-size is too small.`가 나타남. 2026-10-10 17:39:07 KST 정상 프로그램 종료 메시지 `simulation finished`, `Good Bye !`, `n6_des.tdr` 쓰기 및 라이선스 반환이 있더라도 5V 목표 달성/물리적 성공이 아니라 **수치적 최소 time-step 실패**. Wallclock 525152.85s ≈145h52m32s, peak mem 5.94GB. 마지막 accepted voltage는 제공된 50줄에 없어 UNRESOLVED; 깊은 원인(물성/mesh/수치 설정) 역시 확정 불가.
- 별개 프로젝트 `CMP_BASELINE_1.2.0_CAL/n2_des.log`에서 t=0.828339→0.828343s BE step은 Newton 2회 후 `|RHS| less than 1e-3`로 accepted, 표기 anode=4.142E+00 V, total current=4.678E-14 raw. 기존 4.138V보다 약 0.004V 진전(4.142/5≈82.84% 전압 구간이지 walltime 아님). 후속 t=0.828343→0.828348s attempt은 Iteration 11까지 `RHS≈1.09e-03 >1e-03`; 스크린샷/로그가 중간에 끝나 아직 accepted/failure 미확인. 5V 완료·tau_max=100ns 실제 유효성·ETA 미확인.
- 변경: GitHub 진단 기록뿐. 학교 서버 소스, SWB, 실행 중 CAL, 완료된 `JUSUBIN_FAST_HALF_5V_TEST` 결과는 건드리지 않음.
- NEXT READ-ONLY: `grep -n 'anode ' /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1/n6_des.log | tail -n 5` 로 FAST 마지막 성공 전압을 확인하고 n6_des.sta/err 및 버전 비교. CAL은 시간 경과 뒤 tail로 accepted t/V, `Newton didn't converge`, step-size, fatal/Good Bye 여부 확인. FAST n6 즉시 재실행 또는 MinStep/Iterations 임의 완화 금지.

## 2026-10-10 ~19:02 KST — 이택규 FAST_C1 n6 / CAL n2 로그 분리 진단 (READ ONLY)

1. 학교 서버에서 `tail -n 50 /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1/n6_des.log`를 확인하고, failed 원인 판단이 부족하면 `n6_des.err`, `n6_des.sta`, SWB node output/exit status 확인. '빨강=failed' UI와 실제 solver fatal cause는 구분.
2. 별도로 `tail -n 50 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.log`로 accepted t/V, cutback, job exit, Good Bye 확인. CAL status는 별도 프로젝트를 선택해 확인.
3. 로그 확보 전 두 프로젝트에서 Abort/Run/Reset/Preprocess/입력 수정 금지. 완료된 5V_TEST 기준 결과와 현재 실행 기록 보존. 이후 원인에 맞춰 하나씩 조치.

## 2026-10-10 ~18:08 KST — 주수빈 CAL n2 high-bias cutback 추적 (OBSERVED)

- 4.138V 부근 BE attempt에서 Newton 15회 후 RHS=1.21e-3>1e-3, `Newton didn't converge` 및 step cutback 확인. 새 시도 t=0.827672→0.827674 s, dt=2.8452e-6 s 시작만 확인; 전체 job failure 아님.
- PRIORITY: running source/solver/job 보존. 일정 시간 간격으로 `tail -n 40 .../CMP_BASELINE_1.2.0_CAL/n2_des.log` 비교하고 accepted t/V가 늘어나는지, reject 반복/MinStep/fatal/Good Bye 여부 확인. 출력 timestamp 및 process로 실행/정지 구분.
- 전압 82.8%가 곧 wallclock 82.8%라는 해석 금지. ETA 단정 금지, 100ns effective 적용 아직 입증 안 됨.

## 2026-10-10 ~18:07 KST — 주수빈 CAL 4.138 V 진행 인수인계 (OBSERVED)

- 최신 SWB n2 Output 화면에서 직전 accepted step 결과 anode 4.138 V(5 V 대비 전압 스윕 약 82.76%) 및 다음 BE attempt t=0.82766→0.827663 s 시작 확인. 5 V 완료 또는 다음 시도의 수렴은 미확인.
- 최우선: 진행 중 소자/설정 손대지 말고 `tail -n 40 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.log`를 나중에 다시 확인해 accepted V·retry·fatal/Good Bye 및 종료 여부 기록.
- CAL 종료 후만: 100ns InGaN override 실제 적용증거 검증, 기준 1ns와 같은 조건 I(V)/QW SRH/Rrad/Auger 비교; 원본 및 CAL 소스 보존. 전압 진행률로 ETA 산출 금지.

## 2026-10-10 — 이택규 CAL SDevice log confirms 4.122V (OBSERVED)

- Live CAL `n2_des.log`: accepted BE step to t=0.824478s, V=4.122V, Newton RHS=7.30e-4 under threshold 1e-3, raw anode current 4.344e-14. Next BE attempt t=0.824487s only observed through iteration 5 (RHS=1.10e-3), not yet confirmed accepted. No 5V completion or actual InGaN 100ns model proof.
- Next: keep run intact; compare later log tail for progress/cutback; inspect parameter loading read-only. Do not infer remaining wallclock from ~82.45% voltage sweep.

## 2026-10-10 12:09 KST — CAL SDevice continues running in SWB (USER-REPORTED / LOG UNVERIFIED)

- Worker 이택규 reports that the previously launched `CMP_BASELINE_1.2.0_CAL` SDevice still appears **running** in SWB at ~12:09 KST on Oct 10, with no completion observed.
- Start time described as "어제 새벽 1~2시" (literally Oct 9 01:00–02:00), which would imply 34h09m–35h09m elapsed, but the same CAL project's SDE meshing was previously screenshot-confirmed completed **Oct 10 00:11:50 KST**. A **different interpretation of the date** (Oct 10 01:00–02:00) implies 10h09m–11h09m; therefore actual start date/time is **UNRESOLVED**, and must not be treated as known.
- **SWB running display is user-reported only**; there is no freshly supplied CAL `n2_des.log` or `n2_des.out`, no observed accepted BE steps/current voltage, no proof the 100ns material override was applied, and no reliable ETA. Do not call this a hang or success.
- Immediate next action **READ ONLY**: inspect `tail -n 40 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.log` and the SWB job/experiment identity and start timestamp; compare changing accepted-voltage/current and Newton retry patterns. Keep existing run and original completed 5V parent intact; no parameter/source edits while it is running.

## 2026-10-10 — User priority: run current CAL first; defer native SWB parameter portability

- Decision by 이택규: **do not change** current CAL `Parameters="FASTC1_pp6_des.par"` to `@parameter@` yet. Perform this migration in the next new device/project for professor-facing copy/paste reproducibility. Keep already saved cloned InGaN Scharfetter 100ns custom .par.
- Immediate execute gate: in `CMP_BASELINE_1.2.0_CAL` single NtSide0 SWB experiment, run SDE to build mesh first (clone currently showed -- for tools); inspect SDE mesh/geometry success. Preprocess SDEVICE and confirm correct custom .par / InGaN lifetime override. Then run existing successful-style 0–5V Transient-BE (not failed QS), monitor convergence and verify actual log model coefficients. Existing 5V clone source is a FULL run, not a short smoke. No CAL run confirmed yet.
- Next model versions may use standard SWB SDEVICE `sdevice.par` and `@parameter@` after checking its contents. Keep current completed parent and results unchanged, check very low 2D current/J & QW recombination, eventually same-current sidewall/Full-Half validation.

## 2026-10-10 — CAL parameter integration into standard SWB editors (PROPOSED)

- For professor copy/paste reproducibility, migrate CAL cloned custom par into native `sdevice.par`, and cloned SDEVICE File entry to `Parameters="@parameter@"` only after inspecting any existing sdevice.par contents.
- Keep all custom GaN Mg, Thermionic, lattice and InGaN SRH blocks. Verify SWB preprocess ppN_des.par and effective models before short smoke; leave finished 5V parent untouched.
- Presentation handoff must contain SDE, SDEVICE, parameter inputs plus NtSide run conditions. Nothing migrated yet.

## 2026-10-10 — Separate CAL candidate ZIP created; next SWB clone and smoke (ACTIVE)

1. Download locally prepared private `CMP_BASELINE_1.2.0_CAL_INPUT_CANDIDATE.zip` via chat (only source + README; not on public GitHub). Static checked: SDE bytes identical to 5V_TEST parent; executable SDevice lines identical; GaN Mg/Lattice/Thermionic preserved; material InGaN Scharfetter tau_max electrons/holes changed to literature sensitivity 100ns. This zip is NOT an SWB importable project and is NOT Sentaurus-tested.
2. On user's workstation/SWB, use `Project > Save As > Clean Project` from completed `JUSUBIN_FAST_HALF_5V_TEST` to new `CMP_BASELINE_1.2.0_CAL`. This retains source and tool flow without copying old node outputs; preserve original project. Confirm location and tool flow.
3. Replace ONLY the new project's named `sde_dvs.cmd`, `sdevice_des.cmd`, `FASTC1_pp6_des.par` from ZIP. Check names, path, Fermi/Thermionic/Piezoelectric, NtSide=0 and param reference, SDE mesh. Do not generate `sdevice.par` from Silicon template and do not modify system MaterialDB.
4. Preprocess and audit pp deck; verify model parameter inheritance/actual changed InGaN Scharfetter logged. Make separate 0-0.3V Transient-BE smoke input from copied SDevice, since ZIP's actual Solve Goal=5.0V. Do not launch full 5V until smoke passes.
5. Then NtSide0 5V exploratory CAL sensitivity run, extract same-bias and eventually same-current charge/radiative/SRH/Auger/J; matched-condition NtSide1e18 follow-up only after its preprocess gate. Add validated intermediate spatial snapshots when going beyond the initial control.
6. Full/Half+coarse error, material realism, low J/injection, 5V steady status remain publication gates.

## 2026-10-10 — Actual 5V parent archive audit complete; CAL next experiment gate (ACTIVE)

- New detailed evidence: `CMP/reviews/BASELINE_1_2_0_CAL_AUDIT_20261010.md`. 5V parent HDF5 shows effective InGaN recombination B=2e-10 cm3/s, Auger=1e-30 cm6/s, SRH tau=1ns, exactly; Mg incomplete ionization valid in DopingConcentration via occupation factor. Raw terminal J/Areal normalization, steady-state, Full/Half/mesh and physical calibration remain unresolved.
- **FIRST read-only:** inspect local Sentaurus T-2022.03 MaterialDB `InGaN.par` recombination section and official SDevice material-specific parameter override syntax; preserve FASTC1 custom GaN Mg + lattice/thermionic definitions. Verify whether to override both Clean/DmgL InGaN regions in .par. Do not improvise syntax or mutate vendor MaterialDB.
- Then prepare *separate* `CMP_BASELINE_1.2.0_CAL` branch, isolate SRH lifetime sensitivity (100ns vs old 1ns as literature candidate, not physical fit), hold geometry/doping/polarization/Radiative/Auger/numerics and NtSide0, perform preprocess+short Transient BE smoke, then 5V run only on PASS. Check source/header discrepancy: old header falsely claims staged increments and 4/4.5/4.8/5V Saves, whereas executed deck had single Increment1.2 ramp and only final Save. Add validated within-sweep TDR snapshots/Save as needed for matched-current extraction.
- Finally make NtSide1e18 comparison at matched injected current, check current/J scaling and full/half numerical equivalence. No full A/B production before gates.

## 2026-10-09 — Naming policy confirmed; use CMP_BASELINE_1.2.0_CAL (ACTIVE)

- Naming standard: `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>`; `CMP/PROJECT_NAMING_CONVENTION.md`. Supersedes the earlier proposed `CMP_BASELINE_CAL_V1` candidate label; no SWB project renamed or created yet.
- All nine required private 5V_TEST files confirmed present by user `ls -lh`; next user action is to archive/share those actual files privately for code review (do not upload vendor source to public GitHub).
- Inspect effective InGaN recombination parameters, 2D current/AreaFactor/injection and physics before a new parameter-only branch; run short smoke before NtSide0/1e18 5V comparisons. Preserve Full/Half verification requirement and completed reference outputs.

## 2026-10-09 — CMP_BASELINE_CAL_V1 near-final candidate preparation (이택규, PROPOSED)

1. Do not delete or move the pre5V archive; user elected to retain it where it is. Preserve completed `JUSUBIN_FAST_HALF_5V_TEST` and full/fine FAST_C1 references.
2. Obtain the actual `JUSUBIN_FAST_HALF_5V_TEST` private SDE/SDevice input, effective parameter files, preprocessed decks, completed `n2_des.log` and mesh using a private chat attachment (do not upload vendor decks to public GitHub). Verify filenames/existence before archiving.
3. Read exact active physics/material mixing; verify effective InGaN SRH/Radiative/Auger parameters, current/AreaFactor convention, injection/QW carrier balance and 5V state. Continue MgMinus interpretation as an unresolved issue, not automatic proof of model failure.
4. Design `CMP_BASELINE_CAL_V1` as a distinct branch, keeping the known 5V-convergent Half+Coarse geometry, existing Mg/EBL/nGaN and trap-off references; propose only evidence-backed minimum recombination/injection-related changes. Literature sensitivity results are not experimental calibration.
5. Perform preprocess and short Transient-BE NtSide0 smoke, inspect current/recombination/numerical behavior, then run to 5V if passed. Repeat NtSide1e18 with identical calibrated physics and current conditions after trap-ON gate, maintaining same-current comparisons.
6. Before publication-grade freeze, verify Full/Half+Coarse and mesh-convergence errors, 2D current normalization, extraction robustness and steady-state adequacy. Broad Project A/B production remains NO-GO until additional gates pass.

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


## 2026-10-09 11:30 KST priority
1. Verify completed `JUSUBIN_FAST_HALF_SWB` terminal/log evidence: final 0.3 V, normal completion, no fatal/error, output files.
2. Extract total wallclock/runtime and I-V points from the completed half+coarse transient.
3. Check the `JUSUBIN_FAST_HALF_SWB_Copy` QS smoke status/result separately.
4. Compare Half+coarse transient vs QS Copy, then against full FAST_C1 reference before adopting the fast branch for production A/B.


## 2026-10-09 — QS Copy failed sweep verification first
1. In `JUSUBIN_FAST_HALF_SWB_Copy`, inspect `tail -n 20 n2_des.plt` to establish LAST accepted anode voltage; note goal 0.3V remains UNVERIFIED after MinStep stop.
2. Inspect `grep -nE 'Step-size less|Computing step from|Finished, because' n2_des.log | tail -n 15` and QS `.err` for step cutbacks, Newton failures and underlying cause.
3. Do not infer speedup from QS 5:06:57 vs original transient 6:56:59: QS did not complete a comparable 0.3V curve.
4. Preserve Common Baseline, original transient result and QS Copy, and avoid unverified solver edits.


## 2026-10-09 — QS Copy last accepted bias determined
- 작업자: 이택규. OBSERVED from user-provided `JUSUBIN_FAST_HALF_SWB_Copy/n2_des.plt` tail and `n2_des.log` grep.
- Last recorded QS pseudo-time: 6.43487876313307E-02; last anode OuterVoltage: 1.93046362893992E-02 V (0.0193046363 V; 19.3 mV, only ~6.435% of requested 0.3 V).
- Last log attempts at t=0.0643488 to 0.0643505 then terminated `Step-size less than MinStep (step-size = 8.3986e-07)`.
- QS runtime 18417.09 s but did NOT reach goal. Cannot compare as speedup to original transient that reached 0.3 V in 25019.43 s.
- Root numerical/physics trigger not yet established. Next: inspect QS log around lines 6900-7000 and `n2_des.err`; no blind MinStep or baseline modification.


## 2026-10-09 — Next gate after QS Newton diagnostic
- QS Copy: confirmed Newton failure after 15 iterations and repeated step reduction near 19.3 mV, stopping at MinStep. Do not change common physics/mesh or rerun without numerical cause review.
- Inspect actual QS `pp2_des.cmd` Math / Solve (`RHSMin`, `Digits`, `NotDamped`, `LineSearchDamping`, `Extrapolate`, `Coupled`, QS step settings) and original transient deck for controlled diff.
- Decide whether to prioritize original successful transient reference and higher-bias/physics checks versus separate numerical-only QS solver sensitivity pilot. No speedup claim allowed.


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


## 2026-10-09 — Original half smoke source/mesh files confirmed, 5V copy proposed
- 작업자: 이택규. User shell `ls -lh` verified in `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_SWB`: `sdevice_des.cmd` 5.9K (Oct 8 18:36), `sde_dvs.cmd` 20K (Oct 8 17:48), `pp2_des.cmd` 5.8K (Oct 8 18:44), `n1_msh.tdr` 1.6M (Oct 8 18:08). `du -sh .` = 23M.
- OBSERVED only: these four files exist. Content/provenance and suitability for high-bias 5V have not yet been fully reviewed. Background SVisual job reported Done (no simulation failure implied).
- PROPOSED (not yet executed by user): safely copy directory with guard to `JUSUBIN_FAST_HALF_5V_TEST`, check copied SDevice source with `cmp`; next verify actual SWB project association before changing any deck or launching.
- Do not assume filesystem copy automatically creates an independently recognized SWB project; original full reference and 0.3V smoke remain protected. Never blindly replace Goal without checking FinalTime/step controls and high-bias stability.


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


## 2026-10-09 — 5V_TEST backup archive validated; SDevice launch now permitted
- 작업자: 이택규; 상태: CONFIRMED archive readability from user terminal.
- At `JUSUBIN_FAST_HALF_5V_TEST`, command `tar -tzf ../JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz > /dev/null` completed; C-shell `echo $status` returned `0`.
- Together with prior `ls` (12M archive present), this verifies archive tar listing/readability but not an independently completed restore test. Original `JUSUBIN_FAST_HALF_SWB` and QS Copy are preserved.
- Prior pp2 preflight checked Transient FinalTime 1.0, anode Goal 5.0V, `Grid=n1_msh.tdr`, NtSide=0 `Conc=0` replacements, RHSMin=1e-3, sweep Coupled Iterations=15.
- Next permitted action: in SWB `JUSUBIN_FAST_HALF_5V_TEST`, run SDevice Node2 ONLY (F7), not SDE. User has NOT yet provided evidence that 5V job was launched. Ask for Node2 View Output once started; confirm fresh log versus inherited Oct9 01:39 copied 0.3V outputs, monitor nonlinear convergence and bias progression. 5V success/high-bias physics/IQE validation remain unverified.


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


## 2026-10-09 16:40 KST — 5V SDevice runtime estimate (INFERENCE; not a measured 5V duration)
- 이택규 asked expected completion time for running `JUSUBIN_FAST_HALF_5V_TEST` 5V Transient, SWB Node2 launched at 11:33:14 on Oct9.
- Earlier 0.3V smoke: FinalTime=0.06, MaxStep=1e-3, actual wallclock 25019.43s (6h56m59s). Copied 5V test: FinalTime=1.0, same MaxStep=1e-3; the ratio of minimum accepted steps is about 16.7x (60 -> 1000). Pure linear extrapolation yields ~116h = ~4.8-4.9 days, **NOT** a confirmed or reliable ETA. Offered rough multi-day planning range 3–7+ days with possibility of early convergence failure, and higher runtime given nonlinearity and concurrent pp6/pp12.
- At 16:40 KST about 5h07m elapsed since SWB launch. Current actual 5V solver progress and ongoing job liveness UNVERIFIED; must inspect `tail -n 30 n2_des.log` in copied test before updating ETA, and confirm fresh log timestamp/current voltage. Do not invent completion date or claim guaranteed success.


## 2026-10-09 — Concept-study focus: Baseline qualification and Project A Carbon implementation
- 작업자: 이택규; USER says hands-on TCAD temporarily unavailable and requests conceptual study. Existing 5V_TEST SWB Node2 launch was observed earlier, but no new log/process evidence of current progress; do NOT assume run stopped or completed.
- CONFIRMED from CMP/PROJECT_AB_PRE_RUN_AUDIT.md and JuSubin/TIMELINE.md: 5V arrival alone is NOT a publication-ready Common Baseline. Half+coarse NtSide=0 is trap-off control; final validation requires consistent NtSide=1e18 nominal damaged reference, full-vs-half mesh/geometry and convergence checks, unbiased same-current I/Vf, MQW Rrad/RSRH/RAuger, integrated sidewall SRH and IQE/injection/current-crowding, and 2D current normalization. Common baseline parent FAST_C1 usable candidate, Project A/B production still NO-GO until gates.
- Project A 1st-stage TCAD is NOT carbon implantation process simulation. Geometry defines GaN `Cedge_L/R` immediately inside preexisting 5nm Dmg_L/R region, first test upper n-GaN under MQW; SDevice implements distinct C-related deep acceptor/trap/compensation physics (nominal literature anchor C_N approx Ev+0.9eV with variable capture cross sections), donor/compensation slot, explicit GaN region boundary meshing, A-null carbon-off control. Half domain retains one physical sidewall and one center symmetry boundary, not two Cedge regions in half representation.
- Carbon ion implantation is a possible physical fabrication option BUT not decided as exact process route and requires separate depth/lateral profile, implantation damage/activation/recovery study; don't call current Stage1 model simulated implantation or proven fabrication. Hypothesis is steering current away from sidewall to reduce SRH and improve IQE; may also increase Vf/reduce injection, not demonstrated.
- NEXT while user studies: explain C incorporation vs ion implantation and electrically compensated semi-insulating GaN:C, distinguish A mechanism-screen from future SProcess/process-realistic study; no TCAD changes requested. Once TCAD accessible review actual 5V_TEST log and baseline comparator, not rerun/cancel based on conversational assumption.


## 2026-10-09 — Project A carbon location vs existing MQW edge traps clarified
- 작업자: 이택규; user concept question: Is C placed near n-GaN rather than MQW, and did MQW have traps?
- VERIFIED from `CMP/PROJECT_AB_PRE_RUN_AUDIT.md` §4 and JuSubin TIMELINE: Stage1 Project A Cedge region is localized GaN immediately inside preexisting 5 nm physical sidewall damage, first proposed in *upper n-GaN just below MQW* (not carbon implanted in entire MQW or across full n-GaN). It is a hypothesis/parameterized model, not an executed C-device result. In half-domain one retained physical sidewall Cedge only; symmetry center has no damage.
- VERIFIED baseline trap geometry: preprocessed half-domain has 12 DmgL regions (pGaN, EBL, Barrier0–4, QW1–4, nGaN); each is sidewall-damage region with acceptor trap parameterized by `@NtSide@`. Thus yes, QW1–4 have sidewall-edge trap definitions, but not distributed through the pristine central MQWs. `NtSide=0` means declared trap concentration 0 (5V_TEST branch); nominal `NtSide=1e18 cm^-3` activates damage traps, to be validated with proper same-source test.
- IMPORTANT physics distinction: Carbon C-related deep acceptor/compensation in Cedge is NOT the existing sidewall Dmg trap. Baseline Dmg trap nominal Et=Ev+0.75eV, e/h sigma=1e-15cm2; proposed C_N literature anchor near Ev+0.9eV is independent and must not be substituted as same species without model justification. Project A causal hypothesis is current steering to lower sidewall SRH, not yet proven; C-off null, trap-on damage case and matched-current IQE metrics required.
- No TCAD code changes, no new solver/output progress evidenced. Existing 5V_TEST startup remains last live evidence.

## 2026-10-09 — After confirmed Half+Coarse 5V_TEST completion (이택규)

1. **Do not rerun or cleanup** the finished `JUSUBIN_FAST_HALF_5V_TEST` Node2; preserve `n2_des.log`, `n2_des.plt`, `n2_des.tdr`, and both `n2_5V_ckpt*.sav` files. Keep unrelated pp6/pp12 runs unchanged.
2. First non-destructive check: verify `ls -lh n2_des.plt n2_des.tdr n2_5V_ckpt_des.sav n2_5V_ckpt_circuit_des.sav`, then inspect full voltage/current curves; do **not** interpret `1.448E-11` as A or J without verifying 2D units and AreaFactor.
3. Validate output physics: MQW radiative/SRH/Auger recombination, integrated IQE components, carrier distribution, contact e/h/displacement current, operating-current plausibility; check actual `pp2_des.cmd/par` and fields.
4. Compare half/coarse `NtSide=0` with original full/fine same-trap pristine reference at matched bias/current, with symmetry ×2 handling and mesh-convergence gates; investigate why measured 5V runtime 10596.76 s differs sharply from older 0.3V smoke 25019.43 s before claiming acceleration/equivalence.
5. Next separate **nominal damage** `NtSide=1e18` branch with exact physics/source verification and short preprocess/solver gates; compare same-current I(V), sidewall SRH, MQW recombination and IQE. Project A/B production remains blocked until pre-run audit gates pass.

Evidence: user-provided Oct9 completed `n2_des.log` (anode 5.000E+00; Curve trace finished; final TDR/checkpoints saved; normal completion at 14:29:52 KST). Previous instruction to simply check if Node2 is running has been superseded.

## 2026-10-09 — Next diagnostic after verified 5V file listing (이택규)

1. In copied `JUSUBIN_FAST_HALF_5V_TEST`, preserve all `n2_*` output and checkpoint files. No re-run or cleanup.
2. Read-only parse of `n2_des.plt` 17 datasets: count complete rows, first/last anode OuterVoltage and TotalCurrent, full 0–5V curve and numerical trends. File timestamp confirms write near successful finish but full data content is unparsed.
3. Investigate missing `pp2_des.par`: in `pp2_des.cmd`, inspect preprocessed File/Parameters linkage; list actual `*.par`. `grep AreaFactor` produced no `pp2_des.cmd` match; 2D current and mesa-width normalization remain NOT CONFIRMED.
4. After IV/units sanity gate, check `n2_des.tdr` radiative/SRH/Auger fields and integrate QW, then compare full/fine vs half/coarse NtSide=0 at same current and initiate controlled nominal damaged NtSide=1e18 branch. Publication-grade A/B remains NO-GO.

Evidence: user-provided Oct9 `ls -lh --full-time`, `head -n 30 n2_des.plt`, `grep -ni 'AreaFactor' pp2_des.cmd pp2_des.par`.

## 2026-10-09 — After 1023-point Half 5V I–V output (LeeTaekGyu)

1. Preserve `JUSUBIN_FAST_HALF_5V_TEST` final PLT/TDR/checkpoint. Parsed 1023 complete 17-column DF-ISE rows, V=0 to 5V, final raw anode TotalCurrent 1.44801646079583E-11; sample shows rise after ~4V. Do not infer absolute ampere/current density or normal LED behavior yet.
2. Actual `pp2_des.cmd` Parameters target is `FASTC1_pp6_des.par` and that file exists. Read full contents plus active Physics/Plot blocks and all AreaFactor references; investigate whether radiative recombination coefficient is nonzero for GaN/InGaN and output plots have required field data.
3. Resolve effective 2D depth/mesa width and contact vs carrier/displacement current; compare physical injection/recombination and full/fine pristine counterpart at matched V/J; follow G1–G5 of `PROJECT_AB_PRE_RUN_AUDIT.md`.
4. Only after current/physics/mesh checks, test separate nominal NtSide=1e18 damage reference then freeze common baseline. A/B production remains NO-GO.

Evidence: user Oct9 awk output and `sed -n '1,65p' pp2_des.cmd` plus `find . -maxdepth 1 -type f -name '*.par'`.

## 2026-10-09 — Next after 5V Anode currents and recombination declarations (LeeTaekGyu)

1. Preserve all `JUSUBIN_FAST_HALF_5V_TEST` files/checkpoints. Last PLT record: time=1.0 V=5.0; raw anode I_disp=3.29132361382365E-18, I_e=2.78143237811134E-13, I_h=1.42020180788235E-11, I_total=1.44801646079583E-11. Displacement minor, hole-dominated **at anode**; MQW injection still unverified.
2. Global Physics includes SRH/Auger/Radiative and Plot lists associated fields. `FASTC1_pp6_des.par` has Mg ionization, Thermionic, lattice but no explicit Radiative coefficient. Confirm effective GaN/InGaN radiative material parameters via actual SDevice log/material database or official T-2022.03 docs; a field declared in Plot does not prove emission.
3. Inspect final `n2_des.tdr` directly in SVisual: look for positive, physically located `RadiativeRecombination` in each clean InGaN QW; validate units, SRH/Auger/density, regional integration; separate LED luminescence from electrical I-V. Do not claim valid IQE until rates integrated/physical checks pass.
4. Resolve 2D current units, effective AreaFactor, and appropriate full-mesa vs half-domain normalization before absolute J and matched-current comparison. Then nominal NtSide=1e18 baseline separate controlled branch; A/B production still NO-GO.

Evidence: user's last-row DF-ISE awk and `cat FASTC1_pp6_des.par`, grep of executable `pp2_des.cmd`.

## 2026-10-09 — Immediate QW-location gate after 5V SVisual Radiative map

1. OBSERVED on `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`: `RadiativeRecombination` scalar colorbar max=7.483e19 and min≈-7.512e-34 cm^-3 s^-1, top thin layers colored and lower bulk near zero. This proves nonzero values exist in spatial output **somewhere**; not yet tied to any named InGaN Clean_QW region.
2. SVisual GUI next (no computation change): keep scalar checked; use Data Selection `Regions` to locate `Clean_QW1`–`Clean_QW4`, zoom the upper active stack, and Probe one or more points per clean QW with region and full Radiative field label visible. Screenshot for reproducible source evidence.
3. Subsequently compare SRHRecombination/AugerRecombination and carrier densities and integrate per-QW regions; confirm optical radiative coefficient source and full/half current normalization before quoting IQE or electroluminescence. Maintain NtSide=0 pristine status; A/B NO-GO.

## 2026-10-09 — After four 5V InGaN QW positive Rrad Probes (이택규)

1. User SVisual Probes **OBSERVED** `Clean_QW1=1.836010164996e13`, `Clean_QW2=3.558921779790e12`, `Clean_QW3=8.395713573050e14`, `Clean_QW4=7.094266327897e18` cm^-3 s^-1, each one *local point* (not per-well integrated or average) with corresponding x/y logged in LeeTaekGyu timeline.
2. First next GUI test (read-only): switch SVisual scalar to `SRHRecombination` and probe `Clean_QW4` at previous x=0.245093340874, y=0.58321731303, then `AugerRecombination` at the same coordinate, preserving the Rrad reference; repeat QW1–QW3 when workflow validated. Beware selection point may shift; verify Probe zone each time.
3. Then integrate Rrad/RSRH/RAuger over each full active QW using validated units/mesh, compute clearly labelled recombination-based `IQE_rec`, and cross-check electrical injection, 2D current/AreaFactor and full-vs-half mesh equivalence. Do not infer IQE from one point or claim QW4 dominates total photon production.
4. Preserve completed NtSide=0 5V_TEST results; nominal damaged NtSide=1e18 baseline and A/B production gates remain pending. No rerun, no file cleanup or code change.

## 2026-10-09 — 5V_TEST local SRH Probe in Clean_QW4 (OBSERVED; not co-located with earlier Rrad)

- 이택규 supplied SVisual Probe screenshot for `n2_des` 5V test: Zone `Clean_QW4(InGaN)`; selected field `srhRecombination`; (x,y,z)=(0.244864017914, 0.599783903626, 0); SRH = `1.681637512936e+22` cm^-3 s^-1 (field units refer to same SVisual recombination output convention).
- The previous QW4 local `RadiativeRecombination=7.094266327897e+18` was probed at (x,y,z)=(0.245093340874, 0.58321731303, 0). They are in the same named region but have **different coordinates**, especially lateral y. It is invalid to form a local loss ratio or IQE from the two values without co-locating them. The high SRH number is a measured point, not evidence of whole-QW dominance.
- NEXT: in SVisual use Probe At or coordinate entry to probe `SRHRecombination` at the exact earlier QW4 Rrad coordinates and verify zone. Then measure Auger at that same point; subsequently validate spatial integrals for IQE. Preserve outputs; no solver/source modifications.

## 2026-10-09 — SVisual Probe At decimal precision limitation and workaround (OBSERVED UI / PROPOSED NEXT)

- 작업자: 이택규 reports SVisual `Probe At...` input accepts only about five decimal places; exact earlier QW4 Radiative coordinate entry is impractical. This is a GUI limitation reported by user, not a solver/data failure. No new physics measurements or code edits.
- Preferred **test**: at existing QW4 probe position uncheck `Show Only Active Field` in Probe panel to see whether `RadiativeRecombination`, `srhRecombination`, and `AugerRecombination` appear at the same Probe point; verify screenshot before claiming UI successfully exposes all fields.
- Fallback: use rounded coordinates (x=0.24509, y=0.58322, z=0) consistently for *new* Radiative, SRH, Auger probes; inspect returned coordinates and zone each time. Cannot reuse prior 12-decimal Radiative value directly with a new rounded-coordinate SRH value as a fully co-located comparison. No IQE from point probes; eventual QW integration still required.

## 2026-10-09 — QW4 co-located radiative/SRH/Auger diagnostic: local nonradiative loss dominant

1. Preserve final 5V_TEST outputs. All co-located at Clean_QW4 x=0.244864017914, y=0.651958341615, z=0: Rrad=7.103015017104e18, SRH=1.681575471039e22, Auger=1.238545872618e15, Total=1.682285896396e22 cm^-3 s^-1. Pointwise Rrad fraction ≈0.0422%: **LOCAL ONLY, NOT DEVICE IQE**.
2. Do not claim caused by sidewall traps: NtSide=0 disables defined damaged-edge traps but SRH() remains active. Inspect spatial QW and Dmg rates, actual lifetime/material physics, electron/hole density and any band/profile artifacts before parameter changes.
3. Determine total and per-QW integrated Rrad/SRH/RAuger via validated SVisual integration, then recombination IQE, V(I), current normalization and half/full equivalence; QW1–QW3 local nonradiative probes may help establish spatial trends. Publication-ready baseline and Project A/B production still pending.
4. Keep copies/reference Node6/12 processes and checkpoints untouched. See LeeTaekGyu/TIMELINE and Issue #7 for evidence.

## 2026-10-09 — Project A fabrication route feasibility questions (PROPOSED; not selected)

- Distinguish as-grown electrically active GaN:C compensation from *implant-damage-based* resistive isolation. Published As/F microLED implantation does NOT prove implanted C_N creates the same trap/compensation physics; old experimental reports show implanted-C electrical activity may be absent or damage dominated.
- Examine two non-final routes against Stage1 Cedge upper-nGaN adjacent to mesa sidewall: (A) post-mesa selective nGaN sidewall C+ angled implantation requiring pGaN/MQW height-selective protection and low-thermal-budget damage handling; (B) pre-MQW patterned upper-nGaN carbon implantation or selective C-doped growth, followed by MQW epitaxy and later mesa alignment. Quantify shadowing, alignment, damage, profile and MQW thermal constraints before adoption.
- Only after a grounded process choice: plan TCAD geometry/profile link (including C straggle, activation fraction and residual damage separately), appropriate mask-off / anneal-only / inert-ion controls, and verification by depth-profile/structural/electrical/optical experiments. Do not alter Common Baseline or launch Stage1 A/B production based on this exploratory discussion.

## 2026-10-09 — SVisual region-integrated IQE gate prioritized over more point probes

1. QW3 point in 5V_TEST: Clean_QW3(InGaN), x=0.219173763524, y=0.555622585194, Rrad=8.333611568957e14, srh=5.390114530106e19, Auger=5.79338765299e8 (per cm3 second). These are single-point diagnostics only.
2. First verified operation: keep final `n2_des.tdr` open; choose RadiativeRecombination; SVisual Tools > Integrate (∫dr), Region/Material tab choose Clean_QW3 only, Full/Complete Domain, Start Integration; screenshot Integral AND Domain units. No code edit, cleanup or rerun.
3. After confirming SVisual's exact 2D output and region selector, integrate `srhRecombination` and `AugerRecombination` in the same QW, then QW1..4 and associated `DmgL_QW*` portions as intended by full-QW physical region definition. Check sign convention and physical current normalization.
4. Compute IQE_rec as sum of *integrals* of Rrad divided by sum of all three types of integrals; local point percentages, averaging local fractions and selecting only pristine Clean wells are not device IQE. Compare NtSide=0 and nominal damaged NtSide=1e18 at matched current after model validation.

## 2026-10-09 — SVisual Field Integration QW region scope clarified (PROPOSED, pending output)

- 이택규 screenshot shows choices `Clean_QW3` and `Clean_QW3+DmgL_QW3` in Field Integration selector. For full physical QW3 recombination accounting in current Half model, select `Clean_QW3+DmgL_QW3` as a single combined group, not both it and `Clean_QW3` (would double count).
- `Clean_QW3` alone excludes the QW3 damaged sidewall; still useful later for separate core-vs-edge attribution. `NtSide=0` deactivates parameterized sidewall traps but the DmgL_QW3 geometric region still exists.
- This is a selection decision, NOT an executed/verified integral. Next capture chosen field `RadiativeRecombination`, selected group, numerical Integral/Domain and actual 2D units; verify group region membership before claiming whole-well total. Repeat same group for SRH/Auger, and other QWs before IQE computation. Keep comparison scope consistent for full/fine and damaged NtSide=1e18 branches.

## 2026-10-09 — Next after Clean_QW3 region integral and ROI '+ label' correction

1. OBSERVED 5V_TEST SVisual `RadiativeRecombination` area integral Clean_QW3 alone = 2.657110e+02 [s^-1 um^-1], domain 5.985012e-03 [um^2]. This is not combined QW3.
2. **Do NOT rely on `Clean_QW3+DmgL_QW3` as a combined 2D volume/area; likely a lower-dimensional interface label.** Locate independent `DmgL_QW3` row in Regions list, select only this, press Start Integration. Verify output lists `DmgL_QW3` under Regions of Dimension 2, capture Integral and Domain. Add independent integrals from Clean_QW3 and DmgL_QW3 after confirming nonoverlap, rather than double-counting or trusting selection highlight.
3. For each QW1..4 integrate exact bulk Clean_QW + separate DmgL_QW (in full model add DmgR_QW), for Rrad, SRH, Auger, then compute IQE_rec from sums of like-normalized integrals. Record SVisual units per um depth; verify 2D thickness and current normalization for physical optical totals.
4. No SDE/SDevice rerun or cleanup. Correct prior log saying '+' item represented combined region; label remains UNRESOLVED pending dimensional confirmation.

## 2026-10-09 — After full QW3 Half-domain Radiative integral (OBSERVED)

1. User verified standalone 2D `DmgL_QW3` Rrad Integral=0.526818 [s^-1 um^-1], domain 0.00001500002 um²; prior standalone `Clean_QW3`=265.711 [s^-1 um^-1], domain 0.005985012 um². **Sum full QW3 half-domain Rrad=266.237818 [s^-1 um^-1]**, area=0.00600001202 um². This is integrated radiative only, not IQE.
2. Next read-only SVisual integration: field `srhRecombination`; integrate both *standalone* `Clean_QW3` and `DmgL_QW3` as two separate 2D regions, confirm each output line and Total Integral/Domain. Same process with `AugerRecombination`.
3. Repeat all three rates for QW1/QW2/QW4 using standalone Clean and DmgL. Compute `IQE_rec = ΣRrad_integral/(ΣRrad+ΣRSRH+ΣRAuger)` from consistent 2D normalized integrals; do NOT average probe ratios. Then validate absolute out-of-plane normalization, NtSide=1e18 and full/fine comparison.
4. Preserve finished Node2 results and original simulations. Avoid selecting plus-named interface instead of 2D Dmg region.

## 2026-10-09 — QW3 5V SRH Dmg edge integral confirmed

- New 2D SVisual `DmgL_QW3` SRH Integral=1.655249e3 [s^-1 um^-1], Domain=1.500002e-05 um²; compare same Dmg region Rrad=0.526818. NtSide=0 trap-off condition, generic SRH() active; no causal attribution. `Clean_QW3` SRH pending.
- **Next**: Field `srhRecombination` standalone `Clean_QW3` and Start Integration; send Region of Dimension 2, Integral, Domain. Then Auger for same standalone Clean and DmgL and sum; verify normalized 2D ratio before broader 4-QW IQE. Keep current data intact.

## 2026-10-09 — QW3 DmgL Auger spatial integral measured (OBSERVED)

- 이택규 supplied direct SVisual Field Integration screenshot for completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des`: `AugerRecombination` `Regions of Dimension 2: DmgL_QW3 (InGaN)`; `Integral=5.774334e-02 [s^-1*um^-1]`, `Domain=1.500002e-05 [um^2]`.
- Prior directly observed same-region 2D Radiative `0.526818`, SRH `1655.249` [s^-1 um^-1] and same Domain. Therefore DmgL_QW3 has all 3 regional integrals and SRH dominates *this segment*. At `NtSide=0`, generic SRH remains active; do NOT attribute to parameterized edge traps or infer full QW/device IQE.
- The earlier request was `Clean_QW3` SRH; user instead measured DmgL_QW3 Auger, which is useful and preserved. Still missing standalone `Clean_QW3` SRH and Auger for full QW3 radiative-vs-nonradiative integration. Clean_QW3 Radiative=265.711 [s^-1 um^-1]. NEXT: switch field `srhRecombination` + select only standalone `Clean_QW3` + Start Integration, screenshot. Then `AugerRecombination` + standalone `Clean_QW3`, repeat. No code edits or rerun.

## 2026-10-09 — QW3 integrated recombination gate completed; next QW1/QW2/QW4

1. OBSERVED via SVisual Clean_QW3 2D Integral SRH=584161.1, Auger=12.65704, Rad=265.711; DmgL_QW3 SRH=1655.249, Auger=0.05774334, Rad=0.526818, units s^-1 um^-1. Full QW3 = Rrad 266.237818, SRH 585816.349, Auger 12.71478334. `IQE_rec,QW3=0.0454256871%` from integrals only, **NOT whole-device IQE**.
2. QW3 SRH Clean region ~99.717% of integrated QW3 SRH even at `NtSide=0`; do not attribute to sidewall traps without physical validation. Audit effective SRH lifetime parameters and radiative materials DB plus carrier profiles.
3. Repeat six 2D region integrals per remaining QW: independently `Clean_QWn` and `DmgL_QWn` for Rrad/SRH/Auger, check right pane `Regions of Dimension 2` and physical domains. Avoid plus-named interfaces. After four wells, calculate device recombination-based `IQE_rec` as `ΣRrad/(ΣRrad+ΣRSRH+ΣRAuger)`; compare same-current damaged NtSide=1e18 and full/fine after pre-run gates.
4. Keep completed `JUSUBIN_FAST_HALF_5V_TEST` result files/checkpoints and existing reference jobs unchanged. No numerical/physical-source edits until validation.

## 2026-10-09 — Immediate model plausibility audit after QW3 0.0454% radiative fraction

1. **Before labeling LED nonphysical or modifying parameters**: inspect LIVE active `JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd` Physics, region traps, solve sections, `FASTC1_pp6_des.par` (seen no explicit radiative coefficients/lifetime), and `n2_des.log` for effective radiative/SRH lifetime/material DB values, warnings, convergence and any unit factors. Treat published default values as hypotheses until active parameters confirmed.
2. Confirm electrical J(V) using 2D contact normalization, half-domain physical width and any AreaFactor; raw final terminal current 1.448e-11 in plot units may be very low. Verify QW e/h distributions at matched current (QW3 point eDensity ~1.386e14, hDensity ~4.508e11 cm^-3, NOT region representative). Check polarity, polarization, EBL/injection and existing thermionic solver.
3. Continue separate 2D Rrad/SRH/Auger integrals for all 4 QWs (Clean+DmgL) then compute recombination-based full MQW IQE (do NOT treat QW3 0.0454257% as device IQE). Distinguish lateral mesa Dmg sidewall vs vertical QW/Barrier interface, and confirm if any real interface trap was configured before blaming boundary SRH.
4. Only after physics and injection gates, compare NtSide0 vs nominal damage NtSide1e18 and full/half mesh at matched bias and same current; production A/B NO-GO until verified. No code change requested this turn.

## 2026-10-09 — QW4 complete 2D Clean+DmgL integration result and follow-up

- OBSERVED from 6 distinct 2D field-region values: Clean_QW4 Rad=38746.96, SRH=35617690, Auger=1327.983; DmgL_QW4 Rad=98.768, SRH=226496.2, Auger=2.414354 [s^-1 um^-1]. Combined QW4 Rad=38845.728, SRH=35844186.2, Auger=1330.397354, fraction IQE_rec,QW4=0.1082525242% **QW4 only**. QW3 previously 0.0454256871%.
- NEXT: QW1 and QW2 six standalone-region (Clean and DmgL) 2D integrals each; then sum all 4 wells and calculate whole-MQW recombination ratio. Keep separate field Domain verification; do not use plus-named interfaces as 2D regions.
- Critical before final Baseline: effective SRH/radiative parameters, current-density normalization, physical injection/transient state, half/coarse vs full/fine and nominal NtSide1e18 damaged sidewall comparison. Preserve existing SDevice files and results.

## 2026-10-09 — After QW2 clean/edge full 2D integrations and pp2 model grep

- QW2 full 2D Half-domain: Clean [Rad=83.3149, SRH=54645.76, Auger=1.736316] + DmgL [Rad=0.1672872, SRH=141.6049, Auger=0.003800247], [s^-1 um^-1]. QW2 sum: Rrad 83.4821872; SRH 54787.3649; Auger 1.740116247; `IQE_rec,QW2 = 0.1521382378%`. Together with QW3 0.0454256871%, QW4 0.1082525242% these are independent *QW-only* ratios; QW1 missing.
- Immediate read-only next: SVisual `n2_des` standalone 2D `Clean_QW1` and `DmgL_QW1` Rrad, SRH, Auger integrals; record six values and Domains, then full four-well recombination-based IQE as ratio of summed integrals. Do not average QW efficiencies.
- Active physics grep: pp2:68 DefaultParametersFromFile; pp2:80 SRH(), :82 Auger(), :84 Radiative; no explicit Tau/Lifetime/coeff/AreaFactor in pp2_des.cmd and FASTC1_pp6_des.par. Material database and effective parameter sources need checking; 2D terminal current normalization and injection must be verified *before* final baseline / IQE interpretation. No edit/restart needed.

## 2026-10-09 — All four MQW area integrals complete; next validation is material physics/injection (no rerun)

- QW1 Clean 2D Rrad=857.9041, SRH=77658.39, Auger=252.5448; DmgL Rrad=19.46374, SRH=496.6036, Auger=2.309115 [s^-1 um^-1], domains Clean=5.985012e-3, Dmg=1.500002e-5 um². Full QW1 Rrad=877.36784, SRH=78154.9936, Auger=254.853915; QW1-only ratio=1.1065691%.
- Full four-well Half+Coarse NtSide=0 5V 2D sums: radiative=40072.8158452, SRH=36562944.9075, Auger=1599.706168587, total=36604617.4295138, MQW recombination-based radiative fraction **0.1094747566%**. QW4 provides ~96.93785% of summed radiative integral. Do not call this experimental IQE/EQE, or an accepted baseline.
- NEXT read-only: inspect *effective* material parameters used by active `pp2_des.cmd` / `FASTC1_pp6_des.par` and SDevice log (Radiative coefficient, e/h SRH lifetimes, trap contributions in InGaN); verify 2D current normalization and J-V, carrier injection, QW electric fields and mesh dependence. Compare matched-current damaged NtSide=1e18 and full/fine only after current reference audit. Preserve output and running Node6/12 jobs. No source edit/relaunch.

## 2026-10-09 — Literature-vs-model provenance and loaded material parameters audit

- Paper/source division **confirmed in documentation**: Kou 2019 four In0.15 QWs × 3nm, five GaN barriers ×22nm, nGaN4um, EBL26nm, pGaN120nm; Wu 2023 5nm acceptor-like damaged-edge concept; Chen 2024 demonstrates actual 4x4um class microLED; JBD official 4um PIXEL PITCH, *not* known mesa width. 4um TCAD mesa and numerical n-base/nitride are **representative modeling choices**, not literal JBD geometry. No new live SDE measurement; actual Half+Coarse boundaries remain to be verified.
- From active n2_des.log grep: SRH, Radiative, Auger and default-parameter loading confirmed; GaN.par and InGaN.par loaded. The values and interpolation behavior for SRH carrier lifetimes and Radiative coefficients remain unknown. `Use Si parameters` line cannot be assigned to InGaN without log context.
- Immediate (READ-ONLY): `sed -n '264,355p' n2_des.log` and `sed -n '940,975p' n2_des.log`, plus inspecting SRH/Radiative/Auger in actual T-2022.03 MaterialDB/GaN.par / InGaN.par / InN.par. Verify live pp1_dvs.cmd actual layer thickness/mesa before claiming exact coded match. Do not edit code or accept Baseline until low SRH/IQE and current normalization are understood.

## 2026-10-09 — Terminal shell mismatch during MaterialDB grep (OBSERVED / RESOLVED COMMAND SYNTAX)

- Worker: 이택규, active `JUSUBIN_FAST_HALF_5V_TEST`. User ran requested read-only `sed -n '330,350p' n2_des.log` successfully, output includes `Without incomplete ionization`, `Use Si parameters`, `With SRH-Recombination` (without field/doping/temperature-dependent lifetimes), `With Auger-Recombination`, `With Radiative Recombination`, `Without Surface-Recombination`.
- Earlier GPT incorrectly supplied a **bash-style** `DB=...; for m in ...; do ...; done` block while the terminal is very likely `csh/tcsh`: user output `DB=...: Command not found`, `for: Command not found`, `m: Undefined variable`, `DB: Undefined variable`. Thus none of the `InGaN.par`/GaN/InN grep lines executed. This is **shell syntax**, not a Sentaurus simulation/code failure. No file writes or device restart occurred.
- Corrected next READ-ONLY single command without variables/loops: `grep -niE 'SRH|Radiative|Auger|taun0|taup0|Scharfetter' /user/tools/synopsys/sentaurus/T-2022.03/tcad/current/lib/sdevice/MaterialDB/InGaN.par | head -n 70`. Wait for actual output before interpreting default InGaN Radiative coefficient or SRH lifetimes. Check the log's `Use Si parameters` in correct surrounding device/region context rather than assume Si physics applies to InGaN. No TCAD source edits.

## 2026-10-09 — Read-only InGaN.par recombination section located (OBSERVED, values not yet inspected)

- Worker 이택규 ran csh/tcsh-compatible command in the 5V_TEST directory:
  `grep -niE 'SRH|Radiative|Auger|taun0|taup0|Scharfetter' /user/tools/synopsys/sentaurus/T-2022.03/tcad/current/lib/sdevice/MaterialDB/InGaN.par | head -n 70`
- Actual output:
  `870:Scharfetter * relation and trap level for SRH recombination:`
  `883:Auger * coefficients:`
  `884:{ * R_Auger = ( C_n n + C_p p ) ( n p - ni_eff^2)`
  `893:RadiativeRecombination * coefficients:`
  `894:{ * R_Radiative = C (n p - ni_eff^2)`
- This confirms only the **section/comment locations** in InGaN.par, **not** any numerical SRH lifetimes or Auger/Radiative coefficients. No effective QW parameter values or physical cause of low MQW radiative ratio established. Avoid claiming that parameters are absent, zero or correct merely from these comment matches.
- NEXT READ-ONLY csh/tcsh-compatible command: `sed -n '855,925p' /user/tools/synopsys/sentaurus/T-2022.03/tcad/current/lib/sdevice/MaterialDB/InGaN.par`. Inspect comments, actual material coefficients, and presence of interpolation or inherited defaults. If material file is only a ternary placeholder, inspect InN.par and GaN.par plus effective SDevice log; compare bias/carrier injection before any correction. No code changes or rerun.

## 2026-10-09 — Next check before any Baseline rerun (physics and literature validation)
1. First read only actual active `pp2_des.cmd` global/region Physics, In composition, lifetime overrides and Solve; and `n2_des.log` material model loading context plus 2D current / AreaFactor. Terminal csh/tcsh: avoid Bash variables or for-loop syntax. Do not change DB files.
2. Verify exact In0.15Ga0.85N effective SRH and Radiative parameters; InGaN.par GaAs-derived vendor defaults (taumax 1ns, rad C 2e-10) require calibration. Paper anchor Kou 2019 DOI 10.1364/OE.27.00A643 has numeric SRH 1e-7 (original inverse-seconds typo), Baek 2023 DOI 10.1038/s41467-023-36773-w uses 100ns, rad 1e-10, Auger 1e-31 but different device structure. Do not silently assume 100ns is exact actual lifetime.
3. Normalize 5V NtSide0 I_2D 1.44801646079583e-11 using verified 2D units / Half mesa width from mesh (≈2um). Provisional J≈7.24e-4 A/cm2 under A/um no scaling, far from 0.1 A/cm2 literature comparator, NOT verified. Audit electron-hole injection, Mg incomplete ionization and effective polarization, and transient final vs steady.
4. If needed after audit, separate literature-calibrated parameter branch (sensitivity 1/10/100ns as proposals) while preserving current 5V full-QW IQE_rec 0.1094747566% and original source. Short pilot first, then defect NtSide0/1e18 matched-current and Full/Half/mesh validation. Only then long runs and Project A/B.

## 2026-10-09 — Next exact active-code inspection after live model grep

- New OBSERVED pp2 lines 128/137 region `IncompleteIonization`, lines 141-361 `Traps`, `Transient=BE` at 515, `Transient(` at 585. Actual scope and numerical `Conc` unspecified; need extract before calling defect-OFF true or active Mg ionization confirmed. Plot xMolefraction at 486 is output-only until SDE composition is checked.
- Immediate csh/tcsh compatible read-only commands: `sed -n '112,175p' pp2_des.cmd` then `sed -n '505,615p' pp2_des.cmd`. Inspect active concentration in all Dmg region traps (first + expanded rest when needed), material-ionization regions, transient goal/hold, terminal current scaling.
- Preserve 5V_TEST and reference sources, audit MaterialDB effective InGaN lifetime and actual 2D current injection, then decide calibrated separate-branch short pilot; no new long-run until pre-run gates.

## 2026-10-09 — SWB Material Parameter dialog handling and JuSubin handoff tasks

- **HOLD current GUI**: SWB screenshot is `JUSUBIN_FAST_HALF_SWB` original, `Create Parameter File: sdevice.par does not exist`; `Silicon` is new-file template default. **Cancel**, do not create file or overwrite original. Completed baseline proof is separate `JUSUBIN_FAST_HALF_5V_TEST`; its live pp2 used `FASTC1_pp6_des.par` and loaded actual InGaN/GaN MaterialDB. No reason to say 5V simulation was silicon simply from this GUI.
- Proposed NEW separate branch only after source backup: copy 5V_TEST under a distinct calibration name; compare `sdevice_des.cmd` File Parameters, `FASTC1_pp6_des.par`, preprocessed `pp2_des.cmd`/par and material defaults; then `Choose Materials` → GaN, InGaN, AlGaN, Nitride (include InN only if needed); inspect generated .par and merge needed preexisting custom physics; preprocess and diff, never launch full run before preflight.
- From JuSubin Oct8: Mg/p-GaN & n-GaN doping profile unverified; half+coarse 138194/65513 built but full 290814 reference equivalence not proven; QS copy Oct9 later failed at ~0.0193 V before 0.3 V target; NtSide1e18 accelerated trap-on validation remains undone, while separate NtSide0 5V and QW1..4 integrated values now successful. C2 Save/Load reference work not proven.
- Main physic gate: uncalibrated InGaN recombination materials originally borrowed from GaAs (1ns file tau max; Radiative C2e-10); published InGaN examples use alternate 100ns, yet effective parameter and electrode current normalization unknown. MatDB copy is not calibration; correct via hypothesis-controlled literature parameter branch after audit, preserve 5V_TEST reference. Dope/profile → material provenance and 2D J → Nt0 short stable pilot → Nt1e18 same-current → Half-Full mesh convergence → A/B no GO until validated.

## 2026-10-09 — Immediate next after original FASTC1 custom .par contents verified

- Original `JUSUBIN_FAST_HALF_SWB/FASTC1_pp6_des.par`: only lattice axes, Thermionic Formula 1, GaN pMagnesiumActiveConcentration Ionization E_0 .2eV, alpha 8e-9, g4, Xsec1e-14. No InGaN-specific SRH/Auger/Radiative custom values in this copy; default material database input has uncalibrated GaAs-derived rates. However check effective QW material mixing and any regional overrides separately; do not claim original and 5V_TEST par byte-identical yet.
- NEXT user terminal (read only): `sed -n '112,175p' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd`. Confirm Mg ionization Physics scope / actual trap concentration rather than assume activation. Keep original & completed 5V_TEST intact and proceed with independent calibration after doping/J checks. SWB popup Cancel and no new sdevice.par.

## 2026-10-09 — 5V_TEST confirmed region-specific Mg and NtSide=0 trap excerpts

이택규 directly inspected the active completed 5V_TEST `pp2_des.cmd` (lines 112–175): `Clean_pGaN` and `DmgL_pGaN` explicitly enable `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`; `DmgL_pGaN` and `DmgL_EBL` trap entries are `Acceptor Conc=0, EnergyMid=0.75 eV from valence, e/h cross-section=1e-15 cm²`. This verifies local Mg ionization *model declarations* and two explicit trap-OFF regions, NOT actual Mg free-carrier/donor doping profile. All other trap region concentrations require complete deck grep (prior audit indicated 12 zero). Global log 'Without incomplete ionization' cannot override observation of region-specific code without scoping analysis. No files altered, 5V results preserved. NEXT READ-ONLY `grep -nE 'Physics \(Region=|IncompleteIonization|Traps|Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd`, then SDE doping profile and physics/current density calibration. Publication-grade baseline validation still pending.

## 2026-10-09 — After 12/12 sidewall trap concentrations verified zero

- OBSERVED in completed `JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd`: all twelve DmgL trap `Conc=0` (pGaN, EBL, Barrier0..4, QW1..4, nGaN); model Mg `IncompleteIonization` enabled specifically in Clean_pGaN and DmgL_pGaN. **NtSide0 trap off verification COMPLETE**; do not repeat this gate. Still need corresponding NtSide1e18 trap active test and physical compare.
- NEXT: check active `pp1_dvs.cmd` SDE doping declaration+placement for pMg and n donor. Suggested csh-safe read-only command `grep -niE 'define-constant-profile|define-analytical-profile|define-constant-profile-placement|define-constant-profile-region|pMagnesiumActiveConcentration|Doping|Donor|Phosphorus|SiliconActiveConcentration' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd | tail -n 100` then inspect ranges with `sed` and SVisual actual n1_msh.tdr (SDE may need mesh in Plot).
- Preserve working NtSide0 5V_TEST and source. Continue 2D J, InGaN effective recombination lifetime/rad calibration and transients before a separate pilot. No broad Project A/B production.

## 2026-10-09 — Active 5V_TEST SDE numeric doping constants observed (NOT an error conclusion)

- 이택규 ran `grep -nE -C 3 'N_Mg_p|N_A_EBL|N_D_n|x_Al_EBL' .../JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd | head -n 100`. Live SDE shows `x_In=0.15` at line 100, `x_Al_EBL=0.15` at line 102, `N_Mg_p=9.59e18 cm^-3` at line 119, `N_A_EBL=3e17` at 121, `N_D_n=5e18` at 123, `N_D_bar=1e15` at 125. Prior lines 501-615 show these variables assigned to intended pGaN, EBL, nGaN/base regions.
- **Critical semantic distinction**: `CMP/COMMON_BASELINE.md` documents `p-GaN effective active acceptor≈3e17 cm^-3`, while SDE assigns **raw `pMagnesiumActiveConcentration`=9.59e18 cm^-3**, with specific GaN `IncompleteIonization` and E0=0.2eV etc in SDevice. This is NOT automatically an error: Mg dopant density ≠ actual ionized Mg acceptor concentration, hole density, or effective active acceptor density. But the intended correspondence to documented 3e17 target is NOT YET CALIBRATED/VERIFIED; do not call 9.59e18 physically valid just from ionization declaration. Very high Mg input may present compensation/solubility concerns needing later literature physical validation.
- `N_A_EBL=3e17, N_D_n=5e18, N_D_bar=1e15, x_In=0.15, x_Al_EBL=0.15` match nominal documented model values (subject to actual SDE material/profile assignment). No code or simulation errors in this grep, no need to rerun now.
- JuSubin TIMELINE earlier records a Half+Coarse `DopingConcentration` SVisual screenshot color scale near -9.59e18 to +5e18, suggestive of signed *input/net dopant profile* representation but no pointwise verified ionized Mg/free-hole density or across-layer cutline. Do not equate `DopingConcentration` with p or ionized Mg.
- NEXT read-only, csh-safe: `sed -n '105,128p' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd` (inspect inline comments on rationale for 9.59e18); then probe existing n2_des.tdr for `pMagnesiumMinusConcentration`, `hDensity`, `DopingConcentration` in central Clean_pGaN away from contacts and verify 3e17 target only if this is the intended metric. Later calibration/low-current analysis separately. Preserve all sources/data; no new run.

## 2026-10-09 — Verify carrier density after discovering prior Mg calibration comment

Live `pp1_dvs.cmd` comment states N_Mg_p=9.59e18 was calibrated previously for pGaN `hDensity ~ 3e17 cm^-3` at 300K with incomplete ionization; this is a COMMENT, not current measured output. NEXT: in SVisual load the already completed 5V `n2_des.tdr`, select `hDensity` and probe representative Clean_pGaN region bulk coordinate; record units, bias 5V, then if possible `pMagnesiumMinusConcentration` and 0V equilibrium comparison. DO NOT change Mg input just because raw dopant 9.59e18 differs from effective target 3e17. Keep sources/results and no new solver run.
