## 2026-10-10 ~20:35 KST — Mg Acceptor/Minus vs NetDoping output relation unresolved (OBSERVED DATA / MODEL AUDIT)
- Additional direct 5V NtSide0 Clean_pGaN Probe shows AcceptorConcentration=9.59e18 cm^-3 (X=0.05,Y=1.0um); matching MgActive=MgMinus=9.59e18, but Donor=0 and signed Doping≈-3.00032e17, hDensity≈+3.00034e17 cm^-3. Current interpretation of active ionization, net doping recalc and species fields needs verification. This is not a simulation crash nor grounds for blind code edits. Next read actual pp2/n2 ionization and parameter binding read-only, then determine meaning from T-2022.03 references.

## 2026-10-10 — Mg Minus equals Mg Active in Clean_pGaN (UNRESOLVED interpretation)

- Screenshot, worker 주수빈, `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` 5V NtSide0, (X=0.05,Y=1.0 um) Clean_pGaN: pMagnesiumActive and pMagnesiumMinus both 9.59e18 cm^-3; hDensity 3.000342790006e17 cm^-3. This is an *interpretation/validation blocker*, **not a runtime crash**. Sentaurus species naming links Minus to ionized acceptor; confirm effective output semantics and charge balance before concluding Mg ionization/compensation.
- Read-only next: probe DopingConcentration, AcceptorConcentration, DonorConcentration, eDensity in same zone; inspect actual custom species definitions and material ionization. Do not infer hDensity/total Mg equals ionized fraction.

## 2026-10-10 ~19:43 KST — SVisual Cutline signed net-doping graph successfully restored (OBSERVED screenshot)

- 작업자 주수빈. 완료된 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` (NtSide=0, 5 V) `DopingConcentration` `Cutline_Y Plot`에서 Y-axis 수동 범위 설정 후 음·양 signed net-doping plot 전체가 다시 표시되는 것을 직접 확인.
- Current screenshot: p-side upper region roughly −3e17 cm^-3; shallow stacked EBL/MQW region shows multiple transitions; long n-GaN body has near-constant +5e18 cm^-3. Values are approximate visual readings, not separately extracted exact layer-point quantities. Underlying constant-profile SDE model is consistent; do not extrapolate to measured SIMS/MOCVD dopant grading or claim free holes equal net doping.
- **GUI issue resolved**: previous `Axis Properties` Y-Min/Max both Fixed at approx 1e-20 erroneously clipped curve; manually entered sensible linear signed Y-range (~−4e17 to +6e18), now displays step-like complete-depth plot. Only view settings changed, no TCAD code/data nor live CAL job affected.
- Next: on the **right 1D graph X axis** double-click axis tick, Axis Properties Main set fixed Min=0 and Max=0.4 μm (Log Scale off), keep fixed linear Y bounds unchanged, share zoomed plot for pGaN/EBL/MQW doping interpretation; later compare `hDensity`, pMg species in identical cutline.

## 2026-10-10 ~19:37 KST — SVisual Y-axis fixed-range root cause confirmed (OBSERVED GUI; remedy not yet tested)

- 작업자: 주수빈. 완료된 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`에서 `DopingConcentration` / `Cutline_Y Plot` 표시 이상을 조사.
- 제공된 T-2022.03 SVisual `Axis Properties > Main` 직접 캡처에서 **Y축 Min = 9.9927e-21, Max = 1.00073e-20** 및 양쪽 **Fixed 체크**를 확인. `Log. Scale`은 해제되어 있음.
- 확정된 GUI 원인: 잘못 저장된 극히 좁은 Y축 고정 범위가 10^17~10^18 cm^-3 수준 signed DopingConcentration 데이터를 가림. 이는 원래의 도핑 입력이나 TCAD 계산에 대한 오류 증거가 아님. 과거 'log axis 때문에 보이지 않는다' 해석은 이 최신 화면에 대해서는 정정됨.
- 제안한 복구(아직 실행결과 미확인): `Axis Properties`의 Min/Max 양쪽 `Fixed` 해제, `Log. Scale` 해제 유지, 1D cutline 자동 축으로 복원되는지 확인 후 QW/EBL 인접 깊이 구간 분석.
- 소스·파라미터·결과 파일·실행 중인 별도 CAL job 수정 없음. 후속 스크린샷으로 표시 복구 검증 필요.

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

## 2026-10-10 — FAST_C1 n6 numerical termination: Step-size is too small (OBSERVED LOG)

- 작업자 이택규가 학교 서버 실제 터미널 로그 두 개 제공. FAST_C1 `GaN_PiN_Diode_FAST_C1/n6_des.log` (NtSide=0)는 반복 Newton 15회 초과 후 `Newton didn't converge, trying again with smaller timestep...` 그리고 `Finished, because... Step-size is too small.`가 나타남. 2026-10-10 17:39:07 KST 정상 프로그램 종료 메시지 `simulation finished`, `Good Bye !`, `n6_des.tdr` 쓰기 및 라이선스 반환이 있더라도 5V 목표 달성/물리적 성공이 아니라 **수치적 최소 time-step 실패**. Wallclock 525152.85s ≈145h52m32s, peak mem 5.94GB. 마지막 accepted voltage는 제공된 50줄에 없어 UNRESOLVED; 깊은 원인(물성/mesh/수치 설정) 역시 확정 불가.
- 별개 프로젝트 `CMP_BASELINE_1.2.0_CAL/n2_des.log`에서 t=0.828339→0.828343s BE step은 Newton 2회 후 `|RHS| less than 1e-3`로 accepted, 표기 anode=4.142E+00 V, total current=4.678E-14 raw. 기존 4.138V보다 약 0.004V 진전(4.142/5≈82.84% 전압 구간이지 walltime 아님). 후속 t=0.828343→0.828348s attempt은 Iteration 11까지 `RHS≈1.09e-03 >1e-03`; 스크린샷/로그가 중간에 끝나 아직 accepted/failure 미확인. 5V 완료·tau_max=100ns 실제 유효성·ETA 미확인.
- 변경: GitHub 진단 기록뿐. 학교 서버 소스, SWB, 실행 중 CAL, 완료된 `JUSUBIN_FAST_HALF_5V_TEST` 결과는 건드리지 않음.
- NEXT READ-ONLY: `grep -n 'anode ' /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1/n6_des.log | tail -n 5` 로 FAST 마지막 성공 전압을 확인하고 n6_des.sta/err 및 버전 비교. CAL은 시간 경과 뒤 tail로 accepted t/V, `Newton didn't converge`, step-size, fatal/Good Bye 여부 확인. FAST n6 즉시 재실행 또는 MinStep/Iterations 임의 완화 금지.

## 2026-10-10 ~19:02 KST — FAST_C1 n6 red Failed status screenshot (OBSERVED UI / ROOT CAUSE UNRESOLVED)

- 이택규 SWB 캡처: 선택 프로젝트 `GaN_PiN_Diode_FAST_C1`, row NtSide=0 SDevice `[n6]` 빨간색. SWB 기본 색상은 `failed=#FF0000`, 따라서 실패 상태로 해석하되 custom node-color 여부 및 실행 종료 로그 미확인. 이 화면 자체는 `CMP_BASELINE_1.2.0_CAL`의 상태를 보여주지 않음.
- 원인, 마지막 accepted voltage, 재시작 가능성, 5V 도달 여부 전부 UNRESOLVED. CAL은 별도 n2로 마지막 직접 로그 ~4.138 V cutback 및 5V 미확인.
- Next READ ONLY: `GaN_PiN_Diode_FAST_C1/n6_des.log` tail 및 `n6_des.err/.sta` 확인, `CMP_BASELINE_1.2.0_CAL/n2_des.log` tail 비교; 변경/중단/재실행 금지.

## 2026-10-10 — Outdated SDevice comments falsely advertise numerical ramp/Save schedule (OBSERVED)

- Source: private `CMP_BASELINE_1.2.0_CAL_AUDIT.tar.gz` inspection of successful 5V_TEST `sdevice_des.cmd` vs `pp2_des.cmd` and `n2_des.log`. Header claims 0–4V Increment1.2, 4–5V Increment1.05, Save at 4.0/4.5/4.8/5V; mid-Solve comment claims short 0–0.3V smoke. Actual executable has single 0–5V Transient Increment1.2 and Save at 5V only. Solver completed, so this is a **documentation/extraction/checkpoint-plan mismatch**, not a simulation failure. Intermediate 4–5V TDR coverage absent in active command. No source edited. Correct in a separate future CAL branch after preserving originals and verifying exact syntax.

## 2026-10-08 — cmp216 FAST_C1_ACCOUNT_TEST n6 logging stopped during new BE-step (OBSERVED / TERMINATION CAUSE UNRESOLVED)

- OBSERVED incomplete log, **not a confirmed software error**: next BE-step printed iteration header but no iterations; subsequent grep found no `fatal`, `killed`, `aborted`, `signal`, `good bye`, or `simulation finished` report. Earlier grep `license` shows successful checkout Oct 7 16:22.
- Status UNRESOLVED: possible OS/session termination or other interruption requires evidence; do not assign root cause without exit code/system logs.
- Next: review login history and launch method/job state on ssudisu2; preserve existing simulation files.

## 2026-10-04 — B0 CSV ratio check command quoting error under csh/tcsh

- 작업자: 이택규
- 상태: OBSERVED / RESOLVED COMMAND SYNTAX
- multiline `python3 -c '...'` command was pasted into csh/tcsh and split across prompts, causing `Unmatched '`, `Badly placed ()'s`, and globbing errors.
- no file/simulation change occurred.
- correction: use a single-line awk command for the CSV retry-dt/rejected-dt ratio check.

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

## 2026-09-26 — Project Log does not expose root cause

Project Log shows:
- Node 12 SDevice starts normally.
- It exits abnormally shortly afterward.
- Scheduler marks node failed.
- `gsub exits with status 1`.

This is a wrapper/scheduler-level symptom, not the internal SDevice root-cause message.

Combined with prior evidence, the strongest current root-cause candidate remains the Mg incomplete-ionization parameter/material-scope mismatch in InGaN, but this Project Log alone does not prove it.

---

## 2026-09-26 — Existing Node6 vs current Node12 is not an apples-to-apples baseline comparison

New evidence:
- Node6 `pp6_des.par`: GaN Ionization uses PDopantActiveConcentration and NDopantActiveConcentration.
- Node12 `pp12_des.par`: GaN Ionization uses pMagnesiumActiveConcentration.

Thus the generated parameter files are from different model revisions.

Consequence:
- Do not use current Node12 (even if fixed) against historical Node6 for final NtSide effect quantification.
- Node12-only fixes may be used for crash diagnosis only.
- Final comparison must rerun NtSide=0 and NtSide=1e18 from one frozen source/PAR revision.

Status: **COMPARISON INVALIDATED / ROOT CAUSE DIAGNOSIS CONTINUES**

---

## 2026-09-26 — Mg incomplete-ionization parameter scope mismatch

Evidence:
- `pp12_des.par` defines:
  - `Material="GaN"`
  - `Ionization { Species("pMagnesiumActiveConcentration") { E_0=0.2, alpha=8e-9, g=4.0, Xsec=1e-14 } }`
- No InGaN Ionization block is present.
- Failed Node 12 log reports missing incomplete-ionization parameters for an Mg-related species in InGaN QW regions immediately before SDevice exits.
- Current source activates `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")` globally.

Most likely cause:
Incomplete ionization is being invoked in InGaN regions without material/species ionization parameters.

Proposed fix:
Remove the global incomplete-ionization activation and enable it only in p-GaN regions where the GaN Mg ionization parameters apply.

Status: **CAUSE STRONGLY IDENTIFIED / FIX PROPOSED; requires rerun confirmation**

---

## 2026-09-26 — Current source has no NtSide conditional; Node 6 is stale relative to current source

Confirmed from full current SDevice source:
- `@NtSide@` is used only as trap `Conc`.
- No `#if/#else/#endif` or other NtSide-dependent insertion controls `Thermionic`, `IncompleteIonization`, or Plot fields.
- Current source always contains:
  - `Thermionic`
  - `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`
  - Mg/quasi-Fermi extra Plot fields.

Consequence:
The successful pp6 deck lacking these items cannot have been generated from the current source revision. Node 6 is a stale/historical generated deck relative to the current source.

Current Node 12 failure candidate:
Mg incomplete ionization is selected explicitly, and Node12 log terminates after reporting missing incomplete-ionization parameters in InGaN QW regions.

Required next evidence:
Inspect `pp12_des.par` for `Ionization`, `Magnesium`, and `InGaN` parameter definitions before changing the physical model.

Status: **ROOT CAUSE NARROWED / NOT YET CONFIRMED**

---

## 2026-09-26 — Node 12 rerun reproduces exit failure

Observed:
- Node 12 rerun alone.
- Failure reproduced.

Interpretation:
- Reproducible, not obviously a one-off execution glitch.
- Given same-source NtSide split, focus shifts to parameter-dependent preprocessing or stale generated-node provenance.
- pp6 vs pp12 differences remain diagnostic evidence but not proof of manual source differences.

Next:
- Inspect original source conditionals around NtSide.
- Verify whether Node 6 was preprocessed from the same current source revision as Node 12.

Status: **REPRODUCIBLE / ROOT CAUSE UNRESOLVED**

---

## 2026-09-26 — Correction to Node 6/12 deck-drift interpretation

User confirmed:
- Same original SDevice code was used.
- Only Workbench parameter `NtSide` was split into 0 and 1e18.

Correction:
The pp6/pp12 differences do **not** prove that the user manually changed Physics/Plot between branches. They may be generated by parameter-dependent preprocessing or node/version behavior.

Do not apply the previously proposed removal of `Thermionic`, species-selected `IncompleteIonization`, or extra Plot fields until the original source is inspected.

Next:
1. Inspect original `sd_fdiv_des.cmd` for `@NtSide@` and preprocessor conditionals.
2. Search source for `Thermionic`, `IncompleteIonization`, `Dopants`, `eQuasiFermiEnergy`, Mg Plot fields.
3. Compare Node 6/12 Job Log source path/timestamps and input-file provenance.

Status: **UNRESOLVED / PRIOR FIX RETRACTED**

---

## 2026-09-26 — Root-cause confounder identified: Node 6/12 are not NtSide-only decks

Exact preprocessed diff:
- Node 12 only: `Thermionic`
- Node 12: `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`
- Node 6: `IncompleteIonization`
- Node 12 only Plot fields: `eQuasiFermiEnergy`, `hQuasiFermiEnergy`, `pMagnesiumActiveConcentration`, `pMagnesiumMinusConcentration`
- Intended trap difference remains `Conc=0` vs `Conc=1e18`

Consequence:
The Node 12 exit(1) cannot be attributed to NtSide=1e18 alone because physics/output configuration drift is present.

Proposed minimal diagnostic fix:
Restore Node 12 source Physics/Plot to the successful Node 6 configuration and keep only NtSide=1e18 as the changed parameter. Rerun only the 1e18 branch.

Status: **PROPOSED FIX / ROOT CAUSE NOT YET CONFIRMED**

---

## 2026-09-26 — Node 12 deck-drift suspicion

New evidence from failed Node 12 preprocessed deck:
- global `Thermionic` present
- `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`
- expanded Plot output set
- NtSide trap Conc=1e18 throughout DmgL/R sidewall regions

This differs from the synchronized baseline/old successful-deck record, which used plain `IncompleteIonization` and did not record `Thermionic`.

Interpretation:
- The failed branch may contain deck drift beyond NtSide.
- This is not yet the proven crash cause.
- Exact successful Node 6 pp6_des.cmd comparison is required before modifying physics.

Status: **UNRESOLVED**

---

## 2026-09-26 — Successful Node 6 lacks Node 12 Mg incomplete-ionization message

New evidence:
- Successful NtSide=0 Node 6 reaches 5 V and normal completion.
- User searched successful `n6_des.log`: no `mMagnesiumActiveConcentration` message.
- Failed Node 12 shows repeated `mMagnesiumActiveConcentration` incomplete-ionization messages in InGaN immediately before exit.

Interpretation:
- This message is now a strong failure-correlated difference.
- However, root cause is not yet proven because Node 6 and Node 12 may have preprocessed deck/parameter differences beyond NtSide.

Required next comparison:
1. `pp6_des.cmd` vs `pp12_des.cmd`
2. `pp6_des.par` vs `pp12_des.par`
3. Confirm whether the only intended CMD difference is trap `Conc=0` vs `Conc=1e18`.

Status: **UNRESOLVED**

---

## 2026-09-26 — Node 12 log terminates after incomplete-ionization messages

Observed:
- `n12_des.log` ends immediately after repeated messages that `mMagnesiumActiveConcentration` has no incomplete-ionization parameters in InGaN QW regions.
- The tool then checks licenses back in.
- No normal solver start/completion sequence is visible.

Interpretation: **UNRESOLVED**.
This message can no longer be assumed harmless solely from formatting; its causal role must be tested against the successful NtSide=0 branch.

Highest-value comparison:
- Search the successful NtSide=0 node's `*_des.log` for `mMagnesiumActiveConcentration`.
- If identical messages occur and the successful run proceeds, they are not the failure root cause.
- If absent in the successful branch, investigate parameter/material setup differences in the failed branch.

---

## 2026-09-26 — Node 12 Find Error contains warnings only

Observed:
- Workbench `Find Error` reaches `**** End`.
- Visible entries are model/material warnings only:
  - vanOverstraetendeMan E0 isotropic vs anisotropic values.
  - missing incomplete-ionization parameters for `mMagnesiumActiveConcentration` in InGaN QW regions.
- No explicit `ERROR` / `FATAL` root-cause line is visible.

Interpretation:
- These warnings are not yet proven to be the cause of `sdevice exit(1)`.
- The actual SDevice log file `n12_des.log` is now the highest-priority evidence source.

Next:
1. Open `n12_des.log`, inspect the last 50–100 lines.
2. Search there for error/fatal/abort/exception/signal.
3. If non-diagnostic, inspect `n12_des.sta`.

Status: **UNRESOLVED**

---

## 2026-09-26 — Node 12 SDevice exit(1) after successful preprocessing

Job Log evidence:
- Preprocessor successfully initialized.
- `pp12_des.cmd` and `pp12_des.par` were generated.
- Node dependency on node 1 was resolved.
- SDevice launched as:
  `sdevice --max_threads 4 pp12_des.cmd`
- SDevice then terminated with:
  `sdevice exited abnormally: exit(1)`

Interpretation:
- Workbench preprocessing/dependency failure is not the primary blocker.
- The failure occurs inside SDevice after launch, likely during deck/model/material initialization before normal solve completion.
- Exact root cause still requires the first explicit SDevice error/fatal message.

Next:
1. Use Node 12 Job Log **Find Error**.
2. Search `n12_des.err` for `Error:`, `Fatal`, `Unsupported`, `not found`, `invalid`, `cannot`.
3. If needed inspect `n12_des.sta`.

Status: **UNRESOLVED**

---

## 2026-09-26 — Node 12 gjob abnormal child exit

Observed in `n12_local.err`:
```text
Job failed
Error: Unknown error: child process exited abnormally
gjob exits with status 1
```

Meaning:
- Workbench wrapper confirms the SDevice child process exited abnormally.
- This is **not yet the root cause**; it is a generic wrapper-level failure report.

Next:
1. Inspect Node 12 Job Log bottom section.
2. Inspect `n12_des.job` if Job Log is non-diagnostic.
3. Inspect `n12_des.sta` for the last tool stage/status.
4. Search `n12_des.err` / `n12_des.out` for segmentation, killed, memory, fatal, abort, license, or signal text.

Status: **UNRESOLVED**

---

## 2026-09-26 — NtSide=1e18 Node 12 early termination evidence

Observed from Node 12:
- `n12_des.err`: E0 anisotropy and incomplete-ionization parameter warnings are visible; no explicit fatal line in the provided view.
- `n12_des.out`: output ends after material/reference-potential initialization and license check-in.
- Missing normal terminal text: `Sentaurus Device simulation finished`, `Good Bye !`.
- No visible `.tdr` / `.plt` output in the Node Output Files list.

Interpretation: **UNRESOLVED**, but the failure appears to occur before normal solve/output completion rather than as an observed late transient convergence failure.

Next evidence:
1. `n12_local.err`
2. Workbench Job Log
3. `n12_des.job` if needed
4. Search `n12_des.err` for `Error`, `Fatal`, `abort`

Do not alter Nt/Et/sigma/geometry until the process exit reason is known.

---

## 2026-09-26 — NtSide=1e18 baseline split-run failed

Observed:
- Sentaurus Workbench split run에서 `NtSide=0`은 완료.
- `NtSide=1e18`은 failed 상태.

Cause: **UNRESOLVED**

Required evidence:
1. failed 1e18 SDevice node의 `*.err`
2. 해당 `*.out` 마지막 50~100줄
3. 가능하면 failed node 번호와 preprocessed `pp*_des.cmd`

Do not change baseline trap density/energy/cross section or geometry before identifying the actual first failure message.

Status: **UNRESOLVED**

---

# Error Log

## 2026-09-21 — SVisual1 Tcl title

Error:
```text
invalid command name "v"
```

Cause:
Tcl에서 `[V]`가 command substitution으로 해석됨.

Fix:
```tcl
-title {Anode Voltage [V]}
-title {Anode TotalCurrent [raw 2D output]}
```

Status: **Resolved**

---

## 2026-09-21 — SVisual1 fit command

Error:
```text
invalid command name "fit_plot"
```

Cause:
현재 Sentaurus Visual T-2022.03 환경에서 해당 Tcl command가 유효하지 않음.

Status: **Resolved/removed from active script**

---

## 2026-09-21 — SVisual2 invalid create_plot option

Error:
```text
create_plot: "-2d" is not a valid property
```

Cause:
SVisual Tcl에 잘못된 `create_plot -2d` 사용.

Status: **Resolved by minimal dataset-based plot script**

---

## 2026-09-21 — Workbench reference macro

Error:
```text
ERROR: @node|sdevice@: tool instance 'sdevice' doesn't exist
```

Cause:
현재 Workbench flow에서 `@node|sdevice@` reference가 유효하지 않음.

Fix:
바로 앞 SDevice를 `@previous@`로 참조하도록 변경.

Status: **Resolved**

---

## 2026-09-21 — SVisual2 cannot load TDR

Current error:
```text
File 'n9_des.tdr' could not be loaded.
```

Known facts:
- Node 10 = SVisual2
- Node 9 = SDevice2
- Node 9 solver output에는 `Sentaurus Device simulation finished`, `Good Bye !`가 기록됨
- Node 9 Explorer Output Files 화면에서 `n9_des.tdr`이 확인되지 않음
- SVisual2는 현재 `n9_des.tdr`을 hard reference함

Status: **UNRESOLVED**

Next diagnostic:
1. `pp9_des.cmd`의 preprocessed `File { ... }` 블록에서 실제 `Plot = "..."` 값 확인
2. Node 9 Output Files 전체 목록에서 실제 TDR 이름 확인
3. `@tdrdat@` macro가 어떤 파일명으로 치환되는지 확인
4. 필요 시 SVisual2를 실제 output filename에 맞춤

Do not change baseline physics parameters while diagnosing this.


## 2026-10-09 — QS Copy sweep stopped below minimum step (UNRESOLVED)

- Work session: 이택규, inspecting JuSubin's separate `JUSUBIN_FAST_HALF_SWB_Copy` QS smoke.
- Evidence (`n2_des.log` tail, user-provided): `Finished, because... Step-size less than MinStep (step-size = 8.3986e-07)`.
- SDevice wrote `n2_qs0p3_ckpt_des.sav`, circuit `.sav`, and `n2_des.tdr`, then `Good Bye !` at 2026-10-09 00:28:10 KST; wallclock 18417.09 s (5:06:57), peak 2.96 GB.
- Interpretation: QS sweep did not complete normally at goal; `Good Bye` and saves are not proof of reaching 0.3 V. Last accepted voltage/underlying Newton or cutback failure is **not yet verified**.
- Contrast: original half+coarse transient reached 0.3 V, wallclock 25019.43 s. Run durations are NOT a valid speed benchmark with different end conditions.
- Next: inspect QS last accepted anode bias in final `n2_des.plt` record, repeated rejected steps in `n2_des.log`, and the full `.err` output. Preserve both branches and Common Baseline before proposing solver changes.


## 2026-10-09 — QS Copy last accepted bias determined
- 작업자: 이택규. OBSERVED from user-provided `JUSUBIN_FAST_HALF_SWB_Copy/n2_des.plt` tail and `n2_des.log` grep.
- Last recorded QS pseudo-time: 6.43487876313307E-02; last anode OuterVoltage: 1.93046362893992E-02 V (0.0193046363 V; 19.3 mV, only ~6.435% of requested 0.3 V).
- Last log attempts at t=0.0643488 to 0.0643505 then terminated `Step-size less than MinStep (step-size = 8.3986e-07)`.
- QS runtime 18417.09 s but did NOT reach goal. Cannot compare as speedup to original transient that reached 0.3 V in 25019.43 s.
- Root numerical/physics trigger not yet established. Next: inspect QS log around lines 6900-7000 and `n2_des.err`; no blind MinStep or baseline modification.


### 2026-10-09 confirmed failure mechanism (OBSERVED) — QS Copy
- Final failed QS step t=0.0643488 to 0.0643505 (1.6797e-6): Newton Bank/Rose `Coupled` Poisson+electron+hole factor=1, |Rhs| nonmonotonic (from 3.80e1, peaks to 1.26e8, last 1.85e6); `#iterations larger than 15` after 208.16 s (assembly 41.26, solve 161.58). Then half-step retry proposed at 8.3986e-7, smaller than MinStep 1e-6; QS stops.
- `.err` contains `vanOverstraetendeMan` E0 isotropic 1 vs anisotropic 4e5 mismatch; only isotropic value used. No basis to attribute QS Newton failure to this warning. Also InGaN region DOS mass material interpolation lines.
- CONFIRMED immediate cause: Newton not converged at iteration limit and next cutback below MinStep. UNRESOLVED root cause of poor conditioning/divergence. No evidence that blindly lowering MinStep fixes issue.


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

## 2026-10-09 — Correction: wrongly interpreted SVisual '+' group as combined QW bulk (GPT guidance error)

- User screenshot of SVisual Field Integration `RadiativeRecombination` with `Clean_QW3` and `Clean_QW3+DmgL_QW3` highlighted displays output ONLY for `Regions of Dimension 2: Clean_QW3`, Integral 2.657110e+02 [s^-1 um^-1], Domain 5.985012e-03 [um^2].
- GPT earlier incorrectly stated `Clean_QW3+DmgL_QW3` was guaranteed combined whole-QW ROI; current evidence does NOT support that and likely represents a boundary/interface label (exact '+' metadata unconfirmed). Do not claim total QW3 integral from this selection.
- Safe fix (read-only): independently integrate `Clean_QW3` and *standalone* `DmgL_QW3` using SVisual's `Regions of Dimension 2` pane to verify each result and sum their integrals (avoid overlapping selections or confusing interface). No user computation or device source needs rerun, no data was deleted or changed.

## 2026-10-09 — Shell syntax mistake in supplied MaterialDB inspection command (RESOLVED GUIDANCE)

- Assistant provided Bash assignment `DB=/...` and Bash `for m in ...; do` while user's current shell reports C-shell-family errors (`Command not found`, `Undefined variable`). Read-only `sed -n '330,350p' n2_des.log` worked. No MaterialsDB parameter values were retrieved; no simulation/model/source error from this incident.
- Corrected with one literal-path C-shell-compatible command `grep -niE 'SRH|Radiative|Auger|taun0|taup0|Scharfetter' /user/tools/synopsys/sentaurus/T-2022.03/tcad/current/lib/sdevice/MaterialDB/InGaN.par | head -n 70`. After output verify effective parameter selection/material DB and exact status of `Use Si parameters`. Do not rerun/modify TCAD.
