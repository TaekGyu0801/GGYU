## 2026-10-12 CAL4V material parameters
- 이택규의 실제 100ns model parameter-file 검사에서 InGaN Scharfetter taumax=1e-7 s for electrons and holes, taumin=0, Nref=1e16 cm^-3, gamma=1 confirmed. Effective spatial lifetime not confirmed. Next audit model overrides and carrier injection/2D current normalization. No TCAD files changed.

## 2026-10-12 — CAL4V global physics verified, custom par inspection next
- 2026-10-12 이택규 CAL4V의 실제 `pp2_des.cmd` lines 14–90 read-only sed 출력 제공. File: Grid=n1_msh.tdr; Parameters=FASTC1_pp6_des.par; Plot=n2_des.tdr; Current=n2_des.plt; Output=n2_des.log. Electrode anode/cathode both initial Voltage=0.0. Global Physics: Temperature=300.0, Fermi, Thermionic, Piezoelectric_Polarization(strain), DefaultParametersFromFile, EffectiveIntrinsicDensity(NoBandgapNarrowing), Recombination(SRH(), Auger(), Radiative). 이 블록은 세 재결합 모델 활성화의 직접 증거지만 InGaN 유효 SRH tau=100ns 또는 국소 재결합 수치의 근거 자체는 아니다. 이전 whole pp2 grep에는 AreaFactor 미표시; 단자 전류 단위, 2D normalization 미확인. 다른 per-material/per-region Physics overrides, 명시적 surface recombination 설정 존재 여부도 아직 미확인. NEXT 별도 CAL4V custom active par `FASTC1_pp6_des.par`에서 InGaN Scharfetter/SRH tau 및 active material blocks 읽기전용 검사; 이후 pp2 global/local Physics 범위와 current scaling 검증. 서버 파일이나 계산 결과 변경 없음. 주수빈의 5V_TEST split parity/QW integration과 다른 독립 track 유지.

## 2026-10-12 — 이택규 CAL4V model/current read-only audit handoff
- Worker: 이택규 / AI: ChatGPT. CAL4V pp2_des.cmd effective grep observed lines: 20 Grid=n1_msh.tdr; 22 Parameters=FASTC1_pp6_des.par; 26 Current=n2_des.plt; 60 Thermionic; 64 Piezoelectric_Polarization(strain); 462 PE_Polarization/vector; 466 PiezoCharge. The searched AreaFactor is absent. This does NOT prove 2D current normalization or actual active piezo charge magnitude. No source/physics changes. NEXT `sed -n '14,90p' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/pp2_des.cmd`, then check effective parameter file and log for current-unit/physics interpretation. Separate 주수빈 5V_TEST n2/n4 trap-ON/OFF proposed track remains distinct.

## 2026-10-12 — Proposed handoff to JuSubin for 5V_TEST n2/n4 and LeeTaekGyu CAL4V audit
- 2026-10-12 ~17:03 KST, current worker 이택규 says he is now working alongside 주수빈 and wants nonoverlapping tasks. Proposed coordination (not confirmed as accepted by 주수빈): 이택규 owns read-only physical Gate0/low-current audit in separate project `CMP_BASELINE_1.3.0_CAL4V` (2D terminal current units/AreaFactor, active InGaN SRH 100ns, QW injection/EBL/polarization) without source modifications; 주수빈 may own `JUSUBIN_FAST_HALF_5V_TEST` NtSide0 Node2 vs NtSide1e18 Node4 5V parity gate (pp2/pp4 deck and .par/mesh differ only trap) followed by paired MQW Rrad/SRH/Auger integrals, avoiding overlapping CAL4V. Both finished sources/results remain protected. Last user-provided `pp4_des.cmd` grep explicitly showed 12 Traps Conc=1e18, confirming planned NtSide1e18 actual preprocessing (pending pp2-vs-pp4 other-input parity). No fresh simulation or technical result here; this is a PROPOSED parallel work allocation. AI cannot directly send task to collaborator's separate chat; share via GitHub as a proposed handoff only.

## 2026-10-12 — 5V_TEST n4 output confirmed; verify node-specific NtSide before comparison
- 2026-10-12 현재 작업자 이택규가 SWB Node4 Explorer 실제 `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/n4_des.out` 마지막 화면 제공. 노드 n4: 5.000E+00 V, electron current 7.534E-14, hole current 6.975E-12, total terminal current 7.050E-12 (log raw values; 2D units/AreaFactor unverified), successful `n4_5V_ckpt_des.sav` and `n4_des.tdr` writes, `Curve trace finished`, `Sentaurus Device simulation finished`, `Good Bye`. Finished Mon 2026-10-12 00:12:02 KST; wallclock 29806.55s (~8h16m46.55s), CPU total 80172.55s, peak memory 3.11GB. **CONFIRMED 5V SDevice n4 completion**, but screenshot does not show NtSide parameter: intended n4 NtSide1e18 split condition NOT CONFIRMED until pp4_des.cmd actual DmgL trap `Conc` audit and parent n2 input comparison. Previous 5V_TEST NtSide0 n2 terminal raw I2D~1.4480164608e-11, so n4 raw current ratio ~0.487; no trap-only causal claim without pp2/pp4 parity. CAL4V 100ns 4V MQW radiative fraction=0.0122426% remains distinct simulation and bias; do not confuse n4 5V with CAL n2 4V. GitHub COMMON_BASELINE.md explicitly says blue InGaN/GaN, xIn=0.15 4QW, nominal ~445nm; desired color BLUE not red, spectral peak not verified by EL. Researcher asks whether normal efficiency '0.1': distinguish fractional 0.1=10%, 0.1%=0.001 as fraction, 0.1 A/cm2 current density not an efficiency. None is default expected at arbitrary J; literature (Kou 2019 10.1364/OE.27.00A643; Baek 2023 10.1038/s41467-023-36773-w; Wang 2023 10.1038/s41467-023-43472-z) confirms blue microLED efficiency depends on J, fabrication and sidewalls. CAL 0.01224% is modeled MQW 3-mechanism radiative share, NOT observed experimental EQE, and physical low-J Gate0/2D current normalization still open. NEXT read-only `grep -nE 'Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp4_des.cmd | head -n 16` to confirm actual trap concentrations. Further compare pp2/pp4 other physics/current and matched 5V QW recombination; preserve all existing outputs. No server code modified.

## 2026-10-12 — Low-J baseline gate literature and next check
- 2026-10-12 Research assessment (이택규 question whether CAL4V radiative fraction 0.01224% is typical): Treat result as unusually low vs peer-reviewed working MicroLEDs, NOT sufficient proof of a model defect. Evidence: CAL4V 4.000V 2D raw terminal current 3.498e-14 (assuming A/µm), conditional half width ≈2µm gives J=(3.498e-14/2)*1e8≈1.749e-6 A/cm²; current conversion/AreaFactor/actual injection/steady-state remains unverified. Thus this is ~0.01/1.749e-6 ≈5718x below a published low-J example 0.01 A/cm² and ~0.1/1.749e-6≈57176x below 0.1 A/cm² benchmark. Published 3.5µm NBE-etched blue MicroLED Nature Communications 2023 DOI 10.1038/s41467-023-43472-z reports peak EQE 37.5% around 3 A/cm² and at 0.01 A/cm² only ≈26% relative droop; Nature Communications 2023 DOI 10.1038/s41467-023-36773-w reports 10x10µm blue MicroLED EQE 3.00% at 0.1 A/cm². Neither EQE benchmark is directly comparable to this model's MQW three-rate radiative share due to injection, geometry, sidewall processing and extraction differences. SRH normally dominates extremely low-current regime (literature-supported), but here NtSide0 still high SRH implies bulk/volume SRH or injection bottleneck rather than explicit sidewall trap; cannot infer causal parameter without matching sample and checking effective par. Existing parent 1ns at 5V had 0.10947% integrated QW fraction; CAL100ns at 4V is NOT matched bias, so changing lifetime cannot be causally judged. Recommended PRIORITY: verify current units, 2D AreaFactor, actual working J, effective InGaN 100ns parameter overrides, p/hole-injection/EBL/polarization/quantum well carrier densities, compare QW rates at same current and bias before baseline freeze, and avoid unmotivated long reruns. This is literature-backed review/diagnostic recommendation; NO simulation/model edit or confirmation of a single root cause.

## 2026-10-12 — CAL4V 4V full MQW integrated, distinct NtSide split verification pending
- 2026-10-12 이택규가 Sentaurus Visual 캡처 3장으로 완료된 `CMP_BASELINE_1.3.0_CAL4V` `n2_4V_final_des` (4.000V; custom InGaN 100ns Scharfetter taumax model) 8개 **2D** QW 영역 `Clean_QW1..4 + DmgL_QW1..4` 적분 결과를 제공. 세 필드 모두 정확히 동일 영역, Total Domain=2.400002e-02 µm². 전체 적분값 [s^-1 µm^-1]: RadiativeRecombination=6.286680e-04; srhRecombination=5.134239; AugerRecombination=2.127778e-04. 합=5.1350804458. Radiative/(Rrad+SRH+Auger)=0.01224261249%; SRH share=99.98361378%, Auger=0.004143612%. 여기서 방사비율은 해당 세 재결합 필드의 **MQW spatial integrated radiative fraction**이며, 100ns 모델 소자/실험 검증 IQE 또는 EQE가 아님. QW1 Clean+DmgL accounts for approx 98.78% all-4QW Rrad. DmgL 4QW only radiative ≈5.35942e-05 and SRH≈0.020185 (subtract clean 4QW totals; rounded), not independent lifetime physics validation. Preexisting 1ns parent result (NtSide0, **5V**) 4-QW Clean+DmgL Rrad=40072.8158452, SRH=36562944.9075, Auger=1599.706168587 and radiative fraction=0.1094747566%; because these are at DIFFERENT biases (100ns 4V, 1ns 5V), cannot attribute change to lifetime or claim 100ns improves/worsens IQE. Parent 4V near-terminal-current PLT exists but 4V TDR spatial map not yet established. Low-J Gate0 and current-normalization/physical validity still UNRESOLVED. Next inspect other user-reported completed NtSide1e18 split normal-finish log; for IQE causality compare same J/voltage/regions/geometry and effective .par, ideally reuse saved checkpoints, avoid rushing new multi-day run. No code/server run changed.

## 2026-10-12 — Handoff clean-four-QW analysis
- CAL4V final 4V/100ns SVisual screen: 4 Clean_QW1..4 integrated Rrad total=5.750738e-4, SRH total=5.114054, Auger total=2.046436e-4 (s^-1 um^-1); total area=0.02394002 um2. Clean-only radiative fraction 0.01124326%. DmgL_QW1..4 NOT included; do not treat as full MQW or device IQE. Next add these 4 damaged 2D QW regions and integrate same fields, then check against matching 1ns bias/current and low-J Gate0. Evidence: screenshot supplied by 이택규.

## 2026-10-12 — Handoff: CAL4V QW1 integrated; remaining QWs required
- 2026-10-12 이택규 공유 SVisual `CMP_BASELINE_1.3.0_CAL4V/n2_4V_final_des` Field Integration 실제 결과: Dimension 2 region `Clean_QW1` 하나만 선택, Domain=5.985012e-03 um^2; RadiativeRecombination=5.674131e-04 s^-1 um^-1; srhRecombination=4.940556 s^-1 um^-1; AugerRecombination=2.045051e-04 s^-1 um^-1. 3항 합=4.9413279182 s^-1 um^-1. Clean_QW1에 한정한 radiative fraction =0.0114830084%, SRH fraction=99.9843783%. VERIFIED screenshot-based single-region integrations and ARITHMETIC; NOT entire four QWs, not total device IQE. Other QWs may differ substantially. Next integrate 2D volume Clean_QW1..4 AND DmgL_QW1..4 in all three fields (avoid `Clean_QW1+DmgL_QW1` interface rows if shown as Dimension 1). Compare 100ns 4V with 1ns at matched V/J and check current normalization. No TCAD source edits. NtSide1e18 split separate log verification remains.

## 2026-10-12 — Handoff: CAL4V voltage achieved; QW analysis next (OBSERVED)
- 이택규가 실제 `CMP_BASELINE_1.3.0_CAL4V/n2_des.log` grep 출력 공유. 마지막 `Computing BE-step from 0.799739 s to 0.8 s (Stepsize: 2.6098e-04 s)` 직후 `anode 4.000E+00 5.270E-20 3.498E-14 3.498E-14`가 표시됨. 직전 단계 0.798939→0.799739s에서는 anode 3.999V, 총전류 표기 3.496E-14. 앞서 확인된 동일 Node2 `Curve trace finished` / `Good Bye` 및 final `n2_4V_final_des.tdr`, `n2_4V_ckpt_des.sav` 저장과 연결되므로 100ns CAL4V에서 최종 time 0.8s / anode 4.000V, 로그 전류 마지막 열 3.498E-14 달성과 정상 완료 CONFIRMED. 로그 전류 물리 단위/2D AreaFactor 및 정상 DC상태는 독립 검증 미완료; 기존 기록의 2D A/um 관행에 따른 원시 수치이며 조건 없이 면적 전류밀도나 IQE로 간주하지 않는다. 참고: 기존 1ns 5V_TEST 가까운 4.003369V에서 I2D=3.505521343e-14였고 CAL4V 4.000V와 약 0.2% 원시 전류 차이이나 서로 완전한 동일 바이어스 아님. 100ns의 재결합 개선 여부 미확정. NEXT 이미 확보한 final TDR의 4QW별 Radiative/SRH/Auger 적분과 비교전류 정상화 후 연구 판단; 별도 NtSide1e18 split은 실제 로그 미검증. 원본 데이터 보존.

## 2026-10-12 — CAL4V completed; outcome analysis handoff (OBSERVED screenshot)
- Current worker: 이택규; source run by: 주수빈; AI: ChatGPT.
- Screenshot supplied by current worker 이택규 of SWB Node 2 Explorer in `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/n2_des.out` confirms `Curve trace finished.`, `Plot(FilePrefix="n2_4V_final")` written to `n2_4V_final_des.tdr` successfully, `Save(FilePrefix="n2_4V_ckpt")` wrote `n2_4V_ckpt_des.sav` and circuit .sav, `n2_des.tdr` written, `Sentaurus Device simulation finished`, `Good Bye !`. Completed on Mon Oct 12 01:12:13 2026 (KST); wallclock 29706.72s (~8h15m6.72s), total CPU 84070.27s (~23h21m10.27s), peak memory 4.05 GB. Status **OBSERVED/CONFIRMED NORMAL SDEVICE FINISH and saved spatial final state**, replacing prior RUN-CLICKED-ONLY uncertainty for this CAL4V n2. Important: screenshot tail does NOT show numeric final anode V/current, nor `pp2_des.cmd` active physics/Goal/FinalTime, so numerical 4.000V endpoint and current/IQE are NOT YET EXTRACTED/INDEPENDENTLY VERIFIED. Prior source Goal=4.0, FinalTime=0.8, InGaN Scharfetter taumax 100ns were reviewed in previous conversation. Other reportedly completed NtSide=1e18 split not yet supported by its own log. Baseline physical Gate0 (low J, radiative fraction ~0.1095% old 5V) remains open. Protect saved results and existing 5V parent. Next: read-only last bias/current in n2_des.log or n2_des.plt, inspect n2_4V_final_des.tdr, extract 4 QW integrated radiative/SRH/Auger and compare matched V/J to old 1ns; independently inspect NtSide1e18 node output.

## 2026-10-12 — Handoff: 두 run 완료 사용자 보고 / 실출력 검증 필요
- 제보자/현재 작업자: 이택규; 원래 실행한 연구자: 주수빈; AI: ChatGPT.
- 이택규가 2026-10-12 대화에서 주수빈이 전날 실행해 두고 간 '두 개' 시뮬레이션이 모두 끝났다고 보고. 직전 인수인계상 대상은 (1) 기존 `JUSUBIN_FAST_HALF_5V_TEST` 기반 NtSide=1e18 split과 (2) `CMP_BASELINE_1.3.0_CAL4V` (100ns, 0→4V)로 추정되며 **어느 두 SWB node인지 실제 로그나 화면으로 확인하기 전까지 프로젝트/노드 매칭 미검증**. 사용자 보고는 완료 주장의 근거이나 actual SDevice `Good Bye`/final V/timestep/terminal current/PLT/TDR/SAV는 미제공. NtSide=1e18 case가 NtSide-only matched input인지도 재확인 필요. 새 런이나 baseline freeze를 의미하지 않음. 기존 5V_TEST NtSide0 및 5V CAL 보호. 다음: 두 SWB 노드 이름, `n*_des.log` 마지막 35~50행, `pp*_des.cmd` Goal/Trap, 생성 PLT/TDR/SAV 확인→주입 전류 및 4QW Rrad/SRH/Auger를 동일 바이어스/전류 조건에서 비교. Gate0 낮은 J, 물리적 IQE/Full-Half 검증은 계속 미해결.
- READ FIRST: two project node IDs, last nN_des.log lines and ppN_des.cmd, generated final PLT/TDR/SAV. Already failed old trap-ON run and original 5V CAL must not be mixed with newly reported run.

## 2026-10-11 — CAL4V Run clicked (USER-REPORTED, actual solver status pending)
- 주수빈 confirmed cloned CAL4V source `FinalTime=0.8` and clicked SWB **Run** for `CMP_BASELINE_1.3.0_CAL4V`. Previous actual screenshot independently showed `Goal anode Voltage=4.0`, final Plot `n@node@_4V_final`, Save `n@node@_4V_ckpt`, cloned custom InGaN Scharfetter electron/hole `taumax=1e-7s`. Keeps 5V/s ramp.
- Status **RUN REQUESTED by researcher**, not yet independently OBSERVED SDevice process/preprocessed deck/accepted BE-step and certainly NOT completion. Current 4V TDR/SAV absent/unconfirmed. Do not interrupt running original 5V CAL or preserve-solved 5V_TEST parent. NtSide1e18 split run still unverified.
- NEXT read-only in new CAL4V folder: `ls -lt n*_des.log n*_des.err n*_des.out 2>/dev/null | head -n 12`, then actual nN_des.log tail, preprocessed ppN Goal/FinalTime/Plot/Save/Parameter. Check SWB SDevice node state. Initial failure/syntax errors before overnight run are high priority; do not claim CAL4V will finish today. Physical low-J Gate0 persists.

## 2026-10-11 17:39 KST — CAL4V clone is still original 5V source
- OBSERVED grep of newly cloned `CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd`: `FinalTime=1.0`, `Voltage=5.0`, `FilePrefix=n@node@_5V_ckpt`; previous multiline script did not apply.
- Gave JuSubin short terminal commands `cd` to clone, `cp -pn sdevice_des.cmd sdevice_des.cmd.bak_5V`, `sed -i -E` changing FinalTime1→0.8, Goal Voltage5→4, 5V_ckpt→4V_ckpt, then GNU sed insert post-transient `Plot(FilePrefix="n@node@_4V_final")` immediately before end Save. Await user execution: NOT yet confirmed applied.
- Original active CAL5V and completed parent must not be touched. Next inspect `tail -n 40 sdevice_des.cmd` and `grep ... InGaN .../FASTC1_pp6_des.par` for 100ns, optional intermediate t0.76 Plot/Save after file structure confirmation; SWB Preprocess before Run. Low-J Gate0 persists.

## 2026-10-11 17:28 KST — JuSubin 4V CAL Python heredoc still in terminal continuation (OBSERVED)
- MobaXterm screenshot displays `?` continuation prompt for pasted Python code and closing `? PY`, but **no SUCCESS/STOP or normal prompt**. The clone source edit is unverified; this is an interactive-shell input state, not SDevice solver failure. Advise one Enter on closing PY; if `?` persists Ctrl+C, explicitly enter bash and retry script. Read-only `grep -nE 'FinalTime|Voltage|3p8V|4V_final|4V_ckpt' .../CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd` plus backup listing before SWB Preprocess/Run. Active 5V CAL and parent 5V_TEST unchanged as far as evidence shows.

## 2026-10-11 17:20 KST — JuSubin 4V CAL source-tail screenshot
- Original running CAL source observed: anode Goal5V, FinalTime1.0, Increment1.2, InitialStep1e-5, MinStep1e-9, MaxStep1e-3, coupled15; one 5V Save after transient. Stale comment 0.3V ignored.
- Copy/paste change proposed for NEW clone only: FinalTime0.8, Goal4.0, intermediate Plot/Save at t0.76, final Plot+Save 4V, preserve 100ns InGaN .par. No running jobs or source changed yet. Next SWB Clone→edit→Preprocess verify→Run. Record run only on user proof.

## 2026-10-11 — JuSubin: separate 100ns CAL 4V clone requested; NOT RUN
- DECISION: clone live `CMP_BASELINE_1.2.0_CAL` to versioned project (candidate `CMP_BASELINE_1.3.0_CAL4V`, check name uniqueness), keep active CAL as-is. User plans a 4V run with 100ns InGaN SRH and NtSide0, besides separate 5V_TEST NtSide1e18 split.
- Draft source changes only in cloned `sdevice_des.cmd`: Transient Goal anode 5V→4V and FinalTime1→0.8 to keep ramp 5V/s, add post-ramp 4V Plot TDR + Save checkpoint. Need actual source Solve tail and pp2 lines 580–612 before final exact patch; never edit generated pp2. Preprocess validate then Run.
- No server code edit/job start/abort has been observed; physical low-current baseline Gate0 unresolved. Preserve original results and active jobs.

## 2026-10-11 — JuSubin DECISION: 5V_TEST parent NtSide0 → NtSide1e18 split now (RUN UNVERIFIED)
- Due to very slow 100ns CAL, researcher chooses prior completed `JUSUBIN_FAST_HALF_5V_TEST` NtSide0 5V as **working numerical comparison parent** and NtSide=1e18 SDevice split; this does NOT certify physical common baseline or indicate new run already launched. CAL ongoing/unchanged, parent 5V outputs must stay preserved.
- Sep26 trap-on Node12 fail involved stale/nonidentical source or parameter revision, so only clean same-input `ppN_des.cmd/par` NtSide-only comparison passes the pre-run gate. First preserve n2 5V logs/PLT/TDR, add NtSide=1e18 parameter case with original 0 case intact; preprocess before costly RUN; verify all damaged-region Conc, no other Physics/Math/Solve/custom .par change, intended 5V Goal and no stale cached 0-case. Run trap-on only after checks. No new server actions confirmed yet.
- Gate0 physical low J and 0.10947% QW radiative fraction not resolved; Project A/B paper-grade baseline still not frozen. NEXT screenshot SWB split tree or ppN_des.cmd to validate then run.

## 2026-10-11 — Prior low-J audit already performed by LeeTaekGyu (HANDOFF CORRECTION)
- User JuSubin correctly pointed out historical sequence: Oct9 parent 5V_TEST 4QW regional Rrad/SRH/Auger integrals and actual InGaN.par Scharfetter 1ns maximum lifetime were inspected by LeeTaekGyu; excessive SRH from overly short lifetime became a **hypothesis**.
- Oct10 clone CAL custom .par **actually updated** to InGaN Scharfetter taumax=1e-7s (100ns both carriers) and saved on server (confirmed by tail; change should not be repeatedly questioned as though never made). Same geometry and numerics parent remained a numerical reference. 100ns max is not uniform effective lifetime or proof it fixes terminal low-J.
- At approx 4.0V, prior 5V_TEST I2D 3.505521343e-14 A/um at 4.003369V and CAL I2D 3.497895e-14 A/um at 3.999674V (~0.22% raw difference at slightly different bias), no observed improvement in electrical current at that comparison point. No CAL ~4V spatial QW IQE TDR yet; 5V CAL incomplete.
- Stop proposing to redo the **already completed** prior baseline SRH / MaterialDB investigation. Next question is whether 100ns affects recombination/IQE at matched injection, while isolating distinct carrier transport/current density normalization concern (Gate0). Preserve CAL and finished parent, no code/job action.

## 2026-10-11 — 주수빈: 5V_TEST working baseline proposal
- Proposed, not adopted/frozen: use completed NtSide=0 JUSUBIN_FAST_HALF_5V_TEST as numerical reference rather than waiting for CAL. SDevice finished 5V Oct9; preserve both jobs/decks.
- Blocker: 5V nominal J ~7.24e-4 A/cm2 conditional, very low QW radiative share; 2D normalization, effective recombination, NtSide1e18, Half vs Full unvalidated. No server input edits.
- Next: audit saved 5V_TEST terminal currents and TDR injection physics read-only, then plan a controlled separate short calibration trial only upon approval. Project A/B production not ready.

## 2026-10-11 — 주수빈 4V diagnostic cutoff requested (PROPOSED, not adopted)
- User worries 100ns CAL 5V ramp costs too much time; asks whether 4V endpoint is acceptable and why 5V was originally chosen. GitHub `COMMON_BASELINE.md` documents initial forward sweep 0→5V but does not identify 5V as a mandatory physical turn-on or operating voltage.
- 4V can bound a **separate diagnostic pilot**, but 4V alone cannot validate the baseline while 5V_TEST low-J Gate0 remains unresolved. Current CAL PLT near 4V raw I2D 3.497895e-14 A/um (conditional J ~1.75e-6 A/cm² for 2um width, 2D normalization and displacement not validated). Existing nominal 5V_TEST J ~7.24e-4 A/cm² is already low under documented convention.
- Old 0→5V reference and running CAL protected; current CAL already accepted ~4.179V and post-transient `Save` cannot retrospectively yield a 4V TDR. Any new shortened run needs versioned copy, maintained comparison conditions, explicit 4V spatial `Plot/Save` and controlled validation. No server edits.
- NEXT read-only `sed -n '580,612p' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/pp2_des.cmd` for goal/ramp; check effective 100ns par before claiming calibration, discuss user decision about new 4V pilot vs running CAL. NOT confirmed baseline freeze.

## 2026-10-11 16:46 KST — 주수빈 CAL Save placement confirmed
- OBSERVED in live node2 `pp2_des.cmd` screenshot: `Save(FilePrefix="n2_5V_ckpt")` is after the transient block; no intermediate time-specific Plot/Save lines in grep. `Plot="n2_des.tdr"` declares an output file, not a 4V snapshot. 4V PLT terminal I-V is available; 4V TDR unknown.
- File points to `FASTC1_pp6_des.par`. Comment claims 0–0.3V smoke but actual run accepted ~4.179V. Actual Goal is in unseen code lines.
- Blocker: no confirmed spatial ~4V IQE map and very low-J Gate0; 5V CAL status pending. No code or active job modifications. Protect common baseline.
- Next read-only: `sed -n '580,612p' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/pp2_des.cmd`; then inspect existing spatial output locations and effective 100ns override. Do not abort active CAL.

## 2026-10-11 ~16:45 KST — JuSubin locates CAL pp2_des.cmd (OBSERVED)
- READ-ONLY `ls -lh .../CMP_BASELINE_1.2.0_CAL/*des.cmd` screenshot verifies three files: `FASTC1_pp6_des.cmd`, `pp2_des.cmd`, `sdevice_des.cmd`. Node2 `pp2_des.cmd` present (~5.8 KB, Oct10 00:40). No file body/Plot/Save schedule was printed yet; no proof of a 4V spatial TDR.
- Previous accepted 100ns CAL state ~4.179 V; screenshot shows old log only and cannot establish further progress. Existing low-J baseline Gate0 unresolved.
- NEXT read-only inspect `grep -nEi -C 4 'Plot|Save|CurrentPlot|Time[[:space:]]*=' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/pp2_des.cmd | tail -n 120` and, if appropriate, alternate TDR locations. No changes to CAL process, solver or source.

## 2026-10-11 ~16:41 KST — 주수빈 CAL 100ns 4.179V read-only handoff (OBSERVED)
- Worker 주수빈 / ChatGPT. Source: current MobaXterm `CMP_BASELINE_1.2.0_CAL/n2_des.out` screenshot. Accepted BE 0.835804→0.835806s with RHS 7.30e-4 (<RHSMin 1e-3); accepted anode 4.179E+00 V, TotalCurrent 5.555E-14 A/um (2D convention). Voltage sweep to 5V ~83.58%, not wallclock percentage; increment from previous CAL 4.14965446V PLT ~0.029V.
- Next trial 0.835806→0.835808s, Newton RHS iter2–6 1.03e-3–1.09e-3; screen ends mid-step, later success/cutback/failure unknown. Do not confuse with separate completed `JUSUBIN_FAST_HALF_5V_TEST` or earlier failed FAST_C1.
- Blockers unchanged: low-current Gate0, 100ns CAL 5V not yet verified, no confirmed CAL ~4V saved spatial TDR and thus IQE/QW maps not extractable solely from PLT.
- Already tried: read-only CAL PLT at ~4V, top-level n2 file listing (no n2*.tdr/sav), tail log observation. No failed new remedy; no code changes. Baseline-protected 4um mesa, 5nm damage, common A/B contacts/physics must remain unchanged.
- NEXT: do not stop/abort active CAL without user decision. Read-only inspect current `n2_des.log`/`n2_des.out` and actual existing command file (`ls .../*des.cmd`), Plot/Save schedule, and potential nested/alternate TDR output before discussing early termination. No user/server action taken in this turn beyond screenshot review.

## 2026-10-10 ~22:38 KST — JuSubin CAL 100ns 4V spatial checkpoint handoff
- WORKER 주수빈 / AI ChatGPT. OBSERVED on user's shell screenshot: read-only `find .../CMP_BASELINE_1.2.0_CAL -maxdepth 1 -type f -name 'n2*' ...` prints `n2_des.err 12KB`, `n2_des.job 4KB`, `n2_des.log 5120KB`, `n2_des.out 5376KB`, `n2_des.plt 1416KB`, `n2_des.sta 4KB`, `n2_local.err 0KB`; no top-level n2 TDR or SAV. Previously confirmed near-4V PLT row V=3.99967374V, time=.79993475s, terminal 2D I=3.497895e-14 A/um. The PLT only gives terminal transient data, not volumetric QW recombination maps; 4V TDR availability currently UNRESOLVED.
- No solver/control/source file changes have been made, **do not Stop/Abort running CAL**. NEXT READ-ONLY find actual command file and inspect Plot/Save schedule (e.g. `ls .../*des.cmd`; `grep -nEi -C 3 'Plot|Save|CurrentPlot|FinalTime|Time[[:space:]]*=' .../n2_des.cmd`). Check for TDR in nested/other-named files if needed. Keep Gate0 low-injection unresolved, no baseline freeze/A-B production.

## 2026-10-10 22:30 KST — JuSubin 4V CAL retrieval handoff (OBSERVED)
- Worker: 주수빈 (ChatGPT). Source: user's screenshot of terminal read-only parse of `CMP_BASELINE_1.2.0_CAL/n2_des.plt`.
- Real near-4V record: transient time 0.79993475s; V=3.99967374; `anode TotalCurrent=3.497895e-14` (2D A/um). Last record shown: time 0.82993089s; V=4.14965446; I=4.839436e-14 A/um. 100ns refers InGaN SRH lifetime (not transient time step). PLT text format has 17 fields; index0 time,index9 anode OuterVoltage,index15 anode TotalCurrent.
- Researcher asks whether 4V can replace 5V due slow convergence beyond 4V. Answer: 4V usable for read-only transient I–V sensitivity and intermediate diagnostics; not yet validated baseline/optical IQE, because low-J Gate0 unresolved and TDR spatial checkpoint at 4V not confirmed. Need ensure terminal current excludes displacement if interpreting as diode conduction. DO NOT stop/abort running CAL before checking TDR/Save.
- Next: read-only check saved n2*.tdr/n2*.sav in CAL, actual output time/bias state and Plot/Save directive; preserve original baseline/5V_TEST and CAL. No software changes executed.

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

## 2026-10-10 — successful 5V_TEST Thermionic vs Piezo model log context inspected (OBSERVED; no physics bug proven)

- 이택규가 성공한 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` lines 345–425 실제 서버 출력을 제공. 셸 첫 입력이 두 `sed` 명령이 합쳐져 `.../n2_des.logsed` 파일 에러를 출력했으나 **뒤따른 동일 출력으로 필요한 본문을 정상 확보**, TCAD 자체 오류와 무관.
- 실제 물리 모델 설명: `With Thermionic Emission at heterointerfaces for electrons and holes` 바로 아래 `Without Piezo`; 별도 항목 `Without polarization` (line373), `Piezoelectrice Activation = 1` (line379), `Piezoelectric polarization model: strain` (line416), `With default parameters from file`, 이어 `Clean_pGaN` region override `With incomplete ionization` (line425 onward). 또한 이전 grep line803 `ThermionicEmission: Formula = 1, instead of: 0 [1]`. **Formula1 인식/이종계면 thermionic 켜짐 확정.**
- `Without Piezo`는 ThermionicEmission 하위 옵션 문맥에 있고, `Without polarization`는 strain piezo 모델 자체 상태와 구별해야 하는 별도 물리 설정 출력으로 보임. **근거만으로 실제 interface polarization charge 분포가 올바르거나 전역 piezo가 OFF라는 결론 불가**. No Piezo file도 model OFF 증거가 아님. 파라미터/분극 값을 수정하지 말 것.
- 계산 성공한 5V_TEST의 low J (~7.24e-4 A/cm2 nominal) 물리 원인 remains UNRESOLVED. Alias Plot deprecation warnings nonfatal. Next rather than repetitive grep/screenshots, use existing band, quasi-Fermi & density observations to prioritize a targeted quantitative injection/transport audit (exact layer boundary/QF drops and effective polarization charge); new experiment only after validated causal hypothesis and user approval.
- No server/TCAD code/CAL job changes.

## 2026-10-10 — Claude v2 independent CMP audit submitted; low-current Gate 0 prioritized (DOCUMENT-BASED REVIEW / PROPOSED)

- 작업자 이택규가 Claude 작성 `CMP MicroLED TCAD — 독립 중간 기술감사 및 연구계획 재수립 (v2)` 전문을 채팅 업로드함. **Claude의 독립 감사 의견이며 이번 메시지는 새 실험/로그가 아님.** Claude는 GitHub 기록과 구 FAST 입력은 보았으나 5V_TEST/CAL 현재 실제 pp/log/TDR을 직접 읽지 못했다고 보고함.
- Claude의 핵심 의견: JUSUBIN_FAST_HALF_5V_TEST NtSide0 5V transient 성공(~10596.76s)에도 raw I2D=1.44801646e-11 A/um, half mesa width≈2um, assumed AreaFactor1이면 nominal J≈7.24e-4 A/cm²; QW Rrad share≈0.1095%. 충분한 구동 전류·주입·IQE 검증이 **Baseline freeze 이전 Gate 0**이 되어야 함. 수치는 기존 GitHub 감사 기반이며 새 측정 아님. `not turned on` 결론은 비교대상 J–V/전류 정규화 검증 전에는 물리 가설로 남김.
- 수용 가능한 점: 5V_TEST 계산 플랫폼 보존, high-bias FAST_C1 n6 ~4.801V step-size failure는 재실행 보류, CAL n2 100ns sensitivity current reported ~4.144V accepted unverified로 관찰·중단 사용자 승인 필수; A/B 동일 J·null controls, τ sensitivity, QW와 Cedge 총 비방사, transient trap DC check, stripe vs 3D 형상 한계 분리.
- 별도 검증 필수: Claude가 제시한 활성층 외 `2.9V drop`은 단일 QW n,p, ni 가정 기반 추정이지 밴드/준페르미 지도에서 측정된 전압 분배 아님. 분극 activation/thermionic/EBL를 저전류 확정 원인으로 판단 금지. FAST half/full ~1% 동일은 4.798 vs 4.801V 단일 단자전류의 근사 보정이므로 메쉬 수렴·공간발광 정확도는 미증명. 2D stripe perimeter/area가 4um square보다 2배 작은 기하학적 사실에서 실제 SRH 2배 과소평가를 단정할 수 없음. 1D pilot 분 단위/10월23일 초록 데드라인/수치 PASS 기준은 Claude의 제안이며 별도 확인 필요.
- 우선순위 제안: **S0 원본 5V_TEST 결과의 구동 전류/J 및 potential/band/quasi-Fermi 분포 점검(기존 TDR)** → **S1 EBL doping/polarization/thermionic interpretation 및 재결합 영역별 전류 회계** → 원인 가설이 분리되면 기존 소자 보존한 별도 소형 1D/pilot 설정 검토(사용자 승인 전 미실행) → NtSide0/1e18 동일 J → A/B. CAL은 보고서의 임의 시간·전압 임계치만으로 중단 결정하지 않음.
- 서버/SWB/코드/CAL 변화 없음. Claude에게 직접 메시지 보내지 않음.

## 2026-10-10 — Claude independent mid-project review handoff prepared (PROPOSED / NOT SENT)

- 이택규 요청으로 ChatGPT가 Claude에게 복사할 독립 기술감사 프롬프트 작성: 공통 MicroLED baseline 및 A C-edge/B AlGaN-side-barrier 목적, 세 버전 비교(5V_TEST success ~10596.76s, FAST_C1 4.801V failed ~525152.85s, CAL 100ns candidate last accepted ~4.142V), 최근 pp inputs 및 failure evidence, Mg/2D J/IQE model validation, minimal-cost go/no-go roadmap.
- 구분: 계산 성공은 물리적 calibration success가 아님. FAST_C1 실패는 MinStep reached direct cause이며 underlying Newton instability unresolved. CAL 100ns effective application and 5V outcome unverified; no conclusion same-root-cause. Claude를 통한 리뷰 요청은 사용자 전달을 기다리는 단계이며 AI가 Claude 채팅에 직접 전송한 것이 아님.
- NEXT: 사용자 Claude 리뷰 결과를 현재 Github evidence와 비판적으로 대조. School server jobs and inputs untouched.

## 2026-10-10 (last log time unspecified) — FAST_C1 n6 tiny BE-steps oscillate near 4.801V; final minimum step failure (OBSERVED)

- Worker 이택규 supplied filtered **actual** `GaN_PiN_Diode_FAST_C1/n6_des.log` tail. Pseudo-time printed `0.960247 s` on successive BE attempts (6 decimal digits only), corresponding to ~4.801235 V at unchanged 0→5V ramp. Last repeated anode printed `4.801E+00V`, not proof exact zero time advancement.
- Seen rejected timestep trials: `9.0176e-08, 4.5088e-08, 2.2544e-08` s; some intervening **accepted** attempts printed with anode current (e.g. following `1.1272e-08, 6.7632e-09, 1.0145e-09` s). Newton alternated failures and very small accepted progress. Last rejected attempt `1.2174e-09 s` immediately followed by `Step-size is too small.`
- If the previously documented `MinStep=1e-9 s` is indeed active in **this actual pp6 deck**, next 0.5× cutback = `6.087e-10s`, explaining stopping threshold. This must be verified against `GaN_PiN_Diode_FAST_C1/pp6_des.cmd` (not yet shown).
- Earlier detailed n6 Newton tail alternated electron C-norm errors ~0.966 and ~74.4 at adjacent x=0.119–0.120um, y=2.617188um; Poisson and hole errors small there. **Electron-equation instability seen, underlying physics/material/mesh root cause unproven**; cannot blame Mg/traps without regional/model checks.
- Prior process end: 2026-10-10 17:39:07 KST after 525152.85s wallclock, n6_des.tdr written at failure. No successful 5V. Last 4.801V/5V≈96.02% *voltage* sweep only.
- CAL n2 separate: latest direct observed ~4.142 V accepted, 5V/100ns override unresolved; no new CAL evidence in this turn. Preserve active CAL and prior completed 5V_TEST parent.
- NEXT READ-ONLY: inspect exact preprocessed FAST_C1 pp6 `MinStep`, `Iterations`, `RHSMin`, and solving block; save logs/tdr; do not merely lower MinStep, rerun 145h or claim saved TDR is restart checkpoint. No school-server changes.

## 2026-10-10 after 19:02 KST — FAST_C1 n6 MinStep failure confirmed; CAL n2 advances to ~4.142 V (OBSERVED LOG)

- 작업자 이택규가 학교 서버 실제 터미널 로그 두 개 제공. FAST_C1 `GaN_PiN_Diode_FAST_C1/n6_des.log` (NtSide=0)는 반복 Newton 15회 초과 후 `Newton didn't converge, trying again with smaller timestep...` 그리고 `Finished, because... Step-size is too small.`가 나타남. 2026-10-10 17:39:07 KST 정상 프로그램 종료 메시지 `simulation finished`, `Good Bye !`, `n6_des.tdr` 쓰기 및 라이선스 반환이 있더라도 5V 목표 달성/물리적 성공이 아니라 **수치적 최소 time-step 실패**. Wallclock 525152.85s ≈145h52m32s, peak mem 5.94GB. 마지막 accepted voltage는 제공된 50줄에 없어 UNRESOLVED; 깊은 원인(물성/mesh/수치 설정) 역시 확정 불가.
- 별개 프로젝트 `CMP_BASELINE_1.2.0_CAL/n2_des.log`에서 t=0.828339→0.828343s BE step은 Newton 2회 후 `|RHS| less than 1e-3`로 accepted, 표기 anode=4.142E+00 V, total current=4.678E-14 raw. 기존 4.138V보다 약 0.004V 진전(4.142/5≈82.84% 전압 구간이지 walltime 아님). 후속 t=0.828343→0.828348s attempt은 Iteration 11까지 `RHS≈1.09e-03 >1e-03`; 스크린샷/로그가 중간에 끝나 아직 accepted/failure 미확인. 5V 완료·tau_max=100ns 실제 유효성·ETA 미확인.
- 변경: GitHub 진단 기록뿐. 학교 서버 소스, SWB, 실행 중 CAL, 완료된 `JUSUBIN_FAST_HALF_5V_TEST` 결과는 건드리지 않음.
- NEXT READ-ONLY: `grep -n 'anode ' /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1/n6_des.log | tail -n 5` 로 FAST 마지막 성공 전압을 확인하고 n6_des.sta/err 및 버전 비교. CAL은 시간 경과 뒤 tail로 accepted t/V, `Newton didn't converge`, step-size, fatal/Good Bye 여부 확인. FAST n6 즉시 재실행 또는 MinStep/Iterations 임의 완화 금지.

## 2026-10-10 ~19:02 KST — 이택규 SWB 빨간 FAST_C1 n6 / 진행 중 CAL n2 구분 필수 (UNRESOLVED)

- 증거: 사용자가 제공한 T-2022.03 SWB 이미지. 활성 트리 선택 `GaN_PiN_Diode_FAST_C1`; NtSide0 `[n6]` red failed (default palette), `[n12]` pale blue, n1 yellow. 실제 n6 error log 아직 제공되지 않음. `CMP_BASELINE_1.2.0_CAL`은 같은 트리의 다른 프로젝트이며 이 캡처에 실행 상태 안 나옴.
- 마지막 CAL 직접 로그(주수빈, ~18:08 KST): n2 약 4.138V, Newton 15 반복 후 cutback, 5V 미완료. 사용자 보고도 아직 미완료. 어느 계산도 이번 턴에서 중단/재실행/수정하지 않음.
- FIRST READ: 학교 서버 `GaN_PiN_Diode_FAST_C1/n6_des.log` tail + err/sta, `CMP_BASELINE_1.2.0_CAL/n2_des.log` tail; 작업자가 출력 보내면 정확한 오류원인 판정. Common baseline / CAL / 완료된 5V_TEST 보호.

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

## 2026-10-10 — Shared mandatory naming rule reiterated for 주수빈 as well as 이택규 (DECISION)

Worker 이택규 explicitly requests that **주수빈's future CMP-created project names/files** follow the same confirmed format `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>`. This applies across separate chats and Claude whenever the agent reads CMP common instructions. Canonical updated `CMP/PROJECT_NAMING_CONVENTION.md` and entry-point `CMP/AGENTS.md`. Version the project and released bundles, but **do not rename SWB-consumed native files** such as sde_dvs.cmd, sdevice_des.cmd, sdevice.par and pp/n outputs. Preserve old projects and record provenance, parent and changes. Future new projects should be easy for professor to reproduce via SWB GUI parameter editors where feasible; do not alter current running CAL code. This is a shared policy, NOT a change actually made in 주수빈's separate private SWB directory.

---

## 2026-10-10 — CAL 5V Run pressed by 이택규 (USER REPORTED)

- Worker reports starting CMP_BASELINE_1.2.0_CAL NtSide0 5V SDevice in SWB. No new solver log or completion checked yet.
- Relative to prior finished NtSide0 Half+Coarse 4-QW trial, new InGaN Scharfetter tau_max=100ns replaces 1ns. Same geometry/doping/Transient BE intended. Old SDevice 5V walltime ~2h56m, new duration uncertain; a 3-6h figure is a non-validated planning estimate only.
- Next: read cloned n2_des.log progress/effective model and check SWB node status. Preserve prior results.

## 2026-10-10 — 이택규 decides current CAL run before SWB-native parameter migration

- User instruction: first run the present separate `CMP_BASELINE_1.2.0_CAL` as configured: cloned SDE and SDevice; `sdevice_des.cmd:22 Parameters="FASTC1_pp6_des.par"` and the saved cloned custom .par already has `Material="InGaN" Scharfetter taumax=1e-7,1e-7`. Do not change to standard `sdevice.par/@parameter@` for this device; adopt professor-facing copy/paste layout for **subsequent** newly created devices. The immediate priority is testing present candidate.
- No CAL SDE/SDEVICE job or preprocess completed on record. Next: run SDE mesh, verify its success, preprocess SDevice and prove actual material parameter input and solver recognition, then user can launch current 5V NtSide0 Transient-BE and provide log/results. Preserve original completed 5V_TEST and Full reference. CAL 100ns is a sensitivity run, not experimental fit.

---

## 2026-10-10 — User requires professor reproducibility through SWB-native code+parameter editors

이택규 live `grep` on cloned CAL SDEVICE: line22 `Parameters = "FASTC1_pp6_des.par"`, line68 `DefaultParametersFromFile`. This nonstandard direct filename means professors copying only SWB SDE/SDevice code would not necessarily have required GaN Mg and InGaN SRH overrides. Official Sentaurus SWB docs endorse common `sdevice.par` / `@parameter@` expansion with preprocessing. Plan **not yet executed**: first inspect any existing cloned `sdevice.par` (possibly default Silicon), then move actual custom blocks into it preserving originals and alter cloned SDevice File line to `Parameters="@parameter@"`; preprocess and verify `ppN_des.par` and effective log before any solver run. Presentation handoff requires three text inputs + NtSide and validation, not two files. Preserve finished reference, custom .par backup and parent result.

---

## 2026-10-10 — Separate CAL project cloned in SWB (OBSERVED / NOT RUN)

Worker 이택규 provided screenshot showing `CMP_BASELINE_1.2.0_CAL` in SWB, SDE→SDEVICE and NtSide=0, with `--` tool results; parent project still listed separately. Actual new source and parameter contents remain unchecked. Next verify new project file inventory, then install private candidate .par only in new clone and preprocess/short smoke. Do not claim CAL simulation has run or lifetime override is active.

---

## 2026-10-10 — CAL SRH-only private input candidate ready (PROPOSED / NOT SENTARUS TESTED)

Worker 이택규 supplied current server default InGaN Scharfetter/Radiative/Auger section. ChatGPT used confidential 9-file completed parent archive to build `CMP_BASELINE_1.2.0_CAL_INPUT_CANDIDATE.zip` privately; this is a ZIP of three source inputs and README, **not** a full SWB project. It preserves original SDE byte for byte; executable SDevice lines identical (only header/comments corrected); original custom LatticeParameters, Thermionic, GaN Mg block remain. Added InGaN-specific Scharfetter tau_max=1e-7 s for n/p, other default Scharfetter terms unchanged; GaN and AlGaN not changed. Private candidate par SHA256 adfe81ab03b8f0ca84b09b9a4373fdc8e71f7a5faa00ce01a7c0b82b7fb2f1ad. Zip static checks pass; **local T-2022.03 preprocess not performed**. Vendor central MaterialDB not edited.

New branch to be created in SWB using `Project > Save As > Clean Project` from parent to `CMP_BASELINE_1.2.0_CAL`, then install candidate files only in clone. Source still does one full 0-to-5V Transient Increment=1.2 and Save at 5V, so make separate short 0-0.3V smoke before using source for long solve. Do not confuse 100ns literature sensitivity with experimental lifetime calibration or solved/correct IQE. Follow `CMP/reviews/BASELINE_1_2_0_CAL_AUDIT_20261010.md` and `CMP/PROJECT_NAMING_CONVENTION.md`. No code added to public GitHub, no new project/run yet.

---

## 2026-10-10 — Crucial CAL audit evidence and recommended experiment for Claude/next AI

Actual privately uploaded successful JUSUBIN_FAST_HALF_5V_TEST 5V archive has been inspected. See public-safe `CMP/reviews/BASELINE_1_2_0_CAL_AUDIT_20261010.md` before suggesting any new code. Key computational evidence: eight 5V InGaN QW Clean/Dmg regions show exactly Rrad=Bnp with B=2e-10, Auger=A np(n+p) with A=1e-30, and SRH=np/[tau(n+p)] with tau=1ns, computed from HDF5 fields. The 0.10947% four-well model radiative share is not calibrated LED IQE. pGaN occupation*MgActive equals ionized -DopingConcentration (effective ~3e17 at some locations), so previous MgMinus raw field did NOT prove incomplete ionization inactive. Last 5V raw current 1.448e-11 with provisional J much lower than 0.1A/cm2; scaling unverified.

Actual SDevice code has SINGLE 0–5V Transient Increment=1.2 and single 5V Save; header claims 4,4.5,4.8 saves and highbias Increment1.05 but source does not implement them. 5V save was written on server but omitted from private upload. Need fix code/header consistency and verify same-current spatial snapshot availability before long reruns.

Proposed SRH material sensitivity is **NOT** a physically fitted baseline. Literature Baek et al Nat Comm 2023 DOI 10.1038/s41467-023-36773-w chose 100ns, B=1e-10, Auger=1e-31 in a DIFFERENT Silvaco six-well epitaxy. First read actual installed T-2022.03 InGaN.par Scharfetter section and official material override syntax, preserve GaN Mg/LatticeParameters/Thermionic. Then isolated copy `CMP_BASELINE_1.2.0_CAL` with SRH-only sensitivity, short Transient smoke -> 5V NtSide0 -> NtSide1e18 with same physics and current comparison. Full-vs-Half numerical equivalence + J normalization remain final gates. Do not claim Claude was contacted directly; use this handoff for any later AI. No new TCAD solver run or code modifications.

---

## 2026-10-09 — Canonical naming adopted and 5V_TEST file inventory verified (DECISION/OBSERVED)

- Worker 이택규: new future Baseline candidate is **`CMP_BASELINE_1.2.0_CAL`**, not `CMP_BASELINE_CAL_V1`. Official policy `CMP/PROJECT_NAMING_CONVENTION.md`: `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>`, independent A/B lineages, NtSide is a run variable.
- User server listing confirms 9 source/preprocessed/mesh/log/results file paths exist in `JUSUBIN_FAST_HALF_5V_TEST`, but the private bytes have not yet been provided for review. Next AI/Claude: review exact sources and effective material/current models before proposing edits. Preserve finished 5V_TEST, pre5V tar.gz and Full/Fine FAST_C1. No new solver work performed.

---

## 2026-10-09 — Claude / next AI review request: CMP_BASELINE_CAL_V1 proposal (PROPOSED, NOT SENT DIRECTLY)

Worker 이택규 chose to keep `JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz` in place and prepare a separate near-final candidate `CMP_BASELINE_CAL_V1`. Existing 5V NtSide0 Half+Coarse transient result (138194 elements; modeled 4QW radiative fraction ~0.10947%; low provisional J) must be preserved and not treated as a calibrated IQE. Region-specific Mg IncompleteIonization runs with E0=0.2eV/g=4; local hDensity matched historical target, yet MgMinus interpretation unresolved. The installed MaterialDB InGaN recombination defaults are annotated GaAs-derived and require validation of effective alloy mixing/overrides. QS branch previously failed near 0.0193V; use proven Transient-BE for first candidate.

For Claude or another AI reading this *later*: independently review actual private 5V_TEST input and log when made available, check applied InGaN SRH/Radiative/Auger, current units and injection, and recommend minimal literature-supported parameter-sensitivity tests with exact model precedence and reproducible comparisons. Do NOT claim direct Claude consultation, edit protected full baseline, change arbitrary values for a target efficiency, or run 5V production before private source review and short smoke. Full/Half+Coarse and same-current NtSide0/1e18 remain gates before final freeze.

---

## 2026-10-09 — Mg calibration source comment

이택규 observed in actual 5V_TEST pp1_dvs.cmd: comment says N_Mg_p=9.59e18 was previously tuned for 300 K p-GaN hDensity near 3e17 with incomplete ionization. This is a historical comment, NOT present measured hole density. Next probe existing n2_des.tdr hDensity in Clean_pGaN using SVisual; do not change Mg input or rerun.

---

## 2026-10-09 — Active SDE 5V_TEST dopant numeric values; Mg concentration vs effective ionization (이택규)

- OBSERVED `pp1_dvs.cmd` constants: `N_Mg_p=9.59e18`, `N_A_EBL=3e17`, `N_D_n=5e18`, `N_D_bar=1e15` [cm^-3]; `x_In=x_Al_EBL=0.15`. Actual species placements from prior 501–615 inspection pMg in Clean/DmgL pGaN, effective p EBL, n donor Clean/DmgL/base. All 12 NtSide0 trap Conc=0.
- `CMP/COMMON_BASELINE.md` calls p-GaN **effective active acceptor≈3e17 cm^-3**, not explicitly a raw input Mg atom density. Don't incorrectly substitute 3e17 for current `N_Mg_p=9.59e18` which is fed into incomplete-ionization model. Whether ionized Mg density/mobile holes meet 3e17 benchmark remains UNRESOLVED (must inspect 5V `n2_des.tdr` `pMagnesiumMinusConcentration` and `hDensity` in Clean_pGaN). No proof physical Mg model calibrated or invalid based solely on input.
- Prior JuSubin TIMELINE records Half+Coarse signed `DopingConcentration` color scale near -9.59e18 to +5e18 in mesh; supports gross sign/magnitude but NOT actual ionized/carrier concentrations, nor doping transition validation.
- NEXT read-only `sed -n '105,128p' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp1_dvs.cmd` for inline rationale (then verify actual TDR carrier/ionized Mg data and spatial cutline). Baseline untouched.

---

## 2026-10-09 — Handoff: SWB missing sdevice.par dialog, safe GaN MaterialDB strategy, Subin validation gates (이택규 / ChatGPT)

- OBSERVED screenshot original **JUSUBIN_FAST_HALF_SWB**, separate from successfully completed **JUSUBIN_FAST_HALF_5V_TEST**. In SWB SDevice `Tool > Edit Input > Parameter` prompts `Create Parameter File: sdevice.par does not exist` with `Silicon` default, `Choose Materials`, `Create Empty File`. This is an authoring step, NOT a solver result or evidence of a silicon LED simulation. User requested plan to build a physically credible GaN baseline and summarize JuSubin's October 8 handoff.
- Confirmed from N-2017.09 Sentaurus Workbench UG pp65–68: `Choose Materials` copies material parameter files and includes them in new `sdevice.par`; common sdevice.par may differ from per-instance .par. GaN/InGaN/AlGaN/Nitride material names must be derived from SDE mesh; don't select only GaN; InN is alloy constituent for mixing but may not be a mesh material. Actual finished 5V_TEST had `ModelParameters=FASTC1_pp6_des.par` in n2_des.log and parsed InGaN.par/GaN.par DB through `DefaultParametersFromFile` (not necessarily SWB-generated sdevice.par). **First check active original `File { Parameters=... }` to determine whether generated sdevice.par would even be used.** Do not lose FASTC1 custom lattice/Thermionic/Mg definitions.
- User screenshot original project current safest action: **Cancel**; work on an independent copied project based on finished 5V_TEST after backup, not original user project, and avoid blind selecting Silicon or writing parameter files in the live original.
- From JuSubin TIMELINE 2026-10-08: Half+Coarse mesh built 138,194 elements, 65,513 points; Mg/n-GaN doping and Full/Half equivalence not verified; QS 0–0.3V probe proposal. On 2026-10-09 TaekGyu verified QS Copy fails at 0.019304636V (Newton 15 iterations then below MinStep). Finished off-trap NtSide0 Half 5V_TEST (5V SDevice 2h56m); *all 12* preprocessed Dmg Conc values in that result were previously observed zero; SVisual 4-QW recombination ratio 0.1094747566%, not physical final IQE; NtSide1e18 ON not yet run on this accelerated branch.
- SCIENTIFIC BLOCKERS: InGaN.par GaAs-origin recombination values explicitly need calibration; effective material mixing and custom overrides unresolved, 2D current/J and hole/Mg/polarization injection unresolved; Transient 5V endpoint not independently steady-state-verified; Half+Coarse vs Full and same-current Nt0/Nt1e18 sidewall comparison pending. No basis to condemn Kou-based geometry or switch all physical models to GaN manually. P1 read-only source physics + material/parameters precedence + current/doping; P2 separate literature calibration parameters and short pilot; P3 matched-current off/on and full/half mesh; P4 freeze baseline only after gates; no broad A/B yet.
- Do NOT edit TCAD files, create GUI par, or start jobs without user explicit action. No provenance of other JuSubin live work beyond GitHub and supplied conversations. Relevant files documented in CURRENT_STATUS/NEXT_ACTIONS/LIVE_STATE and Issue #7.

---

## 2026-10-09 — Baseline physics plausibility + literature rerun plan (이택규 / ChatGPT)

- Latest log proves `DefaultParametersFromFile` loads InGaN.par/InN.par and active custom FASTC1_pp6_des.par; no standalone Lifetime file is normal, not proof of no SRH lifetime. Vendor InGaN.par GaAs-derived recombination warning: taumax 1ns, Radiative C 2e-10 cm3/s, Auger 1e-30 cm6/s. Numeric effective QW parameters/mixing unresolved. `Use Si parameters`, `Without incomplete ionization` in default-device block need scoped verification.
- Peer papers: Kou 2019 DOI 10.1364/OE.27.00A643 numerical SRH lifetime 1e-7 (unit printed s^-1, inconsistent with lifetime) and Auger 1e-30; Baek Nature Communications 2023 DOI 10.1038/s41467-023-36773-w simulator SRH=100ns, Radiative=1e-10, Auger=1e-31, but 6-QW/different epitaxy. Neither is a unique fit to current 4-QW device.
- 5V_TEST final 4-QW 2D IQE_rec ratio=0.1094747566% is a *modeled* recombination share only. 2D terminal current 1.448e-11 unverified units, 2um Half width inferred from 3nm QW ×0.006um²; conditional J≈7.24e-4 A/cm2 if A/um and no scale. Injection/polarization, material calibration, steady vs transient, and full/half equivalence unresolved.
- DECISION: keep current sources/results intact; **no blind rerun** or geometry remake. Audit live pp2/global region physics, actual effective material and current normalization. Then, with team approval, separate literature-calibrated parameter sensitivity branch and short NtSide0 pilot, followed by matched-current NtSide1e18, full/fine & mesh convergence. Project A/B not approved until physically credible baseline.

---

## 2026-10-09 — InGaN.par actually uses GaAs-derived uncalibrated recombination model parameters (이택규)

- **OBSERVED** live file line ~868 warning `Parameters for the recombination models below were taken from GaAs and require calibration for accurate simulations`. Scharfetter taumin=0, taumax=1e-9 s, Nref=1e16 cm^-3, gamma=1; Auger A=1e-30 cm6/s; Radiative C=2e-10 cm3/s. MaterialDB InGaN.par has been parsed according to earlier `n2_des.log`, but effective alloy parameters and overrides remain unverified.
- 5V_TEST Half+Coarse NtSide0 four-QW `IQE_rec=0.1094747566%` from 2D integrals is not a validated InGaN LED physical IQE, and GaAs-borrowed coefficients are an explicit **physical calibration blocker**, not the established only root cause. SRH remains on, 2D current injection very low/unverified.
- NEXT read-only `sed -n '945,970p' n2_des.log`, `sed -n '270,310p' n2_des.log`, audit alloy/material mixing/effective coefficients, J normalization, then literature calibration BEFORE any new physics branch. Protect baseline and outputs.

---

## 2026-10-09 — All four InGaN QW integrated Rrad/SRH/Auger complete (이택규)

- Latest user SVisual Clean_QW1 (Rrad=857.9041, SRH=77658.39, Auger=252.5448) and DmgL_QW1 (Rrad=19.46374, SRH=496.6036, Auger=2.309115) [s^-1 um^-1] confirm last missing well. Derived QW1 total Rrad=877.36784, SRH=78154.9936, Auger=254.853915, well ratio=1.1065691%.
- Sum all four wells Clean+DmgL at 5V NtSide0: Radiative=40072.8158452, SRH=36562944.9075, Auger=1599.706168587, total=36604617.4295138 [s^-1 um^-1], **MQW recombination radiative fraction=0.1094747566%**. QW4 provides ~96.94% of MQW integrated radiative. This is NOT experimentally validated LED IQE/EQE or final reference.
- NEXT: inspect active effective SRH lifetimes and Radiative coefficients/material DB, 2D J-V normalization, carrier distribution/polarization, then full/fine and NtSide1e18 comparisons. Preserve files, no solver change.

---

## 2026-10-09 — QW2 recombination integrals complete / default-parameters audit ongoing (LeeTaekGyu)

- 5V_TEST NtSide=0 Half, SVisual Clean_QW2 Rad=83.3149, SRH=54645.76, Auger=1.736316 [s^-1 um^-1]; DmgL_QW2 Rad=0.1672872, SRH=141.6049, Auger=0.003800247. Sum QW2 Rrad=83.4821872, SRH=54787.3649, Auger=1.740116247, QW-only recombination radiative fraction 0.1521382378%. QW1 still missing; QW3 0.0454256871% and QW4 0.1082525242% known.
- Read-only grep live pp2_des.cmd and FASTC1_pp6_des.par finds DefaultParametersFromFile and SRH/Auger/Radiative model declarations, but no explicit lifetime/radiative material coefficients or AreaFactor in these two files; verify effective material database and current units, no cause assigned.
- NEXT: QW1 6 independent Clean/DmgL 2D integrations, full 4-QW summation; inspect physical effective parameters. Do not edit/rerun TCAD or call QW-only numbers device IQE.

---

## 2026-10-09 — QW4 2D radiative/SRH/Auger integrals complete (이택규)

- QW4 final 5V_TEST NtSide0 Half: independently integrated Clean (Rrad=38746.96, SRH=35617690, Auger=1327.983; area=0.005985012 um²) and DmgL (Rrad=98.768, SRH=226496.2, Auger=2.414354; area=0.00001500002 um²). SVisual integral units s^-1 um^-1.
- Summed QW4 Rrad=38845.728, SRH=35844186.2, Auger=1330.397354, total 35884362.325354. Derived QW4-only recombination radiative fraction 0.1082525242%; QW3-only earlier 0.0454256871%. Device-wide IQE pending QW1/2, along with physics plausibility audit. No code changes.
- NEXT: six standalone 2D region integrals each QW1 and QW2, then 4-QW IQE_rec from integrals, effective SRH/material/injection audit before baseline acceptance.

---

## 2026-10-09 — Full QW3 2D recombination integral completed; very low recombination share (이택규)

- OBSERVED SVisual Clean_QW3 2D: SRH=5.841611e5, Auger=12.65704, earlier Radiative=265.711; DmgL_QW3 2D SRH=1655.249, Auger=0.05774334, Rad=0.526818; all s^-1 um^-1. Sum QW3 half-domain Rrad=266.237818; SRH=585816.349; Auger=12.71478334. Derived local-to-QW spatial-integrated recombination ratio Rrad/all = 0.0454256871% at 5V, NtSide=0. This is **QW3 only; device IQE unverified**.
- Clean holds 99.717% of QW3 integrated SRH, so don't claim sidewall-specific trap caused low fraction; ordinary SRH physics is active and material parameter/current injection audit is pending.
- NEXT: same verified 2D separate-region integrations for Clean/DmgL_QW1,2,4; verify materials radiative, SRH lifetimes and current unit. Keep baseline/code/results unchanged.

---

## 2026-10-09 — QW3 full radiative 2D integration gate passed

- 이택규 5V_TEST SVisual: Clean_QW3 integral 265.711, DmgL_QW3 integral 0.526818, sum 266.237818 [s^-1 um^-1]; respective domains 0.005985012 and 0.00001500002 um², summed 0.00600001202 um². Both verified as separate dimension-2 regions.
- This is not device IQE. Next integrate SRH and Auger over the same standalone regions, then all four QWs. Do not choose plus-named interface as union, modify code, or rerun.

---

## 2026-10-09 — Correction: '+' region labels in SVisual integration (이택규)

- Observed screenshot output clean QW3-only radiative 2D integral 2.657110e+02 [s^-1 um^-1] and domain 5.985012e-03 um². Left `Clean_QW3+DmgL_QW3` selection did not show as separate 2D integrated region.
- Prior GPT incorrectly claimed '+' is combined area: retract that assumption. Likely interface/boundary (not confirmed metadata). Safest exact follow-up: select standalone `DmgL_QW3` region only, Start Integration, verify Regions of Dimension 2, then add nonoverlapping Clean_QW3 + DmgL_QW3; do NOT infer full-well value from '+' selected row.
- No remote source change or rerun; preserve data. Continue other QWs, SRH/Auger and IQE after region verification.

---
## 2026-10-09 이택규 handoff: 5V_TEST at Clean_QW4 same (x,y)=(0.244864017914,0.651958341615): Rrad=7.103015017104e18, SRH=1.681575471039e22, Auger=1.238545872618e15 cm^-3 s^-1. Pointwise radiative share ~0.0422%, not device IQE. Check spatial integrated MQW rates and effective SRH/material parameters next. NtSide=0 does not disable all SRH. Preserve outputs; no solver edits.

## 2026-10-09 — 5V copied Half+Coarse SDevice finished; postprocessing/validation now first (이택규 / ChatGPT)

- OBSERVED: user terminal `JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` shows final anode 5.000 V, total current 1.448E-11 in output units, `Curve trace finished`, `Sentaurus Device simulation finished`, `Good Bye !` 2026-10-09 14:29:52 KST. Wallclock 10596.76 s, peak memory 2.97 GB. `n2_5V_ckpt_des.sav`, circuit checkpoint, `n2_des.tdr` written. No active pp2 in `ps`; pp6/pp12 references still observed.
- This resolves the uncertainty about whether copied NtSide=0 Half/Coarse Node2 reached 5V. It does not validate emission/IQE, current normalization, NtSide=1e18 damaged baseline or full/fine equivalence; treat 5V test only as solver endpoint success.
- NEXT FIRST: preserve Node2 outputs/checkpoints; review full `n2_des.plt` 0–5V trajectory and units, physical current/recombination; compare Full vs Half at equivalent bias and same current. Evaluate baseline gates before launching NtSide=1e18; A/B production NO-GO.
- Do not: cleanup/rerun successful Node2, interrupt pp6/pp12, conclude physical speedup from old estimated ETA (measured runtime supersedes it), modify baseline geometry/trap/physics without review.

---
## 2026-10-09 — User temporarily shifts from TCAD operations to conceptual Project A study (이택규)
- User says interactive TCAD unavailable; asks if 5V Half/Coarse Test is Baseline and whether Project A Carbon is implanted. **Do not assume existing SWB Node2 5V process stopped**; no fresh log.
- Answer: 5V completion necessary but not sufficient. NtSide=0 is pristine/trap-off control; nominal damaged baseline NtSide=1e18 required, plus full-vs-half/coarse equivalence, matched-current I-V/SRH/Rrad/RAuger/IQE/current-crowding, current normalization.
- Verified protocol: CMP/PROJECT_AB_PRE_RUN_AUDIT.md section 4 defines `Cedge_L/R` GaN immediately inside 5nm damage, first location upper nGaN beneath MQW, with carbon deep acceptor/compensation and carbon-off null control. Stage1 is **device-level carbon mechanism screen**, not SProcess implantation. Physical C implantation is only potential later process path; may add damage and activation issues, not yet chosen. Hypothesized reduced sidewall recombination/IQE benefit remains unproven.
- Next: explain mechanism and implantation/profile distinctions; when TCAD accessible, inspect live 5V Node2 log and preserve the running project.

---

## 2026-10-09 11:33 KST — Copied Half 5V Node2 submitted/running in SWB
- OBSERVED SWB Project Log screenshot for `JUSUBIN_FAST_HALF_5V_TEST`: preprocess initialized; Node2 submitted for local execution; ready -> pending -> running; SDevice job 2 started 11:33:14 Oct9 2026. This confirms startup only, not solver convergence, ongoing process, or 5V reached.
- Preflight copy+readable archive, pp2 Goal5.0V/FinalTime1.0 and Grid/NtSide=0 previously passed. Other pp6 and pp12 running concurrently on same account.
- NEXT: in copied folder check `ps -fu semi437 | grep '[s]device'`, `ls -lh --full-time n2_des.log`, `tail -n 20 n2_des.log`; do NOT Clean Up Node, rerun F7, or disturb original/other jobs.

---

## 2026-10-09 — pp2 5V not running; other jobs active (이택규)
- OBSERVED `ps` on semi437: PID 69457 pp6_des.cmd since Oct04, PID 93915 pp12_des.cmd since Oct06; no pp2_des.cmd. Copied 5V_TEST `n2_des.log` is original completed 0.3V smoke (mtime Oct9 01:39:13, wallclock 25019.43s, peak 2.61GB, Good Bye); **NOT** a 5V result.
- SWB screenshot showed 5V_TEST open with SDE→SDEVICE, NtSide=0; no active node2 run in process evidence. Clean Up Node not needed, risks clearing inherited results. Tested pre5V tar archive readable and pp2 preprocessed FinalTime1.0 Goal5V Grid n1_msh NtSide0 verified.
- NEXT: user may select copied project's SDevice Node2 only and F7 (if resource pressure from pp6/pp12 acceptable); inspect fresh `n2_des.log`, SWB View Output and convergence. No 5V launch confirmed as of last user terminal. Do not touch original SDE/other running jobs.

---

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
