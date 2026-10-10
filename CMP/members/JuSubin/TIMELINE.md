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
