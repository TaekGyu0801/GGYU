## 2026-10-10 22:39 KST — Project A carbon high-resistivity edge literature and feasibility review (PROPOSED)
- Worker: 이택규. Research request: evaluate physical/process/TCAD feasibility of Project A and recover original carbon high-resistance literature.
- Recovered original project literature map from CMP/PROJECT_AB_TCAD_IMPLEMENTATION_PLAN.md: Richter 2020 (10.1002/crat.201900129), Ramdani 2012 (10.1016/j.sse.2012.04.034), Cao 2023 (10.1038/s41598-023-41678-1), Chang 2020 (10.1186/s11671-020-03372-3), Taube 2015 (10.1002/pssa.201431724). Distinguish C-doped grown material, C implantation-induced lattice damage and actual microLED sidewall data.
- Proposed first mechanism screen remains existing documented plan: preserve 5nm Dmg and common baseline; SDE Cedge region inside damage in upper n-GaN below MQW; SDevice carbon-related deep acceptor/compensation vs A-null same mesh. Trial lateral wC 0/0.05/0.10/0.20/0.30um is proposed not fabricated or validated. No evidence that local carbon implantation microLED sidewall is validated by these papers. A/B production remains NO-GO due to low-J Gate0 and extraction/mesh/active-deck requirements.
- No code/simulation changed. NEXT: audit actual active SDE mesh/region coordinates and current paths, compare Cedge upper-n only vs additional location options, validate null control, then small pilot after Gate0.

## 2026-10-10 ~22:11 KST — CAL 4.149V accepted; next BE-step Newton oscillatory (OBSERVED server log, READ ONLY)

- 이택규가 학교 서버 `CMP_BASELINE_1.2.0_CAL/n2_des.log` `tail -n 60` 실제 출력 제공. CAL n2 100ns sensitivity의 **accepted** 두 단계 확인: (1) 직전 접촉 anode=4.149E+00V, total current=4.831E-14 (로그 표시 단위, 2D normalization 주의); (2) `Computing BE-step from 0.829858 s to 0.829862 s (Stepsize 3.8830e-06 s)` 후 Newton iteration2 RHS=8.97e-04<1e-3, `Finished because |RHS| less than 1e-3`, anode 4.149E+00V, total current 4.832E-14. **4.149V는 이번 실제 로그에서 정상 수렴 확인됨**; 표시가 소수 셋째 자리로 반올림되어 정확한 몇 mV 변화인지는 이 로그로 계산 불가.
- 다음 trial: `Computing BE-step from 0.829862 s to 0.829867 s (Stepsize:4.6596e-06s)`; Newton iteration2-9 RHS around 1.28e-3–1.34e-3 (criterion 1e-3), reported C-norm error alternating ~1.21e3 and 4.76e3. Tail 끝에 iteration9까지만 나타나서 **그 step 수렴 여부, 컷백 여부, 프로세스 현재 구동/최종 종료 상태는 이 스냅샷만으로 미확정**. `Step-size is too small`/Abort/Finished simulation 등 최종 실패 출력 없음.
- 5V 목표 대비 4.149/5=82.98%은 **전압 스윕 비율, 연산 시간 비율 아님**. CAL 5V ETA 근거 부족; CAL이 현재도 CPU 소비 중이라는 것은 로그 스냅샷만으로 확정 못 함. 4V 기준점 과학적 채택 여부는 별도 J/IQE Gate0로 판단, 그냥 4V 도달했기 때문에 중단하면 안됨.
- NEXT: 기존 CAL 그대로 보존, 필요 시 일정 시간 뒤 `tail -n 60 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.log` 재확인해 다음 step accepted/bias progression/step-cutbacks 확인. FAST_C1 실패와 혼동하지 말 것. Server code/CAL process user action 없음.

## 2026-10-10 ~22:11 KST — CAL 100ns n2 accepted ~4.149V; next step Newton oscillatory (OBSERVED LOG)

- **Evidence:** 이택규 실서버 `CMP_BASELINE_1.2.0_CAL/n2_des.log` latest 60 lines shared. BE from 0.829858 to 0.829862 s (stepsize 3.8830e-06s), iter2 `|Rhs|=8.97e-04 < RHSMin 1e-3`, `Finished, because... |RHS| less than 1.0000E-03`; anode=`4.149E+00 V`, total current=`4.832E-14` (2D A/um convention). **Thus 4.149 V was accepted**, not just being attempted. Next BE 0.829862→0.829867s (trial 4.6596e-06s), Newton iter2–9 oscillates RHS ~1.28–1.34e-03 (>1e-3), no eventual convergence/failure outcome in this truncated tail.
- Voltage fraction 4.149/5≈82.98% is **bias sweep fraction, NOT runtime progress**. Step2 completed in 86.24s vs earlier 13.67s; no reliable 5V ETA. Note previous accepted iteration still reports `error=1.11e+03` alongside small RHS, so examine numerical convergence robustness before claiming high-accuracy physical solution.
- Preliminary magnitude under parent-model width convention 2um: J~4.832e-14/2*1e8≈2.416e-6 A/cm² **conditional**; this is a transient total terminal current including possible displacement, not directly accepted as steady-state LED J. Cannot compare blindly against 5V_TEST parent's 5V result because voltage and SRH lifetime differ; low-current physical validation unresolved.
- NEXT read-only: inspect later CAL log and retained PLT 4V+ sweep only as useful; do NOT abort/modify/restart CAL just because 4V was exceeded. 4V is not an automatic verified working baseline. Preserve old 5V parent, project A/B NO-GO.

## 2026-10-10 — Discussion: 4 V vs 5 V CAL endpoint (TECHNICAL ADVICE, NO DECISION TO STOP)

- 이택규 질문 `왜 꼭 5V야? 4V이면 안 돼?`에 5V는 microLED 공통 필수 전압이 아니라 검증을 위해 선택한 high-bias endpoint임을 설명. 4V도 실질 주입/재결합/타당한 동작 J, IQE와 matched-J A/B 비교가 확보되면 SCIENTIFIC operating point 가능.
- 기존 completed parent 5V에서 nominal J~7.24e-4A/cm², QW Rrad share~0.1095%라는 low-drive issue 있으므로 4V로 내린 것만으로 baseline valid 해지는 것은 아님. 별도 CAL (100ns SRH)에서 바이어스별 terminal J를 검토해 보는 것을 제안함.
- CAL user-reported ~4.149V, acceptance not yet verified. 4V step의 log/plt, saved 4V TDR/checkpoint availability를 검증하기 전 계산 중단하지 말 것. User 승인/서버 변경 없음.


## 2026-10-10 — CAL n2 ~4.149V progress (USER REPORT, accepted step not verified)

- 이택규가 별도 100ns sensitivity run `CMP_BASELINE_1.2.0_CAL` n2의 현재 표시 전압이 약 **4.149 V**라고 보고. 이전 사용자 보고 ~4.144V, 이전 실제 로그 accepted ~4.142V 대비 표시 기준으로 최대 +0.007V. 5V sweep 기준 82.98%이지만 **wall-clock/progress 퍼센트가 아님**. **4.149V가 accepted BE step인지는 최신 실제 log 미확인.** 계산 시간 및 완료 ETA 추정 근거 없음.
- NEXT read-only: `tail -n 60 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.log` 를 실서버에서 실행, accepted/rejected step, timestep, actual anode voltage와 수렴 상태 확인 후 ETA 판단. CAL abort/restart/수정 금지.

## 2026-10-10 — LeeTaekGyu decision: do not idle for CAL; parallel low-current baseline Gate0 using existing data (PROPOSED)

- 작업자 이택규가 `그냥 CAL 돌아가기 전까지 기다리는 게 나을까?` 요청. 답: CAL 100ns sensitivity is independent of physical baseline validity. Continue current CAL unchanged and periodically review **accepted** BE time/bias and cutbacks; do not abort/reset or run FAST again merely by schedule. CAL user last reported attempting ~4.144V, last provided actual accepted n2 log ~4.142V; no newer status in current chat.
- Existing completed 5V_TEST, model current ~1.448e-11 A/um, nominal J~7.24e-4 A/cm², MQW Rrad share ~0.1095%. EBL/transport injection and active operating-current range unresolved. More repetitive manual SVisual screenshots not needed; now prioritize quantitative assessment from already obtained band/quasi-Fermi and carrier density data before authorizing any new pilot or physics changes.
- **IMPORTANT freshly read collaborator JuSubin records** (~2026-10-10 21:57 KST): at `Clean_pGaN` (X=.05um,Y=1um), Ev=-5.130097037559 eV, EFp=-4.999999973858 eV, hDensity=3.00034279e17 cm^-3, EFp-Ev=.13009706 eV. At `Clean_EBL` (X=.13um,Y=1um), Ev=-5.252508407140 eV, EFp=-4.999999939039 eV, hDensity=5.787900714824e15 cm^-3, EFp-Ev=.25250847 eV. Ratio of holes ~51.84, local gap difference ~.1224114eV. These are **two local-point observations**, NOT EBL barrier height nor proof low-J cause. Avoid duplicating JuSubin's probe work. Both probes nominal 5V_TEST TDR; current-state proof for exact TDR saved bias per snapshot remains a separate validation check even though archival 5V log shows successful 5V endpoint.
- PROPOSED NEXT decision gate: cross-check archived n2 final bias/TDR state if needed, use existing Ev(x),EFp(x), carrier/current/polarization data to discriminate actual transport bottleneck. If existing data are insufficient, design a **separately cloned low-cost 1D or targeted pilot** with one physics variable at a time, user approval before Run and calibrated target J–V from literature. A/B full DOE remains NO-GO until physical operation established.
- No code/server job change. GitHub planning update only.

## 2026-10-10 — successful 5V_TEST Thermionic vs Piezo model log context inspected (OBSERVED; no physics bug proven)

- 이택규가 성공한 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` lines 345–425 실제 서버 출력을 제공. 셸 첫 입력이 두 `sed` 명령이 합쳐져 `.../n2_des.logsed` 파일 에러를 출력했으나 **뒤따른 동일 출력으로 필요한 본문을 정상 확보**, TCAD 자체 오류와 무관.
- 실제 물리 모델 설명: `With Thermionic Emission at heterointerfaces for electrons and holes` 바로 아래 `Without Piezo`; 별도 항목 `Without polarization` (line373), `Piezoelectrice Activation = 1` (line379), `Piezoelectric polarization model: strain` (line416), `With default parameters from file`, 이어 `Clean_pGaN` region override `With incomplete ionization` (line425 onward). 또한 이전 grep line803 `ThermionicEmission: Formula = 1, instead of: 0 [1]`. **Formula1 인식/이종계면 thermionic 켜짐 확정.**
- `Without Piezo`는 ThermionicEmission 하위 옵션 문맥에 있고, `Without polarization`는 strain piezo 모델 자체 상태와 구별해야 하는 별도 물리 설정 출력으로 보임. **근거만으로 실제 interface polarization charge 분포가 올바르거나 전역 piezo가 OFF라는 결론 불가**. No Piezo file도 model OFF 증거가 아님. 파라미터/분극 값을 수정하지 말 것.
- 계산 성공한 5V_TEST의 low J (~7.24e-4 A/cm2 nominal) 물리 원인 remains UNRESOLVED. Alias Plot deprecation warnings nonfatal. Next rather than repetitive grep/screenshots, use existing band, quasi-Fermi & density observations to prioritize a targeted quantitative injection/transport audit (exact layer boundary/QF drops and effective polarization charge); new experiment only after validated causal hypothesis and user approval.
- No server/TCAD code/CAL job changes.

## 2026-10-10 — completed 5V_TEST n2_des.log confirms ThermionicEmission Formula=1, piezo strain model (OBSERVED)

- 이택규가 실서버 `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/n2_des.log`에서 `grep -niE 'thermionic|polariz|piezo|warning|unrecognized|unknown' ... | head -n 60` 출력 제공. 354행 `With Thermionic Emission at heterointerfaces for electrons and holes`; 803행 `ThermionicEmission: Formula = 1, instead of: 0 [1]`. 기존 Claude 의심(`Thermionic` 파라미터 섹션명 불일치로 Formula1 적용 안 될 가능성)은 이 실행 로그에 대해 사실상 배제. Thermionic 수송 자체의 충분성은 미검증.
- 379행 `Piezoelectrice Activation = 1`, 416행 `Piezoelectric polarization model: strain`; 반면 355행 `Without Piezo`, 373행 `Without polarization`도 있어 서로 다른 model/section context 확인 전 전역 분극이 모두 켜지거나 꺼졌다고 단정 금지. 293행 `no Piezo file`은 곧바로 오류로 해석 금지.
- 2148행 `WARNING: Doping concentration (Nnet) will be recalculated because of incomplete ionization!`은 알려진 Mg incomplete-ionization 적용 메시지; 574/583/585/587/589행은 Plot alias deprecation warnings, 현재 low current/root solver failure 원인 증거가 아님. NEXT read-only: `sed -n '345,425p' .../n2_des.log`로 분극 문구가 속한 블록 문맥과 물리 scope 확인. 서버 SWB 파일/계산 CAL/FAST 변경 없음.

## 2026-10-10 — 5V reference SVisual qualitative band/carrier screening completed; stop repetitive GUI work (OBSERVED / DECISION)

- Worker 이택규 submitted final SVisual screenshot of JUSUBIN_FAST_HALF_5V_TEST n2_des.tdr, existing C1 cutline at lateral Y≈2um, vertical X=0–0.4um. Two variables selected: eDensity and hDensity, simultaneously plotted log scale Y 1e6–1e20 cm^-3. p-side holes dominate (red), n-side electrons dominate (green), MQW multi-peak density profiles show both carriers in different narrow wells/regions. **Colors inferred from previously displayed hDensity, legend not visible; figures approximate.** These are expected general p/n trends and insufficient to identify injection bottleneck alone.
- Previous GUI session also recorded Ec, Ev, eQuasiFermiEnergy, hQuasiFermiEnergy in same cutline at 5V. User requested stopping repeated screen tasks ('언제까지 해야해'); AI agreed SVisual qualitative screening is **complete for now**, no more incremental GUI screenshots requested. This is not a validated physical baseline, nor proof of cause behind exceptionally low nominal 5V current density.
- Next decision work: summarize existing data, identify which exact numeric region/voltage-loss values would discriminate polarization/EBL/contact/MQW injection hypotheses; focus original 5V TDR and actual model. Avoid repetitive manual plotting, unnecessary long simulations, FAST rerun or CAL editing.

## 2026-10-10 — 5V_TEST hole-density log plot fixed to 1e6–1e20 cm^-3 (OBSERVED screenshot)

- 이택규가 동일한 SVisual 스크린샷 두 장 제공. `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`의 C1 (lateral Y≈2.0µm), 깊이 X=0–0.4µm에서 이전에 사용자 선택했다고 보고한 `hDensity` cutline의 Y축을 `Log. Scale=ON`, `Fixed Min=1e6`, `Fixed Max=1e20`으로 성공적으로 설정함. 화면상 p-GaN 상단 X≈0–0.11µm에서 약 1e17cm^-3 농도 평탄부, X≈0.12µm에서 큰 정공 농도 피크, X≈0.14–0.26µm EBL/MQW 인접 스택에서 좁은 양의 피크와 깊은 골 반복, X≈0.27µm 이후 1e6 이하로 범위 바깥. 정량값·피크 region assignment는 그래프 육안 개략치, 단독 screenshot에 변수 legend는 없음.
- 관찰은 `정공이 MQW에 전혀 없다`를 지지하지 않음; 일부 좁은 구간에서 고농도 존재. 장벽에서의 낮은 정공 농도는 통상 quantum well carrier confinement과 과도한 주입 장벽 모두 가능한 해석이므로 원인 미확정. NTSide0 5V 매우 낮은 J의 물리 원인 진단에는 같은 위치 eDensity와 region-specific e/h probe를 비교해야 함.
- NEXT GUI read-only: `Data Selection`으로 가서 C1의 `eDensity`를 추가(다중 선택 Ctrl)하거나 단독 표시해 1e6–1e20 로그 Y축과 함께 스크린샷 제출. 기존 hDensity 그래프 내용 보존 권고. 학교 서버 코드·실행 중 CAL 변경 없음.

## 2026-10-10 — 5V_TEST SVisual apparent hDensity vertical cutline viewed in linear scale (OBSERVED screenshot)

- 이택규가 성공한 JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr, lateral C1 Y≈2.0 um, X depth 0–0.4 um에서 hDensity로 변경했다고 보고한 후 SVisual 스크린샷 제출. 그래프 Y축은 선형이고 0, 2e19, 4e19 등의 눈금 및 X≈0.12um, ≈0.25um에서 날카로운 큰 피크가 관찰됨. 변수 legend는 표시되지 않아 그림만으로 실제 hDensity임을 독립 입증하지 못함. 큰 동적 범위 때문에 다른 위치 농도가 0 부근에 눌려 보여 EBL/MQW carrier injection 원인은 이 화면만으로 확정 불가.
- NEXT GUI read-only: 오른쪽 1D plot의 **Y축 숫자** 더블클릭해 Axis Properties Y의 Log. Scale 체크, Min/Max Fixed 해제(auto), X=0–0.4um 유지. 로그 그래프와 curve 변수/단위 확인 후 정공 분포 해석; 필요시 probe 수치 및 eDensity 비교. 서버/SWB 계산/진행 중 CAL 변경 없음.

## 2026-10-10 — SVisual 5V_TEST 4-band (Ec/Ev/Fn/Fp) cutline overlay confirmed (OBSERVED SCREENSHOT)

- 이택규가 성공한 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`의 Y≈2.0µm C1 깊이 X=0–0.4µm에서 `ConductionBandEnergy`(red), `ValenceBandEnergy`(green), `eQuasiFermiEnergy`(blue), `hQuasiFermiEnergy`(cyan) 네 개 곡선을 동시에 표시한 SVisual 화면 공유.
- 그래프상 p-GaN (X≈0–0.12µm) Fp는 Ev와 간격 존재; QW/EBL (X≈0.12–0.27µm) Ec/Ev와 Fn/Fp에 급격한 단계 변동; nGaN (X>≈0.27µm) Fn는 Ec 부근. **근본 원인/장벽 높이/실제 injection efficiency는 아직 미확인**. GUI 스크린샷 육안 관찰이므로 수치 전압분배 단정 금지.
- NEXT: 그래프 보존 후 동일 C1의 `hDensity`를 별도 단독 표시(logarithmic positive y-axis)해 p-GaN/EBL/MQW 정공 분포를 관찰, 이후 `eDensity` 등 비교. 서버 원본, CAL, FAST_C1 변경 없음.

## 2026-10-10 — SVisual existing 5V reference Ev 0–0.4 µm profile observed (OBSERVED screenshot)

- 작업자 이택규가 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`의 Y≈2.0 µm 내부 cutline C1에서 `ValenceBandEnergy(C1(n2_des))` 1D 곡선을 X=0–0.4 µm 깊이 범위로 실제 표시한 SVisual 스크린샷 제출. 값은 p-GaN 상단 x≈0–0.12 µm Ev≈-5.2 eV 주변 plateau, EBL/MQW 구간 x≈0.12–0.27 µm에서 급격히 변동하고 x>≈0.27 µm nGaN에서 대략 -3.5 eV 수준 평탄부(모두 **화면 육안 개략값**이며 Probe 수치가 아님).
- 오른쪽 1D plot legend에는 **ValenceBandEnergy 하나만** 존재하며 이전 `ConductionBandEnergy` 곡선이 Ev로 교체된 것으로 보임. 이전 AI의 '더블클릭하면 곡선 추가' 단정은 현 GUI 동작에 맞지 않았음. 현재 두 곡선을 함께 오버레이했다는 주장은 하지 않음.
- NEXT GUI read-only: 화면 왼쪽 아래 `Data Selection` 탭으로 돌아간 상태 스크린샷을 받아 vT-2022.03 실제 UI에서 두 band curves를 함께 표시하는 기능을 확인. 이후 e/h QuasiFermiEnergy 및 도핑/분극과 함께 주입장벽을 평가. 에너지 요철만으로 저전류 근본 원인을 단정할 수 없음. 학교서버 CAL/FAST/5V 데이터나 물리 코드 미변경.

## 2026-10-10 — 5V Half+Coarse SVisual ConductionBandEnergy vertical cutline created (OBSERVED screenshot; interpretation pending)

- 이택규가 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`를 SVisual T-2022.03에서 열고 `ConductionBandEnergy`를 선택, 물리 도메인 X=세로 약 0–4.6 µm / Y=가로 약 0–2.5 µm 중 Y≈2.0 µm에 수직 Cutline C1을 생성. 화면 왼쪽 2D 소자 내 C1 검은 수직선, 오른쪽 `Cutline_Y Plot`에 빨간 `ConductionBandEnergy(C1(n2_des))` 1D 곡선 실제 표시. 메쉬 65,513 points / 138,194 elements, 과거 보관된 결과와 일치.
- 현재 우측 1D 전체 깊이 0–4.6 µm를 표시해 활성층·EBL·pGaN의 x≈0–0.4 µm 에너지 변화가 좌측에 압축되어 있음. 이 화면만으로 저전류 근본 원인 또는 EBL 장벽 높이를 확정할 수 없음.
- NEXT UI READ ONLY: 우측 1D x-axis Axis Properties Main에서 Min=0 Max=0.4 µm linear/fixed로 범위 확대 후 스크린샷; 이후 동일 C1에 ValenceBandEnergy, e/h QuasiFermiEnergy 등을 함께 표시·자료 추출. TCAD 코드 또는 CAL 실행 변경 없음.

## 2026-10-10 — Claude v2 independent CMP audit submitted; low-current Gate 0 prioritized (DOCUMENT-BASED REVIEW / PROPOSED)

- 작업자 이택규가 Claude 작성 `CMP MicroLED TCAD — 독립 중간 기술감사 및 연구계획 재수립 (v2)` 전문을 채팅 업로드함. **Claude의 독립 감사 의견이며 이번 메시지는 새 실험/로그가 아님.** Claude는 GitHub 기록과 구 FAST 입력은 보았으나 5V_TEST/CAL 현재 실제 pp/log/TDR을 직접 읽지 못했다고 보고함.
- Claude의 핵심 의견: JUSUBIN_FAST_HALF_5V_TEST NtSide0 5V transient 성공(~10596.76s)에도 raw I2D=1.44801646e-11 A/um, half mesa width≈2um, assumed AreaFactor1이면 nominal J≈7.24e-4 A/cm²; QW Rrad share≈0.1095%. 충분한 구동 전류·주입·IQE 검증이 **Baseline freeze 이전 Gate 0**이 되어야 함. 수치는 기존 GitHub 감사 기반이며 새 측정 아님. `not turned on` 결론은 비교대상 J–V/전류 정규화 검증 전에는 물리 가설로 남김.
- 수용 가능한 점: 5V_TEST 계산 플랫폼 보존, high-bias FAST_C1 n6 ~4.801V step-size failure는 재실행 보류, CAL n2 100ns sensitivity current reported ~4.144V accepted unverified로 관찰·중단 사용자 승인 필수; A/B 동일 J·null controls, τ sensitivity, QW와 Cedge 총 비방사, transient trap DC check, stripe vs 3D 형상 한계 분리.
- 별도 검증 필수: Claude가 제시한 활성층 외 `2.9V drop`은 단일 QW n,p, ni 가정 기반 추정이지 밴드/준페르미 지도에서 측정된 전압 분배 아님. 분극 activation/thermionic/EBL를 저전류 확정 원인으로 판단 금지. FAST half/full ~1% 동일은 4.798 vs 4.801V 단일 단자전류의 근사 보정이므로 메쉬 수렴·공간발광 정확도는 미증명. 2D stripe perimeter/area가 4um square보다 2배 작은 기하학적 사실에서 실제 SRH 2배 과소평가를 단정할 수 없음. 1D pilot 분 단위/10월23일 초록 데드라인/수치 PASS 기준은 Claude의 제안이며 별도 확인 필요.
- 우선순위 제안: **S0 원본 5V_TEST 결과의 구동 전류/J 및 potential/band/quasi-Fermi 분포 점검(기존 TDR)** → **S1 EBL doping/polarization/thermionic interpretation 및 재결합 영역별 전류 회계** → 원인 가설이 분리되면 기존 소자 보존한 별도 소형 1D/pilot 설정 검토(사용자 승인 전 미실행) → NtSide0/1e18 동일 J → A/B. CAL은 보고서의 임의 시간·전압 임계치만으로 중단 결정하지 않음.
- 서버/SWB/코드/CAL 변화 없음. Claude에게 직접 메시지 보내지 않음.

## 2026-10-10 — CAL lifetime setting verification already performed; corrective handoff (USER CORRECTION)

- 이택규가 AI의 재확인 요청을 정정함: 성공한 기존 5V 소자를 복제한 CAL에서 InGaN Scharfetter electron/hole SRH lifetime 1ns→100ns (`taumax=1e-7s`)로 설정하는 작업은 이택규와 ChatGPT가 함께 수행했고 변경 설정 파일도 당시 검토함. 기존 파일 수정 자체를 미검증이라고 반복 질문하지 말 것.
- 구분: 변경을 함께 설정/확인한 기록은 존재하나, CAL 실행 중인 해의 실제 lifetime 효과를 수치적으로 독립 추출해 완전 검증했는지는 별도 문제. 이 차이를 설명할 때 이미 확인한 사용자 작업을 부정하거나 기초 단계로 되돌리지 않음.
- 현재 우선 연구 질문: 왜 동일 Half+Coarse 부모(5V 성공)에서 lifetime만 100ns로 의도적으로 바꾼 CAL이 4.144V 부근에서 고전압 Newton 수렴 병목을 보이는가? 원인 미확정. CAL 원본/run 보존, accepted BE pseudo-time·스텝만 읽기 전용 분석, 물리 메커니즘 및 수치 반응 구분.

## 2026-10-10 — CAL n2 ~4.144 V calculating (USER-REPORTED / ACCEPTANCE UNVERIFIED)

- 작업자 이택규 직접 보고: `CMP_BASELINE_1.2.0_CAL`이 현재 약 **4.144 V 계산 중**. 직전 실제 공유 n2 로그에서 확인된 accepted 전압은 4.142 V; 이번 보고는 이전보다 약 0.002 V 높은 시도/진행으로 보이지만 **새 n2_des.log 스텝 수렴 결과는 제출되지 않아 4.144 V accepted라고 확정할 수 없음**. 5V/100ns effective 적용 모두 미확인.
- 시간당 속도, 최종 종료 예상, 근본적인 고전압 수렴 문제의 동일성은 아직 판단 불가. 현재/목표 전압 비율은 ≈82.88% *스윕 구간*일 뿐 시간 진행률 아님.
- NEXT: 기존 CAL 작업 그대로 보존, 현재/이후 `n2_des.log`의 accepted t/V, Newton 컷백, timestep, 최소 간격 경고 비교하는 읽기 전용 감시. CAL 임의 Abort·Reset·파라미터 수정하지 않음. 최근 FAST_C1 4.801 V MinStep 실패는 별도 사례.

## 2026-10-10 — 이택규 Claude 독립 기술감사 요청 준비 (HANDOFF / PROPOSED)

- 사용자가 기존 성공한 NtSide0 5V Half+Coarse (wallclock 10596.76s), FAST_C1 n6 4.801V MinStep 실패(wallclock 525152.85s), CAL InGaN 100ns 후보 ~4.142V 고전압 수렴 병목 차이를 의문으로 제기하고, Claude와 중간 기술감사/향후 로드맵 검증을 요청함.
- ChatGPT는 세 프로젝트가 동일한 계산이 아니며 FAST_C1은 수치 설정/메쉬 및 geometry 조건 차이, CAL은 InGaN SRH tau_max 변경 시도 등의 후보 요인을 구분함. 특정 고전압 수렴 실패의 근본 원인은 아직 확정하지 않음. 새 실제 로그 없음. 사용자에게 Claude용 비판적 독립감사 프롬프트 제공(실제 GitHub 소스·학교 서버 preprocess 비교, low J, SRH, Mg, solver, symmetry, GO/NO-GO 및 일단 READ ONLY).
- NEXT: Claude 독립감사 결과 및 사용자가 제공한 실제 diff/로그와 대조 후 결정. 실행 중 CAL을 Abort/Reset/코드변경하지 않음. 완료 5V_TEST와 FAST 로그 보존. Claude에게 직접 메시지 송신 아님.

## 2026-10-10 — CAL 4V+ 수렴 불안정 우려에 따른 판단 보류 및 감시 계획 (PROPOSED)

- 작업자 이택규가 FAST_C1 n6의 약 4.801V 실패와 CAL n2의 약 4.142V 부근 반복 Newton 문제를 비교하면서 CAL 실패 위험에 대한 우려를 표시. 이후 즉시 contact 좌표 확인을 멈추고 CAL 리스크를 우선 재평가하기로 대화 방향 변경. **CAL 중단(Abort)은 요청·실행되지 않음.**
- 실제 확인: FAST_C1은 Iterations15, MinStep1e-9 하에서 Step-size too small로 실패; CAL은 최근 accepted anode 약 4.142V까지 전진했으며 후속 RHS 1.03e-3~1.09e-3 근방에서 수렴 기준 1e-3 위로 반복한 구간 관측. 이 두 계산의 근본 원인 동일 여부·CAL 최종 실패 여부·100ns 유효 적용 여부 불명.
- NEXT READ ONLY: CAL n2 실제 상태를 서로 시간 간격을 둔 두 로그로 비교. `anode` 마지막 accepted 전압뿐 아니라 BE pseudo-time, step size/retry 추세, log 수정 시각 및 solver running 여부 확인. 전진하면 유지, 정체 + 극소 스텝 반복이면 중단/짧은 pilot 분기 여부를 연구자가 결정. 5V parent를 별도 보존, FAST_C1 즉시 재실행 금지. TDR은 검증된 restart 체크포인트가 아님.

## 2026-10-10 — Half+Coarse completed 5V reference top/bottom contact placement logic verified from live pp1 (OBSERVED; actual mesh edge IDs pending)
- 작업자 이택규가 원본 `JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd` lines 420–500을 실서버 출력으로 제공. SDE는 `sdegeo:define-contact-set "anode"` 및 `"cathode"`를 정의.
- Anode `sdegeo:set-contact`는 x=`x0`에서 y=`(yL+yDL)/2` 및 y=`(yDL+yC)/2`의 **두 top edge ID**를 동일 `"anode"`로 등록함. 소스 주석에 Half top consists of DmgL + Clean이라고 명시. Cathode는 x=`xb`, y=`yC/2`인 bottom n-GaN numerical/contact base edge를 `"cathode"`로 등록.
- 이 근거는 Half-device에도 양 전극이 남아 있고 top/bottom 전류 경로를 의도했음을 확인함. 하지만 `x0,xb,yL,yDL,yC` 실제 정의/수치, 접촉 edge 선택의 유효성, 기하학적 중앙대칭/측벽 위치, 최종 mesh/전류밀도 정규화는 **미검증**. 코드의 주석이나 `find-edge-id` 선언만으로 실제 경계검증 완료 주장 금지.
- 다음: `grep -nE 'define (x0|xb|yL|yDL|yC)' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd`의 실제 좌표 확인, SVisual 메쉬에서 contact 위치 확인. 시뮬레이션/입력 수정 없음.

## 2026-10-10 (user terminal capture, exact time unspecified) — Confirmed completed 5V half-device TDR exists (OBSERVED / READ-ONLY)

- 작업자 이택규가 실제 학교 서버에서 `ls -lh /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` 실행. 출력: `-rw-r--r--. 1 semi437 semi437 16M Oct 9 14:29 .../JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`. 완료된 NtSide=0 5V Half+Coarse baseline parent의 postprocessing 결과 파일 존재와 대략적인 크기/수정일만 **실제 확인**.
- 별도 과거 `n2_des.log`와 PLT 분석에서 해당 부모 5V Transient 종료까지 확인되었으나, **이번 ls 명령만으로 TDR 내부 데이터 완전성, electrode mesh, centerline symmetry, 5V steady state, 공정/물리 모델 타당성은 증명되지 않음**.
- NEXT (READ ONLY): 부모 `pp1_dvs.cmd`의 `sdegeo:*contact*`, `anode/cathode`, `pp2_des.cmd`의 Electrode 설정과 실제 `n1_msh.tdr`를 대조해 Half에서 양 전극 및 한쪽 sidewall과 중앙 대칭면이 존재하는지 검증. 이후 QW Rrad/RSRH/RAuger 전체 적분과 2D current normalization. 완료 parent TDR, FAST_C1 실패 로그, 실행 중 CAL 모두 원형 보존.
- GitHub 기록만 업데이트. 서버 코드 및 실행 변경 없음.

## 2026-10-10 — 이택규 Baseline-first / A·B stage-gated execution roadmap (PROPOSED; team approval pending)

- 작업자 요청: FAST_C1 실패·CAL 지연과 별도 완료된 5V Half+Coarse를 바탕으로 향후 연구 실행 계획 작성. **사용자 승인 전 계획안(PROPOSED)** 이며 소스/solver 변경 또는 연구 결론 확정 아님.
- P0 (즉시, 읽기 전용): `JUSUBIN_FAST_HALF_5V_TEST` 5V NtSide0 완성 파일/로그/원시 입력·해시/백업 보존. `GaN_PiN_Diode_FAST_C1` n6은 4.801V에서 15 Newton 회수·MinStep=1e-9로 실패: 재실행 보류, 기존 중간 TDR 활용/원인 비교. CAL n2는 마지막 실측 4.142V accepted, NtSide0 InGaN 100ns 후보: 원본 보존, 현재 상태·effective par·accepted step 추적.
- P1 (장시간 계산 전): Half-도메인 실제 anode/cathode/대칭면 및 측벽 메쉬 검토, 2D current→J 정규화, Mg/EBL 도핑과 hDensity 구분, 5V steady-state/초기입력, 극단적 낮은 전류 및 1ns QW SRH·B·C와 polarization 모델 물리성 점검. 기존 5V TDR에서 전체 QW별 Rrad/SRH/Auger와 sidewall SRH를 동일 도메인/단위로 적분해 IQE_rec workflow 입증.
- P2 (기준 소자 확정): 동일한 freeze physics+mesh에 NtSide=0 vs 1e18 defect ON/OFF 모델, 전류 인가·광재결합/전류 밀도 영향 비교; Full/Fine vs Half/Coarse 및 mesh/convergence/일반동작 확인. 100ns CAL은 자료기반의 **분리된 민감도 시험**이고 baseline 과학 검증을 대신하지 못함. 특성이 맞지 않으면 calibration gate NO-GO 유지.
- P3 (A/B): Common Baseline 동결 후 A carbon compensation edge 모델과 B localized lateral AlGaN heterobarrier를 분리 버전으로 설계. 두 프로젝트 각각 null control → SDE mesh → SDevice preprocess → short smoke/Save-Load → representative high-bias pilot → selective DOE. B vertical span/QW replacement과 2D geometry contact, A trap/compensation 정의 사전 확정. 전류밀도 동일 조건의 sidewall SRH, QW Rrad/SRH/Auger, injection/leakage, IQE_rec, Vf penalty 비교. A/B 후보를 baseline 확정 전 생산 스윕하지 않는다.
- P4: 검증을 통과한 후보만 full/fine 재검증 후 PPT/논문, 출처/수치·오류·한계·재현성 SWB-native SDE/SDevice/Parameter 입력 정리.
- 이택규 제안 역할: 수치 수렴·CAL 및 full/half 동등성/재현성, 주수빈 제안 역할: SVisual 도핑/재결합 적분과 출력 검증. **실제 분담 미확정**. 시간은 smoke/pilot wallclock 측정 이전 예측하지 않음.
- 근거: 사용자 제공 실제 pp6_des.cmd, n6 종료 로그, CAL n2 4.142V 로그; CMP/PROJECT_AB_PRE_RUN_AUDIT.md G1~G5 및 Modes 0~4, Issues #1~#6. 변경 사항: GitHub 계획 제안 기록뿐.

## 2026-10-10 (user command output; exact time not given) — FAST_C1 live pp6 Solve-block scope and half-electrode question (OBSERVED / EXPLANATION)

- User-provided exact server `sed -n '815,885p' /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1/pp6_des.cmd`: initial `Coupled(Iterations=500, LineSearchDamping=1e-2){Poisson}`, then initial `Coupled(Iterations=100){Poisson Electron Hole}`; subsequent `Transient(InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Goal anode Voltage=5.0){Coupled(Iterations=15){Poisson Electron Hole}}`. This resolves initial-vs-transient Iterations ambiguity. No separate `Decrement` line within supplied excerpt. The 4.801V `Step-size is too small` outcome is consistent with MinStep1e-9; underlying Newton instability still unresolved.
- User asked if anode/cathode can be omitted/unsimulated for half-domain device. Explanation: Half-domain symmetry reduction does NOT eliminate either electrical terminal; electrodes and full current path must be retained on kept half, with correct symmetry center and surviving physical edge/contact topology. Earlier actual CAL logs have anode/cathode voltage and opposing total currents, supporting presence of both electrodes, but live contact geometry and 2D current normalization/symmetry equivalence are not proven by terminal logs alone. FAST_C1 n6 deck and separate Half+Coarse CAL must not be conflated.
- No new model/input modification or scientific calibration claim; next validation is READ ONLY of active half SDE contact positions/names, mesh boundaries, pp2 electrode File/Physics and mirror condition, then compare full/half matched-current J and QW recombination. Preserve current CAL and prior valid parent.

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

## 2026-10-10 after 19:02 KST — FAST_C1 n6 MinStep failure confirmed; CAL n2 advances to ~4.142 V (OBSERVED LOG)

- 작업자 이택규가 학교 서버 실제 터미널 로그 두 개 제공. FAST_C1 `GaN_PiN_Diode_FAST_C1/n6_des.log` (NtSide=0)는 반복 Newton 15회 초과 후 `Newton didn't converge, trying again with smaller timestep...` 그리고 `Finished, because... Step-size is too small.`가 나타남. 2026-10-10 17:39:07 KST 정상 프로그램 종료 메시지 `simulation finished`, `Good Bye !`, `n6_des.tdr` 쓰기 및 라이선스 반환이 있더라도 5V 목표 달성/물리적 성공이 아니라 **수치적 최소 time-step 실패**. Wallclock 525152.85s ≈145h52m32s, peak mem 5.94GB. 마지막 accepted voltage는 제공된 50줄에 없어 UNRESOLVED; 깊은 원인(물성/mesh/수치 설정) 역시 확정 불가.
- 별개 프로젝트 `CMP_BASELINE_1.2.0_CAL/n2_des.log`에서 t=0.828339→0.828343s BE step은 Newton 2회 후 `|RHS| less than 1e-3`로 accepted, 표기 anode=4.142E+00 V, total current=4.678E-14 raw. 기존 4.138V보다 약 0.004V 진전(4.142/5≈82.84% 전압 구간이지 walltime 아님). 후속 t=0.828343→0.828348s attempt은 Iteration 11까지 `RHS≈1.09e-03 >1e-03`; 스크린샷/로그가 중간에 끝나 아직 accepted/failure 미확인. 5V 완료·tau_max=100ns 실제 유효성·ETA 미확인.
- 변경: GitHub 진단 기록뿐. 학교 서버 소스, SWB, 실행 중 CAL, 완료된 `JUSUBIN_FAST_HALF_5V_TEST` 결과는 건드리지 않음.
- NEXT READ-ONLY: `grep -n 'anode ' /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1/n6_des.log | tail -n 5` 로 FAST 마지막 성공 전압을 확인하고 n6_des.sta/err 및 버전 비교. CAL은 시간 경과 뒤 tail로 accepted t/V, `Newton didn't converge`, step-size, fatal/Good Bye 여부 확인. FAST n6 즉시 재실행 또는 MinStep/Iterations 임의 완화 금지.

## 2026-10-10 ~19:02 KST — FAST_C1 n6 red Failed UI, CAL remains unconfirmed (OBSERVED / UNRESOLVED)

- 이택규가 SWB T-2022.03 스크린샷 제공. 현재 열린 프로젝트는 `GaN_PiN_Diode_FAST_C1`이며 `NtSide=0` SDevice `[n6]`가 빨간색, `NtSide=1e18` `[n12]`은 연파란색, `[n1]` SDE는 노란색. SWB 기본 색상 기준 빨간색=failed, 연파랑=running, 노랑=done. 단 사용자 환경의 색상 커스터마이즈/정확한 종료 원인은 확인 전.
- 화면의 `CMP_BASELINE_1.2.0_CAL`은 왼쪽 프로젝트 목록에 있으나 **선택되지 않아** 실제 n2 상태가 표시되지 않음. 사용자에 따르면 여전히 미완료. CAL 마지막 직접 확인은 ~18:08 KST 4.138 V 부근 Newton cutback; 5V 완료 여부는 미확인.
- 두 프로젝트/노드를 혼동하지 않는다. FAST_C1 `n6_des.log` 및 `.err/.sta` 마지막 구간과 CAL `n2_des.log`를 읽기 전용으로 요청. 기존 실행을 abort/rerun/reset/edit하지 않음. 원인 미확인, 최초 보고 단계.

## 2026-10-10 (after 12:09 KST; exact log capture time not given) — CAL NtSide0 SDevice actually advancing to 4.122 V (OBSERVED LOG, NOT FINISHED)

- Worker 이택규 supplied live command output from `tail -n 40 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.log`.
- Last **confirmed completed** step is `Computing BE-step from 0.824472 s to 0.824478 s`, `Finished, because |RHS| less than 1.0000E-03`. Newton iteration 2 RHS `7.30e-04`; per-step total wallclock 7.39 s. Terminal `anode voltage=4.122E+00`, `anode total current=4.344E-14` in raw output units. If the known 0–5V linear time ramp is unchanged, `0.824478*5≈4.12239 V`. Thus approximately 82.45% of **voltage sweep**, not runtime, complete.
- The **next BE attempt** `0.824478→0.824487 s` at `8.3662e-06 s` shows iterations 0–5; final printed iteration 5 RHS `1.10e-03` above `1e-03` threshold. Its acceptance, cutback, failure or subsequent progress cannot be determined because output excerpt ends mid-iteration.
- **Interpretation:** Real numerical progress verified at least to 4.122 V (stronger evidence than SWB Running). There is a possible Newton convergence slowdown at high bias, not yet confirmed stall/error. 100ns InGaN override **still NOT verified effective** from this excerpt; time-to-finish cannot be projected reliably.
- **Read-only next action:** retain running job and unchanged input; sample log later to check last accepted t/V and repeated 'Newton didn't converge'/step-retry messages; also inspect preprocessed/custom parameter usage only without edits. No source or simulator modification was made by AI.

## 2026-10-10 12:09 KST — CAL SDevice continues running in SWB (USER-REPORTED / LOG UNVERIFIED)

- Worker 이택규 reports that the previously launched `CMP_BASELINE_1.2.0_CAL` SDevice still appears **running** in SWB at ~12:09 KST on Oct 10, with no completion observed.
- Start time described as "어제 새벽 1~2시" (literally Oct 9 01:00–02:00), which would imply 34h09m–35h09m elapsed, but the same CAL project's SDE meshing was previously screenshot-confirmed completed **Oct 10 00:11:50 KST**. A **different interpretation of the date** (Oct 10 01:00–02:00) implies 10h09m–11h09m; therefore actual start date/time is **UNRESOLVED**, and must not be treated as known.
- **SWB running display is user-reported only**; there is no freshly supplied CAL `n2_des.log` or `n2_des.out`, no observed accepted BE steps/current voltage, no proof the 100ns material override was applied, and no reliable ETA. Do not call this a hang or success.
- Next **READ ONLY**: inspect `tail -n 40 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.log` and the SWB job/experiment identity and start timestamp; compare changing accepted-voltage/current and Newton retry patterns. Keep existing run and original completed 5V parent intact; no parameter/source edits while it is running.

## 2026-10-10 — User closes session and applies version policy to both researchers (DECISION)

- 이택규 ended today's work and explicitly requested that **주수빈 also use the CMP semver naming convention for all newly created projects and versioned released files** in future. Confirmed `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>` and made shared policy mandatory in PROJECT_NAMING_CONVENTION.md/AGENTS.md, plus RELAY and team timeline. Existing project names and SWB native filenames stay intact.
- Current CAL SDevice 5V was user-reported launched; no new progress/log/completion checked. No school-server or SDevice changes made during this request.

## 2026-10-10 — Worker authorizes direct 5V CAL sensitivity run, skipping additional short smoke (DECISION / NOT YET LAUNCHED)

- Worker 이택규 explicitly requests starting the already prepared `CMP_BASELINE_1.2.0_CAL` at 5 V now rather than further serial verification. Assistant agrees it is defensible as an **exploratory 100ns InGaN SRH sensitivity trial**, NOT publication-grade certified baseline.
- Gates already OBSERVED: original JUSUBIN_FAST_HALF_5V_TEST NtSide0 Half+Coarse succeeded 5V with same SDE/SDevice source hashes; new cloned SDE user reports yellow `done`; cloned custom `FASTC1_pp6_des.par` now displays InGaN Scharfetter `taumax=1e-7,1e-7 s`; cloned SDevice File still explicitly `Parameters = "FASTC1_pp6_des.par"`. Physical lifetime application must be checked in new runtime log; no new SDevice simulation has yet been confirmed started or completed.
- Immediate direction: SWB select only `NtSide=0` SDevice node and RUN, which should preprocess automatically; inspect first generated `pp2_des.cmd` and early `n2_des.log` for custom `.par` load and InGaN material model parse. If error appears, pause and diagnose. Observe full 5V transient run may take hours and has only final Save/Plot, so no intermediate checkpoint/restart expected. Preserve old 5V_TEST/Full reference. After completion compare I(V), QW Rrad/SRH/Auger, 2D J, numerical convergence; physical parameter and full/half validation still open.

## 2026-10-10 — CAL SDE node now reports DONE in SWB (USER-OBSERVED)

- 이택규 explicitly confirms yellow `done` status for the SDE node in `CMP_BASELINE_1.2.0_CAL` after prior SDE GUI `Meshing successful` at 00:11:50 KST. Thus SWB SDE workflow step is reported completed, not merely internal mesh command.
- This is NOT proof SDevice has run nor material 100ns parameter has been parsed by SDevice. Next action: in SWB open Project > Operations > Preprocess (Ctrl+P) **only**, do NOT Run. Check preprocessor success and generated CAL `pp2_des.cmd` parameter reference plus on-disk custom `FASTC1_pp6_des.par`; actual effective tau_max must be confirmed via SDevice log on short smoke before 5V production.
- Preserve SDE DONE node, original 5V_TEST, project inputs. Source: user statement, not independently fetched SWB log.

## 2026-10-10 — CAL project SDE editor reports successful meshing (OBSERVED; SWB node/file gate pending)

- Worker 이택규 supplied SDE GUI screenshot titled `n1_dvs.cmd - Sentaurus Structure Editor@ssudisu3 T-2022.03` for `CMP_BASELINE_1.2.0_CAL`. Scheme Commands pane visibly displays `Meshing successful`, `End Time: Sat Oct 10 00:11:50 2026` (Start 00:11:28), with half-device cross-sectional geometry displayed. This is direct evidence the SDE mesh-generation command returned success inside the editor, NOT proof that the SWB node status has turned DONE, exact `n1_msh.tdr` was emitted in intended project, or SDEVICE calculated 5V.
- Next READ ONLY: `ls -lh /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n1_msh.tdr` to check on-disk mesh and timestamp, then check SWB SDE node Done and preprocess SDEVICE, confirming effective 100ns InGaN from custom .par before the 5V run. Keep completed parent unchanged.

## 2026-10-10 — User defers SWB-native parameter migration; run current CAL pilot first (DECISION)

- Worker 이택규 explicitly decided: for the **current** `CMP_BASELINE_1.2.0_CAL` candidate, keep its existing working input route `sdevice_des.cmd` File `Parameters="FASTC1_pp6_des.par"` and material-specific InGaN Scharfetter tau_max=1e-7s both carriers already added to that custom .par; **do not migrate now** to `sdevice.par` or `Parameters="@parameter@"`. The SWB-native standard copy/paste method is planned for the **next new device/project**.
- User wants to run current trial promptly. In clone SWB screen SDE and SDEVICE had `--`; no local SDE mesh has been proven generated, and no CAL SDevice preprocess/run log yet. Recommendation: run cloned SDE first and verify mesh, preprocess SDevice and inspect actual new custom par and effective Scharfetter 100ns in pp files/log, then allow existing unchanged NtSide=0 0–5V Transient-BE candidate (no unvalidated QS). Save and audit actual output. This is the user's decision to start work, NOT an observed simulation completion or launch; ChatGPT has no school server execution access.
- Keep completed `JUSUBIN_FAST_HALF_5V_TEST`, original backup and Full/Fine reference untouched. New solver results must be evaluated for the previously observed very-low current and 2D J uncertainty; do not claim physical calibration from 100ns trial.

## 2026-10-10 — Professor-facing SWB reproducibility requirement; migrate custom par to native SWB input (DECISION / PROPOSED MIGRATION)

- Worker 이택규 wants code/parameter copy-paste **within SWB** for CMP presentation/professor to reproduce; professor may inspect/run inputs. Observed cloned CAL `sdevice_des.cmd:22 Parameters = "FASTC1_pp6_des.par"`, `line 68 DefaultParametersFromFile` (live user grep). Current solver depends on custom external file, so copying only SDE and SDEVICE command inputs into another project is NOT self-contained and risks a missing/wrong file.
- Official Sentaurus training `https://ghzphy.github.io/Sentaurus_Training/sd/sd_10.html` and SWB tutorial `https://ghzphy.github.io/Sentaurus_Training/swb/swb_07.html` confirm SWB standard common input `sdevice.par`, expansion `File { Parameters="@parameter@" }` to preprocessed `ppN_des.par`; GUI `Tool > Edit Input > Parameter` edits the SWB parameter input.
- Proposed portability workflow (NOT applied): preserve backup/source and completed parent; inspect existing cloned `sdevice.par` first (could contain unrelated/default blocks), then in cloned `CMP_BASELINE_1.2.0_CAL` replace its full contents with the validated custom `FASTC1_pp6_des.par` including original LatticeParameters, Thermionic, GaN Mg ionization and InGaN Scharfetter tau_max=1e-7 s both carriers; modify clone `sdevice_des.cmd` File/Parameters to `"@parameter@"` using SWB Edit Input Commands. Preprocess-only and compare `ppN_des.par`, `ppN_des.cmd`, runtime effective model BEFORE any solver run. The 100ns is nominal max, concentration-dependent with Nref/gamma, not globally constant effective lifetime.
- Deliver professor reproducible project as SWB **three input blocks** SDE + SDEVICE + sdevice.par, parameter table NtSide/conditions, project parent and hashes; source comments and references; do not claim two text blocks alone suffice. No migration/solver executed yet.

## 2026-10-10 — CAL clone InGaN Scharfetter 100ns saved on school server (OBSERVED)

- Worker 이택규 ran `tail -n 15 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/FASTC1_pp6_des.par`; actual output now includes newly appended `Material = "InGaN" { Scharfetter { taumin = 0,0; taumax = 1e-7,1e-7; Nref = 1e16,1e16; gamma = 1,1; Talpha = 0,0; Tcoeff = 0,0; Etrap = 0; } }` after existing GaN block.
- Therefore **remote cloned .par file modification is observed**, not merely proposed. Original successful 5V_TEST, new cloned SDE/SDevice source and central MaterialDB remain untouched as far as visible. No SWB preprocessing, runtime log confirmation of material-specific override, pilot or 5V CAL run yet. Trailing '}' with no newline is minor formatting, not automatically a syntax error.
- Independent archived successful parent `sdevice_des.cmd` references `Parameters = "FASTC1_pp6_des.par"` and `Grid="@tdr@"`; new cloned copy previously matched parent hash. Need validate exact new active deck with read-only grep then SWB preprocess of cloned project, correct physics recognition, and separate truly short Transient-BE smoke before full 5V.

## 2026-10-10 — CAL InGaN override STILL absent from server .par (OBSERVED)

- Worker 이택규 executed read-only absolute path `tail -n 18 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/FASTC1_pp6_des.par`. Output showed end of existing GaN Mg Ionization Species block and final closing braces only. No appended `Material = "InGaN"` / Scharfetter override appears at EOF.
- Prior errors in home directory resulted from wrong current directory and accidentally pasting terminal prompt/output; no TCAD syntax error or simulation failure evidenced.
- Assistant asked worker to return to MobaTextEditor editing live candidate par, Ctrl+End, append the InGaN Scharfetter tau_max=1e-7s both-carrier block, Ctrl+S and approve upload, then repeat read-only absolute-path tail. There is no evidence edit/save occurred yet. Keep original completed 5V_TEST and clone backup untouched; do not preprocess/run until file verified.

## 2026-10-10 — Windows archive viewer mistaken for active CAL source path (OBSERVED / CORRECTED)

- Worker 이택규 shared screenshot of Windows File Explorer within MobaXterm RemoteFiles temporary view of `CMP_BASELINE_1.2.0_CAL_AUDIT.tar`, displaying archived `FASTC1_pp6_des.par` and other old 5V files. This is **not** the editable live SWB candidate directory. No manual edit of the live 100ns parameter was evidenced by this screenshot.
- Corrected workflow: use MobaXterm live SFTP navigator to `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/`, open `FASTC1_pp6_des.par` there; preserve existing GaN Mg and append InGaN Scharfetter 100ns only in cloned candidate. Do not edit prior 5V audit tar contents or original completed project.
- Next: screenshot SFTP live folder/editor, verify target path before change; later grep/SWB preprocess and short transient smoke. No run started.

## 2026-10-10 — Exact cloned CAL .par current contents read before edit (OBSERVED)

- Worker 이택규 used cd to the cloned SWB project `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL` and ran `cat FASTC1_pp6_des.par` on live server. File contains only `LatticeParameters { X=(0,0,-1); Y=(1,0,0) }`, `Thermionic { Formula=1 }`, and `Material="GaN" { Ionization { Species("pMagnesiumActiveConcentration") { E_0=0.2; alpha=8e-9; g=4; Xsec=1e-14 } } }`.
- CONFIRMED actual cloned .par has no InGaN/Scharfetter block yet; original Mg and crystal/thermionic config intact. Instructed user to append material-specific InGaN Scharfetter tau_max=1e-7 s for both electron/hole, with taumin=0, Nref=1e16, gamma=1, Talpha/Tcoeff/Etrap=0, preserving earlier blocks. This remains a proposed manual edit until user shows result.
- Do not claim a simulation run or physical calibration. After saved file, read-only grep/check and SWB preprocess/log proving effect, then short transient smoke.

## 2026-10-10 — CAL par backup made, 100ns InGaN override still absent (OBSERVED)

- 이택규 server shell executed `cp -p /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/FASTC1_pp6_des.par /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/FASTC1_pp6_des.par.bak_1ns` without error (copy command returned to shell; backup existence not independently listed).
- Subsequent `grep -n -A 10 'Material = "InGaN"' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/FASTC1_pp6_des.par` returned no matching lines: no literal material override exists in cloned .par at inspection time. Thus the manual 100ns SRH override has **NOT** yet been applied; previous successful 5V parent remains separate.
- Next: append only `Material="InGaN"/Scharfetter` block to cloned .par, `taumax=1e-7s` both carriers with other defaults unchanged; keep existing GaN Mg/Thermionic/Lattice definitions; save, recheck grep then SWB preprocessing/short smoke before full run. No simulation result or parameter effect confirmed.

## 2026-10-10 — User opted for manual CAL parameter copy/paste instead of ZIP transfer (PROPOSED / NOT YET APPLIED)

- User shell found `~/CMP_BASELINE_1.2.0_CAL_INPUT_CANDIDATE.zip` missing on school server. This is only a transfer gap, not a TCAD error.
- User asked to manually paste the full candidate parameter text. Assistant provided full text of custom `FASTC1_pp6_des.par` to paste **only into cloned** `CMP_BASELINE_1.2.0_CAL`: original LatticeParameters, Thermionic, GaN Mg Ionization retained; InGaN-specific Scharfetter with `taumax=1e-7 s` both carriers, unchanged taumin/Nref/gamma/Talpha/Tcoeff/Etrap. Text formatting condensed vs ZIP, physical parameter blocks equivalent; do not expect ZIP byte SHA256 after manual edit.
- Instructions: first `cp -p` cloned 283B original parameter to `.bak_1ns`, then edit cloned `FASTC1_pp6_des.par` only. Following save run read-only `grep` to verify effective text, then SWB preprocess/log, make a genuinely short Transient smoke before 5V. `sde_dvs.cmd`, `sdevice_des.cmd`, completed parent, vendor MaterialDB unchanged. **No confirmation yet that worker pasted or ran code**.

## 2026-10-10 — CAL clone parent-input SHA256 exact match (OBSERVED)

- User terminal SHA256 in `CMP_BASELINE_1.2.0_CAL`: `sde_dvs.cmd` 4a30e922aade3c9ed576889598a0f6b7ef164d675f284470388f21d1f35458d5, `sdevice_des.cmd` 1a89149505d4556bfb7bed81bd5326a36dd173c8b7d298f83584c5b4921fae91, `FASTC1_pp6_des.par` 60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039. GPT independently compared against exact private nine-file successful 5V parent archive and verified **all three hashes identical**. Clone input provenance PASS; no new 100ns CAL parameter has yet been installed, preprocessed or simulated.
- Private candidate ZIP re-inspected: `sde_dvs.cmd` unchanged, `sdevice_des.cmd` only comments updated, candidate `FASTC1_pp6_des.par` 981 bytes (SHA256 adfe81ab03b8f0ca84b09b9a4373fdc8e71f7a5faa00ce01a7c0b82b7fb2f1ad) adds InGaN Scharfetter tau_max 1e-7s for both carriers without changing GaN Mg/Lattice/Thermionic. Installing **only candidate .par in the new clone** is sufficient for the intended physics-only sensitivity; original zip file must be transferred from private chat to school server before this can happen.
- Next: worker downloads ZIP from chat, transfers via secure SFTP to /user/semi/semi437/ and confirms the exact remote path and filename. Subsequently preserve original 283B cloned par as backup, extract only candidate par to cloned project, hash-check, preprocess, check material parameter application, and conduct short transient smoke before 5V. Do not overwrite completed JUSUBIN_FAST_HALF_5V_TEST or vendor MaterialDB.

## 2026-10-10 — New CAL SWB clone source files exist, candidate override not installed (OBSERVED)

- 이택규 terminal `ls -lh` in new `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/`: sde_dvs.cmd 20K, sdevice_des.cmd 5.9K, FASTC1_pp6_des.par 283B, all timestamp Oct 9 23:35.
- OBSERVED only file existence and lengths, not hash equality. Compared to privately prepared candidate ZIP, which contains an approximately 981B modified custom .par with proposed InGaN Scharfetter 100ns, the new project's 283B .par suggests proposed override has NOT been installed. No preprocess/run evidence.
- Next safest READ ONLY step: sha256sum these three NEW project files and compare with privately audited parent input SHA256 in private README. If identical, upload ZIP to server via SFTP, preserve originals in new folder before installing candidate, verify new parameter hash and then preprocess/short Transient smoke. Keep finished JUSUBIN_FAST_HALF_5V_TEST unchanged.

## 2026-10-10 — CMP_BASELINE_1.2.0_CAL project visible in SWB (OBSERVED)

- Worker 이택규 supplied actual Sentaurus Workbench screenshot. In project tree under `/user/semi/semi437/tmp/myproject/`, the separate `CMP_BASELINE_1.2.0_CAL` project is selected, and the tool flow shows SDE → SDEVICE, single visible NtSide=0 experiment. Existing successful `JUSUBIN_FAST_HALF_5V_TEST` is still separately listed in tree.
- No completed jobs are indicated in shown SDE/SDEVICE result cells (`--`). Screenshot is evidence the project exists in Workbench, NOT evidence that source files/custom InGaN Scharfetter parameter override copied, preprocessed, simulated, or physically validated.
- Next non-destructive check: `ls -lh /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/sde_dvs.cmd /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/sdevice_des.cmd /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/FASTC1_pp6_des.par`. Then inspect contents and *only in clone* install private input candidate ZIP if needed. Do not run/preprocess yet or alter original.

## 2026-10-10 — CAL 1.2.0 independent SRH-only input candidate package prepared (PROPOSED / LOCAL STATIC PASS)

- Worker 이택규 shared actual T-2022.03 MaterialDB/InGaN.par excerpt 855–925. This confirms GaAs-derived, calibration-needed SRH `Scharfetter` taumin=0/taumax=1e-9 both carriers/Nref=1e16/gamma=1, Auger A=1e-30, Radiative C=2e-10. Existing 5V TDR audit independently confirmed these active effective QW rates.
- ChatGPT constructed private zip `CMP_BASELINE_1.2.0_CAL_INPUT_CANDIDATE.zip` using the uploaded parent source (not uploaded to public GitHub). It includes three files inside a folder named `CMP_BASELINE_1.2.0_CAL`: unchanged `sde_dvs.cmd` (SHA256 4a30e922aade3c9ed576889598a0f6b7ef164d675f284470388f21d1f35458d5), same executable `sdevice_des.cmd` with only source header/comment corrections, and custom `FASTC1_pp6_des.par` preserving original LatticeParameters/Thermionic/GaN Mg and appending material-specific InGaN `Scharfetter` tau_max=1e-7 s for both carriers, with unchanged other Scharfetter fields. New private par SHA256 adfe81ab03b8f0ca84b09b9a4373fdc8e71f7a5faa00ce01a7c0b82b7fb2f1ad. README included. ZIP Python static check `testzip()=None`, SDE byte-identical, non-comment SDevice lines identical.
- External Synopsys Sentaurus training example supports material/region .par Scharfetter overrides, but the exact candidate has **NOT** been accepted by local T-2022.03 SWB preprocessing or run. The source's actual Transient goal is still 5V; it is NOT a short smoke deck; must prepare distinct short test and confirm effective settings via generated pp and runtime log.
- 100ns is a literature-motivated **sensitivity test** (Baek et al. 2023 different device), NOT measured calibration of this 4QW LED. No originals edited; no new SWB project created or simulation launched. Follow up by installing only into separate cloned project, preprocess/smoke first, and confirm model effect while verifying raw 2D current and Full/Half comparison gates.

## 2026-10-10 — Actual 5V TDR physical model audit completed

- User-uploaded private 9-file CAL audit archive inspected: source, preprocessed source, log, PLT and HDF5 final TDR. See CMP/reviews/BASELINE_1_2_0_CAL_AUDIT_20261010.md for detailed nonproprietary findings.
- OBSERVED: SDevice finished 5V, 10596.76 s; actual Transient is single 0-to-5V Increment=1.2 and 5V Save only, despite misleading comments claiming staged ramp/checkpoints.
- DERIVED across all 8 Clean/DmgL InGaN QW field arrays: B=2e-10 cm3/s, Auger=1e-30 cm6/s, SRH tau=1ns, exactly within numerical rounding. Main modeled 4QW 0.1094747566 percent radiative fraction not yet physically calibrated.
- DERIVED across all pGaN fields: ionized net acceptor equals MgActive times Mg trap occupation; occupation maximum 3.1286%, net ~3.00033e17 cm-3. Displayed MgMinus raw input is not sufficient to conclude Mg fully ionized.
- Current at 5V 1.44801646079583e-11 in raw 2D terminal conventions. J normalization and actual device validity need testing. No new TCAD project created or simulations launched.
- Next: inspect local InGaN.par exact parameter syntax, isolated SRH-only literature sensitivity CAL candidate followed by short Transient-BE smoke and NtSide 0/1e18 comparison.

## 2026-10-09 — Baseline CAL 1.2.0 audit archive integrity check PASS

- OBSERVED: 이택규 executed tar -tzf on the prepared audit tar.gz; shell printed ARCHIVE OK, confirming gzip/tar listing succeeded without error.
- The private archive still needs to be uploaded in this chat. No simulation or code modification occurred.
- Next: inspect all nine inputs/results before preparing a separate CAL candidate.

## 2026-10-09 — CAL v1.2.0 private 9-file review archive created on server (OBSERVED)

- Worker 이택규 ran shell in completed `JUSUBIN_FAST_HALF_5V_TEST`: `tar -czf ~/CMP_BASELINE_1.2.0_CAL_AUDIT.tar.gz sde_dvs.cmd sdevice_des.cmd FASTC1_pp6_des.par pp1_dvs.cmd pp2_des.cmd n1_msh.tdr n2_des.log n2_des.plt n2_des.tdr` and `ls -lh ~/CMP_BASELINE_1.2.0_CAL_AUDIT.tar.gz` returned 11 MB regular file dated Oct 9 23:05 at `/user/semi/semi437/CMP_BASELINE_1.2.0_CAL_AUDIT.tar.gz`.
- OBSERVED: archive exists at reported server path; contents/integrity/hash and private bytes are not yet available to ChatGPT in this session. User needs to transfer archive securely and upload it in chat for actual code/results review. Tar operation did not edit existing source/output or launch simulation.
- NEXT: review uploaded archive, verify actual material and current normalization, then plan independent `CMP_BASELINE_1.2.0_CAL` candidate and smoke tests. No new SWB project has been created.

## 2026-10-09 — Confirmed CMP semantic-version project naming; input inventory PASS (OBSERVED / DECISION)

- Worker 이택규 explicitly adopted `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>` (no extra v/V1). Next proposal is `CMP_BASELINE_1.2.0_CAL`. Independent future types include PROJECTA/PROJECTB, each with own version lineage; NtSide is a run variable. Exact rules: `CMP/PROJECT_NAMING_CONVENTION.md`. This supersedes the earlier proposed `CMP_BASELINE_CAL_V1` name.
- Actual user shell `ls -lh` in finished `JUSUBIN_FAST_HALF_5V_TEST` confirms all nine expected review artifacts exist: `sde_dvs.cmd` 20K, `sdevice_des.cmd` 5.9K, `FASTC1_pp6_des.par` 283B, `pp1_dvs.cmd` 20K, `pp2_des.cmd` 5.8K, `n1_msh.tdr` 1.6M, `n2_des.log` 1.2M, `n2_des.plt` 412K, `n2_des.tdr` 16M. File existence only; contents / exact revisions still require private package review.
- Next: user privately transfers these files for inspection and comparison; no source edits, no SWB project creation/renaming and no TCAD jobs performed here. Original 5V project, pre5V archive and Full reference remain untouched.

## 2026-10-09 — Semantic-version-style baseline project naming proposed (PROPOSED)

- Worker 이택규 proposed software-style three-component versions (major.minor.patch) for CMP project names such as `CMP_BASELINE_1.2.1_CAL_V1` to make relative recency/change scale clear.
- ChatGPT recommended a single version source `CMP_BASELINE_v<major>.<minor>.<patch>_<purpose>` instead of duplicate version fields (`1.2.1` plus `V1`). Examples only, not actual assigned release numbers: `CMP_BASELINE_v1.0.0_REF`, `CMP_BASELINE_v1.1.0_CAL`, `CMP_BASELINE_v1.1.1_CAL`; geometry/core physics changes -> major, validated new calibration/capability -> minor, nonphysical small correction -> patch. Any small code edit with scientifically significant result change must not be hidden under patch. NtSide0/1e18 denotes experiment configuration, not separate code version.
- IMPORTANT: naming convention remains a proposal pending user confirmation; the existing golden v1.2 lineage should be mapped explicitly before assigning an actual next number. No SWB project renamed, no TCAD code changed, no solver launched.

## 2026-10-09 — New near-final CMP_BASELINE_CAL_V1 preparation selected (PROPOSED)

- Worker: 이택규. User opted to keep the 12 MB pre5V backup unchanged and asked to prepare a new near-final baseline; permission granted to seek Claude review if helpful, but no Claude direct communication has occurred.
- PROPOSED separate branch `CMP_BASELINE_CAL_V1` from the completed `JUSUBIN_FAST_HALF_5V_TEST`. Preserve original 5V results, backup, and full FAST_C1 baseline. Keep Half+Coarse geometry, 4-QW Kou epitaxy, 5nm physical damaged sidewall, Mg/EBL/nGaN doping, and known working Transient-BE scheme; do not repeat failed QS without separate validation.
- First gate: secure the actual private SDE/SDevice/custom .par, pp-decks, mesh and finished log into a user-shared archive, confirm the effective InGaN SRH/Radiative/Auger model, current density/AreaFactor, carriers/injection, and output coverage before choosing scientifically motivated minimum parameter-only calibration. Do not tune merely to obtain higher IQE.
- Next: create separate clone after source review, perform short `NtSide=0` smoke and 5V candidate, then `NtSide=1e18` matched-physics comparison. Full-versus-Half/Coarse numerical validation and scientific plausibility remain final publication gates. No TCAD files edited and no new solver jobs started by AI.

## 2026-10-09 — pre5V archive contents observed

- 이택규 terminal `tar -tzf ...pre5V_20261009.tar.gz | head -n 30` confirmed project metadata, SDE cmd, pp1_dvs.cmd, n1_msh.tdr, FASTC1_pp6_des.cmd in archive. Only first 30 entries viewed; full integrity not verified.
- Recommendation: keep the 12 MB backup and relocate outside myproject if cluttered; preserve successful 5V_TEST. No files deleted or new run executed.

## 2026-10-09 — Pre-5V backup archive exists, content not yet verified (OBSERVED)

- 이택규 actual server shell `ls -lh /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar*` returned `JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz`, 12 MB, Oct 9 11:25; this is outside the main project directory, not a SWB simulation node. Exact contents and independent recovery copy remain UNVERIFIED.
- Before any deletion user should inspect safely with `tar -tzf ... | head -n 30` and decide whether archived pre-5V input is redundant; preserve completed 5V_TEST inputs/outputs and Full reference. No file deleted, modified or simulation launched.

## 2026-10-09 — User asks to clean pre5V archive and choose near-final next run (PROPOSED)

- 이택규 screenshot shows SWB project `JUSUBIN_FAST_HALF_5V_TEST` and second entry text truncated `JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.g...`, likely a pre-5V `.tar.gz` backup archive, not another simulation node. Filename suffix, archive contents, storage redundancy not yet checked. Recommendation: do NOT delete until listing and a recovery copy are independently verified; use read-only `ls -lh .../JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar*` first.
- User wants another nearly-final Baseline run. Proposed next: preserve completed 5V NtSide0 and source; clone independent branch and review actual effective InGaN SRH/Radiative/Auger and electrical current/AreaFactor/injection BEFORE choosing a justified parameter-only calibration; short NtSide0 transient smoke then 5V with fixed geometry and repeat NtSide1e18 with identical physics if passed. Full/Half+coarse numerical equivalence required before final/publishable claims; avoid failed QS method. No TCAD writes, deletion, or run performed.

## 2026-10-09 — Daily verified outcomes and near-final baseline run request (OBSERVED + PROPOSED)

- Worker 이택규 requested recap of October 9 work and expressed preference to run a near-final baseline candidate rather than spend more days on preliminary checks. This is intent, not permission to modify source or evidence of a run.
- Today verified in supplied 5V_TEST data: Half+Coarse NtSide0 transient to 5 V completed (recorded runtime ~2h56m); 138194 mesh elements vs Full 290814; all 12 DmgL trap Conc=0; four-QW integrated modeled radiative recombination fraction 0.1094747566%, SRH about 99.886%; p-GaN local hDensity 3.001343e17 cm^-3 and activated region-scoped Mg IncompleteIonization; effective Mg GaN log E_0=0.2eV, alpha=8e-9eV cm, beta=0, gamma=1, g=4, Xsec=1e-14cm2, b_Nref=6e18, E_Nref=2e18; QS test failed at ~0.019304636 V (per earlier records). T-2022.03 InGaN.par GaAs-derived 1ns recombination lifetime default and unverified material mixing/parameters; very low modeled IQE_rec not physically calibrated. Raw current to J normalization and steady-state criterion remain unverified; Full/Half and NtSide1e18 accuracy pending.
- PROPOSED next run: preserve completed sources/results; before new 5V near-final candidate, review actual effective InGaN recombination parameters and 5V I(V)/2D current normalization/injection on existing results; create distinct literature-calibration sensitivity branch with parameter-only modifications once justified; short convergence/representative high-bias pilot; then NtSide0/1e18 paired 5V exploratory runs. Keep Full/Half+mesh equivalence mandatory before publication/final baseline freeze. No source changed or simulation started.

## 2026-10-09 — Actual Mg ionization log confirmed; exploratory Half test vs Full gate discussed (OBSERVED / PROPOSED)

- Worker 이택규 provided real `JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` excerpt lines 818-842: effective GaN Mg acceptor species `pMagnesiumActiveConcentration` has `E_0=0.2 eV`, `alpha=8e-9 eV cm`, `beta=0`, `gamma=1`, `g=4`, `Xsec=1e-14 cm^2`, `Xsec_formula=1`, `highdop_formula=1`, `b_Nref=6e18 cm^-3`, `b_pow=2`, `E_Nref=2e18 cm^-3`, `E_pow=2`. Separate `vanOverstraetendeMan impact ionization E0` message concerns a different process, not Mg incomplete ionization.
- Earlier user excerpt of actual log confirms `With incomplete ionization` on `Clean_pGaN` and `DmgL_pGaN` and automatic net doping recalculation. MgMinus field's equality with raw Mg in one SVisual Probe is still unexplained; physical calibration not frozen.
- User asks whether to skip full vs half comparison and proceed with next runs. Recommendation (PROPOSED, not user-approved execution): exploratory NtSide=1e18 Half+Coarse pilot may proceed in a separate copy after preprocess/short smoke with same physics, without waiting for comprehensive Full/Half equivalence; however publication-grade final baseline/A/B production MUST check full-vs-half current normalization, spatial QW/edge quantities and separate mesh-convergence because Half+Coarse changes two variables. Keep finished NtSide=0 and full/fine reference untouched. No TCAD run/source edits occurred in this chat.

## 2026-10-09 — Full GaN Mg ionization parameter block from active 5V_TEST (OBSERVED)

- Worker 이택규 supplied `sed -n '20,55p' FASTC1_pp6_des.par`: `Material="GaN" / Ionization / Species("pMagnesiumActiveConcentration")` has `E_0=0.2`, `alpha=8e-9`, `g=4.0`, `Xsec=1.0e-14`. All four declared coefficients are present in actual referenced parameter file.
- Earlier pp2 command declared `IncompleteIonization` for Clean_pGaN and DmgL_pGaN, and SVisual Probe returned Clean_pGaN hDensity≈3.001343e17 while MgActive=MgMinus=9.59e18 cm^-3. Effective ionization, output dataset semantics, and material model calibration remain UNRESOLVED. No parameter changes or simulation runs.
- Next: inspect relevant Sentaurus T-2022.03 reference syntax and output variable definitions; evaluate simulation field's meaning before assuming fully ionized Mg. Preserve baseline.

## 2026-10-09 — 5V_TEST custom GaN Mg ionization coefficients observed

- 이택규 user terminal grep on actual `FASTC1_pp6_des.par`: `Material = "GaN" { Ionization { Species ("pMagnesiumActiveConcentration") { E_0 = 0.2; alpha = 8e-9` (lines 24-32). More lines are not yet shown; units, degeneracy and effective model still require confirmation.
- Prior `pp2_des.cmd` activates IncompleteIonization in Clean_pGaN and DmgL_pGaN; active parameter file path verified in n2_des.log. Prior SVisual Clean_pGaN hDensity≈3.001343e17, MgActive and MgMinus each 9.59e18 cm^-3. No claim of correct ionization physics from partial deck.
- Next: read-only show entire GaN Ionization section with `sed -n '20,55p' FASTC1_pp6_des.par`; no rerun or code edits.

## 2026-10-09 — 5V_TEST actual SDevice parameter path verified (OBSERVED)

- User shell `grep` on active pp2_des.cmd and n2_des.log: pp2_des.cmd line 22 `Parameters = "FASTC1_pp6_des.par"`; line 68 `DefaultParametersFromFile`; n2_des.log line 291 ModelParameters same file; line 760 reads it, line 804 loads MaterialDB/GaN.par; Silicon.par is also loaded. `Use Si parameters` appears in generic default-device log; does NOT by itself prove GaN regions use silicon material physics.
- Existing SVisual screenshot: Clean_pGaN hDensity ~3.001343e17, Mg active and Mg minus ~9.59e18 cm^-3; unresolved effective incomplete ionization and interpretation.
- Next read-only inspect fast custom par and GaN material parameters for Mg doping ionization, without changing runs.

## 2026-10-09 — 5V_TEST Clean_pGaN SVisual Probe: hole density target matched (OBSERVED)

- Worker: 이택규. User supplied screenshot of existing `JUSUBIN_FAST_HALF_5V_TEST/n2_des` SVisual Probe in region `Clean_pGaN(GaN)`, coordinate (x,y,z)=(0.0741335366319,1.00590269042,0) displayed in the viewer (coordinate units not independently confirmed).
- Measured `hDensity=3.001343052563e17 cm^-3`, `eDensity=9.691983460557e7 cm^-3`, `pMagnesiumActiveConcentration=9.59e18 cm^-3`, `pMagnesiumMinusConcentration=9.59e18 cm^-3`. Relative difference from historical target 3e17 is +0.0447684% at this single point. Snapshot's actual bias/temperature and steady-state status not independently confirmed.
- The target free-hole concentration is numerically matched **at one sample location**; this does not establish whole-pGaN spatial uniformity, equilibrium calibration, valid Mg physics, or publication-grade baseline.
- Notable unresolved: `pMagnesiumMinusConcentration` equals total active Mg as displayed, seemingly inconsistent with an incomplete-ionization interpretation, even though free-hole concentration is ~3.0e17. Need inspect definition of exported Minus field, doping model activation and charge compensation, SDevice region model and active parameters before inferring ionization fraction. Do not change Mg or rerun yet.
- NEXT: inspect existing `n2_des` probe at another interior Clean_pGaN point, verify output bias/temperature and 0V baseline if available, read active `pp2_des.cmd` incomplete-ionization and models. No TCAD code changed or new jobs started.

## 2026-10-08 — FAST_HALF_BULK_R15 SWB manual implementation package prepared

- 작업자: 이택규; 상태: PROPOSED / STATIC CHECKED / NOT RUN.
- User specifically chose to create new SWB project, tools, parameters and source manually rather than use Claude standalone run_r15h.sh.
- From Claude ZIP made a **separate chat-delivered** SWB-ready four-file package `CMP_FAST_HALF_SWB_READY_20261008.zip` (not committed because it contains full TCAD source): `sde_dvs.cmd`, `sdevice_des.cmd`, `sdevice.par`, `SWB_README_KO.md`.
- SDE change vs Claude half code: `sde:build-mesh "" "n@node@"`; half y=0..2.5um, physical damaged DmgL 5nm and bulk mesh factor 1.5 preserved.
- SDevice changes vs Claude Node6 standalone: `Grid=@tdr@`, `Parameters=@parameter@`, `Plot=@tdrdat@`, `Current=@plot@`, `Output=@log@`, intermediate FilePrefix=`n@node@_inter`; 12 left-side trap concentrations `@NtSide@` for SWB split `0` / `1e18`. Original physics/Math/RHSMin=1e-3, Iterations=15, Increment=1.2, endpoint=5 V retained.
- par `sdevice.par` has SHA256 `60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039`, same as recorded FAST_C1 parameter file.
- Static substitutions/counts passed; **no SWB preprocess, SDE mesh, SDevice or comparison run yet**. Need actual Workbench mesh/preprocess check; do not call this confirmed numeric equivalent; preserve original full/fine reference.

## 2026-10-08 — Claude FAST_HALF_BULK_R15 package static audit by ChatGPT

- 작업자: 이택규; 상태: REVIEWED / STATIC TEST PASS / SENTAURUS NOT RUN.
- User supplied `FAST_HALF_BULK_R15_for_GPT_20261008.zip` (14 files; source SDE, standalone SDevice decks, scripts and README). `sha256sum -c SHA256SUMS` all PASS, Python syntax 4 scripts PASS, POSIX shell `sh -n` PASS; SDE Scheme parentheses/strings statically balanced.
- SDE cuts at proposed yC=2.5 um with one DmgL physical sidewall and clean artificial symmetry face; `BulkFac=1.5` is restricted by protection windows. Actual SDE mesh and source-vs-input exact diff not verified here (original active SDE/pp6 archive not in this review session).
- Node6 retains 12 DmgL trap regions at Conc=0; Node12 retains 12 DmgL trap regions at Conc=1e18; 0 DmgR region Physics in both. Main deck Iterations=15, RHSMin=1e-3, Increment=1.2, 5V target. Smoke normalized transient scaling appears consistent with T-2022.03 UG p.144-145, requires log validation.
- **Safety finding:** supplied `tdr_region_integrals.py` not tested on result TDR; its potential-ordering check can skip when `ElectrostaticPotential` unavailable yet continue printing metrics, and missing SRH gets default 0 in q*SRH print. Do NOT use those integrals as validated scientific results until corrected/tested.
- Current decision: **GO for separate SDE-only mesh Gate a**, not yet GO for full 5V run. Gate b Poisson and Gate c 0–1V detached smoke must complete PASS before Node6 trial. Historical FAST_C1 reference runs remain untouched. No sentaurus job launched from ChatGPT environment.
- Review note delivered to user as `FAST_HALF_R15H_GPT_REVIEW_20261008.md`. Do not publicly commit full vendor input/decks.

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


## 2026-10-09 11:30 KST — JUSUBIN_FAST_HALF_SWB completion reported

- 작업자: 이택규
- 상태: OBSERVED (user report; terminal/log not yet re-verified in this session)
- 이택규가 주수빈이 전날 실행한 `JUSUBIN_FAST_HALF_SWB`가 모두 완료되었다고 보고함.
- 이 보고로 Half+coarse transient branch는 "running"에서 "completion reported" 상태로 이동.
- 단, 최종 bias 도달, fatal/error 부재, 산출물 존재, elapsed time, I-V/IQE 유효성은 아직 로그로 재확인하지 않았으므로 CONFIRMED로 승격하지 않음.
- 다음: project terminal에서 n2_des.log/out/err와 최종 .plt/.tdr 존재를 확인하고, final 0.3 V 도달/normal termination/accepted final step을 검증. 그 후 QS Copy 결과와 runtime·I-V를 비교하고 full FAST_C1 reference 대비 half+coarse validation을 진행.


## 2026-10-09 — JuSubin Half transient completion verified; QS Copy early stop
- 이택규가 `JUSUBIN_FAST_HALF_SWB` n2의 0.3 V 정상 종료, wallclock 25019.43 s, PLT/TDR/SAV 생성 및 0.3 V 전류 성분을 확인함.
- 주수빈의 별도 `JUSUBIN_FAST_HALF_SWB_Copy` QS n2 로그: `Step-size less than MinStep (step-size = 8.3986e-07)`로 수렴 중단; 18417.09 s; SAV/TDR 저장과 SDevice 종료는 확인되나 0.3 V 도달 미확인.
- QS가 더 빨랐다는 성능 해석 불가. 다음: QS PLT의 최종 수렴 전압과 로그 cutback/solver 오류 파악, Common Baseline 변경 보류.


## 2026-10-09 — QS Copy last accepted bias determined
- 작업자: 이택규. OBSERVED from user-provided `JUSUBIN_FAST_HALF_SWB_Copy/n2_des.plt` tail and `n2_des.log` grep.
- Last recorded QS pseudo-time: 6.43487876313307E-02; last anode OuterVoltage: 1.93046362893992E-02 V (0.0193046363 V; 19.3 mV, only ~6.435% of requested 0.3 V).
- Last log attempts at t=0.0643488 to 0.0643505 then terminated `Step-size less than MinStep (step-size = 8.3986e-07)`.
- QS runtime 18417.09 s but did NOT reach goal. Cannot compare as speedup to original transient that reached 0.3 V in 25019.43 s.
- Root numerical/physics trigger not yet established. Next: inspect QS log around lines 6900-7000 and `n2_des.err`; no blind MinStep or baseline modification.


## 2026-10-09 — QS Copy Newton divergence root symptom checked
- 작업자 이택규; user-shared `n2_des.log` lines 6900-6997 from QS Copy show Coupled Poisson/electron/hole using Bank/Rose nonlinear solver, factor 1.0, Newton residual erratic (`|Rhs|` from 38 to up to 1.26e8, ending 1.85e6). Coupled exhausted 15 iterations in 208.16 s, then failed retry because half-step 8.3986e-7 < MinStep 1e-6. Last accepted bias 0.0193046363 V, goal 0.3 V. Error file E0 anisotropic/isotropic mismatch notice; not identified as termination cause. Numerical trigger observed, fundamental cause unresolved. No TCAD changes. Next inspect actual pp2_des.cmd Math/Solve settings and compare original transient in controlled no-change analysis.


## 2026-10-09 — QS preprocessing numerical settings
- OBSERVED: `JUSUBIN_FAST_HALF_SWB_Copy/pp2_des.cmd` uses Quasistationary, InitialStep 0.03, MinStep 1e-6, MaxStep 0.15, RHSMin 1e-3 and QS Coupled Iterations 15. `LineSearchDamping=1e-2` shown in earlier startup Coupled block with 500 iterations, not in listed QS inner Coupled line.
- QS last accepted bias 0.019304636 V; nonlinear Newton convergence failure after 15 attempts confirmed from logs. Full Math and Solve block comparison pending; no code changed.


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


## 2026-10-09 — New half 5V test project opened in SWB (user report)
- 작업자: 이택규. OBSERVED from user statement: after `swb /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST &`, user reports the copied project was created/opened.
- GUI screenshot/node flow/path independent verification still pending. Original `JUSUBIN_FAST_HALF_SWB` left unchanged. No 5V code edit, preprocess or SDevice run confirmed.
- Next: user sends full SWB screenshot showing copied project and SDE/SDevice nodes, then review code/step settings before launch.


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


### 2026-10-09 — Project A study: Cedge position and existing MQW damage traps
- 이택규 asked whether Carbon sits in n-GaN rather than MQW and whether MQW had traps.
- Stage1 Project A places localized Cedge in upper n-GaN immediately under MQW, directly inside sidewall damage strip, separate from native MQW regions.
- Existing baseline defines DmgL sidewall trap regions for QW1 through QW4, plus other epitaxial layers. NtSide=0 keeps these trap concentrations zero; NtSide=1e18 activates nominal damaged-edge traps.
- Carbon deep acceptor and existing sidewall traps are different physical models; reducing sidewall SRH is a hypothesis, not a proven result. No code was changed.

## 2026-10-09 14:29:52 KST — Half+Coarse 5V_TEST Node2 successfully completed (OBSERVED / SOLVER COMPLETE)

- Worker: 이택규; device run in SWB copy `JUSUBIN_FAST_HALF_5V_TEST`.
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

## 2026-10-09 — 5V_TEST SVisual Clean_QW1–QW4 region names verified (OBSERVED)

- 이택규 provided screenshot from Sentaurus Visual `JUSUBIN_FAST_HALF_5V_TEST` with widened Regions Name column. Visible named regions: `Clean_EBL`, `Clean_QW1`, `Clean_QW2`, `Clean_QW3`, `Clean_QW4`, `Clean_nGaN`. This confirms the four clean QW **region labels are present in SVisual**, not that radiative rate within each is positive. Prior screenshot displayed a positive spatial `RadiativeRecombination` field (legend max 7.483e19 cm^-3 s^-1) without mapping it to individual named QWs.
- NEXT: keep RadiativeRecombination selected; zoom thin upper active stack in SVisual, probe local numeric values with explicit Clean_QW1..4 region identification, then review SRH/Auger and QW integration. Do not clean/re-run Node2, claim IQE, or modify original full baseline.

## 2026-10-09 — 5V_TEST SVisual active-stack zoom; point sampling next (OBSERVED)

- 이택규 screenshot: `n2_des` final SVisual `RadiativeRecombination` selected; left Regions table visibly lists `Clean_EBL`, `Clean_QW1`, `Clean_QW2`, `Clean_QW3`, `Clean_QW4`, `Clean_nGaN`, with Clean_QW3 row highlighted. Zoomed upper multilayer active stack shows horizontally layered nonuniform radiative colors; legend global max 7.483e19 cm^-3 s^-1, min near zero. The selected row alone does not assign each colored band to a known QW; no individual QW numeric Probe value measured yet.
- Read-only NEXT: use SVisual Probe toolbar to click inside a thin QW layer. Probe pane Var Values contains RadiativeRecombination point value and Cell Info can identify containing region, allowing QW1..4 assignment; continue to SRH/Auger and integrated rates after sampling. No solver/code change and no assertion of IQE.

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

## 2026-10-09 — SVisual Probe At decimal precision limitation and workaround (OBSERVED UI / PROPOSED NEXT)

- 작업자: 이택규 reports SVisual `Probe At...` input accepts only about five decimal places; exact earlier QW4 Radiative coordinate entry is impractical. This is a GUI limitation reported by user, not a solver/data failure. No new physics measurements or code edits.
- Preferred **test**: at existing QW4 probe position uncheck `Show Only Active Field` in Probe panel to see whether `RadiativeRecombination`, `srhRecombination`, and `AugerRecombination` appear at the same Probe point; verify screenshot before claiming UI successfully exposes all fields.
- Fallback: use rounded coordinates (x=0.24509, y=0.58322, z=0) consistently for *new* Radiative, SRH, Auger probes; inspect returned coordinates and zone each time. Cannot reuse prior 12-decimal Radiative value directly with a new rounded-coordinate SRH value as a fully co-located comparison. No IQE from point probes; eventual QW integration still required.

## 2026-10-09 — 5V_TEST co-located Clean_QW4 Probe shows dominant local SRH (OBSERVED; device IQE UNRESOLVED)

- Worker 이택규 provided three SVisual Probe screenshots on the completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des` final TDR. All three are the **same point**: zone `Clean_QW4(InGaN)`, x=`0.244864017914`, y=`0.651958341615`, z=0. This differs from earlier SRH y=0.599783903626 and initial Rrad y=0.58321731303; do not mix old and new point values.
- Same-point fields in cm^-3 s^-1 (screen values): `RadiativeRecombination=7.103015017104e18`; `srhRecombination=1.681575471039e22`; `AugerRecombination=1.238545872618e15`; `TotalRecombination=1.682285896396e22`. Sum agrees with displayed TotalRecombination within screenshot precision.
- Derived **LOCAL radiative fraction only**: `100*Rrad/(Rrad+Rsrh+RAuger)≈0.0422%`; local nonradiative fraction ≈99.9578%; SRH dominates at this sampled point. This is **NOT** full-QW or full-device IQE, nor proof of overall LED performance/failure. QW1–QW3 require corresponding SRH/Auger samples and integrated full-QW volumes for recombination-based IQE.
- Importantly `NtSide=0` disables parameterized damaged-edge traps in this reference branch but does NOT disable the generic `SRH()` bulk nonradiative recombination physics; high QW local SRH does not by itself prove sidewall damage or carbon-project effect. Need inspect active carrier lifetime, material parameters and field/region distribution before root-cause claims.
- NEXT: preserve outputs and avoid rerun; use read-only SVisual integrated QW Rrad/SRH/Auger workflow and compare QW1–4, inspect actual active SRH lifetime and material database, 2D current normalization/physical injection. Use same-bias/current full vs half/fine check before declaring Common Baseline. No TCAD code modified.

## 2026-10-09 — Project A fabrication-route feasibility brainstorm (PROPOSED / NOT APPROVED / NOT RUN)

- Worker: 이택규. Request: evaluate how the Stage1 Project A localized upper-nGaN-sidewall GaN:C Cedge could be fabricated. **No process route selected, no implantation/epitaxy performed, no TCAD/SProcess code modified.** Original frozen Common Baseline, Cedge conceptual position inside existing 5nm damaged-sidewall strip under MQW, and NtSide0/1e18 comparison remain unchanged.
- Candidate POST-MESA: completed LED epitaxy → ICP mesa etch exposes nGaN sidewall → protect pGaN/MQW and all non-target surfaces with *selective vertical-height mask/spacer* → angled/rotated C-ion implantation into exposed upper-nGaN sidewall → damage-recovery/thermal-budget gate → passivation and contacts. Critical unsolved gates: selectively exposing only target nGaN sidewall without irradiating QWs; finite ion straggle/depth/dose, angular shadowing; implanted C electrical activity vs implantation-induced isolation; post-MQW anneal thermal damage risk. Without selective mask this does **not** implement the current localized nGaN-only Cedge.
- Candidate PRE-MQW: grow nGaN up to intended upper region → lithographically mask future mesa-edge ring → implant C into exposed nGaN or grow selective GaN:C → validated recovery/cleaning and epitaxial regrowth → deposit MQW/EBL/pGaN → accurately align future mesa etch to buried annulus → passivation/contact. Protects already-formed MQW from carbon implantation anneal (since it is grown later) but has severe future-mesa overlay, high-quality epitaxial regrowth, and implant-damage recovery gates. Exact 5nm Dmg in TCAD is **not** a realizable lithographic alignment tolerance specification.
- Literature DOES demonstrate related *non-carbon* isolation concepts: As sidewall implantation in InGaN microLED (Next Nanotechnology 2025 DOI 10.1016/j.nxnano.2024.100101), F-implanted p-GaN current confinement ring in 6-10um microLED (ACS Photonics 2026 DOI 10.1021/acsphotonics.5c02363). Neither verifies a C-implanted upper-nGaN sidewall ring. Earlier `Characterization of Ca and C implanted GaN` (Materials Science and Engineering B 1997 DOI 10.1016/S0921-5107(97)00144-X) documents implantation damage/incomplete anneal with C+, and a Sandia 1995 report `Role of C, O and H in III-V nitrides` reports no measurable electrical activity for implanted C under its investigated conditions. Carbon-doped GaN growth literature supports C_N deep acceptor around Ev+0.9–1.1eV, but implanted-carbon activity cannot be assumed to match as-grown GaN:C.
- InGaN MQWs have temperature-dependent degradation/intermixing sensitivity; reports show significant degradation around 930–950 C for particular structures (J Alloys Compounds 2022, DOI 10.1016/j.jallcom.2021.163519; J Crystal Growth 2005 DOI 10.1016/j.jcrysgro.2005.04.002). Do not establish a universal safe/unsafe anneal temperature or prescribe unverified implantation energy/dose/angle/temperature.
- Next research gates: 1) team decides whether target is a chemically active C_N-compensated GaN:C edge vs damage-based implantation isolation (different device physics!); 2) compare POST vs PRE-MQW process feasibility, alignment and thermal budgets; 3) obtain measured/proven C depth and lateral profile/activation data, SRIM/SProcess process profile model before claiming fabrication realism; 4) ensure experimental masked/annealed control and inert-ion damage controls to separate C compensation vs irradiation damage; 5) keep current Baseline electrical/radiative validation priority unchanged.

## 2026-10-09 — Corrected measurement priority: QW3 probes confirmed, per-region integration needed (OBSERVED / SCIENTIFIC DECISION)

- Worker: 이택규. User submitted SVisual Probe screenshots in the successful `JUSUBIN_FAST_HALF_5V_TEST/n2_des` 5V result. Clean_QW3(InGaN) same location x=0.219173763524, y=0.555622585194, z=0: `RadiativeRecombination=8.333611568957e14`, `srhRecombination=5.390114530106e19`, `AugerRecombination=5.79338765299e8` cm^-3 s^-1. Other captured fields include electron density 1.385821616728e14 and hole density 4.507709343047e11 (units of densities expected cm^-3, panel exact unit not shown). Numerical point checks are local only, no physical IQE claim.
- User correctly identified that publication analysis requires **integrating the recombination rate over each entire QW**, not further collecting isolated probes. Adopt `CMP/PROJECT_AB_PRE_RUN_AUDIT.md` G5 and metric definition: integrate Rrad, SRH, Auger over each QW region, sum integrals, THEN compute recombination-based IQE. Do not average or sum local fractional IQEs. The local QW3 and QW4 probes suggest large SRH at those sampled points but are not representative of whole-well rates.
- First non-destructive operational check: SVisual Tools > Integrate (∫dr right toolbar), field RadiativeRecombination, Region/Material filter Clean_QW3 only, complete spatial domain and Start Integration. Save/report raw integral AND domain units displayed; then integrate same QW's srhRecombination and AugerRecombination and expand QW1..4. Include DmgL_QW regions as appropriate for complete active-QW physical volume and matched full/half comparisons, explicitly avoid counting Clean-only as total QW losses. Two-dimensional SVisual integration produces an area integral with native geometrical units; out-of-plane depth/2D normalization and actual physical cm unit conversion MUST be verified for absolute recombination counts; a ratio of comparably normalized integrals cancels common factors.
- Older and newer Sentaurus Visual User Guides document Field Integration GUI and `integrate_field -field ... -regions {Clean_QW3}`; current environment T-2022.03-specific GUI behavior and output units still require a user screenshot before scripting/automation is treated as validated. No TCAD source or baseline changes or new solver runs.

## 2026-10-09 — SVisual Field Integration QW region scope clarified (PROPOSED, pending output)

- 이택규 screenshot shows choices `Clean_QW3` and `Clean_QW3+DmgL_QW3` in Field Integration selector. For full physical QW3 recombination accounting in current Half model, select `Clean_QW3+DmgL_QW3` as a single combined group, not both it and `Clean_QW3` (would double count).
- `Clean_QW3` alone excludes the QW3 damaged sidewall; still useful later for separate core-vs-edge attribution. `NtSide=0` deactivates parameterized sidewall traps but the DmgL_QW3 geometric region still exists.
- This is a selection decision, NOT an executed/verified integral. Next capture chosen field `RadiativeRecombination`, selected group, numerical Integral/Domain and actual 2D units; verify group region membership before claiming whole-well total. Repeat same group for SRH/Auger, and other QWs before IQE computation. Keep comparison scope consistent for full/fine and damaged NtSide=1e18 branches.

## 2026-10-09 — SVisual QW3 Rrad integral and ROI correction

- 이택규 screenshot shows Clean_QW3(InGaN) only: RadiativeRecombination Integral=2.657110e+02 [s^-1 um^-1], Domain=5.985012e-03 [um^2], dimension 2. Full QW3 (including DmgL_QW3) not yet measured.
- Prior guidance calling Clean_QW3+DmgL_QW3 a combined 2D QW region was not supported; it is likely an interface label. Safest next: independently select DmgL_QW3 (standalone name), press Start Integration, verify right output Regions of Dimension 2 DmgL_QW3, then add to Clean_QW3; same procedure SRH/Auger and other QWs. Preserve files. No device IQE yet.

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

## 2026-10-09 — Live SWB original SDevice source uses FASTC1_pp6_des.par, not sdevice.par (OBSERVED; SWB popup resolved)

- Worker 이택규 executed read-only `grep -nE 'Parameters|DefaultParametersFromFile' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_SWB/sdevice_des.cmd` in terminal currently at `JUSUBIN_FAST_HALF_5V_TEST`. Actual **original SWB source** output: `22: Parameters = "FASTC1_pp6_des.par"`, `68: DefaultParametersFromFile`.
- This establishes the original source `File { Parameters=... }` explicitly references the custom FASTC1 parameter file rather than newly generated `sdevice.par`. Therefore previous `Create Parameter File: sdevice.par does not exist` / default radio Silicon in SWB is a GUI input-generation request, **NOT evidence finished GaN-InGaN LED ran with Silicon** or a defect requiring creation of `sdevice.par`. Actual completed 5V_TEST `n2_des.log` independently confirms `ModelParameters file: FASTC1_pp6_des.par` and material-default loading for GaN.par, InGaN.par/InN.par through `DefaultParametersFromFile`. A SWB-generated sdevice.par would **not be automatically used by this literal explicit File parameter reference unless deck/tool config changes**; unnecessary and risks custom parameter shadowing.
- **Action**: press Cancel in original GUI if still open, do not select Silicon or GaN/Create Parameter File in original project and do not overwrite original FASTC1 or MaterialDB. Next read-only inspect actually used custom `FASTC1_pp6_des.par` for `Material=...`, `Region=...`, `Scharfetter`, `RadiativeRecombination`, `Auger`, `Ionization`, `Magnesium`, `LatticeParameters`, `Thermionic` and dump full parameter content with `sed` if short. Also inspect `pp2_des.cmd` Physics region ionization/trap scope. MaterialDB GaAs-derived InGaN lifetime 1ns is **unvalidated for actual effective QW**, and physically realistic SRH and current injection remain Baseline physical blocker.
- **Recommended separate branch**: only after source/read-only verification copy completed 5V_TEST to new calibrated branch, retain existing custom FASTC1 parameters, add *scoped* explicit literature-backed InGaN recombination parameters to a NEW custom .par, preprocess and verify material/region precedence, run short pilot and then NtSide0/1e18 current-matched and mesh Full/Half tests. Never change working original, never assert all defaults right or wrong without effective parameter context. No SDevice source or data changed during this terminal check.

## 2026-10-09 — Runtime SDevice 5V_TEST Mg incomplete ionization / first Dmg trap verification (OBSERVED)

- 이택규 directly pasted read-only `sed -n '112,175p' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd` actual preprocessed live deck. `Physics(Region="Clean_pGaN") { IncompleteIonization(Dopants="pMagnesiumActiveConcentration") }`; `Physics(Region="DmgL_pGaN")` has same `IncompleteIonization` plus `Traps((Acceptor Conc=0 Level FromValBand EnergyMid=0.75 eXsection=1e-15 hXsection=1e-15))`. `Physics(Region="DmgL_EBL")` also `Traps((Acceptor Conc=0 ...))`.
- DIRECT EVIDENCE: model's Mg incomplete-ionization is configured for Clean and left-damaged pGaN regions; sidewall Trap concentration zero in DmgL_pGaN and DmgL_EBL at NtSide0. Previous global log `Without incomplete ionization` does not negate explicit region-specific Physics. The numerical p-Mg distribution, free hole concentrations and scope of remaining 10 DmgL traps are not established by THIS excerpt; prior 5V_TEST preprocessed verification reportedly all 12 Dmg Trap Conc=0, but use independent full-region scan to reconfirm before declaring broad scope.
- Original separate SWB branch custom `FASTC1_pp6_des.par` holds Mg GaN Ionization E_0=.2, alpha=8e-9, g=4, Xsec=1e-14; do not claim original and completed 5V_TEST custom par files are identical without checksum.
- No new TCAD failures or source changes. Next read-only all-region audit `grep -nE 'Physics \(Region=|IncompleteIonization|Traps|Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd` then doping concentration/donor SDE code and mesh, before physics parameter calibration and 2D injection/current normalization.

## 2026-10-09 — Completed 5V_TEST n2 SDevice preprocessed 12 sidewall traps all OFF (OBSERVED / VERIFIED)

- Worker 이택규 executed directly `grep -nE 'Physics \\(Region=|IncompleteIonization|Traps|Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd`, showing physical-region declarations. `Clean_pGaN` `IncompleteIonization` line 128 and `DmgL_pGaN` `IncompleteIonization` line 137.
- Every one of **12 separate preprocessed left damaged-region traps has `Conc=0`**: DmgL_pGaN (line 145), DmgL_EBL (165), DmgL_Barrier0 (185), DmgL_QW1 (205), DmgL_Barrier1 (225), DmgL_QW2 (245), DmgL_Barrier2 (265), DmgL_QW3 (285), DmgL_Barrier3 (305), DmgL_QW4 (325), DmgL_Barrier4 (345), DmgL_nGaN (365). This is **confirmed Trap OFF** for all model's parameterized `DmgL_` sidewall trap regions in completed 5V NtSide=0 deck, not just two example regions. No right-side traps expected in symmetric Half.
- Scientific boundary: global `Recombination(SRH(),Auger(),Radiative)` remains ON and can generate a high baseline SRH without parameterized NtSide traps. Thus measured 5V all-QW SRH fraction 99.886% CANNOT be attributed to any of these explicit sidewall trap concentrations (zero). Cannot conclude sidewall physical damage is absent in reality, or that all other SRH and interface recombination in model is eliminated.
- Mg incomplete ionization `Physics` declarations shown for Clean/DmgL pGaN, but actual Mg donor concentration placement and free-carrier profile are STILL UNVALIDATED. `NtSide=1e18` counterpart also has NOT passed SDevice 5V convergence; no Full/Half+coarse matching, 2D J normalization, material lifetime or transient steady-state acceptance.
- NEXT READ ONLY: inspect preprocessed `pp1_dvs.cmd` from completed `JUSUBIN_FAST_HALF_5V_TEST` for `sdedr:define-constant-profile`, placements and `pMagnesiumActiveConcentration` / n donors, then verify n1_msh.tdr concentration profiles in SVisual. No new run or changes.

## 2026-10-09 — 5V_TEST SDE p-GaN, EBL and n-GaN doping region placement inspected (OBSERVED / VALUES PENDING)

- Worker 이택규 directly supplied read-only `sed -n '501,615p' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd`. Actual SDE declarations:
  - `CP_pGaN_Mg`: `pMagnesiumActiveConcentration` assigned variable `N_Mg_p`, placed in `DmgL_pGaN` and `Clean_pGaN`.
  - `CP_EBLp`: `PDopantActiveConcentration` assigned `N_A_EBL`, placed in `DmgL_EBL` and `Clean_EBL`. Explicit code comment calls it an effective active acceptor approximation **deliberately separate from GaN Mg incomplete-ionization calibration**.
  - `CP_EBLx`: `xMoleFraction` assigned `x_Al_EBL`, placed in `DmgL_EBL` and `Clean_EBL`.
  - `CP_nGaN`: `NDopantActiveConcentration` assigned `N_D_n`, placed in `DmgL_nGaN`, `Clean_nGaN`, and `nGaN_base`.
- These observations support correct intended doping **species/region assignment in SDE code**, NOT actual numeric concentrations or actual meshed profiles/free carrier density. The current excerpt does not contain the values of `N_Mg_p`, `N_A_EBL`, `N_D_n`, `x_Al_EBL`, and does not cover QW/Barrier background doping or mole fraction sections below line 615. Cannot declare the entire doping validation gate passed.
- Previous live `pp2_des.cmd` shows `IncompleteIonization` only in `Clean_pGaN` / `DmgL_pGaN`, and all 12 DmgL sidewall traps `Conc=0` in NtSide=0. This now gives a consistent intended separation of GaN Mg and generic effective EBL p-doping, but material-specific activation and numerical ionized density still require validation.
- NEXT read-only: inspect actual parameter constant definitions with `grep -nE 'N_Mg_p|N_A_EBL|N_D_n|x_Al_EBL' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd | head -n 40`; if numeric definitions split across lines, `sed -n '95,145p' .../pp1_dvs.cmd`. Then inspect SVisual `n1_msh.tdr` Mg/n dopant and EBL Al fraction spatial profiles, compare with specified Kou-based baseline. No edits or rerun.

## 2026-10-09 — Active 5V_TEST SDE numeric doping constants observed (NOT an error conclusion)

- 이택규 ran `grep -nE -C 3 'N_Mg_p|N_A_EBL|N_D_n|x_Al_EBL' .../JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd | head -n 100`. Live SDE shows `x_In=0.15` at line 100, `x_Al_EBL=0.15` at line 102, `N_Mg_p=9.59e18 cm^-3` at line 119, `N_A_EBL=3e17` at 121, `N_D_n=5e18` at 123, `N_D_bar=1e15` at 125. Prior lines 501-615 show these variables assigned to intended pGaN, EBL, nGaN/base regions.
- **Critical semantic distinction**: `CMP/COMMON_BASELINE.md` documents `p-GaN effective active acceptor≈3e17 cm^-3`, while SDE assigns **raw `pMagnesiumActiveConcentration`=9.59e18 cm^-3**, with specific GaN `IncompleteIonization` and E0=0.2eV etc in SDevice. This is NOT automatically an error: Mg dopant density ≠ actual ionized Mg acceptor concentration, hole density, or effective active acceptor density. But the intended correspondence to documented 3e17 target is NOT YET CALIBRATED/VERIFIED; do not call 9.59e18 physically valid just from ionization declaration. Very high Mg input may present compensation/solubility concerns needing later literature physical validation.
- `N_A_EBL=3e17, N_D_n=5e18, N_D_bar=1e15, x_In=0.15, x_Al_EBL=0.15` match nominal documented model values (subject to actual SDE material/profile assignment). No code or simulation errors in this grep, no need to rerun now.
- JuSubin TIMELINE earlier records a Half+Coarse `DopingConcentration` SVisual screenshot color scale near -9.59e18 to +5e18, suggestive of signed *input/net dopant profile* representation but no pointwise verified ionized Mg/free-hole density or across-layer cutline. Do not equate `DopingConcentration` with p or ionized Mg.
- NEXT read-only, csh-safe: `sed -n '105,128p' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd` (inspect inline comments on rationale for 9.59e18); then probe existing n2_des.tdr for `pMagnesiumMinusConcentration`, `hDensity`, `DopingConcentration` in central Clean_pGaN away from contacts and verify 3e17 target only if this is the intended metric. Later calibration/low-current analysis separately. Preserve all sources/data; no new run.

## 2026-10-09 — SDE Mg calibration rationale from actual 5V_TEST comment (OBSERVED COMMENT, NOT MEASURED hDensity)

- 이택규 read `sed -n '105,128p' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd`. Source comment says: `Mg concentration calibrated previously in this project so that hDensity ~ 3e17 cm^-3 at 300 K with incomplete ionization.` Defined Mg input `N_Mg_p=9.59e18 cm^-3`; EBL effective active acceptor `N_A_EBL=3e17`; n-GaN donor `N_D_n=5e18`; barrier background `N_D_bar=1e15`.
- Distinguish **commented historical calibration intention** from actual reproducible `hDensity`/ionized Mg values: no p-GaN carrier-density probe or calibration condition/equilibrium state was supplied. The comment does NOT prove the current 5 V transient p-GaN `hDensity=3e17`, especially near interfaces/bias. Mg raw input 9.59e18 need NOT be changed to 3e17; do not modify existing .par or do an unnecessary SDE rerun.
- Next action: open preserved `n2_des.tdr` in SVisual, inspect `hDensity` as a 2D field in `Clean_pGaN` at a representative bulk point away from junction/contacts, record coordinates/units/value and bias (5 V). Where available also inspect `pMagnesiumMinusConcentration` (ionized Mg) from same data; check initial 0 V/equilibrium TDR or original calibration artifact before claiming 300 K zero-bias target 3e17 truly reproduced. Do not equate pMagnesiumActiveConcentration or DopingConcentration with free hole density.
- 12/12 NtSide0 sidewall traps verified zero and SDE Mg/EBL/n donor source placements checked earlier. Remaining: effective Mg/holes, donor actual map, 2D J normalization, InGaN SRH calibration and Full/Half comparison. No new run.
