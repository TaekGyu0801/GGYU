## 2026-10-12 — 이택규 CAL4V polarization 50% one-variable experiment (DECISION / PROPOSED; not yet run)
- User explicitly chooses an immediate isolated sensitivity test: clone current completed CAL4V, change ONLY effective polarization-charge activation 1.0 to 0.5 (after verifying the actual active Sentaurus T-2022.03 syntax/parameter scope). No assumption this is experimentally calibrated.
- Verify actual server parent input, pp2_des.cmd/.par, Physics scope, interface polarization charge and absence of independent overriding FixedCharge; clone and preserve parent TDR/log/mesh/results. Nominal Goal 4V, FinalTime 0.8s, 5V/s transient, contacts, geometry, doping, NtSide=0, SRH lifetime, traps, all other physics, material parameters, mesh, solver held fixed.
- Candidate name CMP_BASELINE_1.4.0_POL50, subject to server name collision and version policy check (physics change needs MINOR not PATCH). SWB native filenames unchanged; check original model actually applies activation 1 and where.
- Claude may prepare/run isolated clone after preprocessed one-factor diff and quick syntax smoke. No second factor or additional bias hold. Compare parent/new exact bias/time, anode/cathode currents, EBL/QW SRH+Radiative, e/h QF/density, actual PE_Charge distribution, geometry and unit consistency. Improvement proves sensitivity only, not polarization as sole cause.
- No school server execution or code edit by ChatGPT. JuSubin 5V_TEST unchanged; Claude/user must report actual simulation outcome and GitHub sync according to protocol. Prior CAL4V 99.77% EBL SRH user-reported, cause UNRESOLVED.

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

## 2026-10-12 JuSubin matched-current voltage from 5V_TEST transient PLT
OBSERVED n2 data: V=4.91836886499322 I=6.84313365428304e-12, and V=4.92336886499322 I=7.14463993632474e-12. Target n4 final 5V raw I=7.05011114486348e-12. LINEAR INTERPOLATION gives n2 V=4.921801256006416, n4 needs 78.198744 mV more for same raw TotalCurrent on 5 V/s Transient. Not a DC steady-state resistance or equal-J MQW comparison. No TDR at n2 4.9218V, no corresponding ROI recombination measured. Next read-only current components/displacement near n2 target, 2D AreaFactor and saved snapshot needs. No solver files modified.

## 2026-10-12 — 이택규 Claude CAL4V 4V whole-domain recombination integration; interpretation correction (USER-REPORTED / DERIVED / UNRESOLVED)
- SOURCE: 이택규 전달 Claude 19:30 KST server-output summary; raw server .tdr / SVisual integration report not directly retrieved by this ChatGPT. Claude says CAL4V 4V `n2_4V_final_des.tdr` integrated whole-domain: SRH=12294.2, Radiative=2.43e-3, Auger=2.96e-4 [s^-1 um^-1]. Per reported named regions: Clean_EBL=12230.8, DmgL_EBL=34.8; Clean QW1 4.94, QW2 0.125, QW3 0.049, QW4 5e-5; previous 8-QW total SRH≈5.134. Anode TotalCurrent=3.498e-14 [A/um]. No source modifications or new simulations.
- DERIVED from transmitted values: EBL SRH subtotal 12265.6 / total 12294.2 = 99.76737% of modeled whole-domain SRH. 8-QW SRH fraction ≈0.04176%; Barrier1(19.6)+Barrier2(3.69)=0.18944%. Strong evidence for modeled EBL SRH localization **if** all region integrations are correct; NOT proof EBL hole barrier causes it. Check AlGaN actual SRH lifetime/Scharfetter parameters, electron/hole densities, field and region tags.
- DERIVED: q*(12294.2 + 0.00243 + 0.000296)=1.9697484e-15 [A/um]. Ratio to anode total=0.0563107=5.6311%. Under unverified normalization W=2um, equivalent J_rec=9.8487e-8 A/cm2. **CRITICAL CORRECTION**: the remaining 94.3689% is NOT demonstrated capacitive/transient current. q*net recombination is a bulk recombination sink, not independently the total DC conduction: it does not account for possible carrier through-current/leakage, carrier storage, generation, contact/boundary and terminal signs. Claim '94% charging and 5.6% true DC' is UNRESOLVED, not OBSERVED or CONFIRMED. Read-only anode Charge dQdt small (≈0.008 ratio 2.5–4 V) also does not prove or disprove total device charging since electrode charge scope differs from entire device; reported contact DisplacementCurrent ~1e-18 alone cannot classify the remainder.
- Claude ranks EBL/Barrier0/QW1 boundary hole transport candidate P1, intrawell NLM P2; both PROPOSED. Previous user-reported EBL hQuasiFermi flat complicates direct assignment of large hQF drop inside EBL; full cutline must resolve actual layer boundaries. Need both e/hCurrentDensity and n/p as well as QF, Potential, Ec/Ev, srhRecombination and PE_Charge.
- NEXT READ ONLY: (1) Verify entire integration spatial coverage/units, EBL effective SRH lifetime in actual `pp2_des.par` or effective SDevice material properties; (2) central verified CLEAN growth-direction x cutline from p-GaN through EBL–Barrier0–QW1 and MQW, with ElectrostaticPotential, Ec/Ev, e/hQF, e/hDensity, e/hCurrentDensity, SRH, PE_Charge; geometry lateral cutline to check y=2um clean position; (3) assess spatial current continuity/cathode currents and transient balance. No NLM/polarization/lifetime changes before verification. JuSubin 5V_TEST untouched.
- REFERENCE for general continuity/electrode-charge concepts: Sentaurus Device UG O-2018.06 Ch. 7 Electrode Charge Calculation and Ch. 8 Carrier Transport in Semiconductors, https://studylib.net/doc/27467177/sdevice-ug---%E5%89%AF%E6%9C%AC (older publicly viewable edition, NOT independent verification of T-2022.03 exact text).

## 2026-10-12 — 이택규 CAL4V Claude 19:30 재판단 전달 / ChatGPT 독립 검토 (USER-REPORTED / DERIVED / UNRESOLVED)
- SOURCE: 이택규가 Claude 작성 `CAL4V_LOWJ_LOWIQE_DIAGNOSIS.md` 텍스트를 현재 채팅에 제출. 이는 **Claude 보고서의 내용**이지 ChatGPT가 Sentaurus 학교 서버나 T-2022.03 원본 문서를 직접 검증한 결과가 아님. 기존 CAL4V 코드/실행 변경 없음.
- Reported CAL4V 4V: anode TotalCurrent=3.498e-14 A/um; QW integrals Rad=6.29e-4, SRH=5.13, Auger=2.13e-4 s^-1 um^-1. From these values, q*(Rad+SRH+Auger)=8.221e-19 A/um and ratio to anode total=2.350e-5 (0.002350%). This **does not itself prove** 98% charging current or hole-only starvation: QW-outside recombination, other leakage paths, transient charge and sign/normalization must be checked.
- Claude RETRACTED claims that 4V current is 98% charging, MQW QF jumps add up to 2V loss, or EBL band bending proves 1V electrostatic loss. Claude reported parent 5V displacement=3.29e-18 against total=1.448e-11 (different run/bias); cannot infer 4V CAL4V charging fraction from 5V parent electrode component. Earlier 4V I(V) plateau and tau-insensitive anode current are suggestive, not direct transient charging measurement.
- Claude also reported flat hQuasiFermi through EBL on user SVisual cutline, reducing evidential support for EBL as dominant **hole electrochemical potential drop**. QW1 radiative concentration alone cannot establish which carrier is limiting; inspect n, p, e/h current and QF across verified coordinates.
- Claude reported T-2022.03 UG text inspection: NonLocal keywords exist but proposed V2 has potential wrong mesh-side coverage and missing tunneling mass mt. Exact manual excerpts were not independently made accessible to this ChatGPT; no V2 deployment. Model choice (NLM/polarization/composition variation) UNRESOLVED, baseline protected.
- Important verification boundary: SDevice `anode Charge` is **electrode charge plus associated doping-well space charge**, not necessarily the device-wide stored-charge integral (O-2018.06 UG, Electrode Charge Calculation). Thus d(anode Charge)/dt / anode TotalCurrent near one is a diagnostic only, NOT a sufficient standalone confirmation that 90-100% of current is junction charging; require terminal signs/conservation, time/bias dependence and charge scope. 4V conduction-vs-charging remains unresolved.
- NEXT (READ-ONLY): inspect CAL4V `n2_des.plt` actual datasets and synchronized `anode/cathode Charge, TotalCurrent, DisplacementCurrent, eCurrent/hCurrent, time, bias`; estimate finite differences with units/signs and no sharp arbitrary thresholds. Then export verified central clean-region TDR cutline e/hQF, density, current, Ec/Ev, Potential, polarization fields; resolve actual NLM coverage/manual before any user-approved small-scale smoke. JuSubin 5V_TEST untouched.

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

## 2026-10-12 — JuSubin 5V_TEST n2/n4 eight-QW three-channel recombination comparison (OBSERVED)
- Worker 주수빈. Evidence: Sentaurus Visual Field Integration pasted outputs for RadiativeRecombination, srhRecombination, AugerRecombination on 8 distinct 2D regions Clean_QW1..4 + DmgL_QW1..4 (avoid '+' interface labels). Total Domain 0.02400002 um² for each node, units for all integrals s^-1 um^-1.
- n2 NtSide0: Radiative 40072.82; SRH 36562940; Auger 1599.707; 3-channel total 36604612.527; Radiative fraction 0.10947478264%; SRH share 99.88615498397%; Auger share 0.00437023339%.
- n4 NtSide1e18: Radiative 7056.261; SRH 14411700; Auger 265.2578; 3-channel total 14419021.5188; Radiative fraction 0.04893716949%; SRH share 99.94922319250%; Auger share 0.00183963801%. n4 Auger detailed Clean region sum (display rounded)=264.6098086; DmgL region sum=0.6480449636; rounded sum 265.25785356 (within display rounding of stated total).
- n4 relative to n2 at nominal 5V: Radiative -82.3914%; SRH -60.5839%; Auger -83.4184%; radiative fraction relative decrease 55.2982% (absolute -0.0605376 percentage points).
- Grouped 3-channel radiative shares from region-rounded sums: n2 Clean ~0.10984%, DmgL ~0.05195%; n4 Clean ~0.04909%, DmgL ~0.02484%. Regional fractions represent spatially integrated model channel ratios only.
- CRITICAL INTERPRETATION: these are 4QW modeled 3-channel recombination fractions, NOT measured EQE or independently validated whole-device IQE. n2 raw 5V current=1.4480164608e-11 vs n4=7.050e-12 (different injection), so fixed-voltage difference is not matched-current trap causal proof. TCAD 2D current AreaFactor, time-dependent/displacement contribution, QW hole injection and physical calibration still require validation. Node2 explicit 12 DmgL sidewall traps Conc=0 while global SRH is active. Dominant SRH is an observation, its microscopic cause is not established.
- NEXT: review n2/n4 electrode TotalCurrent vs DisplacementCurrent and normalized J from saved .plt; examine whether equal-current comparison is possible with existing saved intermediate 2D TDRs, else mark additional snapshot requirements before any new run. Do not modify baseline/code or rerun until plan approved.

## 2026-10-12 — 이택규 CAL4V MQW nonlocal tunnel v2 (PROPOSED; independent literature review)
- 이택규가 사용자 보고 SVisual cutline에서 각 QW/barrier 계면 ~0.35-0.5eV e/h QF 급변과 밴드 스파이크를 보고, Claude가 MQW reference-surface NonLocal tunneling 모델을 제안. 각 QW의 eQF-hQF 값은 약 1.95/1.90/1.75/1.45eV이며 이는 인가전압 손실이 아님. Thermionic 이종접합은 QF 불연속을 허용하므로 계단만으로 터널링 누락을 입증하지 못함. 4V displacement-current 분리, 2D J normalization, 중앙 cutline 좌표 검증은 계속 미완료.
- Rahman et al. 2022 J Appl Phys DOI 10.1063/5.0125684 실제 PDF p3/p5 확인: Silvaco TCAD에서 thermionic+field emission+nonlocal quantum-barrier tunneling을 적용했으며 모델 수송개선에 기여. 단 균일 In well에서는 여전히 실험과 전압 차이가 크며 low-In/high-In lateral composition-fluctuation 경로를 함께 사용해 개선. 이 논문은 Sentaurus T-2022.03의 특정 Math/Physics 구문을 검증하지 않음.
- 제안한 MaterialInterface=InGaN/GaN / Length=5e-7 cm / Permeation=5e-7 cm / Direction=(1 0 0) / MaxAngle=5은 user PROPOSED. 5nm path-limit는 22nm barrier를 가로지르는 직접 interwell tunnel 보장하지 않고, plane당 QW interfaces는 4×2=8이며 clean/damaged 분할 면수는 실제 mesh/log 검증 필요. T2022 공식 UG 원문은 현재 연결된 저장소에 없고 구버전 가이드로만 일반 키워드를 확인했으므로 syntax exact UNVERIFIED. Current>1e-12 A/um (3.5V) 기준 임의의 성능 임계값이고 이 alone 물리적 타당성 지표로 채택 금지.
- NEXT 현재 n2_des.plt에서 DisplacementCurrent/TotalCurrent 분리 및 4V TDR cutline carrier densities, band/potential and current density; 실제 공식 UG T2022 문법·nonlocal line/physics parameter 확인 후 별도 versioned small prototype 검토. 원본 CAL4V와 주수빈 5V_TEST 코드/결과 수정 없음.

## 2026-10-12 — JuSubin 5V_TEST n2 8-QW Auger integrated; 3-channel rad fraction established (OBSERVED)
- Worker: 주수빈; evidence: pasted SVisual Field Integration results `n2_des` / `AugerRecombination` for 8 separate 2D QW areas (Clean_QW1..4, DmgL_QW1..4), excluding '+' boundary entries.
- Auger total = 1.599707e+03 s^-1 um^-1; total domain = 2.400002e-02 um^2. Clean integrals [252.5448,1.736316,12.65704,1327.983] subtotal 1594.921156; DmgL integrals [2.309115,0.003800247,0.05774334,2.414354] subtotal 4.785012587. Rounded constituent sum=1599.706168587 vs display total 1599.707 (rounding).
- From same n2 8-region ROI: Rrad=40072.82, SRH=36562940, Auger=1599.707 s^-1 um^-1. Three-channel normalized shares: Rad=0.10947478264%, SRH=99.88615498397%, Auger=0.00437023339%. The bulk SRH channel dominates; Auger is not observed as the main efficiency-limiting recombination channel at this specific modeled bias.
- These are model internal QW 3-channel integration shares, NOT experimentally calibrated EQE or definitive whole-device IQE. Need check recombination sign conventions/current normalization, equal-current normalization, QW hole injection/physics and baseline validation.
- Next: obtain n4_des AugerRecombination integration over identical 8 2D QW regions; calculate both nodes' 3-channel shares, distinguish fixed-5V and equal-current comparisons. No model/source/run changes.

## 2026-10-12 — JuSubin 5V_TEST n4 8-QW SRH integrated; 2-channel comparison (OBSERVED)
- Worker: 주수빈. User-provided Sentaurus Visual Field Integration exact result: dataset n4_des, field srhRecombination, 8 separate 2D QW regions Clean_QW1..4 and DmgL_QW1..4. Total Integral=1.441170e+07 s^-1 um^-1, Total Domain=2.400002e-02 um^2.
- n4 Clean_QW1=7.535253e4, QW2=2.335633e4, QW3=2.936031e5, QW4=1.392685e7; subtotal of region-rounded values=14,319,161.96. n4 DmgL_QW1=3.279025e2, QW2=8.810076e1, QW3=7.204654e2, QW4=9.139782e4; subtotal=92,534.28866. Rounded-entry sum=14,411,696.24866 vs displayed SVisual total=14,411,700, normal decimal rounding difference.
- Previously observed same 8-region n2 SRH total=3.656294e+07; n2/n4 Radiative totals=4.007282e4/7.056261e3 s^-1 um^-1. At nominal 5V, n4 SRH total lower by 60.5839%, while Radiative lower by 82.3914%.
- Two-channel Rad/(Rad+SRH) is n2 0.1094796%, n4 0.0489381% (n4 ~55.30% relatively lower). This is NOT final IQE; Auger integration incomplete, both 5V terminal currents differ and current-density normalization/physics remain unresolved. SRH falling with trap ON does not prove nonradiative trap effect absent: injection levels differ.
- NEXT: On n2 and n4 SVisual integrate AugerRecombination for same eight 2D QW regions, inspect signs, then calculate 3-channel radiative share; matched-current comparison separately. No solver rerun or TCAD code/mesh change.

## 2026-10-12 — 주수빈 5V_TEST n2 8-QW SRH SVisual integration (OBSERVED)
- 실제 사용자 제공 SVisual Field Integration 원문: dataset n2_des, field srhRecombination (lowercase s), 8 separate 2D QW ROI Clean_QW1..4 + DmgL_QW1..4. Reported Total Integral=3.656294e+07 s^-1 um^-1, Total Domain=2.400002e-02 um^2.
- Clean_QW1=7.765839e4, QW2=5.464576e4, QW3=5.841611e5, QW4=3.561769e7; Clean subtotal from rounded entries=36,334,155.25 s^-1 um^-1.
- DmgL_QW1=4.966036e2, QW2=1.416049e2, QW3=1.655249e3, QW4=2.264962e5; DmgL subtotal from rounded entries=228,789.6575 s^-1 um^-1.
- Display-rounded 8 entries sum=36,562,944.9075, differs from authoritative SVisual Total=36,562,940 by 4.9075 due to field output rounding. QW4 total SRH share ~98.0342%; DmgL share ~0.62574%.
- Previously n2 same 8 QW ROI Radiative total=4.007282e+04; 2-channel radiative share (excluding Auger) =0.10947957%, NOT final radiative fraction or IQE. 12 sidewall DmgL trap concentrations in n2=0; background SRH remains ON; no proven causal attribution.
- NEXT: n4_des srhRecombination integration on same 8 ROI; then AugerRecombination both n2/n4 before final ratio and equal-J discussion. No simulation or source modifications.

## 2026-10-12 — CAL4V low-J literature and model critique (REVIEW)
- 2026-10-12 18:23 KST, worker 이택규 shared Claude independent CAL4V low-J diagnosis for critical review. This is REVIEW, NOT actual new simulation evidence. 1. CAL4V 4V Transient ramp 5V/s, terminal total=3.498e-14 A/um. Claude says 98% displacement and conduction 0.7e-15 A/um. Actual charging fraction UNVERIFIED: plateau alone cannot decompose; inspect n2_des.plt anode DisplacementCurrent and TotalCurrent data at 4V. Current-density conversion remains conditional on 2D normalization. Output eCurrent~5.27e-20, hCurrent~3.498e-14, total~3.498e-14 should be identified carefully before claims. 2. With all current assumed capacitive, C'=I/(5V/s)=6.996e-15 F/um. eps_r 9.5 and 2um x1um assumed footprint give equivalent t~24.0nm near EBL 26nm; arithmetic correct but distributed capacitance cannot localize EBL voltage drop. Need actual Ec/Ev/Potential profile. 3. From Rrad/SRH ≈ B tau (n+p) with B=2e-10 cm3/s and tau=100ns, n+p≈6.12e12 cm-3 conditional on ideal Bnp, equal lifetimes, negligible SRH n1/p1, uniform carrier density; integrated 8-QW values and doping-dependent lifetime invalidate direct inference. Not proof of low hole density. 4. EBL hole barrier/polarization is scientifically plausible from published studies but causal ranking remains PROPOSED; alternative current normalization, contact injection, active hole doping, band offsets, distributed carrier density, missing calibrated transport physics remain. 5. Literature verified: Lu et al 2021 Nanoscale Research Letters 16:99 DOI 10.1186/s11671-021-03557-4 explicitly uses 50% polarization and 100ns SRH; Yin et al 2024 Frontiers of Optoelectronics 17:8 DOI 10.1007/s12200-024-00111-9 explicitly uses 50% polarization, 100ns and SRV=1e4 in different MIS microLED; Baek et al 2023 Nat Commun 14:1386 DOI 10.1038/s41467-023-36773-w is low-current QB/EBL engineering (not source for 50% polarization); Rahman et al 2022 JAP 132:235702 DOI 10.1063/5.0125684 explains composition fluctuations / limits 1D fixed-polarization models, not proof a specific Nonlocal tunneling keyword is mandatory. 6. Do not copy global eBarrierTunneling+hBarrierTunneling with NonLocal Barrier(Region=Clean_EBL Region=DmgL_EBL) Length=4e-6 into current model. Sentaurus documentation states Barrier(...) mesh configuration primarily for direct insulator barriers; AlGaN EBL is semiconductor, actual valid T2022.03 geometry and tunneling masses/method unknown. Turning polarization off only at AlGaN/GaN interfaces does NOT remove InGaN/GaN MQW QCSE. Polarization 0% and 50% allowed only as clear diagnostic/sensitivity hypothetical with original 100% controlled, no arbitrary recalibration. Next: inspect existing n2_des.plt dataset list for DisplacementCurrent/TotalCurrent and 4V values, then SVisual existing n2_4V_final_des.tdr vertical center cutline Ec/Ev, quasi Fermi, n/p, PiezoCharge and current density; ONLY then consider independently versioned 1D controlled stack or 2D half run. 1D loses mesa/sidewall and QS may not converge; no promise faster. Maintain JuSubin 5V_TEST split ownership. No simulation/TCAD source changed.

## 2026-10-12 — JuSubin 5V_TEST n2/n4 4QW RadiativeRecombination integration (OBSERVED)
- 작업자: 주수빈; AI: ChatGPT. 실제 Sentaurus Visual `Field Integration` 출력 원문 제공. 8개 2D QW ROI: Clean_QW1..4 + DmgL_QW1..4, '+' 결합 경계 제외. 단위 s^-1 um^-1; 각 n2/n4 적분 총 Domain=2.400002e-02 um^2.
- NtSide=0 n2 total=4.007282e+04; Clean total=3.995389e+04; DmgL total=1.189258452e+02. NtSide=1e18 n4 total=7.056261e+03; Clean total=7.03327165e+03; DmgL total=2.298885541e+01.
- n2→n4 radiative integral -82.3914% at nominal 5V; Clean -82.3965%; DmgL -80.6696%. QW4 strongly dominates radiative integral.
- IMPORTANT: n4 5V raw terminal current 7.050e-12 vs n2 1.4480164608e-11 (-51.31%), so observed radiative decrease is NOT an IQE decrease or controlled equal-J causal estimate. Bias at TDR should remain independently checked if needed, 2D AreaFactor/current normalization unverified.
- Prior live preprocessed cmd diff observed only trap Conc=0→1e18 and node output filename changes; both Grid=n1_msh.tdr, Parameters=FASTC1_pp6_des.par. Exact parameter runtime version / physical baseline validation unresolved.
- NEXT: Integrate SRHRecombination (or signed SRH field where listed) and AugerRecombination on precisely same eight 2D QW regions for both n2/n4; then compute Rrad/(Rrad+RSRH+RAuger) carefully with any signed generation terms, evaluate equal-current comparison separately. No server source changes.

## 2026-10-12 — CAL4V NtSide0 explicit traps OFF; SRH remains high (OBSERVED)
- 2026-10-12 이택규 read-only live CAL4V pp2_des.cmd grep confirms twelve explicit `Traps` blocks at 141/161/181/201/221/241/261/281/301/321/341/361, all corresponding `Conc=0` lines 145/165/185/205/225/245/265/285/305/325/345/365. Therefore 4V completed CAL4V n2 is **explicit NtSide trap OFF** (source preprocessing evidence), yet prior MQW 8-QW integrated recombination Rrad=6.286680e-4, SRH=5.134239, Auger=2.127778e-4 (s^-1 µm^-1), radiative fraction 0.01224261249% and SRH 99.98361378%. Those zero-concentration explicit sidewall traps cannot cause observed CAL4V SRH dominance, but unknown other SRV/interface or bulk SRH mechanisms cannot be excluded. Active global Physics contains SRH(), Auger(), Radiative, Fermi, Thermionic, Piezoelectric_Polarization(strain), custom referenced InGaN Scharfetter taumax=1e-7 s; physical carrier transport and 2D current normalization remain unverified. Hypotheses about bad contact, EBL/polarization or carrier imbalance remain UNRESOLVED, not findings. Next read-only inspect current-density normalization in SDevice output and available .plt or existing electron/hole densities in 4V final TDR, and possibly effective QW doping. No code or simulator change. Independent track from JuSubin 5V_TEST trap ON/OFF study.

## 2026-10-12 — CAL4V region Physics audit step (OBSERVED)
- 이택규 provided real CAL4V pp2_des.cmd read-only grep: global Physics line 50, Piezoelectric_Polarization(strain) 64, global SRH() 80; separate Physics(Region="Clean_pGaN") at 126 and 12 Physics(Region="DmgL_...") at 135,159,179,199,219,239,259,279,299,319,339,359. No separate Recombination/SRH declaration and no literal SurfaceRecombination, SurfaceTrap, Interface= matched in this search. Plot SRHRecombination et al at 398+ are output field names, not evidence of extra active recombination. IMPORTANT search omitted Traps, so region-specific explicit traps may still exist; absence of named surface keywords does not prove actual SRV=0. Existing CAL4V referenced InGaN Scharfetter taumax=1e-7s remains confirmed nominal. Root cause of low J/radiative fraction unresolved. NEXT perform read-only `grep -nEi 'Traps|Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/pp2_des.cmd | head -n 35` to check n2 trap concentrations. No model changes; separate JuSubin 5V_TEST split task unaffected.

## 2026-10-12 — CAL4V InGaN SRH tau confirmation
- 이택규 CAL4V 실제 referenced FASTC1_pp6_des.par InGaN Scharfetter 설정 확인: taumin=0,0; taumax=1e-7,1e-7 seconds (100ns both carriers), Nref=1e16,1e16 cm^-3; gamma=1; Talpha/Tcoeff=0. Field-dependent effective SRH lifetime NOT proven 100ns; dopant dependence and other Physics overrides pending. 4V raw current, low-J and 4-QW radiative fraction 0.0122426% still physically unvalidated. Next inspect actual QW carrier injection and current normalization, not re-run or blindly edit tau.

## 2026-10-12 — LeeTaekGyu CAL4V global Physics read-only verification
- 2026-10-12 이택규 CAL4V의 실제 `pp2_des.cmd` lines 14–90 read-only sed 출력 제공. File: Grid=n1_msh.tdr; Parameters=FASTC1_pp6_des.par; Plot=n2_des.tdr; Current=n2_des.plt; Output=n2_des.log. Electrode anode/cathode both initial Voltage=0.0. Global Physics: Temperature=300.0, Fermi, Thermionic, Piezoelectric_Polarization(strain), DefaultParametersFromFile, EffectiveIntrinsicDensity(NoBandgapNarrowing), Recombination(SRH(), Auger(), Radiative). 이 블록은 세 재결합 모델 활성화의 직접 증거지만 InGaN 유효 SRH tau=100ns 또는 국소 재결합 수치의 근거 자체는 아니다. 이전 whole pp2 grep에는 AreaFactor 미표시; 단자 전류 단위, 2D normalization 미확인. 다른 per-material/per-region Physics overrides, 명시적 surface recombination 설정 존재 여부도 아직 미확인. NEXT 별도 CAL4V custom active par `FASTC1_pp6_des.par`에서 InGaN Scharfetter/SRH tau 및 active material blocks 읽기전용 검사; 이후 pp2 global/local Physics 범위와 current scaling 검증. 서버 파일이나 계산 결과 변경 없음. 주수빈의 5V_TEST split parity/QW integration과 다른 독립 track 유지.

## 2026-10-12 — Parallel worker task split to avoid overlap (PROPOSED)
- 2026-10-12 ~17:03 KST, current worker 이택규 says he is now working alongside 주수빈 and wants nonoverlapping tasks. Proposed coordination (not confirmed as accepted by 주수빈): 이택규 owns read-only physical Gate0/low-current audit in separate project `CMP_BASELINE_1.3.0_CAL4V` (2D terminal current units/AreaFactor, active InGaN SRH 100ns, QW injection/EBL/polarization) without source modifications; 주수빈 may own `JUSUBIN_FAST_HALF_5V_TEST` NtSide0 Node2 vs NtSide1e18 Node4 5V parity gate (pp2/pp4 deck and .par/mesh differ only trap) followed by paired MQW Rrad/SRH/Auger integrals, avoiding overlapping CAL4V. Both finished sources/results remain protected. Last user-provided `pp4_des.cmd` grep explicitly showed 12 Traps Conc=1e18, confirming planned NtSide1e18 actual preprocessing (pending pp2-vs-pp4 other-input parity). No fresh simulation or technical result here; this is a PROPOSED parallel work allocation. AI cannot directly send task to collaborator's separate chat; share via GitHub as a proposed handoff only.

## 2026-10-12 — Low-IQE candidate causes collected (PROPOSED, no code changes)

- 이택규 shared four unverified possibilities: sidewall SRV/surface traps, polarization/QCSE, Auger-vs-SRH lifetime/current regime, and MQW/sidewall mesh. Logged for later audit, **not scientifically confirmed** and no parameter tuning adopted.
- Constraints: NtSide0 explicit 12 DmgL trap concentrations already 0 in its verified pp deck (not proof SRV everywhere zero); CAL4V 4V radiative fraction 0.0122426%, SRH share 99.9836%, Auger share 0.00414%; low-J normalization and polarization validity unresolved. Do not presume values such as SRV 10³–10⁴ cm/s or polarization Scale 0.3–0.5 are appropriate without literature calibration.
- Immediate next remains pp4_des.cmd trap Conc verification on completed Node4 5V before causal comparisons.

## 2026-10-12 — 5V_TEST Node4 normal finish verified and NtSide input pending
- 2026-10-12 현재 작업자 이택규가 SWB Node4 Explorer 실제 `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/n4_des.out` 마지막 화면 제공. 노드 n4: 5.000E+00 V, electron current 7.534E-14, hole current 6.975E-12, total terminal current 7.050E-12 (log raw values; 2D units/AreaFactor unverified), successful `n4_5V_ckpt_des.sav` and `n4_des.tdr` writes, `Curve trace finished`, `Sentaurus Device simulation finished`, `Good Bye`. Finished Mon 2026-10-12 00:12:02 KST; wallclock 29806.55s (~8h16m46.55s), CPU total 80172.55s, peak memory 3.11GB. **CONFIRMED 5V SDevice n4 completion**, but screenshot does not show NtSide parameter: intended n4 NtSide1e18 split condition NOT CONFIRMED until pp4_des.cmd actual DmgL trap `Conc` audit and parent n2 input comparison. Previous 5V_TEST NtSide0 n2 terminal raw I2D~1.4480164608e-11, so n4 raw current ratio ~0.487; no trap-only causal claim without pp2/pp4 parity. CAL4V 100ns 4V MQW radiative fraction=0.0122426% remains distinct simulation and bias; do not confuse n4 5V with CAL n2 4V. GitHub COMMON_BASELINE.md explicitly says blue InGaN/GaN, xIn=0.15 4QW, nominal ~445nm; desired color BLUE not red, spectral peak not verified by EL. Researcher asks whether normal efficiency '0.1': distinguish fractional 0.1=10%, 0.1%=0.001 as fraction, 0.1 A/cm2 current density not an efficiency. None is default expected at arbitrary J; literature (Kou 2019 10.1364/OE.27.00A643; Baek 2023 10.1038/s41467-023-36773-w; Wang 2023 10.1038/s41467-023-43472-z) confirms blue microLED efficiency depends on J, fabrication and sidewalls. CAL 0.01224% is modeled MQW 3-mechanism radiative share, NOT observed experimental EQE, and physical low-J Gate0/2D current normalization still open. NEXT read-only `grep -nE 'Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp4_des.cmd | head -n 16` to confirm actual trap concentrations. Further compare pp2/pp4 other physics/current and matched 5V QW recombination; preserve all existing outputs. No server code modified.

## 2026-10-12 — Literature benchmark for low-J CAL4V baseline
- 2026-10-12 Research assessment (이택규 question whether CAL4V radiative fraction 0.01224% is typical): Treat result as unusually low vs peer-reviewed working MicroLEDs, NOT sufficient proof of a model defect. Evidence: CAL4V 4.000V 2D raw terminal current 3.498e-14 (assuming A/µm), conditional half width ≈2µm gives J=(3.498e-14/2)*1e8≈1.749e-6 A/cm²; current conversion/AreaFactor/actual injection/steady-state remains unverified. Thus this is ~0.01/1.749e-6 ≈5718x below a published low-J example 0.01 A/cm² and ~0.1/1.749e-6≈57176x below 0.1 A/cm² benchmark. Published 3.5µm NBE-etched blue MicroLED Nature Communications 2023 DOI 10.1038/s41467-023-43472-z reports peak EQE 37.5% around 3 A/cm² and at 0.01 A/cm² only ≈26% relative droop; Nature Communications 2023 DOI 10.1038/s41467-023-36773-w reports 10x10µm blue MicroLED EQE 3.00% at 0.1 A/cm². Neither EQE benchmark is directly comparable to this model's MQW three-rate radiative share due to injection, geometry, sidewall processing and extraction differences. SRH normally dominates extremely low-current regime (literature-supported), but here NtSide0 still high SRH implies bulk/volume SRH or injection bottleneck rather than explicit sidewall trap; cannot infer causal parameter without matching sample and checking effective par. Existing parent 1ns at 5V had 0.10947% integrated QW fraction; CAL100ns at 4V is NOT matched bias, so changing lifetime cannot be causally judged. Recommended PRIORITY: verify current units, 2D AreaFactor, actual working J, effective InGaN 100ns parameter overrides, p/hole-injection/EBL/polarization/quantum well carrier densities, compare QW rates at same current and bias before baseline freeze, and avoid unmotivated long reruns. This is literature-backed review/diagnostic recommendation; NO simulation/model edit or confirmation of a single root cause.

## 2026-10-12 — CAL4V 100ns full 8-QW recombination summary
- 2026-10-12 이택규가 Sentaurus Visual 캡처 3장으로 완료된 `CMP_BASELINE_1.3.0_CAL4V` `n2_4V_final_des` (4.000V; custom InGaN 100ns Scharfetter taumax model) 8개 **2D** QW 영역 `Clean_QW1..4 + DmgL_QW1..4` 적분 결과를 제공. 세 필드 모두 정확히 동일 영역, Total Domain=2.400002e-02 µm². 전체 적분값 [s^-1 µm^-1]: RadiativeRecombination=6.286680e-04; srhRecombination=5.134239; AugerRecombination=2.127778e-04. 합=5.1350804458. Radiative/(Rrad+SRH+Auger)=0.01224261249%; SRH share=99.98361378%, Auger=0.004143612%. 여기서 방사비율은 해당 세 재결합 필드의 **MQW spatial integrated radiative fraction**이며, 100ns 모델 소자/실험 검증 IQE 또는 EQE가 아님. QW1 Clean+DmgL accounts for approx 98.78% all-4QW Rrad. DmgL 4QW only radiative ≈5.35942e-05 and SRH≈0.020185 (subtract clean 4QW totals; rounded), not independent lifetime physics validation. Preexisting 1ns parent result (NtSide0, **5V**) 4-QW Clean+DmgL Rrad=40072.8158452, SRH=36562944.9075, Auger=1599.706168587 and radiative fraction=0.1094747566%; because these are at DIFFERENT biases (100ns 4V, 1ns 5V), cannot attribute change to lifetime or claim 100ns improves/worsens IQE. Parent 4V near-terminal-current PLT exists but 4V TDR spatial map not yet established. Low-J Gate0 and current-normalization/physical validity still UNRESOLVED. Next inspect other user-reported completed NtSide1e18 split normal-finish log; for IQE causality compare same J/voltage/regions/geometry and effective .par, ideally reuse saved checkpoints, avoid rushing new multi-day run. No code/server run changed.

## 2026-10-12 — Team CAL4V clean-four-QW integrals
- CAL4V final 4V/100ns SVisual screen: 4 Clean_QW1..4 integrated Rrad total=5.750738e-4, SRH total=5.114054, Auger total=2.046436e-4 (s^-1 um^-1); total area=0.02394002 um2. Clean-only radiative fraction 0.01124326%. DmgL_QW1..4 NOT included; do not treat as full MQW or device IQE. Next add these 4 damaged 2D QW regions and integrate same fields, then check against matching 1ns bias/current and low-J Gate0. Evidence: screenshot supplied by 이택규.

## 2026-10-12 — CAL4V first QW integrated recombination result (OBSERVED)
- 2026-10-12 이택규 공유 SVisual `CMP_BASELINE_1.3.0_CAL4V/n2_4V_final_des` Field Integration 실제 결과: Dimension 2 region `Clean_QW1` 하나만 선택, Domain=5.985012e-03 um^2; RadiativeRecombination=5.674131e-04 s^-1 um^-1; srhRecombination=4.940556 s^-1 um^-1; AugerRecombination=2.045051e-04 s^-1 um^-1. 3항 합=4.9413279182 s^-1 um^-1. Clean_QW1에 한정한 radiative fraction =0.0114830084%, SRH fraction=99.9843783%. VERIFIED screenshot-based single-region integrations and ARITHMETIC; NOT entire four QWs, not total device IQE. Other QWs may differ substantially. Next integrate 2D volume Clean_QW1..4 AND DmgL_QW1..4 in all three fields (avoid `Clean_QW1+DmgL_QW1` interface rows if shown as Dimension 1). Compare 100ns 4V with 1ns at matched V/J and check current normalization. No TCAD source edits. NtSide1e18 split separate log verification remains.

## 2026-10-12 — CAL4V final TDR displays radiative and SRH fields (OBSERVED)
- 2026-10-12 이택규 제공 Sentaurus Visual T-2022.03 screenshots for `CMP_BASELINE_1.3.0_CAL4V` loaded dataset `n2_4V_final_des` (saved final 4V field). Observed Scalars `RadiativeRecombination` visible, color range min -8.67029e-34 max 7.00132e13 cm^-3 s^-1; `srhRecombination` visible, min -6.57253e-06 max 2.98898e18 cm^-3 s^-1. Earlier screenshot showed `AugerRecombination` as available Scalar. Mesh status shows Elements=138194, Points=65513. These are MAXIMUM VALUES ACROSS DISPLAYED SPATIAL FIELD and may not be colocated / may be in different physical regions. DO NOT interpret ratios of maxima as IQE or whole-QW integrated recombination; maxima do not establish 100ns physical IQE improvement. Need use Regions tab to identify Clean_QW1..4 and DmgL_QW1..4 region names in current saved TDR, then integrate RadiativeRecombination, srhRecombination, AugerRecombination separately in matched QW regions, ensure geometry/units 2D and compare to prior 1ns at matched bias. Other NtSide1e18 split separately pending log verification. Data only displayed, no 3-rate integral or new run/code change.

## 2026-10-12 — CAL4V completed at 4.000V, time 0.8s (OBSERVED)
- 이택규가 실제 `CMP_BASELINE_1.3.0_CAL4V/n2_des.log` grep 출력 공유. 마지막 `Computing BE-step from 0.799739 s to 0.8 s (Stepsize: 2.6098e-04 s)` 직후 `anode 4.000E+00 5.270E-20 3.498E-14 3.498E-14`가 표시됨. 직전 단계 0.798939→0.799739s에서는 anode 3.999V, 총전류 표기 3.496E-14. 앞서 확인된 동일 Node2 `Curve trace finished` / `Good Bye` 및 final `n2_4V_final_des.tdr`, `n2_4V_ckpt_des.sav` 저장과 연결되므로 100ns CAL4V에서 최종 time 0.8s / anode 4.000V, 로그 전류 마지막 열 3.498E-14 달성과 정상 완료 CONFIRMED. 로그 전류 물리 단위/2D AreaFactor 및 정상 DC상태는 독립 검증 미완료; 기존 기록의 2D A/um 관행에 따른 원시 수치이며 조건 없이 면적 전류밀도나 IQE로 간주하지 않는다. 참고: 기존 1ns 5V_TEST 가까운 4.003369V에서 I2D=3.505521343e-14였고 CAL4V 4.000V와 약 0.2% 원시 전류 차이이나 서로 완전한 동일 바이어스 아님. 100ns의 재결합 개선 여부 미확정. NEXT 이미 확보한 final TDR의 4QW별 Radiative/SRH/Auger 적분과 비교전류 정상화 후 연구 판단; 별도 NtSide1e18 split은 실제 로그 미검증. 원본 데이터 보존.

## 2026-10-12 — 두 시뮬레이션 완료 보고 접수 (USER-REPORTED; OUTPUT UNVERIFIED)
- 이택규가 2026-10-12 대화에서 주수빈이 전날 실행해 두고 간 '두 개' 시뮬레이션이 모두 끝났다고 보고. 직전 인수인계상 대상은 (1) 기존 `JUSUBIN_FAST_HALF_5V_TEST` 기반 NtSide=1e18 split과 (2) `CMP_BASELINE_1.3.0_CAL4V` (100ns, 0→4V)로 추정되며 **어느 두 SWB node인지 실제 로그나 화면으로 확인하기 전까지 프로젝트/노드 매칭 미검증**. 사용자 보고는 완료 주장의 근거이나 actual SDevice `Good Bye`/final V/timestep/terminal current/PLT/TDR/SAV는 미제공. NtSide=1e18 case가 NtSide-only matched input인지도 재확인 필요. 새 런이나 baseline freeze를 의미하지 않음. 기존 5V_TEST NtSide0 및 5V CAL 보호. 다음: 두 SWB 노드 이름, `n*_des.log` 마지막 35~50행, `pp*_des.cmd` Goal/Trap, 생성 PLT/TDR/SAV 확인→주입 전류 및 4QW Rrad/SRH/Auger를 동일 바이어스/전류 조건에서 비교. Gate0 낮은 J, 물리적 IQE/Full-Half 검증은 계속 미해결.

## 2026-10-11 — JuSubin reports 4V CAL4V Run initiated after FinalTime=0.8 check (USER-REPORTED; SOLVER START UNVERIFIED)
- Worker 주수빈 explicitly reports checking `FinalTime=0.8` in separately cloned `CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd` and clicking SWB **Run** for the new CAL4V simulation. The previous screenshot independently verified this clone's `Goal anode Voltage=4.0`, post-transient `Plot(FilePrefix="n@node@_4V_final")` and `Save(FilePrefix="n@node@_4V_ckpt")`, and custom `FASTC1_pp6_des.par` InGaN Scharfetter `taumax=1.0e-7s` for electrons/holes. New `FinalTime=0.8` is **USER-CONFIRMED**, not in a new screenshot. This retains nominal 5V/s ramp 0→4V. Source editing DONE by user; SWB Run action USER-REPORTED.
- Do NOT claim run has entered SDevice, succeeded or finished; **no new generated `ppN_des.cmd`, `nN_des.log`, job status, process PID, PLT, spatial TDR or SAV supplied yet.** SWB may auto-preprocess on Run; verify actual preprocessed Goal=4.0 FinalTime=0.8 Plot/Save and parameter file, and initial log for syntax/error/accepted time steps. End-point Plot/Save created only after successful final solve. Do not promise it finishes tonight.
- NEXT short READ-ONLY run-health check in `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V`: `ls -lt n*_des.log n*_des.err n*_des.out 2>/dev/null | head -n 12`; based on actual node filename, `tail -n 35 nN_des.log` and `grep -nE 'FinalTime|Voltage|4V_final|4V_ckpt|Parameters' ppN_des.cmd`; inspect SWB status screenshot if no logs yet. Leave existing 5V `CMP_BASELINE_1.2.0_CAL` and completed `JUSUBIN_FAST_HALF_5V_TEST` untouched; NtSide1e18 separate split status also not yet confirmed.
- Scope: exploratory SRH 100ns/4V sensitivity model. Prior low-J Gate0 and 5V_TEST physical baseline freeze unresolved. No ChatGPT access to school server, no direct run or code edit by assistant.

## 2026-10-11 17:39 KST — JuSubin confirms CAL4V clone still 5V source, before terminal patch (OBSERVED)
- User terminal screenshot directly shows normal shell read-only grep of `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd`: line 587 `FinalTime = 1.0`, line 597 `Voltage = 5.0`, line 608 `FilePrefix = "n@node@_5V_ckpt"`. There are also 0V initial electrodes at lines 38/43. No `3p8V`, `4V_final`, `4V_ckpt`. Confirms previous lengthy Python heredoc did NOT change this clone; no 4V simulation launched. Existing CAL5V remains separate active job.
- Decision: perform safe backup and short single-line shell sed edits in clone only. Replace FinalTime1.0→0.8, transient Goal Voltage5.0→4.0 (preserving 5V/sec rate), rename post-transient checkpoint to 4V, insert spatial Plot at 4V; optionally add intermediate t=.76 (~3.8V) Plot and Save once Solve shape checked. Do not touch 0V electrode defaults or custom CAL InGaN Scharfetter `taumax=1e-7`. Verify effective custom .par after clone; current `sdevice_des.cmd` grep alone does not prove clone's material params.
- NEXT: backup `sdevice_des.cmd` within `CMP_BASELINE_1.3.0_CAL4V`, use short commands in ordinary shell, grep/tail source after, SWB Preprocess only and check generated ppN/Plot/Save before RUN. This is a diagnostic 4V CAL, not frozen physical baseline. No remote edit performed by ChatGPT.

## 2026-10-11 17:36 KST — JuSubin normal shell restored; CAL4V SDevice file found (OBSERVED)
- Screenshot shows normal `$` prompt and `ls -l` confirms 5981-byte `CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd` (mtime Oct9 23:35); existence only, 4V edit not proven. Prior multiline script had not produced SUCCESS/STOP. NEXT read-only grep of FinalTime/Voltage/3p8V/4V_final/4V_ckpt/5V_ckpt to determine source state before writing a short non-heredoc patch. Active original CAL not touched by this check.

## 2026-10-11 17:28 KST — JuSubin 4V CAL Python heredoc still in terminal continuation (OBSERVED)
- MobaXterm screenshot displays `?` continuation prompt for pasted Python code and closing `? PY`, but **no SUCCESS/STOP or normal prompt**. The clone source edit is unverified; this is an interactive-shell input state, not SDevice solver failure. Advise one Enter on closing PY; if `?` persists Ctrl+C, explicitly enter bash and retry script. Read-only `grep -nE 'FinalTime|Voltage|3p8V|4V_final|4V_ckpt' .../CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd` plus backup listing before SWB Preprocess/Run. Active 5V CAL and parent 5V_TEST unchanged as far as evidence shows.

## 2026-10-11 17:20 KST — JuSubin confirms CAL Solve tail (OBSERVED)
- Existing active CAL source actually sets Transient FinalTime=1.0, anode Goal=5.0, Increment1.2 and Coupled Iterations15; final Save at 5V. Screenshot read-only only.
- Proposed separate 4V clone source change: FinalTime=.8 and Goal=4.0, with 3.8V interim spatial Plot/Save and 4V final Plot/Save; input 100ns unchanged. Not edited/run yet. Original jobs preserved.

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

## 2026-10-11 ~16:41 KST — JuSubin CAL 100ns n2 accepted ~4.179V (OBSERVED)
- Screenshot from `CMP_BASELINE_1.2.0_CAL/n2_des.out`: BE 0.835804→0.835806s accepted (`RHS=7.30e-04 <1e-3`); anode=4.179E+00 V, total current=5.555E-14 A/um in 2D convention.
- 5V goal relative sweep ~83.58%, **not runtime completion**; ~0.029V advancement vs Oct10 PLT 4.14965446V. Next BE 0.835806→0.835808s Newton iter2-6 RHS ~1.03e-3 to 1.09e-3 above threshold; later convergence unresolved. 5V not confirmed; no runtime ETA.
- Continue preserving CAL job; check subsequent log and Plot/Save/TDR availability read-only; 4V IQE state not confirmed, low-current Gate0 still blocking baseline freeze and A/B. No TCAD/solver/code change.

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

## 2026-10-10 ~22:11 KST — CAL 100ns n2 accepted ~4.149V; next step Newton oscillatory (OBSERVED LOG)

- **Evidence:** 이택규 실서버 `CMP_BASELINE_1.2.0_CAL/n2_des.log` latest 60 lines shared. BE from 0.829858 to 0.829862 s (stepsize 3.8830e-06s), iter2 `|Rhs|=8.97e-04 < RHSMin 1e-3`, `Finished, because... |RHS| less than 1.0000E-03`; anode=`4.149E+00 V`, total current=`4.832E-14` (2D A/um convention). **Thus 4.149 V was accepted**, not just being attempted. Next BE 0.829862→0.829867s (trial 4.6596e-06s), Newton iter2–9 oscillates RHS ~1.28–1.34e-03 (>1e-3), no eventual convergence/failure outcome in this truncated tail.
- Voltage fraction 4.149/5≈82.98% is **bias sweep fraction, NOT runtime progress**. Step2 completed in 86.24s vs earlier 13.67s; no reliable 5V ETA. Note previous accepted iteration still reports `error=1.11e+03` alongside small RHS, so examine numerical convergence robustness before claiming high-accuracy physical solution.
- Preliminary magnitude under parent-model width convention 2um: J~4.832e-14/2*1e8≈2.416e-6 A/cm² **conditional**; this is a transient total terminal current including possible displacement, not directly accepted as steady-state LED J. Cannot compare blindly against 5V_TEST parent's 5V result because voltage and SRH lifetime differ; low-current physical validation unresolved.
- NEXT read-only: inspect later CAL log and retained PLT 4V+ sweep only as useful; do NOT abort/modify/restart CAL just because 4V was exceeded. 4V is not an automatic verified working baseline. Preserve old 5V parent, project A/B NO-GO.

## 2026-10-10 22:04 KST — JuSubin independently confirms 5V_TEST n2 terminal completion (OBSERVED from screenshot; old job ended 2026-10-09 14:29:52 KST)

- Worker 주수빈 re-read existing `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` via grep/tail (two screenshots repeat identical output). Last accepted BE step: `0.999674 s -> 1.000000 s`. Terminal anode voltage `5.000E+00 V`; terminal electron current `2.781E-13`, hole current `1.420E-11`, total current `1.448E-11` in Sentaurus 2D current-per-length convention (A/um, not total measured 3D A). `Sentaurus Device simulation finished (Date: Fri Oct 9 14:29:52 2026 KST)` and `Good Bye!` show successful completion.
- This closes uncertainty about **solver log reaching 5V**, but does not yet prove specific opened `n2_des.tdr` snapshot was written at the final 5V state. Document provenance/time/Plot directive if required. Independently reported raw I2D ~1.44801646e-11 A/um / nominal J~7.24e-4 A/cm2 under documented width normalization and MQW Rrad share~0.1095% remain LOW-J GATE0 blocker; successful solver convergence is not physical baseline validation.
- A separate `n1_msh.tdr: Permission denied` arose because TDR binary/data file was typed as an executable in shell; **not a TCAD job failure**. Existing MgMinus ionization-field interpretation and EBL barrier causality also unresolved. CAL project status not updated and its running job must remain untouched.
- NEXT: prioritize quantitative low-current/injection Gate0 from existing outputs, verify TDR time-bias linkage if necessary, no repeated reruns or unsolicited code edits.

## 2026-10-10 ~21:57 KST — JuSubin Clean_pGaN and Clean_EBL numerical Ev/EFp comparison (OBSERVED SVisual screenshots; derived local-gap difference; transport cause UNRESOLVED)

- Worker 주수빈 provided TWO Probe screenshots in project `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, NtSide=0. Both at Y=1.0 um, Z=0; see zone to avoid accidental interface mixing.
- **Clean_pGaN(GaN)** X=0.05 um: `ValenceBandEnergy = -5.130097037559 eV`, `hQuasiFermiEnergy = -4.999999973858 eV`. Derived local `EFp-Ev = 0.130097063701 eV`. Earlier same-point `hDensity=3.000342790006e17 cm^-3`.
- **Clean_EBL(AlGaN)** X=0.13 um: prior screenshot `ValenceBandEnergy=-5.252508407140 eV`, `hQuasiFermiEnergy=-4.999999939039 eV`, so `EFp-Ev=0.252508468101 eV`; `hDensity=5.787900714824e15 cm^-3`; `Acceptor=3e17`, `Doping=-3e17`, `Donor=0 cm^-3`.
- DERIVED difference in **local** gaps EBL minus pGaN `0.122411404400 eV`. pGaN/EBL hole-density ratio ~51.84. Increased local EFp–Ev at EBL is consistent with lower hole density via nondegenerate `p ≈ Nv exp[-(EFp-Ev)/kBT]`, recognizing Nv differs for GaN vs AlGaN and thermodynamic/bias conditions matter. Not the full spatial hole-injection barrier or proof that EBL causes weak terminal current.
- IMPORTANT: device is labeled 5V_TEST but these snapshots alone do NOT prove TDR represents fully converged 5.0V final bias; an earlier `n2_des.log` screenshot mid-run showed anode around 4.139V at t~0.8277s. Verify actual final condition/status before claiming any 5V conclusion or baseline acceptance.
- Next: read-only inspect latest `n2_des.log` for last converged anode OuterVoltage/completion or recorded terminal voltage; then examine spatial Ev/EFp/valence-band offsets across exact EBL and MQW boundaries if low holes still important. No TCAD code/model or separate CAL job modified.

## 2026-10-10 — successful 5V_TEST Thermionic vs Piezo model log context inspected (OBSERVED; no physics bug proven)

- 이택규가 성공한 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` lines 345–425 실제 서버 출력을 제공. 셸 첫 입력이 두 `sed` 명령이 합쳐져 `.../n2_des.logsed` 파일 에러를 출력했으나 **뒤따른 동일 출력으로 필요한 본문을 정상 확보**, TCAD 자체 오류와 무관.
- 실제 물리 모델 설명: `With Thermionic Emission at heterointerfaces for electrons and holes` 바로 아래 `Without Piezo`; 별도 항목 `Without polarization` (line373), `Piezoelectrice Activation = 1` (line379), `Piezoelectric polarization model: strain` (line416), `With default parameters from file`, 이어 `Clean_pGaN` region override `With incomplete ionization` (line425 onward). 또한 이전 grep line803 `ThermionicEmission: Formula = 1, instead of: 0 [1]`. **Formula1 인식/이종계면 thermionic 켜짐 확정.**
- `Without Piezo`는 ThermionicEmission 하위 옵션 문맥에 있고, `Without polarization`는 strain piezo 모델 자체 상태와 구별해야 하는 별도 물리 설정 출력으로 보임. **근거만으로 실제 interface polarization charge 분포가 올바르거나 전역 piezo가 OFF라는 결론 불가**. No Piezo file도 model OFF 증거가 아님. 파라미터/분극 값을 수정하지 말 것.
- 계산 성공한 5V_TEST의 low J (~7.24e-4 A/cm2 nominal) 물리 원인 remains UNRESOLVED. Alias Plot deprecation warnings nonfatal. Next rather than repetitive grep/screenshots, use existing band, quasi-Fermi & density observations to prioritize a targeted quantitative injection/transport audit (exact layer boundary/QF drops and effective polarization charge); new experiment only after validated causal hypothesis and user approval.
- No server/TCAD code/CAL job changes.

## 2026-10-10 ~21:51 KST — JuSubin Clean_EBL Ev versus EFp measured at same point (OBSERVED screen, derived difference; barrier cause UNRESOLVED)

- Worker 주수빈. Completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` NtSide=0 nominal 5V, SVisual Probe coordinates X=0.13um, Y=1.0um, Z=0, Zone `Clean_EBL(AlGaN)`. New screenshot directly shows `ValenceBandEnergy=-5.252508407140e+00 eV`. Previous directly observed at identical coordinates `hQuasiFermiEnergy=-4.999999939039e+00 eV` and `hQuasiFermiPotential=+4.999999939039 V`.
- DERIVED local separation `EFp-Ev = +0.252508468101 eV` (about 9.77 kBT at 300 K), compatible with locally suppressed mobile hole density under nondegenerate `p ~ Nv exp((Ev-EFp)/kBT)`. Prior same-point hDensity=5.787900714824e15 cm^-3 while EBL Acceptor=3.0e17, Doping=-3.0e17, Donor=0.
- CRITICAL: 0.2525 eV is **local Ev-to-EFp energy separation, NOT EBL hole-injection barrier height**, and by itself does not establish excessive barrier, net hole-current limitation or explain low device J. Need compare spatial Ev and EFp plus region boundaries, transport/current density and possibly EQ state before cause conclusion. pGaN MgMinus output interpretation remains separate unresolved concern.
- NEXT READ-ONLY: use SVisual Probe on same finished TDR at verified `Clean_pGaN(GaN)` X=0.05um Y=1.0um for numerical `ValenceBandEnergy` and `hQuasiFermiEnergy`; then compare regional gaps, and align Ev/QF spatial profiles. No SWB input, TCAD run, or CAL changes.

## 2026-10-10 ~21:48 KST — JuSubin Clean_EBL hole quasi-Fermi energy point probe (OBSERVED SVisual screenshot)

- Worker 주수빈: finished `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` (NtSide=0 nominal 5V), SVisual Probe at (X=0.13 um, Y=1.0 um, Z=0) in verified `Clean_EBL(AlGaN)`: `hQuasiFermiEnergy=-4.999999939039e+00 eV` and `hQuasiFermiPotential=+4.999999939039e+00 V` shown in Probe Var Values. These are opposite-sign representations; do not equate the absolute EFp value to hole barrier height.
- Previous identical point: `AcceptorConcentration=3.000000e17 cm^-3`, `DonorConcentration=0`, `DopingConcentration=-3.000000e17 cm^-3`, `hDensity=5.787900714824e15 cm^-3`.
- NEXT read-only: in same Probe coordinate and Clean_EBL Zone, scroll Var Values to `ValenceBandEnergy` and capture numerical eV value; then calculate `hQuasiFermiEnergy-ValenceBandEnergy` only as local energetic separation (not entire interfacial injection barrier). To evaluate EBL injection obstacle compare Ev and EFp across pGaN/EBL/MQW coordinates/cutline after alignment. No code, parameter, saved solver output, or CAL job changed.

## 2026-10-10 ~21:43 KST — JuSubin QF 1D upper stack plot observed
- OBSERVED 5V NtSide0 SVisual existing center C1 cutline hQuasiFermiEnergy plotted on X=0–0.4um. Around X=0.15–0.25um several large rising steps; Ev had sharp drops/peaks nearby in earlier screenshot. Energy-step origins and EBL barrier not yet established; next compare numerical Ev and EFp at same physical point/region before causal claims. No code or jobs changed.

## 2026-10-10 ~21:37 KST — Upper 0–0.4um ValenceBandEnergy cutline zoom observed (OBSERVED SVisual screenshot / CAUSAL INFERENCE UNRESOLVED)

- Worker **주수빈** displayed `ValenceBandEnergy(C1(n2_des))` in completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` (NtSide0 5V) using same vertical interior C1 line at Y≈1.0 um. **Right 1D plot X axis now 0–0.4 um** (confirmed visually), with resolved sharp energy structure in upper pGaN/EBL/MQW layers.
- Approximate visual band-edge features (not point-extracted): X=0–0.11um ~-5.1eV; pronounced downward feature around X≈0.12–0.15um to roughly -5.6eV; repeated abrupt peaks and dips around X≈0.17–0.26um; beyond ~0.28um ~-3.5eV plateau. Exact interfacial region mapping, magnitude of hole barrier, and peak origins are NOT verified by a color/curve screenshot; these are hypotheses for carrier barrier and band offsets, not validation of EBL injection-loss mechanism.
- Previous same SVisual Probe: `Clean_EBL(AlGaN)` X=0.13um Y=1um, Acceptor=3e17, Donor=0, Doping=-3e17, `hDensity=5.787900714824e15 cm^-3`; cannot attribute low biased mobile holes solely to an EBL barrier yet.
- NEXT read-only UI: retain reference Ev screenshot; click existing C1 dataset on right 1D Data Selection and select `hQuasiFermiEnergy` from lower field list; check legend changes and that 0–0.4um horizontal axis remains or reapply bound. Compare Ev vs hole quasi-Fermi for band-edge proximity and carrier transport. If both can be overlaid later, do so after verifying each alone. No TCAD source, model or running CAL change.

## 2026-10-10 ~21:29 KST — JuSubin 5V Clean_EBL net doping and donor Probe confirmed (OBSERVED, PHYSICS CAUSE UNRESOLVED)

- Worker 주수빈 provided SVisual Probe screenshot of saved, completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, NtSide=0, 5V endpoint. Coordinates `X=0.13 um,Y=1.0 um,Z=0`; Zone `Clean_EBL(AlGaN)`.
- **New directly observed:** `DonorConcentration = 0.000000000000e+00 cm^-3`; `DopingConcentration = -3.000000000000e+17 cm^-3`. Prior screenshots **same point**: `AcceptorConcentration=3.000000000000e17 cm^-3`, `hDensity=5.787900714824e15 cm^-3`.
- EBL effective acceptor input and signed net doping agree with nominal acceptor=3e17 / donor=0. The local 5V mobile hole density is ~51.8x lower than effective acceptor doping, so this is NOT evidence that SDE EBL dopant is missing/misassigned. It may reflect a space-charge/polarization/heterojunction/bias effect; **no single mechanism or bad EBL design is proven from one local point**. Kou literature nominal hole concentration is not interchangeable with 5V local electron/hole density.
- Next **read-only** on same existing TDR: vertical cutline across pGaN/EBL/MQW (Y=1.0 um), inspect `ValenceBandEnergy` and `hQuasiFermiEnergy` plus local hole density to investigate effective hole-injection barrier. Start by checking availability of `ValenceBandEnergy` in Data Selection; no new solver jobs nor model changes. Existing MgMinus custom mapping versus effective net doping is a SEPARATE unresolved item.

## 2026-10-10 ~21:26 KST — 5V Clean_EBL AcceptorConcentration matches nominal 3e17 (OBSERVED)
- 주수빈: SVisual completed 5V NtSide0 Clean_EBL(AlGaN), X=0.13,Y=1.0 um, `AcceptorConcentration=3.000000000000e17 cm^-3`; previously same point `hDensity=5.787900714824e15 cm^-3`, around 52x lower. Confirms modeled EBL acceptor input is present, NOT literature free-hole density match at bias. EBL transport/0V calibration not yet resolved. Next DopingConcentration+Donor probe same point. No simulation/source changes.

## 2026-10-10 ~21:22 KST — JuSubin 5V Clean_EBL hole-density observation
- OBSERVED by 주수빈 at X=0.13 µm Y=1 µm on completed 5V NtSide0 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`: `Zone=Clean_EBL(AlGaN)`, `hDensity=5.787900714824e15 cm^-3`, ~52x below nominal literature EBL hole concentration 3e17 at this particular biased location. No judgment that input dopant is wrong: carrier concentration under 5V need not equal nominal acceptor or equilibrium concentration. NEXT same point `AcceptorConcentration` and signed net doping check. No model edits.

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

## 2026-10-10 ~21:05 KST — Node2 runtime GaN Mg ionization species parameters observed (OBSERVED SCREENSHOT / CALIBRATION UNRESOLVED)

- Worker: 주수빈. Actual read-only `sed -n '810,850p' JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` screenshot shows `Reading parameters for material "GaN"`, `Species "pMagnesiumActiveConcentration"` `type = acceptor`, runtime values `E_0=0.2eV`, `alpha=8e-9 eV*cm`, `beta=0`, `gamma=1`, `g=4`, `Xsec=1e-14 cm^2`, `Xsec_formula=1`, `highdop_formula=1`, `b_Nref=6e18 cm^-3`, `b_pow=2`, `E_Nref=2e18 cm^-3`, `E_pow=2`. This is stronger than just pp2 file reference: SDevice reports the *effective runtime-read* parameters.
- One-point 5V Clean_pGaN Probe X=0.05um Y=1.0um: `hDensity≈3.00034e17`, `DopingConcentration≈-3.00032e17`, `Acceptor=pMagnesiumActive=pMagnesiumMinus=9.59e18 cm^-3`. With `IncompleteIonization` ON and runtime `Nnet` recalculation confirmed, the equality of active and exported minus field to 9.59e18 remains a field-definition/ionization-output validation question, not proof of full ionization or successful physical calibration.
- Sentaurus training about AlGaN incomplete ionization provides doping species `datexcodes.txt` mapping of `ionized = MagnesiumMinusConcentration`; **the current custom pMagnesium mapping must be checked on the actual installed runtime before asserting exact semantics**. Next READ ONLY: inspect `datexcodes.txt` selected by project/system and check whether `AccepMinusConcentration` was requested/exported, then make same-point verification. No code or running CAL job modified.

## 2026-10-10 ~21:02 KST — JuSubin effective Mg ionization region scopes verified
- Screenshot of `JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd` confirms `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")` in Clean_pGaN and DmgL_pGaN. DmgL_pGaN trap block has `Conc=0`; output Plot requests MgActive and MgMinus and doping/polarization variables. This is verified model configuration, not complete physical validation of 5V p-GaN doping. Next review actual species output interpretation and `AccepMinusConcentration`; preserve existing simulation state.

## 2026-10-10 ~20:59 KST — n2 effective parameter file binding confirmed from pp2_des.cmd (OBSERVED TERMINAL SCREENSHOT)

- 작업자: 주수빈. Actual read-only grep of `JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd` showed line 22 `Parameters = "FASTC1_pp6_des.par"`, line 68 `DefaultParametersFromFile`, lines 128-129 and 137-138 `IncompleteIonization( Dopants="pMagnesiumActiveConcentration" )`, and Plot lines 456/458 `pMagnesiumActiveConcentration` and `pMagnesiumMinusConcentration`.
- The previously inspected named `FASTC1_pp6_des.par` in the same working directory has a GaN Ionization Species pMagnesiumActiveConcentration block with `E_0=0.2`, `alpha=8e-9`, `g=4.0`, `Xsec=1e-14`. The effective Node2 SDevice input explicitly REFERENCES this file despite pp6 in the filename; runtime n2 log confirms Mg incomplete ionization is enabled and net doping is recalculated. File reference established; precise resolved parameter semantics/ionized-species output remain to be validated.
- Previously Clean_pGaN 5V Probe at X=0.05/Y=1um yielded hDensity≈3.00034e17, DopingConcentration≈-3.00032e17, Acceptor=MgActive=MgMinus=9.59e18, Donor=0 cm^-3. These values are not proof of correctly calibrated ionization physics; exported MgMinus and recalculated net-doping relation remains unresolved.
- NEXT read-only: inspect `sed -n '115,145p;450,465p' .../JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd` for region-specific Mg ionization scope and Plot fields, then if needed cross-check T-2022.03 species mapping/ionized acceptor fields. Do not change current TCAD decks nor running separate CAL simulation.

## 2026-10-10 ~20:49 KST — Mg ionization parameters found in FASTC1_pp6_des.par (OBSERVED)

- 주수빈 provided live terminal screenshot of `grep -n -A 18 -B 3 'Ionization' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/FASTC1_pp6_des.par`.
- **Actual file contents observed** at lines 24–40: `Material = "GaN" { Ionization { Species ("pMagnesiumActiveConcentration") { E_0 = 0.2; alpha = 8e-9; g = 4.0; Xsec = 1.0e-14; } } }`. E_0 in eV; Xsec in cm2; alpha is the dopant-density dependence parameter. These are actual values in the named .par, not independent confirmation of which effective parameter file n2 used.
- Prior live `n2_des.log` directly confirmed `With incomplete ionization`, selected pMagnesium, and `Nnet will be recalculated`; prior same-position SVisual Probe (Clean_pGaN X=0.05um,Y=1.0um at 5V) gives `hDensity≈3.00034e17`, `DopingConcentration≈-3.00032e17`, `MgActive=MgMinus=Acceptor≈9.59e18 cm^-3`. Physical reconciliation of exported MgMinus with Nnet remains unresolved; single-point hole match is NOT a full doping model validation.
- **NEXT READ ONLY**: determine which parameter file actual n2 run used from `pp2_des.cmd` File/Parameter block and/or `n2_des.job`/`n2_des.log`; do not presume `FASTC1_pp6_des.par` was consumed merely because it is in the directory. Inspect output species mapping only after verifying source. No SWB source changed or CAL interrupted.

## 2026-10-10 ~20:40 KST — 5V_TEST region scope and Nnet recalculation log context (OBSERVED)

- 주수빈 terminal screenshot of read-only `sed -n '410,445p;2138,2160p' JUSUBIN_FAST_HALF_5V_TEST/n2_des.log` confirms region **DmgL_pGaN** `With incomplete ionization` selected `pMagnesiumActiveConcentration`; subsequent **DmgL_EBL** lists no incomplete-ionization. Previously inspected live pp2 Physics confirms `Clean_pGaN` also has region-specific incomplete ionization.
- Log explicitly identifies three recognized species used in acceptor/donor concentrations: `NDopantActiveConcentration (donor)`, `PDopantActiveConcentration (acceptor)`, `pMagnesiumActiveConcentration (acceptor)`. `DopingConcentration` and `TotalConcentration` are recomputed, and `WARNING: Doping concentration (Nnet) will be recalculated because of incomplete ionization!` is printed. Thus this warning is not itself a fatal error.
- The `With Bulk Traps` declaration lists acceptor trap Ev+0.75eV and electron/hole cross-sections 1e-15cm2; it **does not prove trap concentration >0**. Earlier preprocessed NtSide=0 deck independently verified all 12 sidewall traps `Conc=0`.
- IMPORTANT UNRESOLVED: Clean_pGaN 5V Probe X=0.05,Y=1um: hDensity≈3.00034e17 and signed Doping≈−3.00032e17 vs MgActive=MgMinus=Acceptor≈9.59e18. Region activation and Nnet recalculation are observed but not an independent proof of correctly calibrated ionization fraction or semantics of exported MgMinus. Sentaurus device guide uses `AccepMinusConcentration` to visualize ionized acceptor density; verify whether output is available and investigate custom `datexcodes.txt` mapping/Plot before interpretation. No new TCAD run or code edit.
- NEXT READ-ONLY: inspect effective GaN Ionization Species block in existing `FASTC1_pp6_des.par` and relevant `pp2_des.cmd` Plot fields, then reconcile field semantics; do not alter running CAL or finished baseline.

## 2026-10-10 — JuSubin Mg ionization runtime verification
- OBSERVED log for completed 5V NtSide0: region With incomplete ionization, selected pMagnesiumActiveConcentration (lines 422-432), Nnet recalculation warning (line 2148). General Without incomplete ionization line 335 does not cancel region-specific activation. Physical output relation MgMinus 9.59e18 versus net doping -3e17 remains to verify. No code edits.

## 2026-10-10 — JuSubin AcceptorConcentration probe confirms 9.59e18
- Observed SVisual at 5V NtSide0, Clean_pGaN X=0.05um Y=1.0um: AcceptorConcentration=9.59e18 cm^-3, same as pMagnesiumActive/Minus from previous Probe. Net Doping approx -3.00032e17, hDensity approx 3.00034e17, Donor=0. Physical Mg ionization mapping remains unverified despite local hole target agreement. Next check live n2 log, pp2 deck and GaN ionization parameters read-only. No solver changes.

## 2026-10-10 ~20:31 KST — JuSubin Clean_pGaN net doping and free holes agree at one point (OBSERVED)

- SVisual Probe of 5V NtSide0 `JUSUBIN_FAST_HALF_5V_TEST`, Zone Clean_pGaN at X=0.05, Y=1.0 um: DonorConcentration=0, DopingConcentration≈-3.0003179e17, hDensity (earlier same coordinate)≈+3.0003428e17 cm^-3. Earlier `pMagnesiumActiveConcentration=pMagnesiumMinusConcentration=9.59e18` remains not yet reconciled with signed net doping.
- This is good local numerical correspondence with nominal 3e17 free hole target, not full Mg incomplete-ionization calibration or full device validation. Next same-point AcceptorConcentration and effective species mapping; keep running CAL intact.

## 2026-10-10 — Claude v2 independent CMP audit submitted; low-current Gate 0 prioritized (DOCUMENT-BASED REVIEW / PROPOSED)

- 작업자 이택규가 Claude 작성 `CMP MicroLED TCAD — 독립 중간 기술감사 및 연구계획 재수립 (v2)` 전문을 채팅 업로드함. **Claude의 독립 감사 의견이며 이번 메시지는 새 실험/로그가 아님.** Claude는 GitHub 기록과 구 FAST 입력은 보았으나 5V_TEST/CAL 현재 실제 pp/log/TDR을 직접 읽지 못했다고 보고함.
- Claude의 핵심 의견: JUSUBIN_FAST_HALF_5V_TEST NtSide0 5V transient 성공(~10596.76s)에도 raw I2D=1.44801646e-11 A/um, half mesa width≈2um, assumed AreaFactor1이면 nominal J≈7.24e-4 A/cm²; QW Rrad share≈0.1095%. 충분한 구동 전류·주입·IQE 검증이 **Baseline freeze 이전 Gate 0**이 되어야 함. 수치는 기존 GitHub 감사 기반이며 새 측정 아님. `not turned on` 결론은 비교대상 J–V/전류 정규화 검증 전에는 물리 가설로 남김.
- 수용 가능한 점: 5V_TEST 계산 플랫폼 보존, high-bias FAST_C1 n6 ~4.801V step-size failure는 재실행 보류, CAL n2 100ns sensitivity current reported ~4.144V accepted unverified로 관찰·중단 사용자 승인 필수; A/B 동일 J·null controls, τ sensitivity, QW와 Cedge 총 비방사, transient trap DC check, stripe vs 3D 형상 한계 분리.
- 별도 검증 필수: Claude가 제시한 활성층 외 `2.9V drop`은 단일 QW n,p, ni 가정 기반 추정이지 밴드/준페르미 지도에서 측정된 전압 분배 아님. 분극 activation/thermionic/EBL를 저전류 확정 원인으로 판단 금지. FAST half/full ~1% 동일은 4.798 vs 4.801V 단일 단자전류의 근사 보정이므로 메쉬 수렴·공간발광 정확도는 미증명. 2D stripe perimeter/area가 4um square보다 2배 작은 기하학적 사실에서 실제 SRH 2배 과소평가를 단정할 수 없음. 1D pilot 분 단위/10월23일 초록 데드라인/수치 PASS 기준은 Claude의 제안이며 별도 확인 필요.
- 우선순위 제안: **S0 원본 5V_TEST 결과의 구동 전류/J 및 potential/band/quasi-Fermi 분포 점검(기존 TDR)** → **S1 EBL doping/polarization/thermionic interpretation 및 재결합 영역별 전류 회계** → 원인 가설이 분리되면 기존 소자 보존한 별도 소형 1D/pilot 설정 검토(사용자 승인 전 미실행) → NtSide0/1e18 동일 J → A/B. CAL은 보고서의 임의 시간·전압 임계치만으로 중단 결정하지 않음.
- 서버/SWB/코드/CAL 변화 없음. Claude에게 직접 메시지 보내지 않음.

## 2026-10-10 20:21 KST — JuSubin pGaN Mg fields inconsistent with naive hole interpretation (OBSERVED / UNRESOLVED)

- In 5V NtSide0 `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, SVisual Probe Zone Clean_pGaN, (X=0.05,Y=1.0 um), `pMagnesiumActiveConcentration=9.59e18`, `pMagnesiumMinusConcentration=9.59e18`, while earlier `hDensity=3.000342790006e17 cm^-3`. The local hole target numerically matches Kou, but **ionization physics is NOT thereby validated**.
- Minus is an ionized-acceptor related field in Sentaurus dopant mapping. Equal exported Mg fields require review of actual T-2022.03 `datexcodes` mapping, IncompleteIonization and effective values. Next: same-coordinate net-doping, donor/acceptor/electron probes and read-only live model check. No TCAD source/run changed.

## 2026-10-10 — JuSubin Clean_pGaN single-point hole density probe
- OBSERVED 5V NtSide0 SVisual Probe, project `JUSUBIN_FAST_HALF_5V_TEST`, X=0.05 um Y=1 um, Zone Clean_pGaN(GaN): `hDensity=3.000342790006e17 cm^-3`. This agrees with nominal target at one point only. Mg input, ionization field, 0V state and spatial profile remain to validate. Next read MgActive/MgMinus at same point. No simulator changes.

## 2026-10-10 ~19:46 KST — JuSubin p-GaN/EBL/MQW net-doping cutline X=0–0.4 μm zoom observed (OBSERVED SCREENSHOT / APPROXIMATE READOUT)

- 작업자 주수빈; source: successful 5V `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr` NtSide0 `DopingConcentration` on interior half-device Cutline C1, lateral Y≈1 μm. SVisual Axis Properties 1D X-axis Min=0 Max=0.4 μm with signed linear concentration Y-axis now working.
- Visual approximate X ranges: `0–~0.10 μm` plateau around `−3e17 cm^-3` (upper p-side); `~0.10–0.12 μm` signed net doping rises toward zero; `~0.12–0.26 μm` appears near zero on linear Y-axis; around `~0.27 μm` abrupt transition to about `+5e18 cm^-3` n-GaN plateau. These are graph visual estimates only, not numeric point extraction, and exact region boundaries await Regions/Probe identification.
- Important interpretive boundary: plotted signed `DopingConcentration` is not raw Mg dose, ionized Mg or free `hDensity`. Apparent upper transition cannot be asserted as physical Mg backdiffusion or graded SDE profile without inspecting raw dopant species, model and materials. Small EBL/background 1e15–3e17 may be compressed on +6e18 linear graph.
- NEXT read-only GUI: in SVisual Data Selection with cutline C1 selected, inspect `hDensity` (positive, log Y scale may be appropriate only after Y fixed bounds reset), compare carrier-density shape in pGaN/EBL and to intended 3e17 cm^-3 reference; if available plot `pMagnesiumActiveConcentration` and `pMagnesiumMinusConcentration` separately to explain net doping. Do not edit SDE/SDevice or interrupt ongoing independent CAL simulation.

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

## 2026-10-10 ~18:33 KST — 주수빈 5V Baseline signed DopingConcentration vertical cutline linear-axis verified (OBSERVED UI)

- 주수빈 provided Sentaurus Visual screenshot of completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des.tdr`, NtSide=0, after toggling Cutline_Y Plot from logarithmic to linear Y-axis. Existing vertical (growth-axis X) cutline at lateral Y≈1.0 μm passes clean semiconductor away from physical damaged sidewall.
- Direct plotted `DopingConcentration` shows roughly −3×10^17 cm^-3 upper p-side, multiple narrow variations around EBL/MQW, and roughly +5×10^18 cm^-3 constant plateau in n-GaN. The graph shows a step-like nominal signed net-doping distribution along this cutline. Numerical transition boundary and dopant activation details are NOT precisely extracted at this zoom.
- This is not a direct measurement of raw Mg input 9.59×10^18 cm^-3, `hDensity`, ionized Mg fraction, Mg diffusion, or actual physical SIMS depth profile. The loaded 5V output remains a Transient endpoint, not independently proven equilibrium or steady-state.
- Next read-only GUI validation: zoom cutline X≈0–0.4 μm to distinguish p-GaN/EBL/MQW region steps, then show `hDensity` and optionally `pMagnesiumActiveConcentration` and `pMagnesiumMinusConcentration` where available. Preserve original saved results and ongoing separate CAL n2 job; no source changes.

## 2026-10-10 — Kou 2019 nominal epitaxy doping vs CMP step-constant profiles reviewed (REVIEWED / NO SOLVER CHANGE)

- 작업자: 주수빈. 사용자가 layer별 동일 도핑을 구현한 실제 CMP 모델의 문헌 타당성을 재질문. 실제 Kou et al., *Optics Express* 27 A643-A653 (2019) Section 2, DOI 10.1364/OE.27.00A643 확인.
- **Direct paper:** n-GaN 4 μm Si doped 5e18 cm^-3; p-Al0.15Ga0.85N EBL 26nm and p-GaN cap 120nm each **hole concentration** 3e17 cm^-3 (Mg dopant concentration이라고 보고하지 않음); 20nm heavily doped p-GaN ohmic contact layer **also specified**. Paper does not specify SIMS-calibrated vertical concentration profile or graded Mg transition function. Therefore uniform-per-layer SDE doping is a defensible simplifying *interpretation*, NOT proved literal reproduction of growth profiles or proof authors applied exact constant doping commands.
- **Existing CMP actual 2026-10-09 pp1 audit:** N_Mg_p=9.59e18 cm^-3 nominal Mg input in Clean/DmgL pGaN with incomplete-ionization SDevice physics; nominal p-GaN 3e17 target is hole density, not identical to Mg input. A single SVisual sample hDensity~3.001e17 was reported at one 5V result point and cannot establish unbiased whole-depth calibration. EBL nominal effective acceptor 3e17, n-GaN donors 5e18, barrier 1e15 (numerical assumption). Region-based constant input does not imply constant mobile electron/hole density under bias.
- **Paper/model gap:** a separate 20nm highly doped p-GaN contact cap occurs in Kou; CMP COMMON_BASELINE vertical stack does not list that separate p+ region, though exact live SDE current geometry/contact doping must be checked before treating it as confirmed omission.
- **Experimental context:** Gutt et al. PSS C (2011), DOI 10.1002/pssc.201001039 and Bakhtiary-Noodeh et al., Journal of Crystal Growth 602 (2023) 126962 DOI 10.1016/j.jcrysgro.2022.126962 support real Mg memory/back-diffusion/graded near-boundary profiles; no direct SIMS profile for the CMP representative device has been supplied. Avoid inventing gradient depth/concentrations.
- **Decision PROPOSED, NOT RUN:** retain current original and CAL running job unchanged; perform read-only vertical SVisual cutline of nominal Mg species, ionized Mg/net doping, hDensity and EBL; verify p+ contact layer/source. If experiment needed, create separately versioned sensitivity branch with literature/SIMS-backed graded Mg interface and same mesh/physics, compare QW hole injection, I(V), SRH/Rrad/current at matched injection. No code, parameter, or SWB job modified.

## 2026-10-10 ~18:07 KST — 주수빈 CAL 진행 상태 스크린샷 확인 (OBSERVED)

- 주수빈이 이택규의 기존 `CMP_BASELINE_1.2.0_CAL` NtSide0 실행 상황을 SWB Node n2 Output 창으로 공유. 직전 accepted step 뒤 displayed anode=4.138 V, next BE attempt pseudo-time 0.82766 -> 0.827663 s. 이전 기록 4.122 V보다 약 0.016 V 진전. 5 V 기준 약 82.76% 전압 스윕이며 wallclock 진행률 아님.
- 다음 단계 수렴/5 V 완료/100 ns override effective 여부는 화면에서 확정 불가. `n2_des.err` E0 warning은 fatal 원인으로 확정하지 않음. 서버 소스/작업은 변경하지 않음.
- NEXT: 현재 실행 유지, 후속 로그 read-only 확인과 5 V 성공 후 이전 1 ns Baseline 대조.

## 2026-10-10 12:09 KST — CAL SDevice continues running in SWB (USER-REPORTED / LOG UNVERIFIED)

- Worker 이택규 reports that the previously launched `CMP_BASELINE_1.2.0_CAL` SDevice still appears **running** in SWB at ~12:09 KST on Oct 10, with no completion observed.
- Start time described as "어제 새벽 1~2시" (literally Oct 9 01:00–02:00), which would imply 34h09m–35h09m elapsed, but the same CAL project's SDE meshing was previously screenshot-confirmed completed **Oct 10 00:11:50 KST**. A **different interpretation of the date** (Oct 10 01:00–02:00) implies 10h09m–11h09m; therefore actual start date/time is **UNRESOLVED**, and must not be treated as known.
- **SWB running display is user-reported only**; there is no freshly supplied CAL `n2_des.log` or `n2_des.out`, no observed accepted BE steps/current voltage, no proof the 100ns material override was applied, and no reliable ETA. Do not call this a hang or success.
- Next **READ ONLY**: inspect `tail -n 40 /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/n2_des.log` and the SWB job/experiment identity and start timestamp; compare changing accepted-voltage/current and Newton retry patterns. Keep existing run and original completed 5V parent intact; no parameter/source edits while it is running.

## 2026-10-10 — Joint researcher naming convention applies to future JuSubin work (DECISION)

- Worker 이택규 requests all **future new CMP** projects created by either researcher (이택규 or 주수빈) follow `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>` (e.g. BASELINE/PROJECTA/PROJECTB). Current naming guide and AGENTS.md updated so any AI/Claude session reading the repo can follow it.
- Scope is new projects/user-authored releases; preserve Sentaurus native tool-input/output file names and preexisting archives/projects to avoid breaking SWB links. No claim that 주수빈 has acknowledged or already renamed projects. No solver edits/runs in this policy update.

## 2026-10-10 — 이택규 CAL input candidate created off-server, no simulator run (PROPOSED / STATIC CHECKED)

- User provided installed T-2022.03 InGaN.par SRH/Auger/Radiative section proving vendor's GaAs-derived 1ns lifetime warning and default coefficients. Private ChatGPT downloadable `CMP_BASELINE_1.2.0_CAL_INPUT_CANDIDATE.zip` generated from validated 5V_TEST input files: same SDE, same executed SDevice sweep/model (comments corrected only), GaN Mg and crystal orientation intact, InGaN SRH Scharfetter tau_max set to 100ns both carriers in custom .par. This is a *literature sensitivity proposal*, not calibrated or run. New SWB clone pending.

## 2026-10-10 — 이택규 verified actual 5V parent model via uploaded HDF5 archive (OBSERVED/DERIVED)

- Baseline candidate `CMP_BASELINE_1.2.0_CAL` under preparation, not yet created; confidential nine-file input and result archive read privately by GPT. Audit without proprietary contents: `CMP/reviews/BASELINE_1_2_0_CAL_AUDIT_20261010.md`.
- Strong model discovery: every Clean/DmgL 5V QW rate field follows Radiative B=2e-10, Auger C=1e-30, and SRH tau=1ns. Mg incomplete ionization produces reduced net doping through 0.031286 maximum pGaN occupation. 5V current remains low, physical calibration remains open.
- SDevice code comments incorrectly advertise 4V/4.5V/4.8V Saves and staged increment; actual run only had 5V Save and constant Increment=1.2. No code modifications or new solver job.

## 2026-10-09 — CMP naming/version policy confirmed by 이택규 (DECISION)

- Use `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>` for new project candidates; see `CMP/PROJECT_NAMING_CONVENTION.md`. New proposed Baseline candidate: `CMP_BASELINE_1.2.0_CAL`, not yet an existing simulation. PROJECTA/B have independent version histories; preserve parent Baseline provenance and NtSide run metadata.
- Existing 5V_TEST private artifact filenames and sizes confirmed in server shell; no new code or simulation generated. Retain the previous completed 5 V NtSide0 run and pre5V archive.

## 2026-10-08 — 주수빈 Half+coarse SDevice QS 가속 시험 후보

- 작업자: 주수빈; 상태: PROPOSED / CODE STATIC PASS; 런타임 미검증.
- Half+coarse mesh (138,194 elements) 생성/visual gate 통과 후, SDevice Transient 0→0.3V smoke 한 step 약 109.74s 중 solve 약 90.20s를 관찰.
- steady-state I-V/IQE 목적에 더 적합하고 adaptive step 수를 줄일 수 있는 Quasistationary 0→0.3V 별도 시험 deck 작성. 원래 Physics/Trap/Math/ILS 및 initial Poisson/Coupled 유지, QS ramp 설정만 신규.
- 원본 full FAST_C1/Project A/B 기준 모델은 변경하지 않음. 짧은 smoke와 full-reference 동등성 시험 전 production 채택 금지.

## 2026-10-08 — Fast pilot direction: half-domain + relaxed remote bulk mesh

- 작업자: 이택규; 상태: PROPOSED / NOT IMPLEMENTED.
- Time-constrained request: run a **separate experimental branch** applying both half-domain symmetry and modest remote bulk/numerical n-GaN coarsening to investigate runtime, without stopping existing FAST_C1 or changing frozen physical baseline parameters.
- Must verify exact active SDE contacts/doping/geometry symmetry and retained-side 5nm physical damage; preserve MQW, EBL, heterointerfaces and damage/edge refinement; avoid changing tolerance/traps/polarization simultaneously.
- One combined pilot provides feasibility data, not independent attribution of speedup. Requires SDE mesh review + actual preprocessed region/physics scope review + short solver smoke before longer run.
- Exact active SDE/SDevice code is not publicly synced, so implementation pending obtaining originals. No simulation result yet.

## 2026-10-08 — First Node 6 QW local Probe observations (not emission validation complete)

- 이택규 SVisual screenshots from `n6_inter_0004_des`: `Clean_QW1`–`Clean_QW4` are confirmed InGaN zones. Selected field is horizontally clipped (`...bination`); tentatively `RadiativeRecombination`, pending fully visible name confirmation.
- Local values [cm^-3 s^-1 if radiative]: QW1 5.531972320698e12, QW2 9.346620224854e14, QW3 4.188264170176e13, QW4 6.069760269935e14.
- Positive point values cannot prove total QW emission, normal LED operating current or IQE. Continue active-material radiative parameter + actual QW volume/area integration + e/h and terminal-current checks before accepting normal LED baseline.

## 2026-10-08 — Half-domain / injection sanity review (not an approved baseline change)

- 작업자: 이택규 / Claude proposal reviewed by ChatGPT; 상태: REVIEWED / PROPOSED.
- Baseline Node6 at 4.7128 V has I=2.8954e-12 A/um; under nominal 4 um lateral area, J≈7.24e-5 A/cm2. Arithmetic matches SDevice T-2022.03 2D-current convention, but low injection and high-bias IV require physical sanity check; no assertion of LED failure until terminal current composition, live input/contacts and existing TDR band/current/recombination are verified.
- Half-domain has conditional symmetry rationale and may reduce degrees of freedom, but is NOT yet implemented or validated; current full/fine FAST_C1 remains reference. Do not co-change mesh and domain without isolating effects.
- RhsMin L2 sqrt(2) argument is a model-dependent hypothesis; changing convergence threshold needs separate validation, not automatic adoption.
- Existing A/B GO/NO-GO gates remain. Reference: LIVE LOG Issue #7 review dated 2026-10-08.

## 2026-10-07 — Project A/B production pre-run GO/NO-GO audit

- 작업자: 주수빈
- 상태: REVIEWED / TEAM GATE
- FAST_C1/Common Baseline은 Project A/B의 parent로 사용 가능하며 physical baseline을 다시 만드는 것은 불필요.
- 하지만 multi-day A/B production sweep은 즉시 시작하지 않기로 함.
- 시작 전 필수: 실제 active preprocessed deck 확인, 모든 spatial output 및 region-integral extraction 선검증, 2D current-density normalization, A/B parameterized geometry+mesh+null controls, Save/Load smoke, 대표 pilot.
- A는 same-material GaN Cedge 내부 경계에 명시적 mesh refinement가 필요.
- B는 AlBarrier의 exact vertical span을 먼저 확정해야 하며, QW edge를 치환하는 경우 active QW volume 변화가 comparison metric에 반영되어야 함.
- 상세 기준: `CMP/PROJECT_AB_PRE_RUN_AUDIT.md`.

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

## 2026-10-04 — FAST C1 B0 review strengthened acceptance criteria

- **작업자:** 이택규
- **구현/검토:** Claude B0 review + ChatGPT verification
- **상태:** PROPOSED / READY FOR SEPARATE PREPROCESS
- C1 source remains `Iterations=15`; no physics/source change beyond the already-reviewed numerical cap.
- ~4.33 V interpretation corrected: first rejected attempt with changed Newton count, not trajectory divergence.
- A1'/A1'' added: preserve accepted/rejection trajectory over overlap and require C1 rejection message to show 15-cap.
- full CSV cutback-ratio constancy remains pending; observed examples are ~0.5.
- live x6/x7/x8 remain untouched.

## 2026-10-04 — FAST_BASELINE C1 selected as first numerical candidate (PROPOSED)

- **작업자:** 이택규
- **구현:** Claude / **검토:** ChatGPT
- **상태:** PROPOSED / REVIEWED / NOT EXECUTED
- Copy x8 golden 대비 유일한 executable change는 forward Transient inner Coupled `Iterations=15`.
- Common Baseline physics/traps/geometry/step controls는 유지.
- Synopsys 2022 training의 15–20 iteration 권고와 방향은 일치하지만, 프로젝트의 ~50-iteration failure 기록과 documented default 20 사이 불일치가 있어 B0 raw-log audit이 선행되어야 함.
- 최종 FAST 채택 전에는 numerical/physical equivalence + runtime 모두 검증.
- live x6/x7/x8은 보존.

## 2026-09-28 — Final SDevice v1.2 source-sync gap 발견

- **작성자:** ChatGPT
- **참여자:** 이택규 / 주수빈
- **구분:** 공용 동기화 점검
- **상태:** OBSERVED + UNRESOLVED
- **내용:** JuSubin의 Issue #7 및 개인 타임라인에는 Final SDevice v1.2 수정 이력이 기록되어 있으나, 실제 `CMP/tcad/CURRENT/sdevice2_defect_on.cmd`는 오래된 버전으로 남아 있어 최신 실행 코드와 GitHub source-of-truth가 불일치함.
- **주의:** Gmail에 도착한 내용은 Issue #7 알림이므로 연구 진행 로그 반영 여부는 확인할 수 있지만 실제 코드 파일 업로드 여부를 대신하지 않음.
- **다음:** exact Final SDevice 전체 원문을 회수하여 CURRENT에 동기화하고 provenance를 재검증.

---

## 2026-09-22 — CES2027 선발 발표 구성 착수

- **작성자:** ChatGPT
- **참여자:** 주수빈
- **구분:** 팀 발표 준비
- **상태:** PROPOSED
- **내용:** 15분 발표를 Common Baseline의 문헌 근거, baseline 구조 검증, Project A/B의 TCAD 구현/공정 비교 전략 중심으로 구성하기로 함.
- **발표 원칙:** 지난 1주차의 일반 배경은 최소화하고, baseline provenance와 검증 가능성 및 fair comparison design을 핵심으로 제시.
- **계획 파일:** `CMP/CES2027_PRESENTATION_PLAN.md`

---

## 2026-09-21 — CMP 프로젝트 내 의미 있는 작업 자동 저장 범위 재확정

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영 결정
- **상태:** CONFIRMED
- **내용:** 사용자가 CMP 프로젝트 안에서 수행하는 연구 작업은 작업자가 이택규/주수빈 누구든 별도 "저장해" 요청 없이 의미 있는 변경이 생길 때 GitHub에 자동 기록하도록 재확정.
- **포함:** 코드 수정, 오류/해결, simulation 결과, baseline/설계 판단, blocker, 다음 작업, 인수인계.
- **제외:** 단순 잡담, 일반 개념 질문, 연구에 반영하지 않은 사소한 아이디어.
- **경계:** AI가 보지 못하는 다른 비공개 채팅을 실시간으로 직접 읽는다고 가정하지 않으며, 각 채팅의 AI가 GitHub에 기록해야 장기 동기화가 보장됨.

---

## 2026-09-21 — 주수빈 Common Baseline 코드 최종화 / pre-run 검토 진행

- **작성자:** ChatGPT
- **참여자:** 주수빈
- **구분:** 병렬 연구 진행
- **상태:** OBSERVED — 공유 프로젝트의 주수빈 채팅 사용자 보고 기준
- **내용:** 주수빈이 메인 SDevice 및 앞서 검토된 관련 코드를 최종 수정했다고 보고했으며, Project A/B 공통 baseline으로 장기간 사용할 수 있는지 simulation 전에 최종 논리 검토 중.
- **실행 계획:** 계산 비용을 고려해 우선 `NtSide=0`과 `NtSide=1e18` 두 조건만 먼저 실행해 baseline 동작을 확인할 계획.
- **제약:** 한 조건 run이 약 3일 걸릴 수 있다고 보고되어, 전체 sweep 전 정적 코드/논리 검증이 중요함.
- **검증 수준:** 최신 전체 코드와 실행 결과는 이 기록 시점에 GitHub에서 직접 검증되지 않았으므로 성공/정확성을 CONFIRMED로 간주하지 않음.
- **다음:** 수빈 최신 코드 동기화 → 최종 검토 → 두 조건 실행 → 결과 기록.

---

## 2026-09-21 — Sentaurus T-2022.03 공식 매뉴얼/예제 참고자료 색인

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 참고자료 / 연구 인프라
- **내용:** 사용자가 제공한 SDevice/SDE/SMesh/SVisual T-2022.03 User Guide와 Sentaurus example 자료를 검토해 GitHub reference index와 file manifest로 기록.
- **중요 확인:** textured solar-cell 공식 example의 SDevice File block에서 `plot=@tdrdat@`, `grid=@tdr@`, `current=@plot@`, `output=@log@`, `parameter=@parameter@` Workbench macro 패턴 확인.
- **현재 blocker 관련 의미:** SDevice2 command macro를 임의 변경하기보다 `pp9_des.cmd`의 실제 preprocessing 결과를 우선 확인해야 한다는 기존 진단을 강화함.
- **보안/저작권:** Synopsys 원본 User Guide에는 proprietary notice가 있어 public GGYU에는 원문 PDF/전체 예제 코드를 업로드하지 않고 색인·요약·hash만 저장.
- **상태:** CONFIRMED

---

## 2026-09-21 — Claude용 GitHub 연동 작업 프롬프트 추가

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영
- **내용:** Claude가 GitHub의 현재 연구 상태를 우선 읽고, 실제 코드/로그를 기준으로 이어서 코드를 작성·디버깅하며, 의미 있는 결과를 다시 GitHub에 기록하도록 전용 시작 프롬프트를 추가.
- **파일:** `CMP/prompts/CLAUDE_GITHUB_WORK_PROMPT.md`
- **상태:** CONFIRMED

---

## 2026-09-21 — AI Shared Memory Protocol v2 구축

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영 결정
- **내용:** 이택규 GPT / 주수빈 GPT / Claude가 작업 시작 시 서로의 최신 GitHub 기록을 읽고, 의미 있는 작업 결과를 자동으로 GitHub에 쓰도록 최상위 공용 프로토콜을 구축함.
- **핵심:** READ-first → 작업 → 의미 있는 결과 WRITE → Issue #7 append → 필요 시 RELAY 인수인계.
- **추가:** 동시 수정 충돌 방지, 기록 실패 시 성공 주장 금지, 상태 라벨 표준화, 응답 종료 시 실제 동기화 항목 표시.
- **상태:** CONFIRMED

---

## 2026-09-21 — 새 채팅 시작 브리핑에 마지막 작업 + 대시보드 링크 추가

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영 결정
- **내용:** 새 채팅에서 `이택규` 또는 `주수빈`으로 시작할 때, 첫 답변에 현재 진행 상황뿐 아니라 가장 마지막으로 한 작업과 CMP 대시보드 링크를 항상 포함하도록 규칙 추가.
- **대시보드:** https://taekgyu0801.github.io/GGYU/
- **상태:** CONFIRMED

---

## 2026-09-21 — CMP AI 공통 협업 규칙 확정

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영 결정
- **내용:** 이택규 GPT, 주수빈 GPT, Claude가 같은 CMP 프로젝트에서 따를 세션 시작/자동 기록/코드 수정/충돌 방지/AI 인수인계 규칙을 `AI_COLLAB_RULES.md`로 통합.
- **상태:** CONFIRMED
- **목적:** 서로 다른 노트북과 AI 계정에서 작업해도 GitHub를 기준으로 동일한 연구 상태를 유지.

---

## 2026-09-21 — 주수빈 collaborator 권한 확인 완료

- **작성자:** ChatGPT
- **계정:** `soybeanmilk0514-jpg`
- **저장소:** `TaekGyu0801/GGYU`
- **확인 결과:** `write` 권한
- **상태:** CONFIRMED
- **의미:** 주수빈 계정은 GGYU 저장소를 읽고 수정할 수 있음.
- **다음 작업:** 주수빈 ChatGPT/Claude 계정에서 GitHub를 연결하고 GGYU 읽기/쓰기 테스트 수행.

---

## 2026-09-21 — 주수빈 GitHub collaborator 초대 전송

- **작성자:** ChatGPT
- **사용자 보고:** 이택규가 주수빈 GitHub 계정을 `TaekGyu0801/GGYU` collaborator로 초대함.
- **상태:** OBSERVED (사용자 보고 기준, 수락 여부/최종 권한은 아직 미확인)
- **다음 확인:** 주수빈이 초대를 수락한 뒤 collaborator permission 확인.
- **후속 작업:** 주수빈 ChatGPT/Claude 계정에서 GitHub 연결 후 `GGYU` 읽기/쓰기 테스트.

---

## 2026-09-21 — 주수빈도 CMP 프로젝트 내 이름 확인 방식으로 작업

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영 결정
- **내용:** 주수빈도 CMP 프로젝트 안에서 새 채팅 시작 시 `주수빈`이라고 입력해 작업자를 식별하고, GitHub 최신 상태 브리핑 및 자동 기록 흐름을 사용하기로 함.
- **효과:** 별도 긴 시작 프롬프트를 매번 붙일 필요 없이, 프로젝트 공통 규칙 + GitHub sync를 통해 동일한 연구 상태에서 이어서 작업 가능.
- **조건:** 주수빈 계정에서 GitHub 저장소 읽기/쓰기 권한이 있어야 자동 기록 가능.

---

# CMP 팀 타임라인

이 파일은 이택규 / 주수빈 / ChatGPT / Claude의 **공용 작업 이력 요약**이다.

개인 세부 기록은:
- `members/LeeTaekGyu/TIMELINE.md`
- `members/JuSubin/TIMELINE.md`

를 사용한다.

## 2026-09-21 — 공동 연구 GitHub/AI 협업 구조 구축

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용
- **내용:** GitHub를 ChatGPT ↔ Claude ↔ 연구자 간 Single Source of Truth로 사용하도록 구조 정리.
- **추가된 핵심:** Common Baseline, Current Status, Error Log, Next Actions, AI Handoff, .ai-sync, 연구 대시보드, Phase Issues.
- **현재 연구 상태:** Common Baseline validation 진행 중.
- **현재 난관:** SDevice2 → SVisual2 TDR output/linkage 문제.
- **다음 작업:** pp9_des.cmd의 preprocessed File/Plot output filename 확인.

---

새로운 의미 있는 작업이 생기면 최신 기록을 위쪽에 추가한다.


## 2026-10-09 11:30 KST — JUSUBIN_FAST_HALF_SWB completion reported

- 작업자: 이택규
- 상태: OBSERVED (user report; terminal/log not yet re-verified in this session)
- 이택규가 주수빈이 전날 실행한 `JUSUBIN_FAST_HALF_SWB`가 모두 완료되었다고 보고함.
- 이 보고로 Half+coarse transient branch는 "running"에서 "completion reported" 상태로 이동.
- 단, 최종 bias 도달, fatal/error 부재, 산출물 존재, elapsed time, I-V/IQE 유효성은 아직 로그로 재확인하지 않았으므로 CONFIRMED로 승격하지 않음.
- 다음: project terminal에서 n2_des.log/out/err와 최종 .plt/.tdr 존재를 확인하고, final 0.3 V 도달/normal termination/accepted final step을 검증. 그 후 QS Copy 결과와 runtime·I-V를 비교하고 full FAST_C1 reference 대비 half+coarse validation을 진행.


## 2026-10-09 — Transient pass, QS Copy MinStep stop
- User-provided logs: JuSubin half+coarse original transient completed to anode 0.3V (25019.43 s), I-V file exists.
- Distinct QS Copy ended because `Step-size less than MinStep (8.3986e-07)` after 18417.09 s; result save/normal program exit does not prove sweep completion. Final accepted voltage and failure mechanism pending.
- Team action: diagnose QS plot/log before solver alterations; full/fine reference equivalence pending.


## 2026-10-09 — QS Copy last accepted bias determined
- 작업자: 이택규. OBSERVED from user-provided `JUSUBIN_FAST_HALF_SWB_Copy/n2_des.plt` tail and `n2_des.log` grep.
- Last recorded QS pseudo-time: 6.43487876313307E-02; last anode OuterVoltage: 1.93046362893992E-02 V (0.0193046363 V; 19.3 mV, only ~6.435% of requested 0.3 V).
- Last log attempts at t=0.0643488 to 0.0643505 then terminated `Step-size less than MinStep (step-size = 8.3986e-07)`.
- QS runtime 18417.09 s but did NOT reach goal. Cannot compare as speedup to original transient that reached 0.3 V in 25019.43 s.
- Root numerical/physics trigger not yet established. Next: inspect QS log around lines 6900-7000 and `n2_des.err`; no blind MinStep or baseline modification.


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


## 2026-10-09 — Half 5V test SDevice edit performed in copied SWB project
- 작업자: 이택규. OBSERVED from terminal in `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST`: user ran `cp -p sdevice_des.cmd sdevice_des_0p3V_backup.cmd`, then `sed -i` replacing `FinalTime = 0.06` with `1.0`, `Goal Voltage = 0.3` with `5.0`, and `Save FilePrefix n@node@_smoke_ckpt_0p3V` with `n@node@_5V_ckpt`.
- Follow-up `grep -nE 'FinalTime|Voltage =|FilePrefix =' sdevice_des.cmd` confirmed line 587 FinalTime=1.0, line 597 Goal Voltage=5.0, line 608 new 5V Save prefix; initial electrode Voltage=0.0 appears at lines 38 and 43.
- Code modification is OBSERVED in the user's remote copied project, NOT yet synced as full source to GitHub. Backup command executed but exact backup-byte equality not independently checked. Original `JUSUBIN_FAST_HALF_SWB` and QS Copy were not targeted.
- Numerical intent: preserve the old 5 V per time-unit voltage ramp by adjusting 0.3/0.06 to 5/1; note `Transient` time is physical simulation time and this is not a steady-state QS. Not yet validated for high-bias convergence/current/IQE. The old 0.3V smoke comment in source may remain stale.
- NEXT: in the copied SWB project select SDevice Node 2 and run Ctrl+P preprocessing only; check generated `pp2_des.cmd` for actual FinalTime=1.0, anode Goal Voltage=5.0, Save prefix and expected mesh/physics/NtSide before F7. Do NOT run 5V yet; check that copied project prep is independent from original.


## 2026-10-09 — 5V copied Half/Coarse transient backup and Grid/Trap preflight observed
- 작업자: 이택규; 상태: OBSERVED from user's terminal (archive integrity check pending; 5V run NOT YET observed).
- At `/user/semi/semi437/tmp/myproject`, user executed `tar -czf JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz JUSUBIN_FAST_HALF_5V_TEST`; `ls -lh` confirms archive 12M, timestamp Oct 9 11:25. This is an existing compressed project snapshot made *after* 5V source edits, containing copied old 0.3V outputs; not a verified successful 5V result. Archive contents/integrity have not yet been independently checked with `tar -tzf`.
- In copied project `pp2_des.cmd` grep: Grid=`n1_msh.tdr` line20; 12 displayed region-level `Conc=0` lines145–365; RHSMin=1e-3 line510; startup Coupled Iterations=500 and 100; sweep `Coupled(Iterations=15)` line600. Earlier pp2 verification showed executable Transient, FinalTime=1.0, Goal anode=5.0, Save prefix `n2_5V_ckpt`.
- Original 0.3V smoke and separate QS Copy preserved. Current blocker: archive integrity check and launching SDevice Node2 only in copied SWB; don't launch SDE or modify original. 5V high-bias numerical/physical validity, IQE, I-V, mesh/symmetry equivalence are not established. Allow initial run only as exploratory independent branch, with output/log monitoring and no runtime/accuracy promise.
- NEXT: `tar -tzf ../JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz > /dev/null` and `echo $status` (C-shell-compatible; 0 expected); then copied SWB Node2 SDevice Run F7 only; inspect new n2_des.log/err after startup, verify no immediate failure and logs no longer Oct 9 01:39 copied outputs.


## 2026-10-09 — 5V copied project Node2 not running; old 0.3V log confirmed
- 작업자: 이택규; OBSERVED user terminal from `JUSUBIN_FAST_HALF_5V_TEST`.
- `ps -fu semi437 | grep '[s]device'` showed ONLY two old active sdevice processes: PID 69457 running `pp6_des.cmd` since Oct04, and PID 93915 running `pp12_des.cmd` since Oct06 (both 99% CPU). No `pp2_des.cmd` SDevice process present in this observed process list. A queued SWB job, if any, was not separately checked.
- `n2_des.log` mtime Oct 9 01:39:13 +0900; its tail says the *old original 0.3V smoke* completed with `Good Bye` Oct9 01:39:13, wallclock 25019.43 s and 2.61GB peak memory. This log was inherited by directory copy and is NOT a 5V result.
- Therefore no indication 5V SDevice Node2 has launched; do NOT Clean Up Node merely to start. Existing pre5V archive readable (tar listing status 0), pp2_des.cmd preprocessed 5V parameters confirmed earlier.
- NEXT: if concurrent machine/license resources are acceptable, select **only** SDevice Node2 in the SWB copied `JUSUBIN_FAST_HALF_5V_TEST` and run F7. Avoid SDE re-run. Monitor fresh `n2_des.log` timestamp and View Output; check convergence and actual attained anode voltage. CPU contention from pp6/pp12 may prolong 5V run. Do not mark 5V started/completed before evidence.

## 2026-10-09 — 이택규 Half+Coarse 5V_TEST 5V 달성 (OBSERVED)

- OBSERVED source: user-provided terminal in `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST`, `tail -n 40 n2_des.log` after run. Final anode voltage `5.000E+00 V`, anode electron `2.781E-13`, hole `1.420E-11`, total current `1.448E-11` (terminal output units require current-normalization audit). `Finished, because... Curve trace finished.`, `Sentaurus Device simulation finished`, `Good Bye !` at 2026-10-09 14:29:52 KST.
- OBSERVED files written per log: `n2_5V_ckpt_des.sav`, `n2_5V_ckpt_circuit_des.sav`, `n2_des.tdr`. `wallclock=10596.76 s` (2 h 56 m 36.76 s), total CPU 30641.23 s, peak memory 2.97 GB. `ps` showed only pp6 PID 69457 and pp12 PID 93915; no active pp2 at check.
- Proven: copied **Half+Coarse NtSide=0** Transient Node2 reached 5V and terminated normally. Not proven: publication-grade/common damaged NtSide=1e18 baseline, physical I-V/current-density validity, full-vs-half equivalence, IQE/optical emission, extracted current units, or A/B improvements. Do not treat save filename alone as 5V evidence; here independently supported by final 5V terminal row + normal curve trace.
- Previous 116h extrapolated runtime and 3–7+day planning range are superseded by the **measured 10596.76 s** for this run; reason for fast runtime relative to old 0.3V smoke remains unverified. Do not infer speedup or solver equivalence without source/deck/log comparison.
- NEXT: preserve 5V outputs/checkpoints and current reference pp6/pp12 jobs; inspect `n2_des.plt` for full I-V, ensure actual postprocess unit/AreaFactor/2D symmetry normalization, compare intermediate MQW Rrad/SRH/Auger and carrier/injection with full/fine at matched bias/current; then separate nominal `NtSide=1e18` damage case after controlled preprocess/short-run gate. Project A/B production remains NO-GO pending existing audit.

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

## 2026-10-09 — 5V_TEST four InGaN Clean_QW local RadiativeRecombination Probe measurements (OBSERVED; IQE NOT YET)

- 작업자: 이택규. User supplied four direct Sentaurus Visual Probe screenshots in `JUSUBIN_FAST_HALF_5V_TEST` / `n2_des`, with scalar `RadiativeRecombination`, explicit zone label, x/y coordinates and Magnitude (cm^-3 s^-1, unit grounded in preceding SVisual legend).
- `Clean_QW1(InGaN)`: x=0.169818746552, y=0.560459877538, z=0, `Rrad=1.836010164996e+13`.
- `Clean_QW2(InGaN)`: x=0.194326754006, y=0.556958733616, z=0, `Rrad=3.558921779790e+12`.
- `Clean_QW3(InGaN)`: x=0.22058533342, y=0.56571159342, z=0, `Rrad=8.395713573050e+14`.
- `Clean_QW4(InGaN)`: x=0.245093340874, y=0.58321731303, z=0, `Rrad=7.094266327897e+18`.
- Result: **each of four named InGaN QWs contains a positive local Rrad point**, beyond mere output declaration or plot-wide maximum. The QW4 sampled point exceeds sampled other QW values by several orders of magnitude. HOWEVER: points differ in both vertical and lateral coordinates (x/y), so local values are **NOT** region-integrated emission, per-well averages or a verified QW4 total-emission dominance. Do not treat local peak, photon escape, IQE or material radiative coefficient as validated.
- Remaining: check SRH and Auger at the *same probe coordinates*, map Rrad spatially through each QW and perform mesh/region correct integrals, confirm 2D current normalization, injection/current plausibility and half-vs-full correspondence; NtSide=0 branch only. No new solver or source changes.

## 2026-10-09: 이택규 5V_TEST Clean_QW4 같은 좌표 Probe. x=0.244864017914, y=0.651958341615, z=0, InGaN. Radiative 7.103015017104e18, SRH 1.681575471039e22, Auger 1.238545872618e15, Total 1.682285896396e22 (cm^-3 s^-1). Local radiative fraction about 0.0422%; NOT integrated IQE. Verify physical rates and lifetimes before baseline freeze; no code change.

## 2026-10-09 — Project A fabrication-route feasibility brainstorm (PROPOSED / NOT APPROVED / NOT RUN)

- Worker: 이택규. Request: evaluate how the Stage1 Project A localized upper-nGaN-sidewall GaN:C Cedge could be fabricated. **No process route selected, no implantation/epitaxy performed, no TCAD/SProcess code modified.** Original frozen Common Baseline, Cedge conceptual position inside existing 5nm damaged-sidewall strip under MQW, and NtSide0/1e18 comparison remain unchanged.
- Candidate POST-MESA: completed LED epitaxy → ICP mesa etch exposes nGaN sidewall → protect pGaN/MQW and all non-target surfaces with *selective vertical-height mask/spacer* → angled/rotated C-ion implantation into exposed upper-nGaN sidewall → damage-recovery/thermal-budget gate → passivation and contacts. Critical unsolved gates: selectively exposing only target nGaN sidewall without irradiating QWs; finite ion straggle/depth/dose, angular shadowing; implanted C electrical activity vs implantation-induced isolation; post-MQW anneal thermal damage risk. Without selective mask this does **not** implement the current localized nGaN-only Cedge.
- Candidate PRE-MQW: grow nGaN up to intended upper region → lithographically mask future mesa-edge ring → implant C into exposed nGaN or grow selective GaN:C → validated recovery/cleaning and epitaxial regrowth → deposit MQW/EBL/pGaN → accurately align future mesa etch to buried annulus → passivation/contact. Protects already-formed MQW from carbon implantation anneal (since it is grown later) but has severe future-mesa overlay, high-quality epitaxial regrowth, and implant-damage recovery gates. Exact 5nm Dmg in TCAD is **not** a realizable lithographic alignment tolerance specification.
- Literature DOES demonstrate related *non-carbon* isolation concepts: As sidewall implantation in InGaN microLED (Next Nanotechnology 2025 DOI 10.1016/j.nxnano.2024.100101), F-implanted p-GaN current confinement ring in 6-10um microLED (ACS Photonics 2026 DOI 10.1021/acsphotonics.5c02363). Neither verifies a C-implanted upper-nGaN sidewall ring. Earlier `Characterization of Ca and C implanted GaN` (Materials Science and Engineering B 1997 DOI 10.1016/S0921-5107(97)00144-X) documents implantation damage/incomplete anneal with C+, and a Sandia 1995 report `Role of C, O and H in III-V nitrides` reports no measurable electrical activity for implanted C under its investigated conditions. Carbon-doped GaN growth literature supports C_N deep acceptor around Ev+0.9–1.1eV, but implanted-carbon activity cannot be assumed to match as-grown GaN:C.
- InGaN MQWs have temperature-dependent degradation/intermixing sensitivity; reports show significant degradation around 930–950 C for particular structures (J Alloys Compounds 2022, DOI 10.1016/j.jallcom.2021.163519; J Crystal Growth 2005 DOI 10.1016/j.jcrysgro.2005.04.002). Do not establish a universal safe/unsafe anneal temperature or prescribe unverified implantation energy/dose/angle/temperature.
- Next research gates: 1) team decides whether target is a chemically active C_N-compensated GaN:C edge vs damage-based implantation isolation (different device physics!); 2) compare POST vs PRE-MQW process feasibility, alignment and thermal budgets; 3) obtain measured/proven C depth and lateral profile/activation data, SRIM/SProcess process profile model before claiming fabrication realism; 4) ensure experimental masked/annealed control and inert-ion damage controls to separate C compensation vs irradiation damage; 5) keep current Baseline electrical/radiative validation priority unchanged.

## 2026-10-09 — 5V SVisual Clean_QW3 Rad field integral and '+' label correction (OBSERVED / UNRESOLVED)

- Worker 이택규 supplied `Field Integration` screenshot for `JUSUBIN_FAST_HALF_5V_TEST/n2_des`: field `RadiativeRecombination`, right pane `Regions of Dimension 2` shows ONLY `Clean_QW3 (InGaN)` with `Integral = 2.657110e+02 [s^-1*um^-1]`, `Domain=5.985012e-03 [um^2]`. This is **Clean_QW3-only 2D area integral**, not full QW3 or total photon output, and NOT IQE. Left list highlights both `Clean_QW3` and `Clean_QW3+DmgL_QW3` but only Clean_QW3 appears in right output, possibly stale result until Start Integration; do not interpret highlighted items as proven integrated.
- **Correction of previous GPT claim:** `Clean_QW3+DmgL_QW3` should NOT be assumed to denote union of bulk regions or selected as sole full-well ROI. Its structure and lack of inclusion in the dimension-2 output indicate it is likely a lower-dimensional boundary/interface label. Exact T-2022.03 metadata for '+' label has not been independently inspected, so interface interpretation remains PROVISIONAL. Safest method: select standalone region `DmgL_QW3` (not '+' named item), click `Start Integration`, verify `Regions of Dimension 2: DmgL_QW3`, record its Integral/Domain, then **sum independent Clean_QW3 and DmgL_QW3** integrals for whole QW3 (or choose both standalone 2D regions and verify both appear in output). Do not double-count interface or mix old results.
- The physical measured rate is 2D area-integrated per out-of-plane unit; raw SVisual [s^-1 um^-1] is NOT absolute 3D photon rate without explicit effective thickness. Same geometric normalization cancels for recombination fraction ratios when all wells are treated consistently; continue SRH/Auger over same 2D set and four QWs before IQE.
- Source: user screenshot Oct9 and earlier GitHub `PROJECT_AB_PRE_RUN_AUDIT.md`, SVisual manual Integration Tool general region-filter procedure. No code or TCAD source modified, no new run.

## 2026-10-09 — QW3 full 2D Radiative integration obtained from separate Clean/Dmg regions (OBSERVED)

- Worker 이택규; user SVisual Field Integration screenshot of completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des`, field `RadiativeRecombination`, `Regions of Dimension 2` explicitly lists **DmgL_QW3 (InGaN)**: `Integral=5.268180e-01 [s^-1*um^-1]`, `Domain=1.500002e-05 [um^2]`.
- Previously directly observed **Clean_QW3 (InGaN)**: `Integral=2.657110e+02 [s^-1*um^-1]`, `Domain=5.985012e-03 [um^2]`.
- These are separate disjoint **2D area region** integrals, so the full QW3 half-device measured raw regional sum = **266.237818 s^-1 um^-1**; total measured 2D domain area = **0.00600001202 um^2**. Arithmetic: 265.711 + 0.526818; 0.005985012 + 0.00001500002. **Derived**, not direct SVisual combined group output.
- This supersedes earlier incorrect idea that '+' item is a merged area. The `Clean_QW3+DmgL_QW3` entry should not be used as integrated 2D union without proof (likely lower-dimensional interface). Not full device IQE/absolute 3D photon rate. At NtSide=0, parametric damaged-edge traps are off, while DmgL_QW3 geometry exists.
- NEXT READ-ONLY: Integrate `srhRecombination` for standalone Clean_QW3 and DmgL_QW3 (or both as explicitly distinct 2D regions with actual Total Integral verification), then `AugerRecombination` same region scope. Keep units and voltage fixed; after all four QWs, compute recombination-based IQE from summed Rrad/SRH/Auger integrals; confirm normalization, full-vs-half equivalence and current physics before declaring baseline.
- No TCAD source edit, no new run; original files and checkpoints retained.

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

## 2026-10-09 — 이택규 QW4 Clean+DmgL 2D integrals obtained (OBSERVED + DERIVED)

- 5V_TEST NtSide=0 Half. SVisual Clean_QW4 2D integrals [s^-1 um^-1]: Rad 38746.96, SRH 35617690, Auger 1327.983, Domain 0.005985012 um². DmgL_QW4: Rad 98.768, SRH 226496.2, Auger 2.414354, Domain 0.00001500002 um². Summed QW4 Rrad 38845.728, SRH 35844186.2, Auger 1330.397354, total 35884362.325354. QW4-only recombination radiative fraction 0.1082525242%; SRH 99.8880400%. Prior QW3-only radiative fraction 0.0454256871%.
- This is NOT device IQE/EQE, and strong SRH requires effective material physics and current/injection sanity checks. QW1 and QW2 integrations pending. No source/run modifications.

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

## 2026-10-09 — Completed 5V_TEST n2 SDevice preprocessed 12 sidewall traps all OFF (OBSERVED / VERIFIED)

- Worker 이택규 executed directly `grep -nE 'Physics \\(Region=|IncompleteIonization|Traps|Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd`, showing physical-region declarations. `Clean_pGaN` `IncompleteIonization` line 128 and `DmgL_pGaN` `IncompleteIonization` line 137.
- Every one of **12 separate preprocessed left damaged-region traps has `Conc=0`**: DmgL_pGaN (line 145), DmgL_EBL (165), DmgL_Barrier0 (185), DmgL_QW1 (205), DmgL_Barrier1 (225), DmgL_QW2 (245), DmgL_Barrier2 (265), DmgL_QW3 (285), DmgL_Barrier3 (305), DmgL_QW4 (325), DmgL_Barrier4 (345), DmgL_nGaN (365). This is **confirmed Trap OFF** for all model's parameterized `DmgL_` sidewall trap regions in completed 5V NtSide=0 deck, not just two example regions. No right-side traps expected in symmetric Half.
- Scientific boundary: global `Recombination(SRH(),Auger(),Radiative)` remains ON and can generate a high baseline SRH without parameterized NtSide traps. Thus measured 5V all-QW SRH fraction 99.886% CANNOT be attributed to any of these explicit sidewall trap concentrations (zero). Cannot conclude sidewall physical damage is absent in reality, or that all other SRH and interface recombination in model is eliminated.
- Mg incomplete ionization `Physics` declarations shown for Clean/DmgL pGaN, but actual Mg donor concentration placement and free-carrier profile are STILL UNVALIDATED. `NtSide=1e18` counterpart also has NOT passed SDevice 5V convergence; no Full/Half+coarse matching, 2D J normalization, material lifetime or transient steady-state acceptance.
- NEXT READ ONLY: inspect preprocessed `pp1_dvs.cmd` from completed `JUSUBIN_FAST_HALF_5V_TEST` for `sdedr:define-constant-profile`, placements and `pMagnesiumActiveConcentration` / n donors, then verify n1_msh.tdr concentration profiles in SVisual. No new run or changes.

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
