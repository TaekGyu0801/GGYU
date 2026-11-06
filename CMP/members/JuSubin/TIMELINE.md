## 2026-11-06 — 4차 발표 최종 PPT 수정: 교수 요구사항 반영, 실제 Raw Data 우선 (PRESENTATION ONLY)
- 작업자: 주수빈; AI: ChatGPT; 상태: OBSERVED 기존 학교 실행 데이터 재사용 + PRESENTATION EDIT. **신규 학교 코드/실행/결과 없음**.
- 사용자 제공 교수 요구사항: 첫 번째 또는 두 번째 장에 Baseline 구조·층별 두께·도핑·Trap·전기적 값의 표, 실제 SDE/SVisual/Mesh/Raw Plot만 사용, AI 모식도/임의 가공 그래프 사용 금지, 실제 TCAD 캡처 없으면 해당 자리 안내문, Project A/B는 향후 원본 결과 입력용 공백 유지.
- 최종 17장 채팅 산출물 `CMP_4차발표_교수님요구사항_최종수정_주수빈.pptx` 제작. 3차 발표 디자인(미색 배경, 남색/청록 글꼴·강조) 유지. 슬라이드2에 현재 학교 `CMP_WU_Copy` **Wu-inspired 10µm PILOT** 구조/파라미터 표 및 5V 원본 terminal(raw 2D) 수치(n21 OFF Ie1.695e-4, Ih2.399e-3, Itot2.569e-3; n25 ON Ie1.690e-4, Ih2.397e-3, Itot2.566e-3). 2D raw 값을 실제 pixel 전류 또는 J로 단정하지 않음. EBL0 nm/pGaN120nm, trap Et/sigma는 pilot, 최종 정량 Baseline 아직 미확정으로 명시.
- 슬라이드3~5 Kou 4µm representative epi + Wu 5nm localized damage 혼합 모델에서 Wu 10µm 별도 PILOT으로 재설계한 역사적 출처 및 차이 유지. 논문 혼합이 과거 수치 오류의 검증된 원인이라는 오해 방지.
- 슬라이드6~8 실제 n1_msh.tdr, n21_des.tdr, n25_des.tdr의 Geometry/Doping/Recombination/Trap 콘투어 캡처 위치·파일명·변수 안내로 구성. 슬라이드9 인공 막대그래프 제거 → 실제 n21/n25 .plt SVisual I–V 캡처 자리 및 실제 5V 로그 원시 전류 2개로 대체.
- 슬라이드10은 실제 저장된 5V 12개 QW 분할 영역 Field Integration 적분값을 표기: OFF Radiative9.902518e15/SRH6.102184e14/Auger4.442221e15, ON Radiative9.869850e15/SRH6.086824e14/Auger4.424524e15 [s^-1 um^-1]. 동일 V이나 I 차이 있고 explicit eGap trap term이 포함되지 않은 전체 IQE는 미확정임을 표시. OFF/ON 실제 SVisual Field Integration 이미지 삽입 자리 확보.
- Project A/B 12/13/15/16장은 페이지명 외 **내용 없음**. 최종 파일 내 사진 객체 및 embedded image **0개**; 실물 학교 TCAD 사진은 제공되지 않아 의도적으로 미삽입. 총 17장, 16:9, PowerPoint/한쇼 편집 가능. 자체 슬라이드 렌더/오버플로 검사를 통과함.
- 저장 위치: 채팅 downloadable PPTX와 미리보기 PNG; GitHub에는 PPTX 바이너리를 업로드하지 않음. 발표 수정을 넘는 공통 Baseline/학교 코드 변경 없음.
- NEXT: 학교 SVisual에서 실제 원본 캡처를 가져와 자리 교체; 후속 Project A/B 파라미터 확정 후 연구자가 빈 페이지 작성.

## 2026-11-06 — 주수빈 EBL=0nm의 최종 Baseline 여부·EBL-free 물리적 타당성 검토 (READ-ONLY)
- 사용자 질문: '지금 우리 최종 baseline 구조가 EBL=0nm야?? Micro-LED에서 EBL 층이 없어도돼?'.
- GitHub 최신 확인: 활성 학교 `CMP_WU_Copy`의 이전 실제 `pp1_dvs.cmd` 관측값 `tEBL=0.000µm`은 **Wu 기반 10µm 작업용 pilot의 임시 설정**으로 확인됨. 원본 Wu 2023 출판사 공개 설명에서 EBL 유무·두께가 확인되지 않았으므로 'Wu 논문 EBL=0'으로 표현 불가. **최종 scientific baseline 미확정**.
- 별도 보호된 `CMP/COMMON_BASELINE.md`는 Kou vertical epitaxy 기반 4µm representative hybrid 구조로 **p-Al0.15Ga0.85N EBL=26nm**를 규정. 현재 학교 Wu 10µm pilot이 이 protected baseline을 자동 대체하지 않음.
- 문헌 확인(2026-11-06): `Wu et al. 2023` DOI 10.1016/j.micrna.2023.207542 공개 본문에서 Fig1 EBL 불명. EBL-free microLED 자체는 문헌에서 가능; blue low-current microLED without EBL experimental Zheng et al. Opt Express 2025 DOI 10.1364/OE.549908에서 peak EQE 32.8→34.6% at 0.4 A/cm2 보고(다른 소자); IEEE TED 2024 DOI 10.1109/TED.2024.3478197 also low-J EBL-free efficiency/hole injection improvement in a modeled device. 다른 연구의 효과를 현재 CMP 성능으로 전이하지 않음. EBL removal은 구조에 따라 hole injection 개선 또는 electron overflow 증가를 야기할 수 있으므로 범용 최적값 아님.
- 제안: 발표에는 'EBL 0nm (Wu 모델 임시 설정, 원문 Fig1 미확인)' 표기, Wu 논문 그림 확인 전 Kou의 26nm EBL을 기계적으로 이식하지 않고 기존 Wu pilot 수치·결과 보존. 충분한 근거 없이 EBL 미포함 구조를 final 확정이라고 표현하지 않음. 실험·코드·baseline status 변경 없음.

## 2026-11-06 — 주수빈 4차 발표 PPT 수정: 기존 Kou+Wu 혼합 출처 문제로 서술 교체 (PRESENTATION EDIT ONLY)
- 작업자 주수빈 / AI ChatGPT / 상태: OBSERVED 문헌·기록 기반 서술, PRESENTATION REVISION. 신규 연구 판단 확정 또는 TCAD 실행 아님.
- 사용자 요청: 앞선 발표용 17장 PPT의 '수정 전 문제=Mg 도핑 인식 오류' 서술을 삭제하고, 실제로 이전 4µm CMP Baseline이 **Kou 2019 수직 에피(4×In0.15 QW3nm, GaN QB22nm, AlGaN EBL26nm, nGaN4µm) + Wu 2023 양측 측벽 5nm acceptor-like damage**를 결합한 대표 가정 모델이었다는 내용을 명확히 넣음. 기존 4µm Mesa는 대표 모델 선택이지 Kou 논문 내 4µm Mesa가 아니며 Kou 실제 chip 20/60/100µm.
- 수정된 slide4: 3차 Kou+Wu 혼합 4µm 구조 vs 4차 Wu-inspired 10µm 별도 모델(In0.08 QW3nm×4, QB8nm×5, EBL 0nm pilot)의 수치를 대칭 비교함. 실제 SVisual 이미지 삽입 상자 유지.
- 수정된 slide5: Kou vs Wu 원문에서 가져온 설계 조건과 기존 4µm hybrid 구성, 새 Wu source-grounded pilot 전환을 두 카드와 하단 요약으로 표현. 기존 MgFix 5V 전/후 전류 서술 및 수치 모두 이 슬라이드에서 제거.
- **과학적 한계:** 두 논문의 수치 혼용은 문헌 혼합/정량 검증 부족에 따른 독립 Baseline 재설계 동기이지만, 그 혼합이 과거 solver/전류/QW4 문제의 **확정된 원인이라고 실험적으로 입증되지는 않음**. 새 Wu 모형도 pGaN/EBL/전극 등 Wu Fig1 완전 재현 미검증이며 working PILOT 상태.
- Project A/B의 위치·파라미터 페이지는 제목 외 비워둠, TCAD SVisual 그림 삽입 안내 유지. 3차 발표의 미색·남색·청록 디자인 유지. 수정 결과 17장 PPTX 파일 `CMP_4차발표_Wu_Kou_혼합문제_반영_주수빈.pptx`를 이 채팅에서 제작했고 렌더링 및 overflow 검사 통과. GitHub에는 PPT 바이너리 저장하지 않음.
- 근거: `CMP/COMMON_BASELINE.md`, `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`, 2026-11-03 JuSubin 프로젝트 내 대화/TEAM_TIMELINE, 현재 Wu school 모델 기존 관측 기록.
- 코드/시뮬레이션/검증 상태 변경 없음.

## 2026-11-06 — 4차 발표 PPT 내 인공 소자 그림 제거 및 실제 TCAD 캡처 위치 안내
- 작업자: 주수빈; AI: ChatGPT; 상태: PRESENTATION UPDATE (PROPOSED layout, not new TCAD observation).
- 직전 17장 `CMP_4차발표_3차디자인통일_Baseline변경과정추가_주수빈.pptx`의 4·6·8장에 코드로 그렸던 **설명용 소자 단면도·측벽 그림을 모두 삭제**하고 편집 가능한 실제 TCAD 이미지 삽입 안내 텍스트 상자로 교체함. 전체 슬라이드 17장과 3차 발표 기반 미색/남색/청록 디자인, 측정 수치, Project A/B 빈 슬라이드는 유지.
- 4장: 3차 실제 4µm Full/Half-Mesa SVisual Geometry/Mesh 캡처와 Wu `CMP_WU_Copy/n1_msh.tdr` 10µm Geometry/DopingConcentration 전체 화면.
- 6장: 같은 Wu `n1_msh.tdr`에서 전체 구조(X 적층 전체, Y=0..10µm)와 QW1–4·좌측 5nm 측벽 확대(Y≈0..0.02µm) 두 컷 삽입 권장.
- 8장: 실제 `n21_des.tdr`(Trap OFF), `n25_des.tdr`(Trap ON) `TotalTrapConcentration` 좌측 DmgL_QW1–4를 동일한 배율·영역·색상 범례로 나란히 캡처하여 교체하도록 안내함.
- 제공 파일: `CMP_4차발표_TCAD실제이미지_삽입안내_주수빈.pptx`; PowerPoint 17장, 삽입된 사진 오브젝트 0개, 슬라이드 렌더링으로 가독성 확인. 아직 실제 학교 TCAD 이미지가 PPT에 삽입된 것은 아님. 기존 계산/코드 또는 Baseline 상태 변화 없음.
- 다음: 사용자가 실제 학교 화면에서 캡처해 안내 위치에 붙여넣고 설명 안내문 삭제.

## 2026-11-06 — 4차 발표 PPT Baseline 변경 전후 2장 추가 (주수빈, PRESENTATION ONLY)
- 작업자: 주수빈; AI: ChatGPT; 상태: OBSERVED source data used in draft / PPT revised; 새로운 TCAD 실행·코드 변경 없음.
- 사용자 요청에 따라 3차 발표 PPT와 동일한 미색/남색/청록색, 편집 가능한 소자 개념도, 간결한 수치 카드 형식을 유지하고 기존 15장 → 17장으로 수정.
- 신규 슬라이드 4: 3차 당시 4µm mesa/2µm half/AlGaN EBL/4QW와 현재 학교 Wu-inspired 10µm full 2D stripe/EBL0nm(pilot)/4×3nm QW를 별도 모델로 구분. 3차 발표 출처의 5V OFF raw 전류1.448e-11 및 QW 3항 방사비율0.1095% 기재. **서로 다른 모델이므로 직접 인과 비교 금지** 안내.
- 신규 슬라이드 5: 동일 Wu model의 Mg 도핑 인식 문제 전후를 비교. 입력 MgActive=2e19 cm^-3 유지, 원래 pGaN net Doping≈0 → project-local datexcodes GaN Mg acceptor mapping/SDE rerun 후≈-2e19 cm^-3(메시 표시). 기존 pre-fix OFF n21 5V raw Total=2.884e-5, Hole=3.696e-27 → post-fix OFF n21 5V Total=2.569e-3, Hole=2.399e-3. 두 런 모두 로그/메시 관측 근거 존재. raw 2D 출력, 절대 전류밀도 미검증.
- 유지: Project A/B의 적용 위치·설계 수치 페이지는 제목 외 본문 없음. 현재 Wu 모델은 working pilot이며 저J 광학 IQE 및 final common baseline 검증은 미완료.
- 산출물: 채팅 다운로드용 PPTX `CMP_4차발표_3차디자인통일_Baseline변경과정추가_주수빈.pptx` / 전체 17장 렌더링 확인. GitHub repository에 PPTX 바이너리 저장하지 않음.
- 다음: A/B 위치와 수치 실제 합의 후 발표 슬라이드를 사용자가 직접 채움.

## 2026-11-06 — 4차 CMP 발표 PPT 초안 제작 (주수빈, PRESENTATION ONLY)
- 작업자: 주수빈; AI: ChatGPT; 상태: PROPOSED / 발표 문서 생성, 신규 TCAD 실행 없음.
- 사용자 제공 3차 발표 PPTX 형식(미색 배경·남색 타이틀·청록색 강조·중앙 구분 슬라이드)을 참고하여 수정 가능한 15장 4차 발표 PPTX를 채팅 산출물로 제작함.
- Baseline 파트: 현재 활성 Wu-inspired 10µm CMP_WU_Copy 작업용 pilot 구조/주요 치수, Trap OFF/ON 조건, 2026-11-06 기존 C1 동일 J IV 보간 ΔV 수치를 시각화. 저J 광학 IQE와 최종 검증은 미완료임을 명시.
- Project A/B 파트: 목차, 섹션 구분 및 적용 위치/방식·설계 파라미터 제목의 **빈 슬라이드만** 준비함. 위치·수치·기구를 **확정하거나 기입하지 않음**. 향후 연구원이 직접 채울 예정.
- 초안은 사용자가 제공한 기존 PPTX 기반의 별도 채팅 다운로드 파일이며 GitHub에 바이너리 PPTX는 올리지 않음. 학교 SDevice/메시/코드 및 물리적 Baseline 결정 변경 없음.
- 다음: A/B 설계 위치 및 수치 합의 후 비어 있는 PPT 슬라이드에 사용자가 직접 내용을 추가하거나 요청 시 반영.

## 2026-11-04 JuSubin measured n25 central QW carrier radiative CSV — OBSERVED / DERIVED (physical root cause still UNRESOLVED)
- Worker **주수빈** executed a single-line awk read-only analysis of saved `CMP_WU_Copy/WU_n25_C1_QW_carrier_rad.csv` from the `n25_des` Trap ON, 5 V, central Y≈5um C1 cutline. Reported samples `QW1 N=3 eMean=1.572e19 hMean=2.857e16 RadMean=3.611e25 npMean=1.806e35`; `QW2 N=4 e=2.053e19 h=1.089e18 Rad=8.874e25 np=4.437e35`; `QW3 N=3 e=3.644e19 h=3.712e18 Rad=1.812e28 np=9.062e37`; `QW4 N=4 e=5.493e19 h=1.874e19 Rad=2.150e29 np=1.075e39`. e/h units cm^-3, Radiative cm^-3 s^-1, np cm^-6; averages are simple **sample means on one line** not 2D integrals/area-averaged rates or IQE.
- Derived `QW4 / QW3`: e=1.507x, h=5.048x, np=11.863x, radiative=11.865x. Derived per-QW `RadMean/npMean` ≈2.00e-10 cm^3/s for all four wells (empirical effective B in these four local samples, **not yet independently verified against pp25_des.par**). The local radiative hierarchy follows local electron–hole product; do NOT multiply separately averaged e and h to reproduce npMean (covariance).
- Earlier independent n21 **Trap OFF** saved 12-QW integrated Radiative has QW4 ≈91.03% share; n25 Trap ON 12-QW Rad also ≈91.10%. Thus QW4 weighting already exists when explicit sidewall Trap is OFF and should NOT be attributed to NtSide ON without independent evidence. Carrier-accumulation **proximate numerical explanation** found, but physical root cause of high n-side QW4 holes, transport/band offsets/polarization/recombination model and Wu fidelity remain UNRESOLVED.
- NEXT: preserve both saved datasets, compare **central Y=5um n21 OFF** eDensity/hDensity with n25 ON using same exact QW regions and optionally examine saved band-edge/quasi-Fermi cutlines. Do not modify active model or rerun canceled hGap. No new SDevice execution and no source changes.

## 2026-11-04 JuSubin multiline AWK csh unmatched quote analysis attempt (OBSERVED COMMAND ERROR; NO DATA LOSS)
- Worker 주수빈 attempted multiline `awk -F, '` in school `CMP_WU_Copy` while analyzing already-exported `WU_n25_C1_QW_carrier_rad.csv`. Interactive csh/tcsh command input returned `Unmatched '.`, `NR: Command not found`, and `if: Expression Syntax` with continuing `else?` prompt; AWK script did not run and NO per-QW numeric results were produced. Existing CSV/TDR and completed n21/n25 remain unchanged as far as the supplied transcript shows.
- FIX (PROPOSED, not yet user executed): press Ctrl+C to terminate `else?` continuation, then paste a **single physical line** `awk -F, 'NR>2 {x=$1+0;q=(x>=.128&&x<.131)?1:(x>=.139&&x<.142)?2:(x>=.150&&x<.153)?3:(x>=.161&&x<.164)?4:0;if(q){n[q]++;e[q]+=$2;h[q]+=$3;r[q]+=$4;np[q]+=$2*$3}}END{for(q=1;q<=4;q++)if(n[q])printf "QW%d N=%d e=%.3e h=%.3e Rad=%.3e np=%.3e\\n",q,n[q],e[q]/n[q],h[q]/n[q],r[q]/n[q],np[q]/n[q];else printf "QW%d NO_DATA\\n",q}' WU_n25_C1_QW_carrier_rad.csv` (show in chat as one line). This only reads CSV; it does not run Sentaurus or edit code.
- NEXT obtain resulting 4 QW lines, avoid claiming actual result before observed. Prior no-hGap-rerun decision remains.

## 2026-11-04 — JuSubin n25 central C1 CSV export verified (OBSERVED / QW NUMERICAL ANALYSIS PENDING)
- 작업자 주수빈 학교 CMP_WU_Copy에서 SVisual Export XY Data 변수 `X,eDensity,hDensity,RadiativeRecombination`를 `WU_n25_C1_QW_carrier_rad.csv`로 저장한 뒤 직접 터미널 `head -n 12 WU_n25_C1_QW_carrier_rad.csv` 결과를 제공함. CSV header 정확히 네 변수, 두 번째 행 `none,none,none,none`(수치 아님; 분석시 제외), 첫 수치 행 X=0, 뒤 X=.0318125..0.12um etc. X~0.12 이하 시작 부분은 QW 비교 범위가 아니라 p측/Barrier0 영역에 해당함. 전체 CSV는 아직 직접 확인하지 않았으며 QW별 e/h/Rad 피크/평균값은 미측정.
- NEXT (READ-ONLY): 저장된 CSV에서 QW1 X=[.128,.131), QW2 [.139,.142), QW3 [.150,.153), QW4 [.161,.164) 샘플 각각 n, mean(eDensity), mean(hDensity), mean(Radiative), max peak 및 n*p 비교. 1D 중앙 cutline의 평균/피크는 2D 영역 적분이나 IQE가 아님. 기존 n21/n25 저장/취소 hGap rerun 보존.

## 2026-11-04 JuSubin C1 Variables export four fields available (OBSERVED / EXPORT PENDING)
- 학교 SVisual `Export XY Data` > `Variables` 스크린샷에서 dataset `C1(n25_des)` 확인. Available Variables에 `X`, `eDensity`, `hDensity`, `RadiativeRecombination`이 보이는 것이 확인됨. `Variables to Export`는 아직 비어 있음; 파일/CSV 저장이나 QW별 수치 추출은 아직 수행되지 않음.
- NEXT: 네 변수를 오른쪽으로 전송하고 Export 버튼으로 저장 형식 확인 후 중앙 Y≈5 um cutline 데이터만 저장하여 QW1..4 정량 비교. TDR, 기존 n21/n25 solver 결과와 취소된 hGap rerun은 그대로 보존.

## 2026-11-04 JuSubin n25 C1 center hDensity QW peaks (OBSERVED / QUANTITATIVE CAUSE UNRESOLVED)
- Worker 주수빈 school SVisual screenshot: saved `CMP_WU_Copy/n25_des` Trap ON with central Y≈5um vertical X-directed cutline C1. Right panel `hDensity(C1(n25_des))` shows 4 narrow hole-density peaks at approximately X=0.129,0.140,0.151,0.162um corresponding to QW1–QW4. Horizontal plot X≈0.12–0.175um and log vertical scale.
- Visually, QW4 hole peak does not appear overwhelmingly larger than other QW peaks, but no numeric peak/region values or precise n*p product were extracted. Existing earlier eDensity C1 screenshot likewise shows 4 QW peaks. **Do not attribute ~91% QW4 radiative integration to holes alone, or infer IQE from these screenshots.**
- NEXT preserve same C1 and extract numerical eDensity/hDensity peaks or average values within all 4 QWs (Y=5um), with attention to logarithmic scale; ideally compare local radiative rate along cutline as well. No new solver or source changes; cancelled hGap rerun remains cancelled.

## 2026-11-04 — JuSubin n25 eDensity C1 X-axis zoom confirmed (OBSERVED / CAUSE NOT YET ESTABLISHED)
- 작업자 주수빈 학교 SVisual screenshot: saved `CMP_WU_Copy/n25_des` Trap ON에서 중앙 Y≈5 um C1 cutline의 `eDensity(C1(n25_des))` 그래프 X축이 이제 약 0.12–0.175 um로 확대됨. QW1,2,3,4에 대응하는 약 X=0.129, 0.140, 0.151, 0.162 um 주변에 전자 밀도 피크 4개가 시각적으로 나타남. 그래프는 로그 스케일이며 픽셀 이미지뿐이므로 각 피크 수치와 상대 피크 비율을 아직 정확히 추출하지 못함. QW4의 ≈91% radiative integrated share가 전자 농도 우세 때문이라고 결론 내릴 수 없음.
- 왼쪽 패널에는 `Legend Properties`가 표시되는데 범례를 선택했기 때문으로 보임. NEXT: Data Selection에서 같은 C1 dataset/plot의 `hDensity` 곡선을 열어 QW별 hole carrier 분포를 확인하고 필요 시 peak/cutline 수치 추출. No new solver, source edit or canceled hGap rerun.

## 2026-11-04 JuSubin n25 C1 centerline eDensity plot created (OBSERVED / QW1-4 NUMERICAL PROFILE UNRESOLVED)
- Worker 주수빈 shared school SVisual screenshot with `n25_des` Trap ON. A vertical C1 cutline is now placed at approximately **Y≈5 um** across the simulated X thickness `0..4.072 um` (left plot). The right panel `Cutline_Y Plot` displays `eDensity(C1(n25_des))` on a log scale vs X, but full horizontal chart range approx X=0..4.1 um compresses narrow MQW x≈0.128..0.164 um to leftmost pixels; no QW-specific carrier comparison can be read reliably.
- This screenshot is progress in read-only saved-TDR spatial diagnostics, not proof of QW4 electron injection mechanism. `hDensity` has NOT yet been added to this cutline plot; at present eDensity selected.
- NEXT set right 1D plot X range approx 0.12..0.175 um via SVisual Plot Properties/axis controls (click right plot then open Plot Properties to inspect); compare resolved QW1..4 eDensity spikes and then hDensity on same line. Preserve n21/n25, do not rerun canceled hGap.

## 2026-11-04 JuSubin SVisual n25 center hDensity viewport confirmed (OBSERVED / NUMERIC DISTRIBUTION PENDING)
- 작업자 주수빈 학교 Sentaurus Visual T-2022.03 스크린샷: `CMP_WU_Copy/n25_des` (Wu Trap ON) scalar `hDensity` 표시, **X 수직 적층 좌표 약 0.11–0.172 um**, **Y lateral 약 4.94–5.03 um**. 이전 Y=0–0.07 um 왼쪽 측벽 화면과 달리 중앙 Y~5 um 영역을 올바르게 보여주며 QW1–QW4 위치 범위를 포함함.
- 컬러바 출력 `hDensity (cm^-3)` 전 범위 약 1e-30부터 1.165e20까지로 매우 넓어 화면이 오렌지색으로 거의 균일하게 보여 QW별 정공 농도 우열 **판정 불가**. 이 이미지만으로 QW4 과집중의 원인을 정공/전자 주입 불균형이라고 결론내리지 않음.
- NEXT (READ ONLY) SVisual의 `Tools` 메뉴 실제 옵션 확인 → Y=5 um에서 X 축 방향 cutline(또는 해당 릴리스의 동등한 수치 추출)으로 hDensity의 QW별 분포 측정 → 같은 cutline에서 eDensity 비교. 학교 코드·솔버/저장된 TDR 수정 없음.

## 2026-11-04 JuSubin n25 hDensity SVisual screenshot left sidewall not center (OBSERVED / LOCATION CORRECTION)
- 작업자 주수빈 provided school Sentaurus Visual screenshot of preserved Wu `CMP_WU_Copy/n25_des`. Active scalar `hDensity (cm^-3)` selected; viewport axes **vertical X** approximately 0.12–0.17 um (MQW stack), **horizontal Y** approximately 0–0.07 um. The plot is therefore at the **left-sidewall edge** (DmgL from Y=0..0.005 um), NOT the intended central cut at Y=5 um.
- SVisual plot screenshot colorbar spans ~1e-30 to ~1.165e20 cm^-3; extreme log range and screenshot alone do not establish which QW has more hDensity, whether QW4 is carrier-rich or why QW4 accounts for ~91% of the previously integrated radiative field. The screenshot shows Elements=44842, Points=20434; mesh identity from title n25_des is displayed.
- Next: user should navigate via Plot Properties axes (if supported in GUI) to X ~0.120–0.172 um, Y ~4.95–5.05 um and examine central `hDensity` then `eDensity`, ideally via central constant-Y cutline/point probes rather than colorbar alone. **No code change or rerun**, canceled hGap rerun remains canceled. The displayed sidewall screenshot is a valid location-specific view, not evidence of central injection.

## 2026-11-04 JuSubin school Wu pp1 actual geometry 10um Cartesian stripe (OBSERVED; PHYSICAL FIDELITY / J UNRESOLVED)
- 작업자 **주수빈** supplied the actual school `CMP_WU_Copy/pp1_dvs.cmd` lines 1–140 via read-only `sed`. This effective preprocessed SDE code explicitly defines `Wm=10.0 um`, `Wdmg=0.005 um` per left/right side, `tP=0.120 um`, `tEBL=0.000 um` (no EBL), four `tQW=0.003 um` InGaN QWs (`xIn=0.08`), five `tQB=0.008 um` GaN barriers, and `tN=3.900 um` nGaN. Derived x-direction total thickness `Xend=0.120+4*0.003+5*0.008+3.900=4.072 um`. This **4.072 um is vertical thickness, not mesa diameter/width**.
- `seg-list` divides y from 0..10 um into left damage 0..0.005, clean 0.005..9.995, right damage 9.995..10.0; total damaged lateral-width share `2*0.005/10=0.001=0.1%`, NOT percentage of actual recombination loss. Geometry is explicitly **2D Cartesian stripe**; header explicitly states NOT measured 10 x 10 um square. Regionwise semiconductor damage (not dielectric replacement).
- Stack is p-side to n-side with QW1 nearest pGaN and **QW4 nearest nGaN**. Whole-width planar `anode` at x=0 and `cathode` at x=Xend are explicitly marked **provisional**; original Wu electrode geometry and EBL presence **unverified**. `PMgActive=2e19 cm^-3` assumes Wu nominal Mg maps to active species; actual ionized/free-hole concentrations unvalidated. `ND=5e18`, `NBg=1e15` background PILOT; local `tP` is PILOT, not Wu-verified. Wu 2023 width/epi claims in header are **source comments**, not independently verified against publication.
- Header `PROPOSED/UNRUN` is stale/inconsistent with previously directly observed n21/n25 completed logs, as already documented. `pp1_dvs.cmd` source geometry + n25 log `Grid=n1_msh.tdr` strongly support the intended 10 um stripe but direct saved-mesh geometric read would further corroborate mesh provenance.
- Scientific conclusion: **DO NOT treat Wu 10 um stripe as the project's protected 4 um Common Baseline** or convert raw 2D terminal current to physical 4 um LED A/cm2 without mapping out-of-plane width/contact area. Keep separate Wu 10 um physics-validation pilot; Common Baseline freeze **UNRESOLVED**, original Wu details unverified. Saved 5 V n21/n25 ON/OFF comparisons remain within-model numerical comparisons; trap-inclusive IQE, 2D current normalization, QW4 (n-side) 91% radiative concentration and carrier transport need further explanation.
- NEXT READ ONLY: inspect saved `n25_des.tdr` or `n21_des.tdr` QW1..4 spatial electron/hole carrier distributions (SVisual `eDensity`, `hDensity`, conduction/valence bands) for n-side QW4 dominance; compare source structure to Wu paper for pilot parameter validity; do not edit/rebuild source or rerun canceled hGap.

## 2026-11-04 JuSubin T2022 AreaFactor official definition (OBSERVED / J NORMALIZATION UNRESOLVED)
- 주수빈 학교 T-2022.03 sdevice_ug.pdf에서 pdftotext grep AreaFactor 문맥 출력(텍스트 2539-2544, 28835-28836). 공식 정의: global Physics AreaFactor는 currents 및 charges multiplier이며 1D/2D에서 모델에 빠진 공간 방향의 연장폭을 나타내는 데 사용 가능. 대칭 모델 부분 영역 보정에도 쓰이고 Electrode/Thermode AreaFactor와 함께 있을 때는 배율이 곱해진다. 2D 트랩 농도 계산에서는 Physics AreaFactor를 z 방향 폭으로 사용.
- 학교 n25_des.log의 실제 anode/cathode area factor=1은 별도로 앞서 검증했음. 그러나 실제 2D 외부 z-width, lateral device/contact dimensions 및 4um 원형 LED로의 물리적 전류 밀도 A/cm2 변환은 확인 안 됨. Previously observed same-bias n21/n25 raw current percentage (~0.0856%) is a within-model comparison only.
- NEXT READ ONLY: check school effective pp25_des.cmd complete global Physics for area scaling and SDE actual lateral width/contact extents; compare manual 2D units before converting raw current to J. Preserve completed outputs, no rerun and no school code changes.

## 2026-11-04 JuSubin Wu n25 actual electrode area factor 1 (OBSERVED; 2D current density STILL UNRESOLVED)
- Worker 주수빈 provided read-only school `bash -lc 'sed -n "215,270p" n25_des.log'` output from `CMP_WU_Copy`. Log "Default device parameters > Electrodes" reports `anode : 0.0000e+00 V (Ohmic), area factor : 1` and `cathode : 0.0000e+00 V (Ohmic), area factor : 1`. It also reports `Grid file: n1_msh.tdr`, `ModelParameters file: pp25_des.par`, `Current file: n25_des.plt`, `Plot file: n25_des.tdr`.
- This **confirms applied electrode area factor = 1 in saved ON run**, despite no explicit AreaFactor grep match in pp25 commands. It does **not** verify whether the terminal current uses A, A/um or another simulator reporting convention, nor does it convert a 2D cross-section to the physical 4-um mesa area. Prior n25 raw 5-V total current 2.56639709344131e-03 must not be labeled calibrated A/cm2.
- NEXT READ ONLY: retrieve exact installed T-2022.03 SDevice User Guide wording on 2D device terminal current units, electrode `AreaFactor`, and any out-of-plane depth convention. Then inspect actual active contact geometry and determine scaling before reporting J. No simulation or code changes; keep canceled hGap rerun canceled.

## 2026-11-04 — 주수빈: Wu n25 전류 정규화 설정 검색 (OBSERVED)
- 학교 출력에서 pp25_des.cmd:214와 n25_des.log:643–644의 eCurrentDensity/Vector, hCurrentDensity/Vector만 확인. 검색한 pp25_des.cmd/par와 n25_des.log에서 AreaFactor, CurrentUnit, 2D/dimension 일치 항목 없음. 전류밀도 Plot 항목만으로 단자 전류 환산/AreaFactor 기본값을 판단할 수 없음.
- 다음: n25_des.log 접촉 정보 확인 및 T-2022.03 2D 전류 단위 확인(읽기 전용). n21/n25 재실행·수정 없음.

## 2026-11-04 JuSubin T-2022.03 trap steady-state net recombination Eq529 (OBSERVED / DERIVED INTERPRETATION)
- 작업자 주수빈, 학교 설치 T-2022.03 SDevice UG `pdftotext -layout ... | sed -n "29105,29175p"` 직접 출력. Chapter 17 p.554 Equation (529): in stationary state, V-model, a trap with concentration N0 has Shockley–Read–Hall-form **net recombination** rate proportional to N0 × thermal velocities × electron/hole cross sections × (np - n_i,eff^2), divided by capture/emission occupancy denominator. This is the **trap-level net e–h-pair recombination law for its stated assumptions**, not instruction to sum distinct e/h trap rates as independent pair losses. Eq. (530) specifies capture-emission detailed balance. Text around p.553 distinguishes electron picture and hole picture (occupation complement and rate sign change).
- IMPORTANT limitation: Wu saved `pp25_des.cmd` declares PooleFrenkel, polarization and quasi-stationary bias sweep; Eq.529's simplified stationary V-model formula is not proof of the **exact net output accounting** for modified field-dependent emission or all model options. Conventional `SRHRecombination` lifetime contribution and explicit `eGapStatesRecombination`/missing `hGapStatesRecombination` must be interpreted from actual physical model and net balance before valid IQE claim; e/h capture channels should NOT simply be added as two full independent recombination-pair losses.
- Data status unchanged: OFF/ON 12-QW fixed 5V three-term Radiative/(Radiative+SRH+Auger) are diagnostic proxies (~66.2156%, ~66.2270%), not complete trap-inclusive IQE; 12-QW OFF eGap missing, ON hGap not output, matched-current scaling and whole-device accounting unverified. No new simulation or changes to school code/outputs. Existing canceled hGap rerun stays canceled.
- NEXT: stop repetitive manual snippets; check whether existing archived saved data and model allow defensible *limited* proxy publication labeling, and read-only validate 2D current normalization and QW4-dominated injection before baseline approval.

## 2026-11-04 JuSubin T2022 p555 local trap capture emission equations 531 532 — OBSERVED / NET PAIR ACCOUNTING UNRESOLVED
- Worker 주수빈 supplied read-only school `pdftotext -layout .../sdevice_ug.pdf - | sed -n "29175,29255p"` output. It directly identifies **T-2022.03 SDevice UG Chapter 17 p.555**, Local Capture and Emission Rates, electron conduction-band capture (Eq. 531), hole valence-band capture (Eq. 532), corresponding thermal/emission rate definitions, trap occupancy and detailed-balance conditions. Formulae show capture/emission dependence on carrier densities, cross-sections, thermal velocities, factors/parameters; `eXsection`/`hXsection` are nominal constant cross-sections with optional model adjustments.
- Important source distinction: manual explicitly states trap **occupancy computation is independent of trap concentration**, while trap charge comes from multiplying occupancy by trap concentration. Trap concentration alone does not imply a specific net recombination rate. Rates can be local for semiconductor traps or semiconductor-interface traps, while insulator-only traps without nonlocal connection are ignored (manual).
- Wu pp25 region traps `Acceptor Level FromValBand EnergyMid=0.75 Conc=1e18 eXsection=hXsection=1e-15 PooleFrenkel` are previously OBSERVED. Yet equations 531/532 are capture processes, not themselves the net trap-mediated electron–hole-pair loss or the rule for adding SRH/eGap/hGap. 2D current normalization, charge/carrier conservation, steady state, and trap-inclusive IQE are **still UNRESOLVED**.
- NEXT read-only check adjoining manual section for occupancy balance / net electron/hole trap processes and distinguish capture vs emission before any IQE denominator. Do not rerun canceled `hGapStatesRecombination` job; preserve school n21/n25.

## 2026-11-04 JuSubin local official T2022 trap capture-emission section located (OBSERVED / PENDING EQUATIONS)
- 작업자 주수빈; 학교 설치 T-2022.03 `sdevice_ug.pdf`에 `pdftotext -layout ... - | grep -n -m 20 -E "Local Capture and Emission Rates|Net Recombination Rate|Electron Capture Rate|Hole Capture Rate"` 명령 실행 결과를 제공. Table-of-contents 텍스트 774행은 Chapter 17 "**Local Capture and Emission Rates**"를 인쇄된 매뉴얼 p.555로 안내; 실제 본문 29180행 근방에 전환 설명, 29189행 trap occupancy 문맥, 29195행 "Local Capture and Emission Rates" 제목이 나타남. 관련 세부 내용의 수식은 아직 읽지 않음.
- NEXT READ-ONLY `pdftotext -layout "$p" - | sed -n "29175,29255p"` to inspect p.555 local capture/emission and trap-occupancy balance formulas. Check correct physical net e-h trap pair accounting vs SRH before any complete IQE. No code changes, solver reruns or hGap rerun authorization.

## 2026-11-04 JuSubin official T-2022.03 Traps p580 local capture emission excerpt — OBSERVED / rate accounting UNRESOLVED
- 작업자 주수빈 executed read-only local `pdftotext -layout .../sdevice_ug.pdf - | sed -n "30495,30545p"` in school CMP_WU_Copy. Direct footer: **Sentaurus Device User Guide, T-2022.03, p.580**, Chapter 17 "Traps and Fixed Charges / Visualizing Traps".
- OBSERVED manual defines `eGapStatesRecombination` and `hGapStatesRecombination` for **conduction-band and valence-band** trap-related recombination outputs, respectively; `TrappingRates` provides per-trap capture and emission processes (local, inelastic tunneling, elastic tunneling). For Acceptor/eNeutral, capture is electron capture; for Donor/hNeutral, capture is hole capture. The displayed interface-insulator-charge visualization note is general guidance, NOT proof that current Wu's `Physics(Region="DmgL/R_QW4")` uses an interface-trap model.
- BOUNDARY: this paragraph does NOT give a double-count-safe equation combining `eGapStates`, `hGapStates`, and ordinary SRH nor validate final IQE. Need investigate underlying net capture/emission balances and steady-state status, only then calculate proper pair-rate accounting. Existing n25 saved eGap only; canceled hGap rerun stays canceled.
- No code, simulations, plot data or school files changed. NEXT user read-only locate "Local Capture and Emission Rates" and related equations in authorized installed T-2022.03 PDF; keep n21/n25 as saved.

## 2026-11-04 — JuSubin T-2022.03 manual PDF text-tool availability 2026-11-04 (OBSERVED / READ-ONLY PREPARATION)
- Worker 주수빈 ran `bash -lc 'for p in pdftotext pdfgrep pdfinfo; do command -v "$p" || true; done'` from school CMP_WU_Copy and reported `/usr/bin/pdftotext` and `/usr/bin/pdfinfo`; no `pdfgrep` found on PATH.
- This enables read-only search of the previously located local T-2022.03 `sdevice_ug.pdf` using `pdftotext -layout ... - | grep -ni -C 5 -E "eGapStatesRecombination|hGapStatesRecombination|SRHRecombination" | head -n 120`. Actual manual text/results **not yet supplied**, so specific accounting rules, electron-vs-hole net trap rate, and final IQE remain UNRESOLVED.
- No school deck edits/simulation, no source manual upload. Keep previously canceled hGap rerun canceled and n21/n25 preserved.

## 2026-11-04 — JuSubin local T-2022.03 SDevice manual path confirmed 2026-11-04 (OBSERVED / STEP 2)
- Worker 주수빈 executed school `bash -lc 'find /user/tools/synopsys/sentaurus/T-2022.03 -type f -iname "sdevice_ug.pdf" 2>/dev/null | head -n 5'` and returned the actual installed document path: `/user/tools/synopsys/sentaurus/T-2022.03/tcad/T-2022.03/manuals/PDFManual/data/sdevice_ug.pdf`.
- This verifies on-school-host existence of the **T-2022.03 SDevice UG** (subject to file contents/version title check), not yet the meaning of SRH/eGapStates/hGapStates or net pair rate accounting. PDF not copied to GitHub (proprietary source).
- NEXT (READ ONLY): check availability of local `pdftotext`, `pdfgrep`, `pdfinfo` tools using `bash -lc 'for p in pdftotext pdfgrep pdfinfo; do command -v "$p" || true; done'`; then locate exact version-matched field definitions and infer only supported trap/SRH bookkeeping. No new solver run, deck change, or change to canceled hGap run.

## 2026-11-04 — JuSubin shell redirect for official T-2022.03 manual search 2026-11-04 (OBSERVED / RESOLVED COMMAND ONLY)
- 작업자 주수빈; 학교 `CMP_WU_Copy`에서 official `sdevice_ug.pdf` 위치 확인을 위해 `find /user/tools/synopsys/sentaurus/T-2022.03 -type f -iname 'sdevice_ug.pdf' 2>/dev/null | head -n 5` 실행을 시도했으나 터미널이 `Ambiguous output redirect.` 반환. This is consistent with csh/tcsh not accepting Bash-style `2>/dev/null`; actual default shell not independently verified.
- A shell-independent invocation `bash -lc 'find /user/tools/synopsys/sentaurus/T-2022.03 -type f -iname "sdevice_ug.pdf" 2>/dev/null | head -n 5'` was provided. User has not yet supplied output; PDF presence and version-specific trap accounting remain UNRESOLVED.
- No simulation started, code/file touched, or physical results changed. NEXT user terminal output, followed by read-only T-2022.03 e/h trap rate and SRH accounting check. Preserve n21/n25 and canceled hGap rerun.

## 2026-11-04 — JuSubin live Wu pp25 Physics/QW4 trap excerpt 2026-11-04 (OBSERVED / INTERPRETATION PENDING)
- 작업자 주수빈, 학교 `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`의 실제 `sed -n '1,48p;159,177p' pp25_des.cmd` 결과를 제공. Effective ON pp25: `Grid=n1_msh.tdr`, `Parameter=pp25_des.par`, 300 K, `DefaultParametersFromFile`, Fermi, Mobility(DopingDependence HighFieldSaturation), `Recombination(SRH Radiative Auger)`, `Piezoelectric_Polarization(strain)`, `IncompleteIonization(Dopants="MagnesiumActiveConcentration")`, `Thermionic`.
- OBSERVED `Physics (Region="DmgL_QW4")` and `DmgR_QW4`: `Traps((Acceptor Level FromValBand EnergyMid=0.75 Conc=1e18 eXsection=1e-15 hXsection=1e-15 PooleFrenkel))`. Earlier Lee independently grepped same parameter consistency in all 22 DmgL/R regions. This is an explicitly modeled 5-nm sidewall-region **bulk/volume trap**, not an interface-only `Physics(RegionInterface=...)` declaration; matching Wu paper physical interface assumptions is UNVERIFIED. Confirmed output setting does not establish net e/h trap recombination or IQE.
- IMPORTANT discrepancy: comment header says `PROPOSED/NOT RUN ON SCHOOL T-2022.03`, but earlier 2026-11-04 directly verified `n25_des.log` completed 5 V. Treat header as stale/misleading execution-status text, not as proof the pp25 deck was not run. File excerpt combines NONADJACENT line ranges (1–48 and 159–177); mid-stream `PooleFrenkel) ) }` alone is NOT evidence of syntax corruption.
- Version-matched T-2022.03 sdevice_ug.pdf is referenced in `CMP/references/TCAD_REFERENCE_INDEX.md` but NOT present in GitHub. 2022 Synopsys Training section 13 distinguishes bulk/interface traps and eGapStatesRecombination versus hGapStatesRecombination (https://ghzphy.github.io/Sentaurus_Training/sd/sd_13.html), not an exact local UG audit. Existing saved n25 Plot lacks hGap. NEXT READ-ONLY: obtain authorized local T-2022.03 official definitions and verify rate balance / net e/h pair accounting, then 2D current normalization and Wu fidelity; preserve n21/n25, do NOT restart canceled hGap run. No code edits, reruns, or model changes.

## 2026-11-04 — JuSubin CANCELLED overnight simulation proposal (REJECTED / NOT RUN)
- USER DECISION: "아니다 이건 하지 말자. 취소해줘ㅈ" — prior optional overnight `hGapStatesRecombination`-only ON rerun proposal is **CANCELLED**. Do not execute or schedule it, do not restart `n29`, and do not modify SDevice/SWB/code.
- ChatGPT had not run or scheduled any school-server simulation. Previously completed `CMP_WU_Copy` n21 OFF and n25 ON TDR/results remain unchanged.
- 2026-11-05 LeeTaekGyu handoff remains **read-only review of saved Wu outputs** and independent assessment of rate accounting/current normalization/physics; any future rerun needs a fresh deliberate user decision. The preceding overnight PROPOSED entry is superseded by this cancellation.

## 2026-11-04 — JuSubin overnight optional rerun proposal (PROPOSED / NOT RUN)
- 작업자 주수빈 asked what to leave running overnight before LeeTaekGyu resumes 2026-11-05. No new run or source modification has been performed by ChatGPT.
- RECOMMENDATION: only if school server's **actual successful post-MgFix** `CMP_WU_Copy` ON deck can be safely duplicated in a new SWB experiment (no overwrite of `n21/n25`): keep exact existing geometry/physics/solver, `NtSide=1e18 cm^-3`, `Vstop=5V`, and add **Plot output only** `hGapStatesRecombination` to the real SDevice code. Check new `pp*_des.cmd` contains the field and the job parses/advances before leaving. Source keyword corroborated by Synopsys Sentaurus training and historical user-guide entries; exact T-2022.03 current school deck is NOT yet supplied/verified in this chat.
- PURPOSE: complement observed `eGapStatesRecombination` with hole trap recombination; then independently validate e/h trap rate accounting, avoid double counting with SRH and only after that evaluate trap-inclusive IQE. ON rerun is highest-value optional night computation; OFF counterpart may be considered later, not necessary to start both blindly.
- DO NOT rerun `n29` NtSide1e17 blind; it previously failed near 2.42 V Newton/MinStep with root unresolved. Do not launch unrun GitHub Wu3.2 candidate blindly, or perturb protected Kou/CMP baseline. If safe output-only duplicate cannot be confirmed, preserve existing data and defer rerun.
- STATUS: PROPOSED, not executed. Previous user no-rerun preference applied to prior analysis; new overnight inquiry invites considering a deliberate additional run, but no user confirmation/execution yet.

## 2026-11-04 — JuSubin Wu n25 ON right damaged QW1 trap concentration verified (OBSERVED / DERIVED)
- USER SVisual `n25_des`, `TotalTrapConcentration`, `DmgR_QW1`: integral **1.500030e+01 [um^-1]**, domain **1.500030e-05 [um²]**; derived mean = (15.00030 / 1.500030e-5) um^-3 = **1.000000e6 um^-3 = 1.000000e18 cm^-3**. Direct local right-side damage QW1 concentration matches ON NtSide=1e18.
- PRIOR verified on same saved n25: `DmgL_QW1` =1e18 cm^-3, `Clean_QW1` =0. OFF n21 `DmgL_QW1` ~1 cm^-3 (negligible but nonzero) and `Clean_QW1` =0. Hence ON left and right damaged QW1 and clean center mapping confirmed; OFF right is NOT separately sampled and all 22 damaged regions NOT individually concentration-validated.
- Prior ON/OFF `eGapStatesRecombination` all 22 damaged regions: ON **4.18789439e13** vs OFF **4.26866644e-5 [s^-1*um^-1]** (same 5V, not identical terminal current). Strong sidewall electron gap-state term response. True trap-inclusive IQE NOT established because `hGapStatesRecombination` was not recorded and rate accounting/current normalization unresolved.
- USER DECISION remains no SDevice rerun. No school code/solver changes. NEXT: consolidate representative spatial trap validation and existing gap-state comparisons; if useful, inspect other saved region trap averages/read-only physics to establish full 22-region uniformity and source fidelity. Do not claim full final baseline validation.

## 2026-11-04 — JuSubin Wu n25 ON targeted TotalTrapConcentration integral confirms DmgL_QW1 NtSide=1e18 (OBSERVED / DERIVED)
- USER SVisual `CMP_WU_Copy/n25_des` Trap ON `TotalTrapConcentration` regionwise integration: `Clean_QW1` Integral **0.000000e+00 [um^-1]**, Domain **2.996991e-02 um2**; `DmgL_QW1` Integral **1.499996e+01 [um^-1]**, Domain **1.499996e-05 um2**. Both regions' combined Total Integral **1.499996e+01 [um^-1]**, Total Domain **2.998491e-02 um2**.
- DERIVED area-averaged DmgL_QW1 TotalTrapConcentration = (14.99996 um^-1)/(1.499996e-5 um2) = **1.000000e6 um^-3 = 1.000000e18 cm^-3** (1 um^-3 = 1e12 cm^-3). Clean_QW1 average=0. This matches programmed ON NtSide1e18 in the left damaged QW1 region versus no additional traps in the same-well clean QW1 region. This directly validates local region placement/concentration for these TWO sampled regions, NOT necessarily all 22 damaged regions. The previous broad-red TotalTrapConcentration screenshot is not sufficient alone for all-region validation; dopant-associated TotalTrapConc semantics elsewhere may differ.
- Already observed ON/OFF 22-damaged-region `eGapStatesRecombination` ON 4.18789439e13 vs OFF 4.26866644e-5 [s^-1*um^-1], strong ON electron gap-state activation. The current result is distinct verification of trap density in DmgL_QW1; neither result alone proves net nonradiative IQE loss, because hGapStates not saved and e/h rate accounting not validated.
- NEXT without rerun: if useful verify `DmgR_QW1` and `Clean_QW1` in ON, `DmgL_QW1` in OFF, and representative other damaged layer(s) for 22-region coverage. No code or SDevice rerun by user decision. Keep 5V matched-current, current-density scaling and total trap-inclusive IQE outstanding.

## 2026-11-04 — JuSubin Wu ON n25 TotalTrapConcentration SVisual screenshot (OBSERVED / VALIDATION PENDING)
- USER screenshot Sentaurus Visual T-2022.03 `CMP_WU_Copy` plot title `n25_des` (Trap ON, NtSide=1e18), selected scalar `TotalTrapConcentration`; visible legend max ~**2.100e19 cm^-3** (Range upper 2.1e19, unchecked Fixed), log-scale lower 1e-30, broad red fields and narrow QW stripes in left-edge crop Y≈0–0.32µm and depth X≈0–0.23µm. Previously OFF `n21_des` same field legend max ~**2.000e19 cm^-3** (upper 2e19; different autoscale). Difference 1.0e18 in DISPLAYED top-of-range matches NtSide magnitude but is NOT yet proof that the intentional traps occupy only sidewalls or that those maxima are at corresponding coordinates. Color displays are not directly comparable with different ranges; field may include other states, exact semantics not yet independently verified.
- NEXT NO RERUN: On saved `n25_des`, SVisual Field Integration `TotalTrapConcentration` for separately selected `DmgL_QW1` and `Clean_QW1`, record integrals AND Domain, compare each integral/area to derive region-average concentration and assess difference; optionally same OFF `n21_des`. Do not claim a specific numerical result before output. Keep previous 22-region eGapStates ON/OFF comparison separate. Existing SDevice runs and code unchanged.

## 2026-11-04 — JuSubin Wu OFF n21 TotalTrapConcentration SVisual screenshot (OBSERVED / INTERPRETATION UNRESOLVED)
- USER screenshot Sentaurus Visual T-2022.03 `CMP_WU_Copy`: plot title `n21_des` (Trap OFF, NtSide=0), selected scalar `TotalTrapConcentration`, color legend ~1.000e-30 to 2.000e19 [cm^-3] (range controls 0 and 2e19). Visible plotted near-edge crop lateral Y≈0–0.32um with device depth X≈0–0.23um; large p/n-related regions appear red, MQW stripes different colors. Since even OFF image shows broad 2e19-scale field, do NOT interpret its red areas as `NtSide=1e18` sidewall traps or call trap spatial localization verified. Source field semantic contributions and plotted color scale require read-only validation; incomplete-ionization trap/dopant interpretation is only a hypothesis.
- No ON `n25_des` `TotalTrapConcentration` screenshot yet; next inspect same scalar in ON with same viewport and fixed range, or use `eTrappedCharge` and source `pp25_des.cmd` regionwise `Traps` declarations as complementary checks. Existing ON/OFF eGapStates across all 22 damaged regions are already complete. No additional SDevice run or code modifications.

## 2026-11-04 — JuSubin Wu OFF n21 14 non-QW eGapStates integral completes all-22 ON/OFF comparison (OBSERVED / DERIVED)
- USER SVisual post-MgFix 5V `n21_des` (`NtSide=0`) `eGapStatesRecombination` 14 non-QW damaged GaN regions: **3.798444e-7 [s^-1*um^-1]**, total Domain **4.060046e-2 um2**. Raw per-region integral in order DmgL_Barrier0..4, DmgL_nGaN, DmgL_pGaN, DmgR_Barrier0..4, DmgR_nGaN, DmgR_pGaN = [1.932145e-9,1.778112e-9,3.728998e-9,8.145429e-9,9.929364e-8,6.561472e-8,9.432686e-9,1.932189e-9,1.775716e-9,3.729097e-9,8.135554e-9,9.929368e-8,6.561950e-8,9.432901e-9]. Printed regional sum 3.79844367e-7 (rounding consistent).
- Earlier OFF same field 8 damaged QWs **4.230682e-5**, Domain **1.200013e-4 um2**; OFF ALL 22 damaged regions **4.26866644e-5 [s^-1*um^-1]**. Earlier ON same 14 non-QW **3.950639e11**, same 8 damaged QWs **4.148388e13**; ON all 22 **4.18789439e13**. Total ON/OFF ratio approximately **9.8107792e17**; huge because NtSide OFF=0 yields near-zero eGapStates (NOT a ratio of LED efficiencies). All-22 eGap QW share ON99.05665%, OFF99.11016%; ON QW-dominant distribution and near-symmetric sides. All numbers compare same nominal 5V/regions/units, but 5V raw I differs ON2.566e-3 vs OFF2.569e-3.
- Scientifically observed: acceptor sidewall trap activation produces very large increase in explicitly plotted electron gap-state recombination term. NOT confirmed: net nonradiative loss or full trap-inclusive IQE; `hGapStatesRecombination` was not plotted, no current-matched field integrations or calibrated 2D current-density conversion, and Wu device source fidelity incomplete. Existing three-term MQW Rad/(Rad+conventional SRH+Auger) OFF66.215622% vs ON66.227019% may not count separate eGapStates. Do NOT add e+h naively or assert trap-induced IQE change from huge eGap ratio. Even illustrative single-additive ON full-22 eGap yield ~66.04144%, strictly NOT validated.
- USER DECISION: no SDevice reruns; previous hGapStates candidate Plot addition reverted. NEXT no-rerun review: check saved n21/n25 `TotalTrapConcentration` and `eTrappedCharge` maps for applied trap localization and consistency if useful, inspect source definitions/output terms, and prepare provisional result table with explicit limitations. Matched-current, hGap or trap-inclusive IQE remain UNRESOLVED.

## 2026-11-04 — JuSubin Wu n21 5V DopingConcentration integrated accidentally instead of eGapStates (OBSERVED / NEXT)
- USER SVisual `n21_des` Field `DopingConcentration` integration across ALL 33 2D regions (not the requested 14 damaged non-QW regions or `eGapStatesRecombination`), total integral **1.939846e8 [um^-1]**, total Domain **4.072000e+01 um2**. This is a **signed net doping field**; integrated total includes cancellation and must NOT be interpreted as trap recombination.
- OBSERVED polarity: `Clean_pGaN` negative integral -1.014793e6 on 1.1988 um2, `DmgL_pGaN` -5.078884e2 on 6e-4 um2, `DmgR_pGaN` -5.079001e2 on 6.000137e-4 um2; `Clean_nGaN` positive +1.948050e8 on 3.896100e+01 um2, each damaged nGaN ~+9.75e4; each GaN Barrier positive ~+79.9201 for clean and ~+0.04 for Dmg; all four Clean QWs and eight Dmg QWs 0. P/n sign and barrier/QW profile qualitatively consistent with earlier intended doping, but this does NOT alone validate active Mg ionization, free hDensity or complete LED physical fidelity.
- STILL PENDING: OFF `n21_des` `eGapStatesRecombination` integral across exactly **14 damaged NON-QW regions**: DmgL/R_pGaN, DmgL/R_Barrier0-4, DmgL/R_nGaN. User should change FIELD, reset region selection from 33, choose only 14. Then compare against same ON `n25_des` field/regions total **3.950639e11 [s^-1*um^-1]**, combine with previously measured 8 damaged QW subtotal. No SDevice rerun or code changes.

## 2026-11-04 — JuSubin Wu n25 ON 5V eGapStates all 22 damaged regions integrated (OBSERVED / DERIVED)
- USER SVisual `n25_des`, `eGapStatesRecombination`: 14 non-QW damaged GaN regions (`DmgL/R_Barrier0-4`, `DmgL/R_nGaN`, `DmgL/R_pGaN`) total **3.950639e11 [s^-1*um^-1]**, Domain **4.060046e-2 um2**. Region values [s^-1*um^-1]: L Barrier0 1.869949e9, B1 1.726971e9, B2 3.648867e9, B3 7.925232e9, B4 9.379776e10, nGaN 7.929615e10, pGaN 9.240180e9; R B0 1.869923e9, B1 1.724461e9, B2 3.648829e9, B3 7.915338e9, B4 9.388470e10, nGaN 7.927525e10, pGaN 9.240310e9. Sum from rounded per-region values 3.9506392e11, consistent with reported total.
- DERIVED non-QW subtotal decomposition: Barrier0-4 L+R **2.1801203e11** (55.184% of non-QW), nGaN **1.585714e11** (40.138%), pGaN **1.848049e10** (4.678%). Within barriers B4 alone L+R **1.8768246e11**, dominant non-QW barrier term.
- Earlier ON `n25_des` 8 damaged-QW eGapStates **4.148388e13 [s^-1*um^-1]**, Domain **1.200013e-4 um2**; OBSERVED sum over all 22 damaged regions (8 QW+14 non-QW), same bias/field = **4.18789439e13 [s^-1*um^-1]**, integrated Domain **4.07204613e-2 um2**. QW fraction **99.05665%**, non-QW **0.94335%**. This is partitioning OF THE EGapStates integral only, not 99% of total physical recombination nor proof of trap loss localized exclusively in QWs.
- PRIOR OFF `n21_des` same eight damaged QWs 4.230682e-05; ON eight damaged QWs 4.148388e13, ratio 9.80548e17; OFF 14 non-QW data not yet integrated. Reiterate `hGapStatesRecombination` not saved in either n21 or n25, user explicitly declines SDevice rerun. ON and OFF 5V raw currents differ slightly, absolute current/J normalization not validated. Full nonradiative trap-inclusive IQE UNRESOLVED. Three-term MQW 66.227019% (ON) vs 66.215622% (OFF) excludes separate gap-state accounting; do not call it final IQE.
- NEXT NO RERUN: OFF `n21_des` `eGapStatesRecombination` on identical 14 non-QW damaged regions, for complete ON/OFF comparison of all 22 damaged regions. Then inspect 5V spatial distribution/field signs and trap e/h net-rate definition if needed, review matched current and 2D scaling. Preserve existing code/results.

## 2026-11-04 — JuSubin Wu 5V OFF n21 vs ON n25 eGapStates 8 damaged-QW comparison (OBSERVED / DERIVED)
- USER SVisual OFF `n21_des` `eGapStatesRecombination` integrated **4.230682e-05 [s^-1*um^-1]** over DmgL_QW1–4 and DmgR_QW1–4 (eight 2D regions), total Domain **1.200013e-04 um2**; region integrals L: 7.304905e-7,7.087208e-7,5.836181e-6,1.387832e-5; R: 7.305117e-7,7.090642e-7,5.836364e-6,1.387717e-5 (same units). Region sum 4.23068222e-5 (reported roundoff).
- Same-regions post-MgFix ON `n25_des` observed earlier **4.148388e13 [s^-1*um^-1]** with same Domain. DERIVED ON/OFF ~**9.80548e17** (~18 decimal orders), OFF extremely small relative to ON but strictly nonzero. OFF per-well L+R QW1 1.4610022e-6, QW2 1.417785e-6, QW3 1.1672545e-5, QW4 2.775549e-5. ON per-well 1.3607449e12,1.3948305e12,1.1418713e13,2.7309600e13. The ON trap-associated electron-field contribution clearly responds strongly to NtSide change in damage regions at same 5V.
- LIMITATIONS: this eGapStates quantity alone is not independently validated net nonradiative loss or complete trap-inclusive IQE; `hGapStatesRecombination` was not saved. ON/OFF raw currents differ ON2.566e-3, OFF2.569e-3 at 5V, and 2D J normalization is unverified. Existing 3-term IQE (OFF66.215622%/ON66.227019%) excludes explicit trap accounting. Do not naively add e+h or label 18-order ratio as IQE decrease.
- USER PRIOR DECISION STILL STANDS: no new SDevice run or hGapStates Plot source change; previous GitHub candidate change was reverted. NEXT: in saved n25 integrate `eGapStatesRecombination` over all 22 trap-bearing DmgL/R_pGaN, Barrier0-4, QW1-4, nGaN regions (or 14 non-QW regions separately), preserve per-region signs, compare 8-QW subtotal; if useful, OFF n21 same regions. Then assess rate definitions and matched-current/2D normalization before final baseline interpretation.

## 2026-11-04 — JuSubin declines costly SDevice rerun; hGapStates candidate change reverted (DECISION / REJECTED)
- USER DECISION: `hGapStatesRecombination` 출력 추가를 위한 학교 SDevice 재실행은 시간이 많이 걸리므로 수행하지 않음. 학교 SWB SDevice 코드, 기존 `n21_des.tdr` 및 `n25_des.tdr` 그대로 보존.
- GITHUB REVERT COMPLETED: earlier proposed single Plot line `hGapStatesRecombination` addition to `CMP/tcad/candidates/CMP_BASELINE_3.2.0_WU2023PHY/sdevice_des.cmd` was removed, restoring original `eGapStatesRecombination eTrappedCharge TotalTrapConcentration`. Revert commit `c3fb0806a2961d65cdcc647a8ebeea76e4367999`. Previous GitHub proposal remains in history but is NOT active.
- NEXT WITHOUT RERUN: use saved 5V `n21_des` Trap OFF eGapStatesRecombination on the same eight DmgL/R_QW1-4 regions as ON; integrate existing `n25_des` eGapStates over all trap-bearing damaged regions (not only QWs); compare carefully with Radiative/SRH/Auger. Existing ON 8-damaged-QW eGapStates 4.148388e13 [s^-1*um^-1]. Missing hGapStates cannot be assumed zero; full trap-inclusive IQE UNRESOLVED; matched current/2D normalization still open. No new simulation/code change on school server.

## 2026-11-04 — JuSubin Wu hGapStatesRecombination Plot added to GitHub candidate (PROPOSED / NOT RUN)
- USER REQUEST: add `hGapStatesRecombination` to Wu SDevice saved output for proper trap electron/hole diagnostics.
- GITHUB CODE CHANGE DONE: `CMP/tcad/candidates/CMP_BASELINE_3.2.0_WU2023PHY/sdevice_des.cmd` `Plot` changed from `eGapStatesRecombination eTrappedCharge TotalTrapConcentration` to `eGapStatesRecombination hGapStatesRecombination eTrappedCharge TotalTrapConcentration` (ONLY single Plot line). Supported in Sentaurus trap plot output; no changes to Physics, Traps, Solve, NtSide or protected 4um baseline. GitHub commit `f457da1b5ad17ab080038e9813a748b791c64f7b`.
- IMPORTANT: SCHOOL SWB `CMP_WU_Copy` original source code cannot be edited by this GitHub action; generated pp21/pp25_des.cmd and saved n21/n25_des.tdr remain unchanged. In school SWB change SDevice source Plot in same way, preserve existing outputs (backup or run new nodes), then rerun SDevice for desired NtSide=0 and 1e18 outputs. Check new pp*_des.cmd Plot and SVisual field before analysis. Avoid modifying generated pp files. This is a `PROPOSED` school change, NOT a completed solver run.
- RATIONALE: user-provided pp21 and pp25 line219 both list eGapStatesRecombination but omit hGapStates. ON n25 8 damaged QW `eGapStatesRecombination` 4.148388e13 s^-1 um^-1; e/h field meanings/accounting and possible spatial trap contributions remain to validate. Do not add e+h blindly or assert final IQE.

## 2026-11-04 — JuSubin Wu n25 ON eGapStates 8-damaged-QW rate; pp25 Plot confirms h field absent (OBSERVED/DERIVED)
- USER SVisual `CMP_WU_Copy/n25_des` 5V post-MgFix Trap ON NtSide1e18: `eGapStatesRecombination` integration over exactly DmgL_QW1-4 and DmgR_QW1-4 (8 regions) gives **4.148388e13 [s^-1*um^-1]** with Domain **1.200013e-4 um2**. Sum of printed region values 4.14838884e13 (rounding consistency). QW1 1.36074490e12 (3.280%), QW2 1.39483050e12 (3.362%), QW3 1.14187130e13 (27.526%), QW4 2.73096000e13 (65.832%). L 2.07421544e13, R 2.07417340e13.
- OBSERVED user shell `grep -nEi 'GapStatesRecombination' /user/semi/semi437/tmp/myproject/CMP_WU_Copy/pp25_des.cmd` output line219: `eGapStatesRecombination eTrappedCharge TotalTrapConcentration`. Thus the current preprocessed ON `Plot` requests eGapStates but NOT hGapStates. Missing SVisual hGapStates field cannot be interpreted as zero trap-related hole recombination. No code changed/solver rerun.
- DERIVED ON 8-dmg-QW eGapStates 4.148388e13 is about 69.42 times 8-dmg-QW conventional srhRecombination 5.975499136e11; its magnitude is ~0.2784% of ON full-12-QW three-term recombination sum. The previously reported OFF 66.215622% and ON 66.227019% are only three-term proxies. If eGapStates were independent net loss added once, provisional ON estimate ~66.0432%; this is a CONDITIONAL illustration, not a validated trap-inclusive IQE. Need determine definition/sign/double counting and full damaged-region inventory (possibly beyond QW).
- NEXT: Check OFF n21 eGapStates integral in identical 8 QW regions if saved; then ON eGapStates over ALL trap-bearing sidewall regions to avoid MQW-only loss undercount. Read-only verify ON pp25 complete Trap region list and plot block, compare n21 pp21 eGapStates, and assess whether hGapStates additional field requires separate future run. Do not overwrite existing n25; matched injected current, 2D current density calibration and Wu source fidelity pending.

## 2026-11-04 — JuSubin Wu n25 ON 5V intrinsic SRH integrated; explicit trap gap-state gate identified (OBSERVED / DERIVED)
- New SVisual ON `n25_des` `srhRecombination`, same Clean_QW1-4,DmgL_QW1-4,DmgR_QW1-4: total **6.086824e14 [s^-1*um^-1]**, Domain0.1199999um2. PostMgFix OFF n21 corresponding total **6.102184e14**. ON vs OFF at 5V **−0.251713%**, not increased. Per-well QW1 −0.48757%, QW2 −1.33900%, QW3 −0.64292%, QW4 −0.15386%. Clean total ON6.080848183e14 vs OFF6.09606245e14 (−0.24958%). DmgL+R ON5.975499136e11 vs OFF6.122045823e11 (−2.39375%). These numbers are intrinsic `srhRecombination` **field** integrals, not yet verified explicit Trap recombination.
- IMPORTANT NEW METHODOLOGY GATE: Sentaurus trap examples/documentation list `eGapStatesRecombination` and `hGapStatesRecombination` separately as trap-associated electron/hole recombination fields. They must be checked on saved `n25_des.tdr` before attributing observed intrinsic SRH drop to damage physics, or interpreting old OFF 66.2156% three-term Rad/(Rad+SRH+Auger) as complete ON trap-aware IQE. Do not add electron+hole gap-state rates together (could double-count); inspect their signs and consistency, integrate separately by region, including all sidewall damaged pGaN/barrier/QW/nGaN regions when evaluating total trap loss, alongside 12 QW regions for MQW-only metric.
- NEXT: SVisual n25 eGapStatesRecombination and hGapStatesRecombination field existence/regionwise integration first (check if actual TDR Plot recorded); n25 AugerRecombination same 12 QW regions for baseline three-term ON metric; combine trap contributions only with explicit consistent accounting and read-only source model inspection. Current comparison only same 5V; raw currents ON2.566e-3/OFF2.569e-3, physical J normalization still open. No code changes/new runs in this turn.

## 2026-11-04 — Wu new ON n25 5V QW Radiative integration
- OBSERVED n25_des SVisual (NtSide=1e18 post-MgFix), same 12 Clean/DmgL/DmgR QW1-4 regions, Radiative total9.869850e15 s^-1 um^-1, region domain1.199999e-1 um2. OFF n21 same region Rad9.902518e15; ON-OFF -0.32990% at 5V. Raw I ON2.566e-3 OFF2.569e-3 (-0.1168% from rounded log), so currents NOT exactly equal.
- Per QW Radiative ON vs OFF: QW1 -0.140%, QW2 -1.305%, QW3 -1.066%, QW4 -0.2575%. DmgL+R QW Rad ON9.441488e12 vs OFF9.826764e12 (-3.921%), clean QW Rad -0.326%. This is NOT yet IQE or proof of SRH trap loss: ON SRH and Auger region integrals missing.
- NEXT ON n25 SRH then Auger same 12-region integration; calculate 5V ON IQE and sidewall losses, then matched-current analysis. No new code/run.

## 2026-11-04 ~01:49+ KST — Wu post-MgFix NtSide1e18 ON n25 5V normal finish VERIFIED, OFF/ON same-voltage current comparison (OBSERVED / DERIVED)
- WORKER 주수빈. New uploaded terminal output from school `/user/semi/semi437/tmp/myproject/CMP_WU_Copy` verifies `n21_des.log` modified 2026-11-03 23:58:02 KST; `n25_des.log` modified 2026-11-04 01:00:20 KST, `n25_des.tdr` saved 2026-11-04 01:00:20.7 KST (~7.6 MB). Therefore earlier concern over OLD pre-MgFix n25 output is superseded: this is post-MgFix fresh trap ON run, corroborated by restored 5V anode hole current.
- ON `n25_des.log`: 5.000V Bank/Rose converged error 1.1827e-03 (<1), `Curve trace finished`, `Writing plot 'n25_des.tdr' ... done`, `Sentaurus Device simulation finished` Wed 2026-11-04 01:00:20 KST; wallclock3690.63s (61min30s), CPU3307.13s, peak755MB. Anode electron +1.690e-4, hole +2.397e-3, total +2.566e-3 RAW native units, cathode total -2.566e-3. Earlier OFF `n21_des.log` 5V electron1.695e-4, hole2.399e-3, total2.569e-3 raw, final normal 23:58:02, QW 3-channel model IQE 66.2156%.
- DERIVED same-voltage raw current ON vs OFF `(2.566e-3-2.569e-3)/(2.569e-3)≈-0.11678%` from rounded displayed 4 significant digit log entries; this is NOT sidewall recombination loss or matched-current IQE difference. Must integrate ON 12 QW Clean_QW1–4 + DmgL_QW1–4 + DmgR_QW1–4 for Rad/SRH/Auger to quantify actual recombination, then compare at matched raw current/J. First verify trap sidewall concentration all intended regions; `pp25_des.cmd` grep head shows repeated Acceptor trap `Conc=1e18` with e/hXsection=1e-15, but head truncated; total count/locations not yet verified. OFF verified `Conc=0` for shown regions.
- PREPROCESSED Wu OFF: `pp21_des.cmd` global `Fermi`, Mobility DopingDependence HighFieldSaturation, Recombination(SRH Radiative Auger), `Piezoelectric_Polarization(strain)`, Mg IncompleteIonization, Thermionic; `pp21_des.par` `LatticeParameters {X=(0,0,-1),Y=(1,0,0)}` with *assumed Ga-polar up* documented as Wu-unverified pilot, hence not established Wu reproduction. n21 log contacts `area factor:1` for each terminal. This does not independently validate conversion from 2D native current to A/cm2. Note `pp21_des.cmd` header still claims 'PROPOSED/NOT RUN' (stale comment) although observed run completed; avoid treating comment as current execution status.
- NEXT: verify total ON trap `Conc=1e18` region count and unchanged physics/mesh, then ON `n25_des.tdr` SVisual radiative/SRH/Auger 12-QW regionwise integrals, compute 5V three-channel IQE; focus DmgL/R trap-induced SRH. 5V current differs ~0.12%, so same-5V is preliminary controlled comparison, matched-current evaluation for definitive conclusions. Audit 2D J normalization and source paper fidelity before final baseline. No server code edit or fresh run by ChatGPT; observation only.

## 2026-11-04 ~01:49 KST — JuSubin Wu post-MgFix Trap ON NtSide1e18 I–V plotted to 5V (USER REPORT + OBSERVED SVISUAL; new solver freshness UNVERIFIED)
- USER REPORT: "NtSide=1e18도 다 돌아갔어" while showing SVisual from `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`. OBSERVED screenshot: `BaselineData_26`, legend `NtSide=1e18`; forward I–V and derived width-normalized J–V extend visually to about 5V, steep current rise after ~3–3.5V, endpoint current visually order 2.5e-3 on label `Anode Current [A/um] (assumed)`; J axis explicitly `Width-normalized |J| [A/cm2] (assumed)`. Image alone does not prove this SVisual dataset reflects *new post-MgFix* trap ON run rather than cached or older preMgFix ON n25; exact 5V current, timestamp, Newton convergence/TDR and node mapping not in screenshot.
- Previous valid postMgFix OFF n21 5V log: anode total raw2.569e-3, model three-channel integrated MQW IQE 66.2156%. Do NOT compute ON/OFF current difference or sidewall efficiency loss from visual estimates, and DO NOT compare pre-MgFix old n25 log to new OFF n21. Current-density AreaFactor remains unknown.
- NEXT IMMEDIATE: user should provide `stat` modification times and `tail -n 45 CMP_WU_Copy/n25_des.log` and pp25 NtSide trap concentration to establish fresh post-MgFix ON 5V normal finish. Confirm n25_des.tdr current and acceptor/hDensity before regionwise SRH/Radiative/Auger 12 QW integrals. Compare at same injected raw current/J, not solely 5V.
- This turn: screenshot + user report only, no code edit or server run by assistant.

## 2026-11-04 — JuSubin Wu n21 preprocessed Physics grep confirms polarization/ionization statements (OBSERVED)
- User read-only shell grep on actual school `/user/semi/semi437/tmp/myproject/CMP_WU_Copy/pp21_des.cmd` and `pp21_des.par` for `PolAct|Piezoelectric|Polarization|AreaFactor|ElectricField|IncompleteIonization` returned: cmd:6 source comment 'Full polarization ON; orientation in sdevice.par'; cmd:28 `Piezoelectric_Polarization( strain )`; cmd:29 `IncompleteIonization( Dopants="MagnesiumActiveConcentration" )`; cmd:213 `Potential SpaceCharge ElectricField/Vector`. No matching `PolAct` or `AreaFactor` declaration in those two searched files.
- Interpretation OBSERVED: active preprocessed SDevice physics contains explicit strain piezoelectric-polarization and Mg incomplete-ionization declarations, and electric-field output (NOT proof of actual field magnitude/sign). Source comment alone cannot establish full spontaneous+piezo polarization magnitude, crystal orientation validity, or QCSE mechanism. AreaFactor absence in these two files does NOT prove native current unit/normalization; require run startup/file/geometry current-unit check and p-n polarity/crystal orientation in parameter file. Do not assume prior 4-um Baseline PolAct controls this Wu deck.
- Prior 5V corrected OFF QW integrated model IQE 66.22% and central e/h peak offsets remain observed, mechanism unresolved. Next read-only inspect pp21_des.cmd main Physics/Electrode/Math blocks, pp21_des.par lattice/orientation parameter definitions, and n21_des.log dimension/area factor metadata. Keep same OFF until review; ON remains future controlled split.
- No simulator rerun or code edit here.

## 2026-11-04 — JuSubin Wu n21 OFF overlay cutline eDensity/hDensity (OBSERVED; mechanism UNRESOLVED)
- SVisual user screenshot central C1 depth cutline Y≈5 um, post-MgFix NtSide=0 at 5V, x≈0.10–0.19 um, log concentration. User explicitly identifies BLUE=hDensity, RED=eDensity. Across four MQW wells, BLUE hole peaks lie consistently toward smaller x (p-GaN side); RED electron peaks toward larger x (n-GaN side). Both carriers have large sharp peaks in all QWs, reaching order 1e20 cm^-3 in QW4. Peak positions are visually offset; direct local wavefunction overlap, per-QW averages and mechanism are NOT established.
- Prior matched-volume QW integrals: MQW 3-rate model IQE≈66.22% at 5V, QW4 accounts for ~91.03% Radiative and ~95.42% Auger. Height of e/h peaks alone does not explain concentration of integrated rates. Material/heterojunction fields and polarization are hypotheses; actual active PolAct/Piezo switch in server preprocessed n21 SDevice must be verified before assigning mechanism. Single 5V high-density result does not validate Wu-paper reproduction.
- NEXT: read-only check active `pp21_des.cmd` and `pp21_des.par` for polarization, ElectricField, AreaFactor/current normalization; then compare QW e/h relative profiles, use matched-density/injection analysis and plan new post-MgFix trap ON only after physical gate. No new solver or code changes.

## 2026-11-04 — 주수빈 Wu MgFix OFF n21 중앙 hDensity Cutline 확인 (OBSERVED / 해석 잠정)
- SVisual screenshot: `CMP_WU_Copy/n21_des`, 5V post-MgFix, NtSide=0, central depth cutline C1 at Y≈5µm. hDensity log plot x≈0.10–0.19µm shows four narrow MQW peaks at x≈0.132/0.143/0.153/0.164µm, maxima roughly 4e19/6e19/7e19/1e20 cm^-3 (visual reading only, unverified point/region values). p-side x≈0.10µm ~1e18, n-side x≈0.18–0.19µm ~1e15–1e16, qualitative decreasing background away from MQW.
- Prior eDensity C1 also had four peaks, generally increasing toward deeper well; thus both carrier populations are appreciable around MQW and QW4 peak is largest in these 1D plots. However e/h peak spatial overlap, per-well averages, and causality of QW4 dominant Rad (91.03%) / Auger (95.42%) are NOT proven from peaks alone. Some concentrations near 1e20 cm^-3 merit physical/injection normalization review.
- Previous identical 12-QW-integral 5V three-channel model IQE=66.2156% (not Wu-calibrated); no new simulator run, code changes or quantitative extracted cutline table.
- NEXT: show eDensity and hDensity on same Y=5µm cutline with depth x≈0.12–0.17µm and log density axis; compare peak positions/overlap vs well boundaries. Audit AreaFactor/current density and lower-current injection conditions before new post-MgFix NtSide1e18 trap ON matched-current split.

## 2026-11-04 — Wu n21 central eDensity Cutline image
- OBSERVED SVisual `CMP_WU_Copy`, n21_des, C1 depth direction at lateral Y≈5 µm, logarithmic eDensity graph. Narrow peaks in MQW X≈0.12–0.17 µm approach order 1e20 cm^-3. The image lacks sufficient x-resolution for QW-specific values. No interpretation of cause established. NEXT zoom x=0.115–0.175 µm and inspect hDensity on same C1.

## 2026-11-04 — Wu MgFix n21 Trap OFF 5V Auger-integral / IQE (OBSERVED + DERIVED)
- SVisual same 12 QW regions: AugerRecombination integrated 4.442221e15 [s^-1*um^-1]. Prior Rad=9.902518e15, SRH=6.102184e14 in identical regions (all 5V, post-MgFix, NtSide=0).
- Calculated MQW three-term IQE 66.2156%, with SRH share4.0804%, Auger share29.7040%. QW1 48.13%, QW2 59.03%, QW3 73.27%, QW4 65.60%; QW4 hosts 91.03% of Rad and 95.42% of Auger, strong imbalance requiring e/h map interpretation.
- This is model-internal 5V recombination metric, NOT validated physical/Wu-paper IQE or current density. NEXT inspect QW e/h cutlines and current normalization; do not compare old preMgFix n25 ON with new postMgFix n21 OFF. New ON later at same physics and matched J. No code or new simulation.

## 2026-11-04 — JuSubin Wu MgFix OFF n21 5V QW Radiative integral received; two-channel ratio calculated (OBSERVED + DERIVED, AUGER PENDING)
- Worker 주수빈; supplied SVisual Field Integration of `RadiativeRecombination` on the same 12 QW regions (`Clean_QW1-4`, `DmgL_QW1-4`, `DmgR_QW1-4`) in `CMP_WU_Copy/n21_des`, post-MgFix NtSide=0, 5V. Reported `Total Integral=9.902518e15 [s^-1*um^-1]`, `Total Domain=1.199999e-1 [um^2]`. Printed 12-region sum 9.90251758326e15, agrees by rounding.
- Per-QW radiative sums derived (Clean+L+R): QW1 7.395981904e11 (0.00746879% of total), QW2 1.0810392696e12 (0.01091681%), QW3 8.860310308e14 (8.947533%), QW4 9.014665915e15 (91.034081%). Rad distribution highly concentrated in QW4; QW3+4 ~99.9816%. Cause unresolved (transport, field/polarization, carrier population etc.); NOT automatically a simulator bug.
- Earlier same exact 12 regions `srhRecombination` total reported 6.102184e14 [s^-1*um^-1], printed sum 6.102184495823e14. Derived two-channel `Rad/(Rad+SRH)` using printed sums: **94.1954364%**, NOT final MQW IQE: Auger integral and other physical validity not yet assessed. By QW (Rad/(Rad+SRH), Auger excluded): QW1 53.512385%, QW2 64.079656%, QW3 88.054062%, QW4 94.856956%.
- Combined DmgL+DmgR Radiative=9.82676356e12 (0.0992350% of total Rad), near their 0.1% MQW area fraction; NtSide=0 means no introduced sidewall trap effect claim. All rates have 2D integration units s^-1 um^-1, NOT absolute device photon rate.
- NEXT: integrate `AugerRecombination` on IDENTICAL 12 regions in same n21_des TDR (verify available field, units and sign); then compute QW IQE from Rad, SRH, Auger with matched regions. Check QW1-4 eDensity/hDensity/field to diagnose QW4 concentration and 2D current normalization. Keep old preMgFix ON n25 separate; only compare newly rerun ON once OFF validated. No new code or simulation executed this turn.

## 2026-11-04 ~01:xx KST — JuSubin Wu post-MgFix OFF n21 5V 12-region QW SRH integrals received (OBSERVED USER SVISUAL; distribution DERIVED)
- User supplied SVisual Field Integration for `CMP_WU_Copy/n21_des`, field `srhRecombination`, post-MgFix NtSide=0, final accepted 5V (confirmed by fresh n21_des.log). **12 QW regions**, Clean_QW1-4 + DmgL_QW1-4 + DmgR_QW1-4; reported Total Integral **6.102184e14 [s^-1*um^-1]** and Total Domain **1.199999e-01 [um^2]**. Local regionwise integral sum from printed digits 6.102184495823e14 (rounding agrees).
- Per-QW totals, adding Clean+L+R (derived from exact supplied printed values): QW1 6.425083825e11 (~0.10529% of sum), QW2 6.059848698e11 (~0.09931%), QW3 1.2020424023e14 (~19.69856%), QW4 4.887657161e14 (~80.09684%). QW3+QW4 ~99.7954% of MQW SRH integral; uneven QW injection/recombination requires inspection and is not proof of a defect alone.
- Damaged stripe L+R combined integral 6.122045823e11 (~0.10033% of total), similar to combined stripe area fraction ~0.1000% (stripes each ~1.5e-5 um2 per QW vs Clean ~0.02997 um2); with NtSide=0, this does **not** establish sidewall impact for Trap ON. Distinguish intrinsic SRH from parameterized sidewall traps, currently OFF.
- 2D integration units are `s^-1*um^-1` and should not be labeled as absolute per-pixel recombination without proper 3D depth normalization. Peak Radiative/SRH visual ratios cannot yield IQE. No radiative or Auger region-integral values yet; MQW IQE **UNRESOLVED**.
- NEXT: same 12 QW regions, identical 5V OFF TDR integrate `RadiativeRecombination` and `AugerRecombination` (if present, inspect output fields), then compute whole-MQW and QW-wise `Rad/(Rad+SRH+Auger)` using consistent signed/units, assess heavily QW4-concentrated generation and carrier e/h cutlines, audit 2D current normalization. Before any ON comparison, rerun fixed-Mg NtSide=1e18; old pre-fix n25 not comparable. No code edits or new runs this turn.

## 2026-11-04 — Wu post-MgFix NtSide=0 n21 fresh 5V solver normal completion VERIFIED (OBSERVED USER LOG)
- Worker 주수빈; project `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`, post-Mg local acceptor mapping and fresh OFF n21. User's exact `tail -n 45 n21_des.log` shows final t=1 and anode=5.000E+00V; Bank/Rose converged with error 6.9604E-01 (<1), `Curve trace finished.`, `Writing plot 'n21_des.tdr' ... done.`, `Sentaurus Device simulation finished` Tue Nov 3 23:58:02 2026 KST; wallclock1589.90s, CPU1426.26s, memory755MB.
- Final 5V terminal RAW outputs: anode electron +1.695E-04, hole +2.399E-03, total +2.569E-03; cathode electron -2.569E-03, hole -4.409E-16, total -2.569E-03. Anode hole fraction ≈93.4% of raw total. Previous accepted 4.932V anode e1.579E-04, h2.296E-03, total2.454E-03. Distinct older intermediate .out/.err/.log tails stopped at 4.332/4.432V, but fresh later final log supersedes them.
- With prior n21 TDR screens: pGaN acceptor up to2e19, global eDensity1.35933e20/hDensity1.16504e20, MQW RadiativeRecombination max3.43425e29 and SRH max2.05925e28 cm^-3s^-1 (all global pixel legend maxima, not QW-integrated). Thus numerical 5V + TDR and nonzero p-side hole-terminal current established; **NO QW-specific IQE, calibrated operating J, or Wu paper reproduction yet**. Terminal hole dominance is NOT QW internal quantum efficiency. 2D I units / AreaFactor and width normalization are assumed, not independently validated. Pre-MgFix n25 5V ON outputs are not valid comparators against post-MgFix n21 OFF.
- NEXT: region-integrate Radiative/SRH/Auger in the same QW1–4 clean+damaged subregions, confirm QW e/h populations and local injection; calculate IQE=Sum(Rad)/(Sum(Rad)+Sum(SRH)+Sum(Auger)) if positive and same signed convention, then verify 2D J normalization; only after OFF validation rerun NtSide1e18 ON with the fixed Mg mesh and compare at matched current. No code changes/new run in this log-inspection turn.

## 2026-11-04 ~01:03 KST — Wu MgFix OFF n21 SRH recombination SVisual map observed (OBSERVED, IQE pending)
- 작업자 주수빈. User-provided Sentaurus Visual screenshot: `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`, dataset `n21_des`, Scalar `srhRecombination`. Global color legend min 0 and max **2.05925e28 cm^-3 s^-1**. Distinct high-SRH red/orange thin MQW stripes around x~0.15–0.165 um; surrounding p/n material largely yellow/lower on displayed scale. This is a spatial visualization, NOT region-integrated QW SRH or sidewall-only SRH.
- Prior same n21 SVisual RadiativeRecombination global max 3.43425e29 cm^-3 s^-1; do NOT divide separately occurring global maxima to estimate IQE. NtSide=0 signifies parameterized sidewall traps OFF, not intrinsic SRH OFF. QW-by-QW region integrals Radiative/SRH/Auger and carrier cutlines still needed; final fresh 5V log verification still pending; ON n25 deferred.
- No new code changes/run claimed. Next: verify final 5V `n21_des.log`, extract QW regionwise recombination integrals and compute IQE from sums, then inspect ON NtSide=1e18 at matched current.

## 2026-11-04 ~00:55 KST — Wu MgFix OFF n21 TDR acceptor holes electrons radiative observed (OBSERVED, IQE unverified)
- OBSERVED user SVisual screenshots of post-MgFix CMP_WU_Copy/n21_des.tdr: top pGaN AcceptorConcentration red, legend max 2.000e19 cm^-3 (old pre-fix SDevice acceptor=0). Global hDensity max 1.16504e20 cm^-3, eDensity max 1.35933e20 cm^-3. These are global extrema, not QW-specific averages.
- RadiativeRecombination global legend maximum 3.43425e29 cm^-3 s^-1 with strong thin red stripes in MQW toward x≈0.15–0.165um (lower wells); visually nonzero QW radiative recombination is confirmed but per-QW rates/IQE and uniformity are NOT. Color scales may be nonlinear; large peaks should be interrogated using regionwise integration.
- Interpretation: SDevice Mg acceptor recognized and carrier populations increased after mapping fix. Still NO proof of quantitatively calibrated LED or Wu paper reproduction, no QW regional rate integrals, final 5V terminal log absent. NEXT inspect final newly dated n21_des.log and 5V contact components; then QW1–4 e/h cutlines and Clean/Dmg QW region integrals Rad/SRH/Auger, current normalization, baseline validation before ON n25.

## 2026-11-04 ~00:47 KST — Wu MgFix OFF n21 SVisual full 0-5V IV curve observed (OBSERVED SCREENSHOT; final solver log pending)
- User reports clean NtSide=0 post-MgFix run completed; SVisual screenshot in CMP_WU_Copy shows BaselineData_22, red NtSide=0 curve extending from 0 to ~5 V with turn-on knee near ~3.2–3.4 V. Left axis 'Anode Current [A/um] (assumed)', visual 5V endpoint ≈2.6e-3 native presumed A/um; right axis 'Width-normalized |J| [A/cm2] (assumed)' endpoint ~2.5e4 under UNVERIFIED dimensional/AreaFactor convention. These are visual approximations only, NOT confirmed exact current/density.
- Earlier same post-fix n21 log directly confirmed 4.332 V convergence and hole-dominated contact current (anode e7.286e-5, h1.415e-3, total1.488e-3 raw); image now strongly suggests 5V data plotted, but user has not supplied current dated final n21_des.log proving numerical normal termination, TDR persisted and 5V e/h terminal components.
- NEXT: tail new n21_des.log and confirm 'Curve trace finished', 'simulation finished', 5V terminal currents; then inspect fresh n21_des.tdr pGaN AcceptorConcentration/hDensity; QW1–4 eDensity/hDensity, Rad/SRH/Auger integrals and physical IQE. Do not run n25 ON until clean validated. Keep preMgFix backups; J normalization unvalidated.

## 2026-11-04 — Wu post-Mg n21 advanced to 4.332V and hole current restored (OBSERVED 4.332V CONVERGED; FULL 5V PENDING)
- OBSERVED user live shell tail post-Mg CMP_WU_Copy/n21_des.out/.log: earlier Newton step backtracking at t≈0.64 was recovered. Converged step at t=0.866477, anode=4.332V with Bank/Rose error=0.24308 (<1), after 3 Newton iterations. Terminal RAW currents anode electron +7.286e-05, hole +1.415e-03, total +1.488e-03; cathode total -1.488e-03. Hole fraction of anode total ≈95.1%, distinctly unlike old pre-fix 5V hole3.696e-27 and electron2.884e-05; voltages differ, so do NOT infer an improvement factor or match-current comparison. These terminal components alone do not prove QW hole density or radiative recombination.
- SDevice then attempted t=0.866477→0.886477 (nominal 4.432V); only Newton iterations0–3 were shown, no convergence outcome for that step. Full 5V run still NOT confirmed. The .err tail reports InGaN eDOSMass/hDOSMass computed via GaN/InN side materials, likely interpolation notices rather than a new fatal event; earlier datexcodes variable redefined warnings remain to classify separately.
- NEXT: keep current n21 solver running if advancing; monitor date and 5V final convergence, do not edit active files or start n25. When done inspect SDevice pGaN AcceptorConcentration/free hDensity, QW1–4 electrons/holes and radiative/SRH/Auger; preserve pre-Mg n21/n25 backups.

## 2026-11-04 ~00:43 KST — Wu post-Mg SDevice n21 Newton step reduction screenshot (OBSERVED SCREENSHOT; run ongoing, outcome unknown)
- User SWB screenshot shows n21_des.out during new post-Mg SDevice run: "Finished, because... #iterations larger than 35" at one Newton attempt, followed by "Newton didn't converge, trying again with smaller step"; quasistationary t=0.637961→0.642158, stepsize=4.1970e-03. Subsequent Newton iteration residuals and error remain high (seen error 3.44e+03 at iteration 5). This is a local failed step and backtracking, NOT definitive full run failure. SWB bottom status still running.
- Bottom n21_des.err shows "datexcodes.txt ... variable ... is redefined" for MagnesiumActiveConcentration, MagnesiumConcentration, MagnesiumChemicalConcentration, MagnesiumMinusConcentration, nSiliconActiveConcentration etc. Likely duplicated installed defaults from copying full GaN example file; warning severity/causality not yet established.
- Post-fix SDE mesh pGaN≈-2e19 net doping confirmed, but SDevice convergence and free-hole/QW physics NOT confirmed. NEXT read-only tail latest n21_des.out/n21_des.err/log and look for actual progression vs shrinking steps; do not change physics or edit datexcodes while running. If stuck/failed, diagnose duplicate mapping + Newton maximum residual position / model parameters; protect pre-fix backups.

## 2026-11-04 — Wu n21 post-MgFix OFF validation checklist agreed (PROPOSED VALIDATION CRITERIA, not new results)
- User asked for concise acceptance plan while new OFF n21 is intended/running; no new 5V post-fix output provided in this exchange. Proposed 3 sequential gates: (1) numerical finish at 5V, new-dated n21_des.log and n21_des.tdr; (2) SDevice pGaN AcceptorConcentration recognized, free hDensity much above old ~1 cm^-3, holes reaching all/active QWs and meaningful bipolar transport (contact partition alone not sufficient); (3) QW RadiativeRecombination >0 and physically meaningful relative to SRH/Auger, compare integrals from consistent QW regions and check IQE=Rrad/(Rrad+RSRH+RAuger) only when appropriate rates/integration defined. 
- No predetermined 5V terminal-current magnitude or Wu-paper IQE pass threshold is justified yet; nominal Mg 2e19 is not free-hole density and pre-fix raw I=2.884e-5 is not reference to match. Do not run ON n25 until clean OFF physical gates pass; later compare OFF/ON at matched current and consistent geometry/units; check remaining Wu paper-fidelity unknowns before final baseline.

## 2026-11-04 — Wu2023 post-fix n21 tail still from Nov03 22:02 pre-fix (OBSERVED, no new SDevice result)
- User printed CMP_WU_Copy/n21_des.log tail after pre-fix backups. Log retains "Sentaurus Device simulation finished" Tue Nov 3 22:02:35 KST, electron current 2.884e-05, hole 3.696e-27 at 5 V; identical to pre-Mg-fix n21 results.
- Thus no post-fix OFF SDevice run has been confirmed. SDE fresh mesh pGaN signed net doping ≈-2e19 and nGaN≈+5e18 still verified. NEXT manually run n21 Trap OFF against fresh n1_msh.tdr in SWB, ensuring a newly dated log, then analyze acceptors, free hole density and QW recombination. n25 ON not yet.

## 2026-11-04 — Wu2023 pre-fix n21 n25 SDevice output backup verified (OBSERVED BACKUP; POST-FIX SDEVICE NOT RUN)
- User terminal command in school CMP_WU_Copy created/listed preMgFix_SDevice_backup, containing six files: n21_des.log 187K, n21_des.plt 30K, n21_des.tdr 7.1M; n25_des.log 192K, n25_des.plt 30K, n25_des.tdr 7.4M; total ~15M. Observed list verifies existence of backup copies (not independent bytewise hashes).
- Corrected SDE mesh pGaN DopingConcentration≈-2e19 and nGaN≈+5e18 previously observed after project-local Mg datexcodes mapping. POST-FIX SDevice still not run per user evidence; physical hole injection, QW recombination unverified.
- NEXT: run n21 clean OFF SDevice only with regenerated n1_msh.tdr; ensure no downstream n25 run. Inspect newly generated 5V logs, AcceptorConcentration and hDensity in pGaN/QWs, and radiative/SRH before ON.

## 2026-11-04 ~00:09 KST — Wu2023 SDE pGaN negative net doping verified after local Mg map (OBSERVED screenshot; device physics pending)
- OBSERVED user SVisual screenshot of school CMP_WU_Copy n1_msh (after user-reported SDE rerun), Scalar DopingConcentration. Top pGaN (x≈0–0.120um) uniform dark blue, color-scale minimum -2.000e19 cm^-3; lower nGaN region red, maximum +5.000e18 cm^-3. These are consistent with signed pGaN ≈-2e19 and nGaN ≈+5e18 (read color legend, not exact point probe). Earlier original mesh had pGaN DopingConcentration≈0 and MgActive 2e19, so net p-acceptor conversion at SDE mesh stage is now visually verified.
- User installed a project-local datexcodes.txt with uncommented GaN MagnesiumConcentration doping=acceptor active=MagnesiumActiveConcentration / ionized=MagnesiumMinusConcentration, and confirmed pre-fix mesh backup. The before/after change strongly supports mapping fix, but no controlled file-loading log proof; SDevice carrier injection/emission/IQE remain UNVERIFIED. Do not equate -2e19 net doping with free hole density or claim baseline physically validated.
- NEXT: preserve prior n21/n25 5V logs/TDR/PLT separately before reruns; run Trap OFF SDevice only against corrected mesh, confirm AcceptorConcentration, pGaN/QW hDensity, radiative/SRH, terminal e/h current and meaningful injection; only then ON. Do not alter Wu 2023 epitaxy, doping dose, EBL/polarization in this gate.

## 2026-11-04 — Wu2023 SDE rerun user-reported after local Mg datexcodes (USER-REPORTED RUN; mesh result UNVERIFIED)
- User states "SDE 새로 다 돌렸어" after verifying CMP_WU_Copy/datexcodes.txt active GaN magnesium acceptor mapping and backup n1_msh_before_MgFix.tdr. No SDE log, new mesh timestamp, DopingConcentration screenshot or actual signed net doping output supplied yet.
- Do NOT treat mapping fix as validated; cannot establish SDE picked up project local datexcodes nor that pGaN net doping is negative. Next direct check: SVisual fresh n1_msh.tdr DopingConcentration in pGaN 0..0.12um (sign and range), nGaN +5e18; optionally SDE log/timestamp if stale. No SDevice rerun until net acceptor verified.

## 2026-11-04 — Wu2023 project-local Mg acceptor map and mesh backup verified (OBSERVED; mapping application untested)
- User terminal verified /user/semi/semi437/tmp/myproject/CMP_WU_Copy/datexcodes.txt exists (3.5 KB, ls timestamp Nov3 23:12) and n1_msh_before_MgFix.tdr mesh backup exists (962 KB, same timestamp). Source command used cp -n, so creation time vs prior existence was not independently established; current presence and contents verified.
- grep confirms project's datexcodes.txt lines26–40: MagnesiumConcentration/MagnesiumChemicalConcentration has UNCOMMENTED doping=acceptor(active=MagnesiumActiveConcentration, ionized=MagnesiumMinusConcentration, material includes GaN). Default installed lib declaration is commented; local version is active.
- Still UNRESOLVED: Did SDE/SWB actually load local file and yield negative pGaN DopingConcentration? No new SDE/SDevice execution yet. Next controlled SDE-only run with existing output backup, inspect signed mesh doping pGaN negative and nGaN +5e18, do not rerun old n21/n25 5V.

## 2026-11-03 — Wu2023 school SDevice IncompleteIonization switch matches Mg Species (OBSERVED; mapping fix pending)
- User provided actual CMP_WU_Copy/pp21_des.cmd. File lines 11–16: Grid=n1_msh.tdr, Plot=n21_des.tdr, Parameter=pp21_des.par. Global Physics lines22–30 include Recombination(SRH Radiative Auger), Piezoelectric_Polarization(strain), IncompleteIonization(Dopants="MagnesiumActiveConcentration"), Thermionic. Actual school pp21_des.par GaN Ionization Species("MagnesiumActiveConcentration") E_0=0.15 alpha=0 g=4; species matches switch.
- Thus SDevice switch and ionization parameter species names DO MATCH; source mesh is still unrecognized acceptor (pGaN MgActive2e19 but net doping0). Installed default datexcodes chemical Mg acceptor link is commented out; local project/home mapping absent at tested paths. Next isolated, project-local datexcodes mapping; SDE mesh-only re-run and pGaN negative doping, nGaN retained 5e18; only then clean SDevice. No new simulation or code changes in user's school project.

## 2026-11-03 — pp21_des.par Mg ionization parameters found (OBSERVED)
- School output grep confirms GaN Ionization Species("MagnesiumActiveConcentration"), E_0=0.15 eV, alpha=0, g=4 in CMP_WU_Copy/pp21_des.par. Parameter header says generic III-N model, not Wu paper value.
- This parameter set does not itself create an Mg acceptor mapping. Default T-2022.03 datexcodes ordinary magnesium acceptor declaration is commented. School SDE places MgActive2e19, original mesh pGaN net DopingConcentration=0 and SDevice AcceptorConcentration=0.
- Next: verify actual SDevice Physics IncompleteIonization; isolate project-local datexcodes Mg mapping, rerun mesh-only and check negative pGaN net doping before 5V SDevice. No code or simulation changed.

## 2026-11-03 — Wu2023 school pp1_dvs MgActive-only confirmed (OBSERVED; mapping correction not yet applied)
- User actually ran grep against school /user/semi/semi437/tmp/myproject/CMP_WU_Copy/pp1_dvs.cmd: line25 PMgActive=2.0e19; line61 (place-field rname "MagnesiumActiveConcentration" pval); lines68–69 apply to pGaN and potential EBL. No MagnesiumConcentration/PDopant entry in the displayed grep output.
- Installed T-2022.03 default lib/datexcodes.txt ordinary MagnesiumConcentration doping=acceptor clause is commented; installed GaN_AlGaN_Polarization example maps MagnesiumConcentration chemical→MagnesiumActiveConcentration acceptor. This is strong evidence of why n1_msh pGaN MagnesiumActive2e19 exists but net doping0 and SDevice acceptor0. Effective runtime override and device par ionization still must be confirmed; no conclusion that repaired physical LED is validated.
- NEXT read-only check school's pp21_des.par Mg ionization Species configuration, then create controlled project-specific mapping in separate copy (never global lib edit). Re-mesh and verify pGaN negative signed DopingConcentration before a clean SDevice rerun. No code or simulation changes yet.

## 2026-11-03 — Wu2023 default datexcodes Mg acceptor declaration commented (OBSERVED / MAPPING ROOT CAUSE STRONGLY SUSPECTED)
- User inspected installed T-2022.03 default lib/datexcodes.txt: at lines 10686–10699, MagnesiumConcentration/MagnesiumChemicalConcentration has the full 'doping = acceptor (active = MagnesiumActiveConcentration, ionized = MagnesiumMinusConcentration, material includes GaN)' clause COMMENTED OUT with '!' prefixes. At lines 13022–13034 the DISTINCT pMagnesiumConcentration species has active acceptor registration. Earlier installed GaN_AlGaN_Polarization example has UNCOMMENTED Mg acceptor mapping.
- User confirmed neither /user/semi/semi437/tmp/myproject/CMP_WU_Copy/datexcodes.txt nor ~/datexcodes.txt exists; other SWB execution directory overrides not excluded. Actual n1_msh MgActive 2e19 yet net pGaN doping~0 and n21 SDevice acceptor0. Evidence strongly supports missing standard Mg acceptor mapping, but effective runtime map and chemical/active-species linkage remain unconfirmed.
- GitHub PROPOSED/UNRUN Wu candidate CMP_BASELINE_3.2.0_WU2023PHY/sde_dvs.cmd places MagnesiumActiveConcentration in pGaN, with no MagnesiumConcentration placement. School pp1_dvs.cmd MAY differ and must be read independently.
- NEXT read-only: grep -nEi 'Magnesium|PMg|DopingConcentration|PDopant' /user/semi/semi437/tmp/myproject/CMP_WU_Copy/pp1_dvs.cmd. Then decide minimally-scoped local datexcodes and species/profile fix preserving prior output and 2023 Wu structure. Validate new SDE mesh signed pGaN negative net doping before SDevice rerun. No code/run change.

## 2026-11-03 — Wu2023 local/home datexcodes absent (OBSERVED; effective runtime mapping UNRESOLVED)
- User executed ls -l /user/semi/semi437/tmp/myproject/CMP_WU_Copy/datexcodes.txt ~/datexcodes.txt; both reported No such file or directory. The user shell is currently in ~, not project directory. This establishes absence at these two tested paths only, not all SWB runtime/working-directory overrides.
- Earlier T-2022.03 installed official GaN_AlGaN_Polarization example contains Mg acceptor doping linkage; does not imply active Wu mapping. SDE mesh MgActive2e19, net doping~0, SDevice acceptor0 remain blocker.
- NEXT read-only: grep 'Magnesium' in installed default /user/tools/synopsys/sentaurus/T-2022.03/tcad/T-2022.03/lib/datexcodes.txt; then inspect SDE pp1_dvs.cmd and actual SWB runtime files before proposing minimal mapping fix. No new run/code edit.

## 2026-11-03 — Wu2023 installed GaN Mg acceptor mapping inspected (OBSERVED / ROOT CAUSE UNRESOLVED)
- User read T-2022.03 Applications_Library/Power/GaN/GaN_AlGaN_Polarization/datexcodes.txt lines 1–65. Official example Variables includes MagnesiumConcentration, MagnesiumChemicalConcentration with 'doping = acceptor (active = MagnesiumActiveConcentration; ionized = MagnesiumMinusConcentration; material = AlN, GaN, AlGaN, InGaAs, InGaAsP, InP)'. MagnesiumActiveConcentration itself is listed separately as active Mg.
- The mapping positively exists in this **installed example**, but does NOT establish it is loaded in the user's CMP_WU_Copy SDE/SDevice runs. Source mesh pGaN MgActive2e19 yet net DopingConcentration~0 and SDevice AcceptorConcentration~0 remain known; mapping/chemical-versus-active source path is under investigation.
- NEXT (READ ONLY): check whether project-local / home datexcodes.txt exists in CMP_WU_Copy; inspect original pp1_dvs.cmd Mg species and actual effective runtime mapping before minimal correction. Preserve finished n21/n25, no rerun/code changes yet.

## 2026-11-03 — Wu2023 installed GaN examples contain Mg species entries (OBSERVED; mapping not yet inspected)
- User ran read-only grep over T-2022.03 Applications_Library/Power/GaN example datexcodes.txt files. Installed GaN_AlGaN_Polarization, GaN_AlGaN_Polz_Calculated, GaN_Fin-HEMT, GaN_HEMT_FermiStat, and pGate_HEMT_CC examples contain MagnesiumActiveConcentration and MagnesiumConcentration references. pGate_HEMT sample itself yielded no Magnesium match.
- This verifies installed example definitions exist but does NOT prove acceptor attribute, local Wu project application, or root cause. Existing source mesh pGaN MgActive2e19 yet DopingConcentration~0 and SDevice AcceptorConcentration~0 remain blocker.
- NEXT READ ONLY: inspect first 65 lines of installed GaN_AlGaN_Polarization/datexcodes.txt for magnesium doping=acceptor(material=...) and compare current CMP_WU_Copy local/home datexcodes with active mesh/SDevice preprocessing. No code edits, no new runs.

## 2026-11-03 — Wu2023 Mg net-doping map diagnostic (OBSERVED)
- User SVisual n1_msh DopingConcentration plot: p-GaN blue near 0; n-GaN +5e18 cm^-3. Earlier same n1_msh showed p-GaN MagnesiumActiveConcentration 2e19 cm^-3.
- Mg field exists but does not contribute to net p-type doping; SDevice AcceptorConcentration 0 and hDensity near zero are consistent. Dopant-species mapping is suspected, exact definition not yet inspected.
- Next: read local and installed datexcodes.txt magnesium donor/acceptor definitions before editing; require negative p-GaN net doping in re-meshed copy, then test SDevice. No code modified.

## 2026-11-03 22:13:17 KST — Wu2023PHY Trap ON n25 5V solver normal finish CONFIRMED (OBSERVED USER LOG)
- School project `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`; user pasted `n25_des.log` tail. Actual 5.000E+00V anode electron `2.858E-05`, hole `2.384E-20`, conduction `2.858E-05` raw native units; cathode electron `-2.858E-05`, hole `-4.223E-29`, conduction `-2.858E-05`.
- Last Bank/Rose solver converged error 8.4932E-01 (<1). `Curve trace finished`, `Writing plot 'n25_des.tdr' ... done`, `Sentaurus Device simulation finished` Tue Nov 3 22:13:17 KST, wallclock 530.09s, CPU 529.57s, peak757MB; licenses returned. Thus Trap ON 5V SDevice completion **now directly verified**, replacing earlier screenshot-only/solved-unconfirmed status.
- Clean n21 5V same nominal source split: anode electron `2.884E-05`, hole `3.696E-27`, conduction `2.884E-05` raw, saved TDR. At 5V ON total is `2.6E-07` raw smaller than OFF (about `0.902%` of OFF). THIS IS ONLY a same-voltage *terminal current* difference, NOT IQE/sidewall recombination loss, and published 2D A/um/AreaFactor conventions not independently validated.
- **Major unresolved physics:** clean n21 SDevice `AcceptorConcentration` 0–0 cm^-3 and `hDensity` max~1 cm^-3, but source mesh `n1_msh.tdr` positively verifies pGaN `MagnesiumActiveConcentration`=2e19 cm^-3. Both terminal currents electronic-dominated; ON p-side hole current `2.384e-20` still negligible against `2.858e-5`. Do not treat emission as validated or attribute I difference to NtSide recombination mechanism without QW carrier/rate investigation.
- **NEXT (no rerun yet):** in `n1_msh.tdr` view signed `DopingConcentration` across p-GaN to differentiate mesh net-acceptor mapping. Then inspect local/installed `datexcodes.txt` (GaN MagnesiumActiveConcentration mapping), `pp21_des.par` & command, p-GaN donor/acceptor maps, QW hDensity/RadiativeRecombination. Only a source-supported minimal fix after cause established; preserve both finished TDR and outputs.

## 2026-11-03 ~23:05 KST — Wu2023PHY original n1_msh Mg 2e19 CONFIRMED; root moved to Mg dopant recognition (OBSERVED)
- User screenshot **correctly shows `n1_msh` (original SDE mesh)**, `MagnesiumActiveConcentration` chosen, top pGaN `x≈0..0.12µm` uniform red at **2.000e+19 cm^-3** (range from 0 to 2e19). Below pGaN MQW/nGaN blue/near-zero. This PROVES SDE Mg profile writing and mesh carrying it; prior assumption that Mg was absent from SDE is rejected.
- Distinct existing `n21_des.tdr` plot showed `AcceptorConcentration` 0–0 and `hDensity` top ~1 cm^-3, 5V anode e=2.884e-5/h=3.696e-27 raw. Combined evidence strongly implicates **SDevice or mesh dopant-species→acceptor mapping, custom datexcodes, actual pp21 parameter/incomplete ionization**, not Mg rectangle/profile omission. Still needs `n1_msh.tdr` `DopingConcentration` distribution: negative p region means mesh net doping recognized, zero means upstream net-doping conversion not recognized.
- Official Sentaurus Training III-N materials reference https://ghzphy.github.io/Sentaurus_Training/sd/sd_16.html explicitly maps Mg chemical species to `MagnesiumActiveConcentration` / `MagnesiumMinusConcentration` with `doping=acceptor(material=... GaN ...)` via project-local `datexcodes.txt`; local override may be necessary based on actual installed mapping. Public example `Material=GaN Ionization Species("MagnesiumActiveConcentration") E_0=0.15` needs actual pp check; never assume Mg nominal input equals free holes.
- **NEXT** (read-only): in presently open `n1_msh` SVisual switch from Mg to `DopingConcentration` and inspect top pGaN range and sign (positive/negative/zero). Also inspect effective local/home/installed `datexcodes.txt` for GaN magnesium acceptor link and `pp21_des.par`/cmd; only after these gates construct minimal species mapping fix. No code edit, no rerun.

## 2026-11-03 ~23:02 KST — Wu2023PHY NtSide=1e18 5V I–V shown (USER SCREENSHOT/REPORT; final SDevice log not yet seen)
- School SVisual screenshot `CMP_WU_Copy` shows `BaselineData_26`, legend `NtSide=1e18`, I-V plot 0→5V with near zero to ~2.5–3V then rises to visual ~2.8e-5 raw at 5V. Conditional width-normalized plot shows ~2.8e2 A/cm², **still A/um+AreaFactor1 ASSUMPTION**. User reports Trap ON run finished, but ON SDevice final `n25_des.log` and exact 5V contact electron/hole current have NOT been furnished in current turn; node mapping n25→26 provisional.
- Clean NtSide=0 already confirmed 5V `n21_des.log` total2.884e-5 raw, dominated by electron current; SVisual prior `AcceptorConcentration` auto range0–0 and `hDensity` auto maximum~1 cm^-3. **No electrically validated p-side hole injection.**
- Similar-looking OFF/ON I-V curves alone cannot demonstrate sidewall recombination insignificance, QW IQE or Wu source replication. Exact matched-current trap effect not established; ON e/h balance and QW radiative/SRH unmeasured.
- NEXT 1: verify ON node `tail -n 50 /user/semi/semi437/tmp/myproject/CMP_WU_Copy/n25_des.log` and record whether 5V `Curve trace finished`, TDR save and terminal-current values. NEXT 2: urgently open `n1_msh.tdr` and inspect `MagnesiumActiveConcentration` across pGaN, not merely `n21_des.tdr` AcceptorConcentration or ON PLT; confirm actual Mg source species then datexcodes/ionization. No new code edits or trap interpretation before doping/holes corrected.
- No new GitHub candidate code and no new simulation initiated by ChatGPT.

## 2026-11-03 ~23:00 KST — Wu2023PHY n21 AcceptorConcentration ZERO at clean 5V (OBSERVED screenshot / doping mapping blocker UNRESOLVED)
- User screenshot in Sentaurus Visual of `CMP_WU_Copy/n21_des.tdr`, vertical x 0..~0.2um near p-GaN and QWs, `AcceptorConcentration` selected. Entire map uniform blue with SVisual range **0 min, 0 max cm^-3**, no p-GaN acceptors reflected in SDevice output (assuming auto-range and no clamping). This accompanies prior n21 hDensity auto max 1 cm^-3 and 5V anode electron2.884e-5/hole3.696e-27 raw.
- **New confirmed physical blocker:** simulator does not represent any p-acceptor in `AcceptorConcentration` field of saved clean 5V TDR. Root cause UNRESOLVED; do NOT assume that Mg source concentration missing from SDE mesh solely from output. Candidate SDE writes `MagnesiumActiveConcentration` in pGaN at nominal2e19; SDevice incomplete ionization and installed `datexcodes.txt` dopant mapping must be differentiated.
- External source corroboration: Sentaurus Mesh training https://ghzphy.github.io/Sentaurus_Training/smesh/smesh_04.html explains active dopant naming and resulting net concentration; Sentaurus Device III-N training https://ghzphy.github.io/Sentaurus_Training/sd/sd_16.html explicitly shows Mg acceptor `datexcodes.txt` material mapping and incomplete-ionization species; Synopsys TCAD News Spring2013 describes dopant declaration through `datexcodes.txt`.
- **NEXT READ-ONLY GATE:** open `CMP_WU_Copy/n1_msh.tdr` (original SDE mesh, NOT n21_des.tdr), inspect `MagnesiumActiveConcentration` in top pGaN and SVisual min/max. If absent/zero, inspect actual `pp1_dvs.cmd` SDE profile placement/species; if present2e19, inspect `datexcodes.txt` acceptor mapping GaN/active species and `pp21_des.par` incomplete-ionization. Also compare donor/nSi and net `DopingConcentration` if needed. No code edits/trap ON or new run before gate.
- No school new run or file edits in this observation; preserve existing 5V TDR and I–V as numerically valid but **not** physically functioning LED baseline.

## 2026-11-03 ~22:57 KST — CMP_WU_Copy n21 5V hDensity map inspected (OBSERVED screenshot; cause UNRESOLVED)
- Sentaurus Visual screenshot of n21_des.tdr at clean 5V has `hDensity` selected with logarithmic color scale. Displayed auto range ~3.79136e-39 to 1 cm^-3. Apparent hole density throughout p-GaN / QW / n-GaN is orders below functional p-type injection; confirm this is not a manual plot range/clipping.
- Corroborating existing n21 5V anode terminal current: electron=2.884e-5 raw, hole=3.696e-27 raw. Nonzero total electrical current DOES NOT validate QW bipolar injection or radiative LED operation.
- Root cause not yet established. Single immediate read-only step: uncheck hDensity in SVisual and display `AcceptorConcentration` across pGaN with its automatic range. If absent/zero inspect `MagnesiumActiveConcentration` / `datexcodes.txt` species, preprocessed SDE, and `pp21_des.par`; if present check Mg incomplete-ionization, band profiles and contacts. Do not prematurely modify physics or run trap-ON.
- No new simulation or code change.

## 2026-11-03 ~22:53 KST — Wu2023PHY clean 5V SVisual1 plots shown (OBSERVED USER SCREENSHOT; NOT physical injection validation)
- Screenshot from school `CMP_WU_Copy` Sentaurus Visual T-2022.03 shows data `BaselineData_22` and two red curves labeled `NtSide=0`: left anode terminal current against anode voltage 0→5V, right width-normalized |J| from nominal 10um plot script. Both display smooth increasing response with visible rise ~2.5–3V, final ordinate approx 2.88e-5 raw left and 2.88e2 A/cm² right.
- SDevice log already separately verified clean n21 5V total raw current +2.884e-5, electron +2.884e-5, hole +3.696e-27, normal finish at 22:02:35, n21_des.tdr saved. Plot confirms SVisual visualization, not calibrated 2D→J scaling or evidence of radiative emission.
- **IMPORTANT:** right `J` assumes native 2D current A/um, width 10um, AreaFactor1; do not present as measured device or 3D pixel J. p-side current almost exclusively electrons, so direct QW hole and radiative verification is still mandatory.
- **NEXT:** reuse existing n21_des.tdr in SVisual 2D view; first inspect hDensity on logarithmic scale across pGaN and QW1–4, then AcceptorConcentration, eDensity, bands/quasi-Fermi and Radiative/SRH distributions. Preserve clean result; do not run trap-on until actual QW electron/hole injection assessed.
- No new school code modification or re-run, GitHub source unchanged.

## 2026-11-03 22:02:35 KST — Wu2023PHY clean n21 5V numerical finish CONFIRMED (user log)
- School CMP_WU_Copy/n21_des.log shows anode5V; electron2.884e-5, hole3.696e-27, total2.884e-5 raw; cathode total-2.884e-5 raw.
- Newton convergence 0.20186; Curve trace finished; n21_des.tdr saved; solver normal finish, 460.97s wallclock, 765MB peak.
- Numerical run confirmed, NOT a physically valid Wu replication. Nearly all terminal current is electronic; pGaN and QW hole density and radiative rate not yet measured. Check TDR carriers, doping, bands, radiative/SRH before ON or baseline freeze. No code change.

## 2026-11-03 — CMP_WU_Copy Wu2023PHY n21 clean sweep reaches 3.713V with finite electron-dominated current (USER LOG OBSERVED, 5V STILL RUNNING)
- User pasted active `/user/semi/semi437/tmp/myproject/CMP_WU_Copy/n21_des.log` tail. Accepted Quasistationary step `t=0.722621 -> 0.742621` (Vstop5 -> anode 3.713E+00 V), Bank/Rose coupled Poisson+electron+hole solved after 3 Newton iterations; final criterion `Error smaller than 1 (1.7198E-01)`. Next step `t=0.742621 -> 0.762621` was IN PROGRESS when log captured (iteration 2 shown). No full 5V completion, TDR, IV/JV, EQE confirmed.
- Direct log at 3.713V: anode electron current `+1.374E-05`, hole `+1.885E-29`, conduction `+1.374E-05` (raw SDevice current units); cathode electron `-1.374E-05`, hole `+2.334E-40`, conduction `-1.374E-05`. Current continuity total terminal signs match. Existing prior Wu10 (DIFFERENT source, PolAct0 etc) clean 5V raw total 3.025E-29. Numerical magnitude increase indicates injection/transport change but cannot be quantified as paper fidelity improvement across differing physics and bias/geometry or verified as functioning LED.
- **Concern:** terminal current overwhelmingly electronic at both contacts and anode hole current essentially zero. Strong diagnostic flag for Mg ionization/species/contact and QW hole transport, but terminal current partitions alone do not establish zero QW hole density or exact causal mechanism.
- **NEXT:** Do not interrupt ongoing run; confirm eventual 5V `Curve trace finished`, final current, TDR saved. Then inspect `pGaN` AcceptorConcentration, `hDensity`, quasi-Fermi, `eDensity`, band edges/field and QW1–4 Radiative/SRH recombination. Preserve output and no parameter/model edits without diagnosis. 2D raw current units and area factor unverified. No new source changes in this turn.

## 2026-11-03 — CMP_WU_Copy SDevice rerun now executing after parameter-file creation (USER REPORT; completion unverified)
- Earlier n21 SDevice fatal: missing `pp21_des.par`; SDE mesh 33 regions and 40006 triangles had loaded.
- User viewed Sentaurus SWB "Create Parameter File" dialog for missing `sdevice.par`, was instructed to choose "Create Empty File", paste project `CMP_BASELINE_3.2.0_WU2023PHY/sdevice.par`, and save. User then said "오 돌아가고 있어" (run is running). **User-reported RUNNING, not independently verified that pp21_des.par populated correctly or that 5V has been achieved.**
- No new SDevice log / solver convergence / terminal current has been shown. No Github code changes.
- NEXT: while run continues, monitor `/user/semi/semi437/tmp/myproject/CMP_WU_Copy/n21_des.log`; wait for actual `Curve trace finished`, final anode5.000V current and TDR write / exit before declaring complete; if error appears extract first fatal. Beware mesh quality min angle ~0.037 degrees later.

## 2026-11-03 21:45:44 KST — Wu2023PHY CMP_WU_Copy n21 SDevice stopped on MISSING PARAMETER FILE (OBSERVED / CAUSE CONFIRMED)
- User pasted exact `tail -n 100 CMP_WU_Copy/n21_des.log`: mesh successfully read and 33 semiconductor regions / 40006 triangle elements were enumerated, doping grid `n1_msh.tdr` successfully read. Immediately after `Reading parameter file 'pp21_des.par' ...` message `Cannot open parameter file 'pp21_des.par' !` causes SDevice exit. Log grep line808 shows same. **This is first confirmed blocker; not yet a physics/solver convergence problem**.
- Nonfatal Plot alias warnings: SRHRecombination and eAmorphousRecombination/eAmorphousTrappedCharge aliases in old runtime. They are unrelated to this stop.
- Current independent candidate `CMP_BASELINE_3.2.0_WU2023PHY/sdevice_des.cmd` declares `Parameter="@parameter@"`; `sdevice.par` is a separate newly added file. Workbench needs the first SDevice tool's Parameter input to contain the companion par text, set as shared sdevice.par or an individual file per tool so preprocessing generates `pp21_des.par`.
- **Suggested SWB fix (NOT executed):** select first SDevice tool icon -> Tool > Edit Input > Parameter (or right click icon -> Edit Input -> Parameter), choose empty/create file if needed, paste committed `sdevice.par` contents, save; confirm SDevice Tool Properties Common File vs Individual File as appropriate (two SDevice columns); verify `sdevice.par` and new `pp21_des.par` exist when preprocessing; then rerun failed SDevice only, not SDE. Further syntax/material/physics issues may still appear after this blocker; do not say fixed until new run.
- **Additional mesh caution:** reported min-angle 0.03724225° and worst quality ratio ~769; non-Delaunay elements0. Mesh generated/loaded but quality warrants later convergence validation, not the cause of missing par.
- Wu old baseline and current GitHub source remain unchanged. NO 5V result from Wu Copy has been observed.

## 2026-11-03 — CMP_WU_Copy n21 SDevice failure path isolated (OBSERVED USER TERMINAL / ROOT CAUSE UNRESOLVED)
- User's latest `find -mmin -60` output identifies the new school project at `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`: latest `n21_des.log` (mtime 1793709944.632), earlier `n1_dvs.log` (1793709765.376), `n1_msh.log` (1793709765.298).
- SWB screenshot from same run reported n21 SDevice failed; SWB project window showed SDE node present. SDE log files existing does **not** establish successful mesh, exact node exit status, or physics validity.
- User's broad `find ... | xargs grep -niE 'error|fatal|undefined|unknown|failed|syntax|not found' | tail -n 40` produced many `Error smaller than 1` normal Newton convergence messages from **older CMP_WU**; only `CMP_WU_Copy/n21_des.log` lines 73/136/199/200/291 (`Absolute error`, `RelErrControl`, `Relative error`) appeared in this last-40 output. **This truncated grep is NOT evidence no fatal message elsewhere**. First failure text and end of n21 log still UNSEEN.
- Diagnostic command requested: `cd /user/semi/semi437/tmp/myproject/CMP_WU_Copy; tail -n 100 n21_des.log; ls -lh *21*des*; grep -niE 'error:|fatal|undefined|unknown|syntax|cannot|warning|abort|failed' n21_des.log | head -n 30`.
- Code correction pending exact first error; do not alter unrelated `CMP_WU` old n21/n25 runs or repeat 5V sweep. No fix/solver success can be claimed from current evidence.

## 2026-11-03 — Wu2023PHY Vstop=5 direct run attempt, ERROR screenshot reported (USER REPORTED / ERROR TEXT UNVERIFIED)
- User chose Vstop=5 (rather than separate 0.1V smoke) due to execution time and initiated school SWB run. This is a Quasistationary ramp to 5V, NOT bypass of all low-bias increments.
- User subsequently attached SWB screenshot reporting an error. Exact failed node, parser/error text and active school PP/par location were not available as plain-text log in the current turn; failure is reported, **root cause UNRESOLVED**, no confirmation 5V reached.
- New GitHub candidate context: CMP_BASELINE_3.2.0_WU2023PHY; exact school file/PP match unverified. Avoid assuming error is from Mg/PooleFrenkel/Thermionic until log shows it. No new code patch and no claim of correction.
- NEXT: use recent n*_des.log, n*_dvs.log or n*_msh.log to locate first error and preprocessed code line; if SDevice, inspect pp*_des.par and Mg/nSi species. Do not repeat long run before diagnosing.

## 2026-11-03 — Wu 2023 physics-first candidate source CREATED (PROPOSED, NO SCHOOL RUN)
- USER DIRECTION: revise entire Wu candidate as far as the 2023 paper actually supports, not by transplanting old V2 or wrong Wu 2026 model.
- CODE CREATED in new isolated `CMP_BASELINE_3.2.0_WU2023PHY`: SDE, SDevice, sdevice.par, SVisual1 and README. Commits b6acbf4, 570f1e2, ebade69, 760c570, 0225a13. Parent 3.0.0 source and school CMP_WU n21/n25 preserved.
- PAPER VERIFIED: 10um; nGaN3.9um Si5e18; 4x In0.08GaN QW3nm, GaN QB8nm; pGaN Mg nominal2e19; sidewall5nm acceptor-like; piezo, incomplete ionization Mg, local field-related trap, SRH/Rad/Auger.
- CODE CHANGES: Mg p input 3e17→2e19 as `MagnesiumActiveConcentration` nominal substitutional assumption; n donor species to `nSiliconActiveConcentration`; `IncompleteIonization(Dopants="MagnesiumActiveConcentration")`; full piezo with assumed c-axis via `LatticeParameters`; new par with provisional Mg E0=0.15eV; optional modeling choices `Thermionic`, `PooleFrenkel`; trap Et and capture cross sections configurable SWB params; adjusted wide-bandgap solver ref values.
- **UNVERIFIED, NOT WU DIRECT:** pGaN thickness120nm, EBL presence (kept 0 but unresolved), full-top/bottom contacts, trap Et0.75eV & sigma1e-15, 5 QB count, crystal orientation assumption, Mg substitutional fraction, E0, Thermionic, PF, B/C/quantum treatment. No syntax/runtime/physical claim.
- STATIC AUDIT: source parens balanced; 22 unique trap region blocks, macro parameter checks; 11 nonzero host layers -> 33 material partitions (not old erroneous count36). New code not run by actual T-2022.03.
- NEXT: create new SWB project with sdevice.par, mesh/PP and doping gate; clean Nt0 0.1V syntax then 5V if accepted, inspect actual ionized Mg and QW transport; only afterward trap ON. Wu Fig1 still needed.

## 2026-11-03 — CORRECTION: Wu (2023) paper-only baseline implementation (user confirmed, source checked)
- **RETRACTION:** 직전 기록의 다른 논문을 Wu baseline의 기준으로 취급한 결정/변경 권고는 잘못된 논문 연결이므로 철회. 사용자가 확인한 대상은 Zhuang Wu et al. (2023), *Physical mechanisms on the size-effect in GaN-based Micro-LEDs*, DOI 10.1016/j.micrna.2023.207542. 앞의 다른 문헌에 의한 EBL/형상/조성 변경 지시는 사용하지 않음.
- **PAPER-VERIFIED SOURCE SNIPPET (ScienceDirect excerpt):** 10um device, 3.9um n-GaN Si5e18, four InGaN/GaN QWs (In x=0.08, 3nm QW/8nm GaN barrier), p-GaN Mg chemical 2e19, acceptor-like sidewall traps within 5nm both sides; models explicitly include piezoelectric polarization and Mg incomplete ionization, local electric-field-related trapping, Radiative/SRH/Auger recombination. The accessed excerpt does **not verify EBL presence/absence**; Fig 1(a) or full paper needs inspection.
- **Current Wu10 pilot deviation:** pGaN MgActive=3e17 not equal chemical Mg2e19, omits IncompleteIonization, PolAct0; tEBL=0 provisional and not proven to match Wu2023 Fig1. Contacts, barrier count, pGaN thickness, material parameters & trap capture kinetics remain provisional.
- **NEXT:** preserve Wu10 n21/n25 completed 5V outputs; verify Fig1 EBL/contact/stack first; implement Wu2023-supported polarization and Mg ionization in an independent protected candidate after species/material params inspection. Confirm read-only n21/n25 TDR doping/carrier/bands and preprocessed runtime. No solver/device code changes in this turn.

## 2026-11-03 — CORRECTION: 2023 Wu paper is the relevant source, NOT 2026 Lili Wu (BIBLIOGRAPHIC FIX / NO RUN)
- **Correction of previous 2026 Wu investigation:** The applicable paper is Zhuang Wu et al. (2023), *Physical mechanisms on the size-effect in GaN-based Micro-LEDs*, Micro and Nanostructures 177, 207542, DOI 10.1016/j.micrna.2023.207542. Earlier entry on Lili Wu (2026) axisymmetry/EBL/alloy gradients/EQE **is NOT applicable** and MUST NOT be used as CMP_WU evidence. This supersedes that entry without deleting historical log.
- **DIRECT SOURCE (2023 Wu paper publicly indexed introduction and simulation methods; https://www.sciencedirect.com/science/article/abs/pii/S2773012323000390):** 10um basic structure; nGaN 3.9um Si5e18; 4 InGaN/GaN QWs, In0.08 3nm QW, GaN 8nm QB; pGaN Mg2e19 cm^-3; acceptor-like traps within 5nm both sidewalls. Physical models explicitly include piezoelectric polarization, Mg incomplete ionization, local-electric-field-related trapping, and Radiative/SRH/Auger.
- **Current Wu10 pilot mismatch:** existing sde_dvs/sdevice files have PolAct0 and NO Mg incomplete ionization, provisional active acceptor 3e17 (not equal to Mg chemical dose 2e19), EBL absent and full-span contacts unverified. Therefore it is NOT a paper-faithful model. This mismatch is NOT PROVEN cause of n21 5V raw I3.025e-29 or n25 5V raw I5.810e-19. Current artifact still in read-only diagnosis; no server rerun or edits.
- **Wu text explicitly names references:** [11] Olivier et al. (2017), Shockley–Read–Hall/Auger size effect (10.1063/1.4993741); [13] Konoplev et al., *From large-size to micro-LEDs: scaling trends revealed by modeling* (10.1002/pssa.201700508; full bibliography alignment pending); [17] Shiqiang Lu et al., *Designs of InGaN Micro-LED Structure for Improving Quantum Efficiency at Low Current Density* (2021, 10.1186/s11671-021-03557-4); [18] Luming Yu et al., *Ultra-small size (1–20μm) blue and green micro-LEDs fabricated by laser direct writing lithography* (2022, 10.1063/5.0099642). [19] older trap-current-collapse model not identified.
- **Related same-lab OPEN paper (not verified Wu reference):** Xuesong Zhang, Luqiao Yin, Kailin Ren, Jianhua Zhang, *Research on Simulation Design of MOS Driver for Micro-LED* (2022, Electronics 11 2044, DOI 10.3390/electronics11132044). Independently designed 10um microLED: nGaN 4um, MQW GaN barrier10nm/InGaN5nm, AlGaN20nm, pGaN0.3um, side passivation2um; piezo, Mg incomplete ionization, tunnel, DD; modeled turn-on ~2.9V and 5V I=88 microamp. That is **not Wu 2023 epitaxy**, nor a directly comparable 2D current unit.
- **Research implication:** Do not assume EBL missing is necessarily problem. Lu [17] shows EBL removal can help hole injection for certain low-J designs; Wu Fig1 complete EBL/contact details still need verification. FIRST inspect n21 TDR and effective material/dopant/contact/field, THEN isolated variant with Wu-reported piezo and Mg ionization (and original trap/contact choice if verified); preserve source decks.
- Evidence links: https://www.sciencedirect.com/science/article/abs/pii/S2773012323000390 ; https://www.mdpi.com/2079-9292/11/13/2044 ; https://link.springer.com/article/10.1186/s11671-021-03557-4 ; https://doi.org/10.1063/1.4993741 ; https://doi.org/10.1063/5.0099642 .
- School code changes/runs: NONE.

## 2026-11-03 — Wu (2026) bibliography/figure cross-check: baseline geometry mismatch (EXTERNAL SOURCE REVIEW / NO RUN)
- Source: Lili Wu et al., *Theoretical study of nanoscale sidewall damage on carrier transport and recombination in InGaN micro-LEDs*, J. Phys. D 59 (2026) 295102, DOI 10.1088/1361-6463/ae7c7d. Publisher preview indexed at https://www.researchgate.net/publication/407015266_Theoretical_study_of_nanoscale_sidewall_damage_on_carrier_transport_and_recombination_in_InGaN_micro-LEDs . Not Wu 2023.
- OBSERVED in publicly available figure captions: paper employs a **2D axisymmetric geometric model**, studies EBL damage (Al gradient 0.150→0) and MQW damage (QW In gradient 0.150→0.145; barrier In 0.050→0.055), and plots radial positions R=480nm vs R=50nm. Reference clean configuration 00 peak EQE claimed 70% at 37 A/cm². Captions do NOT alone establish full epitaxial stack, radius/contact boundary or model physics.
- Existing Wu10 GitHub candidate is 10um planar full-width 2D, QW In0.08, EBL0, PolAct0 and pilot top/bottom Ohmic; NOT shown to match source model. Axisymmetric vs planar geometry and EBL/composition differences are major baseline-fidelity gaps; they are NOT proven to cause ultra-low measured terminal current.
- Useful literature checked: Wu ResearchGate reference list includes Yin et al. (2024) InGaN/GaN MIS 10um device with 2um nGaN / 0.3um superlattice / 9x (3nm/12nm) MQW / 30nm p-AlGaN EBL / 40nm pGaN (this belongs to Yin device, NOT Wu); see https://pmc.ncbi.nlm.nih.gov/articles/PMC10973746/ . Wu reference-list numbering and exact source of its electrical transport parameters not verified from complete PDF.
- NEXT: acquire full Wu 2026 PDF and supplementary material, map references to epitaxy/contact/BC/models and extract actual figure 1 and simulation methods; diagnose saved n21 5V clean TDR for doping/contacts/carriers first, then implement *separate* paper-faithful candidate. Preserve current Wu10 and V2/Kou, do not conflate suggested external-device numbers with Wu baseline.
- No school Sentaurus command/code modified and no new simulation run.

## 2026-11-03 ~22:10 KST — Wu independent baseline design intent clarified (USER DIRECTIVE / PROPOSED DIAGNOSTIC PLAN)
- **사용자 의사 명확화:** Wu 논문 기반 후보는 이전 Baseline의 개선·수정판이나 이전 코드를 가져다 쓰는 작업이 아니라 Wu 논문에서 독립적으로 시작한 새로운 구현 실험. 이전 Baseline의 유사한 낮은 전자/전류 문제는 반복되는 **코드 구현 방식**의 문제 가능성을 발견하는 참고 사례일 뿐, 재사용할 모델/값의 근거가 아님.
- **현 Wu 원문 SDE/SDevice 정적 감사:** full 10um/4QW In0.08, QB8nm, p-GaN MgActive3e17 (pilot), EBL=0 (pilot), top/bottom all-width Ohmic (pilot), DefaultParametersFromFile with no custom .par, native drift-diffusion without explicit Thermionic, PolAct=0 smoke, no incomplete ionization. Trap params pilot. 이러한 선택은 Wu 원문 완전 재현으로 입증되지 않음.
- **HYPOTHESES, not confirmed causal findings:** material/dopant species mapping or installed material params, contact geometry/boundary mapping, heterojunction transport treatment (thermionic vs default), and quantum confinement treatment can contribute to poor carrier injection. Existing Wu 5V NtSide0 raw current 3.025e-29; must NOT infer low QW electron density from anode electron current alone.
- **NEXT (read-only gate):** preserve Wu original n21/n25 TDR and current SWB deck; inspect OFF n21 5V carrier density, doping, band/quasi-Fermi profiles and effective pp command/material params. Then create new isolated Wu-only diagnostic variants altering **one modeling method at a time**, not transplanting V2 code, while keeping Wu literature geometry whenever possible. Thermionic/interface/quantum models must be checked against T-2022.03 guide and runtime. Keep unverified pilot settings visibly labeled, no numerical performance claims without results. No school server change in this chat.

## 2026-11-03 ~22:00 KST — Wu10 vs older V2.1 injection-code comparison (STATIC REVIEW / NO NEW RUN)
- 작업자: 주수빈. 이 채팅에서 기존 Baseline과 Wu10의 반복 저전류를 비교 요청. GitHub Wu10 원본 SDE/SDevice와 COMMON_BASELINE, 이택규 11/03 POL0NOSHELF 실측 기록을 대조함. **기존 V2.1 최신 전체 source/PP/PAR/mesh는 이 채팅에서 직접 비교되지 않음**; 문서화된 설정을 통한 비교이며 원인 확정 아님.
- **OBSERVED prior Lee V2.1 (different geometry/bias):** PolAct=0, NtSide=0, 3.6V native I=4.80713937e-6; NtSide=1e18 I=4.54183989e-6, radiative QW4 share 99.88898644%/99.96413545%. QW4 편중과 주입전류 부족은 동일 현상으로 단정 금지; old-vs-new 전류는 서로 다른 모델/전압/2D 정규화 조건으로 직접 정량 비교 불가.
- **OBSERVED Wu10:** PolAct=0, NtSide=0, 5V raw I=3.025e-29; NtSide=1e18 I=5.810e-19; 정상 수치해 종료했지만 전류 거의 0. Trap OFF부터 문제이므로 trap 효과 때문만은 아님.
- **CODE DIFFERENCES Wu vs protected CMP4/V2:** Full 2D 10um vs Half 4um; 4x In0.08 QW3nm + 5x GaN barrier8nm vs In0.15 and 22nm; EBL t=0 vs AlGaN EBL26nm; Wu full-top/bottom provisional Ohmic contacts; pGaN Mg active3e17 and nSi5e18 nominal reused; Wu DefaultParametersFromFile with NO local .par, no incomplete ionization, pilot PolAct0; old custom .par/IncompleteIonization and differing mobility/solver treatment. Wu no EBL/incomplete-ionization/PolAct0 are unverified simplifications, **not independently proven causes**; removing incomplete ionization alone would not ordinarily explain nearly zero holes when acceptor doping activates correctly. J plot width normalization affects reported J, not raw terminal current.
- **UNRESOLVED root cause:** material parameter files (including bandgap/offset/mobility), actual active donor/acceptor in saved mesh/TDR, electrode-to-region mapping, 5V eDensity/hDensity, quasi-Fermi levels and band barriers, heterointerface transport treatment. Strongest next action is read-only OFF n21_des.tdr doping/e/h/bands and compare ON n25_des.tdr; check Wu pp21_des.cmd, n21 runtime warnings and installed MaterialDB; do not change physics before this gate. Wu physical baseline not validated; Kou candidate separate; CMP4/V2 untouched.

## 2026-11-03 — Wu10 Clean5V n21 full solver success confirmed
- OBSERVED n21_des.log: NtSide0, PolAct0, Vstop5, anode=5.000V, electron2.596e-29, hole4.286e-30, total3.025e-29 raw, cathode -3.025e-29. Curve trace finished, n21_des.tdr saved, finished at 21:00:31 KST, 56.91s wallclock, peak638MB.
- Earlier OBSERVED n25_des.log: NtSide1e18 PolAct0 Vstop5, anode total5.810e-19 (electron1.722e-29, hole5.810e-19), finished 20:58:41 KST, 361.62s.
- Both 5V numerical sweeps complete; I_ON/I_OFF=1.921e10, dominated by tiny hole current in ON, not proof of working LED. Raw A/um unit/area-factor and physical Mg/polarization/contacts/EBL remain unvalidated. Stop additional parameter runs until existing TDR QW carrier/band/recombination distributions and ON 0V spike examined.

## 2026-11-03 20:58:41 KST — CMP_WU n25 NtSide=1e18 5V solver completed (OBSERVED log)
- User pasted actual school `/user/semi/semi437/tmp/myproject/CMP_WU/n25_des.log` tail. Final anode 5.000E+00 V, electron 1.722E-29, hole 5.810E-19, total 5.810E-19 (SDevice raw units); cathode total -5.810E-19. Thus terminal current is hole-dominated (hole/electron ≈3.37e10), but this does NOT independently prove absence of MQW electrons.
- Final Newton solve converged (error 6.1829E-02 < 1), `Curve trace finished`, `Writing plot 'n25_des.tdr' ... done`, simulation finished 2026-11-03 20:58:41 KST; wallclock 361.62s, CPU 149.23s, peak memory 640 MB. `sdevice`, `sdevice-traps`, `sdevice-hetero` checked in. **Confirmed 5V numerical completion for ON only**, not a working microLED/Wu physical reference.
- Wu10 `PolAct=0` pilot with provisional Mg active, EBL absence, simplified contacts, trap defaults; raw current extremely low. 10um width-normalized J would be 5.810e-12 A/cm² **only if** 2D current is A/um and AreaFactor=1. No physically validated injection, current mapping, QW radiative output or IQE.
- Next: read `n21_des.log` final 35 lines (NtSide0 clean 5V expected, verify mapping), then examine saved `n25_des.tdr` e/hDensity and bands/QW carrier injection and PLT zero-V spike; do not change decks based solely on current.

## 2026-11-03 ~21:49 KST — CMP_WU NtSide=0 Vstop=5 SVisual plot; compare clean vs damaged tiny currents (OBSERVED / PHYSICS UNRESOLVED)
- User screenshot of school SVisual T-2022.03 from `/user/semi/semi437/tmp/myproject/CMP_WU`: dataset `BaselineData_22`, legend `NtSide=0`, plotted 0→5V I–V ~`3.0e−29` (label A/um assumed) and J–V ~`3.0e−22` (label A/cm2 assumed). Previous `BaselineData_26` screenshot `NtSide=1e18` 5V I~`5.8e−19` and J~`5.8e−12` (both screenshot estimates).
- **Ratio** I_ON/I_OFF ~`1.9e10` at 5V from graph estimates; scientifically **NOT** a validated sidewall-recombination enhancement/loss because both currents essentially zero, true operating injection absent, trap ON low-bias spike unresolved. The `1e7` J/I conversion shown corresponds to Wu10 `Wmesa=10um` under assumed A/um and AreaFactor1; true units still need validation.
- `NtSide=0` I–V has no obvious sharp ON-type low-voltage peak; plot follows smooth but extremely small magnitude. `PolAct=0`, absent EBL, pilot active Mg/Ohmic contact etc may affect transport, but **none independently proven as root cause**.
- **Evidence level:** actual visual curve reaches 5V in displayed data; 5V SDevice solver normal-finish/contact current for clean `n21` and damaged `n25` NOT yet read from logs. Dataset ID22/26 strongly suggests node 21/25 previous SDevice, but confirm mapping from school SWB.
- **Next immediate read-only step:** user submit `tail -n 35 /user/semi/semi437/tmp/myproject/CMP_WU/n21_des.log` and equivalent `n25_des.log` for 5V completion/current. Then inspect raw `n21_des.plt`/`n25_des.plt` early V/I for ON spike, check actual SDevice units and dominant current/injection barriers via saved TDR and region-wise carriers before any code/parameter modification. No school files were edited here, no Wu paper calibration or final Baseline freeze.

## 2026-11-03 ~21:48 KST — CMP_WU Trap ON NtSide1e18 Vstop5V SVisual curve shown; current remains tiny (OBSERVED / RUN LOG PENDING)
- User screenshot of Sentaurus Visual T-2022.03 in `/user/semi/semi437/tmp/myproject/CMP_WU` displays dataset `BaselineData_26` with legend `NtSide=1e18`. Two curves extend to 5.0 V: I–V left ~`5.8e-19` A/um (screen label 'assumed') and J–V right ~`5.8e-12` A/cm² (screen label 'Width-normalized |J| [A/cm2] (assumed)'). These are **visual graph estimates**, not exact PLT or final solver values; user's statement "다 돌아갔다" refers to shown visualization. Previous SWB screenshot showed n25 SDevice running; n26 dataset likely corresponding SVisual, but verify actual node mapping/log before asserting final solver finish.
- Current plot J/I ≈`1e7`, consistent with **10um** normalization `1e8/10` and previous code fix; this confirms apparent postprocess scaling, NOT that SDevice 2D raw current is independently verified as A/um or real 3D pixel current density.
- Red curve has a narrow anomalous bump near low V (<0.3V), previously visible at 0.1V NtSide1e18. Cause unverified; inspect first points in `n25_des.plt` and log. At 5 V, current still **extremely small**; no convincing LED turn-on, QW emission or physics-calibrated baseline established. `PolAct=0`, trial Mg/contacts/traps/EBL persist.
- **NEXT single diagnostic:** user run `tail -n 45 /user/semi/semi437/tmp/myproject/CMP_WU/n25_des.log` to confirm actual 5V solver finish, terminal current and warnings. If run complete, inspect ON raw PLT points near 0V; compare NtSide0 5V only when its solver result exists and note matched-current physical comparison requirement. Do not rerun/rewrite solver solely based on visualization; 4um CMP/Kou/Lee baseline not touched.
- No school code modified in this turn. Preserve all results and distinguish visual success from physically functioning diode.

## 2026-11-03 ~21:46 KST — CMP_WU Vstop=5V higher-bias runs launched, n25 in progress (OBSERVED screenshot)
- **User decision:** After successful `Vstop=0.1` Wu10 smoke, set up `Vstop=5` runs; if numerical advance becomes excessively slow, evaluate reducing test stop to `4V` or `3V` **only after inspecting the latest converged log**. No time estimate or unverified pass/fail threshold adopted.
- **User-provided school SWB screenshot OBSERVED:** `/user/semi/semi437/tmp/myproject/CMP_WU` has six rows with `NtSide=0,1e18,1e17`, `PolAct=0`, each with `Vstop=0.1` and `5` experiments configured. `Node n25 Output` visible during `Vstop=5` run, actual Quasistationary pseudo-time `t=0.203799→0.223799`, last printed anode `1.019E+00 V` and current `5.602E−21` raw, cathode negative counterpart. Newton at this stage reports `Error smaller than 1.2238E−01` and continues to next step. **No 3V/4V/5V pass, measured LED turn-on, solver termination or IQE result observed.** The node-to-NtSide binding should be checked in PP if needed; do not infer node n25 condition from screenshot alone.
- **Guidance:** Preserve ongoing run if voltage/accepted pseudo-time advances and solver converges. If stalled, check `n25_des.log` last accepted anode voltage, timestep, cutback/Newton messages and stop reason before aborting. Changing Vstop and running a new SWB split is generally a fresh Quasistationary solve; it does not by itself resume from an existing 5V trace. Avoid concurrent multiple 5V jobs if licence/CPU limited.
- **Known limitations unchanged:** `PolAct=0` numerical smoke setting, pMg/EBL/contact and 2D J normalization not physically validated; Wu10 SVisual1 correction proposed but not confirmed on school server. Existing 4um baseline and Kou candidates untouched. No school source code changed by ChatGPT.

## 2026-11-03 — Wu10 SVisual1 4um→10um correction, SDE/SDevice1 independent static audit (PROPOSED FIX)
- **User request:** deliver corrected SVisual1 specifically for the Wu 10um candidate and verify preceding SDE/SDevice1 source. Avoid mixing with older CMP4um transfer ZIP, which contains a different epistack.
- **Code actually COMMITTED:** `CMP/tcad/candidates/CMP_BASELINE_3.0.0_WU10FULL/svisual1_iv.tcl` (new, commit `a504f60`), SVisual1 v1.1 with `Wmesa=10.0` instead of old `4.0`, unique Wu10 IV/JV/CSV names and source voltage/current preserved (including 0 V anomaly). This corrects geometric normalization **conditional on** raw 2D `A/um`, `AreaFactor=1`: J=abs(I)*1e8/10, 0.4× old displayed 4um-normalized J. Material SDE/SDevice source unchanged. Tcl basic syntax and derived data validated in local **mock** T-2022.03 visual-command simulation, NOT actual Sentaurus new-code execution.
- **SDE source static audit OBSERVED:** candidate `sde_dvs.cmd` has Full 2D width10um; both sidewall damage bands 0.005um; 4×In0.08GaN QWs 0.003um and 5×GaN QB0.008um; nGaN3.9um; total stack 4.072um (includes pGaN0.12um). No EBL (tEBL=0); p Mg active3e17, background1e15, full-width top/bottom Ohmic contact are pilot choices, NOT paper-faithful verified. Source partitions intended 36 regions. Full 2D stripe is NOT 10×10um2 square.
- **SDevice1 source audit + runtime OBSERVED:** `DefaultParametersFromFile` global Physics is present (committed prior `066bbc3`, also user confirmed in school pp2). Fermi, recombination SRH/Radiative/Auger, mobility, PolAct parameterization and 24 assumed acceptor trap regions correspond to SDE region labels. User's actual `CMP_WU/n2_des.log` for NtSide0 PolAct0 Vstop0.1 reached `0.100 V`, `+8.387e-31` raw anode / `-8.387e-31` cathode, `Curve trace finished`, `n2_des.tdr` saved, normal exit Tue Nov 3 20:30:09 KST. School ON NtSide1e18 SVISUAL plot screenshot exists, ON solver log not separately audited; abnormal near-0V spike UNRESOLVED.
- **No physical Baseline freeze:** PolAct0 and omitted Mg incomplete-ionization were pilot numerical smoke assumptions; actual active/free-hole concentrations, EBL/contact physics, trap values, quantum transport, mesh/allele/doping map, polarization, current units/AreaFactor, high-V injection, radiative/SRH and matched-current trap loss unvalidated.
- **NEXT:** Paste/run new Wu10 SVisual1 Tcl only using saved SDevice PLTs, check axes/CSV and near-0V PLT points. Separately confirm ON SDevice finish and dimensional current unit, then plan voltage extension cautiously. Do NOT rerun SDE/SDevice to correct plotting width, and do not alter CMP4um/Kou/Lee model.

## 2026-11-03 ~21:30 KST — CMP_WU NtSide1e18 SVisual1 low-bias plot visible (OBSERVED screenshot / solver log pending)
- User provided school Sentaurus Visual T-2022.03 screenshot from `CMP_WU`: dataset `BaselineData 12`, red legends `NtSide=1e18`, 0–0.1 V I–V and J–V plots. This is a real **SVisual plotted result** for Trap ON; school SDevice log for this branch **not yet provided**, so do not report confirmed solver completion/time or physical accuracy.
- Screenshot approximate at 0.1V: I ≈ `4e-22` A/um as labeled; J ≈ `1e-14` A/cm² as labeled. Prior clean `NtSide=0` branch reached 0.1V with logged total anode current `8.387e-31` raw. These are extremely small 0.1V currents; higher ON current is NOT evidence of improved LED performance or calibrated sidewall damage response.
- **Visual anomaly UNRESOLVED**: near 0 V, an apparent sharp red vertical spike reaching ~`6.5e-22` A/um and `1.6e-14` A/cm² before returning toward 0. Potential initial/bias duplicate point or trap-related numerical behavior; do not assert root cause without PLT and n*_des.log. Check exact voltage/current pairs near start, solver progress.
- **Known postprocessing mismatch STILL OPEN**: screenshot J/I≈`2.5e7`, corresponding to previously pasted `Wmesa=4` while Wu10 mesa is `10um`. With verified raw 2D current A/um and AreaFactor=1, change only Wu SVisual code to `Wmesa=10.0`, then displayed J rescales to ×0.4. 2D units still require verification. Leave protected CMP4/Kou/Lee project inputs unchanged.
- **Next:** inspect corresponding Trap-ON `n*_des.log` tail for 0.1 V finish and warnings; inspect initial points in `n*_des.plt`; correct Wu SVisual1 width and replot (no SDevice rerun necessary); do not advance to physical baseline claim on 0.1V plots alone. No school code was changed by ChatGPT in this event.

## 2026-11-03 — CMP_WU node n2 0.1V clean smoke **confirmed finished** from real log (OBSERVED)
- User pasted `tail -n 35 /user/semi/semi437/tmp/myproject/CMP_WU/n2_des.log`. Terminal end shows last `Computing step from t=0.984303 to t=1`, Newton `|RHS|=8.20e-12 < 1e-10`, anode `1.000E-01 V`, anode electron `7.544E-31`, hole `8.430E-32`, total conduction `+8.387E-31`; cathode total `-8.387E-31` (log raw current units; geometry/2D density normalization still unverified).
- `Curve trace finished.`, `Writing plot 'n2_des.tdr' (TDR format) ... done.`, `Sentaurus Device simulation finished (Date: Tue Nov 3 20:30:09 2026 (KST)).`, licence check-ins for sdevice-hetero, sdevice-traps, sdevice. peak memory **632MB**, wallclock **423.72s** (~7m03s), CPU **41.39s**. No UNDEFINED models reported in last part; low-bias 0.1V task finished. Prior screenshot SVISUAL 1 plotted IV/JV up to 0.1V.
- **Status:** Wu10 candidate `NtSide=0, PolAct=0, Vstop=0.1` SDevice solver + SVisual1 smoke **CONFIRMED finish** (not just plot); **NOT** physical LED turn-on/IQE/Wu-model validation. Current ~8.387e-31 is effectively zero; no actual forward injection established. `NtSide=1e18` separate run not confirmed. One successful licence checkout says no enduring guarantee of availability.
- **Open caution:** earlier SVisual1 used `Wmesa=4` while Wu width is 10um, so update *Wu SVISUAL ONLY* to `10.0` and confirm actual SDevice 2D output units/AreaFactor before reporting J. This change does not require SDevice rerun. Preserve CMP4 baseline and Kou/Lee projects.
- **NEXT:** correct Wu10 postprocess width and rerun only SVisual, inspect log output unit conventions; then separate NtSide=1e18 same 0.1V smoke and deliberate bias/injection physics testing. Final baseline not fixed.

## 2026-11-03 ~21:20 KST — CMP_WU NtSide0 0.1V SDevice→SVisual1 plot obtained; Wu10 J normalization mismatch (OBSERVED / PARTIAL PASS)
- **User SWB screenshot OBSERVED:** `/user/semi/semi437/tmp/myproject/CMP_WU`, dataset `BaselineData 6`; SVisual displays I–V/J–V red curve `NtSide=0` extending 0→0.1 V, user confirms SDevice/SVisual1 resumed after licensing wait. Previous `UNDEFINED model` prevented execution; `DefaultParametersFromFile` confirmed in school's `pp2_des.cmd` line22 in preceding terminal. This is a **low-bias procedural smoke pass**, not an independently verified solver finish/log audit or validated forward LED operation.
- **Values visually estimated:** I(0.1V) ≈8.5e−31 A/um; displayed J(0.1V) ≈2.1e−23 A/cm². The displayed J/I scale ≈2.5e7 corresponds to `Wmesa=4um` normalization in earlier chat SVisual1 code, but this Wu10 SDE is **10um** lateral width. Conditional on SDevice current units being A/um, area factor1 and stripe uniformity, use `Wmesa=10.0` → corrected J≈8.5e−24 A/cm² (~0.4× displayed). Actual dimensional units/AreaFactor NOT independently audited; do not report plotted J as calibrated.
- **What is NOT established:** `NtSide=1e18` row completion, high-voltage LED injection, QW1–4 distributions, physical polarization/Mg/trap parameters, matched-current SRH loss, IQE, fully validated Wu replication or final baseline. The plotted current is effectively numerical-zero at 0.1 V and uninformative for turn-on.
- **Changes:** Candidate README status and runtime/normalization note updated in commit `08a0208`; prior GitHub `sdevice_des.cmd` single-line proposed fix commit `066bbc3` remains. No user's school source file automatically changed by GitHub; no server access to edit/validate. Existing CMP4um/Lee/Kou decks untouched.
- **NEXT:** inspect `n2_des.log` terminal finish/target 0.1V; edit *only Wu10 SVisual1* local Tcl `set Wmesa 4.0`→`10.0`, rerun just SVisual, check current units; after status gate compare NtSide0 and 1e18 low-bias smoke then cautious bias/injection checks. Avoid unnecessary SDevice rerun before license availability.

## 2026-11-03 ~21:09 KST — CMP_WU first SDevice runtime: license checkout succeeded, GaN/InGaN UNDEFINED material models (OBSERVED / PROPOSED FIX)
- School screenshot: `/user/semi/semi437/tmp/myproject/CMP_WU/n2_des.out` and `n2_des.err`. SWB NtSide=0, PolAct=0, Vstop=0.1. SDevice log at Tue Nov 3 20:19:12 2026 shows `checked in 1 sdevice-traps license(s)`, `checked in 1 sdevice license(s)`: prior license WAIT no longer blocks this **one execution** (other users/host not verified).
- Runtime blocker (OBSERVED): `Region "Clean_pGaN" (Material "GaN"): UNDEFINED model "Bandgap", "eDOSMass", "hDOSMass", "Scharfetter", "Auger", "RadiativeRecombination", "ConstantMobility", "DopingDependence"`; similar across Dmg GaN/InGaN. SDevice stops before electrical validation. No successful 0.1V/I-V result.
- GitHub Wu10 pilot `CMP/tcad/candidates/CMP_BASELINE_3.0.0_WU10FULL/sdevice_des.cmd` previously omitted `DefaultParametersFromFile` and a local `.par` override. Minimal **PROPOSED**, not yet server-tested patch adds global `Physics { DefaultParametersFromFile ... }`; commit `066bbc3`. Do not disable `CheckUndefinedModels`, do not fabricate GaN numbers, no SDE or other baseline changes.
- NEXT: user applies one-line patch to school's SDevice command (GitHub change is NOT automatically deployed), inspect installed MaterialDB GaN.par/InGaN.par, preprocess and rerun same clean low-bias smoke. If undefined persists, read first material parameter warnings, exact `pp2_des.cmd` and MaterialDB resolution before any physics change. Kou candidates/Lee project untouched.

## 2026-11-03 — 주수빈 Kou 원문 수치 재검토 / 20um Full3D SDE 코드 신규 작성 (PROPOSED, NOT RUN)
- 사용자 정정: 기존 Kou4 4um mesa/5nm 손상 폭은 CMP 임의 목표였으며 Kou 논문 재현 모델에 쓰면 안 됨. 기존 `CMP_BASELINE_3.1.0_KOU4FULL`은 **Kou 원문 재현 용도로 철회**, 단 과거 CMP4 후보로는 보존.
- 문헌 확인: Kou 2019 Optics Express DOI 10.1364/OE.27.00A643 Section2 Fig1: 20×20/60×60/100×100um², 측벽 손상 안쪽 폭 4um, 20um 소자는 Clean core 12×12=36%; nGaN4um Si5e18, QW4×3nm In0.15, QB22nm, EBL26nm pAl0.15, pGaN120nm, p+ contact GaN20nm, pGaN/EBL hole3e17.
- **새 독립 코드 실제 GitHub 커밋 (시뮬레이션 미실행):** `CMP/tcad/candidates/CMP_BASELINE_4.0.0_KOU20FULL3D/sde_dvs.cmd` (commit 55d431d)와 README (9d9deba). 20×20 square 3D damage ring, central 12×12, 13층 × 9타일 =117 cuboids; 5개 QB를 가정한 수직 총 두께 4.288um. Scheme 괄호 정적 체크만 완료.
- 중요한 미확인: 원문에서 고농도 p+ Mg 구체값 없음 → pPlusPilot1e19 가정; p/EBL hole3e17 ≠ MgActive3e17 실제 동치 아님; 전면 상/하 Ohmic contact는 임시이며 원문 Fig7 p-contact 4um 그림과 다름; 4 QW에 GaN barrier 5개 배치 가정, 실제 원문 확인 필요. 3D SDE Mesh/SDevice/트랩/양자모델/Sentaurus 호환성 실행 미확인. 기존 Kou4 SDevice는 새 코드에 호환되지 않음.
- **NEXT:** SWB에서 신규 `CMP_BASELINE_4.0.0_KOU20FULL3D` SDE만 전처리/mesh; 117 region, 4um ring, QW/EBL/p+ 층, contact, 3D mesh 요소수/메모리 검증. 3D 자원 문제가 크면 사용자에게 2D 근사 시 36%→60% 면적 차이를 명시 후 분리 진행. SDE 통과 이후 Kou20에 맞는 SDevice 제작.
- 보호: Wu10 후보, 이택규 POL0 프로젝트, `CMP/COMMON_BASELINE.md` 미변경. 현재 최종 Baseline은 미선정.

## 2026-11-03 — 주수빈 Kou4 SDevice pilot code added (CODE COMMITTED, NOT RUN)
- `CMP/tcad/candidates/CMP_BASELINE_3.1.0_KOU4FULL/sdevice_des.cmd` added; matching Full2D SDE region names with SWB `NtSide`, `PolAct`, `Vstop`. One SDevice can run separate clean and damaged parameter splits; no SDevice2/SVisual2 required for first smoke.
- Initial proposed syntax/solver smoke AFTER SDE mesh pass: NtSide=0, PolAct=0, Vstop=0.1. Not an LED operating-point or physics validation.
- Uses provisional CMP volumetric 5nm trap-host regions and inherited pilot physics; Kou original surface recombination formulation NOT reproduced. EBL/pGaN/contacts/Mg/MaterialDB and current normalization remain blockers. No server run or parser verification.
- NEXT: SDE preprocess/mesh audit, then SDevice clean smoke log and effective PP inspection. Do not claim baseline freeze.

## 2026-11-03 ~20:46 KST — JuSubin Kou4 Full2D SDE candidate created (PROPOSED / NOT RUN)
- USER DECISION: Wu and Kou candidates separately run, then choose final Baseline based on validated simulation quality; this chat concentrates on Kou.
- CODE COMMITTED: `CMP/tcad/candidates/CMP_BASELINE_3.1.0_KOU4FULL/sde_dvs.cmd` and `README.md`; independent Full 2D 4µm CMP Kou-derived stack (4×3nm In0.15GaN QW, 5×22nm GaN QB, 4µm nGaN, symmetric 5nm trap-host strips); original old shelf deck not copied.
- PROVISIONAL and NOT Kou exact published replication: pGaN 0.12um, EBL absent, active Mg 3e17, donor 5e18, background 1e15, full-top/bottom Ohmic contacts, 5nm damaged strips; SDevice, trap model and calibrated physical defaults are not created/verified. No school-server run, mesh nor results observed.
- NEXT: create independent school SWB project, SDE-only preprocess and build, inspect effective geometry/contacts/QWs/mesh and logs, then Kou-specific SDevice after SDE pass. Wu candidate unchanged; physical Baseline not fixed; matched-4um geometry/J comparison needed.

## 2026-11-03 ~20:46 KST — Simplify Wu10 SWB node count for time; keep distinct clean/damaged data (USER PROPOSED / NO RUN)
- **Worker:** 주수빈. Asked whether SDevice2 and SVisual2 are essential or can be omitted due to time.
- **GPT recommendation:** For first clean smoke use SWB **SDE → SDevice** only; no SVisual script necessary, visualize completed .tdr/.plt manually later. A separate SDevice2 is **not required**: existing single SDevice cmd uses `@NtSide@`, so run `NtSide=0` Clean first, and after model checks run `NtSide=1e18` Damaged with separate SWB parameter split/experiment or preserved separate job outputs, ensuring matched physical inputs and saved individual files. **Do not omit the damaged test itself**: Clean/Trap ON current-matched comparison is mandatory before calling it a sidewall-loss Baseline. `NtSide=1e18` remains pilot CMP value, not confirmed Wu density.
- **No physical design/code changes** or node deletion executed by assistant; user may simplify current SWB diagram. Existing GitHub candidate sources `CMP/tcad/candidates/CMP_BASELINE_3.0.0_WU10FULL` unchanged. SDE mesh `done` not independently verified in current chat yet; do not start SDevice if SDE mesh absent. First proposed smoke `NtSide=0, PolAct=0, Vstop=0.1` only proves numerical parser/low-bias operation, not credible Wu LED; missing p/EBL/contact/Mg/Trap calibration and QW4 remain.

## 2026-11-03 ~17:43 KST — JuSubin requested code: new Wu-inspired Full10 2D SDE/SDevice draft actually COMMITTED; NOT RUN
- **User direction:** "우선 Wu 논문 기반으로 코드 짜자". Worker 주수빈. New independent project candidate `CMP_BASELINE_3.0.0_WU10FULL` created under `CMP/tcad/candidates/`, not copied from old V2 shelf clone. GitHub source files `sde_dvs.cmd`, `sdevice_des.cmd`, `README.md` committed separately; **code creation CONFIRMED by GitHub commits, local Sentaurus execution NOT DONE**.
- **Wu source directly supported:** W10µm, n-GaN3.9µm, n donor5e18, 4 In0.08 QW3nm, GaN QB8nm, sidewall-host strip5nm each. **PILOT, NOT Wu:** pGaN thickness0.120µm, p active Mg3e17 (NOT Wu chemical Mg2e19), barrier background n1e15, EBL disabled until source confirmed, full-width top/bottom ohmic contacts, CMP-Ev+0.75 trap/Nt1e18/σ1e−15, PolAct=0 numerical smoke, built-in MaterialDB values unverified. No mixing these guesses into an asserted exact Wu replica.
- **Workflow:** Full2D Cartesian width10µm, 33 partitioned semiconductor regions incl 22 DmgL/R trap-host regions, 4 QWs + 5 QBs, full left/right edge strips, xMoleFraction0.08; mesh windows for 3nm wells/5nm strips, contact boundaries. SDevice `NtSide`=0/1e18 for OFF/ON, `PolAct` and `Vstop` additional SWB params; 0.1V OFF/PolAct0 suggested **smoke-only** not a valid physical LED run.
- **Static source audit:** GitHub content checked: Scheme parentheses balanced, SDevice braces balanced, 22 unique regionwise trap names and SWB macros present, layer depth4.072µm mathematical sum, BUT this does **not** validate T-2022.03 parsing or simulator convergence. Wu original p/EBL/contact and complete trap data, Mg incomplete-ionization, quantum model, material interpolation/parameters and optical spectrum need source verification before physical reference/Project A/B.
- **Immediate NEXT for JuSubin only:** create new SWB project named candidate (check actual school names), paste SDE input first and run SDE node alone; inspect real SDE preprocessing, mesh quality, material names, contact placement, 5nm strips and QW geometry. Capture actual log/pp and only after pass consider SDevice NtSide0 PolAct0 Vstop0.1; STOP if SDE fails. Original `CMP/COMMON_BASELINE.md`, Lee POL0 work, member B project unchanged. No real run or freeze.
- Public source: https://github.com/TaekGyu0801/GGYU/tree/main/CMP/tcad/candidates/CMP_BASELINE_3.0.0_WU10FULL . Literature DOI https://doi.org/10.1016/j.micrna.2023.207542 .

## 2026-11-03 — 주수빈 directs locking sidewall recombination LOSS validation metric before setting geometry (USER PRIORITY; GPT NUMERIC CUTS PROPOSED, NO RUN)
- User requests: define an **evaluable amount of sidewall nonradiative emission loss**, not simply “what % of the device is Damaged” before choosing Kou/Wu or Wdmg.
- **Primary metric proposal:** at **matched J** and same 300K/epi/contacts, `η_rad,current=q×[∫QW1−4 Rrad dV]/Iterminal` with validated 2D integration/area factor, then `L_sw=(η_clean−η_dmg)/η_clean×100%`. Distinguish from QW-only 3-channel rad fraction and measured EQE; includes altered injection and leakage. Define independently `F_gap,Dmg=q∫Dmg R_gap,net dV/I_dmg×100%`, with correct no-double-count trap rate, to prove sidewall trap mechanism. Require regionwise lateral e/h depletion/current and all-channel balances.
- **Proposed screening convention, NOT externally validated paper/calibration:** 20–40% relative Clean→Damaged loss as useful but not mandatory A/B proof-of-concept range; <10% may be low-sensitivity, 10–20% usable, >40% check excessive injection collapse, >60% extreme caution; never tune Nt or Wdmg just to hit numeric target. **User accepted defining evaluation first, has not specifically approved these numeric thresholds.** Baseline physics validity/reproducibility always dominates the convenient loss range.
- **Proposed operating reference:** 20 A/cm², 300K, Kou J20Acm² source reference; 5 A/cm² secondary only where both curves have common converged J (no extrapolation). Full/Half, 2D stripe versus square current units/normalization need explicit approval and result verification. QW4 OFF anomaly still a gate.
- No new simulation, code, or alteration of protected common Baseline. Full scientific design memo `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`. Sources Kou 10.1364/OE.27.00A643, Wu 10.1016/j.micrna.2023.207542 and current-normalized recombination literature.

## 2026-11-03 — Wu Baseline Full versus Half design recommendation (PROPOSED / NO RUN)
- Worker 주수빈 asked whether new Wu-size10µm then scaled4µm A/B comparison should be FULL or HALF. GPT recommends **Full 2D first** (10µm full with two modeled 5nm damaged sidewalls, assuming Wu source geometry supports two symmetric sidewalls) to verify electrode/mesa geometry, full lateral current, region identities, input physics/mesh, short clean-run behavior and asymmetry. Full is **not 3D/square four-wall geometry**.
- HALF 5µm (for Wu10) or2µm (for scaled4) permitted *only* if geometry/contact/defect/A/B intervention/polarization/BC are mirror-symmetric and after one representative Full/Half comparison: same normalized J; raw I_full≈2I_half with identical out-of-plane/AreaFactor, region-total recombination≈2x, identical QW shares and central/lateral fields/maps. Artificial centerline must have no physical damage/contact, verified zero normal current; do not double AreaFactor. Old CMP Half Full equivalence was never completed.
- Both-sided GaN:C or AlGaN symmetric interventions can be safely tested in validated Half; one-side treatment or asymmetric electrode/Wu C-shaped anode needs Full. New Full does not solve QW4 transport, current units or mesh flaws automatically. Full mesh of 5nm strips will cost more, so test SDE+mesh and quick Nt0 before full sweep.
- Current COMMON_BASELINE 4µm/5nm, Lee PolAct work and T-2022.03 inputs are protected; this is research recommendation not user final numerical adoption, and no new source/run. Further details: `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`.

## 2026-11-03 — JuSubin asks what Wu rebuild actually changes and whether past CMP Baseline failures will recur (RESEARCH ANALYSIS / NO RUN)
- Existing V2.1 source: Kou 4µm mesa 4×In0.15GaN QWs3nm/22nm GaN barriers, nGaN4µm plus independent Wu-inspired 5nm sidewall trap and CMP model parameters; Half2µm, mesh/shelf/contact/current-normalization, QW4 dominance even Nt0/PolAct0 are independently unresolved.
- Proposed Wu rebuild: original Wu 10µm 4QW In0.08GaN QW3nm/8nm GaN barriers, nGaN3.9µm, Mg chemical input2e19, 5nm defect-placement strip, actual original Wu trap values/contacts/p/EBL and simulator details still require full source verification. Scaling back to 4µm with5nm **does not change original geometric damage fraction** (ideal four-side square0.499375%; planar stripe0.25%); Wu10µm fraction0.1999% is lower. Mechanism-driven impact must be measured, not inferred from strip area.
- Rebuilding may improve single-source physics consistency and thinner-barrier interwell injection, but latter is UNPROVEN; does NOT automatically cure QW4 trapOFF localization, lack of quantum/capture models, mesh pathologies, n-GaN shelf contact errors, bias-target completion, area factor or matched-current comparisons.
- GPT recommendation PROPOSED: exact Wu Methods/parameter/source-equivalence audit before full code; SDE/mesh/material/contact QA; clean NtOFF 10µm short run verifying layers, actual target current/voltage and QW1–4 injections; only then damaged ON with matched-I maps; scale to4µm, A/B under frozen damaged parent, compare whole-device rate/current, losses, QW volume, voltage. Kou20 remains fallback if critical Wu values unavailable.
- No guaranteed simulation success, no school server code/job, original COMMON_BASELINE or Lee work changed; details `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`. Wu source DOI 10.1016/j.micrna.2023.207542, Kou DOI 10.1364/OE.27.00A643.

## 2026-11-03 — JuSubin challenges Wu 10um vs CMP 4um 5nm: physical damaged area does NOT equal effective sidewall impact (SOURCE VERIFIED + DERIVED / NO RUN)
- **Question:** selecting Kou20µm/4µm dead-zone might expose stronger damaged-LED loss for Project A/B than Wu10µm/5nm, since Wu 10 is larger than existing CMP4 with the same 5nm damage; asks for objective baseline selection based on ability to show sidewall mitigation.
- **Derived square footprint:** CMP4µm with 5nm strips 0.499375%, Wu10µm with 5nm strips 0.1999% (4µm geometry has 2.5× greater damaged-area fraction and square perimeter/area); Kou20µm with model-wide 4µm effective dead zone64%. A 2D planar stripe includes only two lateral edges and ratios0.25/0.10/40%; do not treat 3D square fractions as solved original cross-sections.
- **Primary source verification:** Wu Methods defines 10µm as an EXAMPLE, studies multiple LED sizes and 5nm localized acceptor traps plus sidewall depletion/lateral current dispersion; Kou 4µm is a modeled equivalent damaged *dead zone*, not measured physical etch penetration. Distinct quantities cannot be compared as if all are etched damage thickness or direct IQE damage fractions. 2025 LSA review documents nm-level structural damage versus greater electrical/optical extent; Wang2023 Optics Letters observed some 10µm LEDs almost fully affected by sidewalls under its fabrication conditions.
- **Prior CMP V2.1 evidence:** 4µm/5nm Trap ON at same3.6V yields trap eGapStates equivalent to ~34.45% terminal current (2D normalization conditional), so narrow zone is not automatically inactive. This is NOT 34.45% area, not matched-current IQE decrease or proven physical trap validity; QW4 persists even trapOFF.
- **Updated independent recommendation PROPOSED:** Wu-size L10µm full original conventional model for validation, then *same complete Wu epi+5nm trap physics* in L4µm scaled separate candidate for stronger surface-to-area Project A/B test; preferably run 4 and10 as size pair, same damaged controls, matched-current loss, absolute QW photon rate, voltage/injection costs and regionwise depletion/Trap maps. Do NOT select Kou20µm based solely on numerical64% dead-zone; unrealistic overwide zone may distort A/B or active volume. Wu full parameters/actual simulator and 4um geometry/effective 2D units must be verified; old 4um code not reused by default.
- User/team have not formally approved replacement of protected CMP COMMON_BASELINE. No source, server run or simulation performed. Full audit: `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`. Sources DOI 10.1364/OE.27.00A643, 10.1016/j.micrna.2023.207542, 10.1038/s41377-025-01751-y.

## 2026-11-03 — Primary Kou vs Wu independent comparative baseline source review (SOURCE VERIFIED + RECOMMENDATION PROPOSED, NO RUN)
- Worker 주수빈 asked for objective selection of which paper's FULL device numerical parameters should define the A/B TCAD comparison Baseline, after considering Kou 20um and Wu 10um alternatives. GPT verified Kou primary open text/PDF and Wu publisher methods/extended abstract, cross-checked previous GitHub assumptions.
- **Kou** APSYS 20/60/100um blue 4QW In0.15/3nm, GaN 22nm QB, 26nm Al0.15 EBL, 120nm pGaN+20nm p-contact, modeled *4um* damaged zone per sidewall (~64% modeled 20um square affected region). Distinct electron/hole traps (Ec−0.24; EV+0.46 stated but competing text says Ev+0.6), and SRH100ns/Auger1e−30/70:30 offset/LEE88.1. Publishes 20µm clean vs damaged J-V at J20Acm−2 of 3.33V and3.23V. **Strength:** accessible numerical reference and reproducibility of published trends; downside very wide effective damage region, APSYS not Sentaurus, full executable model not provided.
- **Wu** TCAD 10um *example* 4×In0.08 QW3nm/GaN QB8nm, nGaN3.9um Si5e18, pGaN Mg2e19 input, 5nm acceptor-like edge traps, polarization/Mg-ionization/local-field capture/Rad-SRH-Auger; mechanistically studies depletion, lateral currents and recombination, proposes optimized C-shaped anode. **Strength:** best match to localized edge engineering research question. **Missing verified:** exact simulator brand, full numerical contacts/p/EBL geometry, traps Et/Nt/sigma and full deck, so cannot simply paste in Sentaurus or claim exact Wu reproduction.
- **Independent recommendation (not a final group decision):** for A/B mechanism POC, **Wu 10um original ordinary-electrode whole-device baseline is preferred SCIENTIFIC candidate**, but freeze/code only after obtaining and auditing complete Wu parameters. If unavailable, **Kou 20um III/C is superior documented numerical fallback**, with clear 4um modeled damaged zone caveat. Do NOT secretly combine Kou In15/QB22 with Wu 5nm and call it reproduction. Neither necessarily fixes the old QW4 at trapOFF. A/B must share matched-current damaged parent, report absolute photon-generation per current, trap/nontrap loss, voltage, emission volume and 2D normalization, then test size/depth sensitivity.
- GitHub original common 4um/5nm source of truth and Lee experiments unchanged, no SDE/SDevice file/run, no team scope adoption. Detailed audit in `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`.
- Primary sources: https://doi.org/10.1364/OE.27.00A643 ; https://doi.org/10.1016/j.micrna.2023.207542 .

## 2026-11-03 ~16:22 KST — JuSubin proposes Wu 2023 full TCAD Baseline instead of Kou 20um (USER PROPOSED / NO RUN)
- User asks whether using **Wu et al. 2023's entire device** rather than only its 5nm defects makes Project A/B feasibility TCAD more straightforward than Kou-based 20um candidate, because Wu used TCAD.
- Primary publisher text source DOI 10.1016/j.micrna.2023.207542 verifies Wu models 10um LED example, nGaN3.9um/nSi5e18, four QWs In0.08 3nm, GaN barriers8nm, pMg2e19, 5nm acceptor traps each side; polarization/Mg incomplete ionization/local-field trapping/SRH-Rad-Auger modeled; C-shaped anode improved lateral current distribution as paper's proposed intervention.
- **Critical correction:** Kou also used TCAD numerical modeling with APSYS. Wu's exact tool name (Sentaurus or otherwise) and executable SDE/SDevice deck **NOT CONFIRMED** by source examined. Wu source values still incomplete for exact reconstruction (contact geometry, EBL/p thickness, full traps and other material parameters); adoption therefore does NOT itself guarantee easier/reproducible solver.
- **GPT assessment PROPOSED:** Wu 10um original ordinary-anode clean/damaged pair may be the *more relevant mechanism baseline* for localized 5nm traps and sidewall depletion/lateral-current loss. Do not copy Wu's already-optimized C-shaped anode as baseline. Validate full source parameter/provenance and effective T-2022.03 physics -> 10um trap OFF/ON matched current model -> A/B one-factor relative to frozen damaged control -> optional 4um scaling. The Wu In8%/barrier8nm stack differs substantially from Kou 15%/22nm, with optical properties requiring reevaluation; do not call hybrid a Wu replica.
- **Status:** User proposed alternative; not formal team approval/replacement of protected COMMON_BASELINE 4um/5nm; Lee PolAct tasks unaffected. New coding/simulation not performed. Full audit in `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`.
- Source DOI https://doi.org/10.1016/j.micrna.2023.207542 and Kou https://doi.org/10.1364/OE.27.00A643.

## 2026-11-03 — Kou explicitly sets 4um modeled damaged width; proposed two-tier trap reference (PRIMARY SOURCE VERIFIED / NO RUN)
- **Worker:** 주수빈. Asked how to define damaged region logically if Kou paper was thought to leave it unspecified for new 20um Project A/B POC. **Correction:** Original Kou 2019 *Optics Express* §2 (p.A645) explicitly states the damaged region depth/width is **4µm** at each mesa sidewall, and Fig1 20µm LED C has central usable width12µm, usable area36%, modeled damaged area64%. Previous assistant wording “not clearly set” was wrong regarding width; actual etched crystal defect penetration and spatial trap distribution are NOT measured/proven in that paper.
- Kou §2 defines distinct electron trap Ec−0.24eV/σ3.4e−17cm²/N1e13cm−3, hole trap reported ambiguously 0.6eV above Ev vs Ev+0.46eV/σ2.1e−15cm²/N1.6e13cm−3. Exact APSYS/Sentaurus mapping, 4um p-contact and other geometry must be audited before implementing.
- **GPT-recommended PROPOSED design:** use 20um Kou LED III clean and C damaged with original **modeled 4um** lateral zone and Kou trap inputs as literature-reproduction baseline; test A/B modifications relative to the same damaged parent and current. Add independent width sensitivity cases (e.g., 0.5, 1, 4um) at same nominal trap settings to expose robustness/sensitivity, with original 4um at reference. A Wu-inspired **5nm** region is *separate independently calibrated model*, not a Kou numerical replica or an automatic replacement. Large modeled damaged share may exaggerate A/B improvement; must include emitting-volume and voltage penalties and ensure intervention physically plausible. 4um is not the measured etch-defect penetration.
- Existing 4um CMP COMMON_BASELINE is **protected**, user/team has not yet finally approved scope change; no physical input deck, server output or new result. Details in `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`.
- Primary paper PDF §2/Fig1 DOI https://doi.org/10.1364/OE.27.00A643; LSA review https://doi.org/10.1038/s41377-025-01751-y.


## 2026-11-03 ~16:22 KST — 주수빈 proposes Kou-size Baseline proof-of-concept for A/B instead of mandatory 4um JBD model (USER PROPOSAL / NO CODE OR RUN)
- **Worker:** 주수빈. User identifies actual CMP goal as evaluating feasibility/applicability of GaN:C Project A and AlGaN Project B sidewall-loss reduction, not exact CES JBD 4um pixel-size reproduction. Proposes adopting Kou 2019 original device dimensions/physics as new Baseline and comparing both techniques on it.
- **GPT research assessment (PROPOSED):** sensible to benchmark Kou's smallest **20um clean LED III vs damaged LED C**, verify same-device I–V/QW carrier/recombination trend in Sentaurus (Kou originally APSYS), freeze an identical damaged control, then change only mechanism-specific lateral GaN:C and AlGaN regions for A/B and compare at matched injection current with emitter volume, all-channel trap loss, voltage/leakage and 2D unit normalization. Optional 60um size check and later 4um scaling only with separate recalibration if scope warrants.
- **Crucial:** Kou's **4um sidewall 'dead zone'** is an effective modeled zone (20um square leaves 12um good width), NOT Wu's 5nm literal trap-placement width or necessarily measured structural etch damage; direct sizes/area and Ntrap are not interchangeable. Model both clean/damaged exactly as far as documented, no blind 4um->20um SDE width change or porting old Bspan QW replacement without physics/active-volume review. Physically implementable GaN:C, regrown AlGaN also separate scope.
- **Claims:** numerical 20um A/B improvements could support *model-level feasibility for a Kou-like microLED*, not 4um JBD results, manufacturability, or general size independence. Initial JBD is motivation, not a tested geometry in such a report.
- **Status:** USER-PROPOSED, NOT team-approved scope/COMMON_BASELINE modification. Existing Lee V2.1/PolAct, JuSubin Bspan, code/results preserved; no simulation conducted. Expanded analysis `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`. Primary Kou DOI 10.1364/OE.27.00A643 and LSA review 10.1038/s41377-025-01751-y.


## 2026-11-03 — JuSubin asks if mixing Kou/Wu different-size device assumptions invalidates 4um Baseline (GPT SCIENTIFIC AUDIT / NO RUN)
- **Question:** whether Kou 2019 vertical 4QW source (lateral20/60/100um, APSYS, 4um damaged *dead zone*) combined with Wu 2023 localized 5nm sidewall acceptor trap model (prior project-reviewed 10um example with differing In0.08/8nm QB) is inherently incorrect for CMP 4um Kou-In0.15/22nm stack.
- **Assessment:** combining sources is allowed for a novel representative model, but treating the hybrid as a **validated 4um reference** without independently testing transferability is an important methodological omission. Different size, epi, trap semantics, contacts and simulator physical implementations interact; cannot assign root cause of QW4 or convergence solely to the combination.
- **Historical OBSERVED:** n6 trap ON at3.6V has significant gap-state recombination-equivalent share ~34.45% of terminal I (2D normalization conditional); QW4 radiation share ~99.97% even with NtSide0. Thus trap active but anomalous QW4 not explained simply by activating or changing 5nm sidewall trap.
- **Recommended gate, PROPOSED only:** Kou epi clean Nt0 physical validation -> matched-current 4um Nt0/Nt1e18 sidewall activation/affected width -> 4/10/20um size sweep with unchanged Wdmg/Nt/Et/sigma -> separate Wdmg and trap-density/sheet-density sensitivities and 2D square-area limit -> Project A/B comparisons using same control. User/team did NOT decide to replace protected 5nm or execute this plan.
- Details: `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`; publications Kou DOI 10.1364/OE.27.00A643 and Wu DOI 10.1016/j.micrna.2023.207542. No new source/deck/run.

## 2026-11-03 — 4µm damaged footprint quantified; existing V2.1 sidewall Trap activation is numerically observable (OBSERVED+DERIVED; NO NEW RUN)
- **Worker 주수빈** asked physical size/fraction and effective action range of damaged region on our 4µm device. Geometry read from V2.1 PP previously OBSERVED: `Wm=4µm`, `Wdmg=5nm`, Half width2µm; actual 2D sidewall strip fraction5nm/2µm=0.25%. Ideal hypothetical four-wall 4×4µm square: border area `16−3.99²=0.0799µm²` = **0.499375%**, not an actual 3D solved map.
- **Existing 10/21 3.6V PLT (NO NEW RUN)**: n2 Trap OFF I3.64728525e-8; n6 Trap ON I9.21970771e-9 raw units (~74.72% lower at SAME voltage). n6 total eGapStates trap recombination equivalent current3.17644732e-9, **34.4528% of n6 terminal current** under 2D integration conversion, and Rad+SRH+Aug+Trap current closure99.99904%; OFF trap contribution effectively zero. Supports actual *Trap recombination channel activation*, not a 34.45% spatial affected region, not same-current improvement, not a full measured SRH sidewall profile. Regionwise attribution and current normalization still need validation. QW4 OFF dominance remains independent blocker.
- **Literature distinction:** Wu2023 5nm from TCAD trap-placement width, not effective dead-zone. Wang2023 FLIM 80µm23% affected and 10µm nearly all under another process; Chen2024 4µm N2 sidewall-treated LOP improvement97.29% at J25Acm2; 2026 review summarizes physical damaged zone vs 0.5–1µm affected under certain etched conditions. These do NOT establish CMP's actual affected width.
- **Illustrative only** 4µm square affected fraction if effective inward reach is0.1µm→9.75%,0.2→19%,0.5→43.75%,1→75%; NONE measured or calculated from CMP field.
- **Proposed next:** inspect matched-current Trap OFF/ON lateral maps and derive explicit field-defined affected width, regionwise eGapStates/edge carrier access, plus size sensitivity 4/10/20µm; don't change protected Wdmg=5nm by assumption. Audit memo: `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`. No code/server action or team baseline approval.

## 2026-11-03 — JuSubin challenges why Wdmg=5nm when size-effect is central (SOURCE VERIFIED + DERIVED, NO RUN)
- **Question:** why did CMP select only 5nm damaged region when Kou's 20µm device had a much larger 4µm dead zone, and can increasing sidewall-to-active-area ratio still be tested?
- **ORIGIN CONFIRMED:** Wu et al. 2023 `Physical mechanisms on the size-effect in GaN-based Micro-LEDs` DOI 10.1016/j.micrna.2023.207542 explicitly uses acceptor-like traps **within 5nm of sidewall edges on both sides** in its 10µm TCAD example. This is a simulation defect placement width, not experimentally established universal 5nm damage penetration or a 5nm limit on electrical influence. Wu uses In0.08/8nm barriers vs CMP Kou-based In0.15/22nm.
- **Derived ideal square area fraction:** with 5nm fixed on four edges, 4µm device 0.499375%, 10µm 0.1999%, 20µm 0.099975%. Thus 20→4µm 5× relative geometrical share even though fraction at 4µm is only ~0.5%. Actual CMP planar half-domain maps to two-side strip ~0.25% at W4µm, not the square with four sidewalls; matching Kou's 4µm dead-zone fraction is an invalid direct comparison.
- **Physical interpretation:** trap-driven depletion, diffusion and lateral current redirection can extend far beyond 5nm. Liu et al. LSA 2025 review (DOI 10.1038/s41377-025-01751-y) summarizes structurally damaged nm-to-tens-of-nm vs hundreds-of-nm/micron electrically affected regions; Wang et al. Opt Lett 2023 DOI 10.1364/OL.501546 reports substantial broad affected emission area. Values vary with etch process and do not directly calibrate CMP.
- **Unverified:** CMP 5nm Nt=1e18 EtEv+.75 sigma1e-15 not calibrated for 4µm; no confirmed 4/10/20µm sensitivity sweep or square-vs-planar calibration. Nt*d equivalent sheet density 5e11cm^-2 per side, a geometric trap conversion not automatically SRV.
- **Recommendation PROPOSED:** keep 5nm as Wu-inspired control *until user/team approves change*; verify ON/OFF defect loss at matched current, 4/10/20µm size sweep with same model, then a documented 5/20/50nm width sensitivity with both fixed Nt and (separately) fixed Nt*d tests. Do not change baseline simply to raise damage fraction. Detail in `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`. No new TCAD code/run.

## 2026-11-03 — Kou 20um dead-zone vs CMP 4um 5nm damage: geometry and trap-model mismatch assessed (SOURCE VERIFIED / NO RUN)
- 주수빈 asks whether prior Baseline implementation failure may stem from too-large numerical/physical differences from Kou. Primary Kou 2019 §2/Fig1 confirms 20/60/100um modeled chips (minimum20um), 4um damaged zone EACH edge on 20um (12um usable width, 36% usable square area), APSYS versus CMP representative 4um mesa, 5nm damage, Sentaurus T-2022.03. Extrapolated CMP 4um square with four 5nm edges retains 99.500625% area; *idealized geometry comparison*, not equivalent recombination/TCAD performance.
- Kou uses separate electron trap Ec−0.24eV, σ3.4e−17, N1e13cm−3 and hole trap Ev+0.46eV parenthetical (text separately says 0.6eV), σ2.1e−15, N1.6e13. CMP one acceptor-like EtEv+0.75, σe/h1e−15, Nt1e18. Different model/region widths, not direct equivalent parameterization.
- **Finding:** Kou vertical 4QW epi parameters essentially match CMP; major departures are lateral size, damage representation, trap semantics, APSYS-vs-Sentaurus, uncalibrated polarization/band/contact. They could explain mismatch of quantitative device I-V/sidewall loss, but **cannot be declared confirmed root cause of numerical convergence or extreme QW4 localization**, which is seen in NtSide0 as well. Maintain Baseline B/FREEZE HOLD.
- Proposed test hierarchy: first compare identical Nt0 vertical-only/wide 2D 4QW behavior to 4um Nt0 at matched current to isolate 1D injection vs lateral effects, then sidewall ON. Do not replace 5nm with Kou 4um automatically. Full numerical audit recorded in `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`.
- Source: https://doi.org/10.1364/OE.27.00A643. NO new code, server run, baseline adoption or team decision.

## 2026-11-03 — Kou 2019 used APSYS µLED simulation; not a 4µm Sentaurus reference (SOURCE VERIFIED / NO RUN)
- Worker 주수빈 asked whether Kou et al. actually implemented the blue µLED with TCAD while preparing the new Baseline specification. Journal primary text Section 2 confirms **APSYS** numerical device simulation (not Sentaurus), six clean/damaged LEDs of 100×100 / 60×60 / 20×20 µm², and a **4µm damaged-sidewall region width** (NOT a 4µm Kou mesa).
- CMP's representative 4µm mesa + 5nm sidewall damaged region remains a mixed Kou vertical + Wu-inspired damage modeling choice; cannot claim exact Kou reproduction. APSYS says it can solve Schrödinger/Poisson/continuity, but model invocation/equivalent Sentaurus quantum treatment is not demonstrated.
- Kou provides 4×3nm In0.15GaN QWs, 22nm GaN QB, 26nm Al0.15GaN EBL, 120nm pGaN, 4µm nGaN, 20nm heavily doped pGaN contact, and paper-specific physical/defect parameters distinct from CMP's. Details and source URL in `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`.
- This is literature confirmation, not a user-approved change of COMMON_BASELINE or new TCAD code/run. Next: compare Kou APSYS controls with effective T-2022.03 models and decide explicitly which assumptions/geometry come from which references before any code.

## 2026-11-03 — JuSubin asks why repeated baseline rewrites did not fix physics; documented retrospective (ANALYSIS / NO RUN)
- **Worker:** 주수빈. Asked specifically to avoid repeating early V1.x/V2.1 mistakes in the proposed clean-sheet rebuild. GPT reviewed historical GitHub error log, baseline P3 and team timelines and 10/15 shelf-removal report.
- **OBSERVED historical failures:** Sept26 actual Node6 vs Node12 effective model/PAR differed beyond NtSide; missing Mg species parameters in InGaN were logged for failed Node12 but sole crash cause unresolved. 10/13 V2 SWB done while final printed voltage ~2.07V despite 3.6V goal. V2 shelf near mesa corner associated with 2.0–2.3V stalls; shelf removal **with cathode change** restored 3.6V in V2.1 but single cause not proven. 10/21 mesh min angle0.0167°/short edge0.0195nm. 11/02 PolAct clone wrong shelf provenance and Iterations20 vs12 observed.
- **Important model caveats:** 10/13 V2 Scharfetter-based doping-dependent SRH sub-ns interpretation was retracted when active SRH syntax lacked DopingDependence; actual runtime physics matters. Historical 5V same-bias OFF/ON radiative-share comparisons at different currents and 4V vs5V/1ns vs100ns comparisons cannot prove trap/lifetime effects. Raw2D current, 4um pixel-vs-mesa, 2D planar-vs-square, full/half equivalence, QW4 root cause and quantum-capture hypothesis unresolved.
- **PROPOSED design gate:** written into `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`: source-model assumptions/physical target -> SDE/material/contact/mesh gate -> effective PP/PAR species/physics gate -> bias endpoint + I/J/Full-Half gate -> matched-current recombination/channel gate -> immutable one-variable diff/revision; do not use numerical convergence or 'Good Bye' as physical validation.
- **No user/team final redesign approval, no new SDE/SDevice code or school-server run.** Existing protected Baseline B/FREEZE HOLD and Lee diagnostics unchanged.

## 2026-11-03 — JuSubin proposes clean-sheet Baseline redesign for original CMP research aim (USER-PROPOSED / NO CODE / NO RUN)
- **Worker:** 주수빈. **User assessment:** existing Baseline code/implementation may be inconsistent with the intended reference device and A/B sidewall research; would like to design entirely new code around the original agreed criteria. This is a proposed research pivot, NOT a team-approved replacement or claim of a proven code bug.
- **GPT independent review:** `CMP/COMMON_BASELINE.md` fixes representative 4um mesa (JBD 4um pixel pitch is not actual mesa), Kou 4QW epi, 5nm damage and nominal traps. Prior V2.1 reported QW4 >99.88% across PolAct variants, but exact source/mesh equivalence, 2D current scaling, physical cause remain unresolved. JuSubin's Project B `Bspan>0` previously replaces selected QW-edge semiconductor with AlGaN rather than an exterior coating; physical implementation must be clarified before rebuild.
- **PROPOSED workflow:** separate versioned clean-sheet candidate, first a documented reference-device geometry/material/contact specification; full 4um 2D primary validation, Half only after equivalence; SDE structure/mesh validation -> Nt0 clean LED injection/4QW diagnostics -> identical Nt1e18 damaged-sidewall counterpart -> matched-current baseline/mesh/units/QW validation -> independent A/B clones. Preserve original project and team-protected common constraints.
- **New design memorandum:** `CMP/members/JuSubin/BASELINE_REBUILD_PROPOSAL_20261103.md`; no executable Sentaurus decks authored, no school-server commands executed, no new simulator results. T-2022.03 official UG and effective pp/source must guide any later syntax. Proposed new project name tentative only.
- **Team status unchanged:** Baseline physical B/FREEZE HOLD; Lee's PolAct same-input diff/matched-current gate remains pending; Project B 10/22 subsequent job completion unverified. No finalized user/team adoption of redesign.

## 2026-10-24 — JuSubin 10/29 joint 14-minute paper review: Baek 2023 recommended as selected topic (USER-REQUESTED PLANNING; NO TCAD RUN)
- User provided the actual 2nd-week 19-slide CMP PPT and Kou et al. 2019 11-page PDF, and requests selection of the JuSubin individual review paper and a joint PPT framework with 7 minutes each. User states LeeTaekGyu will review Kou, and JuSubin separately reviews a complementary paper.
- **Updated recommendation/working selection (supersedes 2026-10-24 earlier Zhao shortlist, no claim of user's final approval):** Baek, Woo Jin et al., "Ultra-low-current driven InGaN blue micro light-emitting diodes for electrically efficient and self-heating relaxed microdisplay," Nature Communications 14, 1386 (2023), DOI 10.1038/s41467-023-36773-w, open access. Week-2 Project B slides 15–16 had already cited Baek 2023, Chang 2020, and Furtmayr 2011, while Lee's Kou review covers 4-QW baseline and size-dependent sidewall damage.
- Paper actual studied **vertical QB thickness** 3.5/7.5/10.5nm (6 QWs) and **AlInGaN EBL** redesign (17nm Al0.2In0.02Ga0.78N Mg2e18 -> 45nm Al0.12In0.02Ga0.86N Mg2e19cm^-3), in 10–80um pixels. Not a micro-LED with intentionally substituted AlGaN lateral Edge/barrier like CMP Project B. Must not present as direct validation of Bspan.
- Author OBSERVED/PUBLISHED results: 10x10um peak EQE 2.90%(QB3.5),3.01%(QB7.5),3.12%(QB10.5) without added passivation; JmaxEQE as size 80->10um shifts 55.5->250(QB3.5),10.2->30(QB10.5) A/cm2. After Balanced EBL JmaxEQE 3.1->4.0 A/cm2. At fixed 0.1A/cm2, 10x10um EQE 2.04% (as-deposited) vs 3.00% (passivated), different from peak EQE. Source nature.com/articles/s41467-023-36773-w, Figs1–5 / Methods.
- Paper SILVACO Atlas modeling assumes PEF 50% theoretical, SRV1e5cm/s, tauSRH100ns, B1e-10 cm3/s, Auger1e-31cm6/s; not numerically interchangeable with CMP Sentaurus baseline.
- Presentation plan (14 min): Lee 6 slides/~7min (Kou problem/model, sidewall EQE and current/carrier findings), JuSubin 6 slides/~7min (Baek rationale Fig1, QB Fig2, EBL + TCAD Fig3, experimental Fig4/5, Project B relevance and distinctions). Focus paper's figures vs excessive codes/TCAD launch status; shared closing differentiates disease (Kou), vertical epitaxy workaround (Baek), lateral Edge idea (CMP).
- Explicit literature nuance: Chang L. et al. Nanoscale Res Lett 15:160 (2020), DOI 10.1186/s11671-020-03372-3 favors *thinner* QB in different conditions, whereas Baek 2023 favors *thicker* QB; not universal design law. Furtmayr et al. PRB 84 205303 (2011) concerns GaN/AlGaN nanowire nanodisc shell, not CMP mesa; Zhao 2026 concerns InGaN/AlGaN digital alloy epitaxial barriers, not Project B Edge material replacement.
- Baseline 4um geometry/QW4 ~99.9688% abnormal dominance and physical FREEZE HOLD unchanged; no new user server result, code edit, or simulation performed. Upcoming 10/26 progress presentation may report latest Bspan nodes only after runtime status verification.

## 2026-10-24 — 주수빈 10/29 개별 논문리뷰 후보 독립 조사 (SOURCE-VERIFIED LITERATURE; PROPOSED ONLY)
- 일정 (사용자 보고): 2026-10-26(월) CMP 공동 프로젝트 진행상황 발표, 2026-10-29(목) 개인 논문리뷰 발표. 이택규는 Kou 원논문을 리뷰할 예정. 사용자 주수빈 논문 선정은 아직 미확정.
- 1순위 제안 (NOT SELECTED): Zhao et al., "Weak polarization electric field III-N LEDs on polar plane with enhanced efficiency and strong lateral carrier confinement," Light: Science & Applications 15, 300 (2026), DOI 10.1038/s41377-026-02359-6, OA. InGaN/AlGaN 디지털합금 초격자 양자장벽 연구. peak EQE 15%, PEF~0.5MV/cm, 10–60um microLED, simulated lateral e/h density, PL and size-dependent EQE; sidewall sensitivity ~50% 감소는 저자 분석. 저널 원문 확인.
- 2순위 대안: Gong et al., "Reversed Size Dependence of External Quantum Efficiency in GaN Micro-LEDs with an AlGaN-Interlayered QW-QD Composite Active Region," Photonics 13, 806 (2026), DOI 10.3390/photonics13090806. 5–50um microLED, 1nm Al0.1Ga0.9N interlayer; QD localization+LEE 복합효과라 Project B 직접 재현은 아님.
- 3순위 대안: Park et al., "Role of Sidewall Conditions in the External Quantum Efficiency of InGaN-Based Micro-LEDs," phys. status solidi RRL 19, 2500042 (2025), DOI 10.1002/pssr.202500042. 10–40um ALD sidewall passivation 실험; Project B AlGaN 장벽과 물성/구조 다름.
- 엄격한 적용 범위: 해당 논문들 모두 현재 CMP 4um half-device에서 시행하는 *측벽 Edge AlGaN material replacement*와 일치하지 않는다. EQE를 CMP TCAD QW-only IQE나 current-normalized photon yield와 동일시하거나 논문 효율을 CMP 예측 수치로 사용하지 않는다. 10/22 Project B Bspan0/1/3 완료·성능결과 확인 여부 및 Baseline QW4 물리검증 blocker는 변경 없음.
- 추천 발표 구성 (PROPOSED): 문제(측벽 SRH) → 논문 장벽/캐리어 구속 메커니즘 → Fig.3/6/7/8 주요 데이터 → 4um Project B와 비교/한계 → 추가할 TCAD 분석 (matched-J, lateral Ec/Ev, carrier distribution, Rad/SRH/Auger, Edge trap).
- 이 기록은 AI 조사와 **추천**만 포함하며 사용자 논문 확정 또는 새 실험/시뮬레이션 진행을 의미하지 않는다.

## 2026-10-22 — JuSubin clarifies SWB staged serial execution for Project B (USER-REPORTED QUEUE INTENT)
- User clarifies copied SWB `/user/semi/semi437/CMP_B0/CMP_BASELINE_2.0.0_V2` is scheduled to run Bspan=0→1→3 sequentially. Earlier absence of `pp31_dvs.cmd` does NOT justify separately launching n31; likely next stage not yet reached. Do not claim live scheduler status or assured run from image alone; current actual n17 mesh and n24 iteration were observed.
- CORRECTED action: do not manually submit duplicate n31 or restart any SDevice. While SWB runs, **read-only inspect n17_msh.tdr in SVisual** for Bspan1 `Edge_QW1..4` AlGaN, `Clean_QW` & `Dmg_QW` InGaN, material/mesh and intact damage region. Prepare controlled comparison for Trap ON branches n6(Bspan0), n30(Bspan1), n44(Bspan3), and Trap OFF branches n2/n24/n38, with current-matched voltage, QW Rad/SRH/Auger, Dmg trap recomb, carrier/band profiles and changed QW active volume. No software/deck changes or new run by assistant.
- Pending user SVisual screenshot on existing `n17_msh.tdr`; no new TCAD results as of this note. Common Baseline physical freeze still provisional.

## 2026-10-22 — Project B Bspan3 n31 preprocess not found; execution status requires SWB check (OBSERVED)
- User ran Bash read-only command against cloned `/user/semi/semi437/CMP_B0/CMP_BASELINE_2.0.0_V2`: `grep: pp31_dvs.cmd: No such file or directory`. Because it was chained by `&&`, `ls -lh n31_msh.tdr` did not execute. Thus **pp31 absent is observed**, while n31 mesh presence/absence and job/scheduler state are not proved by this call.
- Earlier user SWB screenshot showed `Bspan=3 [n31]:3` as a white/uncompleted-looking cell, in contrast to yellow completed Bspan1 n17. This suggests n31 has not completed, but screenshot may be stale; do not claim it has failed.
- NEXT inspect current SWB Bspan3 n31 scheduler state and start SDE n31 only if not queued/running, verify Bspan=3 in preprocessed pp31 and new n31 mesh before enabling Bspan3 device node. Don't modify source, interrupt n24, or repeat a completed run.

## 2026-10-22 — Project B 실행 로그 1차 검증 (USER OBSERVED; NOT COMPLETE)
- 사용자 Bash wrapper 실행 성공. 경로 `/user/semi/semi437/CMP_B0/CMP_BASELINE_2.0.0_V2`에서 `pp17_dvs.cmd:45 (define Bspan 1)` 확인. `n17_msh.tdr` 존재(2.0M, Oct22 15:29). Bspan1 SDE mesh file OBSERVED (new mesh provenance/timestamp relative to user start plausible; region-level material inspection remains).
- n24_des.log last lines show Newton iterations: Rhs 2.63e10 → 5.25e8 → 2.00e4, iterations 0/1/2, no finish status. This means SDevice iteration recorded, not convergence completion or definite live PID. n30, n38, n44 log files absent on check. n31 pp31_dvs.cmd matching Bspan and n31_msh.tdr not found by command; SDE Bspan3 may be queued, not submitted or failed; do not label fail without SWB scheduler.
- Shell prior `for: Command not found` resolved as read-only diagnostic succeeds under `bash -lc '...'`. No TCAD edits or extra RUN performed by ChatGPT.
- NEXT immediate: inspect SWB n31 SDE scheduler status. If already pending/queued/running, do not resubmit; if ready/not submitted, run SDE n31 *only* and verify new pp31 Bspan=3 + mesh, then analyze Bspan3. Preserve n24 and other jobs.

## 2026-10-22 — Project B read-only diagnostic command rejected by user shell (OBSERVED, NO TCAD EFFECT)
- In screenshot-confirmed SWB project `/user/semi/semi437/CMP_B0/CMP_BASELINE_2.0.0_V2`, user pasted assistant Bash `for ... do ... done` command into login shell and observed `for: Command not found.`. This is a **shell command-compatibility error**, likely login csh/tcsh, not SDE/SDevice failure. No file modifications, simulation cancellation or changes reported.
- Fix (PROPOSED, not yet user tested): wrap existing read-only inspection in `bash -lc '...'` using ASCII-only echo labels; inspect pp17/pp31 Bspan + n17/n31 mesh + n24/n30/n38/n44 device logs. Do not rerun SWB/alter code because of this shell error.

## 2026-10-22 — JuSubin Project B Bspan 0/1/3 node matrix screenshot and RUN reported (USER OBSERVED/REPORTED; COMPLETION UNVERIFIED)
- User SWB screenshot header: `/user/semi/semi437/CMP_B0/CMP_BASELINE_2.0.0_V2` (separate visible path from older root `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`; protect parent). User states already cloned, split and running Bspan=1/3; no proof of individual terminal solve success, so mark SWB setup OBSERVED and simulation launch USER-REPORTED.
- Screenshot shows one copied SWB project with 3 Bspan groups: `Bspan=0` SDE n1, SDevice Trap OFF n2 (NtSide=0), ON n6 (NtSide=1e18); `Bspan=1` SDE n17, OFF n24, ON n30; `Bspan=3` SDE n31, OFF n38, ON n44. `Wedge=0.1`, `PolAct=0.5`, `NCedge=0`, `V1=2.0`, `Vmax=3.6`, `NPlot=8` appear shared. Color cells in screenshot do NOT prove every run done; n31 SDE appears not yellow done; must verify actual preprocessed `pp17_dvs.cmd`, `pp31_dvs.cmd`, timestamp of `n17_msh.tdr`, `n31_msh.tdr`, and final SDevice logs n24/n30/n38/n44.
- **No source modification indicated/needed at first pass:** observed SDE in-Bspan? mapping prewires 1 & 3 lateral AlGaN replacements; SDevice AlGaN/GaN and AlGaN/InGaN Thermionic blocks and polarization already present. Don't edit protected original or copied *generated* pp*. If error occurs use actual log and minimal justified change in copied user project only. Do not launch duplicate RUN before inspecting jobs.
- NEXT: in screenshot-specific copied project folder read-only inventory + grep SDE parameter substitutions and n24/30/38/44 logs. Ensure Bspan1 and 3 use new meshes, verify region material/xMoleFraction/5nm Dmg and contacts. Once completed, current and matched-current QW/sidewall recombination analysis. Unresolved baseline physical freeze/2D current normalization and QW4 issue remain; result not publication-confirmed.

## 2026-10-22 — 주수빈 Project B 즉시 구현 계획 승인 (USER DECISION, RUN PENDING)
- User requests today completing Project B implementation while operationally assuming Baseline frozen; this is NOT evidence of scientific freeze. Parent CMP_BASELINE_2.0.0_V2 remains protected.
- NEW separate SWB ProjectB: CMP_PROJECTB_1.0.0_ALBARRIER, Save As parent, change Bspan0→3 in SWB only, Wedge0.1um, xAlB0.15, Wdmg0.005um, existing traps/physics unchanged. First SDE mesh, verify newly generated mesh and AlGaN QW/Barrier Edge, then Trap ON 3.6V pilot. School server clone/run NOT YET OBSERVED.
- Execution plan: CMP/members/JuSubin/PROJECT_B_IMPLEMENTATION_RUNBOOK_20261022.md. Preserve source and provenance, do not assert baseline calibration or actual IQE.

## 2026-10-22 — JuSubin GaN/InGaN vs AlGaN band-parameter audit (OBSERVED + DERIVED; NO PROJECT B RUN)

### Direct server evidence (read-only)
Source: `CMP_BASELINE_2.0.0_V2/pp2_des.par`, user terminal `sed -n '1,85p' pp2_des.par` on 2026-10-22. `LatticeParameters: X=(0,0,-1), Y=(1,0,0)`; `Material=GaN`: Eg0=3.4376 eV, Chi0=4.1000 eV, alpha=9.09e-4, beta=830, Tpar=300 K; `Material=InGaN`: Eg0=2.8569 eV, Chi0=4.5065 eV, alpha=8.09e-4, beta=799, Tpar=300 K. Both displayed ConstantMobility(300,10), Scharfetter taumax=1e-7, Radiative C=2e-11, Auger A=5e-31. Previous actual `pp2_des.par` output: `AlGaN` Eg0=3.7564 eV, Chi0=3.8768 eV, Tpar=300 K; actual preprocessed SDE `xIn=xEBL=xAlB=0.15`, `Wedge=0.1um`, `Bspan=0`, `Wdmg=0.005um`.

### Conditional analytic estimates (not Sentaurus solved band structure)
Using electron-affinity/Anderson vacuum-reference rule at 300K with `Ec=-Chi`, `Ev=-Chi-Eg` and neglecting electrostatic potential, strain-induced changes, interface charges, polarization and local carrier redistribution:
- GaN: Ec=-4.1000 eV, Ev=-7.5376 eV
- InGaN: Ec=-4.5065 eV, Ev=-7.3634 eV
- AlGaN: Ec=-3.8768 eV, Ev=-7.6332 eV
- Going from GaN into AlGaN: nominal electron upward Ec=+0.2232 eV, hole downward Ev=0.0956 eV.
- Going from InGaN into AlGaN: nominal electron upward Ec=+0.6297 eV, hole downward Ev=0.2698 eV.
Neither is the actual 2D lateral barrier under bias. Do not claim physically validated sidewall confinement from numbers alone. Recombination and strain/polarization are model-dependent.

### Practical design decision
- The `Bspan=3, xAlB=0.15, Wedge=0.1um` case is an INITIAL PROPOSED geometry/material-substitution screening candidate, not a proven optimal design and **not yet launched**; `Bspan=0` with same sidewall trap and frozen source/mesh is the proper control. `Bspan=1` is a candidate for localization-range sensitivity, after basic smoke.
- `Bspan>0` changes material in the lateral 100nm QW Edge, i.e. 5% of 2um half QW lateral width; compare corrected active region integral and absolute radiative emission at matched current as well as defect trap SRH, band-edge lateral cutlines and current crowding.
- Previously audited `AlGaN` params have fixed scalar Eg0/Chi0 without explicit composition-dependent interpolation visible in displayed section. Don't vary `xAlB` as if bandgap/affinity automatically recalibrate; inspect runtime mole-fraction interpolation in T-2022.03 effective material parameters before alloy sweeps.
- No TCAD code, SDevice input, new SWB project or simulation modified. Must check final Baseline frozen status/source provenance before independent Project B clone.
- Today's prep work is now sufficiently defined: await verifiable freeze; then clone preserved baseline into independently named Project B, run separate preprocess/SDE mesh smoke for Bspan=3, inspect AlGaN Edge region xMoleFraction and new lateral Ec/Ev and polarization before running 3.6V ON trap comparison.

## 2026-10-22 — JuSubin Project B SDevice material-interface model declarations observed (SERVER OUTPUT, NO B RUN)
- User provided read-only `grep -nEi 'AlGaN|Piezoelectric_Polarization|Thermionic|MoleFraction|BandOffset|Bandgap' pp2_des.cmd pp2_des.par | head -n 90` from actual server `CMP_BASELINE_2.0.0_V2`.
- OBSERVED: `pp2_des.cmd` line21 `Piezoelectric_Polarization( strain activation=0.5 )`; lines24-26 `Physics (MaterialInterface="InGaN/GaN") { Thermionic }`, `AlGaN/GaN`, `AlGaN/InGaN`. Lines59-67 requested `ConductionBandEnergy`, `ValenceBandEnergy`, `BandGap`, `ElectronAffinity`, `xMoleFraction` plot outputs. `pp2_des.par` line112 `Material = "AlGaN" { Bandgap {...}` start, lines166/169/172 `ThermionicEmission { Formula = 1 }` under relevant interface sections (verify exact headers via expanded excerpt).
- Inference limited: these are present in baseline preprocessed n2 deck with **Bspan=0**; they DO NOT confirm correctness or runtime application of newly introduced lateral AlGaN interfaces at Bspan>0, orientation-dependent polarization charge, model parameter suitability, or Project B performance.
- NEXT READ-ONLY: `sed -n '1,34p' pp2_des.cmd` and `sed -n '108,176p' pp2_des.par` to inspect effective AlGaN Bandgap, electron affinity, alloy interpolation and all Thermionic context. No code changes and no Project B simulation until verified Common Baseline freeze.

## 2026-10-22 — JuSubin Project B active V2.1 Bspan/Edge code hooks verified (OBSERVED USER TERMINAL)
- User ran READ-ONLY `grep -nEi 'Bspan|Wedge|Wdmg|AlGaN|Aluminum|Edge_|Dmg_' sde_dvs.cmd pp1_dvs.cmd | head -n 140` in actual school server directory `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`; source and preprocessed SDE printouts matched semantic definitions.
- OBSERVED `sde_dvs.cmd`: Wdmg=0.005um (line38); Wedge=`@Wedge@` line39; Bspan=`@Bspan@` line45; `Xd=Xs-Wdmg`, `Xe=Xd-Wedge` lines54–55. Actual `pp1_dvs.cmd` has Wedge=0.1um and Bspan=0 (lines39,45).
- OBSERVED documented mapping: `Bspan=0` baseline no new lateral AlGaN edge; Bspan1 -> Edge of QW1–4, Bspan2 -> Edge of QW1–4 plus B1–B3, Bspan3 -> Edge of QW1–4 plus B0–B4; explicit `in-Bspan?` function and conditional `AlGaN` material selection lines80–89. `MF_AlB` material profile for selected AlGaN edge referenced at line112; value/composition and actual geometric/electrical interpretation are UNVERIFIED. `Edge_`/`Dmg_` region dynamic names lines128–129; Edge keeps host doping by source comment at line133.
- INTERPRETATION: This is a PREWIRED lateral **material substitution** in QW and optionally GaN barrier EDGE regions, **not proof of a deposited outside coating**, unchanged active/emissive area, polarization consistency or viable physical performance. Baseline unchanged, no Bspan>0 preprocessing or RUN tested. Potential material-replacement/polarization/offset impacts are open review items.
- NEXT FIRST: read-only `sed -n '65,145p' pp1_dvs.cmd` to obtain `base-mat`, `in-Bspan?`, actual "MF_AlB" definition/use and `make-layer` region geometry; if Al mole fraction outside displayed block then grep `MF_AlB|MoleFraction|Aluminum|xAl` in pp1_dvs.cmd. Verify sidewall and vertical extents before choosing a Project B test condition. Do not edit V2.1 or start Project B runs pending frozen baseline.

## 2026-10-22 — 주수빈 Project B 단독 담당 방향 명확화 (USER DECISION; PREPARATION STARTED)
- 사용자 2026-10-22 명시: 오늘 Baseline 최종 검증/확정이 이루어질 경우, **이택규는 Project A(GaN:C), 주수빈은 Project B(AlGaN)로 분리 진행**한다. 이는 사용자 제공 분업 계획이며 이택규와의 독립적 직접 합의는 현재 채팅에서 검증되지 않음. Baseline freeze 사실도 아직 미확인.
- 주수빈의 오늘 당장 작업은 Project B-only 기하/재료/물리 모델 사전 확인과 한 가지 pilot 및 후속 조성·폭 DOE 설계. 독립 계획 문서 `members/JuSubin/PROJECT_B_PLAN_20261022.md` 작성(PROPOSED). 이전 A/B 양쪽 검토 제안보다 최신 사용자 지정 분담을 우선한다.
- FIRST SERVER ACTION: `CMP_BASELINE_2.0.0_V2` SDE 코드에서 Bspan/Wedge/Wdmg, AlGaN/Edge/Dmg region 생성 및 활성 preprocessing READ-ONLY 검사. 소자 코드/런 변경 없음. Baseline 확정 후 별도 versioned `CMP_PROJECTB_1.0.0_ALBARRIER` 후보 구현/short smoke; 확정 전 장시간 run 금지.

## 2026-10-22 — 주수빈 Project A/B 설계 준비 착수 (USER-APPROVED DIRECTION; PROPOSED DESIGN)
- 주수빈이 이택규와 Baseline V2.1 최종 검증을 중복하지 않고 Project A(GaN:C 고저항 측벽 Edge), Project B(측벽 AlGaN lateral heterobarrier) 구현 준비에 집중하기로 선택. 이택규와의 상호 역할 승인/전담 확정은 아직 아님.
- GitHub Phase #3/#4/#5, AI_SHARED_MEMORY_PROTOCOL 및 선행문헌을 기반으로 독립 설계 준비 문서 `members/JuSubin/PROJECT_AB_PREPARATION_20261022.md` 작성. 실제 Sentaurus 소스/런/새 프로젝트 생성 없음.
- Project A는 nominal C dose를 고정 저항 또는 이온화 acceptor/trap 밀도로 단정하지 않으며, GaN 영역과 QW를 구분한 C 모델 검증이 선행되어야 함. Project B는 실제 Bspan geometry, Al mole fraction, polarization/band offsets 검증이 선행되어야 함. 수치 sweep은 PROPOSED screening only.
- 다음 최우선: 학교 서버 `CMP_BASELINE_2.0.0_V2`에서 `sde_dvs.cmd`/`pp1_dvs.cmd`의 Wedge/Bspan/Wdmg 및 Edge/Dmg 재료·영역 생성 부분을 READ-ONLY 출력으로 확인. Common Baseline/기존 n2/n6 결과 보존; 이택규의 2D current normalisation 및 Full/Half 최종 검증 후 본격 A/B pilot.

## 2026-10-15 — n6 적분 시도에서 n2 데이터셋/8영역 선택 오류 확인 (OBSERVED)
- 사용자가 새로 전달한 SVisual 출력은 `Dataset: n2_des`, `Field: RadiativeRecombination`. Clean_QW1..4 및 Dmg_QW1..4만 포함한 8개 2D 영역의 Total Integral 1.447895e11 s^-1 um^-1, Total Domain 0.02279999 um². n6의 측정 결과가 아님.
- 앞서 n2 12개 QW 적분(1.524099e11, 0.02399999um²)과의 차는 약 7.6204e9 s^-1 um^-1로 이전 Edge_QW1..4 적분합과 일치함. 물리 변화가 아닌 ROI/데이터셋 선택 차이.
- 다음은 SVisual에서 n6_des 데이터셋이 선택된 상태를 확인하고, Clean/Edge/Dmg × QW1..4 전체 12개에 Radiative 적분 수행. 코드는 변경하지 않음.

## 2026-10-15 — V2.1 n2 12 QW 3채널 재결합 적분 완료 (OBSERVED/DERIVED)
- **OBSERVED SOURCE:** 주수빈 2026-10-15 Sentaurus Visual n2_des / AugerRecombination / Regions of Dimension 2 결과 원문. QW1~4 각각 Clean/Edge/Dmg 총 12 ROI, Total Integral **6.265625e10 s^-1 um^-1**, Total Domain **2.399999e-02 um²**. 개별 영역 표시 수치 합 6.26562547006376e10 (반올림 범위 내).
- **Auger QW별 합(표시 정밀도):** QW1 7.10119054e4, QW2 1.102859532e5, QW3 3.918102779e6, QW4 6.26521553e10 s^-1 um^-1. QW4 Auger 집중 약 99.99346%.
- **3채널 같은 ROI 합계(OBSERVED + ARITHMETIC):** Radiative 1.524099e11, srhRecombination 1.253894e10, Auger 6.265625e10, sum=2.2760509e11 s^-1 um^-1. Radiative share 66.96243%, SRH 5.50908%, Auger 27.52849%. QW별 radiative/(Rad+SRH+Auger) from rounded region sums: QW1 7.70%, QW2 8.90%, QW3 25.78%, QW4 67.01%. All three fields Total Domain identical 0.02399999 um². **Derived modeled 3-channel QW radiative fraction, NOT independently validated physical IQE/EQE.** Earlier V2.1 n2 Radiative local max 3.07538e25 cm^-3 s^-1 is distinct from these integrals.
- **LIMITS/BLOCKERS:** Verify spatial n2 TDR corresponds to 3.6V endpoint, active AreaFactor/2D current units, QW trap recombination/other sources/leakage/current continuity, physical material Auger parameters. Very uneven QW4 dominance and 27.53% Auger warrant eDensity/hDensity and band/physics audit, not proof of wrong model. Fixed-voltage n2 vs n6 at different currents cannot isolate trap effect as matched-current IQE.
- **NEXT:** SVisual n6_des.tdr source, region/field consistency; all 12 QW ROI Rad, SRH, Auger and Domain; calculate identical metrics. Maintain original SDE/SDevice/sim output unchanged.

## 2026-10-15 — 주수빈 V2.1 n2 12 QW SRH 적분 확보 (OBSERVED)
- **OBSERVED, 사용자 SVisual 원문(2026-10-15):** `Dataset=n2_des`, `Field=srhRecombination`, Clean/Dmg/Edge QW1~4의 정확히 12개 2D region; Total Integral=`1.253894e+10 s^-1 um^-1`, Total Domain=`2.399999e-02 um²`. 개별 표시값 합계 `1.253894043236e10`으로 총합과 출력 반올림 내 일치.
- QW1/QW2/QW3/QW4 (각 Clean+Dmg+Edge): `2.251474379e7`, `2.770548437e7`, `1.198340442e8`, `1.236888616e10 s^-1 um^-1`; SRH의 약 `98.6438%`는 QW4. 같은 12개 QW `RadiativeRecombination` 적분은 이전에 `1.524099e11`로 관찰, 동일 Domain. 두 채널만의 Radiative/(Radiative+SRH)≈92.398%; **Auger 미적분이므로 최종 3채널 비율/IQE 확정 불가**.
- 물리 경계: 현재 n2 파일 시점의 3.6V TDR 저장 bias, 타 모델 calibration, AreaFactor, current leakage, `n6`의 동일 ROI 적분은 여전히 검증 전. QW4에 Rad와 SRH가 모두 집중하지만 원인 미확정. 신규 실행·소스 변경 없음.
- **다음:** `n2_des`에서 동일 12개 ROI `AugerRecombination` Field Integration 실행하고 Total Integral/Domain 원문 전달 → 3채널 비율 산출. 그다음 n6 같은 12 ROI 반복.

## 2026-10-15 — 주수빈 V2.1 n2 MQW Radiative 적분 (OBSERVED)
- 실제 SVisual Field Integration 출력: n2_des RadiativeRecombination, 4QW×Clean/Edge/Dmg 총 12개 영역, Total Integral 1.524099e11 s^-1 um^-1, Total Domain 0.02399999 um².
- QW별 합계(QW1~4): 1.884852e6, 2.718766e6, 4.298663e7, 1.52362276e11. QW4가 전체의 약 99.9688%를 차지. IQE가 아닌 방사 재결합 공간 비율, 물리 원인 미확정.
- Dmg_QW1..4 실제 region 명칭 적분 출력에서 개별 확인. 다음: 정확히 동일한 12 QW ROI의 SRH/Auger 적분 및 n6 동일 작업. 최종 TDR bias/AreaFactor/물리 보정은 미확인. 소스/시뮬레이션 수정 없음.

## 2026-10-15 — n2 SVisual RadiativeRecombination 시각화 (OBSERVED SCREENSHOT; no integral)
- 주수빈 제공 `CMP_BASELINE_2.0.0_V2` Sentaurus Visual T-2022.03 `n2_des` 캡처에서 Scalars `RadiativeRecombination` 체크, 우측 범례 최대 `3.07538e25 cm^-3 s^-1` 표시 확인. **국소 필드 최대값이지 QW 지역 통합 값 아님**; 방사 재결합 총량, IQE 미측정.
- Regions 현재 스크롤 위치에 `Edge_QW3`, `Edge_QW4` 표시 확인, 다른 QW Region은 해당 화면에서 확인되지 않음. 스크린샷 하단 Elements=129404, Points=62529.
- 다음: SVisual Field Integration 대화창의 Region/Material 탭에서 실제 Clean/Edge/Dmg × QW1..4 총 12개 선택(실제 전체 존재 확인 후), `RadiativeRecombination` 적분 및 Total Integral/Domain 원문 확보. 이후 동일 영역으로 SRH/Auger. GUI Regions 화면의 표시 체크만으로 통합 ROI가 제한되는 것은 아님.
- 서버 소스·시뮬레이션 수정 없음.

## 2026-10-15 — V2.1 MQW 영역 생성 규칙 서버 SDE 코드에서 확인 (OBSERVED CODE EXCERPT)
- 주수빈이 실제 서버 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2/sde_dvs.cmd`에 대해 `grep -nEi 'qw|quantum|edge|dmg|region' ...` 출력 제공. QW1~4 각각 0.003 µm, `Wdmg=0.005` µm (5nm), `Wedge=@Wedge@`, `Xd=Xs-Wdmg`, `Xe=Xd-Wedge` 코드 확인.
- 영역명은 SDE 스크립트의 `(string-append "Edge_" name)`, `(string-append "Dmg_" name)` 등 런타임 구성으로 만들어져 정확 이름 검색이 빈 결과였음. 기존 SVisual Clean_QW1~4 화면과 합치면 의도된 MQW ROI는 **QW1~4 × Clean/Edge/Dmg = 12개의 2D 물리 영역**으로 추론되며 최종 실제 메쉬의 12 영역 존재는 GUI 확인 예정. 사용자의 `Dmg_QW14` 표기는 정확 라벨인지 약칭인지 미확정.
- SDE 17-20행: Edge는 Project A/B hook이고 baseline에서는 Clean과 같은 물질/도핑이라고 주석; Dmg은 측벽 trap 대상이라고 주석. 이것이 n2/n6 활성 SDevice Trap 범위 및 Bspan 실값을 직접 검증한 것은 아님.
- 다음 SVisual: 12개 실제 region을 확인한 뒤 동일 ROI에 Radiative/SRH/Auger 적분. 인터페이스 항목, EBL/barrier는 QW 적분에서 제외. 소스/기존 계산 수정 없음.

## 2026-10-15 — V2.1 SDE exact region-name grep returned no matches (OBSERVED TERMINAL)
- 주수빈은 `CMP_BASELINE_2.0.0_V2`에서 `grep -n -E -C 3 'Dmg_QW|Edge_QW|Clean_QW' sde_dvs.cmd | head -n 130` 실행 후 출력이 없는 것을 확인. 이는 해당 파일의 정확한 문자열 검색 불일치만 뜻하며, SVisual에 QW 영역이 없거나 메쉬 오류임을 의미하지 않음.
- 가능성(미확인): region label을 동적으로 생성했거나 다른 코드/전처리 파일에서 정의. 다음 읽기 전용 검사: `grep -nEi 'qw|quantum|edge|dmg|region' sde_dvs.cmd | head -n 100`.
- 실제 MQW Clean/Edge/Dmg ROI 관계가 확인되기 전 재결합 적분 보류. 소스·서버 run 변경 없음.

## 2026-10-15 — V2.1 SVisual MQW region naming correction (USER-REPORTED UI; mapping UNRESOLVED)
- 주수빈은 n2 SVisual `Regions`에 기존 5V_TEST에서 기대한 `DmgL_QW1~4`가 없고 대신 `Dmg_QW14`(사용자 표기 그대로, 단일 이름/연속 범위 여부 미확정)와 `Edge_QW1~4`가 있다고 보고. 화면에서 직접 확인된 `Clean_QW1~4`와 함께 V2.1 QW ROI 구성의 정확한 포함/중복 관계는 미확인.
- AI가 이전 버전의 region 이름을 V2.1에 그대로 적용한 안내를 정정함. ROI 정합 없이 적분/수치 합계 산출 금지.
- 다음: 서버 현재 `CMP_BASELINE_2.0.0_V2` 경로의 실제 SDE 소스 `sde_dvs.cmd`/`pp1_dvs.cmd`에서 `Dmg_QW|Edge_QW|Clean_QW` 문자열 정의를 read-only 검사하도록 요청. 실제 명칭과 위치 확인 후 Rad/SRH/Auger 동일 ROI 적분 진행. 코드/시뮬레이션 변경 없음.

## 2026-10-15 — 주수빈 V2.1 n2 SVisual 공간 데이터 오픈 및 QW 영역 최초 확인 (OBSERVED SCREENSHOT)
- 사용자 업로드 Sentaurus Visual T-2022.03 스크린샷: 상단 창 제목에 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`, 플롯 타이틀 `n2_des`가 표시. `Regions` 패널에서 `Clean_QW1`~`Clean_QW4`와 `Clean_EBL` 영역이 보임. `Scalars` 패널에서 `AugerRecombination` 필드 존재 확인, 현재 체크된 표시는 `DopingConcentration`임.
- SVisual 하단 표시 Elements=129404, Points=62529. 이를 바탕으로 표시 데이터셋의 메쉬 카운트 관찰 (이 수치가 향후 다른 조건도 같다는 뜻 아님).
- **한계:** `DmgL_QW1~4` 존재 여부와 Radiative/SRH 필드명은 패널 스크롤 위치 때문에 미확인, TDR 최종 바이어스/재결합 적분량 역시 미확인. 계산 완료와 파일 존재는 앞선 터미널 출력으로 별도 확인했으나 현 이미지 자체에 3.6V 표시 없음.
- 다음: Region 목록을 위로 스크롤해 DmgL QW 확인, Scalars에서 Radiative와 SRH 필드 확인, 동일한 QW ROI 선정 및 SVisual Field Integration; 원본 코드 및 실행 변경 없음.

## 2026-10-15 — 주수빈 V2.1 n2/n6 3.6V 목표 도달 및 결과 파일 직접 확인 (OBSERVED USER TERMINAL)
- 근거: 주수빈이 2026-10-15 실제 학교 서버에서 복사한 읽기 전용 출력. 경로 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`; `cat n2_des.sta n6_des.sta`에서 두 노드 모두 `done`; `grep '^ *anode' n2_des.log | tail -3` 마지막 (3.576V,2.424e-08), (3.592V,3.180e-08), (3.600V,3.647e-08); n6 동일 전압에서 7.077e-09 / 8.433e-09 / 9.220e-09 (SDevice raw terminal total-current log values).
- 파일 존재: n2_des.plt 293K, n2_des.tdr 21M (Oct14 15:44); n6_des.plt 295K, n6_des.tdr 23M (Oct14 17:43). 출력 시점 및 최종 전압 기록은 사용자가 직접 제시한 실제 파일/로그 텍스트로 **OBSERVED**. 이는 종전의 Claude 단독 RUN 전사 근거를 강화함.
- 동일 3.6V n6/n2 raw terminal current ratio = 9.220e-09/3.647e-08≈0.2528. 진정한 QW 주입/효율/트랩 효과 원인, 2D A/µm/AreaFactor 정확한 설정, TDR가 목표 3.6V 최종 저장본인지, 활성 코드 Wshelf·PolAct·접촉 설정은 아직 **UNRESOLVED**.
- 원본 소스/실행 변경 없음. 다음은 TDR 저장 시점·활성 덱 정의와 SVisual ROI·물리 필드 확인 후 QW별 Radiative/SRH/Auger 적분; 단일 전압에서 IQE causality 단정 금지.

## 2026-10-15 — 주수빈 검증 대상 V2_Copy → V2.1 물리 검증으로 변경 (PROPOSED; NO NEW RUN RESULT)
- 작업자 주수빈은 직전 `CMP_BASELINE_2.0.0_V2_Copy` 수렴 진단 선택에서 변경해, 이택규/Claude가 3.6V 목표 도달을 보고한 `CMP_BASELINE_2.0.0_V2` (내부 구조 V2.1, shelf 제거/PolAct0.5)를 대상으로 **전류·MQW Rad/SRH/Auger·IQE의 독립 검증**을 시작하기로 함. 기존 V2_Copy 기록은 이전 선택 이력이며 현재 작업 대상 아님.
- 진행 단계: 서버 출력 대기. 사용자에게 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`에서 n2/n6 TDR/PLT 존재 여부, *.sta, 로그 마지막 anode 전압/전류를 읽기 전용 확인하는 명령 제공. 사용자 실제 검사 결과는 아직 전달되지 않음.
- 이후 파일 출처와 최종 바이어스 검증을 통과하면 기존 5V_TEST와 같은 SVisual 방식으로 동일 QW ROI의 Radiative/SRH/Auger 적분 → 정의를 분리한 QW IQE 추정 → 동일 전류밀도 비교. 원본 코드/시뮬레이션을 임의 변경하지 않음.
- 이택규 역할(구조/solver 검증)은 GPT의 권장 분담이며 당사자 간 확정 합의 또는 실시간 진행으로 주장하지 않음.

## 2026-10-15 — V2_Copy 독립 검증 담당 선택 (PROPOSED, 검증 실행 전)
- 작업자: 주수빈. 본인 요청으로 이택규의 두 V2 계보를 비교한 뒤 `CMP_BASELINE_2.0.0_V2_Copy`를 우선 검증 대상으로 선택.
- GitHub 기존 실행 보고 기준 V2_Copy는 shelf 유지/하부 cathode 유지/PolAct=0, n2(NtSide=0) 약 2.069V, n6(NtSide=1e18) 약 2.036V에서 정체. 이 수치는 Claude 보고의 전사값이며 이 세션에서 학교 서버 원본 로그 미열람.
- 계획: 원본 보호 및 read-only 로 *.sta, pp*.cmd, n2/n6 log 마지막 accepted V, 비수렴/MinStep/CNormPrint/NewtonPlot와 shelf/cathode/mesh 설정 점검. 실패 메커니즘 특정 전 임의 모델 수정·재실행 없음. V2.1과 shelf 외 PolAct/cathode도 달라 인과 단정 금지.
- 상태: PROPOSED 검증 계획; 실제 수빈 검사 결과는 아직 없음.

## 2026-10-13 — 3주차 발표 12번 '향후 연구 계획' 단일 슬라이드 개정 (PRESENTATION / OBSERVED)
- 사용자 요청으로 기존 13장 중 **12번 슬라이드만** 가독성 중심의 4단계 로드맵으로 재설계하고, 요청대로 한 장짜리 편집 가능한 PowerPoint로 출력: `CMP_3주차_12번_향후연구계획_한장.pptx` (채팅 산출물; GitHub 바이너리 업로드 안 함).
- 핵심 순서 유지: ① 전류 정규화·Mg/EBL/MQW 수송 검증 → ② 동일 전류의 Trap별 QW SRH/Radiative 비교 → ③ Full/Half·Mesh 정확도 검증과 Baseline 확정 → ④ Project A C 고저항 Edge와 B AlGaN Barrier 성능 평가.
- 하단 지표는 측벽 SRH↓, QW Radiative↑, IQE↑, 구동전압 페널티로 축약. 미해결 항목은 향후 단계로 표시했으며 이미 완료된 것처럼 표현하지 않음.
- 원본 2주차 밝은 배경·청록색 팔레트·헤더/푸터 계승. 수정 슬라이드만 분리한 PPTX의 slide count=1, ZIP 무결성 및 LibreOffice PDF 1페이지 변환·PNG 렌더링 확인. TCAD 코드·시뮬레이션·연구 결론 변경 없음.

## 2026-10-13 — 3주차 PPT 11번 슬라이드 가독성 개정 (PRESENTATION / OBSERVED)
- 사용자 요청으로 11번 '추가 원인 검토'의 장황한 로그 상태표를 교체. 9·10번 개정 슬라이드 유지, 13장 전체 PPTX 산출물 `CMP_Week3_JuSubin_Slide11_Clear.pptx` (채팅 전달, GitHub에 PPT 바이너리는 올리지 않음).
- 핵심 흐름을 ① 손실 위치: 이택규의 별도 CAL4V에서 전체 domain SRH 중 EBL 약 99.77% 집중으로 보고 ② 원인 후보: EBL/MQW 정공 주입 및 수송 제한 가능성은 UNRESOLVED ③ 검증 방향: POL50(activation 1.0→0.5) 별도 분극 민감도 시험, 4V 수송 결과 완료 확인 전으로 축약.
- 실제 CAL4V SVisual cutline 이미지 삽입 위치는 그대로 두고 가짜 SVisual 결과를 생성하지 않음. 사용자 전달 Claude 분석 보고치와 주수빈의 별도 5V_TEST 데이터를 혼합하지 않고, 원본 학교 서버 출력 미검증임을 각주에 표시.
- PPTX 13장 재파싱, LibreOffice PDF 13장 변환, 11번 페이지 렌더링 시각 확인 성공. TCAD 코드·물성·실제 시뮬레이션 변경 없음.
- 다음: 실제 SVisual cutline 확보 시 placeholder 교체; 사용자가 PowerPoint 열림 및 발표 디자인 확인.

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

## 2026-11-04 02:26 KST — Wu CMP_WU_Copy n29 NtSide1e17 convergence hotspot (OBSERVED / ROOT UNRESOLVED)
- 작업자: 주수빈; AI: ChatGPT. 사용자가 제공한 실제 n29_des.out에서 마지막 accepted anode 2.420E+00 V, Quasistationary pseudo-time t=0.484021 확인. 이후 여러 연속 전압 단계에서 Newton 35회 소진, step을 4.1904e-05→1.5985e-10 등 계속 절반으로 감소; 최종 step 7.9926e-11 < MinStep로 종료. SDevice job 종료는 5V 완료가 아님.
- Newton 반복 마지막 21~35에서 global error 약 3.77~6.00으로 진동. max C-norm hole 좌표 (x≈0.1610~0.1615,y=9.995117)um, Poisson/electron error 좌표 (0.1650273,10.0)um. QW4/Barrier4의 우측 손상 측벽에 해당할 가능성 큼: GitHub Wu3.2 candidate SDE상 QW4 x=.161-.164, Barrier4 x=.164-.172, right damage y=9.995-10.0; 학교 pp1 geometry 동일 여부는 미확인.
- 직접 원인은 정공 방정식을 포함한 coupled Newton 비수렴, 근본 물리/수치 원인은 UNRESOLVED. NtSide=1e17이 반드시 비물리적이거나 잘못된 값이라고 판단하지 않음. 제출된 n29_des.err tail 결과 없음.
- 변경: 학교 코드·GitHub deck·n21/n25 5V 저장 자료 변경 없음. 다음: 학교 pp29_des.cmd/pp1_dvs.cmd의 실제 geometry/solver/trap parameter, n29_des.err, 마지막 accepted 상태의 sidewall QW4/Barrier4 근처 정공/전위/트랩 분포를 가능한 한 비실행 방식으로 확인.
