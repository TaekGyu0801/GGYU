## 2026-10-13 — 3주차 PPT 10번 슬라이드 가독성 개정 (PRESENTATION / OBSERVED)
- 사용자 요청에 따라 10번 슬라이드 “문제 해결 시도”를 기존 5행 검사표에서 교수님이 이해하기 쉬운 **세 질문 → 확인된 근거 → 아직 남은 검증** 구조로 재설계. 산출물: `CMP_Week3_JuSubin_Slide10_Clear.pptx` (13장 전체, 기존 9번 슬라이드 개선 상태 유지, 10번만 변경).
- ① 전극/대칭 구조 확인: Half 상부 접촉 2.0 um 및 중앙 대칭면 확인. ② p-GaN Mg 9.59e18 / hole density 약 3e17 cm^-3 관측, 이온화 해석은 미해결. ③ Thermionic 모델 ON 로그 확인, 실제 2D 전류 면적 보정 및 저전류 원인은 미해결.
- 오른쪽 SVisual p-GaN Probe 또는 SDE Contact 실제 캡처를 넣을 플레이스홀더를 유지했으며, 가짜 실험 이미지는 생성하지 않음. 결론은 “구조/Thermionic 일부 설정 확인, 저전류 원인과 전류 정규화는 여전히 검증 중”으로 명시.
- 출력 PPTX는 python-pptx 열기, 13장 검증, LibreOffice 렌더 및 슬라이드 오버플로 테스트를 통과함. 학교 서버 실행, TCAD 코드·물성·시뮬레이션 결과 변경 없음.

## 2026-10-13 — 3주차 PPT 9번 슬라이드 가독성 개정 (PRESENTATION / OBSERVED)
- 사용자 요청에 따라 9번 슬라이드의 장황한 본문을 제거하고, 좌측 5V raw TotalCurrent 2조건 수평 막대와 우측 QW SRH/방사 재결합 핵심 수치로 재설계함. 산출물: `CMP_Week3_JuSubin_Slide09_Clean.pptx` (13장 전체 덱, 9번만 변경).
- 5V raw terminal current: NtSide=0 1.448e-11 vs NtSide=1e18 7.050e-12 (약 51.3% 차이). QW 모델 내부 SRH 비율 약 99.9%; 방사 비율 0.1095% vs 0.0489%를 표시함.
- 저전류와 SRH 우세의 원인은 미확정. 동일 전압에서 서로 다른 전류로 비교한 결과이며, 동일 전류의 순수 Trap 영향으로 확정하지 않음. 2D 전류 정규화 및 IQE calibration 미완료 주의 문구 유지.
- PPTX 13장 파싱·ZIP 무결성·9번 페이지 렌더링 확인 완료. TCAD 코드/시뮬레이션/물리 설정 변경 없음. 사용자 실제 PowerPoint 열림은 확인 전.

## 2026-10-13 — 3주차 PPTX 열기 문제 대응 (DELIVERABLE FIX / USER VERIFICATION PENDING)
- 사용자 보고: 기존 3주차 PPTX가 열리지 않음. 기존 PPTX는 ZIP 무결성, XML 파싱, python-pptx(13장), LibreOffice 파일 열기/렌더링 검사에서 오류 재현되지 않음. 사용자 앱/다운로드 환경 원인은 확인하지 못함.
- LibreOffice Impress Office Open XML 형식으로 다시 저장한 호환성 수정본 `CMP_Week3_JuSubin_Compatible.pptx` 작성. ZIP 압축 배포본과 13장 PDF 미리보기도 채팅에 제공. 수정본 ZIP/슬라이드 파싱/13장 PDF 생성 검사를 통과했으나 실제 사용자 PowerPoint에서 열리는지는 확인 전.
- TCAD 코드/계산/물리 해석/결과 변경 없음. 기존 발표 구조와 7개 목차 유지. 다음: 사용자가 수정본을 실제 PowerPoint에서 열 수 있는지 확인.

## 2026-10-13 — 주수빈 3주차 발표 PPT 초안 제작 (PRESENTATION / OBSERVED)
- 2주차 발표 PDF와 CMP의 2026-10-12 실제 기록을 바탕으로 7개 한국어 목차를 유지한 13장 편집 가능한 발표 PPT 초안을 제작함. 산출물 로컬 파일명: `CMP_PRESENTATION_1.0.0_WEEK3_JUSUBIN.pptx`. GitHub에는 PPT 바이너리를 업로드하지 않았으며, 사용자의 채팅에서 파일로 제공함.
- 구성: 이전 연구 및 현황 → Baseline 계산 문제 → Half-Mesa 물리 타당성/검증 조건 → Baseline 최적화 및 5V 결과 → 예상 외 저전류/SRH 지배 → 도핑·Contact·CAL 모델 진단 → 다음 계획. 기존 2주차 원문보다 기대/문제/대응/검증 수준에 집중하도록 편집.
- 계산 근거로는 JuSubin 5V_TEST NtSide 0/1e18 두 조건 종료, raw current 1.44801646e-11 / 7.05011114e-12, QW 3-channel radiative fraction 0.10947478% / 0.04893717%를 사용함. 두 조건은 5V 고정 전압에서 서로 다른 전류이므로 matched-current IQE 또는 Trap 순수 효과로 결론내리지 않음.
- Full/Half, Mesh, p-GaN SVisual, EBL/MQW cutline은 실제 스크린샷 삽입 위치를 명시한 PLACEHOLDER로 처리했으며 결과 이미지를 생성하거나 꾸며내지 않음. Half의 대칭성 논리는 이론적 전제, Full/Half 수치 동등성은 아직 미검증으로 표시. 이택규 별도 CAL4V 진단과 주수빈 5V_TEST를 구분함.
- **중요:** 본 작업은 발표 자료 작성으로, 소자 코드/학교 서버 시뮬레이션/검증 상태는 변경되지 않았음. 다음 PPT 작업은 실제 SDE/SVisual 원본 캡처 삽입 및 발표 문구 검토.

## 2026-10-12 — JuSubin 5V_TEST numeric SDE y coordinates and half-contact lengths verified (OBSERVED / CONDITIONAL J)
- Worker 주수빈. Actual terminal `sed -n '65,160p' pp1_dvs.cmd` plus prior `sed -n '415,495p' pp1_dvs.cmd`. SDE defines W_mesa=4.000 um, W_domain=5.000 um, W_damage=0.005 um. Therefore yL=(5-4)/2=0.500 um, yDL=yL+W_damage=0.505 um, yC=W_domain/2=2.500 um; x0=0.
- Anode set-contact top two edges centered at y=(yL+yDL)/2 and (yDL+yC)/2: segment DmgL y=0.500..0.505 (0.005um), Clean y=0.505..2.500 (1.995um), half-mesa anode total=2.000um. Bottom cathode in numerical n-GaN base y=0..2.500 total=2.500um. y=yC is an artificial symmetry plane (not an etched wall). Cathode numerical extent is NOT equal to emissive mesa width. Device described as LEFT HALF of full 4um mesa in 2D Cartesian.
- Earlier actual no-match grep for literal `AreaFactor` in pp2_des.cmd, pp4_des.cmd, FASTC1_pp6_des.par, n2/n4 logs. Older Sentaurus UG material indicates default 2D out-of-plane thickness=1um, `AreaFactor` multiplies electrode current; this should be verified against licensed T-2022.03 installation/effective options before publication-grade claims.
- IF default thickness 1um, raw PLT currents representing that 1um extrusion and physical planar mesa width 2um (half): equivalent half-strip area=2um². CONDITIONAL J_n2=1.44801646079583e-11/(2e-8)=7.24008230397915e-4 A/cm², J_n4=7.05011114486348e-12/(2e-8)=3.52505557243174e-4 A/cm² at 5V. Symmetry reconstruction doubles both current and mesa area and cancels for J. Low current density remains a physical-calibration blocker independent of successful solver completion. J is not verified until effective units/normalization and contact physical relevance confirmed.
- No server TCAD source, model, mesh, or output modified. Next verify T-2022.03 default units/AreaFactor applicability, then inspect injection and SRH physics; preserve already completed 5V datasets.

## 2026-10-12 — JuSubin 5V_TEST SDE top/bottom electrode selection read-only (OBSERVED)
- Worker 주수빈, AI ChatGPT. Real server stdout `sed -n '415,495p' pp1_dvs.cmd`, unchanged source.
- SDE `sdegeo:define-contact-set` names "anode"/"cathode". Top p-contact `sdegeo:set-contact` assigns TWO distinct edges by `find-edge-id(position x0 ((yL+yDL)/2) 0)` and `find-edge-id(position x0 ((yDL+yC)/2) 0)` to anode, covering DmgL and Clean pieces of top half-mesa edge (provided edge geometry actually spans respective y ranges).
- Bottom n-contact assigns ONE edge at `position xb (yC/2) 0` to cathode; source comment explicitly says half-domain numerical n-GaN base spans y=0...yC. `y=yC` is artificial mirror-symmetry boundary, NOT etched sidewall.
- From previous observed W_mesa=4.0um and W_domain=5.0um for left-half symmetric model, predicted upper physical mesa span 2.0um and numerical bottom base 2.5um IF variable definitions satisfy yL=0.5, yC=2.5um; numerical values of yL,yDL,yC,x0,xb and exact edge lengths still to be read directly. Do not use bottom numerical-contact width as LED emission area.
- Previous `AreaFactor` literal text check had no matches in pp2_des.cmd, pp4_des.cmd, FASTC1_pp6_des.par, n2/n4 logs; still NO independently established effective 2D raw-current unit/default or verified physical current density. Prior conditional J n2 ~7.24008e-4 A/cm2 and n4 ~3.52506e-4 at 5V require unit and width verification.
- NEXT READ ONLY inspect `pp1_dvs.cmd` numeric definitions `yL,yDL,yC,x0,xb,W_mesa,W_domain` with grep and ensure SDE actual edge spans; no TCAD code/run/result edits.

## 2026-10-12 — JuSubin 5V_TEST SDE Half-Mesa geometry read-only check (OBSERVED; J DERIVED CONDITIONALLY)
- Worker 주수빈. Screenshot of read-only `grep -niE 'mesa|half|domain|contact|electrode|cylindrical' pp1_dvs.cmd | head -n 80` in JUSUBIN_FAST_HALF_5V_TEST.
- SDE comments explicitly: simulate only LEFT HALF of mirror-symmetric full device; physical mesa width=4.0 um, simulated mesa width=2.0 um, 4um representative (not actual JBD mesa). Define W_mesa=4.000, W_domain=5.000; full left edge=(W_domain-W_mesa)/2, centerline=W_domain/2. No DmgR; half top contact DmgL+Clean. Numerical/contact extension domain is not automatically physical mesa width.
- Previously no textual `AreaFactor` found in pp2_des.cmd, pp4_des.cmd, FASTC1_pp6_des.par, n2_des.log, n4_des.log. IF raw 2D anode TotalCurrent is A per um depth with effective AreaFactor=1, and half-mesa lateral 2um width is appropriate, conditional J=I_2D/(2um)*1e8: n2 5V 7.24008230397915e-4 A/cm2, n4 5V 3.52505557243174e-4 A/cm2. These are CONDITIONAL derived values, not confirmed J; exact top-contact extent, actual effective 2D output convention, AreaFactor default, and transient steady-state must be checked before publication-grade current-density assertion.
- Next read-only `sed -n '65,85p;125,150p;410,455p;460,495p' pp1_dvs.cmd` for numeric y bounds and electrode geometry/contact spans (server actual file); no edits/reruns or modification to baseline.

## 2026-10-12 — JuSubin 5V_TEST AreaFactor text audit (OBSERVED)
- User provided actual terminal screenshot running `grep -ni 'AreaFactor' pp2_des.cmd pp4_des.cmd FASTC1_pp6_des.par n2_des.log n4_des.log | head -n 60` from JUSUBIN_FAST_HALF_5V_TEST. No matches printed, prompt returned. This confirms NO explicitly named `AreaFactor` text in these five files; it DOES NOT prove the effective 2D current unit, default scaling, or correct contact/device-area normalization. No error was reported.
- Prior n2 5V raw terminal TotalCurrent=1.44801646079583e-11, n4 5V=7.05011114486348e-12 (different injection). Physical J (A/cm²) remains UNRESOLVED pending mesh 2D planar geometry/active contact width, and Sentaurus T-2022.03 default 2D normalization verification. `COMMON_BASELINE.md` describes representative 4um mesa, 5um numerical domain, Cartesian 2D and no cylindrical symmetry; avoid equating pixel pitch, mesa area and model domain.
- Next read-only inspect n2 active SDevice File/Electrode/Math block and actual SDE dimensions/contact widths; do not assign an unverified current density. No TCAD source or simulation changed.

## 2026-10-12 — 주수빈 5V_TEST n2 matched-current-nearest PLT current decomposition (OBSERVED)
- Worker 주수빈. Terminal read-only parser output nearest recorded `n2_des.plt` point to n4 5V raw TotalCurrent target=7.05011114486348e-12: time=0.984673772998644s; anode OuterVoltage=4.92336886499322V; raw anode TotalCurrent=7.14463993632474e-12; DisplacementCurrent=3.0437121600456e-18; eCurrent=1.01944917915676e-13; hCurrent=7.0426919746969e-12.
- Target-current deviation of this DISCRETE point = +1.34081278% (n2 vs n4); not exactly matched. Displacement/Total at selected n2 bias = 0.0000426013%, confirming negligible final comparison-point capacitive component. n4 actual 5V final Displacement=3.38231191699972e-18, Total=7.05011114486348e-12, fraction=0.0000479753%.
- Previously two-point PLT interpolation gave n2 bias ~4.921801256V for exact n4 raw current and n4-minus-n2 +78.198744mV, but NO spatial TDR at that bias; 5V Radiative/SRH/Auger 4QW ratios cannot be interpreted as matched-current IQE. Neither negligible displacement nor electrode e/h fractions proves steady state or QW injection.
- NEXT: read-only audit effective AreaFactor/2D current normalization in n2/n4 preprocessed SDevice decks and output logs (e.g. grep AreaFactor), before physical current density comparison. No solver rerun, model, mesh or result edits.

## 2026-10-12 — 주수빈 5V_TEST n2/n4 equal-raw-terminal-current bias from n2 PLT (OBSERVED + LINEAR INTERPOLATION)
- Worker: 주수빈. Evidence: user terminal output of read-only 1023-point `n2_des.plt` scan against target `n4_des.plt` last 5V anode TotalCurrent=7.05011114486348e-12 (raw Sentaurus 2D values).
- n2 bracketing recorded points: (V=4.91836886499322, I=6.84313365428304e-12, t=0.983673772998644s) and (V=4.92336886499322, I=7.14463993632474e-12, t=0.984673772998644s). Nearest discrete n2 sample is V=4.92336886499322, I=7.14463993632474e-12 (absolute error=9.452879146125942e-14).
- Derived (LINEAR INTERPOLATION, NOT directly saved 2D result): n2 V at target raw I ≈ 4.921801256006416 V; n4 actual target voltage 5.0 V, so delta V=n4 minus n2≈+0.078198743993584 V = +78.20mV on 5 V/s transient sweep. Do not represent interpolation as an actually computed n2 spatial TDR or as validated steady-state series resistance.
- Only spatial TDR files in recursive project inventory are n2_des.tdr and n4_des.tdr at final nominal 5V. Thus the existing radiative/SRH/Auger eight-QW full-region 5V ratios 0.10947478% (n2) vs 0.04893717% (n4) CANNOT be compared as equal-current spatial recombination results. No intermediate-voltage TDR near ~4.9218V. Same raw electrode current doesn't yet mean calibrated physical current density (AreaFactor check pending) and n2 transient displacement at target bias is not yet checked.
- Next read-only n2 .plt nearest two points' DisplacementCurrent/eCurrent/hCurrent and current monotonicity; verify total-current definition / AreaFactor, decide what time and bias snapshots needed. Any new simulation/continuation requires explicit user decision; preserve completed files.

## 2026-10-12 — JuSubin 5V_TEST project-wide TDR/SAV inventory (OBSERVED)
- Worker 주수빈; actual terminal screenshot command `find . -type f \( -name '*.tdr' -o -name '*.sav' \) | sort | head -n 100` from JUSUBIN_FAST_HALF_5V_TEST; only 10 matching entries displayed.
- TDR: n1_bnd.tdr, n1_msh.tdr, n2_des.tdr, n4_des.tdr. No intermediate-bias spatial TDR in this project inventory. n2/n4 final datasets previously verified as 5V.
- SAV: n2_5V_ckpt_circuit_des.sav, n2_5V_ckpt_des.sav, n2_smoke_ckpt_0p3V_circuit_des.sav, n2_smoke_ckpt_0p3V_des.sav, n4_5V_ckpt_circuit_des.sav, n4_5V_ckpt_des.sav. Saved-state files are NOT automatically visualization-ready intermediate spatial snapshots. Do NOT assume '0p3V' filename proves an actual 0.3V solve: prior QS trace only accepted around 0.019304636V before failure; provenance of these specific SAV files should be separately audited.
- Result boundary: already established n2 and n4 5V 4QW 3-channel recombination fractions stay OBSERVED; true matched-terminal-current spatial 3-channel comparison cannot be produced immediately from existing 5V TDR alone.
- Next: read-only parse 1023-point n2/n4 PLT I-V traces to locate overlapping current bias targets and assess stationarity/displacement; separate any future need for saved spatial TDR from existing checkpoint and request approval before additional simulation. No source/model/result edits.

## 2026-10-12 — JuSubin checks root-level 5V_TEST TDR snapshots (OBSERVED)
- Worker: 주수빈; actual SSH screenshot of `find . -maxdepth 1 -type f -name '*.tdr' | sort` inside JUSUBIN_FAST_HALF_5V_TEST lists only `./n1_bnd.tdr`, `./n1_msh.tdr`, `./n2_des.tdr`, `./n4_des.tdr`.
- Only root-level files were checked; presence or absence of intermediate-voltage spatial TDR in subdirectories is NOT established. n2_des/n4_des are previously verified final 5V SDevice TDR outputs, not demonstrated matched-current spatial snapshots.
- NEXT read-only recursively list project TDR and SAV snapshot files before deciding whether identical injected-current 4QW spatial recombination comparison can be done without new runs; then extract matching-current voltage from n2/n4 PLT. Preserve device files and runs.

## 2026-10-12 — JuSubin 5V_TEST n4 final anode-current decomposition verified (OBSERVED)
- Worker 주수빈. User submitted terminal output from read-only Python parser of `JUSUBIN_FAST_HALF_5V_TEST/n4_des.plt`. Prior shell quoting produced a SyntaxError, but subsequent command succeeded: 1023 records, remainder 0; last time=1.0 s, anode OuterVoltage=5.0 V.
- n4 raw anode: TotalCurrent=7.05011114486348e-12; DisplacementCurrent=3.38231191699972e-18; eCurrent=7.53447212445082e-14; hCurrent=6.97476304130706e-12. Electron + hole + displacement reproduce TotalCurrent (display precision).
- Existing n2 same last-bias: TotalCurrent=1.44801646079583e-11, DisplacementCurrent=3.29132361382365e-18, eCurrent=2.78143237811134e-13, hCurrent=1.42020180788235e-11.
- n4 vs n2 (both 5V final transient points): TotalCurrent -51.31194%, eCurrent -72.91154%, hCurrent -50.88893%. Displacement / Total=0.0000479753% in n4 vs 0.0000227299% in n2; neither final-time total is displacement-dominated. n4 current composition: 1.0687% electron and 98.9312% hole; this is electrode composition, NOT QW injection or carrier balance.
- Prior 4QW eight-region modeled recombination share n2=0.10947478%, n4=0.04893717% (Radiative/(Radiative+SRH+Auger)). Those ratios at 5V are NOT matched-current effect, validated whole-device IQE, or EQE. Model AreaFactor/current units and real steady state remain unverified.
- NEXT read-only examine full n2/n4 I-V records to pick current in overlapping range, extract associated voltages and check pre-existing bias-resolved TDR snapshots. No source/mesh/solver/rerun changes.

## 2026-10-12 — JuSubin n2_des.plt 5V final anode current components extracted (OBSERVED)
- Worker: 주수빈; AI: ChatGPT. Evidence: user-provided MobaXterm screenshot, read-only Python parser on DF-ISE text `n2_des.plt` in JUSUBIN_FAST_HALF_5V_TEST after correcting current-directory FileNotFoundError. 1023 complete records, remainder 0.
- Last record: time=1.0 s, anode OuterVoltage=5.0 V, anode TotalCurrent=1.44801646079583e-11, anode DisplacementCurrent=3.29132361382365e-18, anode eCurrent=2.78143237811134e-13, anode hCurrent=1.42020180788235e-11 (raw PLT 2D units).
- At this final time, DisplacementCurrent/TotalCurrent ~2.273e-7 (0.00002273%). Thus final-time terminal-current magnitude is not dominated by the displacement component; this alone does NOT prove temporal steady state, correct J normalization or adequate MQW hole injection. e/h current values are electrode-current components, not directly quantum-well injection efficiencies.
- NEXT: repeat identical read-only parser for `n4_des.plt`; compare 5V anode current decomposition and check voltage/current traces for matched-current comparison. Keep SDevice model/files/results unchanged.

## 2026-10-12 — JuSubin confirms n2 PLT DF-ISE text Data structure (OBSERVED)
- User screenshot shows `sed -n '1,28p' n2_des.plt` in 5V_TEST: `DF-ISE text`, `Info { version=1.0, type=xyplot, datasets=[time, electrode voltages and eCurrent/hCurrent/DisplacementCurrent/TotalCurrent/charge], functions=[...] }`, followed by `Data {` numeric entries wrapped over multiple lines. This is format inspection, not yet physical current extraction.
- Next read-only parse the data numeric stream as dataset ordered records; validate count and last voltage/time, then compare both n2 and n4 anode current decomposition. Avoid misreading line-wrapped numeric values as independent records; no rerun/code edit.

## 2026-10-12 — JuSubin confirms n2/n4 PLT current field structure (OBSERVED)
- Read-only grep of datasets in 5V_TEST n2_des.plt and n4_des.plt confirms matching current field declarations: time; anode/cathode OuterVoltage, InnerVoltage, DisplacementCurrent, eCurrent, hCurrent, TotalCurrent (plus Charge/QuasiFermiPotential). Actual values and scaling still unverified.
- Next inspect initial .plt Data layout and numeric current decomposition of each node, then assess equal-current voltage and available TDR snapshots. No TCAD source or results modified.

## 2026-10-12 — JuSubin 5V_TEST n2/n4 eight-QW three-channel recombination comparison (OBSERVED)
- Worker 주수빈. Evidence: Sentaurus Visual Field Integration pasted outputs for RadiativeRecombination, srhRecombination, AugerRecombination on 8 distinct 2D regions Clean_QW1..4 + DmgL_QW1..4 (avoid '+' interface labels). Total Domain 0.02400002 um² for each node, units for all integrals s^-1 um^-1.
- n2 NtSide0: Radiative 40072.82; SRH 36562940; Auger 1599.707; 3-channel total 36604612.527; Radiative fraction 0.10947478264%; SRH share 99.88615498397%; Auger share 0.00437023339%.
- n4 NtSide1e18: Radiative 7056.261; SRH 14411700; Auger 265.2578; 3-channel total 14419021.5188; Radiative fraction 0.04893716949%; SRH share 99.94922319250%; Auger share 0.00183963801%. n4 Auger detailed Clean region sum (display rounded)=264.6098086; DmgL region sum=0.6480449636; rounded sum 265.25785356 (within display rounding of stated total).
- n4 relative to n2 at nominal 5V: Radiative -82.3914%; SRH -60.5839%; Auger -83.4184%; radiative fraction relative decrease 55.2982% (absolute -0.0605376 percentage points).
- Grouped 3-channel radiative shares from region-rounded sums: n2 Clean ~0.10984%, DmgL ~0.05195%; n4 Clean ~0.04909%, DmgL ~0.02484%. Regional fractions represent spatially integrated model channel ratios only.
- CRITICAL INTERPRETATION: these are 4QW modeled 3-channel recombination fractions, NOT measured EQE or independently validated whole-device IQE. n2 raw 5V current=1.4480164608e-11 vs n4=7.050e-12 (different injection), so fixed-voltage difference is not matched-current trap causal proof. TCAD 2D current AreaFactor, time-dependent/displacement contribution, QW hole injection and physical calibration still require validation. Node2 explicit 12 DmgL sidewall traps Conc=0 while global SRH is active. Dominant SRH is an observation, its microscopic cause is not established.
- NEXT: review n2/n4 electrode TotalCurrent vs DisplacementCurrent and normalized J from saved .plt; examine whether equal-current comparison is possible with existing saved intermediate 2D TDRs, else mark additional snapshot requirements before any new run. Do not modify baseline/code or rerun until plan approved.

## 2026-10-12 — 주수빈 n2_des Auger 적분 완료 (OBSERVED)
- SVisual 4QW 8개 2D 영역 AugerRecombination total 1599.707 s^-1 um^-1, domain 0.02400002 um^2. Clean total 1594.921156, DmgL total 4.785012587 (표시된 개별 값들의 합).
- 같은 영역 n2 Radiative 40072.82, SRH 36562940. 3-channel radiative fraction=0.10947478%, SRH=99.88615498%, Auger=0.00437023%. 모델 내부 3채널 비율이며 EQE/검증된 IQE는 아님.
- 다음 n4 Auger도 동일 8개 영역 적분; 이후 5V 비교 및 동일 전류 조건 분리. 실제 서버 코드 변경 없음.

## 2026-10-12 — 주수빈 n4_des 8-QW SRH integration observed
- SVisual Field Integration: n4_des srhRecombination eight separate 2D QW regions total=1.441170e7 s^-1 um^-1; total domain=0.02400002 um^2. Clean regions subtotal=14319161.96; DmgL subtotal=92534.28866 (from rounded output).
- Compared with n2 SRH total=3.656294e7, n4 SRH drops 60.5839%; radiative total n2=40072.82 vs n4=7056.261 drops 82.3914%. Two-channel Rrad/(Rrad+SRH): n2=0.10948%, n4=0.04894%. These are NOT final IQE; Auger still pending and terminal currents differ at nominal 5V.
- NEXT: Integrate AugerRecombination for same eight QW regions in n2 and n4, preserve signed values; compare at equal current separately. No TCAD inputs modified.

## 2026-10-12 — 주수빈 5V_TEST n2 8-QW SRH SVisual integration (OBSERVED)
- 실제 사용자 제공 SVisual Field Integration 원문: dataset n2_des, field srhRecombination (lowercase s), 8 separate 2D QW ROI Clean_QW1..4 + DmgL_QW1..4. Reported Total Integral=3.656294e+07 s^-1 um^-1, Total Domain=2.400002e-02 um^2.
- Clean_QW1=7.765839e4, QW2=5.464576e4, QW3=5.841611e5, QW4=3.561769e7; Clean subtotal from rounded entries=36,334,155.25 s^-1 um^-1.
- DmgL_QW1=4.966036e2, QW2=1.416049e2, QW3=1.655249e3, QW4=2.264962e5; DmgL subtotal from rounded entries=228,789.6575 s^-1 um^-1.
- Display-rounded 8 entries sum=36,562,944.9075, differs from authoritative SVisual Total=36,562,940 by 4.9075 due to field output rounding. QW4 total SRH share ~98.0342%; DmgL share ~0.62574%.
- Previously n2 same 8 QW ROI Radiative total=4.007282e+04; 2-channel radiative share (excluding Auger) =0.10947957%, NOT final radiative fraction or IQE. 12 sidewall DmgL trap concentrations in n2=0; background SRH remains ON; no proven causal attribution.
- NEXT: n4_des srhRecombination integration on same 8 ROI; then AugerRecombination both n2/n4 before final ratio and equal-J discussion. No simulation or source modifications.

## 2026-10-12 — JuSubin 5V_TEST n2/n4 4QW RadiativeRecombination integration (OBSERVED)
- 작업자: 주수빈; AI: ChatGPT. 실제 Sentaurus Visual `Field Integration` 출력 원문 제공. 8개 2D QW ROI: Clean_QW1..4 + DmgL_QW1..4, '+' 결합 경계 제외. 단위 s^-1 um^-1; 각 n2/n4 적분 총 Domain=2.400002e-02 um^2.
- NtSide=0 n2 total=4.007282e+04; Clean total=3.995389e+04; DmgL total=1.189258452e+02. NtSide=1e18 n4 total=7.056261e+03; Clean total=7.03327165e+03; DmgL total=2.298885541e+01.
- n2→n4 radiative integral -82.3914% at nominal 5V; Clean -82.3965%; DmgL -80.6696%. QW4 strongly dominates radiative integral.
- IMPORTANT: n4 5V raw terminal current 7.050e-12 vs n2 1.4480164608e-11 (-51.31%), so observed radiative decrease is NOT an IQE decrease or controlled equal-J causal estimate. Bias at TDR should remain independently checked if needed, 2D AreaFactor/current normalization unverified.
- Prior live preprocessed cmd diff observed only trap Conc=0→1e18 and node output filename changes; both Grid=n1_msh.tdr, Parameters=FASTC1_pp6_des.par. Exact parameter runtime version / physical baseline validation unresolved.
- NEXT: Integrate SRHRecombination (or signed SRH field where listed) and AugerRecombination on precisely same eight 2D QW regions for both n2/n4; then compute Rrad/(Rrad+RSRH+RAuger) carefully with any signed generation terms, evaluate equal-current comparison separately. No server source changes.

## 2026-10-12 — JuSubin 5V_TEST n4 final result verified by 이택규
- 2026-10-12 현재 작업자 이택규가 SWB Node4 Explorer 실제 `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/n4_des.out` 마지막 화면 제공. 노드 n4: 5.000E+00 V, electron current 7.534E-14, hole current 6.975E-12, total terminal current 7.050E-12 (log raw values; 2D units/AreaFactor unverified), successful `n4_5V_ckpt_des.sav` and `n4_des.tdr` writes, `Curve trace finished`, `Sentaurus Device simulation finished`, `Good Bye`. Finished Mon 2026-10-12 00:12:02 KST; wallclock 29806.55s (~8h16m46.55s), CPU total 80172.55s, peak memory 3.11GB. **CONFIRMED 5V SDevice n4 completion**, but screenshot does not show NtSide parameter: intended n4 NtSide1e18 split condition NOT CONFIRMED until pp4_des.cmd actual DmgL trap `Conc` audit and parent n2 input comparison. Previous 5V_TEST NtSide0 n2 terminal raw I2D~1.4480164608e-11, so n4 raw current ratio ~0.487; no trap-only causal claim without pp2/pp4 parity. CAL4V 100ns 4V MQW radiative fraction=0.0122426% remains distinct simulation and bias; do not confuse n4 5V with CAL n2 4V. GitHub COMMON_BASELINE.md explicitly says blue InGaN/GaN, xIn=0.15 4QW, nominal ~445nm; desired color BLUE not red, spectral peak not verified by EL. Researcher asks whether normal efficiency '0.1': distinguish fractional 0.1=10%, 0.1%=0.001 as fraction, 0.1 A/cm2 current density not an efficiency. None is default expected at arbitrary J; literature (Kou 2019 10.1364/OE.27.00A643; Baek 2023 10.1038/s41467-023-36773-w; Wang 2023 10.1038/s41467-023-43472-z) confirms blue microLED efficiency depends on J, fabrication and sidewalls. CAL 0.01224% is modeled MQW 3-mechanism radiative share, NOT observed experimental EQE, and physical low-J Gate0/2D current normalization still open. NEXT read-only `grep -nE 'Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp4_des.cmd | head -n 16` to confirm actual trap concentrations. Further compare pp2/pp4 other physics/current and matched 5V QW recombination; preserve all existing outputs. No server code modified.

## 2026-10-12 — JuSubin CAL4V full-MQW results verified by LeeTaekGyu
- 2026-10-12 이택규가 Sentaurus Visual 캡처 3장으로 완료된 `CMP_BASELINE_1.3.0_CAL4V` `n2_4V_final_des` (4.000V; custom InGaN 100ns Scharfetter taumax model) 8개 **2D** QW 영역 `Clean_QW1..4 + DmgL_QW1..4` 적분 결과를 제공. 세 필드 모두 정확히 동일 영역, Total Domain=2.400002e-02 µm². 전체 적분값 [s^-1 µm^-1]: RadiativeRecombination=6.286680e-04; srhRecombination=5.134239; AugerRecombination=2.127778e-04. 합=5.1350804458. Radiative/(Rrad+SRH+Auger)=0.01224261249%; SRH share=99.98361378%, Auger=0.004143612%. 여기서 방사비율은 해당 세 재결합 필드의 **MQW spatial integrated radiative fraction**이며, 100ns 모델 소자/실험 검증 IQE 또는 EQE가 아님. QW1 Clean+DmgL accounts for approx 98.78% all-4QW Rrad. DmgL 4QW only radiative ≈5.35942e-05 and SRH≈0.020185 (subtract clean 4QW totals; rounded), not independent lifetime physics validation. Preexisting 1ns parent result (NtSide0, **5V**) 4-QW Clean+DmgL Rrad=40072.8158452, SRH=36562944.9075, Auger=1599.706168587 and radiative fraction=0.1094747566%; because these are at DIFFERENT biases (100ns 4V, 1ns 5V), cannot attribute change to lifetime or claim 100ns improves/worsens IQE. Parent 4V near-terminal-current PLT exists but 4V TDR spatial map not yet established. Low-J Gate0 and current-normalization/physical validity still UNRESOLVED. Next inspect other user-reported completed NtSide1e18 split normal-finish log; for IQE causality compare same J/voltage/regions/geometry and effective .par, ideally reuse saved checkpoints, avoid rushing new multi-day run. No code/server run changed.

## 2026-10-12 — JuSubin CAL4V results: 4 Clean QW integrals verified by LeeTaekGyu
- 2026-10-12 이택규 provided THREE SVisual Field Integration screenshots for CAL4V final dataset `n2_4V_final_des`, 4.000V, selecting ONLY the four dimension-2 regions `Clean_QW1` through `Clean_QW4` (not damaged sidewall strips). Recombination integrals unit s^-1 um^-1, in QW1/QW2/QW3/QW4 order: Radiative [5.674131e-4, 7.202020e-6, 4.579290e-7, 8.117469e-10] (displayed total 5.750738e-4); srhRecombination [4.940556, 1.246185e-1, 4.882792e-2, 5.108214e-5] (displayed total 5.114054); Auger [2.045051e-4, 1.234635e-7, 1.495005e-8, 8.907546e-11] (displayed total 2.046436e-4). Four Clean QW total area 2.394002e-2 um2. With displayed rounded totals sum=5.1148337178 and eta_rad,clean=0.01124326%, eta_SRH,clean≈99.9848%; QW1 accounts ~98.67% of clean-QW Rrad, ~96.61% clean-QW SRH. This is CONFIRMED SCREENSHOT-BASED 4-CLEAN-QW regional recombination fraction, NOT the full MQW IQE: `DmgL_QW1..4` not selected, no 1ns matched bias / optical injection calibrated comparison. Do NOT compare raw 4V clean-QW value to earlier 1ns 5V full-Clean+DmgL MQW radiative fraction (0.10947%) as lifetime-causality. Next select the 4 additional `DmgL_QW1..4` true 2D regions (not `Clean_QW# + DmgL_QW#` interface rows), while keeping Clean_QW1..4, repeat three integrations, check exactly 8 regions and no other domains, then compare and validate AreaFactor/current. Low-J baseline gate remains UNRESOLVED; no model or server code modified.

## 2026-10-12 — 주수빈 CAL4V run results inspected by 이택규 (OBSERVED)
- 2026-10-12 이택규 공유 SVisual `CMP_BASELINE_1.3.0_CAL4V/n2_4V_final_des` Field Integration 실제 결과: Dimension 2 region `Clean_QW1` 하나만 선택, Domain=5.985012e-03 um^2; RadiativeRecombination=5.674131e-04 s^-1 um^-1; srhRecombination=4.940556 s^-1 um^-1; AugerRecombination=2.045051e-04 s^-1 um^-1. 3항 합=4.9413279182 s^-1 um^-1. Clean_QW1에 한정한 radiative fraction =0.0114830084%, SRH fraction=99.9843783%. VERIFIED screenshot-based single-region integrations and ARITHMETIC; NOT entire four QWs, not total device IQE. Other QWs may differ substantially. Next integrate 2D volume Clean_QW1..4 AND DmgL_QW1..4 in all three fields (avoid `Clean_QW1+DmgL_QW1` interface rows if shown as Dimension 1). Compare 100ns 4V with 1ns at matched V/J and check current normalization. No TCAD source edits. NtSide1e18 split separate log verification remains.

## 2026-10-12 — CAL4V final 4V and current externally confirmed (이택규 log check)
- 이택규가 실제 `CMP_BASELINE_1.3.0_CAL4V/n2_des.log` grep 출력 공유. 마지막 `Computing BE-step from 0.799739 s to 0.8 s (Stepsize: 2.6098e-04 s)` 직후 `anode 4.000E+00 5.270E-20 3.498E-14 3.498E-14`가 표시됨. 직전 단계 0.798939→0.799739s에서는 anode 3.999V, 총전류 표기 3.496E-14. 앞서 확인된 동일 Node2 `Curve trace finished` / `Good Bye` 및 final `n2_4V_final_des.tdr`, `n2_4V_ckpt_des.sav` 저장과 연결되므로 100ns CAL4V에서 최종 time 0.8s / anode 4.000V, 로그 전류 마지막 열 3.498E-14 달성과 정상 완료 CONFIRMED. 로그 전류 물리 단위/2D AreaFactor 및 정상 DC상태는 독립 검증 미완료; 기존 기록의 2D A/um 관행에 따른 원시 수치이며 조건 없이 면적 전류밀도나 IQE로 간주하지 않는다. 참고: 기존 1ns 5V_TEST 가까운 4.003369V에서 I2D=3.505521343e-14였고 CAL4V 4.000V와 약 0.2% 원시 전류 차이이나 서로 완전한 동일 바이어스 아님. 100ns의 재결합 개선 여부 미확정. NEXT 이미 확보한 final TDR의 4QW별 Radiative/SRH/Auger 적분과 비교전류 정상화 후 연구 판단; 별도 NtSide1e18 split은 실제 로그 미검증. 원본 데이터 보존.

## 2026-10-12 — CAL4V completed (confirmed by Lee TaekGyu screenshot)
- 주수빈이 수행한 CMP_BASELINE_1.3.0_CAL4V Node2 calculation: 이택규 제공 n2_des.out 마지막 화면에서 Sentaurus Device simulation finished / Good Bye, final TDR n2_4V_final_des.tdr 및 checkpoint n2_4V_ckpt_des.sav 저장 완료 확인. 종료 시각 Oct 12 01:12:13 KST; elapsed 29706.72s. Final anode current / exact voltage and IQE not visible in image and still require analysis. NtSide1e18 split 별도 실로그 확인 대기. Original baseline, running jobs not modified.

## 2026-10-12 — 주수빈이 수행한 것으로 보고된 두 계산 완료 소식 (이택규 전달; USER-REPORTED)
- 이택규가 2026-10-12 대화에서 주수빈이 전날 실행해 두고 간 '두 개' 시뮬레이션이 모두 끝났다고 보고. 직전 인수인계상 대상은 (1) 기존 `JUSUBIN_FAST_HALF_5V_TEST` 기반 NtSide=1e18 split과 (2) `CMP_BASELINE_1.3.0_CAL4V` (100ns, 0→4V)로 추정되며 **어느 두 SWB node인지 실제 로그나 화면으로 확인하기 전까지 프로젝트/노드 매칭 미검증**. 사용자 보고는 완료 주장의 근거이나 actual SDevice `Good Bye`/final V/timestep/terminal current/PLT/TDR/SAV는 미제공. NtSide=1e18 case가 NtSide-only matched input인지도 재확인 필요. 새 런이나 baseline freeze를 의미하지 않음. 기존 5V_TEST NtSide0 및 5V CAL 보호. 다음: 두 SWB 노드 이름, `n*_des.log` 마지막 35~50행, `pp*_des.cmd` Goal/Trap, 생성 PLT/TDR/SAV 확인→주입 전류 및 4QW Rrad/SRH/Auger를 동일 바이어스/전류 조건에서 비교. Gate0 낮은 J, 물리적 IQE/Full-Half 검증은 계속 미해결.

## 2026-10-11 — JuSubin reports 4V CAL4V Run initiated after FinalTime=0.8 check (USER-REPORTED; SOLVER START UNVERIFIED)
- Worker 주수빈 explicitly reports checking `FinalTime=0.8` in separately cloned `CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd` and clicking SWB **Run** for the new CAL4V simulation. The previous screenshot independently verified this clone's `Goal anode Voltage=4.0`, post-transient `Plot(FilePrefix="n@node@_4V_final")` and `Save(FilePrefix="n@node@_4V_ckpt")`, and custom `FASTC1_pp6_des.par` InGaN Scharfetter `taumax=1.0e-7s` for electrons/holes. New `FinalTime=0.8` is **USER-CONFIRMED**, not in a new screenshot. This retains nominal 5V/s ramp 0→4V. Source editing DONE by user; SWB Run action USER-REPORTED.
- Do NOT claim run has entered SDevice, succeeded or finished; **no new generated `ppN_des.cmd`, `nN_des.log`, job status, process PID, PLT, spatial TDR or SAV supplied yet.** SWB may auto-preprocess on Run; verify actual preprocessed Goal=4.0 FinalTime=0.8 Plot/Save and parameter file, and initial log for syntax/error/accepted time steps. End-point Plot/Save created only after successful final solve. Do not promise it finishes tonight.
- NEXT short READ-ONLY run-health check in `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V`: `ls -lt n*_des.log n*_des.err n*_des.out 2>/dev/null | head -n 12`; based on actual node filename, `tail -n 35 nN_des.log` and `grep -nE 'FinalTime|Voltage|4V_final|4V_ckpt|Parameters' ppN_des.cmd`; inspect SWB status screenshot if no logs yet. Leave existing 5V `CMP_BASELINE_1.2.0_CAL` and completed `JUSUBIN_FAST_HALF_5V_TEST` untouched; NtSide1e18 separate split status also not yet confirmed.
- Scope: exploratory SRH 100ns/4V sensitivity model. Prior low-J Gate0 and 5V_TEST physical baseline freeze unresolved. No ChatGPT access to school server, no direct run or code edit by assistant.

## 2026-10-11 ~17:4x KST — JuSubin CAL4V cloned source edit and 100ns .par CONFIRMED (OBSERVED screenshot; preprocess/run pending)
- Worker 주수빈 supplied terminal screenshot from directory `CMP_BASELINE_1.3.0_CAL4V` showing actual post-edit `sdevice_des.cmd` tail: `Goal {Name="anode" Voltage=4.0}`, old transient step controls retained (`InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2`), `Coupled(Iterations=15){Poisson Electron Hole}`, following Transient close `Plot(FilePrefix="n@node@_4V_final")` then `Save(FilePrefix="n@node@_4V_ckpt")` still inside overall Solve. Source edit **OBSERVED/CONFIRMED** (unlike prior unexecuted terminal heredoc).
- Separate local-to-server read-only grep in screenshot confirms cloned custom `FASTC1_pp6_des.par` `Material="InGaN" {Scharfetter {taumin=0,0; taumax=1.0e-7,1.0e-7; Nref=1.0e16,1.0e16; gamma=1,1; Talpha/Tcoeff/Etrap=0}}` at lines 46–56. Thus intended 100ns **max lifetime input** preserved in clone; material effect in finished simulation not yet proven.
- Screenshot `tail` is cropped ABOVE final-time declaration; `FinalTime=0.8` and actual mesh/grid existence require further independent read-only check. Earlier sed command was instructed to set it, but only Goal4 and Plot/Save + material par can be asserted from current image. No intermediate 3.8V Plot/Save appears, and **recommend NOT adding** it now because it is optional and user wants to launch promptly; final 4V Plot/Save suffice if entire sweep converges.
- NEXT READ-ONLY in cloned project: `grep -nE 'FinalTime|Voltage|FilePrefix|Plot\(|Save\(' sdevice_des.cmd` confirm FinalTime0.8, Goal4, output; `ls -lh n1_msh.tdr` optional if SDE output reused. SWB Preprocess on CAL4V node only; inspect generated ppN for actual Goal/FinalTime/Plot/Save and Parameters .par; Run only after preprocessing is clean, monitor early log; preserve running original `CMP_BASELINE_1.2.0_CAL` 5V and completed `JUSUBIN_FAST_HALF_5V_TEST`. User has not shown preprocess, run, or 4V TDR.
- Physical low-J Gate0 and paper-grade baseline freeze remain unresolved.

## 2026-10-11 17:39 KST — JuSubin confirms CAL4V clone still 5V source, before terminal patch (OBSERVED)
- User terminal screenshot directly shows normal shell read-only grep of `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd`: line 587 `FinalTime = 1.0`, line 597 `Voltage = 5.0`, line 608 `FilePrefix = "n@node@_5V_ckpt"`. There are also 0V initial electrodes at lines 38/43. No `3p8V`, `4V_final`, `4V_ckpt`. Confirms previous lengthy Python heredoc did NOT change this clone; no 4V simulation launched. Existing CAL5V remains separate active job.
- Decision: perform safe backup and short single-line shell sed edits in clone only. Replace FinalTime1.0→0.8, transient Goal Voltage5.0→4.0 (preserving 5V/sec rate), rename post-transient checkpoint to 4V, insert spatial Plot at 4V; optionally add intermediate t=.76 (~3.8V) Plot and Save once Solve shape checked. Do not touch 0V electrode defaults or custom CAL InGaN Scharfetter `taumax=1e-7`. Verify effective custom .par after clone; current `sdevice_des.cmd` grep alone does not prove clone's material params.
- NEXT: backup `sdevice_des.cmd` within `CMP_BASELINE_1.3.0_CAL4V`, use short commands in ordinary shell, grep/tail source after, SWB Preprocess only and check generated ppN/Plot/Save before RUN. This is a diagnostic 4V CAL, not frozen physical baseline. No remote edit performed by ChatGPT.

## 2026-10-11 17:36 KST — CAL4V cloned source file observed
- Screenshot confirms normal shell prompt recovered after multiline input error. `ls -l` confirms `CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd` exists at 5981 bytes with Oct9 23:35 mtime. Whether 4V patch was applied is UNKNOWN; no SUCCESS/STOP output seen.
- Next read-only grep FinalTime/Voltage/3p8V/4V_* before source edit, then use short single-line change with backup on clone only. No run verified; active original CAL must be preserved.

## 2026-10-11 ~17:30 KST — JuSubin reports repeated `?` continuation prompt, CAL4V terminal edit still BLOCKED
- User confirms shell remains stuck at `?` even after prior instruction; previous long Python heredoc did not show any `SUCCESS` or `STOP`. Do not treat code edit as applied. Most likely interactive csh/tcsh multiline/here-document handling, but exact syntax state unverified.
- Safe immediate action: terminal focus → Ctrl+C until normal `$`/`%` prompt → type `bash` as separate command → read-only `ls -l /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd` to check whether separately cloned project actually exists. If absent, clone CAL in SWB before editing. After confirming prompt/target, use shorter Bash-compatible patch, backup before edits and grep source before SWB Preprocess. Do not retry multiline at `?`, do not touch live original CAL or finished 5V_TEST.
- Remaining blocker: new 4V CAL source change, SWB Preprocess/Run have not been verified. NtSide1e18 split plan is separate.

## 2026-10-11 ~17:28 KST — JuSubin shell multiline paste pending (OBSERVED screenshot; source edit UNVERIFIED)
- User attempted to paste proposed Python heredoc updater into MobaXterm terminal for separate 4V CAL clone. Terminal screenshot shows line prefixes `?` throughout the Python body and the closing `? PY` line. There is **no returned shell prompt, SUCCESS or STOP output** visible. `?` indicates the remote interactive shell is still taking multiline input; it is NOT proof Python ran or the 4V source was changed. This is not a TCAD run error.
- Guidance: press Enter once after closing `PY`; if still continuation prompts, Ctrl+C and use bash explicitly (shell may be csh/tcsh). Then read-only inspect candidate `sdevice_des.cmd` for `FinalTime, Voltage, 3p8V, 4V_final, 4V_ckpt` and backup file presence before SWB Preprocess/Run. Never assert edit succeeded before verification, and do not edit/run original active `CMP_BASELINE_1.2.0_CAL`.
- Blocker: user needs safe terminal confirmation of 4V clone input modification. NtSide1e18 parent split run also not yet confirmed. No actual server control by AI.

## 2026-10-11 17:20 KST — JuSubin confirms live CAL source Solve tail; 4V clone patch prepared (OBSERVED original / PROPOSED patch, NOT APPLIED)
- User screenshot of actual READ-ONLY `tail -n 65 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/sdevice_des.cmd`. Observed original post-initialization `Transient(InitialTime=0.0 FinalTime=1.0 InitialStep=1e-5 MinStep=1e-9 MaxStep=1e-3 Increment=1.2 Goal{Name="anode" Voltage=5.0}) {Coupled(Iterations=15){Poisson Electron Hole}}`, followed by `Save(FilePrefix="n@node@_5V_ckpt")`. A stale comment claims 0→0.3V smoke; actual Goal 5.0V. This explicitly resolves prior uncertainty about ramp and source placeholder syntax.
- Assistant supplied copy/paste replacement ONLY from stale smoke comment to end of `Solve` **in a newly cloned SDevice source**, with unchanged initial Coupled solves and 100ns InGaN custom parameter: `FinalTime=0.8`, `Goal{Name="anode" Voltage=4.0}` so same 5V/s ramp; other time-step/Newton unchanged. Include during Transient an optional-protection intermediate spatial `Plot(-Loadable FilePrefix="n@node@_3p8V" Time=(0.76))` and `Save(FilePrefix="n@node@_3p8V_ckpt" Time=(0.76))` (3.8V at t=.76 if voltage ramp linear); after normal end post-transient `Plot(FilePrefix="n@node@_4V_final")` and `Save(FilePrefix="n@node@_4V_ckpt")`. Verified command syntax against Sentaurus Training sd_8 and sd_4; must **preprocess and verify actual pp output** on local T-2022.03 before RUN.
- PROTECTION: do not edit active `CMP_BASELINE_1.2.0_CAL` folder or generated `pp2_des.cmd`; do not stop live n2 that already accepted ~4.179V. Do not mix parent `JUSUBIN_FAST_HALF_5V_TEST` 1ns SRH custom .par or planned NtSide=1e18 split into new 100ns CAL NtSide0 branch. Proposed name `CMP_BASELINE_1.3.0_CAL4V`, confirm unoccupied on remote server.
- Next SWB clone→edit `sdevice_des.cmd` source via Edit Input Commands→Preprocess only→read-only inspect generated ppN Goal/FinalTime/3.8/4V output and included custom `FASTC1_pp6_des.par` 100ns→RUN node→log/PLT/tdr file proof. No actual school-server edits or new run confirmed yet. New 4V branch needs hours to run and 4V completion not guaranteed today. Root physical low-J Gate0 unresolved.

## 2026-10-11 — JuSubin DECISION: stage CAL 100ns 4V branch for run today (CODE PROPOSAL, NOT APPLIED)
- Worker 주수빈: in addition to a separate 5V_TEST NtSide=1e18 split, wants to edit today's 100ns CAL maximum applied voltage from 5V to 4V and launch before leaving. User explicitly requested code revision, but **school-server SWB files are not directly accessible from GitHub/ChatGPT**; no server changes or run verified. Running original `CMP_BASELINE_1.2.0_CAL` last accepted ~4.179V is NOT to be edited in-place, since altering on-disk input cannot retroactively make it save the earlier ~4.0V TDR.
- Planned versioned clone, tentative unique project name `CMP_BASELINE_1.3.0_CAL4V` (must check not already used on school server before creation). Preserve original CAL and 5V_TEST, and 100ns InGaN Scharfetter custom `FASTC1_pp6_des.par`. New case NtSide=0, all material/physics/mesh/solver unchanged except intentional voltage sweep endpoint and output scheduling.
- Known 5V parent/CAL 0→5V ramp: Transient InitialTime=0, FinalTime=1.0s, Goal anode Voltage=5.0V, InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Coupled Iterations=15; post-transient Save named `n2_5V_ckpt`. For matching original 5V/sec ramp up to 4V, change BOTH `FinalTime=0.8` AND `Goal {Name="anode" Voltage=4.0}` (changing only Goal with FinalTime=1 changes dV/dt), and after completed Transient add explicit `Plot(FilePrefix="n@node@_4V_final")` and `Save(FilePrefix="n@node@_4V_ckpt")` within Solve. TDR contains QW spatial fields selected by existing Plot section; PLT stores IV. Do not change Mesh, NtSide, active custom 100ns lifetime, Math/Physics, or original parent's already-completed results.
- Guardrail before copy/paste full live code: **READ ONLY** `sed -n '580,612p' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/pp2_des.cmd` and `sed -n '/^Solve[[:space:]]*{/,/^}/p' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/sdevice_des.cmd` (second command could be adapted for braces); actual live Solve block not fully shared yet, avoid replacing initialization portions. Source file `sdevice_des.cmd` edited in SWB clone, **never manually modify preprocessed `pp2_des.cmd`**. Clone preprocess validate Goal=4/FinalTime=.8, Plot/Save paths, custom .par 100ns, then run node2 only and confirm new log/TDR. 4V convergence is not proof physical baseline/IQE valid; low-J Gate0 remains.
- Status: design explained and evidence-based syntax from Sentaurus Training chapters sd_8/sd_1; user hasn't shown revised live cmd, preprocessing or run log. 5V CAL process not interrupted; 5V_TEST NtSide1e18 launch unverified.

## 2026-10-11 — 주수빈 DECISION: use completed 5V_TEST NtSide=0 reference; proceed with NtSide=1e18 split (DECISION / RUN NOT YET VERIFIED)
- Worker 주수빈 explicitly states CAL runtime is too costly and decides to continue without waiting by using `JUSUBIN_FAST_HALF_5V_TEST` completed NtSide=0, 0→5 V 5V-tested solver result as **working comparative parent** and launching/checking a companion **NtSide=1e18** SWB split. This is a concrete research workflow decision, **not proof NtSide=1e18 run started, preprocessed, converged, or reached 5 V**. Keep NtSide=0 files/results and archived parent unchanged; retain CAL as separate 100ns hypothesis/sensitivity (no stop authorized).
- VERY IMPORTANT provenance: older different branch Sep26 Node12 NtSide=1e18 initialized and failed; its Node6/12 PP decks .par were different/stale, so cannot call old completed NtSide0 and old failed NtSide1e18 an apples-to-apples test. New planned split must come from **the same 5V_TEST SDE/SDevice/custom .par revision** and differ in NtSide only; check effective preprocessed trap Conc at all intended damaged regions and consistent Physics/Math/Solve/parameter reference, rather than simply reusing stale cached output. If same-project split risks invalidating completed results, back up/archive first or clone a separately versioned SWB project per PROJECT_NAMING_CONVENTION.
- QUICK PRE-RUN GATE: (1) preserve `JUSUBIN_FAST_HALF_5V_TEST` completed node n2 log/PLT/TDR and input hash, (2) SWB split setting NtSide=0 vs 1e18 while preserving 0 branch, (3) preprocess new SDevice node and compare new `ppN_des.cmd` with completed `pp2_des.cmd` ignoring expected NtSide trap Conc/output node names, verify `FASTC1_pp6_des.par` same physics and exact 5V goal, (4) only then run new trap-ON SDevice, monitor initial log for convergence and 5V completion. Avoid waiting multi-days for a broken parameter or cached source. Do not regenerate new `sdevice.par` default-Silicon or mix CAL 100ns custom .par into 1ns parent.
- Research qualification: this choice is a **working/numerical baseline operational decision**, NOT scientific Common Baseline freeze; original parent low-J Gate0 and QW SRH issue persist (4QW radiative share 0.10947%, provisional J_5V~7.24e-4 A/cm²). NtSide1e18 can serve comparison only if both branches truly share identical physical input except trap concentration, and trap-on converges. Publication-level A/B IQE still requires current/AreaFactor + physical injection, region-integrated rates and mesh/full equivalence.
- No direct school-server SWB run/start/edit from ChatGPT in this turn; user announced plan. Next: request SWB parameter table/tree screenshot showing both NtSide values or new node PP command output; guide preprocess check then run. CAL preserved.

## 2026-10-11 — JuSubin corrects baseline diagnosis chronology: CAL built from prior TaekGyu audit (CONFIRMED historical records; physics still UNRESOLVED)
- Worker 주수빈 pointed out that 이택규 had **already analysed** `JUSUBIN_FAST_HALF_5V_TEST`'s low-current/low-radiative issue on 2026-10-09 and purposely modified cloned CAL. Cross-checked LeeTaekGyu TIMELINE: complete 5V_TEST NtSide0 4-QW integrated Rrad=40072.8158452, SRH=36562944.9075, Auger=1599.706168587 [s^-1 um^-1], Rrad fraction≈0.1094747566%. These show strong *bulk SRH* recombination in QWs with sidewall parameter NtSide0, not an established sole cause of low contact current.
- Actual factory `MaterialDB/InGaN.par` was inspected by 이택규: default `Scharfetter taumax=1e-9s` both carriers (other defaults C=2e-10, Auger A=1e-30); independent published 100ns case motivated a **literature-based hypothesis/sensitivity check**, NOT proven cause. On 2026-10-10 researcher saved cloned `CMP_BASELINE_1.2.0_CAL/FASTC1_pp6_des.par` with `Material="InGaN" { Scharfetter { taumin=0,0; taumax=1e-7,1e-7; Nref=1e16,1e16; gamma=1,1; Talpha/Tcoeff/Etrap=0 } }`; live file output and user's clarification **OBSERVED/CONFIRMED FILE EDIT**. Parent 5V_TEST preserved. Effective spatial lifetime/100ns impact in running CAL and physical model validity not yet validated.
- IMPORTANT corrected guidance: do **not** ask JuSubin to repeat baseline initial material-file audit or claim CAL was unmotivated. The existing diagnosis was performed and one candidate repair attempted, but low-J Gate0 NOT closed. At nearly matched bias, parent 5V_TEST ~4.00337V PLT I2D=3.505521343e-14 A/um and CAL ~3.99967V I2D=3.497895e-14 A/um (~0.22% raw difference across nonexact biases); this does not show improved injected current at ~4V (nor definitively proves the 100ns runtime effective). Parent 5V at 1.44801646e-11 A/um remains low under conditional normalization. IQE changes at matched injection require spatial QW outputs, which CAL currently lacks near 4V.
- NEXT: review previous baseline audit conclusions as starting point; evaluate CAL relative to parent at matched current/voltage (and QW rates when output exists), verify effective lifetime if scientifically necessary without assuming earlier file work wasn't done. Investigate EBL/transport/polarization/current normalization *remaining* questions, not restart known SRH discovery. Preserve active CAL until output/checkpoint plan; original Common Baseline still not frozen. No school-server changes.

## 2026-10-11 — JuSubin asks to reuse completed 5V_TEST as working baseline (PROPOSED; freeze NOT approved)
- Worker: 주수빈. Research question: instead of waiting for extremely slow `CMP_BASELINE_1.2.0_CAL` 100ns-sensitivity run, can the already completed `JUSUBIN_FAST_HALF_5V_TEST` serve as baseline?
- Review: **YES as numerical/working reference ("solver golden")**, because `JUSUBIN_FAST_HALF_5V_TEST` NtSide=0 achieved full 5.000V transient on 2026-10-09 14:29:52 KST with log completion, and existing TDR/PLT/mesh can be audited without new expensive SDevice runs. **NO as physically validated, frozen common baseline** yet. Distinguish computation completion from qualified MicroLED operation.
- Pending Gate0: raw 2D I2D=1.44801646e-11 A/um at 5V, conditional J≈7.24e-4 A/cm² using 2µm half mesa and documented convention (2D normalization, geometry, AreaFactor, displacement/steady-state still need independent verification); all-QW radiative recombination share previously estimated ≈0.1095% is **not an independently validated IQE**. No proof realistic LED injection despite solver success. Region-specific Mg incomplete-ionization species interpretation, QW material/lifetime/polarization/transport remain unqualified.
- Validation gates: NtSide=0 trap OFF 12 regions verified; NtSide=1e18 trap-ON matched-reference solution not established. Half+Coarse vs Full/Fine mesh/geometry convergence, A/B common conditions and source hashes/clean-account reproduction still pending.
- Proposed approach: preserve `JUSUBIN_FAST_HALF_5V_TEST` and archived source unchanged; treat as WORKING numerical reference, not overwrite `COMMON_BASELINE.md` "freeze". Do inexpensive READ-ONLY audit of completed n2_des.plt/TDR/pp2 cmd and current components / 2D J, QW band/injection/recombination, then target one well-justified calibration/short pilot in a new versioned copy only after researcher approval. Compare matched J and trap-on; proceed to publication-level Project A/B only after physical Gate0. CAL sensitivity does not gate initial audit; keep running job unchanged unless user explicitly decides stop after spatial data preservation plan.
- Status: PROPOSED, no SWB/TCAD changes executed in this response.

## 2026-10-11 ~16:5x KST — JuSubin proposes 4V instead of 5V for future CAL runs (PROPOSED / NOT IMPLEMENTED)
- Researcher asks whether very slow 5V `CMP_BASELINE_1.2.0_CAL` run should instead have 4V endpoint and what applied bias represents; assistant reviewed `CMP/COMMON_BASELINE.md`: Common Physics explicitly says `Initial forward sweep 0 → 5 V`, but does **not** document a special physical 5V threshold or numeric reason it is mandatory.
- Interpretation: 5V was a broad initial forward-bias characterization limit for I–V, injection and sidewall defect comparison, **not a validated device operating voltage**. InGaN/GaN LED IQE and A/B comparisons need meaningful injected current density and QW recombination at matched J; fixed applied bias alone is not the acceptance criterion.
- Existing completed `JUSUBIN_FAST_HALF_5V_TEST`: nominal half-width normalized 5V J ~7.24e-4 A/cm2 (LOW-J Gate0). Separate `CMP_BASELINE_1.2.0_CAL` 100ns transient PLT at 3.99967374V: I2D 3.497895e-14 A/um, conditional nominal J ~1.75e-6 A/cm2 for 2um width; most recent accepted ~4.179V I2D 5.555e-14 A/um, conditional J ~2.78e-6 A/cm2. Geometry/AreaFactor/displacement and SRH lifetime differences prevent direct physical A/B comparison. Low J remains unresolved irrespective of choosing 4V.
- 4V **diagnostic/pilot upper limit is technically acceptable as a proposal**, not common-baseline freeze or universal A/B production cutoff. Do not alter original Common Baseline's 0→5V definition or live CAL without explicit approval. Current CAL already above 4V, so editing endpoint/aborting now will not retroactively produce a saved 4V spatial TDR; current preprocessed `Save(FilePrefix="n2_5V_ckpt")` is after Transient, no 4V intermediate Plot/Save seen. If using new separately cloned 4V pilot, choose explicit time-voltage ramp and in-run 4V spatial output, preserve comparable rate/physics when comparing to 5V parent, verify 100ns effective .par override and do minimal convergence test before full solve.
- NEXT: Read-only confirm full Transient `Goal` via `sed -n '580,612p' .../pp2_des.cmd`, evaluate data-save paths and conditional termination. Decide separate 4V pilot after user confirmation. No school-server operations or code changes.

## 2026-10-11 ~16:46 KST — JuSubin CAL node2 Plot/Save audit (OBSERVED pp2_des.cmd excerpt)
- User-provided screenshot of READ-ONLY grep on actual `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/pp2_des.cmd`. `File` section lines 20-28 points `Grid="n1_msh.tdr"`, `Parameters="FASTC1_pp6_des.par"`, `Plot="n2_des.tdr"`, `Current="n2_des.plt"`, `Output="n2_des.log"`. `Plot { ... Potential ... }` at lines 379-582 specifies **variables**, not a bias-specific snapshot schedule.
- `Transient(` lines 585+, `InitialTime=0.0`, `FinalTime=1.0`, `InitialStep=1e-5`, `MinStep=1e-9`, `MaxStep=1e-3`. After `Transient` closes at lines 604-605, `Save(FilePrefix="n2_5V_ckpt")` occurs at lines 607-609. The grep listed **no intermediate in-transient `Plot(Time=...)` or `Save(Time=...)`** for ~4V.
- Interpretation: existing `n2_des.plt` records terminal I–V near 4V, but neither setting the global TDR filename nor declaring Plot variables proves a 4V spatial TDR exists. Post-transient Save is reached on normal traversal of the Solve sequence after Transient, not automatically at 4V. Do NOT Stop/Abort CAL before assessing loss of unsaved spatial state. Previous top-level n2 listing showed no n2*.tdr/sav; alternate paths not excluded.
- Note line584 comment `Short syntax/mesh/physics smoke: 0 -> 0.3 V only` appears inconsistent with independently accepted ~4.179V; it may be stale and is not proof of active goal. The actual `Goal` lines were not visible in grep; verify `sed -n '580,612p' .../pp2_des.cmd` READ-ONLY before asserting exact ramp mechanics or Save execution.
- NEW attention: `Parameters="FASTC1_pp6_des.par"`; intended 100ns lifetime override should be checked against the *effective* parameter file and runtime log before claiming calibration, but do not change a running model.
- Status OBSERVED command excerpt / UNRESOLVED 4V spatial TDR, 5V completion and physical low-J Gate0. No SWB/SDevice/CAL changes.

## 2026-10-11 ~16:45 KST — JuSubin confirms CAL SDevice command file names (OBSERVED screenshot)
- User ran read-only `ls -lh /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/*des.cmd` on school server. Screenshot lists **`FASTC1_pp6_des.cmd` (~5.5K; Oct9 23:35), `pp2_des.cmd` (~5.8K; Oct10 00:40), `sdevice_des.cmd` (~5.9K; Oct9 23:35)** in CAL folder. File *presence* verified, content / actual Plot/Save directives still **UNRESOLVED**. `pp2_des.cmd` is the next candidate to inspect as node 2 preprocessed deck, not yet shown to be the active executed input by file contents alone.
- Prior accepted CAL n2 ~4.179 V screenshot still latest direct solver observation; no newly proven voltage progression in this screenshot. Older 4V PLT exists, but spatial 4V TDR/SAV not found in initial top-level n2 listing; other names/paths and save schedule unknown.
- NEXT READ-ONLY: `grep -nEi -C 4 'Plot|Save|CurrentPlot|Time[[:space:]]*=' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/pp2_des.cmd | tail -n 120` to inspect effective Plot/Save directives. Do not modify/Stop/Abort CAL; low-J baseline Gate0 unresolved.

## 2026-10-11 ~16:41 KST — JuSubin CAL 100 ns advances to accepted ~4.179 V (OBSERVED n2_des.out screenshot)

- Worker: 주수빈, ChatGPT. Source: user-provided MobaXterm live `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.out` screenshot. This is the separate InGaN SRH-lifetime 100 ns sensitivity case, **not** the already completed 5V_TEST parent.
- A BE step `0.835804 -> 0.835806 s` (stepsize `1.9143e-06 s`) **accepted** with Newton iteration 2 `|Rhs|=7.30e-04 < 1e-03`, `Finished, because |RHS| less than 1e-3`. Accepted anode voltage **4.179E+00 V** and anode terminal `TotalCurrent=5.555E-14` (2D A/um convention; transient displacement/current-density normalization unresolved). At 0-to-5 V per 1 s ramp this corresponds to **~83.58% of bias sweep, not wallclock progress**.
- Next trial `0.835806 -> 0.835808 s`, step `2.2972e-06 s`, screenshots show Newton iterations 0-6 with RHS `~1.03e-03 to 1.09e-03` for iterations 2-6, slightly above `RHSMin=1e-03`. Whether this trial later converges or cuts back is **UNRESOLVED**: screenshot ends mid-iteration; no displayed fatal error or simulation completion.
- Relative to 2026-10-10 ~22:30 saved PLT row 4.14965446 V, latest accepted displayed ~4.179 V is ~0.0293 V higher, with different display precisions/sources. No credible 5V ETA from voltage fraction, especially with repeated tiny steps.
- Existing low-injection / very-low-J Gate 0 persists: no physical baseline freeze or Project A/B production. Previous CAL folder top-level listing had no n2*.tdr/sav; investigate alternate stored spatial outputs and actual Plot/Save directives **READ-ONLY**, do not assume stopping produces a usable 4V TDR. No SWB, code, running job or solver change performed by ChatGPT.
- NEXT: preserve CAL, read-only inspect current later log/out + `ls .../*des.cmd` then `grep -nEi -C 3 'Plot|Save|CurrentPlot|FinalTime|Time[[:space:]]*=' .../pp2_des.cmd` (use actual existing cmd file), and check alternate TDR locations before any shorten/stop decision.

## 2026-10-10 ~22:38 KST — CAL n2* files listed; no TDR/SAV in top-level folder (OBSERVED terminal screenshot; 4V space-state missing or saved elsewhere UNRESOLVED)

- Worker 주수빈 executed READ-ONLY `find /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL -maxdepth 1 -type f -name 'n2*' -printf '%f %k KB\n' | sort` while separate `CMP_BASELINE_1.2.0_CAL` (InGaN SRH tau 100 ns sensitivity) has been progressing slowly above 4V.
- ACTUAL top-level list: `n2_des.err 12 KB`, `n2_des.job 4 KB`, `n2_des.log 5120 KB`, `n2_des.out 5376 KB`, `n2_des.plt 1416 KB`, `n2_des.sta 4 KB`, `n2_local.err 0 KB`. **No `n2*.tdr` and no `n2*.sav` matching this level/name**; do NOT assume no data in subdirectories or alternate file names.
- Previously OBSERVED from valid `n2_des.plt`: near 4V time=0.79993475s, V=3.99967374V, TotalCurrent=3.497895e-14 A/um; last PLT entry shown at time=0.82993089s, V=4.14965446V, I=4.839436e-14 A/um. This permits *transient terminal I–V* diagnostics, but a spatial `4V TDR` suitable for plotting local QW radiative/SRH rates, IQE or bands is NOT documented by this file list.
- CAUTION: `.sta`, `.job`, `.log`, `.plt` cannot simply substitute for 4V 2D spatial state. Merely aborting at >4V will not automatically generate a 4V TDR/snapshot. Need verify `n2_des.cmd`/`pp2_des.cmd` actual Plot/Save directives and any different-named output location before deciding early endpoint; current CAL not stopped/edited. Existing low-J Gate0 remains unresolved. Reported file sizes are `find %k` allocation sizes, not necessarily exact byte sizes.
- NEXT READ-ONLY: `grep -nEi -C 3 'Plot|Save|CurrentPlot|FinalTime|Time[[:space:]]*=' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.cmd | tail -n 100` **only after checking that n2_des.cmd exists**. Otherwise use `ls .../*des.cmd` to identify actual command filename; optional deeper `find` for output types. No SWB/SDE/SDevice/CAL process change.

## 2026-10-10 ~22:30 KST — CAL 100ns 4.0V and latest 4.14965V I–V rows extracted (OBSERVED terminal screenshot; derived interpretation; CAL run untouched)

- Worker **주수빈** used read-only Python to parse 17-field `DF-ISE text` `CMP_BASELINE_1.2.0_CAL/n2_des.plt` and printed **actual near-4V record**: `time=0.79993475 s`, `anode OuterVoltage=3.99967374 V`, `anode TotalCurrent=3.497895e-14` (2D current-per-length A/um). This confirms usable transient I–V output near 4.0 V.
- The **last recorded row in this snapshot**: `time=0.82993089 s`, `anode OuterVoltage=4.14965446 V`, `anode TotalCurrent=4.839436e-14 A/um`. The screenshot was taken ~22:30 KST, but this file's stored latest record does NOT prove that the running job is still exactly at this voltage at time of reading; last successfully written output may lag solver activity.
- Consistent with 5V/1sec ramp; time ~0.8s corresponds 4V. **SRH tau=100ns** in InGaN is a physical recombination lifetime sensitivity parameter, not a simulation step length.
- SCIENTIFIC DECISION: These I–V values allow a 4V read-only current comparison, but currents remain extremely small and old low-J Gate0 is unresolved; neither 4V data availability nor reducing endpoint to 4V establishes physically valid luminous baseline/IQE. Transient TotalCurrent may include displacement current and 2D geometry normalization; need to check components and steady-state comparability. To conclude at 4V and analyze spatial band/recombination, FIRST inspect whether any ~4V TDR/SAV output or Plot/Save snapshots exist. **Do not Abort/Stop the running CAL** without deciding whether needed output is saved. Compare tau 1ns and tau 100ns only at matched voltage/current-density if datasets permit.
- NEXT **read-only**: `find /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL -maxdepth 1 -type f \\( -name 'n2*.tdr' -o -name 'n2*.sav' \\) -printf '%f %k KB\\n'` (actual shell escaping in user command needs only `\\(` escaped parens, not literal double slash). Review Save/Plot directives if no such snapshot. No SWB, source, mesh, running CAL or separate completed 5V_TEST changed.

## 2026-10-10 ~22:25 KST — CAL n2_des.plt confirmed DF-ISE xyplot text with voltage and current datasets (OBSERVED screenshot; 4V record yet UNVERIFIED)

- Worker 주수빈 ran read-only `head -n 30 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.plt` on live server. File starts `DF-ISE text`, `Info { version=1.0; type=xyplot; datasets=[...]; functions=[...]; }` followed by `Data {` with numeric rows. Dataset fields in written order: 1 `time`; 2–9 cathode OuterVoltage/InnerVoltage/QuasiFermiPotential/DisplacementCurrent/eCurrent/hCurrent/TotalCurrent/Charge; 10–17 anode OuterVoltage/InnerVoltage/QuasiFermiPotential/DisplacementCurrent/eCurrent/hCurrent/TotalCurrent/Charge. 17 numeric values per saved record (subject to file completion).
- This **confirms CAL transient output stores time, anode applied voltage, electron/hole/total and displacement current**, and can potentially extract anode I(V) at/near 4V. A head sample only covers initial zero-bias rows: **neither 4V point, its value, saved TDR state, final CAL progress, nor 5V endpoint are confirmed by this screenshot**.
- NEXT READ-ONLY: parse all available complete 17-field DF-ISE Data records with shell `python3 -c` and report nearest-4V and latest saved `time`, `anode OuterVoltage` (field index 9), `anode TotalCurrent` (index 15); note transient current includes displacement, cannot be treated blindly as steady-state J. Leave 100ns CAL running and separate baseline unchanged. If end record is being written, exclude incomplete record, do not interrupt.

## 2026-10-10 ~22:21 KST — JuSubin confirms CAL n2_des.plt exists (1.4MB) (OBSERVED via live terminal screenshot)

- Worker **주수빈** ran `ls -lh` for `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.plt` (separate 100ns InGaN SRH-lifetime sensitivity CAL). **The intended file exists**: mode `-rw-r--r--`, user semi437, displayed size `1.4M`, modification time `Oct 10 21:30`. This is only a file-existence/mtime check; **contents, accepted 4V I-V history, complete 4V TDR/checkpoint, saved dataset completeness and current numerical status are NOT verified**.
- Screenshot also shows a `No such file or directory` from `n2_des.pltls` caused by typing two commands together (extra suffix `ls`), not a missing correct `n2_des.plt`, not a TCAD solver failure.
- Prior team live CAL log at ~22:11 KST accepted ~4.149V, not 5V, and reported severe high-bias step retries. File timestamp does not prove calculation progress to a newer accepted voltage; `n2_des.plt` can be updated during ongoing computation. Preserve running CAL and prior completed 5V_TEST parent, no Stop/Abort.
- NEXT read-only command: `head -n 30 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.plt` to learn PLT format and dataset names; then inspect I(t)/V(t) at saved/accepted ~4V. Separately inspect `pp2_des.cmd` Save/Plot targets before any decision to shorten CAL. No SWB/source/job changes.

## 2026-10-10 after 22:11 KST — JuSubin asks whether slow 100ns CAL can be evaluated only through 4V (PROPOSED SCIENTIFIC CRITERIA, no run change)

- Worker **주수빈** raised same practical question as earlier 이택규 proposal: separate `CMP_BASELINE_1.2.0_CAL` (intended InGaN SRH tau 1ns→100ns, not a 100ns time step) becomes dramatically slow above 4V and asks whether 4V can substitute for 5V. No instruction to kill/change running job.
- Latest **shared GitHub 22:11 KST actual CAL log** recorded an accepted 4.149V at transient t≈0.829862s, 2D anode total current 4.832e-14 A/um. Next BE attempt oscillatory/nonconverged in visible portion; 5V completion unknown, no accurate ETA. Nominal J under previously documented half-width convention ~2.416e-6 A/cm2 (caution: transient current/displacement and normalization must be checked). Separate 5V_TEST parent successful at 5V but low nominal J~7.24e-4 A/cm2 and QW radiative share~0.1095%; this is the major Gate0 blocker.
- RESPONSE: 4V is acceptable **diagnostic or SRH sensitivity comparison at same voltage** and can support scientific A/B only if injection/current density, QW-recombination and IQE evaluated in physically relevant range at matched current density. 4V alone is not sufficient baseline acceptance, and voltage need not universally be 5V. At present low I/J, 4V termination is unlikely to resolve existing weak injection. To capture 4V, first inspect CAL `n2_des.plt` J–V history and actual `Plot/Save` coverage; **abort/stop cannot be assumed to leave a valid 4V TDR/IQE snapshot**, especially if Save only at 5V. Preserve ongoing CAL unless user explicitly decides after evidence; no new code, files, rerun or interruption.
- NEXT read only: inspect CAL `pp2_des.cmd` Save/Plot, `n2_des.plt` existence and 4.0V current history (do not change run). Compare old 1ns/100ns at same bias/J if data available. Coordinarily align with 이택규 to avoid duplicate or premature action.

## 2026-10-10 22:04 KST — JuSubin independently confirms 5V_TEST n2 terminal completion (OBSERVED from screenshot; old job ended 2026-10-09 14:29:52 KST)

- Worker 주수빈 re-read existing `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` via grep/tail (two screenshots repeat identical output). Last accepted BE step: `0.999674 s -> 1.000000 s`. Terminal anode voltage `5.000E+00 V`; terminal electron current `2.781E-13`, hole current `1.420E-11`, total current `1.448E-11` in Sentaurus 2D current-per-length convention (A/um, not total measured 3D A). `Sentaurus Device simulation finished (Date: Fri Oct 9 14:29:52 2026 KST)` and `Good Bye!` show successful completion.
- This closes uncertainty about **solver log reaching 5V**, but does not yet prove specific opened `n2_des.tdr` snapshot was written at the final 5V state. Document provenance/time/Plot directive if required. Independently reported raw I2D ~1.44801646e-11 A/um / nominal J~7.24e-4 A/cm2 under documented width normalization and MQW Rrad share~0.1095% remain LOW-J GATE0 blocker; successful solver convergence is not physical baseline validation.
- A separate `n1_msh.tdr: Permission denied` arose because TDR binary/data file was typed as an executable in shell; **not a TCAD job failure**. Existing MgMinus ionization-field interpretation and EBL barrier causality also unresolved. CAL project status not updated and its running job must remain untouched.
- NEXT: prioritize quantitative low-current/injection Gate0 from existing outputs, verify TDR time-bias linkage if necessary, no repeated reruns or unsolicited code edits.

## 2026-10-10 — JuSubin pGaN energy probe
- Observed Clean_pGaN X=0.05um,Y=1um: Ev=-5.130097037559eV and EFp=-4.999999973858eV. Local EFp minus Ev=0.130097063701eV. Compared with prior Clean_EBL X=0.13um local separation=0.252508468101eV; EBL minus pGaN=0.122411404400eV. Energy-gap difference is not EBL injection barrier. Next confirm actual nominal 5V endpoint, then review layer-wise band edge. No simulator edits.

## 2026-10-10 ~21:51 KST — JuSubin Clean_EBL Ev versus EFp measured at same point (OBSERVED screen, derived difference; barrier cause UNRESOLVED)

- Worker 주수빈. Completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` NtSide=0 nominal 5V, SVisual Probe coordinates X=0.13um, Y=1.0um, Z=0, Zone `Clean_EBL(AlGaN)`. New screenshot directly shows `ValenceBandEnergy=-5.252508407140e+00 eV`. Previous directly observed at identical coordinates `hQuasiFermiEnergy=-4.999999939039e+00 eV` and `hQuasiFermiPotential=+4.999999939039 V`.
- DERIVED local separation `EFp-Ev = +0.252508468101 eV` (about 9.77 kBT at 300 K), compatible with locally suppressed mobile hole density under nondegenerate `p ~ Nv exp((Ev-EFp)/kBT)`. Prior same-point hDensity=5.787900714824e15 cm^-3 while EBL Acceptor=3.0e17, Doping=-3.0e17, Donor=0.
- CRITICAL: 0.2525 eV is **local Ev-to-EFp energy separation, NOT EBL hole-injection barrier height**, and by itself does not establish excessive barrier, net hole-current limitation or explain low device J. Need compare spatial Ev and EFp plus region boundaries, transport/current density and possibly EQ state before cause conclusion. pGaN MgMinus output interpretation remains separate unresolved concern.
- NEXT READ-ONLY: use SVisual Probe on same finished TDR at verified `Clean_pGaN(GaN)` X=0.05um Y=1.0um for numerical `ValenceBandEnergy` and `hQuasiFermiEnergy`; then compare regional gaps, and align Ev/QF spatial profiles. No SWB input, TCAD run, or CAL changes.

## 2026-10-10 ~21:48 KST — JuSubin Clean_EBL hole quasi-Fermi energy point probe (OBSERVED SVisual screenshot)

- Worker 주수빈: finished `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` (NtSide=0 nominal 5V), SVisual Probe at (X=0.13 um, Y=1.0 um, Z=0) in verified `Clean_EBL(AlGaN)`: `hQuasiFermiEnergy=-4.999999939039e+00 eV` and `hQuasiFermiPotential=+4.999999939039e+00 V` shown in Probe Var Values. These are opposite-sign representations; do not equate the absolute EFp value to hole barrier height.
- Previous identical point: `AcceptorConcentration=3.000000e17 cm^-3`, `DonorConcentration=0`, `DopingConcentration=-3.000000e17 cm^-3`, `hDensity=5.787900714824e15 cm^-3`.
- NEXT read-only: in same Probe coordinate and Clean_EBL Zone, scroll Var Values to `ValenceBandEnergy` and capture numerical eV value; then calculate `hQuasiFermiEnergy-ValenceBandEnergy` only as local energetic separation (not entire interfacial injection barrier). To evaluate EBL injection obstacle compare Ev and EFp across pGaN/EBL/MQW coordinates/cutline after alignment. No code, parameter, saved solver output, or CAL job changed.

## 2026-10-10 ~21:43 KST — JuSubin hQuasiFermiEnergy C1 zoom to 0–0.4 um
- OBSERVED SVisual saved JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr, NtSide0 5V, existing vertical interior C1 Y≈1um. Right 1D hQuasiFermiEnergy(C1(n2_des)) is now zoomed to X=0–0.4um. Visually approx -5eV flat to 0.14um, rises 0.15–0.18um, multiple abrupt steps around 0.19–0.25um, ~-2.6eV after 0.25um. These are screenshot estimates, not quantitative fit or proven barrier.
- Prior 1D ValenceBandEnergy C1 shows sharp shifts near 0.12–0.26um. Coincident shifts merit same-coordinate Ev-vs-EFp quantitative comparison; barrier/depletion and low EBL hDensity cause remain UNRESOLVED. NEXT read-only SVisual Probe of ValenceBandEnergy and hQuasiFermiEnergy at existing confirmed Clean_EBL point X=0.13um,Y=1.0um, recording Zone and values, then spatial region-aware comparison. No model or CAL modifications.

## 2026-10-10 ~21:37 KST — Upper 0–0.4um ValenceBandEnergy cutline zoom observed (OBSERVED SVisual screenshot / CAUSAL INFERENCE UNRESOLVED)

- Worker **주수빈** displayed `ValenceBandEnergy(C1(n2_des))` in completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` (NtSide0 5V) using same vertical interior C1 line at Y≈1.0 um. **Right 1D plot X axis now 0–0.4 um** (confirmed visually), with resolved sharp energy structure in upper pGaN/EBL/MQW layers.
- Approximate visual band-edge features (not point-extracted): X=0–0.11um ~-5.1eV; pronounced downward feature around X≈0.12–0.15um to roughly -5.6eV; repeated abrupt peaks and dips around X≈0.17–0.26um; beyond ~0.28um ~-3.5eV plateau. Exact interfacial region mapping, magnitude of hole barrier, and peak origins are NOT verified by a color/curve screenshot; these are hypotheses for carrier barrier and band offsets, not validation of EBL injection-loss mechanism.
- Previous same SVisual Probe: `Clean_EBL(AlGaN)` X=0.13um Y=1um, Acceptor=3e17, Donor=0, Doping=-3e17, `hDensity=5.787900714824e15 cm^-3`; cannot attribute low biased mobile holes solely to an EBL barrier yet.
- NEXT read-only UI: retain reference Ev screenshot; click existing C1 dataset on right 1D Data Selection and select `hQuasiFermiEnergy` from lower field list; check legend changes and that 0–0.4um horizontal axis remains or reapply bound. Compare Ev vs hole quasi-Fermi for band-edge proximity and carrier transport. If both can be overlaid later, do so after verifying each alone. No TCAD source, model or running CAL change.

## 2026-10-10 ~21:36 KST — 5V ValenceBandEnergy C1 cutline plotted, awaiting upper-layer zoom (OBSERVED SVisual Screenshot)

- Worker: 주수빈. In saved completed NtSide=0 5V `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, created existing-type vertical C1 line at internal Y≈1 um and confirmed right 1D `Cutline_Y Plot` legend **`ValenceBandEnergy(C1(n2_des))`**. Full-depth 1D X axis spans ~0–4.5 um, while upper-stack Ev varies sharply near X<0.3 um. The broad plot is not sufficiently resolved for EBL injection barrier assignment.
- NEXT read-only UI: right 1D plot X Axis Properties: Min=0 Fixed, Max=0.4 um Fixed, Log off; keep Energy/Y axis unchanged; capture pGaN/EBL/MQW resolved band edges, and then overlay/compare `hQuasiFermiEnergy` at same C1 to evaluate hole-transport barrier hypotheses. Do not infer barrier magnitude from screenshot before clear zoom and layer boundaries. Existing observation: EBL X=0.13 um/Y=1um 5V Acceptor=3e17, Donor=0, Net=-3e17, hDensity=5.787900714824e15 cm^-3; root cause remains UNRESOLVED.
- No SWB/SDE/SDevice file changes or live CAL job actions.

## 2026-10-10 ~21:33 KST — 5V ValenceBandEnergy 2D field visible; vertical cutline pending (OBSERVED SVisual screenshot)

- Worker 주수빈 opened existing finished `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` NtSide0 5V in SVisual, selected `ValenceBandEnergy` in Scalars and activated its 2D field. Color-bar range approximately -5.66219 to +0.421554 eV. The 2D cross-section contains near-top pGaN/EBL/MQW transitions, but this picture alone does **not** measure valence-band barrier height or establish cause of EBL hole deficit.
- Prior exact Clean_EBL(AlGaN) Probe X=0.13um, Y=1um: Acceptor=3e17, Donor=0, Doping=-3e17, hDensity=5.787900714824e15 cm^-3 at 5V. Distinct pGaN Mg ionized-field semantics remain unresolved.
- Next read-only GUI: create same center-interior vertical X-direction Cutline at Y=1.0um used previously, with `ValenceBandEnergy` field selected on C1 so 1D curve appears. Then X-axis range 0–0.4um and compare `hQuasiFermiEnergy` on same cutline. Need confirm band-edge peak, local coordinates and quasi-Fermi alignment before barrier physics interpretation. No TCAD code/results/jobs changed.

## 2026-10-10 ~21:29 KST — JuSubin 5V Clean_EBL net doping and donor Probe confirmed (OBSERVED, PHYSICS CAUSE UNRESOLVED)

- Worker 주수빈 provided SVisual Probe screenshot of saved, completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, NtSide=0, 5V endpoint. Coordinates `X=0.13 um,Y=1.0 um,Z=0`; Zone `Clean_EBL(AlGaN)`.
- **New directly observed:** `DonorConcentration = 0.000000000000e+00 cm^-3`; `DopingConcentration = -3.000000000000e+17 cm^-3`. Prior screenshots **same point**: `AcceptorConcentration=3.000000000000e17 cm^-3`, `hDensity=5.787900714824e15 cm^-3`.
- EBL effective acceptor input and signed net doping agree with nominal acceptor=3e17 / donor=0. The local 5V mobile hole density is ~51.8x lower than effective acceptor doping, so this is NOT evidence that SDE EBL dopant is missing/misassigned. It may reflect a space-charge/polarization/heterojunction/bias effect; **no single mechanism or bad EBL design is proven from one local point**. Kou literature nominal hole concentration is not interchangeable with 5V local electron/hole density.
- Next **read-only** on same existing TDR: vertical cutline across pGaN/EBL/MQW (Y=1.0 um), inspect `ValenceBandEnergy` and `hQuasiFermiEnergy` plus local hole density to investigate effective hole-injection barrier. Start by checking availability of `ValenceBandEnergy` in Data Selection; no new solver jobs nor model changes. Existing MgMinus custom mapping versus effective net doping is a SEPARATE unresolved item.

## 2026-10-10 ~21:26 KST — 5V Clean_EBL AcceptorConcentration matches nominal 3e17 (OBSERVED SVisual probe)
- 작업자 주수빈: `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` 완료된 NtSide=0, 5V 결과, Probe X=0.13 um, Y=1.0 um, Z=0; Zone `Clean_EBL(AlGaN)`; `AcceptorConcentration=3.000000000000e17 cm^-3` directly observed in latest screenshot.
- Same coordinate previously observed `hDensity=5.787900714824e15 cm^-3` (~51.8 times lower), versus intended effective EBL acceptor input 3e17 and Kou paper nominal EBL hole concentration 3e17. The effective acceptor is correctly represented in TDR, but local biased free-carrier density differs. Do NOT conflate nominal dopant concentration and 5V hole density nor diagnose an injection barrier as proven from one point.
- Next read-only: same SVisual Probe field `DopingConcentration` (and `DonorConcentration`) at X=0.13 um,Y=1.0 um; verify EBL charge/dopant bookkeeping. Then spatial/0V profile and valence-band / quasi-Fermi-barrier analysis if needed. All TCAD and CAL jobs unchanged.

## 2026-10-10 ~21:22 KST — Clean_EBL hDensity probed at 5V
- OBSERVED: 주수빈 SVisual completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` (NtSide=0, 5V), Probe (X=0.13 µm, Y=1.0 µm, Z=0), Zone `Clean_EBL(AlGaN)`, `hDensity=5.787900714824e15 cm^-3` (screenshot readout). Prior 5V point `Clean_pGaN` X=0.05 µm gave hDensity≈3.00034279e17 cm^-3. EBL hole concentration is about 51.8x lower than the 3e17 cm^-3 nominal Kou EBL hole-density reference at this one 5V point.
- INTERPRETATION: 5V local EBL carrier density is not necessarily equal to nominal 0V/equilibrium density or SDE acceptor input; heterojunction/polarization/hole injection effects may dominate. This single point does not establish wrong EBL doping. Need identify nominal EBL accepted and net doping with same-position Probe before judging baseline.
- NEXT read-only: at identical Probe coordinates, scroll `Var Values` to `AcceptorConcentration`, `DopingConcentration`, `DonorConcentration` and capture magnitudes; optionally check hDensity at adjacent EBL points or equilibrium saved state later. MgMinus interpretation still unresolved. No file/source/simulation changes.

## 2026-10-10 ~21:17 KST — Same-point n1 mesh vs 5V net doping directly compared (OBSERVED SVisual screenshots; ionization-field interpretation unresolved)

- Worker 주수빈 opened `JUSUBIN_FAST_HALF_5V_TEST/n1_msh.tdr` and used SVisual Probe at X=0.05 um, Y=1.0 um, Z=0; Zone `Clean_pGaN(GaN)`.
- **Direct initial mesh Probe**: `DopingConcentration = -9.590000000000e18 cm^-3`; `NDopantActiveConcentration = 0`; `PDopantActiveConcentration = 0` (Mg is a separate pMagnesium species). Two screenshots of identical panel provided; count as one observation.
- **Existing previous finished 5V n2 Probe at same coordinates**: `DopingConcentration≈-3.000317924998e17 cm^-3`; `hDensity≈+3.000342790006e17 cm^-3`; `pMagnesiumActiveConcentration=9.59e18 cm^-3`; `pMagnesiumMinusConcentration=9.59e18 cm^-3`; `AcceptorConcentration=9.59e18 cm^-3`; `DonorConcentration=0`.
- Initial nominal net doping and final effective net doping are demonstrably distinct, and SDevice log previously confirmed `IncompleteIonization` and explicit Nnet recomputation. The ratio |Nnet(final)|/|Nnet(mesh)|≈0.0313 is **NOT independently established as the Mg ionization fraction**, because exported MgMinus still equals MgActive while net doping is much lower. Actual species charge/output semantics need validation. Single-point target match is not spatial, EBL or 0V calibration.
- No SDE/SDevice codes, numerical parameters, or CAL job modified. Suggested next step: check whether effective ionized acceptor field `AccepMinusConcentration` can be obtained or verify custom pMagnesiumMinus output behavior in same saved 5V run; preserve this as UNRESOLVED. Optionally proceed to EBL point-by-point hole-density checks once scope clarified.

## 2026-10-10 ~21:15 KST — Initial mesh stores active Mg but not MgMinus (OBSERVED SVisual SCREENSHOT)

- Worker 주수빈 opened `JUSUBIN_FAST_HALF_5V_TEST/n1_msh.tdr` in SVisual. Shown scalar dataset fields: `DopingConcentration`, `NDopantActiveConcentration`, `PDopantActiveConcentration`, `X`, `Y`, `pMagnesiumActiveConcentration`, `xMoleFraction`. **No `pMagnesiumMinusConcentration` exists in the initial mesh field list.** The active Mg plot range reaches `9.59e18 cm^-3`. Mesh elements=138194, points=65513.
- This verifies nominal Mg input was propagated to initial mesh; one cannot calculate initial-to-final evolution of `MgMinus` because n1_msh does not contain that field. Absence of MgMinus on mesh does NOT itself indicate incomplete ionization disabled or incorrect.
- More direct next read-only test: SVisual Probe `DopingConcentration` on `n1_msh.tdr` at Clean_pGaN X=0.05um,Y=1.0um, compare signed net doping with already observed final n2_des at same point (≈-3.0003179e17 cm^-3). This specifically tests numerical Nnet recalculation through SDevice; does not by itself validate MgMinus output mapping. Also compare initial pMagnesiumActive at this coordinate if useful.
- Do not change TCAD source, mesh or running separate CAL model.

## 2026-10-10 ~21:10 KST — Mg ionized species mapping directly found in datexcodes (OBSERVED screenshot; SEMANTIC INCONSISTENCY UNRESOLVED)

- Worker 주수빈 obtained read-only datexcodes species configuration: `pMagnesiumConcentration, pMagnesiumChemicalConcentration` block contains `doping = acceptor( active = pMagnesiumActiveConcentration; ionized = pMagnesiumMinusConcentration )` (displayed near lines 13022–13034). `pMagnesiumMinusConcentration` label near 13037: “pMagnesium- concentration (incomplete ionization)”. Separate `pMagnesiumActiveConcentration` field label near 13011 says substitutional Mg concentration. Screenshot does not expose the filename header, so the exact searched file path/effective runtime mapping provenance is not yet individually established.
- Earlier completed 5V NtSide0 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` Probe, Clean_pGaN X=0.05um,Y=1.0um: pMagnesiumActive=9.59e18, pMagnesiumMinus=9.59e18, AcceptorConcentration=9.59e18, DonorConcentration=0, DopingConcentration≈-3.0003179e17, hDensity≈3.0003428e17 cm^-3. These apparent mismatched magnitudes require explanation: `ionized` mapping identifies the intended field but alone cannot prove `pMagnesiumMinusConcentration` has been dynamically updated to the effective ionized-density value in exported 5V TDR. Cannot declare Mg 100% ionized, fraction 3.1%, or doping calibration confirmed.
- Next read-only check: compare same Mg Minus field in initial `n1_msh.tdr` versus final `n2_des.tdr` at identical Clean_pGaN point, if both are exposed; check whether solver's `AccepMinusConcentration` is available. If still unresolved, document blocker and separately validate EBL (candidate X≈0.135um Y=1.0um, confirm region). Do not modify baseline nor running CAL.

## 2026-10-10 ~21:09 KST — datexcodes check command shell mismatch
- OBSERVED JuSubin terminal screenshot. Assistant's prior bash `for f in ...; do ...; done` was pasted directly into login shell that responds `for: Command not found`, `do: Command not found`, `f: Undefined variable`. This is consistent with csh/tcsh and NOT a TCAD SDevice or model failure. No datexcodes contents obtained; Mg species output interpretation still UNRESOLVED.
- Assistant correction: re-run search via `bash -c 'for f in ...; do if [ -f "$f" ]; then echo "$f"; grep -n -B 12 -A 12 pMagnesiumActiveConcentration "$f"; fi; done'`. Follow up if no files/output. This is read-only and must not change existing 5V baseline or independent CAL run.

## 2026-10-10 ~21:05 KST — Node2 runtime GaN Mg ionization species parameters observed (OBSERVED SCREENSHOT / CALIBRATION UNRESOLVED)

- Worker: 주수빈. Actual read-only `sed -n '810,850p' JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` screenshot shows `Reading parameters for material "GaN"`, `Species "pMagnesiumActiveConcentration"` `type = acceptor`, runtime values `E_0=0.2eV`, `alpha=8e-9 eV*cm`, `beta=0`, `gamma=1`, `g=4`, `Xsec=1e-14 cm^2`, `Xsec_formula=1`, `highdop_formula=1`, `b_Nref=6e18 cm^-3`, `b_pow=2`, `E_Nref=2e18 cm^-3`, `E_pow=2`. This is stronger than just pp2 file reference: SDevice reports the *effective runtime-read* parameters.
- One-point 5V Clean_pGaN Probe X=0.05um Y=1.0um: `hDensity≈3.00034e17`, `DopingConcentration≈-3.00032e17`, `Acceptor=pMagnesiumActive=pMagnesiumMinus=9.59e18 cm^-3`. With `IncompleteIonization` ON and runtime `Nnet` recalculation confirmed, the equality of active and exported minus field to 9.59e18 remains a field-definition/ionization-output validation question, not proof of full ionization or successful physical calibration.
- Sentaurus training about AlGaN incomplete ionization provides doping species `datexcodes.txt` mapping of `ionized = MagnesiumMinusConcentration`; **the current custom pMagnesium mapping must be checked on the actual installed runtime before asserting exact semantics**. Next READ ONLY: inspect `datexcodes.txt` selected by project/system and check whether `AccepMinusConcentration` was requested/exported, then make same-point verification. No code or running CAL job modified.

## 2026-10-10 ~21:02 KST — Effective Node2 Mg ionization region scopes confirmed (OBSERVED)

- Worker 주수빈 supplied terminal screenshot of `sed -n '115,145p;450,465p' JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd`. Effective SDevice deck explicitly has `Physics(Region="Clean_pGaN"){ IncompleteIonization(Dopants="pMagnesiumActiveConcentration") }` and same for `Physics(Region="DmgL_pGaN")`; DmgL_pGaN `Traps((Acceptor Conc=0 ...))`. The Plot section includes `Doping`, `DonorConcentration`, `AcceptorConcentration`, `pMagnesiumActiveConcentration`, `pMagnesiumMinusConcentration`, `PE_Polarization/vector`, and `PE_Charge`.
- Therefore Mg incomplete ionization is configured for two directly displayed half-device pGaN regions, and explicit DmgL trap is switched off (Conc=0) in this NtSide=0 reference. Nothing in this excerpt establishes ionization physics for EBL/MQW or confirms any DmgR region exists in this half mesh.
- The empirical SVisual Clean_pGaN X=0.05,Y=1.0um hDensity≈3.00034e17 and Doping≈−3.00032e17 with MgActive=MgMinus=Acceptor≈9.59e18 still require ionized-output semantics reconciliation. Official SDevice guide says Plot `AccepMinusConcentration` shows ionized acceptor concentration, and custom species are defined by `datexcodes.txt`; exported `pMagnesiumMinusConcentration` alone is not proof of correct ionization fraction.
- NEXT read-only: inspect runtime n2_des.log around species block (lines 810–850) and local/system `datexcodes.txt` if needed; then seek actual `AccepMinusConcentration` field if present. No input/source/solver/CAL changes.

## 2026-10-10 — Node2 Mg parameter binding confirmed
- OBSERVED by 주수빈: active `JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd` line 22 has `Parameters = "FASTC1_pp6_des.par"`; line 68 DefaultParametersFromFile; lines 128 and 137 call Mg IncompleteIonization; 456/458 request Mg active/minus fields.
- Existing linked FASTC1_pp6_des.par has GaN Mg Species Ionization E_0=0.2, alpha=8e-9, g=4.0, Xsec=1e-14. n2 log recognized Mg incomplete ionization and recalculated net doping. Exact MgMinus versus net-doping semantics remain unresolved; next inspect pp2 region scope and actual species output meaning. No simulation changes.

## 2026-10-10 ~20:40 KST — 5V_TEST region scope and Nnet recalculation log context (OBSERVED)

- 주수빈 terminal screenshot of read-only `sed -n '410,445p;2138,2160p' JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` confirms region **DmgL_pGaN** `With incomplete ionization` selected `pMagnesiumActiveConcentration`; subsequent **DmgL_EBL** lists no incomplete-ionization. Previously inspected live pp2 Physics confirms `Clean_pGaN` also has region-specific incomplete ionization.
- Log explicitly identifies three recognized species used in acceptor/donor concentrations: `NDopantActiveConcentration (donor)`, `PDopantActiveConcentration (acceptor)`, `pMagnesiumActiveConcentration (acceptor)`. `DopingConcentration` and `TotalConcentration` are recomputed, and `WARNING: Doping concentration (Nnet) will be recalculated because of incomplete ionization!` is printed. Thus this warning is not itself a fatal error.
- The `With Bulk Traps` declaration lists acceptor trap Ev+0.75eV and electron/hole cross-sections 1e-15cm2; it **does not prove trap concentration >0**. Earlier preprocessed NtSide=0 deck independently verified all 12 sidewall traps `Conc=0`.
- IMPORTANT UNRESOLVED: Clean_pGaN 5V Probe X=0.05,Y=1um: hDensity≈3.00034e17 and signed Doping≈−3.00032e17 vs MgActive=MgMinus=Acceptor≈9.59e18. Region activation and Nnet recalculation are observed but not an independent proof of correctly calibrated ionization fraction or semantics of exported MgMinus. Sentaurus device guide uses `AccepMinusConcentration` to visualize ionized acceptor density; verify whether output is available and investigate custom `datexcodes.txt` mapping/Plot before interpretation. No new TCAD run or code edit.
- NEXT READ-ONLY: inspect effective GaN Ionization Species block in existing `FASTC1_pp6_des.par` and relevant `pp2_des.cmd` Plot fields, then reconcile field semantics; do not alter running CAL or finished baseline.

## 2026-10-10 ~20:38 KST — 5V_TEST n2 log confirms Mg incomplete-ionization and Nnet recalc (OBSERVED)

- Worker 주수빈 provided live read-only terminal output: `grep -niE 'incomplete ionization|recalculat|pMagnesium' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/n2_des.log | head -n 60`.
- Observed: line 335 `Without incomplete ionization` for a distinct/global scope; line 422 `With incomplete ionization`, line 423 `Selected dopants: pMagnesiumActiveConcentration`; line 431/432 repeat; line 821 species `pMagnesiumActiveConcentration`; line 2143 `pMagnesiumActiveConcentration (acceptor)`; line 2148 `WARNING: Doping concentration (Nnet) will be recalculated because of incomplete ionization!`.
- This confirms runtime recognized region-specific Mg incomplete-ionization and Nnet recalculation. It DOES NOT prove ionization coefficient/curve correctly calibrated or resolve why SVisual `pMagnesiumMinusConcentration=pMagnesiumActiveConcentration=9.59e18` while `DopingConcentration=-3.0003179e17` and `hDensity=3.00034279e17 cm^-3` at Clean_pGaN X=0.05um,Y=1um. These are different output quantities; no inference of Mg 100% ionization or a fraction from hDensity/nominal doping without direct verification.
- NEXT read-only: inspect log surrounding line 410–440 (Physics scopes) and 2138–2160 (species/ionization and warning context), then inspect active GaN ionization parameter section as needed; avoid source edits or disrupting separate CAL job.

## 2026-10-10 ~20:35 KST — JuSubin pGaN AcceptorConcentration 9.59e18 independently probed (OBSERVED 5V TCAD output; interpretation unresolved)

- Worker 주수빈 supplied screenshot of completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, NtSide=0, SVisual Probe at (X=0.05, Y=1.0, Z=0) um, Zone `Clean_pGaN(GaN)`. This screenshot explicitly confirms `AcceptorConcentration=9.590000000000e18 cm^-3`.
- Prior screenshots at identical point: `pMagnesiumActiveConcentration=9.59e18`, `pMagnesiumMinusConcentration=9.59e18`, `DonorConcentration=0`, `DopingConcentration≈-3.0003179e17`, `hDensity≈3.000342790006e17 cm^-3`. Kou-inspired free-hole target 3e17 is numerically attained at this one 5V sample location, but effective Mg ionization species interpretation and ionized-doping charge balance remain UNRESOLVED.
- If exported Mg Minus truly represents ionized acceptor for the same state, its equality to total 9.59e18 alongside low signed net doping cannot be explained simply from donor=0. Need inspect exact T-2022.03 field semantics, effective custom parameter/species configuration and n2 runtime ionization/recalculated doping logs; don't declare physical calibration pass/failure based only on variable names.
- Next read-only: inspect pp2_des.cmd region-scoped `IncompleteIonization`, actual `FASTC1_pp6_des.par` ionization block and `n2_des.log` run-time activation; examine `datexcodes` species field mapping if necessary. Keep completed original and ongoing CAL simulation untouched; no code change or rerun.

## 2026-10-10 ~20:31 KST — Clean_pGaN donor and net doping measured at same probe point (OBSERVED)

- 주수빈 SVisual completed 5V NtSide0 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, Probe X=0.05 um, Y=1.0 um, Z=0, Zone `Clean_pGaN(GaN)`.
- New screenshot direct Probe readout: `DonorConcentration=0 cm^-3`; `DopingConcentration=-3.000317924998e17 cm^-3` (screenshot readout approximated from displayed digits). Previous same-point `hDensity=3.000342790006e17 cm^-3`, `pMagnesiumActiveConcentration=pMagnesiumMinusConcentration=9.59e18 cm^-3`.
- Net doping magnitude and hDensity agree closely at THIS single 5V point; consistent with approximately charge-neutral p-type local result, but other charge terms and ionization species mapping have not been fully evaluated. Strong warning: identical MgActive/MgMinus exported values are not reconciled with net doping ≈-3e17; do not infer a Mg ionization fraction or claim physically calibrated doping from the probe alone.
- Next read-only: in same Probe Zone inspect `AcceptorConcentration` (and optionally `eDensity`) then audit actual Sentaurus T-2022.03 species output semantics and Mg incomplete ionization, followed by 0V and EBL carrier profile checks. No input source/run changed.

## 2026-10-10 20:21 KST — p-GaN Mg Active and Mg Minus same values, physically unresolved (OBSERVED)

- Worker: 주수빈. Completed 5V NtSide0 SVisual Probe from `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, coordinate X=0.05 um/Y=1.0 um/Z=0, Zone `Clean_pGaN(GaN)`.
- **New observed:** `pMagnesiumActiveConcentration = 9.590000000000e18 cm^-3`; `pMagnesiumMinusConcentration = 9.590000000000e18 cm^-3`. Previous same-point `hDensity=3.000342790006e17 cm^-3` (5V transient).
- Literature/source semantics: in Sentaurus Device the dopant species ionized field for acceptor is typically `MinusConcentration`. Therefore equality of Active and Minus does **not** demonstrate incomplete Mg ionization despite hDensity matching a target. Exact T-2022.03 custom species mapping/plot output and net doping charge, compensation or possible plot bookkeeping must be audited before physical explanation. It is incorrect to infer ionization fraction as hDensity/MgActive.
- Next read-only GUI: at same 5V coordinate Probe `DopingConcentration`, `AcceptorConcentration`, `DonorConcentration` and if available `eDensity` to check consistency; later audit actual `datexcodes.txt` pMagnesium species mapping, effective GaN Ionization and SDevice region model & Plot. Not evidence the full p-GaN doping calibration is validated.
- No source changes, rerun or CAL interruption.

## 2026-10-10 ~20:10 KST — JuSubin clean p-GaN hDensity target confirmed at one 5V point (OBSERVED)

- Worker **주수빈** supplied Sentaurus Visual **Probe** screenshot of completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, NtSide=0, nominal 5V transient endpoint.
- **Direct readout**: Probe coordinates `X=0.05 um, Y=1.0 um, Z=0`; Zone `Clean_pGaN(GaN)`; `hDensity = 3.000342790006e+17 cm^-3`.
- This matches the nominal Kou-based p-GaN hole-density target 3e17 cm^-3 **at one observed interior location**, not proof of global/equilibrium/0V carrier profile, actual chemical Mg density, effective ionized acceptor fraction, or full physical calibration. Historical SDE Mg input `N_Mg_p=9.59e18 cm^-3` is a *different quantity*.
- **Next view-only**: keep same Probe coordinates and read `pMagnesiumActiveConcentration`, `pMagnesiumMinusConcentration` magnitudes, and optionally `DopingConcentration` to separate nominal Mg input, exported Mg− field, and free holes. Inspect EBL/near-QW hole density and polarization spikes only after confirming Zone of each sample. No SDE/SDevice edits; existing CAL run remains untouched.

## 2026-10-10 ~20:09 KST — Probe pGaN position attempted, value not yet visible

- 주수빈이 finished `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` NtSide0 5V SVisual에서 Probe At X=0.05 um, Y=1.0 um, Z=0 수행 후 화면을 보냄. 주황색 상단 영역에 표식은 보이나 Probe result/Zone/Magnitude 패널이 스크린샷에는 없어 실제 hDensity 측정값이나 Clean_pGaN Zone은 아직 직접 확인되지 않음.
- 다음 확인: Tools > Probe로 아래 Probe panel 다시 표시하고 X/Y/Z 및 Zone=Clean_pGaN(GaN), Var Values > hDensity magnitude를 함께 캡처. 데이터가 보이기 전 도핑 calibration 성공/실패 판정 금지.
- No source, simulation, or running CAL changes.

## 2026-10-10 — JuSubin SVisual Probe At dialog opened
- OBSERVED: In finished 5V NtSide0 SVisual, Probe panel plus Probe At dialog opened. Current X=0.5 um, Y=1.0 um, Z=0; Zone=Clean_nGaN(GaN).
- NEXT: set X=0.05 um for candidate Clean_pGaN, press Probe; verify Zone and hDensity before interpreting. No code changes.

## 2026-10-10 ~19:58 KST — hDensity upper-stack peaks spatially resolved in cutline (OBSERVED / PHYSICAL INTERPRETATION PENDING)

- Worker 주수빈, completed 5V NtSide0 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`: SVisual interior Cutline C1 at lateral Y≈1µm; `hDensity` plotted with linear X axis restricted 0–0.4µm.
- Two sharp high `hDensity` peaks visually at growth-axis X≈0.12µm (above ~4e19cm^-3) and X≈0.245µm (about 5e19cm^-3). A smaller feature near X≈0.22µm. Region attribution and precise numeric magnitude cannot be established from screenshot. pGaN interior `hDensity` ~3e17cm^-3 cannot be resolved accurately due to linear vertical scale at ~5e19.
- Do NOT declare incorrect doping, physical hole accumulation or source of QW recombination loss from the spikes. Model/Scharfetter/lattice polarization, junction/interface and numerical overconcentration remain hypotheses. This is a simulated 5V transient endpoint, not 0V equilibrium carrier density.
- NEXT read-only: SVisual Probe on 2D `n2_des` at representative `Clean_pGaN` coordinate X≈0.05µm,Y≈1.0µm,z=0, record Zone, `hDensity`, MgActive/MgMinus and units; then probe peaks/EBL/QW points by region and check results. Keep running CAL and baseline files untouched.

## 2026-10-10 ~19:56 KST — hDensity C1 Cutline first displayed (OBSERVED GUI / NOT PHYSICS-VALIDATED)

- 작업자 주수빈이 완료된 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` (NtSide0, 5V transient)에서 기존 Clean 영역 vertical `C1(n2_des)` cutline의 variable을 `DopingConcentration`에서 **`hDensity`**로 변경했고, 우측 legend `hDensity(C1(n2_des))`가 직접 확인됨.
- 오른쪽 graph X축은 변경 후 전체 약 0–4.5 µm로 돌아왔으며 Y축 선형에서는 상단 계면/QW 근처로 보이는 X≈0.1–0.25 µm에서 좁고 큰 hole-density spikes가 보임. Y축 4e19 cm^-3 tick 위로 올라가는 peak가 존재하나 **정확한 최대값/영역/물리적 원인은 미확인**. 넓은 n-GaN에서 정공이 작게 보이는 것은 이 선형축 스케일에서의 시각적 인상이며 0이라고 단정할 수 없음.
- Kou의 nominal p-GaN free-hole 3e17 cm^-3 대비 p-GaN 내부 실제 hDensity는 이 화면만으로 정량 비교 불가. 급격한 spike를 Mg 고농도·물리 불량·QW accumulation으로 확정하지 말 것. 5V transient endpoint는 0V equilibrium calibration과 다름.
- NEXT view-only: 오른쪽 1D plot X-axis Axis Properties에서 fixed Min=0 Max=0.4 µm로 확대; 필요하면 hDensity 양수 로그 Y축/정확한 Probe로 p-GaN interior vs EBL/MQW 각 region 분리, Rhs/field check. 그래프 변경은 visualization only; SDE/SDevice/별도 running CAL 수정 없음.

## 2026-10-10 19:46 KST — SVisual cutline upper-layer net doping inspected

- JuSubin 5V NtSide0 `JUSUBIN_FAST_HALF_5V_TEST` screenshot: `DopingConcentration` cutline X 0–0.4 um. Approx net profile upper p-side -3e17 cm^-3 until X ~0.10 um, approaches zero ~0.12 um, near-zero area over ~0.12–0.26 um, +5e18 cm^-3 from ~0.27 um into n-GaN. These are screen estimates; actual individual regions/point values unverified.
- Cutline now displays normally after earlier fixed axis problem. Net doping is not raw Mg dose or mobile hole density; apparent transition is not proof of physical Mg diffusion.
- Next inspect `hDensity` on same C1 cutline, then active Mg species if available. No TCAD code/run changed.

## 2026-10-10 ~19:43 KST — SVisual Cutline signed net-doping graph successfully restored (OBSERVED screenshot)

- 작업자 주수빈. 완료된 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` (NtSide=0, 5 V) `DopingConcentration` `Cutline_Y Plot`에서 Y-axis 수동 범위 설정 후 음·양 signed net-doping plot 전체가 다시 표시되는 것을 직접 확인.
- Current screenshot: p-side upper region roughly −3e17 cm^-3; shallow stacked EBL/MQW region shows multiple transitions; long n-GaN body has near-constant +5e18 cm^-3. Values are approximate visual readings, not separately extracted exact layer-point quantities. Underlying constant-profile SDE model is consistent; do not extrapolate to measured SIMS/MOCVD dopant grading or claim free holes equal net doping.
- **GUI issue resolved**: previous `Axis Properties` Y-Min/Max both Fixed at approx 1e-20 erroneously clipped curve; manually entered sensible linear signed Y-range (~−4e17 to +6e18), now displays step-like complete-depth plot. Only view settings changed, no TCAD code/data nor live CAL job affected.
- Next: on the **right 1D graph X axis** double-click axis tick, Axis Properties Main set fixed Min=0 and Max=0.4 μm (Log Scale off), keep fixed linear Y bounds unchanged, share zoomed plot for pGaN/EBL/MQW doping interpretation; later compare `hDensity`, pMg species in identical cutline.

## 2026-10-10 ~19:40 KST — SVisual 1D doping Y-axis not yet restored after auto-range advice (OBSERVED screenshot)

- 주수빈이 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` 5V NtSide0 `Cutline_Y Plot`의 후속 screenshot을 제공. 왼쪽 2D full geometry와 Cut Y C1은 보이지만, 오른쪽 1D Y axis는 여전히 약 `9.995e-21`–`1.0005e-20`이며 실제 doping magnitude를 나타내지 못함.
- 이전 화면에서 Axis Properties Min/Max Fixed가 잘못 설정된 것이 확인됨. 사용자가 체크 해제를 수행했는지 그 이후 축 자동 설정이 반영되었는지는 이 화면만으로 불확실. 후속 조치로 `Axis Properties > Main`에서 Y1 `Min=-4e17`, `Max=6e18`를 입력하고 각각 Fixed 체크(선형 Log Scale 해제 유지)하여 표시 범위를 수동 제어하는 방법을 제안함. 이는 VIEW ONLY, 실제 5V 시뮬레이션 입력/데이터의 변경 아님.
- 실제 numeric axis restoration 미검증; 후속 화면 확인 필요. 그래도 실패 시 선택 축이 Y1인지, cutline 1D 실제 원자료가 있는지 확인하고 필요하면 Clean 영역 full-height cutline 재생성. 임의 재실행/소스 수정 금지.

## 2026-10-10 ~19:37 KST — SVisual Y-axis fixed-range root cause confirmed (OBSERVED GUI; remedy not yet tested)

- 작업자: 주수빈. 완료된 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`에서 `DopingConcentration` / `Cutline_Y Plot` 표시 이상을 조사.
- 제공된 T-2022.03 SVisual `Axis Properties > Main` 직접 캡처에서 **Y축 Min = 9.9927e-21, Max = 1.00073e-20** 및 양쪽 **Fixed 체크**를 확인. `Log. Scale`은 해제되어 있음.
- 확정된 GUI 원인: 잘못 저장된 극히 좁은 Y축 고정 범위가 10^17~10^18 cm^-3 수준 signed DopingConcentration 데이터를 가림. 이는 원래의 도핑 입력이나 TCAD 계산에 대한 오류 증거가 아님. 과거 'log axis 때문에 보이지 않는다' 해석은 이 최신 화면에 대해서는 정정됨.
- 제안한 복구(아직 실행결과 미확인): `Axis Properties`의 Min/Max 양쪽 `Fixed` 해제, `Log. Scale` 해제 유지, 1D cutline 자동 축으로 복원되는지 확인 후 QW/EBL 인접 깊이 구간 분석.
- 소스·파라미터·결과 파일·실행 중인 별도 CAL job 수정 없음. 후속 스크린샷으로 표시 복구 검증 필요.

## 2026-10-10 ~19:16 KST — SVisual cutline Y-axis zoom-range issue clarified (OBSERVED UI)

- 주수빈 screenshot: original 5V result `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, Cutline_Y Plot has Y ticks `9.995e-21`, `1e-20`, `1.0005e-20`; these are closely spaced **linear** numbers, not evidence of log scale. Prior assistant repeatedly identifying `1e-20` by itself as a logarithmic axis was incorrect.
- The rendered curve is compressed/clipped near the far-left X edge, because the Y plot range is extremely narrow around ~1e-20, missing physical signed DopingConcentration ~-3e17 to +5e18. Existing full vertical C1 cutline continues to be displayed on 2D view. Do NOT infer absent data or failed simulation from this plot.
- Read-only GUI next step: activate **right** Cutline_Y Plot first, then reset that plot's view/zoom (suggested Ctrl+Shift+F already used for 2D view) to restore full signed Y-axis; if unsuccessful check Axis Properties auto/fixed min/max. Keep Log Y off. No source/results/ongoing CAL job edited.

## 2026-10-10 ~19:15 KST — SVisual full device restored; cutline plot Y log reenabled (OBSERVED screenshot)

- 작업자 주수빈. 기존 완료된 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`에서 화면 복구 후 2D 소자 X 약 0–4.5 µm 전체 구조와 중앙 내측의 세로 Cut Y `C1`이 다시 표시됨. 138194 elements, 65513 points.
- 1D `Cutline_Y Plot`에서는 Y축 눈금 `1e-20` 및 오른쪽 `log Y` 토글이 보이며, signed `DopingConcentration`의 음수 값을 표현하지 못하는 로그 스케일이 재활성화된 것으로 해석. 이전 스크린샷의 짧은 붉은 선분 문제를 도핑 프로파일 자체가 손상된 것으로 해석하면 안 됨.
- 다음 읽기 전용 UI 단계: 오른쪽 1D 그래프 활성화 후 `log Y` 해제, 선형 Y축에서 음·양의 DopingConcentration 전체 깊이 프로파일을 확인. 이후 상단 p-GaN/EBL/MQW 구간 확대 및 `hDensity`/Mg species 분리 비교. TCAD 입력, 저장 결과, CAL 실행은 변경하지 않음.

## 2026-10-10 ~19:13 KST — SVisual Cutline 재생성 후 1D 데이터 표시 축소 (OBSERVED GUI / CAUSE UNRESOLVED)

- 주수빈은 기존 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`를 SVisual에서 다시 열고, 새 Cut Y를 만들고 로그 Y를 해제했다고 보고. 스크린샷에서 왼쪽 2D 소자는 상단 X≈0~1.2µm만 확대된 뷰이며, 오른쪽 `Cutline_Y Plot`에는 x≈0.15µm 근처 짧은 음수 DopingConcentration 선분만 표시됨. 소스/데이터 수정 또는 solver failure 증거 없음.
- 가능한 UI 해석: cutline 추출이 2D 현재 보이는 영역으로 제한되었거나 XY 축 표시가 직전 확대 상태를 유지. 원인 확정 전 `DopingConcentration` 전체 구간 데이터가 사라졌다고 판단하지 않음.
- 공식 Sentaurus Visual User Guide는 cutline output이 현재 표시된 2D 영역에 국한될 수 있으며 Reset Zoom으로 전체 데이터 접근 가능하다고 명시. 우선 왼쪽 2D plot 선택 후 View > Reset (Ctrl+Shift+F)으로 full device 표시를 복구하고, 필요시 기존 cutline 제거 후 full 2D 상태에서 Cut Y 재작성·1D linear Y 확인하도록 안내.
- 수행된 것은 GUI 보기 조작뿐; CAL 실행과 저장된 5V 데이터를 변경하지 않음. NEXT: 리셋된 화면 확인 후 단계별 재추출.

## 2026-10-10 ~18:33 KST — 주수빈 5V Baseline signed DopingConcentration vertical cutline linear-axis verified (OBSERVED UI)

- 주수빈 provided Sentaurus Visual screenshot of completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, NtSide=0, after toggling Cutline_Y Plot from logarithmic to linear Y-axis. Existing vertical (growth-axis X) cutline at lateral Y≈1.0 μm passes clean semiconductor away from physical damaged sidewall.
- Direct plotted `DopingConcentration` shows roughly −3×10^17 cm^-3 upper p-side, multiple narrow variations around EBL/MQW, and roughly +5×10^18 cm^-3 constant plateau in n-GaN. The graph shows a step-like nominal signed net-doping distribution along this cutline. Numerical transition boundary and dopant activation details are NOT precisely extracted at this zoom.
- This is not a direct measurement of raw Mg input 9.59×10^18 cm^-3, `hDensity`, ionized Mg fraction, Mg diffusion, or actual physical SIMS depth profile. The loaded 5V output remains a Transient endpoint, not independently proven equilibrium or steady-state.
- Next read-only GUI validation: zoom cutline X≈0–0.4 μm to distinguish p-GaN/EBL/MQW region steps, then show `hDensity` and optionally `pMagnesiumActiveConcentration` and `pMagnesiumMinusConcentration` where available. Preserve original saved results and ongoing separate CAL n2 job; no source changes.

## 2026-10-10 ~18:27 KST — SVisual 5V NtSide0 vertical doping cutline created (OBSERVED UI / interpretation pending)

- 작업자 주수빈은 완료된 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` (5V, NtSide=0)에서 `DopingConcentration`을 표시하고 `Cutline_Y Plot` 생성에 성공함. 사용자 SVisual screenshot: 138194 elements / 65513 points, x vertical 0 to ~4.5 um; cutline은 현재 Clean 영역 좌측 가까이 Y≈0.8 um 위치이며 영역 중앙 Y≈1.5 um에서 추후 재측정 권장.
- 오른쪽 cutline 차트 y축에 1e+15, 1e+09, 1e+03, 1e-3 등이 보이는 일반 logarithmic scale이 적용됨. signed DopingConcentration의 **음수 p형 측은 이 축에서 정상 시각화되지 않으므로** 현재 선 그래프만으로 층별 p/n 도핑 분포를 해석하면 안 됨.
- NEXT GUI: right cutline plot 선택 → 오른쪽 `log Y` 토글 해제해 선형 y축 확인 → 필요시 clean semiconductor 중앙 Y≈1.5 um cutline 다시 생성/이동 → 그래프 캡처하고 pGaN/EBL/nGaN 입력 도핑과 실제 hDensity/ionized Mg 분리 분석.
- 실제 코드, 파라미터, 시뮬레이션 실행상태 변경 없음. CAL 별도 실행 보존.

## 2026-10-10 — Kou 2019 nominal epitaxy doping vs CMP step-constant profiles reviewed (REVIEWED / NO SOLVER CHANGE)

- 작업자: 주수빈. 사용자가 layer별 동일 도핑을 구현한 실제 CMP 모델의 문헌 타당성을 재질문. 실제 Kou et al., *Optics Express* 27 A643-A653 (2019) Section 2, DOI 10.1364/OE.27.00A643 확인.
- **Direct paper:** n-GaN 4 μm Si doped 5e18 cm^-3; p-Al0.15Ga0.85N EBL 26nm and p-GaN cap 120nm each **hole concentration** 3e17 cm^-3 (Mg dopant concentration이라고 보고하지 않음); 20nm heavily doped p-GaN ohmic contact layer **also specified**. Paper does not specify SIMS-calibrated vertical concentration profile or graded Mg transition function. Therefore uniform-per-layer SDE doping is a defensible simplifying *interpretation*, NOT proved literal reproduction of growth profiles or proof authors applied exact constant doping commands.
- **Existing CMP actual 2026-10-09 pp1 audit:** N_Mg_p=9.59e18 cm^-3 nominal Mg input in Clean/DmgL pGaN with incomplete-ionization SDevice physics; nominal p-GaN 3e17 target is hole density, not identical to Mg input. A single SVisual sample hDensity~3.001e17 was reported at one 5V result point and cannot establish unbiased whole-depth calibration. EBL nominal effective acceptor 3e17, n-GaN donors 5e18, barrier 1e15 (numerical assumption). Region-based constant input does not imply constant mobile electron/hole density under bias.
- **Paper/model gap:** a separate 20nm highly doped p-GaN contact cap occurs in Kou; CMP COMMON_BASELINE vertical stack does not list that separate p+ region, though exact live SDE current geometry/contact doping must be checked before treating it as confirmed omission.
- **Experimental context:** Gutt et al. PSS C (2011), DOI 10.1002/pssc.201001039 and Bakhtiary-Noodeh et al., Journal of Crystal Growth 602 (2023) 126962 DOI 10.1016/j.jcrysgro.2022.126962 support real Mg memory/back-diffusion/graded near-boundary profiles; no direct SIMS profile for the CMP representative device has been supplied. Avoid inventing gradient depth/concentrations.
- **Decision PROPOSED, NOT RUN:** retain current original and CAL running job unchanged; perform read-only vertical SVisual cutline of nominal Mg species, ionized Mg/net doping, hDensity and EBL; verify p+ contact layer/source. If experiment needed, create separately versioned sensitivity branch with literature/SIMS-backed graded Mg interface and same mesh/physics, compare QW hole injection, I(V), SRH/Rrad/current at matched injection. No code, parameter, or SWB job modified.

## 2026-10-10 ~18:08 KST — CAL SDevice Newton cutback 확인 (OBSERVED LOG SCREENSHOT)

- 작업자 주수빈이 이택규가 기존 실행한 `CMP_BASELINE_1.2.0_CAL` NtSide=0의 터미널 `tail -n 40 n2_des.log`를 제공함. 새 실행/입력 수정 없음.
- 계산이 4.138V 부근에서 진행 중. 로그에서 해당 BE 시도 15 Newton iterations 이후 마지막 `|Rhs|=1.21e-03` (RHSMin=1e-03 초과), `#iterations larger than 15`, `Newton didn't converge, trying again with smaller timestep...` 확인. 실패한 attempt wallclock 약 51.13초.
- 다음 attempt는 `Computing BE-step from 0.827672 s to 0.827674 s (Stepsize: 2.8452e-06 s)`. 기존 0–5V 선형 ramp를 가정하면 0.827672×5≈4.13836V. 이 시도는 화면 마지막 부분에서 시작만 확인되며 accepted 여부는 미확인.
- 이는 전체 job fatal 종료가 아니라 adaptive timestep cutback의 직접 증거. 고전압 수렴성/런타임 병목 현상 관찰, 남은 벽시계 시간 추정 불가. NtSide=0 CAL 5V 완료와 effective 100ns 모델 확인은 여전히 미완료.
- NEXT: job·input 그대로 보존; 일정 시간 뒤 최신 `n2_des.log`의 accepted t/V 및 cutback 빈도와 mtime, 필요시 프로세스 생존을 read-only 재검증. 절대 이 로그만 보고 solver 또는 MinStep 임의 변경하지 않음.

## 2026-10-10 ~18:07 KST — 주수빈 CAL 실행 상태 인수인계 화면 확인 (OBSERVED SCREENSHOT)

- 작업자 주수빈이 `CMP_BASELINE_1.2.0_CAL` SWB SDevice node n2 Output 스크린샷 제공. 이 계산은 기존 이택규가 실행한 별도 NtSide=0 CAL 후보이며, 주수빈이 새로 실행한 작업은 아님.
- 실제 `n2_des.out` 화면 직전 BE iteration에서 `Finished, because |RHS| less than 1.0000E-03` 후 contact anode `voltage=4.138E+00` 출력. 다음 시도 `Computing BE-step from 0.82766 s to 0.827663 s (Stepsize: 3.2930e-06 s)`가 이어짐. 다음 시도의 최종 수렴은 화면에 없음.
- 기존 0–5 V ramp가 그대로라는 조건에서 약 4.138 V/5 V = 82.76%의 **전압 스윕** 도달(이전 4.122 V 로그 대비 약 0.016 V 추가 진전). Runtime/남은 시간 비율 아님.
- 아래 `n2_des.err`의 vanOverstraetendeMan impact ionization isotropic/anisotropic E0 mismatch 메시지는 출력되어 있으나 이것만으로 fatal/중단 여부 확인 불가. 사진에서 5 V 완료, 실제 100 ns InGaN SRH 효과, 고전압 steady-state 검증 없음.
- NEXT: 소스 변경/중단 없이 나중에 `tail -n 40 .../CMP_BASELINE_1.2.0_CAL/n2_des.log`와 날짜·progress를 읽기 전용 확인; 5 V 정상 종료 시 비교용 I(V)와 QW 재결합 검토.

## 2026-10-08 — Baseline uniform-layer doping physical validity review (PROPOSED VALIDATION)

- 작업자: 주수빈; 사용자 제기: SVisual n1_msh screenshot에서 각 에피층의 DopingConcentration이 균일/step-like로 나타나 실제 MOCVD 성장 도핑 분포와 차이가 있는지 검증 필요.
- OBSERVED: half+coarse mesh 화면 138,194 elements / 65,513 points, signed DopingConcentration color scale 약 -9.59e18~+5.00e18 cm^-3. 이미지 하나만으로 각 material/region의 정확한 입력 donor/acceptor concentration 및 depth profile을 확정할 수 없음.
- REVIEW: piecewise constant intentional doping is a defensible idealized first-order epitaxial TCAD baseline; it is NOT a process-calibrated SIMS-like doping profile. Mg-doped p-GaN/EBL can exhibit memory/back-diffusion/transition profiles (see Bakhtiary-Noodeh et al., Journal of Crystal Growth 602 (2023) 126962, DOI 10.1016/j.jcrysgro.2022.126962; Gutt et al., Phys. Status Solidi C 8 (2011), DOI 10.1002/pssc.201001039).
- UNRESOLVED: active local pp1_dvs.cmd / actual SDE doping placements and composition, region-level active dopants, p-Mg ionization/compensation, and depth cutline have not yet been directly audited in this chat. SVisual screenshot is not evidence of physical doping validation.
- NEXT: read-only grep for sdedr:define-constant-profile/placement and analytic/erf doping directives in active SDE, compare NDonorActive/PDonorActive/MgActive with net DopingConcentration on depth cutline; verify baseline model assumptions/literature; then separate zero-change-reference sensitivity pilot only for plausible Mg transition at p-GaN/EBL/MQW boundaries. Do not change frozen Common Baseline or launch A/B DOE before pilot passes.

## 2026-10-08 — 주수빈 QS 0→0.3 V 성능 시험 SDevice 작성

- 작업자: 주수빈; 상태: PROPOSED / STATIC PASS / SENTARUS NOT RUN.
- 목적: Half+coarse (138,194 elements / 65,513 points)에서도 0→0.3V Transient smoke의 단일 accepted step이 약 109.74s 걸리는 bottleneck 완화. 그중 linear solve 약 90.20s, assembly 18.46s.
- 사용자의 실제 FAST_C1 pp6_des.cmd에서 생성한 SWB Smoke SDevice를 기준으로, File/Electrode/Physics/Plot/Math 전체를 byte-identical 유지하고 Solve sweep만 QS로 변환함.
- 신규 user-delivered private artifact: `sdevice_des_JUSUBIN_HALF_COARSE_QS_SMOKE.cmd` (GitHub 공개 full deck 미업로드), SHA256 `a7281c79e7e440c6192726f4ce6edefb58f8d76ed30ec921900fee5ff5a5ec01`.
- Quasistationary anode 0→0.3 V: InitialStep=0.03, MinStep=1e-6, MaxStep=0.15, Increment=1.5, Decrement=2.0; virtual t 0→1.
- Initial Poisson 500 + coupled 100 유지, within QS Coupled Iterations=15, RHSMin=1e-3, ExtendedPrecision(80), NumberOfThreads=4, Blocked/ILS(set=22) 및 trap physics 불변.
- DmgL Physics 12개, DmgR 0개, `@NtSide@` 12개, `Grid=@tdr@`, parameter file `FASTC1_pp6_des.par` 유지.
- Static audit PASS: braces/parentheses balanced; non-Solve active input completely identical to previous smoke deck; QS syntax based on Sentaurus training example. Actual T-2022.03 preprocess/numerical solve not yet tested.
- Next: preserve current old transient logs and stop only new half+coarse Node2 smoke if user elects replacement; swap SDevice source in JUSUBIN_FAST_HALF_SWB only; preprocess -> verify pp2_des.cmd QS -> run quick 0.3V QS smoke. Compare accepted wallclock, volt/current, convergence; no full 5 V until verified.

## 2026-10-08 — 주수빈 가속 Baseline 전략 수정: Half + selective mesh coarsening

- **작업자:** 주수빈
- **상태:** DECISION / SUPERSEDES PURE-HALF-ONLY PLAN
- 목표를 순수 half-domain 효과 분리 실험이 아니라 **오늘 안에 최대한 빠르게 돌아가는 실용 accelerated Baseline 구축**으로 재정의.
- 주수빈 branch도 독립적으로 **half-domain + selective mesh coarsening**을 동시에 적용.
- centerline mirror half-domain, physical sidewall 1개 및 5 nm damaged region 유지, centerline에는 damage/trap/passivation 없음.
- MQW, EBL, QW/barrier interfaces, 5 nm damage, depletion/high-field/contact-edge는 fine mesh 유지.
- homogeneous remote n-GaN bulk와 numerical n-GaN base를 우선 coarsen.
- 첫 후보: remote homogeneous n-GaN bulk 기존 spacing 대비 약 1.5~2x, numerical n-GaN base 약 2x. graded transition으로 급격한 mesh-size jump 방지.
- physics/traps/materials/contacts/RHSMin=1e-3/Iterations=15 유지.
- full reference 290,814 elements / 137,831 points 대비 mesh 감소와 runtime 측정.
- short smoke equivalence 통과 후 C2 Increment=1.05 + true Save checkpoint 전략 결합.
- publication/final adoption 전 full-vs-accelerated I/Vf/IQE/SRH/Rrad/RAuger/current-field equivalence 검증 필수.

## 2026-10-08 — 주수빈 독립 Half-domain branch 병렬 검증 결정

- **작업자:** 주수빈
- **상태:** DECISION / PROPOSED IMPLEMENTATION
- 이택규의 `FAST_HALF_BULK_R15`은 half-domain + remote bulk mesh relaxation(BulkFac=1.5)을 동시에 적용한 가속 branch.
- 주수빈은 중복 구현 대신 **pure half-domain branch**를 별도로 만들어 half-domain 효과만 분리 검증하기로 결정.
- 주수빈 branch 원칙:
  - full FAST_C1 물리/contacts/traps/vertical epitaxy 유지
  - centerline symmetry cut만 적용
  - physical sidewall 1개 + 5 nm damage 유지
  - centerline에는 damage/trap 없음
  - MQW/EBL/heterointerface/sidewall mesh는 원본과 동일
  - remote bulk mesh도 첫 비교에서는 원본 유지
  - Iterations=15, RHSMin=1e-3 유지
  - 첫 비교에서는 numerical sweep policy도 C1과 동일하게 유지하여 half-domain 효과를 격리
- 비교 후:
  - pure half vs full reference equivalence 확인
  - 이택규 half+bulk-coarse branch와 runtime/accuracy 비교
  - 필요 시 validated pure half에 C2 Increment=1.05/checkpoint strategy를 추가한 통합 후보 생성
- 최종 baseline은 정확도와 runtime이 모두 우수한 branch 하나로 freeze.

## 2026-10-07 — Project A/B multi-day pre-run completeness audit

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** REVIEWED / PRODUCTION A-B NO-GO UNTIL GATES PASS
- FAST_C1/Common Baseline은 A/B의 parent로 사용할 수 있으며 물리 baseline을 다시 구축할 필요는 없다고 판정.
- same-current I-V extraction 및 v1.2 intermediate spatial TDR schedule은 FAST_C1 lineage에 유지되고 실제 Node 6에서 intermediate TDR 생성이 관찰됨.
- 하지만 광범위 A/B multi-day production sweep은 아직 시작하면 안 됨.
- 필수 사전 항목:
  1. 실제 active pp1_dvs/ppN_des.cmd/par audit (stale public CURRENT 사용 금지)
  2. existing TDR에서 SRH/Radiative/Auger/carrier/current/band/trap/polarization dataset 실제 존재 확인
  3. sidewall SRH/MQW Rrad/RAuger/IQE/current crowding/band cutline extraction workflow 선검증
  4. 2D current -> J normalization 확정
  5. Project A: parameterized Cedge_L/R + explicit same-material region mesh + carbon physics + null control
  6. Project B: AlBarrier vertical span 확정 + parameterized xAl/wAl + lateral heterointerface mesh + null control
  7. C2 Save/Load checkpoint smoke 통과
  8. 대표 A/B pilot 후 broad DOE
- Project B가 QW edge를 AlGaN으로 치환하는 geometry라면 active QW volume이 변하므로 total Rrad/IQE만으로 confinement 효과를 해석하지 말고 QW volume normalization 및 injection/leakage metric을 함께 보고해야 함.
- Project A는 GaN:C self-compensation 가능성을 고려해 Stage-1 acceptor 외 optional donor/compensation parameter를 production code 구조에 미리 예약하는 것이 권고됨.
- 상세 GO/NO-GO 문서: `CMP/PROJECT_AB_PRE_RUN_AUDIT.md`.

## 2026-10-07 — FAST_C1 same-current output audit for Project A/B

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** REVIEWED / PARTIALLY CONFIRMED
- FAST_C1 public implementation record confirms the only executable change vs Copy x8 golden source is forward-Transient inner `Coupled`에 `Iterations=15` 추가이며, physics/traps/Math tolerances/ILS/Transient step control/5 V Goal/**spatial Plot schedule**은 유지됨.
- 2026-09-28 Final SDevice v1.2에서 same-current spatial comparison을 위해 Transient 내부에 visualization-only intermediate `Plot(-Loadable ... NoOverWrite Time=(...))` 저장을 추가했음. 저장점은 t=0.80,0.84,0.88,0.92,0.94,0.96,0.97,0.98,0.985,0.99,0.995 → 4.0,4.2,4.4,4.6,4.7,4.8,4.85,4.9,4.925,4.95,4.975 V.
- 실제 FAST_C1 Node 6에서 4.0/4.2/4.4/4.6/4.7 V intermediate TDR 생성이 관찰되어 Plot schedule이 실행 deck에서 작동하는 근거가 있음.
- 따라서 사용자가 기억한 “same-current 비교용 Transient 추가”는 **전류를 Goal로 직접 구동하는 코드가 아니라**, voltage sweep I-V에서 target current에 해당하는 V를 찾은 뒤 그 V 근처의 saved TDR spatial state를 비교하기 위한 output/save-control임.
- Project A/B 공정 비교의 핵심 output(SRH/Radiative/Auger, IQE용 적분, carrier/current maps, band profile, Vf)은 golden v1.2 계열 기록상 의도된 diagnostics에 포함되어 있음. 다만 public GitHub에는 proprietary full active source가 없어 field keyword 전체를 현재 실행 pp deck 기준으로 100% 재감사할 수는 없음.
- **남은 gate 1:** absolute Current Density [A/cm2]는 T-2022.03 2D current/AreaFactor normalization 확인 전 provisional. same raw injected current 비교는 동일 geometry/2D-depth 조건에서 가능하지만 publication J 표기는 확정 전 사용 금지.
- **남은 gate 2:** fixed-voltage TDR grid는 4.925/4.95/4.975 V처럼 5 V 근처가 촘촘하지만, A/B가 더 큰 Vf shift를 만들거나 여러 J operating point를 요구하면 target V에 충분히 가까운 snapshot이 없을 수 있음. A/B production 전에 operating-current window를 정한 뒤 Plot schedule density 또는 exact matched-current state extraction을 재검토해야 함.
- **판정:** 현재 FAST_C1을 다시 버릴 이유는 없음. same-current 비교 기반은 들어가 있으나, “모든 Project A/B current-density comparison이 완성됐다”고 freeze하기 전에 J normalization + snapshot coverage를 최종 확인해야 함.

## 2026-09-29 — Node 6 end-of-ramp failure risk assessment

- **작업자:** 주수빈
- **상태:** RESEARCH JUDGMENT / RUNNING
- 현재 Node 6은 pseudo-time 약 0.93254(약 4.66 V)까지 진행했고, Newton 50회 초과 후 timestep cutback으로 재시도 중.
- 이 상태는 즉시 fatal error를 의미하지 않으며, 캡처 시점에는 solver가 정상적으로 adaptive retry를 수행하고 있음.
- 다만 마지막 고전압 구간에서 반복 비수렴이 지속되어 timestep이 `MinStep`까지 축소되거나 accepted progress가 사라지면 최종적으로 nonconvergence failure가 발생할 가능성은 남아 있음.
- 현재 근거만으로 마지막까지 반드시 성공한다고 보장할 수는 없지만, 이미 high-bias 구간까지 진입했고 자동 cutback이 작동 중이므로 즉각적인 오류 징후로 보지는 않음.
- 판별 기준: pseudo-time이 계속 증가하고 successful step이 간헐적으로라도 나오면 계속 진행; 동일 위치에서 장시간 정지하며 timestep이 계속 축소되면 failure risk 상승.

## 2026-09-29 — Active Node 6 output confirms ongoing solve with severe cutback

- **작업자:** 주수빈
- **상태:** OBSERVED / RUNNING BUT SLOW
- **근거:** 사용자 제공 `Node 'n6' Output` / `n6_des.out` 화면.
- pseudo-time 약 0.93254까지 진행했으며, 0→5 V ramp 기준 약 4.66 V 구간에 해당.
- 한 BE step이 Newton iteration 50회를 넘겨 수렴하지 못해 reject됨.
- SDevice가 자동으로 timestep을 약 8.67e-06으로 줄여 재시도 시작.
- 해당 실패 step의 wallclock은 약 1244 s(약 20.7분), solve time 약 999 s.
- 캡처 시점에는 hang이 아니라 adaptive timestep cutback 중이나, high-bias 수렴성이 나빠 전체 runtime이 크게 늘고 있음.
- 직전 topology 화면만으로 active node를 Node 19로 추정했던 내용은 direct output 증거에 따라 Node 6으로 정정.
- **다음:** `n6_des.out`에서 pseudo-time이 0.93255 이후 계속 증가하는지와 timestep 회복 여부 확인. 장시간 같은 위치 정지 또는 MinStep까지 지속 cutback일 때만 solver intervention 검토.

## 2026-09-29 — 3-day run status screenshot checked

- **작업자:** 주수빈
- **상태:** OBSERVED / RUNTIME BLOCKER
- **근거:** 사용자 제공 Sentaurus Workbench 화면.
- 선택된 상단 SDevice branch는 오른쪽 Properties에서 `Status: waiting` 확인. 즉 해당 branch는 아직 계산 시작 전 대기 상태.
- 하단 branch의 Node 19는 Workbench topology상 실행 중 표시로 보이지만, 이 화면만으로 실제 solver가 계속 전진 중인지/hang인지 확정할 수 없음.
- 따라서 현재 상태는 "두 branch 모두 3일 동안 계산 중"으로 해석하지 않음. 최소 한 branch는 scheduler/resource 대기 상태이며, 실행 중 branch의 실제 진행 여부는 Node 19 Job Log와 `n19_des.out` 마지막 timestamp/BE-step으로 확인해야 함.
- **다음:** Node 19 선택 → Job Log bottom 및 `n19_des.out` 마지막 30~50줄 확인. 마지막 로그 시간이 현재에 가깝고 BE-step이 증가하면 정상 장시간 계산; 오래 멈춰 있으면 resource/hang 진단.

# Ju Subin Timeline

## 2026-09-26 — Project A/B command-level implementation strategy refined

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** RESEARCH JUDGMENT / CES PRESENTATION PLAN
- **Project A:** 1차 mechanism screen은 implantation process simulation이 아니라 SDE에서 upper n-GaN edge를 `Cedge_L/R` GaN region으로 분리하고, SDevice에서 region-specific carbon deep acceptor/compensation을 적용. QW에 carbon trap 직접 삽입하지 않음. C implantation은 damage-induced isolation과 carbon compensation이 섞이므로 후속 process-realistic study로 분리.
- **Project B:** implantation이 아닌 실제 AlGaN material region `AlBarrier_L/R`을 SDE에 삽입. xAl/wAl parameter sweep, lateral GaN/AlGaN interface mesh refinement, SDevice에서 band offset/polarization 기반 confinement을 검증. fabrication analogue는 recess/etch + selective-area AlGaN regrowth이며 exact microLED integration은 hypothesis.
- **공통:** baseline 5 nm DmgL/R 및 defect model 유지. SProcess는 현재 A/B 1차 device-level comparison에는 사용하지 않음.

# Ju Subin Timeline

## 2026-09-26 — CES 발표 9장 구조로 압축

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** DECISION / PRESENTATION STRUCTURE
- **결정:** 15분 제한을 고려해 Week 1 보완/왜 baseline인가/문헌 역할 설명을 여러 장으로 분리하지 않고 초반 1장으로 압축.
- **새 흐름:** 주제·진행상황 요약 → baseline 문헌 근거 → 현재 baseline 구조 → parameter provenance → validation/status → Project A → Project B → fair comparison → conclusion.
- **목표:** 발표 시간을 baseline 구축 논리, 실제 TCAD 수정 지점, A/B 비교 protocol에 집중.

## 2026-09-26 — 발표 핵심 논리: 근거→모델→코드→지표를 연구자 본인이 설명

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** DECISION / PRESENTATION METHODOLOGY
- **사용자 목표:** AI 지시를 따른 인상 대신, baseline과 Project A/B의 근거·코드 변경·검증 지표를 스스로 완전히 이해하고 설명하는 발표.
- **발표 구조:** 각 요소를 DIRECT LITERATURE / LITERATURE-DERIVED MODELING CHOICE / CALIBRATION / PROJECT HYPOTHESIS로 구분.
- **핵심 논리:** 논문에서 무엇을 가져왔는지 → 왜 A/B 공통 baseline에 필요한지 → Sentaurus에서 무엇을 구현하는지 → 어떤 output으로 검증할지 → 최종 A/B를 어떤 기준으로 비교할지.
- **중요:** Carbon high-resistance edge와 localized AlGaN lateral heterobarrier 자체는 문헌 복제 구조로 주장하지 않고, 알려진 Carbon compensation 및 heterobarrier/carrier-confinement physics를 sidewall 접근 억제에 적용하는 연구 가설로 제시.

## 2026-09-26 — CES2027 선발 평가발표 준비 우선순위 전환

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** DECISION / PRESENTATION STRATEGY
- **발표 맥락:** 심사위원은 '공학및지식실무' 교과목 교수 2명이며 1주차 발표를 이미 봄.
- **1주차 약점:** 급한 주제 변경으로 TCAD simulation 결과가 없었고, Project A/B를 실제 TCAD에서 어떻게 구현·검증할지 구체적으로 설명하지 못해 낮은 평가를 받음.
- **이번 발표 핵심 보완:** 주제 재설명보다 (1) Common Baseline 구축 근거, (2) 현재까지 실제 TCAD 구현/실행 증거, (3) Project A Carbon high-resistance edge 및 Project B localized AlGaN lateral heterobarrier의 구체적 TCAD 구현 절차, (4) 비교 지표와 성공 판정 기준을 중심으로 구성.
- **표현 원칙:** 완료된 simulation, 진행 중 validation, 향후 A/B DOE를 명확히 구분. 미완료 결과를 완료처럼 제시하지 않음.
- **발표 목표:** 교수진에게 '아이디어 단계'가 아니라 '실행 가능한 연구 설계와 검증 로드맵을 갖춘 프로젝트'임을 보여주는 것.

## 2026-09-26 — Today-only baseline/PPT deadline strategy

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** DECISION / PRESENTATION PLAN
- **사용자 제약:** 오늘 안에 Common Baseline을 정리하고 PPT 제작까지 완료해야 함.
- **판단:** full 5 V NtSide=1e18 SDevice run은 과거 runtime 기준 수일이 필요하므로 오늘 완료를 기다리는 것은 현실적이지 않음.
- **오늘 목표 재정의:** final source freeze + structural/code validation + NtSide=1e18 initialization/early-solve sanity check + historical NtSide=0 completed reference를 확보하고 PPT에는 full trap-on electrical validation을 ongoing으로 명확히 구분.
- **금지:** 미완료 NtSide=1e18을 완료 결과처럼 제시하지 않음.
- **다음:** 수정 SDevice로 Node12 early initialization 확인 → pp cmd/par sanity check → PPT baseline evidence 정리.


## 2026-09-26 — Node12 최소 수정안 확정

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** PROPOSED FIX
- **수정:** global `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")` 제거.
- **추가:** `Clean_pGaN`, `DmgL_pGaN`, `DmgR_pGaN`에만 동일 `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")` 적용.
- **유지:** `Thermionic`, `NtSide`, trap Et/sigma, geometry, Plot, Math, Solve 전부 유지.
- **검증:** 수정 후 NtSide=0/1e18을 동일 final source/PAR revision에서 재실행.


## 2026-09-26 — Node 12 project/scheduler log interpretation

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED
- **근거:** Project Log 화면.
- **확인:** Node 12 SDevice가 실제로 시작된 뒤 약 수 초 내 `exited abnormally: exit()`로 종료하고 scheduler가 failed 처리, `gsub exits with status 1`.
- **의미:** 이 화면은 실행 실패 사실과 시점을 확인해 주지만, root-cause message 자체는 포함하지 않음.
- **진단 우선순위:** root cause는 `n12_des.log`/`n12_des.err` 및 `pp12_des.par` 내용으로 판단. 현재 가장 강한 후보는 InGaN에서 Mg incomplete-ionization parameter가 없는 상태에서 global Mg incomplete-ionization을 활성화한 material-scope mismatch.


## 2026-09-26 — 중요 정정: Node6/Node12 parameter file도 서로 다른 revision

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / COMPARISON INVALIDATED
- **근거:** 사용자 제공 성공 Node6 `pp6_des.par` 화면과 실패 Node12 `pp12_des.par` 화면 비교.
- **Node6 par:** GaN Ionization에 `PDopantActiveConcentration` (E0=0.15, g=4, Xsec=1e-12) 및 `NDopantActiveConcentration` (E0=0.05, g=2, Xsec=1e-12).
- **Node12 par:** GaN Ionization에 `pMagnesiumActiveConcentration` (E0=0.2, alpha=8e-9, g=4, Xsec=1e-14).
- **결론:** 기존 Node6와 current Node12는 command deck뿐 아니라 parameter file도 다른 revision. 따라서 Node12만 수정해서 기존 Node6와 비교하는 것은 fair NtSide-only comparison이 아님.
- **정정:** 직전 'Node12만 region-scoped Mg incomplete ionization으로 수정 후 기존 Node6와 비교' 제안은 비교 목적에는 철회.
- **올바른 방법:** 최종 baseline source + parameter file을 먼저 freeze하고, 그 동일 revision으로 NtSide=0과 1e18을 둘 다 새로 preprocess/run해야 함.
- **진단 목적:** Node12 crash를 고치기 위한 region-scoped Mg incomplete-ionization 실험은 가능하지만, 그 결과는 기존 Node6와 final quantitative comparison에 사용하지 않음.


## 2026-09-26 — pp12_des.par confirms Mg incomplete-ionization material-scope mismatch

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / PROPOSED FIX
- **근거:** 사용자가 Node 12의 전체 `pp12_des.par` 화면 제공.
- **parameter file 내용:** `Material="GaN"`의 `Ionization` block에 `Species("pMagnesiumActiveConcentration")`만 정의됨 (E_0=0.2, alpha=8e-9, g=4.0, Xsec=1e-14). InGaN/AlGaN Ionization block은 없음.
- **실패 log와 결합한 판단:** current source의 global `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`가 전체 device에 활성화된 상태에서 InGaN QW에서 Mg-related species의 ionization parameter가 없다는 메시지 직후 SDevice가 종료됨. material scope mismatch가 가장 강한 root-cause 후보.
- **최소 수정안:** global IncompleteIonization을 제거하고 Mg가 실제 p-GaN에 필요한 `Clean_pGaN`, `DmgL_pGaN`, `DmgR_pGaN`에만 region-specific으로 적용. Thermionic/trap Et/sigma/NtSide/Plot은 건드리지 않음.
- **검증:** 수정 후 Node12 재-preprocess → 초기화 통과/Poisson solve 진입 여부 확인. 통과 시 원인 확인 강화.
- **공정 비교 주의:** 최종 baseline freeze 후 NtSide=0과 1e18은 동일 final source revision으로 다시 비교해야 함.


## 2026-09-26 — Current full SDevice source inspected; stale Node 6 provenance identified

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / ROOT-CAUSE NARROWING
- **자료:** 사용자가 현재 원본 SDevice 전체 코드를 제공.
- **확인:** source에서 `@NtSide@`는 trap `Conc`에만 사용되며, `NtSide`에 따른 `#if/#else/#endif` conditional은 없음.
- **현재 source 고정 Physics:** `Thermionic`, `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`, Mg/quasi-Fermi 관련 Plot fields 포함.
- **의미:** 현재 source를 preprocess한 Node 12가 이 구성을 갖는 것은 정상. 반면 성공 Node 6 pp6에는 이 항목들이 없으므로 Node 6은 현재 source revision으로 재-preprocess된 node가 아니라 과거 source revision의 generated/output artifact일 가능성이 매우 높음.
- **따라서:** 기존 Node6(success) vs 현재 Node12(fail)는 엄밀한 same-source NtSide-only 비교가 아님.
- **현재 실패 핵심 후보:** species-selected incomplete ionization이 InGaN QW의 Mg species에 적용되면서 parameter file에 해당 ionization parameter가 없어 초기화 종료. 실제 Node12 log가 InGaN QW의 Mg incomplete-ionization parameter missing 직후 종료.
- **다음:** `pp12_des.par`에서 `Ionization`, `Magnesium`, `InGaN` block 확인. parameter definition과 doping species naming을 확인한 뒤 최소 수정 결정.


## 2026-09-26 — Node 12 단독 재실행에서도 동일 failure 재현

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / REPRODUCIBLE
- **근거:** 사용자가 Node 12만 다시 실행했으나 동일하게 failed 상태가 재현됨.
- **의미:** 일회성 queue/license/transient 환경 오류 가능성은 낮아지고, Node 12가 사용하는 현재 preprocessed input/configuration에 재현성 있는 문제가 있을 가능성이 높아짐.
- **중요 정정 유지:** 사용자는 동일 source에서 NtSide만 split했다고 확인했으므로, pp6/pp12 차이는 source를 별도로 편집했다는 뜻이 아님.
- **가장 유력한 설명 후보:** (1) source 내부 NtSide-dependent preprocessor conditional, 또는 (2) Node 6이 과거 source 버전의 stale/cached preprocess/output을 재사용하고 Node 12만 현재 source로 재-preprocess됨.
- **다음:** 원본 `sd_fdiv_des.cmd`에서 `NtSide`, `#if/#else/#endif`, `Thermionic`, `IncompleteIonization`, Mg Plot fields를 직접 확인하고, Node6/12 Job Log의 preprocess source timestamp/provenance를 비교.


## 2026-09-26 — 중요 정정: 사용자 확인상 source는 동일, NtSide만 split

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** USER-CONFIRMED / UNRESOLVED
- **사용자 확인:** Node 6과 Node 12는 원본 코드를 별도로 수정한 것이 아니라 동일한 SDevice source에서 `NtSide`만 0 / 1e18로 split하여 실행함.
- **정정:** 직전의 "Node 12 source deck drift" 해석은 확정할 수 없음. preprocessed deck 차이는 source 자체가 달랐다는 증거가 아니라, NtSide-dependent preprocessing/conditional branch 또는 node input/version/cache 차이일 수 있음.
- **중요:** 원인 확인 전 `Thermionic`, `IncompleteIonization`, Plot 항목을 임의 삭제/변경하지 않음.
- **다음:** 실제 원본 `sd_fdiv_des.cmd`에서 `@NtSide@`, `Thermionic`, `IncompleteIonization`, `Dopants`, preprocessor conditional(`#if` 등) 존재 여부 확인. Node 6/12 Job Log의 source path와 preprocessing 시각도 대조.


## 2026-09-26 — Node 6 vs Node 12 exact Physics/Plot diff identified

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED + PROPOSED FIX
- **근거:** 사용자가 성공 Node 6 및 실패 Node 12의 preprocessed Physics/Trap/Plot block을 직접 제공.
- **공통:** Temperature/Fermi/Piezoelectric/DefaultParameters/Recombination/Mobility/Aniso 및 trap Et=Ev+0.75 eV, e/h Xsection=1e-15는 동일.
- **의도된 차이:** trap `Conc=0` (Node 6) vs `Conc=1e18` (Node 12).
- **추가 비의도 차이:** Node 12에만 `Thermionic`; Node 12는 `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`, Node 6는 plain `IncompleteIonization`; Node 12 Plot에 `eQuasiFermiEnergy`, `hQuasiFermiEnergy`, `pMagnesiumActiveConcentration`, `pMagnesiumMinusConcentration` 추가.
- **판단:** 현재 Node 6/12는 NtSide만 다른 true split이 아님. 따라서 Node 12 실패를 NtSide=1e18 trap 자체의 실패로 결론낼 수 없음.
- **제안:** 원본 SDevice source를 Node 6 physics/plot과 동일하게 복구하고 trap Conc parameter만 1e18로 유지하여 Node 12를 다시 실행. `pp12_des.cmd`는 생성물이라 직접 수정하지 않음.
- **주의:** `Thermionic` 자체가 물리적으로 잘못이라는 판단은 아님. 사용하려면 0/1e18 두 branch에 동일하게 적용해 별도 baseline 재검증.


## 2026-09-26 — Failed Node 12 preprocessed Physics/Plot block captured

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **자료:** 사용자 제공 Node 12 preprocessed SDevice Physics/Plot block.
- **Node 12 global Physics:** `Thermionic` 활성, `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")` 사용.
- **Trap:** DmgL/R의 pGaN, EBL, Barrier0~4, QW1~4, nGaN 전체에 Acceptor trap `Conc=1e18`, `FromValBand EnergyMid=0.75`, `e/h Xsection=1e-15`.
- **Plot:** 기존 baseline 기록보다 확장된 trap/SRH/Mg 관련 output 항목(`eSRHRecombination`, `hSRHRecombination`, `tSRHRecombination`, `TotalTrapConcentration`, trapped charge/gap-state fields, Mg fields 등)이 포함됨.
- **중요 관찰:** GitHub에 동기화된 기존 baseline deck은 plain `IncompleteIonization`이며 `Thermionic`이 없고 Plot 항목도 더 단순함. 따라서 Node 12가 단순히 NtSide만 바뀐 deck인지 아직 보장되지 않음.
- **다음:** 성공 Node 6의 대응 `pp6_des.cmd` Physics/Trap/Plot block을 받아 exact diff. 원인 확정/수정은 diff 이후.


## 2026-09-26 — NtSide=0 성공 run 최종 확인 및 Node 12 차이점 강화

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** CONFIRMED (NtSide=0 completion) / UNRESOLVED (NtSide=1e18 failure)
- **근거:** 성공 Node 6 `n6_des.log` 마지막 화면.
- **NtSide=0 성공:** anode 5.000 V까지 도달, curve trace finished, `n6_des.tdr` 저장 완료, `Sentaurus Device simulation finished`, `Good Bye !` 확인.
- **wallclock:** 약 235312.35 s ≈ 65.4 h ≈ 2.7 days.
- **비교:** 성공 Node 6 log에는 `mMagnesiumActiveConcentration` 검색 결과가 없다고 사용자 확인. 실패 Node 12는 해당 InGaN incomplete-ionization 메시지 반복 직후 종료.
- **해석:** 해당 메시지는 강한 차이점/원인 후보가 되었으나, split deck이 NtSide 외에 달라졌을 가능성을 먼저 배제해야 함.
- **다음:** `pp6_des.cmd` vs `pp12_des.cmd`, 그리고 `pp6_des.par` vs `pp12_des.par` 비교. 의도된 차이가 trap Conc 0 ↔ 1e18뿐인지 확인.


## 2026-09-26 — GitHub 자동 미러 동기화 구축

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Collaboration infrastructure / GitHub sync
- **상태:** CONFIRMED
- **연결 계정:** `soybeanmilk0514-jpg`
- **대상 저장소:** `soybeanmilk0514-jpg/TCAD-MicroLED-Sidewall-Carrier-Confinement`
- **원본 source of truth:** `TaekGyu0801/GGYU`의 `CMP/`
- **구현:** `.github/workflows/sync-cmp.yml` 생성. GitHub Actions가 5분 주기로 원본 CMP 전체를 수빈 저장소의 `CMP/`에 `rsync --delete` 방식으로 미러링.
- **LIVE LOG:** 원본 GitHub Issue #7 comments도 `CMP/.ai-sync/LIVE_LOG_ISSUE_7_MIRROR.md`에 자동 미러링.
- **검증:** 첫 workflow run #1이 2026-09-26에 `success`로 완료됨.
- **경계:** GitHub cron 특성상 완전한 실시간 push mirror가 아니라 최대 수분 단위 동기화. CMP 외 원본 GGYU 파일은 미러링하지 않음.

# Ju Subin Timeline

## 2026-09-26 — Node 12 des.log 종료 지점 확인

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **근거:** `n12_des.log` 마지막 구간.
- **관찰:** 로그는 InGaN QW region의 `mMagnesiumActiveConcentration` incomplete-ionization parameter 메시지 반복 직후 license check-in으로 끝남. 정상 solve 시작/완료 로그는 없음.
- **해석:** 해당 메시지가 단순 warning인지 SDevice initialization을 중단시킨 configuration error인지 아직 확정 불가.
- **가장 강한 판별법:** 성공한 `NtSide=0` node의 대응 `*_des.log`에서 같은 메시지가 존재하는지 비교. 성공 node에도 동일하면 원인 가능성 낮음; failed node에만 있으면 핵심 원인 후보.
- **다음:** 성공 node log 비교 후 필요 시 `n12_des.sta` 확인.


## 2026-09-26 — Node 12 Find Error 결과: explicit fatal 없음

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **근거:** Node 12 Job Log의 `Find Error` 결과 마지막 화면.
- **관찰:** Find Error 결과는 vanOverstraetendeMan E0 anisotropy warning, InGaN QW의 Mg incomplete-ionization parameter warning들을 나열한 뒤 `**** End`로 종료.
- **판단:** 현재 error stream / Find Error 결과에는 직접적인 ERROR/FATAL root cause가 나타나지 않음.
- **다음:** Node Output Files의 `n12_des.log`를 열어 실제 SDevice simulation log의 마지막 부분 확인. 이후 필요 시 `n12_des.sta`.
- **주의:** warning만으로 trap physics 또는 incomplete-ionization을 원인으로 확정하지 않음.


## 2026-09-26 — Node 12 Job Log 확인: preprocessing 성공, SDevice exit(1)

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **근거:** Node 12 Job Log 화면.
- **관찰:** preprocessor가 `pp12_des.cmd`, `pp12_des.par`를 정상 생성했고 dependency 분석도 완료.
- **실행:** `sdevice --max_threads 4 pp12_des.cmd`로 SDevice가 실제 시작됨.
- **종료:** 10:45:47 시작 → 10:45:14? 화면상 약 수십 초 내 `sdevice exited abnormally: exit(1)` 기록. (정확 timestamp 표기는 화면 원문 우선)
- **판단:** Workbench preprocessing/dependency 오류가 아니라 SDevice가 command deck 초기화/모델 설정 단계에서 non-zero exit한 것으로 좁혀짐.
- **다음:** Job Log의 `Find Error` 기능 또는 `n12_des.err` 검색으로 최초 explicit error/fatal line 확인.


## 2026-09-26 — Node 12 local.err 확인: wrapper-level abnormal exit

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **근거:** `n12_local.err` 화면.
- **내용:** `Job failed`, `Error: Unknown error: child process exited abnormally`, `gjob exits with status 1` 확인.
- **해석:** Workbench/gjob가 SDevice child process의 비정상 종료를 감지한 것은 확인되었지만, 이 메시지만으로 원인을 특정할 수 없음.
- **다음:** Node 12 **Job Log** 하단의 command/exit 정보 확인. 필요 시 `n12_des.job` 및 `n12_des.sta` 확인.
- **보호:** 원인 확인 전 Nt/Et/sigma/geometry 변경 금지.


## 2026-09-26 — NtSide=1e18 Node 12 로그 1차 확인

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **근거:** Node 12 Explorer의 `n12_des.err` 및 `n12_des.out` 화면.
- **관찰:** `n12_des.err`에는 vanOverstraetendeMan E0 anisotropy 관련 warning과 InGaN 영역의 `mMagnesiumActiveConcentration` incomplete-ionization parameter warning이 반복되지만, 화면에 직접적인 fatal/error는 보이지 않음.
- **관찰:** `n12_des.out`은 reference-potential/parameter 초기화 뒤 license check-in으로 끝나며 `Sentaurus Device simulation finished` / `Good Bye !`가 없음.
- **관찰:** Node 12 Output Files 화면에 `.tdr` / `.plt` 결과 파일이 보이지 않음.
- **판단:** 현재 증거는 Newton/Transient 수렴 실패보다 Solve 본격 시작 전 초기화/프로세스 종료 가능성을 우선 시사. 정확 원인은 아직 미확인.
- **다음:** `n12_local.err` → Job Log / `n12_des.job` 순서로 process exit reason 확인.


## 2026-09-26 — Common Baseline split-run 결과 확인: NtSide=0 성공, NtSide=1e18 실패

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Common Baseline / simulation result
- **상태:** OBSERVED
- **근거:** 사용자가 학교에서 Sentaurus Workbench split-run 상태 화면을 직접 확인해 제공.
- **관찰:** `NtSide=0` 조건은 정상 완료되었고, `NtSide=1e18` 조건은 failed 상태로 확인됨.
- **현재 해석 경계:** 실패 원인은 아직 확인되지 않았으므로 convergence / trap-coupling / syntax / resource 문제 중 어느 하나로 단정하지 않음.
- **다음:** 실패한 1e18 run의 실제 SDevice `*.err` 및 `*.out` 마지막 구간을 확인해 최초 fatal/error 또는 convergence failure 지점을 식별한 뒤 최소 수정.


## 2026-09-22 — Project A/B TCAD 구현 계획 구체화

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** CES 발표 / Project A-B 연구설계
- **상태:** PROPOSED
- **배경:** 1차 발표 후 교수진이 Carbon high-resistance 영역과 AlGaN lateral barrier를 실제로 어떻게 형성/코딩하고 무엇을 볼 것인지 질문함.
- **Project A 제안:** baseline 5 nm damage는 유지하고 그 안쪽 upper n-GaN edge에 C-doped/high-resistivity guard region을 추가. C-related deep acceptor/compensation으로 current path를 중앙으로 유도하고 sidewall SRH 감소 여부를 확인.
- **Project B 제안:** baseline damage 안쪽 active-region edge에 localized AlGaN lateral heterobarrier를 추가. Al mole fraction/width를 parameter sweep하고 lateral band offset, carrier confinement, sidewall SRH 감소를 확인.
- **공통 평가:** same-current 비교, integrated sidewall SRH, MQW radiative/Auger, IQE, Vf, current crowding, lateral carrier/current maps.
- **주의:** A/B의 실제 공정 치수/농도/Al composition은 아직 freeze하지 않았으며 DOE 제안 단계.
- **산출물:** `CMP/PROJECT_AB_TCAD_IMPLEMENTATION_PLAN.md`

---

## 2026-09-22 — CES2027 선발 발표 스토리라인 설계 시작

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** 발표 / CES2027 selection
- **상태:** PROPOSED
- **목표:** 다음 주 월요일 15분 CES2027 선발 발표를 위해, 1주차 주제 소개 반복이 아니라 Common Baseline의 문헌 근거 → 구조적 검증 → Project A/B TCAD 구현 전략을 중심으로 발표 구조를 재설계.
- **핵심 메시지:** JBD application scale, Kou 2019 vertical epitaxy, Wu 2023 localized sidewall damage, Chen 2024 small-size sidewall evidence를 역할별로 분리해 baseline의 출처를 설명하고, 동일 baseline 위에서 A/B를 공정 비교하는 연구 설계를 강조.
- **주의:** 아직 완료되지 않은 장시간 SDevice 결과는 확정 결과처럼 발표하지 않으며, 구조적 검증과 전기/광학 validation 진행 상태를 구분.
- **산출물:** `CMP/CES2027_PRESENTATION_PLAN.md`

---

## 2026-09-21 — Common Baseline 코드 최종 수정 보고 / 장시간 run 전 최종 검토

- **작성자:** ChatGPT (공유 프로젝트 대화 동기화)
- **작업자:** 주수빈
- **구분:** Common Baseline 검토 / simulation 준비
- **상태:** OBSERVED — 주수빈 채팅의 사용자 보고 기준
- **작업 내용:** 주수빈이 메인 SDevice 코드를 포함해 앞서 검토된 관련 코드들을 최종 수정했다고 보고함.
- **현재 판단 요청:** Project A와 Project B 모두에 사용할 Common Baseline으로 적합한지, 장시간 simulation을 시작하기 전에 코드와 논리를 마지막으로 꼼꼼히 검토하는 단계.
- **우선 실행 계획:** 전체 Nt sweep을 바로 돌리지 않고 먼저 `NtSide=0`과 `NtSide=1e18` 두 조건을 실행해 baseline 동작을 확인할 계획.
- **비용/제약:** 주수빈 보고 기준으로 한 조건의 simulation이 약 3일 소요될 수 있어, run 전 검증을 우선함.
- **주의:** 이 동기화 시점에는 주수빈 측 최신 전체 코드 원문과 실제 simulation 결과를 GitHub에서 직접 검증하지 못했으므로 코드 정확성/실행 성공은 CONFIRMED로 기록하지 않음.
- **다음:** 주수빈 측 최신 전체 코드 동기화 → baseline 최종 정적 검토 → `NtSide=0`, `NtSide=1e18` 실행 → 결과/로그 GitHub 기록.

---

## 2026-09-22 — NtSide split 실행 중 SWB 실행 순서 점검

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Common Baseline / Workbench dependency diagnostic
- **상태:** OBSERVED + UNRESOLVED
- **관찰:** 사용자가 Sentaurus Workbench 화면에서 NtSide=0, 1e18 두 split을 준비/실행하는 과정에서 SDE보다 SDevice가 먼저 동작하는 것처럼 보인다고 보고함.
- **해석:** NtSide가 SDevice에서만 사용되고 SDE geometry/mesh가 이미 유효한 upstream 결과라면 SWB가 SDE를 재실행하지 않고 같은 SDE 결과를 재사용해 SDevice split부터 실행하는 것은 정상일 수 있음.
- **주의:** 반대로 해당 experiment에서 SDE가 한 번도 성공적으로 실행되지 않았는데 SDevice가 시작된다면 SDE→SDevice dependency 또는 SDevice File/Grid 입력 연결을 확인해야 함.
- **다음 확인:** SDevice preprocessed `pp*_des.cmd`의 `File { Grid=... }`가 실제 SDE 생성 TDR을 가리키는지, 그리고 SDE output에 해당 mesh TDR이 존재하는지 확인.

---

## 2026-09-22 — SDE→SDevice dependency 정상 확인

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Workbench dependency diagnostic
- **상태:** CONFIRMED
- **근거:** Node 6 Explorer의 preprocessed `pp6_des.cmd`에서 `File { Grid = "n1_msh.tdr" }` 확인. 동일 Node 6 output 목록에 `n6_des.tdr`, `n6_des.plt`, `n6_des.log` 존재.
- **판단:** 현재 SDevice Node 6는 SDE에서 생성된 Node 1 mesh `n1_msh.tdr`을 정상 입력으로 사용 중이며, SDevice 자체 TDR도 정상 생성하고 있음.
- **결론:** NtSide split 실행에서 SDE가 다시 돌지 않고 SDevice부터 실행되는 현상은 기존 SDE mesh를 재사용하는 정상 동작으로 판단됨. NtSide가 SDE geometry를 바꾸지 않는 한 SDE 재실행은 필수 아님.

---


## 2026-09-22 — NtSide run 장시간 실행 상태 점검

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** SDevice runtime / convergence diagnostic
- **상태:** OBSERVED
- **관찰:** 사용자가 전날 밤부터 실행해 18시간 이상 지난 Node 6 SDevice output을 공유함. 화면상 계산은 정지하지 않았고 BE step을 계속 진행 중임.
- **근거:** `n6_des.out`에 직전 step이 `|Rhs| < 1.0000E-03`로 수렴 완료된 뒤, 다음 BE step이 약 `0.0766738 → 0.0776738`, `Stepsize = 1.0000E-03`로 진행 중. 직전 step 누적 wallclock은 Assembly 약 598.77 s, Solve 약 2928.83 s, Total 약 3563.68 s로 약 59분/step 수준.
- **판단:** 현재 화면만 보면 hang/fatal error라기보다 각 BE step 계산비용이 매우 큰 장시간 run 상태. 18시간 미완료 자체는 현재 step cost와 양립함.
- **추가 관찰:** `.err`의 vanOverstraetendeMan E0 isotropic/anisotropic 값 차이 메시지는 경고로 보이며, 현재 화면에서 run 중단 원인으로 관찰되지는 않음.
- **다음:** `pp6_des.cmd`의 Solve 블록에서 현재 transient/BE 구간의 최종 목표 시간(또는 ramp 목표), InitialStep/MinStep/MaxStep/Increment 설정을 확인해 예상 총 step 수와 총 wallclock을 산정. 코드 변경 전 최신 전체 deck 동기화 필요.

---

## 2026-09-22 — 장시간 run 원인 확인: Transient MaxStep=1e-3

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** SDevice runtime / step-control diagnosis
- **상태:** CONFIRMED (현재 preprocessed deck 및 log 기준)
- **근거:** `pp6_des.cmd`의 Transient block에서 `InitialStep=1e-5`, `MinStep=1e-9`, `MaxStep=1e-3`, `Increment=1.2`, `Goal { Name="anode" Voltage=5.0 }` 확인.
- **교차확인:** 실행 로그의 pseudo-time 약 0.0766738에서 anode voltage가 약 0.3834 V이며, `5.0 × 0.0766738 ≈ 0.38337 V`로 일치. 따라서 현재 transient coordinate가 0→1 동안 anode 0→5 V ramp에 대응함을 강하게 확인.
- **의미:** `MaxStep=1e-3`이면 최대 전압 증가량은 약 5 mV/accepted step. 현재 약 0.077 지점에서 5 V 목표까지 최소 약 923~924 accepted steps가 더 필요함.
- **runtime 추정:** 최근 관찰된 약 3563.68 s/step을 단순 적용하면 남은 시간이 약 38일 규모. 실제 step cost는 bias에 따라 달라질 수 있으므로 이는 거친 추정이지만 현재 설정이 매우 장시간인 원인은 분명함.
- **다음:** `pp6_des.cmd`가 아닌 원본 SDevice deck에서 numerical step strategy를 검토. Common Baseline physics(Nt/Et/sigma/5 nm damage 등)는 변경하지 않으며, A/B 및 Nt 비교에 동일한 numerical protocol을 적용해야 함.

---

## 2026-09-22 — runtime 원인 판단 정정/정밀화

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Runtime diagnosis refinement
- **상태:** OBSERVED / UNRESOLVED
- **사용자 추가 정보:** 최종 수정 전 거의 같은 코드가 약 3일 내 완료된 이력이 있다고 보고함.
- **정정:** 따라서 현재 `MaxStep=1e-3` 자체만으로 이번 느려짐의 '새 원인'이라고 단정할 수 없음. 이전 run에도 동일하거나 유사한 step 설정이 있었다면, 3일→현재 18시간에 pseudo-time ~0.077의 차이는 **accepted step 하나당 계산비용 증가 또는 rejected/cutback 증가**를 우선 의심해야 함.
- **현재 강한 단서:** 최근 한 step의 solve time이 약 2929 s, total 약 3564 s로 매우 큼. 이는 단순 step 개수보다 선형/비선형 solve cost, mesh unknown 수, conditioning, traps/physics coupling, 또는 반복적인 cutback 여부를 비교해야 함을 의미.
- **38일 추정의 지위:** 최근 한 개의 느린 step을 전체에 선형 외삽한 거친 상한성 추정으로만 유지하며, 실제 총 runtime 예측으로 사용하지 않음.
- **다음 비교 우선순위:** (1) 이전 3일 run의 Transient 설정, (2) mesh node/element 수, (3) Physics/Traps/region 적용 차이, (4) Math solver 설정, (5) log의 failed/repeated step 및 step cutback 빈도.

---

## 2026-09-22 — 과거 3일 run 초기 solve 시간 증거 확보

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** old-vs-current runtime comparison
- **상태:** OBSERVED
- **근거:** 사용자가 과거 약 3일 내 완료된 run의 초기 `.out` 로그 화면을 공유함.
- **관찰값:** 초기 0 V coupled solve에서 Assembly 약 350.52 s, Solve 약 232.46 s, Total 약 585.81 s. Newton iteration은 화면상 50회까지 진행 후 `|RHS| < 1.0000E-03`로 수렴.
- **주의:** 이 로그는 anode=0 V 초기 구간이므로 현재 run의 약 0.38 V step(Total ~3563.68 s)과 직접 1:1 비교할 수는 없음.
- **다음:** 과거 run에서 anode 0.3~0.4 V 구간의 step 로그를 찾아 동일 bias에서 Total time / Newton iteration / retry-cutback 여부를 비교.

---

## 2026-09-22 — 과거 3일 run 0.30 V 부근 step 비용 확인

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** old-vs-current runtime comparison
- **상태:** OBSERVED
- **근거:** 과거 약 3일 내 완료된 run의 `.out`에서 anode 약 0.3034 V 및 0.3084 V 구간 로그를 확인.
- **관찰값:**
  - 약 0.3034 V step: Assembly 35.80 s, Solve 136.34 s, Total 172.57 s
  - 약 0.3084 V step: Assembly 42.71 s, Solve 78.79 s, Total 123.94 s
  - 두 step 모두 5회 Newton iteration(0~4) 후 `|RHS| < 1e-3`로 수렴
- **비교:** 현재 run의 약 0.3834 V 부근에서 Total 약 3563.68 s/step이 관찰되어, 과거 0.30 V 부근보다 한 step 계산비용이 이미 매우 크게 증가해 있음.
- **주의:** bias가 정확히 동일하지 않으므로 최종 정량 비교는 과거 run의 0.38 V 부근 로그를 추가 확인해야 함.
- **다음:** 과거 run에서 anode 약 0.38 V(대략 0.375~0.390 V) 구간의 Total time / Newton iteration / retry 여부 확인.

---

## 2026-09-22 — old/current 동일 bias 0.3834 V step 직접 비교

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Runtime root-cause comparison
- **상태:** CONFIRMED (공유된 old/current 로그 화면 기준)
- **old run (~3일 완료):** pseudo-time 0.0756738→0.0766738, accepted anode ≈0.3834 V, Assembly 64.84 s, Solve 108.74 s, Total 177.47 s.
- **current run:** 동일 accepted anode ≈0.3834 V에서 Assembly 598.77 s, Solve 2928.83 s, Total 3563.68 s.
- **비교:** 동일 bias에서 현재 accepted step의 wallclock이 old 대비 약 20.1배 증가. 따라서 이번 slowdown의 주원인은 MaxStep/step count 자체가 아니라 **step 하나를 푸는 계산비용 증가**로 확정적으로 좁혀짐.
- **다음 원인 후보:** mesh unknown 수 증가, Physics/Trap 적용 범위 변화, Math/linear solver 설정 변화, 또는 비선형/선형 반복 비용 증가. old/current startup statistics와 preprocessed deck diff가 우선.

---

## 2026-09-22 — 중요 정정: 0.30~0.38 V의 123~177 s 로그도 현재 run 내부 초기 구간

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Runtime diagnosis correction
- **상태:** CONFIRMED (스크린샷 경로/라인 기준)
- **정정:** 앞선 답변에서 0.303~0.383 V, Total 123~177 s 로그를 '과거 3일 run'으로 잘못 해석했음. 새 스크린샷 상단 경로가 현재와 동일한 `.../n6_des.out`이고 사용자가 '돌아간 것 중 초창기 부분'이라고 설명했으므로, 해당 로그는 **현재 Node 6 run의 초기 구간**임.
- **현재 run 초기 구간 실제 값:** pseudo-time 0.0746738→0.0756738에서 Total 166.16 s, 이어 0.0756738→0.0766738에서 Total 177.47 s, accepted anode ≈0.3834 V.
- **중요 모순/단서:** 같은 현재 run의 나중 화면에서는 accepted anode ≈0.3834 V 직후 Total 3563.68 s가 관찰됨. 따라서 단순 old-vs-new 비교가 아니라 **현재 한 run 안에서 동일 pseudo-time/voltage ramp가 다시 등장하거나 다른 solve stage가 존재하는지** 확인해야 함.
- **다음:** `pp6_des.cmd`에서 `Transient(` 등장 횟수를 검색하고, `n6_des.out`에서 `0.0766738` 또는 `3563.68`을 검색해 느린 구간이 어느 Solve/Transient stage에 속하는지 식별.

---

## 2026-09-22 — 재정정: 0.3834 V / 177.47 s 로그는 과거 3일 완료 run

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Runtime evidence correction
- **상태:** CONFIRMED (사용자 직접 확인)
- **사용자 확인:** 직전 스크린샷의 `n6_des.out`은 현재 실행 중인 노드가 아니라 **예전에 약 3일 만에 완료된 노드의 파일**임.
- **따라서 유효 비교:** old run anode ≈0.3834 V에서 Total 177.47 s (Assembly 64.84 s, Solve 108.74 s), current run 같은 anode ≈0.3834 V에서 Total 3563.68 s (Assembly 598.77 s, Solve 2928.83 s).
- **비율:** current accepted-step wallclock은 old 대비 약 20.1× 증가.
- **결론:** slowdown은 step count 자체보다 per-step computational cost 증가가 핵심이라는 이전 판단을 복구.
- **주의:** 파일명 `n6_des.out`은 서로 다른 프로젝트/노드 복사본에서도 반복될 수 있으므로, 앞으로는 파일명만으로 old/current를 구분하지 않고 사용자의 노드 식별과 경로 맥락을 함께 사용.

---

## 2026-09-22 — 과거 약 3일 완료 node의 full preprocessed SDevice deck 확보

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Old-vs-current runtime baseline capture
- **상태:** OBSERVED
- **자료:** 사용자가 과거 약 3일 만에 완료된 node의 `pp6_des.cmd` 전체 내용을 제공.
- **old deck 주요 설정:**
  - Grid=`n1_msh.tdr`
  - global Physics: Fermi, Piezoelectric_Polarization(strain), SRH/Auger/Radiative, Masetti + CaugheyThomas + Lombardi, IncompleteIonization, Aniso(Poisson)
  - DmgL/R의 pGaN, EBL, Barrier0~4, QW1~4, nGaN에 Acceptor trap 정의
  - **모든 trap Conc = 0**
  - trap: FromValBand, EnergyMid=0.75, e/h Xsection=1e-15
  - Math: NumberOfThreads=4, Digits=5, ErrRef(e/h)=1e4, RHSMin=1e-3, Transient=BE, ExtendedPrecision(80), TensorGridAniso(aniso), Method=Blocked, SubMethod=ILS(set=22)
  - ILS(22): gmres(100), tolrel=1e-10, tolunprec=1e-4, maxit=200, ilut(1e-8,-1)
  - Solve: Poisson-only Coupled Iterations=500 LineSearchDamping=1e-2; full Coupled Iterations=100
  - Transient: InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Goal anode=5.0 V
- **중요:** 현재 slow run의 Transient step-control은 이전에 확인한 값과 동일하므로 step-control 변경만으로 slowdown을 설명할 수 없음.
- **가장 먼저 검증할 것:** 현재 slow Node 6의 trap `Conc`가 0인지 1e18인지 확인. old deck은 명백히 NtSide=0 케이스이므로 current가 1e18이면 직접 runtime 비교가 공정하지 않음.
- **그 다음:** current full `pp6_des.cmd`의 Physics/Math와 old deck을 diff하고, old/current mesh statistics 비교.

---


---

## 2026-09-28 — 1차 수정 Baseline NtSide I–V 비교 및 동일-current 기준 전압 추출

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Preliminary baseline validation / same-current comparison
- **상태:** CONFIRMED (SVisual curve + Tcl extraction)
- **대상:** 1차 수정버전 Baseline, NtSide=0 (dataset n6) vs NtSide=1e18 cm^-3 (dataset n12)
- **관찰:** 동일 applied voltage에서 NtSide=1e18의 forward current가 NtSide=0보다 낮음. 따라서 5 V SRH map을 단순 비교하면 injection-level 차이가 섞임.
- **동일 current 기준 선택:** I = 2e-11 (Sentaurus raw 2D TotalCurrent)
- **Tcl ExtractVti 결과:**
  - NtSide=0: V = 4.928 V
  - NtSide=1e18: V = 4.979 V
  - ΔV ≈ +0.051 V for NtSide=1e18 at the same raw 2D current
- **해석:** sidewall trap 활성화 케이스가 같은 current를 만들기 위해 더 높은 anode voltage를 요구함. 이 결과는 1차 수정버전의 preliminary electrical effect이며 Final Baseline 검증 완료를 의미하지 않음.
- **다음:** 동일 injected current 상태의 2D SRH/Radiative 비교가 필요. 현재 저장된 TDR이 5 V 상태만 포함한다면 해당 bias에서 별도 Plot/Save 또는 재실행 필요.


---

## 2026-09-28 — Final SDevice v1.2: intermediate TDR 저장 추가

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** TCAD code update / output-save control
- **상태:** CONFIRMED (user-provided Final SDevice v1.1 기반 수정)
- **변경 범위:** Physics / trap / solver / 0→5 V ramp는 그대로 유지하고, Transient 내부에 visualization-only `Plot(-Loadable ... NoOverWrite Time=(...))`만 추가.
- **목적:** I–V에서 동일 injected current에 해당하는 각 case의 voltage를 추출한 뒤, 해당 bias에 가까운 2D SRH / Radiative / carrier / band map을 비교할 수 있도록 중간 spatial state 저장.
- **저장 t 값:** 0.80, 0.84, 0.88, 0.92, 0.94, 0.96, 0.97, 0.98, 0.985, 0.99, 0.995.
- **0→5 V linear goal 기준 대응 전압:** 4.0, 4.2, 4.4, 4.6, 4.7, 4.8, 4.85, 4.9, 4.925, 4.95, 4.975 V.
- **5.0 V:** 기존 `Plot="@tdrdat@"` 최종 TDR을 사용하므로 중복 intermediate 5 V 저장은 생략.
- **중요:** 현재 이미 약 2일째 실행 중인 Final run은 중단하지 않음. v1.2는 다음 NtSide/A-B run부터 적용.
