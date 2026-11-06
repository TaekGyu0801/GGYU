## 2026-11-06 Lee scientific interpretation: Wu QW4 91% radiative share is NOT intrinsically invalid — UNRESOLVED physical cause
- Worker 이택규 correctly challenged prior assistant characterization of QW4 ≈91% as inherently abnormal and asked who determines Wu paper agreement. **CORRECTION:** QW4 ~91.03% OFF / ~91.10% ON from stored 12-QW integrated `RadiativeRecombination` is fraction of total *radiative recombination*, NOT QW4 IQE. Such unequal MQW population can occur physically; share alone is not evidence of a modeling error. It already occurs in OFF, so cannot be attributed solely to added sidewall traps.
- Current school Wu `CMP_WU_Copy` QW4 is n-side (x≈.161-.164 µm); literature on InGaN MQWs often emphasizes hole accumulation toward p-side under injection, so high n-side contribution warrants explanation, **not automatic rejection**. Prior saved central C1 data show enhanced QW4 e/h product and radiative rate; this explains numerical correlation, not proven physical cause or publication agreement. No assertion that Wu 2023 reported this precise share.
- Source check: Wu 2023 publisher doi:10.1016/j.micrna.2023.207542 supports 10µm, 4QW, trap-driven radiative/current-spreading trends, but accessible text does NOT establish QW4 91% or original Fig1's precise EBL/pGaN/contact. Independent MQW carrier nonuniformity literature DOI:10.1016/j.cap.2020.09.005 and PhysRevB.101.075305 support possible nonuniform QW recombination, not validation of THIS number.
- Acceptance responsibility remains with researchers (이택규, 주수빈) based on source/physics/evidence, with assistants as independent auditors; reviewer/professor may further review. Restrict Wu-fit claims to documented comparisons; physically unresolved items labeled UNRESOLVED.
- No new school run/code modifications, no new data extracted. Current model remains active Wu Copy n21 OFF/n25 ON 5V, not historical Kou V2. NEXT: do not re-run existing region integrals; check with existing saved band/carrier/polarization and any authentic Wu Fig1 which mechanisms could cause n-side QW4 dominance, and decide whether that affects the proposed sidewall baseline mechanism. Prior canceled hGap rerun stays canceled.

## 2026-11-06 Lee workflow correction — CMP_WU_Copy remains active; Kou V2 audit archival only
- **USER DIRECTIVE / PROPOSED WORKFLOW:** 이택규 corrected assistant's mistaken switch from active school `/user/semi/semi437/tmp/myproject/CMP_WU_Copy` to historical `~/CMP_BASELINE_2.0.0_V2`. Resume **Wu-based 10um candidate** using already completed 5V `n21_des` Trap OFF and `n25_des` Trap ON; preserve both.
- Previous 2026-11-06 Kou V2 n2/n6 file checks and successfully completed intended 3.6V logs were real OBSERVED archival facts, **not evidence the user chose to resume Kou, not a decision to replace Wu, and not a Baseline GO**. Do not continue Kou n2/n6 RadiativeRecombination analysis in this workstream absent new instruction.
- NEXT Wu, READ ONLY: open `CMP_WU_Copy/n21_des.tdr` and `n25_des.tdr` in SVisual; inspect 5V QW1-4 `RadiativeRecombination` spatial maps and regionwise integrals, then sidewall `SRHRecombination` and already saved `eGapStatesRecombination`. Avoid interpreting eGap alone as full net trap loss or simple three-term IQE as trap-inclusive IQE. No new run, source edit, or canceled hGap rerun. Later decide candidate suitability using evidence; no baseline freeze yet.
- Assistant acknowledged the misdirection and corrected active project after user's explicit question "엥 근데 지금 CMP wu copy 해야하는거 아니야?".

## 2026-11-06 Lee Kou V2 n2/n6 full configured 3.6V sweeps finished normally — OBSERVED; optical emission proxy next
- Worker 이택규 checked actual school effective `pp2_des.cmd`/`pp6_des.cmd`: first Quasistationary `Goal { Name="anode" Voltage=2.0 }`, second `Goal { Name="anode" Voltage=3.6 }`, followed by `Plot(FilePrefix="n2_end")`/`Plot(FilePrefix="n6_end")`. Hence 3.6V was **configured endpoint, not an early halt from a 5V goal**.
- Actual `n2_des.log` end: `Writing 'n2_des.tdr' ... done`, `Sentaurus Device simulation finished`, `Good Bye !`, 2026-10-14 15:44:14 KST, wallclock 7230.65s (~2h 00m 30.65s). `n6_des.log`: same normal ending, 2026-10-14 17:43:51 KST, wallclock 7173.64s (~1h 59m 33.64s). Prior terminal output at 3.6V n2 OFF 3.647e-8, n6 ON 9.220e-9; difference -74.72% (raw fixed-V current, **not** IQE).
- **Resolved numerical-status blocker:** V2 nodes 2 and 6 completed their *intended* 3.6V sweep. This does NOT confirm physically realistic LED emission, valid external light intensity, true current-density, IQE decrease, identical source decks except traps, or Baseline freeze.
- NEXT READ ONLY: open saved `n2_end_des.tdr` and `n6_end_des.tdr` in Sentaurus Visual, inspect `RadiativeRecombination` 2D maps with matched color scale and QW1–QW4 region field integration; if field is absent, inspect effective plot output declaration before any rerun. Map is internal photon-generation proxy, not measured brightness or optical extraction. Also assess QW4 dominance and SRH/trap loss without unverified double counting. Preserve outputs and unapproved hGap rerun.

## 2026-11-06 Lee Kou V2 3.6V node 2/6 effective trap sources and terminal last rows — OBSERVED; physical GO UNRESOLVED
- Worker 이택규 ran school read-only Bash loop under csh/tcsh via `bash -lc` in `~/CMP_BASELINE_2.0.0_V2`: for n=2,6, grep source traps/Pol and latest anode row.
- Effective `pp2_des.cmd` (OFF) has `Piezoelectric_Polarization( strain activation=0.5 )`; six displayed damaged-region `Traps(... Acceptor Level fromValBand EnergyMid=0.75 Conc=0 eXsection=1e-15 hXsection=1e-15)`. `pp6_des.cmd` (ON) has same polarization command and displayed traps `Conc=1e18`. This grep samples first six lines, not a complete source diff.
- Last displayed anode rows: n2 OFF at 3.600E+00V electron2.903E-19 hole3.647E-08 total3.647E-08; n6 ON at 3.600E+00V electron4.432E-22 hole9.220E-09 total9.220E-09. Derived (ON-OFF)/OFF = (9.220e-9/3.647e-8-1)*100≈-74.72%, a **raw fixed-voltage terminal-current change**; NOT IQE, isolated sidewall nonradiative loss, physical current density, or independent cause proof.
- Two 3.6V last-anode lines do NOT establish successful target-5V completion or that `n2_end_des.tdr`/`n6_end_des.tdr` are final 3.6V states. Absolute raw current remains small and geometry/physics baseline suitability is unresolved. No rerun, change, or overwrite.
- PROPOSED NEXT focused read-only: determine per-node run termination and whether 3.6V was configured stop or early halt from `n2_des.log`/`n6_des.log` and effective Solve target. Then existing 3.6V QW radiative and defect pair-recombination once if available, before Project A GO; preparatory Project A design can proceed without treating common baseline as frozen. Avoid repeating AreaFactor or Wu terminal checks.

## 2026-11-05 Lee n25 Trap ON 5V terminal freshly reconfirmed alongside n21 OFF — OBSERVED both actual current logs; model loss still UNRESOLVED
- 이택규 school `CMP_WU_Copy` directly checked 5V anode OFF n21 (Ie=1.695e-4 Ih=2.399e-3 total=2.569e-3) and ON n25 (Ie=1.690e-4 Ih=2.397e-3 total=2.566e-3). ON fresh grep now obtained, exactly corroborating prior log. ON/OFF raw total -0.11678% based on rounded output; not IQE, J, or sidewall trap-loss fraction.
- NEXT prioritize read-only existing 5V region-integrated Radiative/SRH/Auger and correctly defined net trap pair rate; original Wu Fig1 EBL/contact fidelity and physical 2D J still unresolved. Preserve n21/n25 and canceled hGap. No solver rerun/source changes.

## 2026-11-05 Lee n21 OFF 5V terminal current reread and prior n25 ON comparison — OBSERVED OFF / historical ON comparison; IQE UNRESOLVED
- 이택규 school `CMP_WU_Copy/n21_des.log` final 5V anode raw currents: electron1.695e-4, hole2.399e-3, total2.569e-3. Same n21 grep was run twice; it does not independently validate Trap ON. Prior observed n25 ON 5V: electron1.690e-4, hole2.397e-3, total2.566e-3. Calculated ON/OFF total -0.1168%; **terminal-current change is not IQE or trap loss fraction**. Raw 2D unit/z width and J still UNRESOLVED.
- NEXT one read-only `grep -E '^[[:space:]]*anode[[:space:]]+[0-9.E+-]+' n25_des.log | tail -n 1`. After confirmation evaluate integrated net trap recombination and IQE; no new simulation, school source edits or canceled hGap restart.

## 2026-11-05 Lee independent Wu paper Fig1/Fig11 check — OBSERVED text / UNRESOLVED Figure 1 pixels
- Publisher source Wu et al. 2023 DOI 10.1016/j.micrna.2023.207542 names Fig. 1(a) as **basic TCAD structure** and Fig. 11 as separately **proposed C-shaped anode**, so C-shaped contact is NOT independently established for baseline Fig1. Accessible source text verifies 10um example, nGaN 3.9um Si5e18, 4 QW 3nm In0.08, GaN barrier8nm, p Mg2e19 nominal, sidewall traps within 5nm.
- Actual Figure 1(a) image/full PDF not obtained via public browsing; ResearchGate lists request PDF/no public full text. **EBL presence, p-GaN thickness, Fig1 contact geometry still cannot be verified.** Current CMP_WU_Copy model (EBL=0, pGaN=0.120um PILOT, planar Ohmic contacts) remains a provisional 10um pilot, not certified exact Wu replica, and not the protected 4um Kou Common Baseline.
- Worker 이택규. No new run or school edits. Next preserve runs; retrieve legitimate original Fig1 when possible, otherwise label pilot assumptions and evaluate physically correct 2D J and trap-inclusive IQE before GO. Source https://www.sciencedirect.com/science/article/pii/S2773012323000390 .

## 2026-11-05 Lee Wu n25 source AreaFactor grep verified — OBSERVED, 2D J still UNRESOLVED
- Worker 이택규 pasted actual school `CMP_WU_Copy` terminal read-only grep: `grep -nEi 'AreaFactor|Physics|Electrode' pp25_des.cmd | head -n 35` lists `Electrode {` at line 18 and global `Physics {` at line 22, with region Physics blocks through line 203; **no explicit AreaFactor occurrence in this effective source grep**. Earlier `n25_des.log` showed anode/cathode electrode area factor=1. This establishes no explicit AreaFactor in this inspected pp25 source, not complete validation of units or geometry.
- Repeated user n25 terminal rows: 4.804V Ie=1.364e-4 Ih=2.100e-3 total=2.236e-3; 4.904V Ie=1.525e-4 Ih=2.251e-3 total=2.403e-3; 5.000V Ie=1.690e-4 Ih=2.397e-3 total=2.566e-3. 5V hole share=(2.397e-3/2.566e-3)*100=93.41% of electrode conduction current, NOT IQE.
- Current-density units/effective z width and projected area are still unresolved; conditional planar 10um stripe J is NOT a verified 4um physical pixel J. NEXT READ ONLY inspect `sed -n '1,33p' pp25_des.cmd` for electrode global physics and `sed -n '1,32p;80,94p' pp1_dvs.cmd` for geometry/contacts if needed; resolve unit convention before any physical J/IQE GO. Do not rerun or modify protected models; canceled hGap run stays canceled.
- No new simulator run or school source edit. Source: user-pasted 2026-11-05 command outputs.

## 2026-11-05 Lee n25 5V terminal electron hole total current and electrode AreaFactor reconfirmed — OBSERVED; physical current-density normalization UNRESOLVED
- Worker 이택규 school `CMP_WU_Copy/n25_des.log` grep returns electrode initial entries `anode` Ohmic area factor 1 and `cathode` Ohmic area factor 1 (lines 236–237). Last terminal current table entries: anode at 4.804V electron 1.364e-4, hole 2.100e-3, total 2.236e-3; 4.904V electron 1.525e-4, hole 2.251e-3, total 2.403e-3; 5.000V electron 1.690e-4, hole 2.397e-3, conduction total 2.566e-3 (Sentaurus 2D terminal-current output convention needs exact-version confirmation). 5V component check electron+hole=2.566e-3; hole fraction 2.397e-3/2.566e-3 = ~93.4% of electrode conduction current, **not** an IQE or QW pair-recombination fraction.
- Historical official Synopsys Sentaurus Device UG N-2017.09 states 2D terminal current default unit A/um, and 2D default missing-direction width 1um unless physics/electrode AreaFactor modifies it. The team's school T-2022.03 UG observation says AreaFactor multiplies currents and charges and may represent missing z width. Under the **conditional** assumptions 2D A/um output, global AreaFactor=1, nominal contact width=10um across stripe, simple planar projected J = (2.566e-3 A/um)/(10um) * 1e8 um2/cm2 = 2.566e4 A/cm2. This number is a *conditional model-stripe J*, NOT verified 10x10um real pixel J or 4um Common Baseline J. Recheck live `pp25_des.cmd` Physics/global AreaFactor and SDevice actual effective unit/geometry and log output before reporting it as validated.
- NOTE: user provided only electrode log and last current entries; **did not yet provide previous requested source grep**. Next READ ONLY single step `grep -nEi 'AreaFactor|^[[:space:]]*Physics[[:space:]]*\\{|^[[:space:]]*Electrode[[:space:]]*\\{' pp25_des.cmd | head -n 35` to check global current scaling. No rerun, no source changes. This raw current should not be labeled as physical measured current or published IQE.

## 2026-11-05 Lee effective Wu school SDE epi and contact configuration confirmed by grep — OBSERVED school source; Wu publication fidelity partially verified, EBL/contacts unresolved
- Worker 이택규 supplied direct school read-only `grep -nE 'Wm|Wdmg|tP|tEBL|tQW|tQB|tN|xIn|anode|cathode' pp1_dvs.cmd | head -n 80` in `CMP_WU_Copy`. Actual effective SDE values: `Wm=10.0µm`, `Wdmg=0.005µm` each side, `tP=0.120µm` comment explicitly PILOT Wu unverified, `tEBL=0.000µm` comment expressly NOT proof Wu has no EBL, `xAlEBL=0.15` UNUSED, `tQW=0.003µm`, `tQB=0.008µm`, `tN=3.900µm`, `xIn=0.08`. Region order pGaN/EBL(0)/B0/QW1/B1/QW2/B2/QW3/B3/QW4/B4/nGaN. Define contacts `anode`/`cathode` and assign on `find-edge-id(position 0.0 ymid 0)` and `find-edge-id(position Xend ymid 0)` respectively; actual full contact spans and Wu publication electrode fidelity are NOT confirmed by this grep alone. No simulation/edit.
- Publisher article Wu et al., *Physical mechanisms on the size-effect in GaN-based Micro-LEDs*, Micro and Nanostructures 177 (2023) 207542, DOI 10.1016/j.micrna.2023.207542, publicly accessible article excerpt confirms example 10 µm, nGaN 3.9µm Si5e18, 4x InGaN In0.08 3nm, GaN QB8nm, pGaN Mg2e19, and 5nm acceptor-like sidewall traps; applied piezoelectric polarization/Mg incomplete-ionization/local field traps/Rad/SRH/Auger. Accessed excerpt does NOT independently confirm pGaN thickness, EBL presence, or exact standard-contact structure from Fig1. These must remain UNRESOLVED; no full paper replica claim.
- Important protected boundary: `CMP/COMMON_BASELINE.md` retains Kou vertical backbone + representative 4µm mesa + Wu sidewall trap concept, so this 10µm Wu school pilot must not silently replace/overwrite protected 4µm Common Baseline. Next READ ONLY: `sed -n '1,32p;80,94p' pp1_dvs.cmd` to inspect exact source header/contacts and their provisional descriptions; then decide whether to obtain original Fig1 and resolve EBL/contact fidelity, before physical J/IQE GO. No rerun, canceled hGap remains canceled.

## 2026-11-05 Lee baseline go/no-go gate shift from field profiling to Wu structural fidelity — PROPOSED workflow change; no new model decision
- Worker 이택규 agreed to proceed beyond repetitive central QW field extraction toward **baseline suitability evaluation**. PRELIMINARY ASSESSMENT: school saved `CMP_WU_Copy` 10 µm lateral stripe is a **separate Wu pilot, not the protected 4 µm Kou-epitaxy Common Baseline**. `CMP/COMMON_BASELINE.md` specifies representative 4 µm mesa, Kou In0.15Ga0.85N 4x QW3nm / 5x GaN barrier22nm, p-Al0.15Ga0.85N EBL26nm, and Wu 5nm damaged-sidewall physics. School Wu effective SDE previously OBSERVED Wm10µm, 4x QW In0.08 3nm, GaN QB8nm, EBL0, 5nm sidewall. These are materially different test vehicles, not interchangeable; neither has a confirmed publication-ready IQE / J normalization baseline.
- Wu 2023 publisher abstract DOI 10.1016/j.micrna.2023.207542 confirms sidewall traps, radiative size effect and lateral current dispersion as research concerns, but accessible abstract does NOT settle exact paper Fig.1 contacts/EBL details. Avoid claiming full Wu paper fidelity or pretending 4um Common Baseline has been replaced.
- NEXT one READ ONLY school step: from `CMP_WU_Copy`, inspect actual effective `pp1_dvs.cmd` geometry variables and anode/cathode placement via `grep -nE 'Wm|Wdmg|tP|tEBL|tQW|tQB|tN|xIn|anode|cathode' pp1_dvs.cmd | head -n 80`. Then build source-by-source structure/contacts/physics fidelity table, identify UNKNOWN paper Fig1 details; only afterward evaluate J normalization, trap pair rate/IQE, and go/no-go to compare Wu pilot vs protected Kou candidate. No SDevice rerun and do not touch canceled hGap output-only run.

## 2026-11-05 Lee n21 OFF central QW1-4 ElectricField-X numerical statistics — OBSERVED; polarization/transport root cause UNRESOLVED
- 작업자 이택규 actually executed one-line read-only AWK on school saved `CMP_WU_Copy/WU_n21_C1_QW_Efield.csv` (n21_des Trap OFF, 5 V, Y=5um central cutline C1, QW1 x=[.128,.131), QW2 [.139,.142), QW3 [.150,.153), QW4 [.161,.164)). Output:
  - QW1 N=3, signed Emean +6.881e5 V/cm, abs mean 6.943e5, min -9.345e3, max +1.041e6.
  - QW2 N=4, signed Emean +8.292e5, abs mean 8.495e5, min -4.064e4, max +1.473e6.
  - QW3 N=3, signed Emean +3.108e5, abs mean 3.590e5, min -7.223e4, max +5.762e5.
  - QW4 N=4, signed Emean +4.901e5, abs mean 5.118e5, min -4.338e4, max +1.524e6.
- DERIVED QW4/QW3 abs-mean ≈1.426x; QW2 abs-mean 8.495e5 > QW4 abs-mean 5.118e5; hence field magnitude does NOT monotonically track QW4's highest carrier/radiative sample means. QW4 peak 1.524e6 V/cm may be boundary-sensitive due to small sample counts and duplicated interface points, so inspect raw per-coordinate entries before attributing physical origin. These are **1D sample arithmetic means and extrema**, not region-weighted field integrals, QW internal fields under independent mesh convergence, or causal evidence of polarization/transport. Previous QW4 relative QW3 high carriers and nearly same OFF/ON central values remain established.
- NEXT (PROPOSED READ-ONLY): print raw `X,ElectricField-X` rows over X=0.150..0.164µm and inspect maxima locations/interface duplicates; consider mesh/physics assumptions only after this. No new SDevice simulation, no source changes, canceled hGap rerun remains canceled.

## 2026-11-05 Lee n21 OFF central ElectricField-X CSV exported — OBSERVED export; QW field comparison pending
- Worker 이택규 provided school terminal `head -n 8 WU_n21_C1_QW_Efield.csv` in `CMP_WU_Copy`: CSV header `X,ElectricField-X`, second row `none,SELECTED` (nonnumeric), first numeric rows X=0.12 -> 9029.3958, X=0.12 -> -17558.221, X=.12128516 -> -15943.13, X=.12327344 -> -13623.278, X=.12526172 -> -11355.53, X=.12725 -> -10085.009. Field units displayed in prior school SVisual screenshot as V/cm; raw CSV header omits unit.
- Context: saved `n21_des` Trap OFF, 5 V, Y=5um central C1 X=.12-.18um. This confirms file export and some non-QW interval points, **not** per-QW ElectricField-X stats, polarization cause, or validated injection barrier. The two X=.12 entries may represent coincident boundary samples; preserve both when comparing and avoid mistaken averaging with duplicate interface points.
- NEXT PROPOSED READ-ONLY: one-line awk samples QW1 [.128,.131), QW2 [.139,.142), QW3 [.150,.153), QW4 [.161,.164), reporting count, signed mean, absolute mean, min/max in V/cm. Compare QW3/QW4 with prior local carrier/band data. No new solver run, physics/code edits, or canceled hGap rerun.

## 2026-11-05 Lee n21 OFF QW3 QW4 interface band steps from saved C1 — OBSERVED / DERIVED; band-step amplitudes not equal transport barriers
- Worker 이택규 read school `CMP_WU_Copy/WU_n21_C1_QW_band.csv` from n21_des Trap OFF at 5V, central Y=5um, and pasted actual X-resolved Ec/Ev/EFn/EFp rows in interval X=0.150..0.165um. At duplicated coordinates (values on two sides of modeled material interfaces), numerical steps:
  - X=.15000001 Barrier2 -> QW3: Ec -0.0808 -> -0.2726, DeltaEc=-0.1918 eV; Ev -3.5177 -> -3.3738, DeltaEv=+0.1439 eV.
  - X=.15300000 QW3 -> Barrier3: Ec -0.1440 -> +0.0478, DeltaEc=+0.1918; Ev -3.2453 -> -3.3891, DeltaEv=-0.1438.
  - X=.16100000 Barrier3 -> QW4: Ec +0.0017 -> -0.1900, DeltaEc=-0.1917; Ev -3.4351 -> -3.2913, DeltaEv=+0.1438.
  - X=.16400000 QW4 -> Barrier4: Ec -0.1040 -> +0.0878, DeltaEc=+0.1918; Ev -3.2052 -> -3.3490, DeltaEv=-0.1438.
- DERIVED interface discontinuity magnitudes are nearly the same for QW3 and QW4: |DeltaEc|≈0.192 eV, |DeltaEv|≈0.144 eV. Thus present data do not show a special QW4-only *material interface band offset*; these individual jumps are not full injection barriers or proof of the root cause of high QW4 n,p. EFn at X=.153 changes -0.2140 -> -0.1340 (0.0800 eV) while EFp -3.2840 -> -3.2830 (0.0010 eV), which must not be assigned to an exact transport mechanism without model validation.
- NEXT READ ONLY: examine X-resolved band bending and carrier/charge profiles across barriers, or matched n25 ON at same central coordinates. Assess polarization, thermionic boundary conditions, geometry fidelity cautiously. No rerun, no changes to saved n21/n25, canceled hGap remains canceled.

## 2026-11-05 Lee n21 OFF Barrier0-4 C1 Ec Ev extrema — OBSERVED / DERIVED; transport barriers and physical cause UNRESOLVED
- 작업자 이택규; direct school csh terminal executed READ-ONLY one-line `awk` on saved `CMP_WU_Copy/WU_n21_C1_QW_band.csv` (n21_des Trap OFF, 5V, central Y=5µm, X cutline .12-.18µm). Five region windows: Barrier0 [.120,.128), B1 [.131,.139), B2 [.142,.150), B3 [.153,.161), B4 [.164,.172), each N=6 samples. Numeric reported extrema in eV:
  B0 Ec min=-0.5787 max=-0.5690; Ev min=-4.0156 max=-4.0039.
  B1 Ec min=-0.4615 max=-0.2697; Ev min=-3.7357 max=-3.5627.
  B2 Ec min=-0.2076 max=-0.0158; Ev min=-3.5113 max=-3.3088.
  B3 Ec min=-0.1440 max=+0.0478; Ev min=-3.4267 max=-3.2453.
  B4 Ec min=-0.1040 max=+0.0878; Ev min=-3.4535 max=-3.2052.
- Derived: B1..B4 Ec maxima ascend; B4 Ev min is lower than B3 Ev min, so not a monotonic simple valence profile across all barriers. Each row gives location-window min/max across six separate points, NOT matching interfacial samples and NOT injection barrier height or carrier barrier energy by itself. Prior OFF QW central mean offsets Ec-EFn QW1..4 .0813,.0727,.0272,-.0009 eV; EFp-Ev .1877,.1612,.0994,.0410 eV; OFF QW4 carrier accumulation seen with traps disabled. Cause cannot be assigned to polarization/contacts/transport solely from extrema.
- NEXT read-only: inspect raw CSV X-resolved Ec/Ev and EFn/EFp around adjacent QW/Barrier interfaces (show actual same-position values and duplicate-interface points), determine barrier direction and energy steps; then compare selected saved n25 ON only if useful. Preserve completed n21/n25 and canceled hGap rerun; no simulation/code modification.

## 2026-11-05 Lee n21 OFF central QW band offsets numerical samples — OBSERVED and DERIVED; physical cause unresolved
- Worker 이택규 actually ran read-only one-line AWK on school saved `CMP_WU_Copy/WU_n21_C1_QW_band.csv` (`n21_des` Trap OFF 5 V, Y=5 µm central C1; QW x ranges [.128,.131)/[.139,.142)/[.150,.153)/[.161,.164)). Reported QW1 N3 Ec=-0.6643 Ev=-3.8774 EFn=-0.7456 EFp=-3.6898 Ec-EFn=+0.0813 EFp-Ev=+0.1877 eV; QW2 N4 Ec=-0.3920 Ev=-3.5771 EFn=-0.4647 EFp=-3.4159 Ec-EFn=+0.0727 EFp-Ev=+0.1612; QW3 N3 Ec=-0.1873 Ev=-3.4005 EFn=-0.2146 EFp=-3.3011 Ec-EFn=+0.0272 EFp-Ev=+0.0994; QW4 N4 Ec=-0.1292 Ev=-3.3144 EFn=-0.1284 EFp=-3.2734 Ec-EFn=-0.0009 EFp-Ev=+0.0410 (rounding may affect last-digit differences).
- DERIVED: QW4 relative QW3 Ec-EFn decreases 0.0281 eV, EFp-Ev decreases 0.0584 eV. This is qualitatively consistent with earlier observed OFF central eMean QW3 3.645e19 vs QW4 5.493e19 (~1.51x), hMean 3.720e18 vs 1.874e19 (~5.04x), and RadMean 1.818e28 vs 2.151e29 (~11.83x). Ec-EFn in QW4 is slightly negative, so do not blindly apply nondegenerate Boltzmann formula. QW-specific means on 1D cutline, not whole-area transport/barrier integrals.
- INTERPRETATION: Relative band-edge/quasi-Fermi alignment correlates with central QW4 higher carrier densities; **does not establish root cause** of alignment. Polarization, barrier band bending, contact/electrode geometry, transport models/quantum assumptions, and Wu paper fidelity remain unresolved. Trap OFF already has QW4 dominance; do not claim trap ON caused it. The numerical profile is not a validated physical IQE.
- NEXT READ ONLY: inspect saved X=0.12–0.18 µm band-edge and quasi-Fermi traces across barriers / optional n25 equivalent under same conditions; discriminate hole injection distribution and potential/band barrier changes, without code changes or rerunning previously canceled hGap. No new solver run.

## 2026-11-05 Lee n21 OFF central band/quasi-Fermi CSV header confirmed — OBSERVED CSV export; QW energy analysis PENDING
- Worker 이택규 terminal output from school `CMP_WU_Copy` confirms exported `WU_n21_C1_QW_band.csv` for saved 5 V Trap OFF `n21_des` central Cut Y C1 (Y=5 µm; X=0.12..0.18 µm). Actual header: `X,ConductionBandEnergy,ValenceBandEnergy,eQuasiFermiEnergy,hQuasiFermiEnergy`; row 2 `none,none,none,none,none` is nonnumeric metadata. First numeric lines x=0.12, 0.12128516, 0.12327344, 0.12526172, 0.12725 µm; these do not yet establish QW1–4 band-edge/energy-offset statistics.
- NEXT: read-only one-line AWK samples QW1 x=[.128,.131), QW2 [.139,.142), QW3 [.150,.153), QW4 [.161,.164), and report per QW mean Ec, Ev, EFn, EFp, Ec-EFn, EFp-Ev. Compare concentration trend with saved n21/n25 carrier/radiative samples before attributing root cause. This calculation is proposed, NOT YET OBSERVED. No new SDevice run/code modification; canceled hGap rerun remains canceled.

## 2026-11-05 Lee n21 OFF versus n25 ON central QW CSV numerical comparison — OBSERVED / DERIVED; physical root cause UNRESOLVED
- 작업자 이택규; actual school `CMP_WU_Copy/WU_n21_C1_QW_carrier_rad.csv`, exported from saved 5 V Trap-OFF `n21_des` using central Y=5 µm C1 X=0.12..0.18 µm; terminal `head -n 8` confirms header `X,eDensity,hDensity,RadiativeRecombination` and nonnumeric metadata row `none,none,SELECTED,none`. Single-line AWK `NR>2` produced exact observed QW samples using X ranges [.128,.131)/[.139,.142)/[.150,.153)/[.161,.164) µm:
- OFF QW1 N3 e=1.574e19, h=2.866e16, Rad=3.612e25, mean(np)=1.806e35;
- OFF QW2 N4 e=2.056e19, h=1.093e18, Rad=8.874e25, mean(np)=4.437e35;
- OFF QW3 N3 e=3.645e19, h=3.720e18, Rad=1.818e28, mean(np)=9.090e37;
- OFF QW4 N4 e=5.493e19, h=1.874e19, Rad=2.151e29, mean(np)=1.075e39. e/h units cm^-3; Rad cm^-3 s^-1, np cm^-6. These are sampled 1D means, NOT 2D integral or IQE.
- Prior separate JuSubin ON n25 C1 measured same N=3/4/3/4, e=[1.572e19,2.053e19,3.644e19,5.493e19], h=[2.857e16,1.089e18,3.712e18,1.874e19], Rad=[3.611e25,8.874e25,1.812e28,2.150e29], np=[1.806e35,4.437e35,9.062e37,1.075e39]. Rounded local numbers show very small ON/OFF differences, especially QW4 nearly unchanged. Central QW4 concentration existed with trap OFF: consistent with prior 2D Rad QW4 ~91.03% OFF and ~91.10% ON, but does not rule out sidewall-local effects. Exact sample coordinate pairing and 2D current normalization/whole device loss remain unverified.
- NEXT READ ONLY: on preserved central n21 cutline inspect / export X, ConductionBandEnergy, ValenceBandEnergy, eQuasiFermiEnergy, hQuasiFermiEnergy (and optionally compare to n25) to understand n-side QW4 carrier accumulation. Do not assert physical root cause without verifying band/transport/contacts/polarization. Do not rerun canceled hGap, overwrite existing results, or modify protected baseline.

## 2026-11-05 — LeeTaekGyu Wu n21 Trap OFF center hDensity cutline shown (OBSERVED screenshot / numeric comparison pending)
- Worker 이택규 supplied school Sentaurus Visual T-2022.03 screenshot of preserved `CMP_WU_Copy/n21_des` (saved Trap OFF, 5 V); `Tools > Cut Y` cutline C1 at `Y=5 µm` with X endpoints `0.12` and `0.18 µm`. The right `Cutline_Y Plot` labels `hDensity(C1(n21_des))` and displays four well-region hole-density peaks; the QW4-side feature is visually the tallest on the logarithmic plot. This is **qualitative screenshot evidence only**: exact hDensity samples and QW4/QW3 ratios are NOT yet measured, and curve scale/upper clipping precludes precise peak value.
- NEXT read-only: select right-side XY plot, open `Data > Export XY Data` if offered, then export eDensity/hDensity/RadiativeRecombination for the same Y=5 µm n21 cutline. Compare numerical QW1–4 intervals against JuSubin's saved n25 Trap ON CSV. Preserve n21/n25 and cancelled hGap rerun; no new simulation, code edit, or validated physical root cause.

## 2026-11-04 JuSubin measured n25 central QW carrier radiative CSV — OBSERVED / DERIVED (physical root cause still UNRESOLVED)
- Worker **주수빈** executed a single-line awk read-only analysis of saved `CMP_WU_Copy/WU_n25_C1_QW_carrier_rad.csv` from the `n25_des` Trap ON, 5 V, central Y≈5um C1 cutline. Reported samples `QW1 N=3 eMean=1.572e19 hMean=2.857e16 RadMean=3.611e25 npMean=1.806e35`; `QW2 N=4 e=2.053e19 h=1.089e18 Rad=8.874e25 np=4.437e35`; `QW3 N=3 e=3.644e19 h=3.712e18 Rad=1.812e28 np=9.062e37`; `QW4 N=4 e=5.493e19 h=1.874e19 Rad=2.150e29 np=1.075e39`. e/h units cm^-3, Radiative cm^-3 s^-1, np cm^-6; averages are simple **sample means on one line** not 2D integrals/area-averaged rates or IQE.
- Derived `QW4 / QW3`: e=1.507x, h=5.048x, np=11.863x, radiative=11.865x. Derived per-QW `RadMean/npMean` ≈2.00e-10 cm^3/s for all four wells (empirical effective B in these four local samples, **not yet independently verified against pp25_des.par**). The local radiative hierarchy follows local electron–hole product; do NOT multiply separately averaged e and h to reproduce npMean (covariance).
- Earlier independent n21 **Trap OFF** saved 12-QW integrated Radiative has QW4 ≈91.03% share; n25 Trap ON 12-QW Rad also ≈91.10%. Thus QW4 weighting already exists when explicit sidewall Trap is OFF and should NOT be attributed to NtSide ON without independent evidence. Carrier-accumulation **proximate numerical explanation** found, but physical root cause of high n-side QW4 holes, transport/band offsets/polarization/recombination model and Wu fidelity remain UNRESOLVED.
- NEXT: preserve both saved datasets, compare **central Y=5um n21 OFF** eDensity/hDensity with n25 ON using same exact QW regions and optionally examine saved band-edge/quasi-Fermi cutlines. Do not modify active model or rerun canceled hGap. No new SDevice execution and no source changes.

## 2026-11-04 — JuSubin n25 central C1 CSV export verified (OBSERVED / QW NUMERICAL ANALYSIS PENDING)
- 작업자 주수빈 학교 CMP_WU_Copy에서 SVisual Export XY Data 변수 `X,eDensity,hDensity,RadiativeRecombination`를 `WU_n25_C1_QW_carrier_rad.csv`로 저장한 뒤 직접 터미널 `head -n 12 WU_n25_C1_QW_carrier_rad.csv` 결과를 제공함. CSV header 정확히 네 변수, 두 번째 행 `none,none,none,none`(수치 아님; 분석시 제외), 첫 수치 행 X=0, 뒤 X=.0318125..0.12um etc. X~0.12 이하 시작 부분은 QW 비교 범위가 아니라 p측/Barrier0 영역에 해당함. 전체 CSV는 아직 직접 확인하지 않았으며 QW별 e/h/Rad 피크/평균값은 미측정.
- NEXT (READ-ONLY): 저장된 CSV에서 QW1 X=[.128,.131), QW2 [.139,.142), QW3 [.150,.153), QW4 [.161,.164) 샘플 각각 n, mean(eDensity), mean(hDensity), mean(Radiative), max peak 및 n*p 비교. 1D 중앙 cutline의 평균/피크는 2D 영역 적분이나 IQE가 아님. 기존 n21/n25 저장/취소 hGap rerun 보존.

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

## 2026-11-04 JuSubin official T-2022.03 Traps p580 local capture emission excerpt — OBSERVED / rate accounting UNRESOLVED
- 작업자 주수빈 executed read-only local `pdftotext -layout .../sdevice_ug.pdf - | sed -n "30495,30545p"` in school CMP_WU_Copy. Direct footer: **Sentaurus Device User Guide, T-2022.03, p.580**, Chapter 17 "Traps and Fixed Charges / Visualizing Traps".
- OBSERVED manual defines `eGapStatesRecombination` and `hGapStatesRecombination` for **conduction-band and valence-band** trap-related recombination outputs, respectively; `TrappingRates` provides per-trap capture and emission processes (local, inelastic tunneling, elastic tunneling). For Acceptor/eNeutral, capture is electron capture; for Donor/hNeutral, capture is hole capture. The displayed interface-insulator-charge visualization note is general guidance, NOT proof that current Wu's `Physics(Region="DmgL/R_QW4")` uses an interface-trap model.
- BOUNDARY: this paragraph does NOT give a double-count-safe equation combining `eGapStates`, `hGapStates`, and ordinary SRH nor validate final IQE. Need investigate underlying net capture/emission balances and steady-state status, only then calculate proper pair-rate accounting. Existing n25 saved eGap only; canceled hGap rerun stays canceled.
- No code, simulations, plot data or school files changed. NEXT user read-only locate "Local Capture and Emission Rates" and related equations in authorized installed T-2022.03 PDF; keep n21/n25 as saved.

## 2026-11-04 — JuSubin 2026-11-04 T-2022.03 official recombination output definitions verified (OBSERVED / INTERPRETATION STILL UNRESOLVED)
- 작업자 주수빈 supplied school terminal output from installed local `sdevice_ug.pdf` (T-2022.03 installation path), `pdftotext -layout ... | grep -ni -C 5 -E 'eGapStatesRecombination|hGapStatesRecombination|SRHRecombination' | head -n 120`.
- Direct manual excerpt shows `Physics{Recombination(SRH...)}` activates SRH model, `Plot{SRHRecombination}` outputs SRH rate (text line 24512–24518). Plot variable glossary names `srhRecombination` = SRH net `R_net` and points to Shockley–Read–Hall Recombination p.473 (text line 83190). The Traps section explicitly states **eGapStatesRecombination is trap recombination rate for the conduction band** and **hGapStatesRecombination is corresponding valence-band rate**, and distinguishes capture/emission/TrappingRates (text lines 30517–30523; Chapter 17 p.543 in glossary).
- Other `eSRHRecombination/hSRHRecombination/tSRHRecombination` outputs on user snippet belong to *Dynamic Nonlocal Path Trap-Assisted Tunneling* (glossary references p.481), so do not equate them with the ordinary `SRHRecombination` + `eGapStates` output interpretation.
- Definitively established by the excerpt: SRH and e/h trap fields are separately named/modelled outputs. NOT YET established: how e/h capture-emission net terms form a single steady-state electron–hole-pair trap loss (incl. non-local effects), whether any cross-field double counting arises in this exact Wu deck, what domain must be integrated, or validated total IQE. Existing Wu n25 has only eGap plotted; no fresh hGap simulation is approved.
- NEXT READ ONLY: print short contiguous official manual passages around extracted text lines 24505–24521 and 30496–30545 to capture surrounding caveats/rate accounting; if necessary inspect trap charge/emission equations before deciding physically justified loss denominator. Preserve n21/n25 and user-canceled hGap rerun. No deck edit or solver run.

## 2026-11-04 — JuSubin live Wu pp25 Physics/QW4 trap excerpt 2026-11-04 (OBSERVED / INTERPRETATION PENDING)
- 작업자 주수빈, 학교 `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`의 실제 `sed -n '1,48p;159,177p' pp25_des.cmd` 결과를 제공. Effective ON pp25: `Grid=n1_msh.tdr`, `Parameter=pp25_des.par`, 300 K, `DefaultParametersFromFile`, Fermi, Mobility(DopingDependence HighFieldSaturation), `Recombination(SRH Radiative Auger)`, `Piezoelectric_Polarization(strain)`, `IncompleteIonization(Dopants="MagnesiumActiveConcentration")`, `Thermionic`.
- OBSERVED `Physics (Region="DmgL_QW4")` and `DmgR_QW4`: `Traps((Acceptor Level FromValBand EnergyMid=0.75 Conc=1e18 eXsection=1e-15 hXsection=1e-15 PooleFrenkel))`. Earlier Lee independently grepped same parameter consistency in all 22 DmgL/R regions. This is an explicitly modeled 5-nm sidewall-region **bulk/volume trap**, not an interface-only `Physics(RegionInterface=...)` declaration; matching Wu paper physical interface assumptions is UNVERIFIED. Confirmed output setting does not establish net e/h trap recombination or IQE.
- IMPORTANT discrepancy: comment header says `PROPOSED/NOT RUN ON SCHOOL T-2022.03`, but earlier 2026-11-04 directly verified `n25_des.log` completed 5 V. Treat header as stale/misleading execution-status text, not as proof the pp25 deck was not run. File excerpt combines NONADJACENT line ranges (1–48 and 159–177); mid-stream `PooleFrenkel) ) }` alone is NOT evidence of syntax corruption.
- Version-matched T-2022.03 sdevice_ug.pdf is referenced in `CMP/references/TCAD_REFERENCE_INDEX.md` but NOT present in GitHub. 2022 Synopsys Training section 13 distinguishes bulk/interface traps and eGapStatesRecombination versus hGapStatesRecombination (https://ghzphy.github.io/Sentaurus_Training/sd/sd_13.html), not an exact local UG audit. Existing saved n25 Plot lacks hGap. NEXT READ-ONLY: obtain authorized local T-2022.03 official definitions and verify rate balance / net e/h pair accounting, then 2D current normalization and Wu fidelity; preserve n21/n25, do NOT restart canceled hGap run. No code edits, reruns, or model changes.

## 2026-11-04 — Lee actual Wu ON Physics/Traps excerpt inspected (OBSERVED / UNRESOLVED)
- User school `pp25_des.cmd` grep confirms global `Physics { Recombination( SRH Radiative Auger ) }` and 22 region-scoped `Traps(...PooleFrenkel)` blocks (11 left/right pairs: DmgL/R pGaN, Barrier0..4, QW1..4, nGaN). This is a configuration check only; full type/Conc/eXsection/hXsection are not shown and physical fidelity/QW4 transport and trap net e/h recombination remain unvalidated. Header line7 labels PooleFrenkel and Thermionic motivated numerical proxies, not direct faithful validation.
- Official Sentaurus Training section 13 confirms PooleFrenkel field-enhanced emission and distinct eGapStatesRecombination versus hGapStatesRecombination outputs (https://ghzphy.github.io/Sentaurus_Training/sd/sd_13.html). Existing pp Plot saved eGap, not hGap; cannot claim net full trap contribution or validated IQE. No new simulation/edit. NEXT read-only `sed -n '1,48p;159,177p' pp25_des.cmd`, then exact T-2022.03 model interpretation and explicit limitations. Do not restart canceled hGap rerun.

## 2026-11-04 — Lee Wu SRH/trap accounting audit (DOCUMENTED older official guides; DERIVED conditional)
- Historical Synopsys User Guides O-2018.06 (SRH model chapter and Traps chapter) and K-2015.06 (heat/rate equation separates SRH net from electron/hole trap net terms), plus official training sdevice/13.9, establish SRH field and explicit trap e/h outputs as conceptually distinct. This is NOT verified against local T-2022.03 UG; that original manual is not hosted in GitHub. Wu pp21/n25 plotted eGap only, no hGap; cannot equate electron-only trap rate with net pair recombination without checking e/h steady-state balance and model options.
- Conditional 12-QW proxy at same 5V: OFF Rad/(Rad+SRH+Auger)=66.2156%; ON same 3 terms=66.2270%; ON adding eGapStates=66.0432% (-0.1724 percentage points vs OFF 3-term). These numbers are illustrative algebra, NOT validated IQE. Missing OFF full eGap, hole gap, non-QW contributions, exact matched-current comparison. No run/code edits. NEXT read-only inspect actual Wu complete Physics/Traps clauses and T-2022.03 documentation before using any trap-inclusive IQE claim.

## 2026-11-04 — Lee n25 ON 12-QW rate fields completed; 5V OFF/ON summary (OBSERVED/DERIVED)
- SVisual saved n25_des Trap ON, all 12 exact QW Clean/DmgL/DmgR regions for RadiativeRecombination (Total 9.869850e15), srhRecombination (6.086824e14), AugerRecombination (4.424524e15), eGapStatesRecombination (4.148388e13), all s^-1 um^-1, domain 1.199999e-01 um2. Earlier n21 OFF matched totals Radiative 9.902518e15, SRH 6.102184e14, Auger 4.442221e15. ON vs OFF changes: -0.329896%, -0.251713%, -0.398382% respectively. eGapStates n25 clean QW1..4 zero; QW1..4 respective shares 3.2802%, 3.3623%, 27.5257%, 65.8318%.
- Source: user SVisual screenshot measurements. All per-region numeric values in Lee TIMELINE and LIVE_STATE.json. No n21 full QW eGap rate integration; no validated trap-inclusive IQE, rate double count check, or whole-device rate accounting. No new run/source edits. NEXT verify eGap/SRH accounting from version-matched reference before any IQE claim. Canceled extra hGap run remains canceled.

## 2026-11-04 n21 QW SRH/Auger batching completed
- OBSERVED (이택규, saved n21_des): 12 exact QW regions SRH Total Integral 6.102184e14, Auger Total Integral 4.442221e15, earlier Radiative 9.902518e15 (all s^-1 um^-1). Derived QW4 share: SRH 80.10%, Auger 95.42%, Radiative 91.03%. Individual integrals in Lee TIMELINE and LIVE_STATE.json. No run/edit. NEXT switch once to n25 and repeat 12-region Radiative, SRH and Auger. These fractions are not IQE; missing hGap and rate accounting unresolved.

## 2026-11-04 — Lee n21 OFF RadiativeRecombination 12-region QW total (OBSERVED)
- Saved SVisual n21_des 5 V Trap OFF Field Integration exact Clean, DmgL and DmgR QW1–4 (12 non-composite regions). Observed total integral 9.902518e15 s^-1 um^-1; total domain 1.199999e-01 um2. Clean_QW4 9.005734e15; DmgL_QW4 4.466154e12; DmgR_QW4 4.465761e12. Derived QW4 total 9.014665915e15, share approx 91.0341% of all 12 selected region radiative integrals. QW3 share ~8.9475%. This is radiative spatial distribution, NOT IQE. Individual region integrals stored in Lee TIMELINE. No solver run or code edit. NEXT stay on n21 to batch the same 12 regions for srhRecombination, then AugerRecombination. Afterwards n25 and physical rate accounting.

## 2026-11-04 — Lee Wu n21 OFF DmgL_QW4 radiative integral recorded
- School SVisual screenshot: n21_des Trap OFF, RadiativeRecombination, DmgL_QW4 only, Integral 4.466154e12 [s^-1*um^-1], Domain 1.500003e-05 [um^2]. Existing n25 ON same field/region 4.297888e12. DERIVED (ON-OFF)/OFF = approx -3.77% at same 5 V, not full IQE. No new run or code edit. To reduce repetitive dataset switching, finish collecting needed n21 fields before n25. Suggested n21 exact QW region Radiative/SRH/Auger integrals (not merged '+' regions), followed by equivalent n25. Physical rate accounting/possible double counting and missing hGap remain UNRESOLVED.

## 2026-11-04 — Lee Wu n25 left-QW4 RadiativeRecombination (OBSERVED)
- SVisual screenshot of saved Trap ON n25_des at 5 V: DmgL_QW4 Field RadiativeRecombination integral +4.297888e12 s^-1 um^-1; Domain 1.500003e-05 um2. Previously same n25 region SRH +2.397133e11, eGapStates +1.365525e13 (integral units identical). Do not naively sum to IQE; rate field definition/overlap and hGap component remain UNRESOLVED. No rerun/code change. NEXT saved n21 OFF DmgL_QW4 RadiativeRecombination read-only, then official field accounting.

## 2026-11-04 — Lee Wu DmgL_QW4 SRH OFF/ON saved-field comparison
- OBSERVED (이택규 SVisual): n21 OFF srhRecombination DmgL_QW4 integral +2.450705e11 s^-1 um^-1, domain 1.500003e-05 um2; previously n25 ON same field/region +2.397133e11 s^-1 um^-1, same domain. DERIVED ON-OFF -5.3572e9 s^-1 um^-1 (~-2.19% versus OFF). The eGapStatesRecombination field rises strongly with Trap ON in the same region, but SRH/eGap double-count rules and missing hGap field prevent trap-inclusive IQE inference. No new simulation or code modifications. NEXT read-only official recombination rate accounting and existing saved radiative/auger fields; respect canceled hGap rerun.

## 2026-11-04 — Lee Wu ON DmgL_QW4 SRH rate field (OBSERVED)
- Saved n25_des SVisual `srhRecombination` Field Integration for DmgL_QW4 exclusively selected: Integral +2.397133e11 s^-1 um^-1, Domain 1.500003e-05 um2. Earlier same region n25 `eGapStatesRecombination` was +1.365525e13 s^-1 um^-1 (ratio 56.96, numerical only); rate-field overlap and correct trap-inclusive IQE accounting remain unverified. No new run/source edits. NEXT inspect saved n21 OFF `srhRecombination` same region, then confirm rate definitions before aggregating rates.

## 2026-11-04 — Wu QW4 left/right Trap OFF versus ON electron gap-state field now compared (OBSERVED)
- 이택규 SVisual screenshots: n21 OFF eGapStatesRecombination DmgL_QW4 integral 1.387832e-05 over 1.500003e-05 um2; DmgR_QW4 integral 1.387717e-05 over 1.500037e-05 um2. n25 ON left integral 1.365525e13, right 1.365435e13 with matching respective domains. Integrals in s^-1 um^-1. Bilateral sum OFF 2.775549e-05 versus ON 2.730960e13 (derived); no new run/edit. OFF is near numerical zero; do not use ratio as physical trap loss or IQE metric.
- This completes the selected QW4 electron-gap-rate field comparison only. Trap+SRH accounting, true IQE, all regions, current normalization, and physics fidelity remain unresolved. Next read-only investigate saved SRH/Radiative/Auger fields and official Sentaurus recombination definitions; do not rerun canceled hGap case.

## 2026-11-04 — Lee Wu n21 OFF DmgL_QW4 eGapStatesRecombination observed
- Worker 이택규; screenshot SVisual n21_des (Trap OFF), DmgL_QW4 only: Integral +1.387832e-05 s^-1 um^-1, Domain 1.500003e-05 um2. Compare saved n25_des (Trap ON) same region Integral +1.365525e13 s^-1 um^-1, same Domain. ON/OFF ratio approximately 9.84e17; OFF value nonzero, and this ratio is not an IQE or full trap nonradiative-loss measure. No new run, no edits. NEXT check OFF DmgR_QW4 read-only, then independently verify trap/SRH accounting.

## 2026-11-04 Lee Wu DmgL_QW4 eGapStates region integration (OBSERVED)
- Saved n25_des (Trap ON) SVisual screenshot: eGapStatesRecombination, DmgL_QW4 only; Integral +1.365525e13 s^-1 um^-1, Domain 1.500003e-05 um2. Earlier Clean_QW4 same rate integral=0. This proves nonzero electron gap-state recombination field integral in left damaged QW4, not full trap recombination or IQE. No rerun/edit. NEXT inspect DmgR_QW4 same field, then compare against saved OFF and establish rate accounting before IQE.

## 2026-11-04 — Lee Wu n21/n25 5.0 V PLT final-row current comparison (OBSERVED / DERIVED)
- Worker: 이택규. Direct school CMP_WU_Copy terminal evidence: `tail -n 12 n21_des.plt`, `tail -n 12 n25_des.plt`. Both files end at `time=1` and `anode OuterVoltage=5.00000000000000 V` with 17-column DF-ISE datasets including time and anode/cathode terminal values.
- OBSERVED OFF n21 (5 V): anode TotalCurrent=2.56859586549120e-03, eCurrent=1.69539310159551e-04, hCurrent=2.39905655533165e-03; corresponding cathode TotalCurrent=-2.56859586549119e-03.
- OBSERVED ON n25 (5 V): anode TotalCurrent=2.56639709344131e-03, eCurrent=1.68952709999954e-04, hCurrent=2.39744438344136e-03; corresponding cathode TotalCurrent=-2.56639709344130e-03.
- DERIVED: 5V fixed-voltage absolute TotalCurrent reduction OFF-ON=2.19877204989e-6, relative reduction 100*(OFF-ON)/OFF=0.085602%. Data are raw 2D PLT terminal-current numbers; physical current-density scaling/units not validated. 5 V near-equal current is not an exact matched-current extraction, and low total-current change does not validate IQE or trap-mediated recombination.
- PLT dataset list lacks recombination integrals (IntegrRad, IntegrSRH, IntegrTrap). Further rate accounting needs saved TDR and authoritative definitions. No new runs, no source edits. Respect JuSubin's cancellation of an overnight hGap rerun; next is read-only review of existing fields and recombination definitions.

## 2026-11-04 Lee Wu right Barrier4 observation
- User SVisual n25 ON TotalTrapConcentration, DmgR_Barrier4: Integral 3.996092e+01 um^-1, Domain 4.000092e-05 um2. Mean 9.990e17 cm^-3 (about 0.1 percent below ON nominal 1e18). Left Barrier4 had similar average. Representative QW1/QW4 left and right traps and clean QW centers had already been checked. This is not a complete IQE or full 22-region uniformity proof. No new runs or source edits. Next investigate recombination accounting and trap-inclusive IQE with saved data only.

## 2026-11-04 — Lee Wu n25 Clean_QW4 trap concentration zero (OBSERVED / DERIVED)
- Worker: 이택규. Screenshot of school saved `CMP_WU_Copy/n25_des` Field Integration, `TotalTrapConcentration`, only `Clean_QW4 (InGaN)` selected. Integral = **0.000000e+00 [um^-1]**; Domain = **2.997006e-02 [um^2]**. Regional mean = 0 cm^-3.
- Alongside previously measured `DmgL_QW4` mean=1e18 and `DmgR_QW4` mean=1e18 cm^-3, the measured **QW4 left-damaged / clean-center / right-damaged regional averages** match the intended ON trap placement. Earlier QW1 left/right and clean spot checks agree. Other damaged layers, within-region uniformity and full trap-inclusive IQE remain unverified.
- No school code edit or SDevice rerun. Next saved n25 `DmgL_Barrier4` and `DmgR_Barrier4` spot checks (if still needed), then focus on rate accounting, matched-current and model fidelity.

## 2026-11-04 — Lee Wu ON DmgR_QW4 trap density checked (OBSERVED / DERIVED)
- Worker: 이택규. Actual saved `CMP_WU_Copy/n25_des` SVisual Field Integration, Field `TotalTrapConcentration`, selected region `DmgR_QW4 (InGaN)`. Screenshot shows Integral=1.500037e+01 [um^-1], Domain=1.500037e-05 [um^2]. Mean = 15.00037 / 0.00001500037 = 1e6 [um^-3] = **1e18 cm^-3**, matching ON NtSide. Earlier DmgL_QW4 region also 1e18 cm^-3; both left and right QW4 regional averages verified. This does NOT establish uniformity inside each region, all 22 damaged regions, recombination loss, or trap-inclusive IQE.
- No rerun or school code edit. NEXT read-only `Clean_QW4` in same n25 TotalTrapConcentration to confirm clean center vs both sidewalls; then sample Barrier4 and review trap-rate accounting.

## 2026-11-04 Lee Wu left QW4 trap ON measurement (OBSERVED)
- User SVisual n25_des TotalTrapConcentration integration region DmgL_QW4 InGaN: Integral 1.500003e+01 um^-1, Domain 1.500003e-05 um2. DERIVED regional mean 1e6 um^-3 = 1e18 cm^-3 = ON NtSide setting. This validates the sampled QW4 left region mean, not full 22-region uniformity or trap-inclusive IQE. No rerun. NEXT right DmgR_QW4 and Clean_QW4 saved TDR.

## 2026-11-04 — Lee Wu n21/n25 runtime grid and doping reads confirmed (OBSERVED)
- Worker: 이택규, school `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`. Direct read-only `grep -niE 'n1_msh.tdr|reading grid|grid file|reading mesh' n21_des.log n25_des.log | head -n 30` supplied.
- Both `n21_des.log` and `n25_des.log` show at line 241 `Grid file: n1_msh.tdr`, line 697 `Reading grid 'n1_msh.tdr' ...`, and line 805 `Reading doping 'n1_msh.tdr' (TDR format) ...`. Thus BOTH solver logs confirm loading mesh and doping from the same *file pathname*. Prior `stat` showed mesh mtime 2026-11-03 23:17:11 before OFF/ON solver completions (23:58:02 / 2026-11-04 01:00:20); both log runs finished normally.
- CMD level: after run-output filename and intended Conc normalization, complete `pp21_des.cmd` vs `pp25_des.cmd` diff exit 0, `pp21_des.par` vs `pp25_des.par` byte cmp exit 0. This supports a controlled Trap concentration comparison. IMPORTANT: same pathname/mtime alone do NOT cryptographically prove identical runtime mesh byte snapshot if changed between starts. Physics validity, matched-current, and trap-inclusive IQE remain UNRESOLVED.
- No code changes or new solver runs; next read saved `n25_des.tdr` in SVisual and measure `TotalTrapConcentration` separately for `DmgL_QW4`, `DmgR_QW4`, `Clean_QW4`, and optionally `DmgL/R_Barrier4`. Record each Integral/Domain to calculate cm^-3. Preserve all files.

## 2026-11-04 — Lee Wu n21/n25 solver completion and mesh mtime validated (OBSERVED / read-only)
- Worker: 이택규. Actual school Bash command under `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`: `stat -c '%n | %s bytes | %y' n1_msh.tdr n21_des.log n25_des.log; grep -E 'Curve trace finished|Sentaurus Device simulation finished|Good Bye' n21_des.log n25_des.log | tail -n 10`.
- `n1_msh.tdr`: 984164 bytes, last modified 2026-11-03 23:17:11.223700114 +0900. `n21_des.log` 284309 bytes, mtime 2026-11-03 23:58:02.616861738 +0900. `n25_des.log` 441702 bytes, mtime 2026-11-04 01:00:20.441108178 +0900.
- `n21_des.log`: `Curve trace finished.`, `Sentaurus Device simulation finished (Date: Tue Nov 3 23:58:02 2026 (KST)).`, `Good Bye !`. `n25_des.log`: same three completion signatures, finished Wed Nov 4 01:00:20 2026 (KST). Confirms **both full solver runs terminated normally and curve traces finished**, not physical/LED or IQE validation, and does not prove actual final bias if log details not reread.
- Earlier full normalized `pp21_des.cmd` vs `pp25_des.cmd` diff=0 and `cmp -s pp21_des.par pp25_des.par` exit=0. Both effective CMDs name `n1_msh.tdr` as input grid. Mesh mtime precedes both completion logs, supporting common-source hypothesis, but **same exact mesh snapshot used at both execution instants is not proved by mtime alone**. Need mesh load/log evidence and provenance if necessary.
- No new simulation, no code or output modifications. Preserve both TDRs. NEXT: read-only grep n21/n25 log for mesh file load and grid/region warnings, then existing saved TDR field integration `TotalTrapConcentration` in QW4/Barrier4 (ON and OFF) before trap-inclusive IQE work.

## 2026-11-04 — Lee Wu n21/n25 parameter-file byte equality (OBSERVED)
- Worker 이택규; school directory `/user/semi/semi437/tmp/myproject/CMP_WU_Copy` in Bash, read-only command `cmp -s pp21_des.par pp25_des.par; echo "PAR_CMP_EXIT=$?"` returned **PAR_CMP_EXIT=0**. Thus full preprocessed parameter files are byte-identical in the observed school directory.
- Combined with earlier complete normalized `pp21_des.cmd`/`pp25_des.cmd` diff `CMD_DIFF_EXIT=0`, OFF/ON CMD and parameter content equivalence is supported, after excluding run-specific filenames and intentional trap Conc=0 vs 1e18 cm^-3. This is **not** yet the complete same-mesh-at-run-time or same-current validation.
- NEXT read-only: inspect `n1_msh.tdr` timestamps and n21/n25 completed logs, plus explicit same input grid file in pp; ensure no mesh regeneration between runs before considering controlled Trap study. No solver/code edits; trap-inclusive IQE remains UNRESOLVED.

## 2026-11-04 — Lee Wu OFF/ON pp21 vs pp25 partial diff (OBSERVED / PARTIAL ONLY)
- Worker: 이택규. User read-only command in school's `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`: `diff -u pp21_des.cmd pp25_des.cmd | head -n 120`. Because `head` truncated at 120 lines, this is ONLY a partial diff, NOT proof all differences are known.
- OBSERVED in shown diff: `Grid="n1_msh.tdr"` remains same in context; File output/current/log/parameter filenames differ as expected (n21 vs n25). Sampled trap-region blocks include same Acceptor Level FromValBand EnergyMid=0.75, eXsection=hXsection=1e-15, PooleFrenkel, with OFF `Conc=0` vs ON `Conc=1e18`. Previous full matching grep separately counted 22 identical-form concentration declarations in each preprocessed CMD.
- UNRESOLVED: remaining trailing pp command differences not seen due head truncation; pp21_des.par vs pp25_des.par not yet compared; equivalent mesh file pathname does not yet prove all run inputs/dates/conditions equal. Do NOT yet claim controlled one-variable experiment, calibrated IQE, or full trap validation.
- NEXT READ ONLY: perform normalized FULL pp cmd comparison (normalize only n21/n25 output file names, their pp parameter filenames, and trap Conc values) and then compare pp21_des.par with pp25_des.par; retain existing n21/n25 files and NO reruns.

## 2026-11-04 — Lee Wu n21/n25 effective command inspection (OBSERVED / read-only)
- Worker: 이택규, school terminal `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`; started a standalone `bash` after earlier tcsh shell quoting failure. Actual files OBSERVED: `n21_des.log` 278K (Nov 3 23:58), `n21_des.tdr` 7.2M (23:58), `n25_des.log` 432K (Nov 4 01:00), `n25_des.tdr` 7.6M (01:00); `pp21_des.cmd` and `pp25_des.cmd` both 5.6K, timestamps Nov 3 23:31 / 23:58. File existence does NOT independently prove clean solver termination; prior saved run summaries exist.
- User-provided `grep -nE` on actual preprocessed pp21/pp25: both line28 `Piezoelectric_Polarization(strain)` and line29 `IncompleteIonization(Dopants="MagnesiumActiveConcentration")`; both line219 `eGapStatesRecombination eTrappedCharge TotalTrapConcentration`. `hGapStatesRecombination` NOT in matching output. Both pp files have 22 trap `Conc=` statements (lines 38..206 step 8). OFF pp21 all `Conc=0`; ON pp25 all `Conc=1e18`; each shown with eXsection=1e-15 and hXsection=1e-15. Confirms **source declarations**, not all 22 resolved TDR regional concentrations. Prior TDR spot checks verified only ON QW1 left/right and OFF QW1 left.
- UNRESOLVED: a complete `diff -u pp21_des.cmd pp25_des.cmd` and pp21/pp25 par/mesh provenance were NOT yet checked; cannot claim NtSide is the sole effective difference. Missing hGap field, trap/SRH accounting, full IQE and current-density units remain unknown. No new TCAD run, source edit or saved TDR modification.
- NEXT READ ONLY: `diff -u pp21_des.cmd pp25_des.cmd | head -n 120`; then inspect pp21/pp25 `.par` and mesh lineage if differences imply more than Trap density. Never restart n21/n25 or n29 automatically.

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

## 2026-11-04 — JuSubin Wu postMgFix n25 ON 5V 12-QW Radiative integral OBSERVED; OFF/ON matched-voltage change DERIVED
- USER SVisual `CMP_WU_Copy/n25_des`, `RadiativeRecombination`, exactly same 12 2D regions (Clean_QW1–4,DmgL_QW1–4,DmgR_QW1–4) as earlier postMgFix OFF n21. Reported ON Total Integral **9.869850e15 [s^-1*um^-1]**, Domain **1.199999e-1 [um^2]**; printed region sum 9.8698494707962e15 (matches by rounding). OFF same regions Rad Total **9.902518e15**. Calculated ON−OFF = **−3.2668e13 [s^-1*um^-1]**, −0.3298959% relative OFF at **same 5V**. 5V raw anode total ON2.566e-3 vs OFF2.569e-3 (rounded logs, −0.1168%), so equal-V comparisons are not strictly equal injected current and cannot by themselves establish IQE loss.
- DERIVED per-well Rad, each Clean+L+R at 5V: QW1 OFF7.395981904e11, ON7.385600935e11 (−0.14036%); QW2 OFF1.0810392696e12, ON1.0669347027e12 (−1.30472%); QW3 OFF8.860310308e14, ON8.765896290e14 (−1.06558%); QW4 OFF9.014665915e15, ON8.991454347e15 (−0.25749%). Strong QW4 emitter remains in ON, but ON QW4 integrated Rad reduced slightly.
- DERIVED clean-only QW Rad OFF9.8926908197e15, ON9.8604079826e15 (−0.32633%); total Damaged L+R QW Rad OFF9.82676356e12, ON9.4414881962e12 (−3.92067%), ON damaged-QW Rad accounts ~0.09566% of ON total (OFF~0.09924%). The large percentage change within narrow damaged segments is not yet confirmed SRH trap effect or source of 0.33% whole-MQW emission change: true trap ON SRH/Auger and carrier/flux redistribution pending. Do NOT equate local Rad decrease with SRH increase; trap may change local injection and recombination.
- 5V OFF 3-channel model IQE 66.2156% from Rad9.902518e15/SRH6.102184e14/Auger4.442221e15. **ON IQE uncomputable until n25 same 12-region SRH and Auger integrals are supplied.** Need compare at matched injected current/J; 2D AreaFactor=1 observed, absolute normalization unverified; ON trap regions list partial.
- NEXT immediate ON `srhRecombination` integration identical 12 regions, then `AugerRecombination`. Preserve per-region numbers esp DmgL/R and contrast OFF QW SRH; calculate ON 3-channel IQE, SRH sidewall change, then evaluate matched-current and 2D normalization. No code modifications or new server run this turn.

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

## 2026-11-04 ~01:35 KST — JuSubin Wu MgFix n21 OFF SVisual central electron-density cutline (OBSERVED screenshot)
- SVisual `CMP_WU_Copy/n21_des`, Cutline C1 drawn along device depth X at lateral Y≈5 µm (full 10 µm mesa center). User now successfully restored curve and zoomed eDensity `eDensity(C1(n21_des))`; x-axis shown approximately 0–0.4 µm, Y1 logarithmic ~1e13–1e20 cm^-3. Four narrow sharp electron-density peaks around the MQW depth x≈0.12–0.17 µm are visible; some peaks approach order 1e20 cm^-3 on the screenshot.
- These peaks align qualitatively with QW layers but exact well assignments, point values, and QW4 carrier excess are NOT established without further x-axis zoom and region markers. Existing QW-integrated Rad (~91% QW4) and Auger (~95% QW4) warrant e/h spatial investigation; do not infer causation from eDensity screenshot alone.
- NEXT: further zoom eDensity X≈0.115–0.175 µm keeping density log axis; then inspect hDensity on same cutline and compare the four QWs. This is SVisual display interaction only; no code or new solver run.

## 2026-11-04 — 주수빈 Wu MgFix Trap OFF n21 5V MQW Auger 적분 및 IQE 산출 (OBSERVED + DERIVED)
- OBSERVED SVisual `CMP_WU_Copy/n21_des`, `AugerRecombination`, same 12 regions (`Clean_QW1-4`, `DmgL_QW1-4`, `DmgR_QW1-4`), 5V fresh post-Mg fix and `NtSide=0`. Total Integral **4.442221e15 [s^-1*um^-1]**, Total Domain **1.199999e-01 um^2**; sum of printed region numbers 4.44222133419256e15, agrees by roundoff. QW Auger sums: QW1 1.5457573904e11; QW2 1.4422855352e11; QW3 2.029537289e14; QW4 4.238968801e15. QW4 holds ~95.4245% of total Auger integral.
- Previous *same* 12 QW volumes: Radiative 9.902518e15 and SRH 6.102184e14 s^-1 um^-1 (reported totals). Sum of printed region values R_rad 9.90251758326e15, R_SRH 6.102184495823e14, R_Auger 4.44222133419256e15, all consistent by rounding.
- DERIVED 3-channel proxy IQE=SumRad/(SumRad+SumSRH+SumAuger)=**66.215619%**; channel shares Radiative66.2156%, SRH4.08038%, Auger29.7040%. QW1 IQE48.12954%; QW2 59.03277%; QW3 73.27482%; QW4 65.59746%. QW4 alone contributes **91.03408%** of all QW radiative, **95.42453%** Auger and **91.89194%** of QW total 3-channel recombination. QW3 highest per-well IQE although QW4 dominates volume-integrated emission. `Clean` overall IQE~66.21561% and side-region `DmgL+R` IQE~66.22882% at trap-OFF (very similar; not a trap-effect comparison).
- Numerical *model* 5V IQE metric only: not physical LED/Wu-paper calibrated proof. The 3-channel formula assumes these simulated terms exhaust the desired QW recombination budget and that their rates/signs correspond. Strong QW4 localization may reflect uneven carrier injection/field/crowding; cause not yet verified. Absolute J unverified (2D current native units/AreaFactor/width), and high 5V injection can exaggerate Auger. IMPORTANT old pre-Mg trap-ON n25 cannot serve as controlled comparator; only new post-fix ON run after OFF check.
- NEXT: inspect QW1–4 center/edge `eDensity`/`hDensity` cutlines and local recombination rates, verify 2D AreaFactor and native J for 5V (and consider representative matched operating current), crosscheck Wu2023 published structure/model. Then rerun fixed-Mg NtSide1e18 Trap ON to verify loss at matched J. No new school simulation or code edits in this observation turn.

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

## 2026-11-04 — JuSubin Wu MgFix NtSide=0 n21 5V solver CONFIRMED (OBSERVED USER n21_des.log)
- Final accepted t=1 / 5.000V, Newton error 6.9604e-01, anode electron1.695e-4, hole2.399e-3, total2.569e-3 RAW (hole fraction~93.4%); cathode total-2.569e-3. `Curve trace finished`, `Writing plot 'n21_des.tdr' ... done`, `simulation finished` Tue Nov3 23:58:02 KST, wallclock1589.90s. Older 4.332V tail was incomplete snapshot and superseded.
- The prior SVisual pGaN acceptor/hole/electron maps and MQW radiative and SRH maps corroborate restored carriers and nonzero recombination, but **QW-integrated IQE and actual 2D current density still UNRESOLVED**. Old pre-Mg ON n25 results cannot be compared to this corrected OFF run.
- NEXT QW1-4 Clean/Dmg integral Radiative/SRH/Auger at 5V and QW carrier profiles; verify J normalization and Wu paper fidelity; then **new** fixed-Mg ON n25 NtSide=1e18 matched-current comparison. No new source edit or simulation initiated by ChatGPT.

## 2026-11-04 ~00:55 KST — Wu MgFix OFF n21 TDR acceptor holes electrons radiative observed (OBSERVED, numerical final log and rates pending)
- OBSERVED user SVisual screenshots of post-MgFix CMP_WU_Copy/n21_des.tdr: top pGaN AcceptorConcentration red, legend max 2.000e19 cm^-3 (old pre-fix SDevice acceptor=0). Global hDensity max 1.16504e20 cm^-3, eDensity max 1.35933e20 cm^-3. These are global extrema, not QW-specific averages.
- RadiativeRecombination global legend maximum 3.43425e29 cm^-3 s^-1 with strong thin red stripes in MQW toward x≈0.15–0.165um (lower wells); visually nonzero QW radiative recombination is confirmed but per-QW rates/IQE and uniformity are NOT. Color scales may be nonlinear; large peaks should be interrogated using regionwise integration.
- Interpretation: SDevice Mg acceptor recognized and carrier populations increased after mapping fix. Still NO proof of quantitatively calibrated LED or Wu paper reproduction, no QW regional rate integrals, final 5V terminal log absent. NEXT inspect final newly dated n21_des.log and 5V contact components; then QW1–4 e/h cutlines and Clean/Dmg QW region integrals Rad/SRH/Auger, current normalization, baseline validation before ON n25.

## 2026-11-04 ~00:47 KST — Wu MgFix OFF n21 SVisual full 0-5V IV curve observed (OBSERVED SVisual curve, final log pending)
- 주수빈 reports post-MgFix clean n21 NtSide=0 simulation finished; SVisual BaselineData_22 plot shows I–V extends ~0 to5V and sharp rise after ~3.2–3.4V, endpoint visually ~2.6e-3 on 'Anode Current [A/um] (assumed)' axis, with calculated/assumed current density plot ~2.5e4 A/cm2 (NOT validated normalization). Previous running n21 4.332V directly confirmed hole-dominated anode current.
- This plot is a useful advancement but NOT yet authoritative final solver convergence: check new n21_des.log for 5V exact terminal currents, 'Curve trace finished' and date, then n21_des.tdr pGaN acceptor/free holes and QW bipolar injection/radiative/SRH/Auger. Current blocker QW emission/IQE; ON n25 not yet to run; keep old backups.

## 2026-11-04 — Wu post-Mg n21 advanced to 4.332V and hole current restored (OBSERVED SOLVER PROGRESS, 5V NOT YET VERIFIED)
- OBSERVED user live shell tail post-Mg CMP_WU_Copy/n21_des.out/.log: earlier Newton step backtracking at t≈0.64 was recovered. Converged step at t=0.866477, anode=4.332V with Bank/Rose error=0.24308 (<1), after 3 Newton iterations. Terminal RAW currents anode electron +7.286e-05, hole +1.415e-03, total +1.488e-03; cathode total -1.488e-03. Hole fraction of anode total ≈95.1%, distinctly unlike old pre-fix 5V hole3.696e-27 and electron2.884e-05; voltages differ, so do NOT infer an improvement factor or match-current comparison. These terminal components alone do not prove QW hole density or radiative recombination.
- SDevice then attempted t=0.866477→0.886477 (nominal 4.432V); only Newton iterations0–3 were shown, no convergence outcome for that step. Full 5V run still NOT confirmed. The .err tail reports InGaN eDOSMass/hDOSMass computed via GaN/InN side materials, likely interpolation notices rather than a new fatal event; earlier datexcodes variable redefined warnings remain to classify separately.
- NEXT: keep current n21 solver running if advancing; monitor date and 5V final convergence, do not edit active files or start n25. When done inspect SDevice pGaN AcceptorConcentration/free hDensity, QW1–4 electrons/holes and radiative/SRH/Auger; preserve pre-Mg n21/n25 backups.

## 2026-11-04 ~00:43 KST — Wu post-Mg SDevice n21 Newton step reduction screenshot (OBSERVED, SOLVER RUNNING)
- User SWB screenshot of new post-Mg n21 SDevice: Newton step exceeds 35 iterations at one step and retreats to smaller quasistationary step (t=.637961→.642158, step=.004197); current iterations show large error ~3.44e3. This is local Newton convergence failure/backtracking, no final job failure or new 5V result yet.
- Error pane contains 'datexcodes.txt ... variable ... redefined' warnings (Mg and nSilicon species) consistent with copy of full GaN example mapping alongside built-in defaults; causality not established. SDE pGaN negative net doping is already observed; SDevice bipolar injection still unverified.
- NEXT immediate read-only live n21_des.out/.err/.log and assess whether t advances/stepsize collapses; if failure confirmed, diagnose runtime mapping collisions and solver; do not modify running files or n25.

## 2026-11-04 — Wu2023 pre-fix n21 n25 SDevice output backup verified (OBSERVED, SDEVICE NEXT)
- User ls output verifies CMP_WU_Copy/preMgFix_SDevice_backup contains pre-fix n21 and n25 des log/plt/tdr pairs (six files totaling ~15MB). SDE Mg acceptor net doping fix previously visually confirmed in new n1_msh.tdr (pGaN≈-2e19 vs old zero; nGaN≈+5e18). No post-fix SDevice run evidence yet.
- CURRENT BLOCKER: free holes and QW radiative/SRH after Mg fix not verified. NEXT: n21 OFF SDevice only, inspect log and fresh AcceptorConcentration/hDensity/QW carrier+rate; n25 ON stays unrun pending clean validity.

## 2026-11-04 ~00:09 KST — Wu2023 SDE pGaN negative net doping verified after local Mg map (SDE OBSERVED, SDEVICE BLOCKER PERSISTS)
- SVisual screenshot n1_msh DopingConcentration after user SDE rerun with local datexcodes Mg acceptor mapping: top pGaN visually ≈-2e19 cm^-3 (blue scale min), bottom nGaN ≈+5e18 cm^-3 (red max). This closes mesh-stage Mg recognition blocker; former pGaN signed net doping≈0 was incorrect. Free-hole density and SDevice p-injection are NOT established by signed net doping.
- Most recent actual work: project-local Mg acceptor map and original mesh backup present, SDE rerun user-reported, fresh mesh doping directly visually inspected. Current blocker: post-fix OFF SDevice acceptor/hDensity/QW carrier+rate verification (old 5V n21/n25 results were pre-fix). Next backup old n21/n25 output before any SDevice reruns, then run OFF-only clean n21 against refreshed mesh, not ON n25; preserve Wu2023 epitaxy/physics.

## 2026-11-04 — Wu2023 SDE rerun user-reported after local Mg datexcodes (USER-REPORTED SDE EXECUTION; PHYSICS UNCONFIRMED)
- User reports SDE fully rerun after creating project-local CMP_WU_Copy/datexcodes.txt with uncommented MagnesiumConcentration acceptor mapping. Only report is available; no SDE log or fresh n1_msh signed DopingConcentration verified. Original SDevice 5V results remain not electrically validated.
- NEXT: open fresh n1_msh.tdr in SVisual and inspect pGaN signed DopingConcentration and nGaN positive doping; if pGaN zero inspect actual working-dir mapping/source chemical vs active species; if negative then check new SDevice OFF acceptor and holes before ON. Do not claim fixed until observed.

## 2026-11-04 — Wu2023 project-local Mg acceptor map and mesh backup verified (OBSERVED, MESH FIX NOT YET VERIFIED)
- In school CMP_WU_Copy the user verified datexcodes.txt 3.5 KB with lines35–39 active Mg chemical→active→ionized doping=acceptor for GaN, and backup n1_msh_before_MgFix.tdr 962 KB. This verifies local mapping content and backup, but NOT that SDE/SWB loads it.
- Next SDE mesh-only run then check pGaN DopingConcentration <0 and nGaN ~+5e18; SDevice 5V OFF/ON not to be run until validated; prior n21/n25 output preserved. School simulation no new execution in provided log.

## 2026-11-03 — Wu2023 school SDevice IncompleteIonization switch matches Mg Species (OBSERVED; MG ACCEPTOR BLOCKER PERSISTS)
- School pp21_des.cmd Physics includes IncompleteIonization(Dopants="MagnesiumActiveConcentration") line29 and File Parameter="pp21_des.par" line16. Actual pp21_des.par GaN Ionization Species("MagnesiumActiveConcentration") E0 0.15, alpha0, g4. Therefore switch/species are aligned; missing switch is ruled out.
- School pp1_dvs.cmd applies MgActive2e19 in pGaN. Installed default lib/datexcodes ordinary Mg acceptor mapping commented; project/home local overrides not present at tested paths; mesh net doping 0 and SDevice acceptor0. Isolated project-local datexcodes mapping remains next test. No code/run change; 5V terminal current does not validate LED emission.

## 2026-11-03 — Wu2023 pp21_des.par Mg ionization species confirmed (OBSERVED, physics fix pending)
- Actual school CMP_WU_Copy/pp21_des.par grep shows Material="GaN" Ionization Species("MagnesiumActiveConcentration") E_0=0.15 alpha=0 g=4. E0 is generic III-N setting, not confirmed Wu parameter. This sets ionization parameters but does not activate Mg dopant acceptor mapping.
- Actual school's pp1_dvs.cmd MgActive2e19 and default installed lib/datexcodes Mg chemical→active acceptor link commented out; pGaN net doping0 and SDevice acceptor0 persist. NEXT: verify pp21_des.cmd Physics IncompleteIonization and test a project-scoped Mg acceptor mapping in isolated SDE mesh, validate negative pGaN signed net doping BEFORE re-running 5V. No code/run modification.

## 2026-11-03 — Wu2023 school pp1_dvs MgActive-only confirmed (OBSERVED; no fix/run yet)
- Actual school /user/semi/semi437/tmp/myproject/CMP_WU_Copy/pp1_dvs.cmd grep: PMgActive 2e19, 'place-field ... MagnesiumActiveConcentration' only; pGaN assigned. Installed default T-2022.03 lib/datexcodes.txt Mg acceptor declaration commented out, official GaN_AlGaN_Polarization example enables Mg acceptor mapping, and no datexcodes present at school project root or home.
- n1_msh pGaN MgActive=2e19 but net DopingConcentration~0, SDevice AcceptorConcentration=0/hDensity near0. Mg mapping root cause very likely, but actual runtime overrides and ionization par require check. Existing 5V n21/n25 solver runs numerically completed, physical validation still blocked.
- NEXT: inspect actual school pp21_des.par species, add controlled project-scoped mapping in separate copy after runtime resolution check; re-mesh signed negative pGaN net doping before OFF SDevice; preserve 5V prior outputs. No file or solver edit in user session.

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

## 2026-11-03 22:02:35 KST — Wu2023PHY CMP_WU_Copy clean n21 5V SDevice FINISHED (OBSERVED USER LOG; physical LED not validated)
- USER-PROVIDED school `/user/semi/semi437/tmp/myproject/CMP_WU_Copy/n21_des.log` final tail: Quasistationary t=0.982621 -> 1.000000, final anode=5.000E+00 V, cathode=0V. Final Newton Bank/Rose error=2.0186E-01 (<1), `Curve trace finished.`, `Writing plot 'n21_des.tdr' (TDR format) ... done.`, Sentaurus Device simulation finished (Tue Nov 3 22:02:35 2026 KST), wallclock460.97s, CPU460.19s, peak memory765MB; hetero/traps/device licenses returned.
- FINAL terminal raw components: anode electron=+2.884E-05, hole=+3.696E-27, total=+2.884E-05; cathode electron=-2.884E-05, hole=+7.591E-36, total=-2.884E-05. Previous accepted step 4.913V anode I=2.780E-05, hole=2.534E-27. 2D raw current units and `AreaFactor` NOT independently confirmed; do not label as 3D amperes or A/cm².
- Comparison: old Wu10 (distinct pilot physics) 5V NtSide0 raw current 3.025E-29; strong raw current change on new candidate, but models, species, polarization, par, traps and transport all changed concurrently. **Cannot attribute causal improvement or claim reproduction/Wu physical baseline.** Mark **numerical clean 5V sweep and TDR confirmed**, **physical device calibration UNRESOLVED**.
- Dominant electron terminal current, near-zero hole terminal current at anode/cathode remain a RED FLAG, though terminal current partitions do NOT prove QW hole density=0. Examine saved n21_des.tdr pGaN `AcceptorConcentration`/`hDensity`/hole quasi-Fermi, QW1–4 `eDensity/hDensity`, conduction/valence bands and `RadiativeRecombination`, `SRHRecombination`, `eGapStatesRecombination`. Inspect Mg ionization/material species and electrodes; inspect C/V-I raw normalization before J. Do NOT run NtSide ON or freeze baseline solely on total I. No code change.

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

## 2026-11-03 — Wu2023PHY direct Vstop=5 run attempted; SWB ERROR reported (UNRESOLVED)
- User stated standalone 0.1V too slow, chose Vstop5 and launched; afterward supplied error screenshot. The exact error text, node, SWB PP and log not available here, so **DO NOT CLAIM WHAT FAILED OR THAT A FIX IS APPLIED**.
- Current independent GitHub source `CMP/tcad/candidates/CMP_BASELINE_3.2.0_WU2023PHY` unchanged; earlier parent and prior Wu10 5V n21/n25 outputs preserved.
- Need recent affected school `n*_des.log`, `n*_dvs.log`, `n*_msh.log` and `pp*_des.cmd/.par`. Stop further reruns until actual first error identified. 0→5V ramp does not skip 0.1V region.

## 2026-11-03 — Wu 2023 physics-first candidate SOURCE CREATED on GitHub (PROPOSED / NO SCHOOL RUN)
- **New source:** `CMP/tcad/candidates/CMP_BASELINE_3.2.0_WU2023PHY/` (SDE/SDevice/par/SVisual1/README), parent 3.0.0 unchanged, separate 3.2.0 version. Full Sentaurus T-2022.03 compile/run NOT performed.
- **Paper-grounded inputs:** W10um, nGaN3.9um Si5e18, 4x In0.08GaN QW3nm with 8nm GaN barriers, Mg nominal2e19, bilateral 5nm acceptor trap strips; piezo, Mg incomplete ionization, field-related trapping, radiative/SRH/Auger.
- **New code:** p input 2e19 `MagnesiumActiveConcentration` (nominal substitutional **assumption**, not real holes), explicit nSi donor species, `IncompleteIonization`, full piezo (crystal axis orientation from separate par), `Thermionic` and `PooleFrenkel` as **NOT-paper-verified proxies**, `TrapEt/SigmaN/SigmaP` SWB parameterization.
- **Blockers:** no Fig1 verification for EBL/pGaN thickness/contact; Mg species+ionization, c-axis polarity and MaterialDB untested; PF model != verified Wu method; actual clean 5V injection unknown. Old Wu10 n21/n25 saved logs only, no new SWB changes.
- **NEXT:** new independent SWB project, mesh/PP/par/Mg-acceptor gate → clean low bias/5V QW carriers/bands/injection → Trap ON at matched current; preserve all older runs.

## 2026-11-03 — CORRECTION: Wu (2023) paper-only baseline implementation (user confirmed, source checked)
- **CORRECTED SOURCE:** Zhuang Wu et al., *Physical mechanisms on the size-effect in GaN-based Micro-LEDs* (2023), DOI 10.1016/j.micrna.2023.207542; ignore erroneous different-paper-based implementation assumptions in earlier entries.
- **VERIFIED PUBLISHER EXCERPT:** 10um, nGaN3.9um Si5e18, four In0.08 InGaN QWs 3nm, GaN QB8nm, pGaN Mg doping2e19 chemical, sidewall acceptor traps within 5nm; physical models piezoelectric polarization, Mg incomplete ionization, field-related trap capture, Rad/SRH/Auger. EBL status unresolved in accessible excerpt; MUST inspect Fig1 before modifying.
- **USER GOAL:** independent Wu2023 baseline, not reusing old V2 assumptions to avoid prior issues.
- **CURRENT CODE DIFFERENCES:** PolAct0 and omitted Mg incomplete ionization; MgActive3e17 pilot, EBL0 as unverified pilot, blanket ohmic contacts. 5V Wu10 OFF/ON numerical completion stands; very small current physics unresolved.
- **NEXT:** preserve existing results, inspect TDR and actual PP/materials, check Wu2023 Fig1/parameters, prepare isolated Wu-only source-correct model once evidence is sufficient. No school code changed.

## 2026-11-03 21:00:31 KST — CMP_WU OFF+ON 5V both actual solver logs verified (OBSERVED)
- **Direct school runtime evidence:** user pasted `n21_des.log` tail for Wu10 clean `NtSide=0, PolAct=0, Vstop=5`. At `5.000E+00 V` anode electron `2.596E-29`, hole `4.286E-30`, total `3.025E-29` (log raw current units), cathode total `-3.025E-29`. Final solver `Error smaller than 1` (1.1212E-12), `Curve trace finished`, `n21_des.tdr` written, simulation finished Tue Nov 3 21:00:31 KST, wallclock 56.91 s, CPU 56.80 s, peak 638 MB. SDevice licenses returned.
- **Matched-V comparison with prior directly verified n25 Trap ON (1e18):** 5V ON anode total `5.810E-19` (electron `1.722E-29`, hole `5.810E-19`), cathode `-5.810E-19`, finished 20:58:41 KST, wallclock 361.62s, peak 640MB. Conditional same-voltage I_ON/I_OFF ≈ `1.921E+10`, but both tiny currents and OFF numerical floor make this **not interpretable as calibrated sidewall LED performance**. Hole component ON/OFF ≈`1.356E+11`, electron ON is ~0.66× OFF. Terminal composition alone doesn't prove QW carrier absence.
- **Status:** BOTH 0→5V forward `PolAct=0` Wu10 SDevice numerical sweeps confirmed complete; earlier SVisual1 both plotted. NOT a physically verified LED baseline, matched-current sidewall reduction, IQE, or Wu replication. Known potential injection/model issue (pilot Mg/EBL/contact, PolAct0), and 2D current A/um, AreaFactor/width normalization still conditional.
- **NEXT:** preserve both `n21_des.tdr` and `n25_des.tdr`. Inspect **same 5V data** in SVisual for `eDensity`/`hDensity`, `ConductionBandEnergy`/`ValenceBandEnergy` through p-GaN → MQWs → n-GaN, and spatial QW `RadiativeRecombination` / `SRHRecombination` / `eGapStatesRecombination`; inspect near-zero-V ON spike separately from `.plt`. Do not run more Vstop or modify physics before diagnosing existing output. Check raw 2D unit & AreaFactor before publishing any J.
- **No school SWB/deck changes** occurred in this ChatGPT turn; evidence is the user's exact pasted logs.

## 2026-11-03 — CMP_WU n25 5V ON SDevice confirmed complete
- OBSERVED user n25_des.log: NtSide1e18, PolAct0, Vstop5 reached 5.000V, anode I_total=5.810e-19 raw (electron1.722e-29; hole5.810e-19), cathode I_total=-5.810e-19. Final Newton converged, Curve trace finished, n25_des.tdr saved; runtime 361.62s wallclock, 640MB peak, ended 2026-11-03 20:58:41 KST.
- Numerical ON run completed, **not** validated working LED: current tiny, postprocess J/A/um convention unverified, physical pilot PolAct0/Mg/EBL/contacts unresolved. NEXT: clean5V n21 log tail and TDR carrier/band/QW check; do not alter decks before evidence.

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

## 2026-11-03 — JuSubin Kou paper-size correction / 20um 3D SDE candidate (CODE COMMITTED / NOT RUN)
- Previous `CMP_BASELINE_3.1.0_KOU4FULL` using CMP4um/5nm is NOT Kou-paper geometry; leave files unchanged for separate CMP4 target only. Paper actually simulates 20,60,100um square and 4um sidewall damaged ring; smallest clean core =12×12/20×20=36%.
- New original source `CMP/tcad/candidates/CMP_BASELINE_4.0.0_KOU20FULL3D/sde_dvs.cmd` + README: 3D Full square, 4um border, 4nm? **CORRECT QW=3nm** ×4 In0.15GaN, 22nm QB, EBL26nm pAl0.15, pGaN120nm, p+20nm, nGaN4um Si5e18. 5QB assumed; total depth4.288um. 117 cuboids. Code-only, no SDE mesh, simulator or solver output.
- UNRESOLVED paper reproduction: pPlus Mg input1e19 is PILOT; p-layers specified as hole 3e17 (not Mg chemical); top/bottom full Ohmic pilot not paper 4um p-contact; quantum physics/traps absent and old Kou4 SDevice incompatible.
- NEXT JuSubin: new SWB Kou20 SDE-only preprocess & mesh, region/contact and 3D resource audit; compatible SDevice only after gate.

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

## 2026-11-03 ~17:43 KST — JuSubin Wu10 Full2D **CODE CREATED** (GitHub confirmed), SDE/SDevice NOT RUN
- **Worker:** 주수빈. New independent original code candidate `CMP/tcad/candidates/CMP_BASELINE_3.0.0_WU10FULL` with `sde_dvs.cmd`, `sdevice_des.cmd`, `README.md` actually committed in GitHub. Width10µm, nGaN3.9µm, 4×In0.08 QW3nm + 5×GaN QB8nm, dual5nm Dmg regions; NtSide/PolAct/Vstop SWB parameterized.
- **STATUS:** CODE CREATED / PROPOSED only, no server preprocessing, SDE mesh, SDevice execution, calibration or Wu replication. All pGaN/EBL/contact/Mg-active/trap assumptions explicitly provisional; `PolAct=0, Vstop=0.1` is low-voltage smoke-only.
- **JuSubin NEXT:** new independent SWB project from scratch -> SDE-only build and effective PP/mesh/contact/composition audit; stop if any geometry/syntax discrepancy. No common Baseline4µm/5nm replacement or interruption of Lee's POL0 read-only gate; earlier physical B/FREEZE HOLD remains.

## 2026-11-03 — Claude independent review received: provisional Baseline B, Project A CONDITIONAL GO (USER-FORWARDED ANALYSIS, NO RUN)
- 이택규가 Claude PolAct=0 독립 검토를 전달. Claude reports read GitHub main `817fa2d` (11/03 10:08 KST) and Issue #7 latest; Claude's own push denied. GPT received the text, but did not independently inspect Claude's private chat or new TCAD data. **Verbatim TIMELINE entry**: `CMP/members/LeeTaekGyu/TIMELINE.md`.
- **Underlying observed data:** same-3.6V PolAct0.5→0 raw currents 131.8× OFF / 492.6× ON; PolAct0 QW4 share OFF 99.88898644%, ON 99.96413545%. Strict single-variable causality **UNVERIFIED** because full SDevice manually pasted and preprocessed command/par/mesh equivalence not checked.
- **Claude interpretation only:** polarization strongly impacts transport/Vf proxy, QW4-only-polarization H1 weakened. Classical DD (no quantum correction), ~3nm well / hypothesized ΔEc~0.41eV electronic capture H2 plausible but NOT directly established. Claimed J≈240/227 A/cm2 depends on conditional 2D width mapping, not 4um pixel calibration. Earlier 1%/80%/±25% thresholds are heuristic, not physical cutoffs.
- **Decision/recommendation:** continue physical Baseline verdict **B / FREEZE HOLD**, use `PolAct=0.5` only as a *provisional* comparator; **Project A CONDITIONAL GO for deck preparation**, not validated physics/claims. For actual A results: read-only exact deck/mesh diff gate, matched-current Trap loss under PolAct0.5 vs 0 (same sign, Claude-proposed ±25% tolerance), and limitations reporting. No user's final GO adoption reported.
- **NEXT FIRST READ ONLY:** `md5` of compared mesh, `pp1_dvs.cmd` diff, `pp2/pp6_des.par` diff, `pp2/pp6_des.cmd` diff `-w -B` in Bash. Then, if clean, PLT matched-I `polact_compare.py`. No new simulation; optional band-offset sensitivity later only with approval. Same-voltage Trap 3.3% vs ~34% is NOT matched current. No TCAD code edited.

## 2026-11-03 — PolAct=0 both PLTs parsed: QW4 still >99.88% while current rises strongly (OBSERVED + DERIVED)
- **작업자:** 이택규. **Source:** user pasted real Bash/Python DF-ISE `n2_des.plt`/`n6_des.plt` final-row extraction in `/user/semi/semi437/CMP_BASELINE_2.1.0_POL0NOSHELF` (2026-11-03, pp previously verified `activation=0`, global Iterations12, both runs finished). Final `anode OuterVoltage=3.600000 V` for both.
- **OBSERVED PolAct=0, Trap OFF n2:** native anode current `4.80713937e-06`; total QW integrated radiative rates: QW1 `7.53686944e18`, QW2 `4.48979847e20`, QW3 `1.98055890e22`, QW4 `1.82316579e25`; QW4 fraction `99.88898644%`.
- **OBSERVED PolAct=0, Trap ON n6:** native anode current `4.54183989e-06`; rates: QW1 `4.28900936e17`, QW2 `5.25004116e19`, QW3 `5.92590845e21`, QW4 `1.66646275e25`; QW4 fraction `99.96413545%`.
- **OLD OBSERVED reference:** original PolAct=0.5 3.6V n2 current `3.64728524885323e-08`, QW4 share `99.96877481383976%`; n6 current `9.21970771341943e-09`, share `99.99294273758203%` (prior 2026-10-31 PLT audit).
- **DERIVED at same voltage, NOT matched current:** change QW4 share n2 `-0.07978837384 percentage points`, n6 `-0.02880728758 pp`; current ratios n2 `131.8004774×`, n6 `492.6229802×`. Formula QW4 share = 100×QW4 Rad / sum(QW1..QW4 Rad). PolAct=0 changes total transport/current dramatically yet QW4 radiative localization remains >99.88%: simple 'polarization-only' cause is **not supported** as sole explanation. NOT proof of classical-DD capture as root cause, since local QW1 JnX/J and matched-current distribution not yet assessed.
- **INTERPRETATION LIMITS:** `strain activation=0` is global (including EBL) and not a physical baseline. Old/new are same-V, very different-I; raw 2D current not independently calibrated as square-pixel A/cm². QW4 fraction ≠ IQE. Need fresh shelfless geometry, SDE/par/mesh, source/PP diff except polarization verified before claiming a strict one-variable sensitivity. Physical Baseline B/FREEZE HOLD; no device code changed.
- **NEXT priority:** using existing PLT histories, compare QW shares and IQE_sim proxy at **matched anode current** where interpolation overlap exists, plus verify geometry/input provenance. If no current overlap, state cannot compare. No further blind re-runs.

## 2026-11-03 — POL0NOSHELF n2/n6 both finished; PolAct=0, global Iterations=12 confirmed (OBSERVED)
- **Worker:** 이택규, school-server output in `/user/semi/semi437/CMP_BASELINE_2.1.0_POL0NOSHELF`. `n2_des.log` tail shows `Sentaurus Device simulation finished (Tue Nov 3 01:52:08 2026 KST)` and `Good Bye!`. n2 wallclock=9809.91s (2h43m29s), peak memory=2.41GB. Prior user output confirmed n6 `Curve trace finished`, `Sentaurus Device simulation finished (Tue Nov 3 04:38:53 2026 KST)` and `Good Bye!`. Both `n2_des.plt` and `n6_des.plt` exist.
- **Effective input OBSERVED:** `pp2_des.cmd:22` and `pp6_des.cmd:22` `Piezoelectric_Polarization(strain activation=0)`. Both lines 175 `Iterations=12`, independent initial Coupled scopes lines 182 (`Iterations=200`) and 183 (`Iterations=100`) unchanged. This resolves previous n2-finished and effective-PolAct uncertainties.
- **Remaining verification:** successful termination ≠ proven 3.6V bias achieved or physical model validity. Fresh mesh `Wshelf=0` and original-vs-copy source/PP equivalence except activation unverified; no new QW-specific Rad integrals or same-current IQE_sim. Comparing `PolAct=0.5` old QW4 shares n2 99.9687748%, n6 99.9929427% to PolAct=0 new values is next. Global PolAct test also affects EBL (not pure MQW polarization). Physical Baseline B / FREEZE HOLD.
- **NEXT:** read-only `grep`/PLT parse confirm actual final anode voltage/current and QW1–4 Rad per n2/n6, then compare QW4 fractions at same terminal current where possible; never label QW4 fraction itself as IQE. Avoid changing original source.

## 2026-11-03 — PolAct=0 POL0NOSHELF n6 finished; n2 output exists (OBSERVED terminal, NOT YET VALIDATED n2)
- 작업자: 이택규 / AI: ChatGPT. 학교 서버의 실제 디렉터리 `/user/semi/semi437/CMP_BASELINE_2.1.0_POL0NOSHELF`를 `find`로 확인한 뒤 해당 디렉터리에서 출력 확인.
- **OBSERVED:** `n2_des.log` 338K (2026-11-03 01:52), `n2_des.plt` 293K (01:52); `n6_des.log` 340K (04:38), `n6_des.plt` 293K (04:38), 모두 실제 `ls -lh`에 존재. `n6_des.log`는 `Curve trace finished.`, `Sentaurus Device simulation finished (Date: Tue Nov 3 04:38:53 2026 KST)`, `Good Bye!` 출력으로 solver 정상 종료 직접 확인.
- **UNRESOLVED:** `grep ... | tail -25`는 n6 최후 부분만 보여 `n2`의 정상 종료를 입증하지 않음. 두 노드 최종 전압 3.6V/전류/재결합 및 실제 pp `activation=0`, `Iterations=12`, 메시 `Wshelf=0`, 원본과 단일변수 일치 모두 검증 전. n6 완료는 물리적 타당성 검증 완료가 아님.
- **NEXT READ ONLY:** `tail -n 12 n2_des.log; tail -n 12 n6_des.log; grep -nE 'Piezoelectric_Polarization|Iterations[[:space:]]*=' pp2_des.cmd pp6_des.cmd` 확인. 이후 원본 PolAct=0.5와 비교해 QW1–4 Rad share, 단자 전류 및 가능한 동일 전류 재결합 비율 평가. Common Baseline physical B/FREEZE HOLD; 서버 원본 소자 무변경.

## 2026-11-02 — Lee confirms full SDevice paste into shelf-free clone (USER-REPORTED, NO RUN VERIFIED)
- 이택규가 이번에는 `CMP_BASELINE_2.0.0_V2`(shelf-free, NOT `_Copy`)를 복사한 뒤 SWB `PolAct=0`으로 바꾸고 GPT가 제공한 **전체 SDevice 코드**를 새 복사본에 붙여넣었다고 확인. 이 변경은 **사용자 보고 완료**, 실제 서버 복제본 디스크의 저장본, 정확한 SWB 새 이름 및 pp 결과는 아직 직접 열람하지 않음.
- 제공 코드의 의도: `Piezoelectric_Polarization(strain activation=@PolAct@)`, Math global `Iterations=12`, 기타 Physics/Trap/CurrentPlot/Solve 원본과 같은 구성. SDE 및 PAR는 복제 원본 그대로 두도록 안내. 사용자가 올바른 원본을 복제했는지는 입력 선택 보고 기준이며 **새 mesh에서 shelf 미존재 재확인 필요**.
- NEXT 최소 게이트: 새 SDE mesh가 shelf-free (Wshelf=0)인지 확인 후 n2 진단 실행; 생성 pp의 activation=0 및 Iterations=12 확인. 본 메시지에서 새 solver 완료/결과 보고 없음. 원본 Baseline B / physical FREEZE HOLD 유지.

## 2026-11-02 — Lee reports PolAct parameter changed in new shelf-free clone; full SDevice source supplied (USER-REPORTED, NO VERIFIED RUN)
- 이택규가 `_Copy`가 아닌 원본 `CMP_BASELINE_2.0.0_V2`에서 다시 만든 보호 복사본의 **SWB PolAct 파라미터를 변경했다**고 보고. 변경된 정확한 UI/실제 pp 값은 새 복사본에서 아직 독립 확인하지 않음.
- 사용자 요구에 맞춰 **전체 SDevice 복붙용 코드** 제공: 이전 학교 서버 원본과 동일한 실행 명령/수치 설정을 유지하도록 구성, global Physics `Piezoelectric_Polarization(strain activation=@PolAct@)` 유지, `Math Iterations=12`, Fermi/Thermionic/Trap/CurrentPlot/Solve 및 V1/Vmax/NPlot 매크로 유지. 새 소스 전체를 실제로 붙여넣거나 실행했는지는 아직 미보고. 기존 코드와의 동일성은 **실행 파일의 pp diff로 검증 필요**, source-only 형식 차이 해석 주의.
- NEXT: 새 프로젝트 실제 이름·부모 원본과 SDE `Wshelf=0`/메시 형상/전극 일치, SWB PolAct=0 및 `ppN_des.cmd` 실효 activation=0/Iterations=12 확인. 10/15 채택된 shelf-free V2.1 이외의 구형 `_Copy` 지오메트리 재사용 금지. 진단 n2 우선, n6는 후속. 새 solver 실행이나 결과는 현재 메시에서 확인되지 않음; physical Baseline B/FREEZE HOLD.

## 2026-11-02 late — Lee identifies wrong shelf-retaining clone for POL0DIAG (USER-REPORTED + OBSERVED IMAGE; GEOMETRY BLOCKER)
- 이택규가 새 `CMP_BASELINE_2.1.0_POL0DIAG` 프로젝트 제작 시 원본 `CMP_BASELINE_2.0.0_V2`가 아닌 **`CMP_BASELINE_2.0.0_V2_Copy` 계열을 복사한 것 같다**고 스스로 확인/설명. 직전 SVisual `n1_msh` 이미지에는 SDE lateral Y≈2um에서 ≈2.5um까지 오른쪽으로 돌출된 red n-GaN-like shelf/턱이 관측됨(Elements 124583, Points 60163). 정확한 새 소스 파일/mesh TDR 경로는 아직 미검증이므로 copy lineage는 USER-REPORTED, geometry는 screenshot OBSERVED.
- **정확한 기존 작업 구조:** 이전 2026-10-22 원본 `CMP_BASELINE_2.0.0_V2/pp1_dvs.cmd` 실측 코드에는 `Wshelf=0`, `Xs=Wm/2=2um`, `Xend=Xs+Wshelf=2um`이며 2026-10-15 사용자가 공유한 Claude 보고에는 shelf 제거 V2.1 n2/n6 3.6V 도달 및 작업용 구조로 선택했다고 기록. 구형 `_Copy` shelf 모델은 원인 분석 대조군이며 V2.1 POL0DIAG 기준 아님.
- **CORRECTION OF ASSISTANT:** GPT가 사진을 보고 '문제 없음'이라 판단했던 답은 **철회**. PolAct는 SDevice 물리 설정이며 shelf geometry에 영향을 주지 않으므로 그 돌출부는 적어도 이번 단일변수 진단에 부적절. 이전 사용자가 고른 shelf-free V2.1을 우선해야 함.
- **ACTION/BLOCKER:** 현재 POL0DIAG의 SDevice 진단을 진행·해석하지 말고 기존 작업/출력을 보존. shelf-free `CMP_BASELINE_2.0.0_V2`에서 **새로운 보호 복사본** 만들기 (기존 잘못된 복사본 덮어쓰기/삭제 금지), PolAct 0.5→0만 SWB parameter 변경하고 SDE/PAR/SDevice/mesh/전극/solver 동일성·`Wshelf=0`·shelf 없는 mesh 확인. Preprocess pp activation=0/Iterations12 확인 후 n2 우선. 실제 새 solver 계산의 시작/완료는 여전히 미확인. Baseline B physical FREEZE HOLD.

## 2026-11-02 23:33 KST — Lee plans to run POL0DIAG after manual setup (USER INTENT, NOT YET RUN)
- 이택규: “그냥 돌릴게 문제 없겠지?” — 보호 복사 프로젝트 `CMP_BASELINE_2.1.0_POL0DIAG`를 직접 실행하려는 의사 표현. 실제 Run 클릭/solver 진행/결과는 아직 보고되지 않았음.
- GPT 설명: SWB PolAct=0 screenshot과 저장 SDevice `Piezoelectric_Polarization(strain activation=@PolAct@)` 및 `Math Iterations=12`는 확인됨. 복제본 전체 SDE/PAR/mesh/노드 연결/실효 pp 차이와 기존 n2/n6 동일 전류 IQE_sim, Claude 진단 판정 기준 사전 확정은 아직 미확인. 그래서 '문제 없음' 보증 불가. 기존 blank `find pp*_des.cmd`는 해당 폴더 최상위에 preprocessed CMD가 없다는 뜻; SWB 전처리 전이라면 정상일 수 있음.
- 권장 실행 범위는 보호 복사본 n2 `NtSide=0` 먼저, n6 `NtSide=1e18`은 n2 정상 확인 뒤. 시작된 경우 생성 `pp2_des.cmd`의 activation=0, Iterations=12 확인, `n2_des.log` 수렴 여부와 바이어스 범위 확인. PolAct=0은 **global** (EBL 포함) 비물리적 진단용이며 원본 Baseline B physical FREEZE HOLD 유지. 연구결과/성공은 아직 없음.

## 2026-11-02 — POL0DIAG root lacks pp CMD files before preprocessing (OBSERVED READ ONLY; NO RUN)
- 이택규가 프로젝트 폴더 `~/CMP_BASELINE_2.1.0_POL0DIAG`에서 `find . -maxdepth 1 -name 'pp*_des.cmd' -print`를 두 번 실행했으며 모두 출력 없음. **확인된 사실은 해당 폴더 최상위에 pp CMD 파일이 현재 없다는 것뿐**; SWB 전처리를 수행하지 않았거나 생성물이 다른 폴더에 있을 가능성은 아직 구분되지 않음. 파일/파라미터 복붙 실패나 solver 오류의 근거가 아님.
- 설명: `sdevice_des.cmd`와 SWB parameter는 소스, `ppN_des.cmd`는 통상 SWB preprocess 산출물. 새 프로젝트에 자동으로 존재할 필요 없음. 다음 권고: 복제한 SWB 노드 연결 상태 점검 후 n2 조건 preprocess만 실행하고 생성물에서 실제 `activation=0`과 `Iterations=12` 확인. Preprocess-only 메뉴의 정확한 사용법은 사용자 SWB 설치 UI에서 검증 전. 원본 프로젝트 불변, 실제 solver 실행 보고 없음. Baseline B physical FREEZE HOLD.

## 2026-11-02 — Lee grep find issued in home, not new POL0DIAG project (OBSERVED READ ONLY / NO RUN)
- User new shell prompt at home `[semi437@ssudisu3 ~]$` and ran `find . -maxdepth 1 -name 'pp*_des.cmd' -print`, with blank output. This does NOT determine whether `CMP_BASELINE_2.1.0_POL0DIAG` has preprocessed pp files, as command was run in wrong directory.
- Next command supplied: `cd ~/CMP_BASELINE_2.1.0_POL0DIAG && find . -maxdepth 1 -name 'pp*_des.cmd' -print`; await results before deciding preprocess-only. Current actual source macro and Iterations=12 confirmed previously, SWB PolAct=0 screenshot reported; no effective pp confirmation or solver run. Baseline B/FREEZE HOLD.

## 2026-11-02 — Lee school shell csh syntax issue recovered by Ctrl-C plan (ERROR, NO RUN)
- User terminal at `CMP_BASELINE_2.1.0_POL0DIAG` rejects ChatGPT-provided Bash `for/do/done` and `$f` with `for: Command not found`, `do: Command not found`, `f: Undefined variable`; `else?` prompt indicates unfinished csh/tcsh input. This reflects incorrect assistant command for the environment; no TCAD run failure or file change.
- Assistant advised `Ctrl+C` and read-only shell-neutral `find . -maxdepth 1 -name 'pp*_des.cmd' -print`. No returned `find` output yet. Effective clone pp activation / solver values not yet established. Baseline B FREEZE HOLD.

## 2026-11-02 — Lee direct terminal confirms POL0DIAG saved source Iterations12 (OBSERVED; NO RUN)
- New project `~/CMP_BASELINE_2.1.0_POL0DIAG`, user-executed source grep: `39: Piezoelectric_Polarization( strain activation=@PolAct@ )`, `276: Iterations = 12`. The SDevice edit to restore original V2.1 numerical iterations **is now verified in saved source**, not merely user report.
- Prior SWB screenshot showed both project rows PolAct=0, but effective preprocessed pp activation remains unverified. Next `ls -l pp2_des.cmd pp6_des.cmd` and inspect pp (preprocess-only if missing). SDE/PAR/mesh equivalence, existing IQE_sim and thresholds still open; no new TCAD solver run reported; Baseline B FREEZE HOLD.

## 2026-11-02 — Lee says full SDevice copy-paste applied in POL0DIAG (USER-REPORTED; NO RUN)
- Worker 이택규: 새 `CMP_BASELINE_2.1.0_POL0DIAG` SWB SDevice 입력을 ChatGPT가 앞서 제공한 **전체 복붙 버전**으로 바꿨다고 보고. 이 버전은 사용자 제공 SDevice 내용에서 global `Iterations=20`만 기존 실행원본과 같이 `12`로 수정한 것. 디스크 실제 파일, preprocess/solver 설정, 전체 원본과 차이의 재검증은 **PENDING**.
- SWB의 `PolAct=0` (n2-equivalent NtSide=0 / n6-equivalent NtSide=1e18) UI는 이전 스크린샷에서 관측. NEXT: clone 저장 입력 grep 확인 후 preprocess only / effective pp activation=0, Math Iterations=12, 나머지 입력 동일성 검사; 동일전류 IQE_sim baseline 및 사전 분석 gate 채택 확인. No new TCAD solver execution, no final physical model acceptance. Baseline B FREEZE HOLD.

## 2026-11-02 — Lee asks for copy-paste SDevice Math fix, patch provided not yet applied (PROPOSED, NO RUN)
- Worker 이택규는 새 POL0DIAG SDevice를 직접 편집하겠다고 하며 복붙 코드를 요청. ChatGPT 제공 변경은 `Math { ... Iterations = 12 ... }` 블록이며 기존 복제본의 `Iterations=20`을 원본 실행 deck `12`로 복원하기 위한 목적. 다른 Math 옵션은 기존 사용자 첨부 파일과 동일하게 유지.
- `Piezoelectric_Polarization(strain activation=@PolAct@)`은 이미 매크로 연결되어 수정 없음, SWB 복제본 PolAct=0은 UI에서 확인한 값. **아직 사용자 적용, preprocess, solver run 보고 없음.** SDE/PAR/복제본 물성 및 실제 pp 비교 미확인. Original protected. Baseline B/FREEZE HOLD.

## 2026-11-02 — Lee live clone diff exposed unintended Iterations change (OBSERVED / NO RUN)
- 실제 학교 서버 diff: original `CMP_BASELINE_2.0.0_V2/sdevice_des.cmd` global `Math Iterations=12`, POL0DIAG clone SDevice `Iterations=20`. 양쪽 `Piezoelectric_Polarization(strain activation=@PolAct@)` 동일; 출력된 나머지 차이는 주석/포맷(Trap 선언 줄바꿈 포함). 앞서 SWB Parameters의 clone PolAct=0 설정과 모순 없음. 파일 자체는 byte-identical이 아니므로 clone source 원본 동일성 gate 실패.
- **Corrective action only proposed; user not yet confirmed execution:** backup new clone SDevice, copy original SDevice into clone, verify `cmp`, then preprocess confirm activation=0 and Iterations=12; full clone equivalence checks still needed. No new solver run or source edit by ChatGPT. Baseline physical B / FREEZE HOLD.

## 2026-11-02 — SDevice user-pasted file PolAct macro valid; solver Iterations discrepancy (OBSERVED, NO RUN)
- Uploaded text `sdevice_des.cmd` shows `Piezoelectric_Polarization(strain activation=@PolAct@)` (line38): SWB PolAct=0 can substitute without changing SDevice physics source IF the actual clone references this file. Header explicitly labels file 2026-10-13 `PROPOSED / NOT RUN`, not a verified deployed final source.
- Uploaded `Math Iterations=20` (line275) **conflicts with** prior 2026-10-31 server-observed original V2.1 processed n2/n6 `pp2_des.cmd` and `pp6_des.cmd` both `Iterations=12` (line174). Current clone's actual editable source and PP have not been inspected, so this is a **proven discrepancy between historical artifacts, not a proven new project error**.
- NEXT: read-only actual original+clone source comparison and preprocess-only effective settings; do not run until numeric solver settings and PolAct are verified. Baseline B/FREEZE HOLD, no new run or code edit by ChatGPT.

## 2026-11-02 — Lee PolAct parameter edit observed in SWB screenshot (OBSERVED UI / NO RUN)
- Worker 이택규 provided screenshot of copied `CMP_BASELINE_2.1.0_POL0DIAG` SWB table. Both parameter rows show **PolAct=0**: row1 NtSide=0, row2 NtSide=1e18. Shared visible settings Wedge=0.1, Bspan=0, NCEdge=0, V1=2.0, Vmax=3.6; NPlot=8 (row1) and 0 (row2). User states only PolAct changed, but without original side-by-side source/PP comparisons this is user report rather than independently verified diff.
- Immediate next: inspect original-to-copy SDevice parameter binding and effective preprocessed source before starting solver; existing n2/n6 same-current IQE_sim and heuristic threshold approval still pending. This screenshot demonstrates UI PolAct=0, **not** actual solver execution or physical cause. No TCAD solver run yet reported. Baseline B / FREEZE HOLD, PolAct=0 diagnostic only, EBL global caveat.

## 2026-11-02 — Lee confirms SWB diagnostic copy created by manual project duplication (USER-REPORTED, NO RUN)
- Worker 이택규: SWB에서 기존 `CMP_BASELINE_2.0.0_V2` 복사 후 `CMP_BASELINE_2.1.0_POL0DIAG` 이름의 새 프로젝트를 만들었다고 보고. 학교 서버 실물 파일이나 full SWB parameter table은 ChatGPT가 직접 확인하지 못함.
- **PROGRESS:** copy/name step USER-REPORTED DONE. **NOT CONFIRMED:** `PolAct=0` 설정, other values identical, cloned node topology, pp diff, identical current baseline, new simulation or result. None reported executed; no code/solver changes by ChatGPT.
- NEXT: user to open SWB Parameters of new project, change only PolAct 0.5→0, show parameter screenshot. Preserve original. Run after pre-run checks including pp diff, same-current n2/n6 IQE_sim, and locked heuristic gates. Baseline physical B / FREEZE HOLD.

## 2026-11-02 — Lee chooses manual SWB source transfer (PROPOSED / NO RUN)
- User explicitly wants to **create new SWB project manually and paste code/parameters** rather than use an automatic copy workflow. No evidence this manual work has started or any run completed. Protected original `CMP_BASELINE_2.0.0_V2` untouched.
- Recommended approach: paste complete existing V2.1 SDE, SDevice, PAR inputs and clone all SWB parameters/topology unchanged except PolAct 0.5→0; first NtSide=0 n2 diagnostic, n6 NtSide=1e18 after verified baseline comparison. Candidate name `CMP_BASELINE_2.1.0_POL0DIAG` subject to server collision check, not claimed to exist. Verify runtime source actually binds `activation=@PolAct@` (Claude-reported line 21 unverified) and diff corresponding preprocessed source before solver. Need existing n2/n6 PLT same-current IQE_sim read-only baseline first.
- User has not yet explicitly locked Claude's proposed heuristic gate thresholds or confirmed final scope; no server action by ChatGPT, NO CODE CHANGE / NO RUN. PolAct=0 diagnostic only (EBL interface also changes); baseline verdict B/FREEZE HOLD.

## 2026-11-02 — Lee tentative PolAct test go-ahead (PROPOSED; NO RUN)
- 이택규가 “일단 수정해서 돌려볼까?”라고 제안. ChatGPT는 **원본 보호 복사본에 한정된 통제 진단**을 권장. 대화만으로는 Claude gate 숫자 최종 채택 및 n2/n6 범위 최종 확정은 아직 미확인.
- 다음 조치: **서버 원본 덱의 PolAct 실제 바인딩 읽기 전용 확인** → 기존 PLT 동일 전류 IQE_sim → SWB 보호 복사 → PolAct만 0.5→0 → pp diff 검증 → n2부터 실행, n6는 이후 비교를 위해 필요. 원본/물성/mesh/접점/solver 변경 금지, global EBL 영향 기록.
- USER CHOICE still needed to lock proposed heuristic (H1 QW1 JnX/J≥1% and QW4<80%; H2 <0.1% and QW4>99%; Project A ±25%) and scope. No school-server access from this ChatGPT; no source edits, no solver run, no claimed completion. Baseline B physical FREEZE HOLD.

## 2026-11-02 — 사용자 결정 대기: PolAct 진단 실험 사전 결정 2건 (이택규, Claude 전달 / NO RUN)
- **현재 상태:** PENDING_USER_DECISION / PROPOSED / UNRESOLVED. 이택규는 (1) 실험 전 판정 기준, (2) 실행 범위를 아직 선택하지 않았음. PolAct 변경 승인·실험 실행·코드 변경 **모두 없음**. V2.1 Baseline 판정 B 및 physical FREEZE HOLD 유지.
- **배경(기존 결과):** n2 기존 분석에서 QW1 중심 JnX/J≈0.005%, QW4가 전체 4QW 방사 재결합의 약 99.97%를 차지함(절대 IQE 아님). 원인 H1(분극 장벽) vs H2(고전 drift-diffusion 즉시 포획) 미확정. PolAct=0은 비물리적 **진단용**이고 Baseline 후보가 아님.
- **결정 1 — 판정 기준값을 실험 전에 고정할지/수정할지 (사용자 선택 대기):** Claude 제안 *heuristic, 문헌 검증 기준 아님*. H1 지지: QW1 중심 JnX/J ≥1% **AND** QW4 방사비중 <80%. H2 지지: QW1 중심 JnX/J <0.1% **AND** QW4 방사비중 >99%. 둘 사이 또는 혼합 결과: 양쪽 기여 가능/판정 보류. Project A 임시 진행 제안: 동일 전류 기준 IQE_sim=q∫Rad_QW/I 에서 Trap OFF→ON 감소율의 부호가 PolAct 0.5와 0에서 같고 상대 차이가 **사전 제안 ±25% 이내**. 상대차의 분모·전류 기준·오차 정의는 검증 및 사전 명시 필요. 선택지: **제안 그대로 채택 / 값 수정 및 새 수치 명기**, 둘 중 아직 **미선택**. 기준이 맞더라도 물리 인과관계가 실험 하나로 증명되지는 않음.
- **결정 2 — 실행 범위 (사용자 선택 대기):** (가) 보호 복사본에서 n2(NtSide=0, Trap OFF)와 n6(NtSide=1e18, Trap ON) **두 노드**를 동일 설정으로 진단: H1/H2 평가 + Project A 민감도까지, 연산 부담 증가(Claude 표현 약 2배, 실제 서버 시간 미확인); (나) n2 **한 노드부터**: 초기 원인 평가만, Project A 진행 판단에는 n6 추가가 필요. Claude는 (가) 권고, 자원 부족 시 (나); **이택규 결정 없음**.
- **어느 선택에도 적용되는 고정 조건:** 원본 `CMP_BASELINE_2.0.0_V2` 변경 금지. SWB 보호 복사본에서 **PolAct만 0.5→0**. Claude 보고에 따르면 덱 21행 `activation=@PolAct@` 사용(실제 pp/덱 행번호 미재검증); 메시, 전극, par, Thermionic·Formula=1, Fermi, 재결합 모델, Math(Iterations=12), Solve 램프 등은 동일하게 유지. 실행 전 원본/복사본 preprocessed pp 차이가 활성화 변경 한 줄만인지 실제 diff 확인. Global activation이므로 QW와 **EBL** 계면 전하가 함께 달라지는 해석 한계 기록.
- **실행 전 READ ONLY:** 기존 n2/n6 .plt로 **동일 전류** IQE_sim 기준값을 계산. 새로운 TCAD 실행 없이 가능하지만 이 메시지에서는 아직 계산하지 않음.
- **상위 기록과 일관성:** 11/02 밤 Claude Baseline 선택지 B는 '진단 실험 계획을 검토'한다는 의미이며 이택규의 세부 기준·범위 선택과 실행 승인을 대신하지 않음. 이 두 결정과 명시적 실행 승인이 없는 한 어떤 노드도 돌리지 말 것.

## 2026-11-02 밤 — Lee / Claude V2.1 Baseline independent decision (USER-FORWARDED, NO RUN)
- PROVENANCE: 이택규가 전달한 2026-11-02 밤 Claude 의사결정 요약. Claude 보고 기준 GitHub main `7a3cacd` (22:25 KST)까지 확인, Issue #7은 접근 거부로 미확인. 이번 ChatGPT 기록 시 Claude의 UG 원문/학교 서버를 직접 재검증하지 않았으며 UG 텍스트는 복제하지 않음.
- DECISION: Baseline 판정 **B 유지 / physical FREEZE HOLD**. 수치적 자기일관성은 기존 실행 기록상 양호하나 MQW 캐리어 분포의 물리 원인은 **UNRESOLVED**. 정상 Baseline 승인도 폐기도 아님. 새로운 시뮬레이션, 코드·mesh·MaterialDB 변경 없음.
- EVIDENCE / DERIVED: 기존 n2/n6 결과에서 QW4가 4QW 방사 재결합을 99.9688% / 99.9929% 차지함(IQE 아님). QW1 중심 JnX=8.85e-5 A/cm², 현 위치 국소 총 J≈1.82 A/cm²에서 약 0.005%. QW4 이전 수송/재결합 분배의 강한 불균형은 관측되지만 원인 분리 실패. Claude는 관측 패턴이 일반적인 p측 발광/정공 병목 기대와 반대라고 해석함(실험 경향의 일반화는 별도 검증 필요).
- POLARIZATION (CLAUDE DERIVED, NOT DIRECT INTEGRAL): 기존 출력 QW Px=+8.216e-7, barrier Px=+3.4e-6 C/cm². UG 식1085로 보고된 q_PE=-activation·∇P에 activation=0.5를 대입한 이상적 계면 sheet 크기 ≈0.5×(3.4e-6−8.216e-7)/q ≈8.05e12 cm⁻². 부호의 Ga-polar 일치 여부와 실제 적용 모델/계면 조건은 Claude 해석이며 완전한 독립 검증 아님. **오전 QW4_PLAN_20261102의 CSV PE_Charge sheet 수치적 적분 단계는 이 의사결정에서 불필요로 대체(SUPERSEDED);** MaterialDB 계수 상속 추적도 중단 권고.
- COMPETING HYPOTHESES (UNRESOLVED): H1 강한 분극 계면 전하로 인한 전자 장벽; H2 classical drift-diffusion의 즉시 포획과 70:30 offset에 의한 우물 집중. 원인/인과관계 확정 금지.
- PROPOSED CHOICE B: 이택규가 **명시적으로 승인한 후에만** 원본 보존된 복사본에서 global PolAct 0.5→0 단일변수 대조; n2 Trap OFF와 n6 Trap ON 2개 조건 (자원 부족 시 n2 우선). Global activation은 EBL 등 다른 계면에도 영향을 주므로 완전한 원인 분리 실험이 아니며 PolAct=0은 진단용으로만, 물리 Baseline 후보로 사용하지 않음.
- CLAUDE HEURISTIC GATES (NOT VALIDATED): n2 QW1 JnX/J ≥1% 및 QW4 방사 비중 <80%면 분극 기여 우세 가설 지지; JnX/J <0.1% 및 QW4>99%면 DD 즉시 포획 가설 지지. 그 외 혼합/불확정; 어느 결과도 단독으로 인과 확증하지 않음.
- PROJECT A CONDITIONAL (PROPOSED ONLY): 동일 주입 전류 IQE_sim의 Trap 감소 효과가 PolAct 0.5와 0에서 부호가 같고 상대차가 사전 설정 제안 허용범위 ±25% 이내일 경우에만 제한적 임시 Baseline(C) 전환 논의. QW 분포/절대 IQE/Vf 주장 금지. Project B에는 자동 적용 금지.
- NEXT (READ ONLY FIRST): (1) 기존 n2/n6 .plt에서 **동일 전류 기준 IQE_sim** 재검산; (2) 복사본의 preprocessed `pp` 차이가 예정된 PolAct 변경만인지 검토(Claude가 제안한 '21행' diff 주장 검증 필요). 실행 승인/복사본 실제 생성 여부는 아직 확인되지 않음.
- LIVE decision now supersedes the earlier 'ask Claude to assess' pending step; no simulation authorization was given.

## 2026-11-02 — Claude independent reassessment proposed (Lee, NO RUN)
- User requests independent review before more TCAD testing. Current blocker: QW4 anomalous 4QW radiative dominance with unresolved cause. Stop repetitive CSV queries; review a single decisive controlled-test design and Baseline B go/no-go for Project A. Candidate polarization activation 0.5-to-0 on protected copy only if user approves. No execution or baseline edits. Relay details in .ai-sync/RELAY.md.

## 2026-11-02 — Lee interwell QF windows audited; end repetitive read-only loop (OBSERVED + PROPOSED WORKFLOW CHANGE; NO RUN)
- OBSERVED user-read-only n2 3.6V qw4_36_depth.csv at Y=1um, hand-selected X windows: B1 x=(0.191,0.213) um N=44 ΔeQF=+0.0109032700 eV max(Ec-eQF)=0.61493831 eV; B2 x=(0.216,0.238) um N=47 ΔeQF=+0.25042766 eV max=0.594776913 eV; B3 x=(0.241,0.263) um N=43 ΔeQF=+0.0099175800 eV max=0.5580799700 eV. The spans are broad user-selected ranges, not yet verified as strictly barrier-only region boundaries; quoted end-to-end eQF difference is not independently a thermionic transport barrier nor proof that B2 causes QW4 dominance. No new solver run.
- Research workflow decision: too many redundant CSV/material grep audits were performed. Confirmed n2/n6 QW4 extreme radiative concentration, local electron-continuity numerical closure, n/p localization, same pointwise Radiative/(n*p) at QW1 and QW4 centers. Fundamental driver of n/p focusing remains UNRESOLVED; Baseline B physical FREEZE HOLD. Shift to concise go/no-go root-cause test design, not continued incremental read-only command requests. Proposed protected copy only after Lee explicitly authorizes: keep mesh, contact, trap-off settings and other parameters fixed, compare polarization interface activation 0.5 vs 0, subject to exact installed T-2022.03 model semantics and runtime sourcing checks. This is PROPOSED, NOT RUN, not a baseline edit or proven mechanism.
- NEXT: stop for now. On continuation present one minimal decisive controlled-test protocol and decision criteria for authorisation, or state risks of advancing Project A on provisional baseline; no automatic SDevice run or source edits.

## 2026-11-02 — Lee QW1/QW4 center radiative normalization equality (OBSERVED + DERIVED; NO RUN)
- OBSERVED from Lee school-server user-executed Python read-only existing n2 3.6V Y=1um fine CSV at QW1 X=0.18948437um and QW4 X=0.26459765um: QW1 RadiativeRecombination=3.0583003e20 cm^-3 s^-1 and Radiative/(n*p)=2.000000011528524e-11 cm3/s; QW4 RadiativeRecombination=3.075366e25 cm^-3 s^-1 and Radiative/(n*p)=1.999999930276919e-11 cm3/s. Source is actual pasted output; no fresh TCAD run.
- DERIVED radiative rate ratio QW4/QW1=100558.01256665; previously observed n*p ratio=100558.0166519; ratio of normalized rates=0.999999959374 (relative difference -0.00000406258%). Therefore QW4 vs QW1 center radiative-rate contrast is numerically explained by n*p difference, with no evidence of a QW4-only larger effective radiative coefficient at those two points. Does not establish that model B is globally identical across all wells or explain upstream reason for n,p concentration. QW4 physical cause remains UNRESOLVED, Baseline B FREEZE HOLD; no deck/lib edits.
- NEXT READ ONLY: inspect interwell electron/hole transport and energy-band/quasi-Fermi profiles in archived n2 depth CSV, with emphasis on potential versus actual flux, then decide whether protected-copy one-variable sensitivity merits user approval. Avoid more redundant recombination normalization commands; no new simulation without approval.

## 2026-11-02 — Lee QW1 vs QW4 center carrier and quasi-Fermi comparison (OBSERVED + DERIVED, NO RUN)
- OBSERVED USER SCHOOL TERMINAL (read-only existing n2 3.6V Y=1um fine CSV): QW1 center-nearest X=0.18948437um, n=4.8448286e15 cm^-3, p=3.1562523e15 cm^-3, Ec-eQF=0.22401485eV, hQF-Ev=0.23767840eV, JnX=8.8535045e-05 A/cm2, JpX=1.823539 A/cm2. QW4 center-nearest X=0.26459765um, n=1.0123225e18, p=1.5189656e18, Ec-eQF=0.08558352eV, hQF-Ev=0.07756020eV, JnX=0.96137367 A/cm2, JpX=0.86228261 A/cm2. Earlier repeated identical QW1/QW4 continuity command is duplicate output, not separate run.
- DERIVED ratios QW4/QW1: electron n=208.9490844x; hole p=481.2560770x; n*p=100558.01665x at selected center points; JnX ratio=10858.6794x. Ec-eQF offset is lower by 0.13843133eV and hQF-Ev lower by 0.16011820eV in QW4. Jn/Jtotal at selected center points QW1=0.00485488639%, QW4=52.71682392%; Jn+Jp QW1=1.823627535045 vs QW4=1.82365628 A/cm2. These are local cutline samples and do NOT prove barrier/transport causation, recombination model validity or 2D current conservation.
- NEXT READ ONLY: evaluate B0-B3/QW1-QW4 full 3.6V depth profile and e/h quasi-Fermi discontinuities and barrier-to-well Jn, plus lateral JnY contribution where possible, to distinguish depletion, capture and electron bottleneck. No model change or new run; Baseline B physical FREEZE HOLD, QW4 cause UNRESOLVED.

## 2026-11-02 — Lee QW1 vs QW4 fine cutline continuity comparison (OBSERVED + DERIVED; NO RUN)
- Lee user server read-only Python over n2 3.6V Y=1um existing fine CSV (identical output posted twice, not two runs): QW1 fine N=66, X=0.1800625..0.19995312um, deltaJnX=0.0001961119898955 A/cm2, qIntTotalR=0.0001961108057556653 A/cm2. QW4 fine N=62, X=0.25543749..0.27428126um, deltaJnX=1.8217438432 A/cm2, qIntTotalR=1.8216004716537455 A/cm2. q conversion 1.602176634e-23 C*cm/um used in trapezoidal depth integration. Closure QW1=99.9993961920%, QW4=99.9921299832%; deltaJnX ratio 9289.30375. Data spans differ and include barriers: not QW-only radiative integral nor proof of full 2D continuity or cause of QW4 carrier accumulation.
- NEXT READ ONLY: compare actual center-point QW1 and QW4 n,p, Ec-eQF, hQF-Ev, Jn/Jp and recombination using existing fine CSVs, then assess interwell transport hypothesis. No TCAD solver run, no deck/MaterialDB modifications. Root cause UNRESOLVED; Baseline B physical FREEZE HOLD.

## 2026-11-02 — Lee InN documented strain polarization equation inspected; pause MaterialDB audit (OBSERVED, NO RUN)
- User's read-only installed T-2022.03 InN.par lines 525–570 show strain-mode Pz=psp_z+2*d31*strain*(c11+c12-2*c13^2/c33), strain=(1-relax)*(a0-a)/a, plus stress-model tensor and crystal/simulation coordinate transformations. No numeric formula assignment shown in this excerpt or prior full 525–645 assignment grep.
- Confirmed only documentation/formula source; actual runtime InGaN interpolation, default formula, applied strain and cause of n2 QW4 ~99.97% concentration UNRESOLVED. No code change, no new simulation. Physical Baseline FREEZE HOLD.
- Lee wants to stop repetitive material-file lookup now. NEXT: return to existing n2 QW4 mechanism validation with read-only runtime/model provenance and 2D transport evidence; prioritize direct decisive checks, not more repetitive MaterialDB greps. Sensitivity tests only with approval.

## 2026-11-02 — Lee InN piezo formula assignment absent in block (OBSERVED; NO RUN)
- OBSERVED from user executed awk with NR 525..645 over installed T-2022.03 MaterialDB/InN.par Piezoelectric_Polarization section: only a0=3.189 Angstrom (line639), a=3.54 Angstrom (line640), relax=0.1 (line641) matched; there was no explicit assignment formula = within the inspected 525–645 range. This confirms absence of literal formula assignment IN THAT BLOCK, not which default formula SDevice uses and not polarization-model inactivity.
- Existing n2 source pp2_des.cmd has Piezoelectric_Polarization(strain activation=0.5) and DefaultParametersFromFile; archived n2 QW1–QW4 Px center matches +8.2162955e-7 C/cm2, but InGaN effective material coefficients/strain and default formula NOT VERIFIED. QW4 ~99.97% QW radiative share cause UNRESOLVED; baseline B physical FREEZE HOLD. No new simulation or any source/material/mesh editing.
- NEXT READ ONLY: inspect unexamined opening of InN Piezoelectric_Polarization block lines 525–570, especially comment about formula default. Then determine actual T-2022.03 default and n2 runtime InGaN material parameter inheritance, without speculative model changes.

## 2026-11-02 — InN.par coordinate transform verified (OBSERVED; NO RUN)
- User read InN.par lines 570–600: stress coordinates -> crystal coordinates -> piezo polarization -> simulation coordinates. No formula assignment in excerpt. Previous n2 lattice orientation X=(0,0,-1),Y=(1,0,0) should govern output Px sign, not the example orientation in file. Next: read-only check formula in InN.par lines 525–645. Baseline physical freeze HOLD; QW4 cause unresolved.

## 2026-11-02 — Lee InN piezo a0 a relax strain defaults observed (OBSERVED + CONDITIONAL DERIVED, NO RUN)
- OBSERVED (user school server, read only): installed T-2022.03 MaterialDB/InN.par lines600–645 Piezoelectric_Polarization block contains d31=-3.5000e-10, d33=+7.6000e-10 cm/V; psp_z=-4.2000e-06 C/cm2; c11=2.2300e11, c12=1.1500e11, c13=9.2000e10, c33=2.2400e11 Pa; e31=-4.8586e-05, e33=1.0629e-04 C/cm2; strain a0=3.189 Angstrom, a=3.54 Angstrom, relax=0.1. The excerpt does not show the piezo model formula number (previous lines needed). `a0` matches GaN piezo a0=a=3.189 Angstrom, consistent with GaN-lattice-reference pseudomorphic simplified strain assumptions; no claim actual active InGaN strain is proven.
- DERIVED (pure InN parameter block only, conditional on simplified-strain equation strain=(1-relax)*(a0-a)/a): strain=0.9*(3.189-3.54)/3.54≈-0.08924. DO NOT apply pure InN strain to InGaN x=0.15; InGaN actual effective parameters/interpolation and runtime overrides not verified. Prior hypothetical linear InGaN spontaneous psp_z=-3.52e-06 C/cm2 and observed QW Px=+8.2162955e-07 are not directly equal; piezo cancellation is a plausible mechanism, NOT confirmed. QW1–4 bulk Px are equal; QW4 ~99.97% recombination root cause remains UNRESOLVED. Physical baseline B/FREEZE HOLD; NO NEW RUN, NO CODE CHANGE.
- NEXT READ ONLY: obtain InN.par lines 570–605 containing piezo formula and model notes; cross-check actual InGaN runtime parameter inheritance and 2D n2 default-sourcing logs before predicting QW polarization. Do not adjust installed MaterialDB or run activation test without approval.

## 2026-11-02 — Lee InN polarization coefficients and conditional InGaN spontaneous interpolation (OBSERVED / CONDITIONAL DERIVED; NO RUN)
- OBSERVED USER SERVER: read-only grep installed T-2022.03 MaterialDB/InN.par found Piezoelectric_Polarization block beginning line525; psp_z=-4.2000e-06 C/cm2 line622, e31=-4.8586e-05 C/cm2 line632, e33=+1.0629e-04 C/cm2 line634, a=3.54 Angstrom line640 and relax=0.1 line641. Previously independently read installed GaN.par piezo block: psp_z=-3.4000e-06, e31=-5.2740e-05, e33=+8.9460e-05 C/cm2, relax=0, a=3.189 Angstrom. InGaN.par header defines x=0 GaN, x=1 InN and describes default linear interpolation for some material-dependent models, with explicit overrides possible.
- DERIVED CONDITIONAL: IF InGaN piezo-model spontaneous-polarization endpoint coefficients inherit linear GaN/InN values, at x=0.15 psp_z=0.85*(-3.4e-6)+0.15*(-4.2e-6)=-3.52e-6 C/cm2. Prior n2 QW1-4 center PE_Polarization-X=+8.2162955e-07 C/cm2 vs hypothetical orientation-flipped spontaneous-only +3.52e-6 gives magnitude difference 2.69837045e-6 C/cm2. This does not prove a specific piezoelectric contribution, runtime parameter origin, interface activation or physical cause; strain and activated polarization model need verification. Previous observed barrier-center Px=+3.4e-06. Do not assume QW4-specific material constants. Baseline B, physical FREEZE HOLD. NO NEW SDEVICE RUN, NO DECK OR LIBRARY EDIT.
- NEXT READ ONLY: inspect installed InN.par polarization block around lines605–645 to identify formula/a0/a and strain model assumptions, then verify effective runtime InGaN polarization coefficients/strain/activation using n2 logs and available parameter sources; avoid new simulation or changing physical baseline without explicit user approval.

## 2026-11-02 — Lee InGaN header endpoints and QWStrain a0 discrepancy (OBSERVED/UNRESOLVED; NO RUN)
- OBSERVED: 이택규 학교 서버 설치 T-2022.03 MaterialDB/InGaN.par lines 1–100 read only. Header explicitly says InGaN(x=0)=GaN and InGaN(x=1)=InN; for unspecified mole-dependent parameters example interpolation P=x*P(InN)+(1-x)*P(GaN), with explicit parameters overriding that interpolation. Epsilon(0)=8.9, epsilon(1)=15.3 consistent with stated endpoints. For n2 xMoleFraction=0.15, conditional linear combination is 0.85*GaN+0.15*InN; this does NOT establish piezoelectric polarization runtime interpolation/override.
- CROSS-CHECK OBSERVED: earlier installed InGaN.par QWStrain section lines~270–271 listed a0(0)=3.5480e-10 m (3.548 Å), a0(1)=3.1890e-10 m (3.189 Å), reversed versus file header's declared GaN(0)/InN(1) and GaN.par piezo a=3.189 Å. Unclear whether QWStrain uses independent endpoint convention or source inconsistency; not confirmed model active; do NOT claim cause of QW4 focus. QW4 radiative localization ~99.97% remains unresolved; Baseline B FREEZE HOLD; no solver/deck/library changes.
- NEXT READ ONLY: verify existence and actual Piezoelectric_Polarization parameters of installed InN.par via grep; inspect InGaN model inheritance rules and effective n2 defaults. No edits or experiments pending explicit consent.

## 2026-11-02 — Lee InGaN QWStrain block inspected; polarization origin unresolved (OBSERVED; NO RUN)
- OBSERVED user pasted read-only `sed -n '225,285p'` installed Sentaurus T-2022.03 MaterialDB/InGaN.par. `QWStrain` block starts at line 238; comments state it models strain-dependent quantum-well subband energy shifts, and wurtzite lattice constants a0/c0 require formula 2. Reported `a0(0)=3.5480e-10 m`=3.548 Angstrom, `a0(1)=3.1890e-10 m`=3.189 Angstrom, `eps(0)=eps(1)=0`, and `a_c(0)=a_c(1)=-4.08 eV`. `* Default formula = 1` is a COMMENT, not proof of active formula. This QWStrain block is not the Piezoelectric_Polarization block; the output lacks polarization-specific psp/e31/e33. `eps=0` does NOT establish zero actual device strain without model and context.
- Previous grep found no explicit InGaN.par Piezoelectric_Polarization section; nonzero InGaN QW Px=+8.2162955e-07 C/cm2 persists in existing n2 cutline (same all QWs). It is possible that model coefficients are inherited/interpolated from endpoint material files, but T-2022.03 actual implementation and provenance have NOT been verified. Do NOT confuse QWStrain parameter a0 with piezo polarization model a0, or assert QWStrain is necessarily enabled. QW4 ~99.97% radiative localization remains causally unresolved. No new TCAD run or source changes. Baseline B physical FREEZE HOLD.
- NEXT READ ONLY: inspect InGaN.par top header for component material and molefraction interpolation convention, check availability of installed InN.par and its polarization block, and compare GaN.par counterpart. Determine actual runtime inherited coefficients/overrides before interpreting QW Px or proposing parameter sensitivity tests; no baseline modification.

## 2026-11-02 — Lee InGaN MaterialDB polarization grep found no direct matching entries (OBSERVED; NO RUN)
- 이택규 학교 서버에서 설치된 T-2022.03 MaterialDB/InGaN.par를 읽기 전용 grep -nEi 'Piezoelectric_Polarization|psp_|relax|e31|e33|d31|d33|strain' 실행. 실제 출력은 line132 주석 EnergyRelaxationTime, line238 QWStrain, line242 주석 StrainConstant eps(formula=1) or lattice constant 3곳뿐이다. 검색어와 일치하는 명시적 Piezoelectric_Polarization/psp/e31/e33/relax 정의는 이 파일의 이번 검색에서 발견되지 않음 (OBSERVED). QWStrain의 구체 내용·분극 모델과의 연결은 아직 미확인.
- InGaN.par 직접 정의 부재 != 실제 SDevice 런타임에서 InGaN 분극 비활성. 기존 n2 3.6V cutline QW1–QW4 모두 Px=+8.2162955e-07 C/cm2 관찰. 물성 상속, 혼합물 interpolation, 명령/기본 물성 중 어떤 출처인지는 아직 검증되지 않음; QW4 약99.97% 집중 원인은 UNRESOLVED. Baseline B physical FREEZE HOLD; 새 simulation 및 source 변경 없음.
- 다음 READ ONLY: sed -n '225,285p' /user/tools/synopsys/sentaurus/T-2022.03/tcad/T-2022.03/lib/sdevice/MaterialDB/InGaN.par 로 QWStrain 원문(블록 경계·의미) 확인. 이후 런타임 분극 파라미터 계승 출처 확인; 단일 변수 실험 승인 전 실시 금지.

## 2026-11-02 — GaN polarization file audit (Lee, OBSERVED; NO RUN)
- GaN.par polarization block: formula=1, relax=0, psp_z=-3.4000e-06, e31=-5.2740e-05, e33=+8.9460e-05 C/cm^2, a0=a=3.189 Å (user server grep).
- InGaN polarization block and runtime coefficient origin unverified; investigate read-only. QW4 causality unresolved, baseline FREEZE HOLD.

## 2026-11-02 — Lee installed AlGaN polarization coefficients observed (OBSERVED, NO RUN)
- Worker 이택규 actual school-server read-only grep of installed T-2022.03 MaterialDB *GaN.par (output truncated by head -n 120): AlGaN.par Piezoelectric_polarization block line1017; formula=1 line1076; relax=0.0 line1078; psp_z(0)=-3.4000e-06, psp_z(1)=-9.0000e-06, B(psp_z(1))=-2.10e-06, C(psp_z(1))=0; e31(0)=-5.2740e-05, e33(0)=8.9460e-05 C/cm^2. GaN.par polarization section heading line737 observed but numeric coefficients not within pasted output; InGaN.par numeric coefficients not within pasted output.
- Previous n2 3.6V barrier-center Px=+3.4e-06 C/cm^2 equals magnitude of AlGaN.par psp_z(0). Known lattice orientation plausibly reverses sign, but effective runtime source, InGaN polarization, activated interface sheet and QW4 cause remain UNVERIFIED. No new solver run or any source/mesh/material library edits; Baseline B physical FREEZE HOLD.
- NEXT READ ONLY: grep assignment lines for psp_z, e31, e33, a0, a, relax and formula in GaN.par, InGaN.par, AlGaN.par WITHOUT head truncation; check InGaN x=0.15 and runtime provenance. No physics perturbation without approval.

## 2026-11-02 — installed T-2022.03 GaN-family MaterialDB file names confirmed (OBSERVED; NO RUN)
- In verified `/user/tools/synopsys/sentaurus/T-2022.03/tcad/T-2022.03/lib/sdevice/MaterialDB`, user actual `find -maxdepth 1` located `GaN.par`, `InGaN.par`, `AlGaN.par`, `AlInGaN.par`. Library content not yet opened, so numeric default polarization constants and effective n2 run origin remain UNVERIFIED.
- NEXT read only grep installed GaN/InGaN/AlGaN polarization blocks. No simulation or source modification, baseline physical FREEZE HOLD.

## 2026-11-02 — actual Sentaurus T-2022.03 MaterialDB directory located (OBSERVED, NO RUN)
- User's `find ... -maxdepth 8 -type d -name MaterialDB` from server returned `/user/tools/synopsys/sentaurus/T-2022.03/tcad/T-2022.03/lib/sdevice/MaterialDB`. This confirms installed MaterialDB directory. No data files or polarization material coefficients read yet.
- NEXT READ ONLY list GaN/InGaN/AlGaN files in that exact directory, then inspect actual polarization coefficients and provenance vs n2 CSV. QW4 root cause UNRESOLVED; Baseline B physical FREEZE HOLD; no run/deck changes.

## 2026-11-02 — school server sdevice executable path confirmed; default MaterialDB not yet found (OBSERVED, NO NEW RUN)
- User actual `which sdevice` = `/user/tools/synopsys/sentaurus/T-2022.03/bin/sdevice`. Env query `env | grep -E '^(STROOT|STRELEASE)='` had no output. Installation executable path verified, but release MaterialDB pathname and actual GaN/InGaN polarization parameters are still unverified.
- NEXT READ ONLY find MaterialDB dirs within `/user/tools/synopsys/sentaurus/T-2022.03` (maxdepth8) and inspect source parameter files after confirmation. No simulation, no source edit; Baseline physical FREEZE HOLD.

## 2026-11-02 — active n2 par polarization constants not explicit; MaterialDB read-only audit pending (OBSERVED/PUBLIC DOC; NO RUN)
- User's `pp2_des.par` grep `Piezoelectric|Strain|e31|e33|Psp|Relax|Lattice|Polarization|a0` shows only global `LatticeParameters`. No polarization-specific coefficient override found in preprocessed PAR; not proof polarization absent, because `pp2_des.cmd` has `DefaultParametersFromFile` and `Piezoelectric_Polarization(strain activation=0.5)`; n2 CSV has Px and interface PE_Charge.
- Public Sentaurus Training Ch16 §16.4.4 confirms GaN/AlGaN/InGaN polarization material defaults from `$STROOT/tcad/$STRELEASE/lib/sdevice/MaterialDB/`. Actual installed T-2022.03 default numerical constants and n2 runtime origin NOT yet opened. QW4 origin remains unresolved.
- NEXT READ ONLY environment STROOT/STRELEASE then actual library GaN/InGaN file polarization parameters and n2_des.log sourcing/overrides; don't run sdevice -P in baseline or perform sensitivity without user approval. Baseline B/FREEZE HOLD.

## 2026-11-02 — Lee active PAR GaN/InGaN band offsets match nominal 70:30 (OBSERVED + DERIVED; NO RUN)
- User server `pp2_des.par`: GaN Eg0=3.4376/Chi0=4.1, InGaN Eg0=2.8569/Chi0=4.5065, AlGaN Eg0=3.7564/Chi0=3.8768eV. All ConstantMobility mumax=300,10. Nominal GaN–InGaN ΔEg=.5807eV, electron step ΔEc=.4065eV, hole step ΔEv=.1742eV, 70:30; Claude's earlier reported offsets corroborated from source. Actual biased Ec−eQF is a different quantity and electron-bottleneck cause is NOT confirmed. `svisual ... Done` indicates viewer job exit, not new simulator run.
- NEXT READ ONLY inspect actual strain/polarization parameter blocks/default library and effective band transport; any `activation 0.5→0` copy experiment remains user-approval-gated. Physical baseline FREEZE HOLD; no device source modification.

## 2026-11-02 — Lee n2 actual polarization/heterojunction physics source audited (OBSERVED + PUBLIC DOC; NO RUN)
- User current server `pp2_des.cmd`: global `Fermi`, `Piezoelectric_Polarization(strain activation=0.5)`, `DefaultParametersFromFile`, `Recombination(SRH Radiative Auger)`, `IncompleteIonization`; `Thermionic` at InGaN/GaN, AlGaN/GaN, AlGaN/InGaN. `pp2_des.par`: `LatticeParameters X=(0,0,-1),Y=(1,0,0)`; corresponding `ThermionicEmission Formula=1` on 3 interfaces. Runtime n2 source not altered.
- Public Sentaurus Training Ch16 §16.4.3 describes `activation` as scaling charge at polarization discontinuities; §16.7.5 supports Fermi + Thermionic Formula1 pairing; §16.3 supports UCS lattice orientation. This corrects prior 'activation might be only piezo component' concern, although original T-2022.03 UG and actual effective applied sheet remain NOT independently measured. Conditional P-jump/q ~1.609e13cm^-2; half scaling ~8.046e12cm^-2 only IF uniform charge scaling.
- NEXT FIRST READ ONLY extract actual `pp2_des.par` Chi0/Eg0/mumax/strain/polarization blocks and imported library defaults, check tunneling explicit settings. QW4 origin UNRESOLVED, baseline verdict B and FREEZE HOLD; `activation .5→0` sensitivity remains PROPOSED, no run.

## 2026-11-02 — 3.6V QW1–4 동일 내부 Px/In 조성 확인 (OBSERVED USER TERMINAL; NO NEW RUN)
- `qw4_36_depth.csv` X-depth Y=1um center nearest samples: QW1/QW2/QW3/QW4 all `Px=8.2162955e-07`, `xMoleFraction=0.15`; B0/B1/B2/B3/B4 all `Px=3.4e-06`, `xMoleFraction=0`. `PE_Charge` at region centers near 0 vs QW4 interface local peak ±1.2297757e21 previously observed.
- Thus QW4 uniquely increased material composition / center polarization magnitude is contradicted; **does not exclude polarization/transport causality**, cumulative voltage profile, QW-to-QW carrier differences, or varying activated interface sheet. User-confirmed center CSV ≠ all eight interface charge measurement.
- NEXT FIRST read-only actual `pp2_des.cmd/par` polarization activation, Fermi, Thermionic and band-offset checks, then interface-by-interface signed charge inspection. Baseline physical FREEZE HOLD, new run/source modification none.

## 2026-11-02 — n2 QW4 fine cutline local electron continuity nearly closes (OBSERVED + DERIVED; NO RUN)
- Read-only user terminal, `qw4_36_qw4fine.csv`, Y=1µm, X=.26300001–.266um, N=24: ΔJnX=1.8216831695A/cm²; q∫Rad dx=1.2205564144284573, q∫Auger dx=.5018975294245672, q∫SRH dx=.09908575891169007, q∫TotalR dx=1.8215397088407301 A/cm². Calculated local depthwise closure=99.9921248293%; relative residual=0.0078751707%; channel percentages Rad 67.00685%, Auger 27.55348%, SRH 5.43967%.
- Interpretation: QW4 local recombination sink quantitatively accounts for almost all depthwise Jn reduction at chosen Y. This does NOT prove why QW4 captures nearly all carriers vs QW1–3, or establish integrated 2D continuity because ∂JnY/∂Y unmeasured. No new run, baseline physical FREEZE HOLD.
- IMMEDIATE READ ONLY: signed PE_Charge and PE_Polarization-X sampling near x=.263/.266um, validate units before sheet integration; check actual polarization/thermionic/band offset settings. PolAct perturbation still unapproved.

## 2026-11-02 — 3.6V QW4 fine CSV 직접 관찰: 높은 재결합과 큰 depth Jn 교환 (OBSERVED/DERIVED, NO RUN)
- User cutline `qw4_36_qw4fine.csv` Y=1um. B3 near x=.26250389: Jn=.0017779541, Jp=1.8218258, Ec−eQF=.352, Rad=9.6067543e14. QW4 x=.26355079/.26459765/.26551366: Jn=.33616893/.96137367/1.5101376, Rad=2.4382434e25/3.075366e25/2.4777785e25. B4 near x=.26656055: Jn=1.8234614, Jp=.0003014948, Ec−eQF=.3675, Rad=7.4700005e18. All Jtotal~1.8236 A/cm².
- DERIVED local JnX(B4−B3)=1.8216834459 A/cm² (~99.9025% B4 JnX). Consistent with intense QW4 recombination sink, **not independent proof of electron interwell bottleneck / polarization / thermionic causal mechanism**. 2D lateral J divergence makes one X cutline insufficient for full recombination current budget.
- NEXT first read-only trapezoidal q∫(Rad/Auger/SRH/TotalRecombination)dx within QW4 [.263,.266]um from existing CSV, compare JnX change at same sample bounds; caveat missing exact edges, current components and Y-derivative. Then signed polarization sheet extraction and source physics. Baseline B FREEZE HOLD; no new solver run/source edit.

## 2026-11-02 — 기존 3.6V cutline에서 B0–B3 전자 결핍 및 QW4 전류 성분 급변 직접 관찰 (OBSERVED/DERIVED; NO RUN)
- 이택규 사용자 터미널 `qw4_36_depth.csv` center-nearest samples (Y=1µm) B0–B3 p/n≈5.9e4, 1.002e5, 4.04e4, 1.43e4; Ec−eQF 0.5070/0.5144/0.4895/0.4449eV and hQF−Ev 0.3012/0.2948/0.2935/0.2758eV. CLAUDE electron scarcity DATA PATTERN corroborated (not cause).
- QW3 n2.339e16/p1.594e16, QW4 n1.0123e18/p1.5190e18 cm^-3; QW4/QW3 n≈43.28, p≈95.30. B3 JnX~0.0017768 / JpX~1.8218269; QW4 center JnX~0.96137367 / JpX~0.86228261. Jtotal ~1.8236 throughout. Spatial re-partition of carrier currents is consistent with strong QW4 recombination sink. **Cause not separated:** barrier transport limitation vs in-well capture/recombination; do not label electron bottleneck CONFIRMED.
- NEXT READ ONLY: QW4 fine CSV values near .260-.270um to check near-interface current changes and energy; later PE_Charge integrated signed sheet with validated units. Baseline verdict B/FREEZE HOLD, no new run/deck changes.

## 2026-11-02 — QW4 3.6V cutline numeric coverage + current stack boundaries verified (OBSERVED; NO RUN)
- `qw4_eq_depth.csv` N392/X0.13988867–0.2973125/Y1; `qw4_36_depth.csv` N392/same; `qw4_36_qw1fine.csv` N66/X0.1800625–0.19995312/Y1; `qw4_36_qw4fine.csv` N62/X0.25543749–0.27428126/Y1. Numeric row filter `r['X'] not in ('none','')` executed successfully after a concatenated-command shell SyntaxError.
- Latest user `pp1_dvs.cmd` top→bottom thickness yields QW1 .188–.191, QW2 .213–.216, QW3 .238–.241, QW4 .263–.266um, adjacent B0–B4 boundaries derived from stack (Y=1 depth cutline covers wells and barriers). Old claimed QW coordinates from 10/12 may be shifted by .020um; do not conflate without verifying dataset version.
- Next read only: sample the current CSV at B0–B3 and QW1–QW4 centers for electron/hole current, density, Ec−eQF and hQF−Ev before judging electron interwell bottleneck. The `PolAct` diagnostic remains PROPOSED and unapproved, Baseline physical FREEZE HOLD.

## 2026-11-02 — 실제 cutline CSV 헤더와 첫 수치 행 확인 (OBSERVED USER TERMINAL, NO RUN)
- 4 CSV wc -l: eq_depth 395, 36_depth 395, qw1fine 69, qw4fine 65; headers include metadata row `none` and fields for signed PE_Charge, PE_Polarization-X, Ec, Ev, e/h QuasiFermiEnergy, n/p, e/hCurrentDensity-X, X/Y/Distance.
- 3.6V depth sample X=0.14um Y=1um TotalCurrentDensity-X~1.8236326 (numeric match to previously calculated conditional 2D J~1.8236426), PE_Charge=-5.5020169e20 is local field, **not** integrated sheet cm^-2.
- NEXT (READ ONLY) verify min/max X/Y for CSV cutlines and actual pp1_dvs.cmd MQW stack, then band/QF/current profile and signed interface polarization charge calculation with validated units and sorted points. Claude electron bottleneck hypothesis and polar-sensitivity run remain PROPOSED; physical baseline FREEZE HOLD.

## 2026-11-02 — 이택규 QW4 기존 cutline CSV 네 파일 발견 (OBSERVED, NO RUN)
- 학교 서버 `CMP_BASELINE_2.0.0_V2` 안에서 사용자 `find -maxdepth 4` 결과 기존 `qw4_eq_depth.csv`, `qw4_36_depth.csv`, `qw4_36_qw1fine.csv`, `qw4_36_qw4fine.csv` **파일 존재** 확인. **데이터 열·단위·값 및 출처 검증은 미완료**.
- `server_readonly_cmds_20261102.sh`는 동일 검색 범위에서 미발견. 이번 작업에서는 새 simulation/코드 변경/CSV 파싱 없음.
- NEXT READ ONLY CSV `wc -l`와 head 구조 확인 후 PE_Charge sheet integral 및 QW3/QW4 quasi-Fermi 후보 수송 병목 검산. 99.97% QW4 집중은 이전 PLT 결과이며 원인 UNRESOLVED. Baseline FREEZE HOLD.

## 2026-11-02 — 이택규 Claude QW4 독립 재평가 수신 (PROPOSED/HYPOTHESIS; NO NEW RUN)
- User forwarded Claude's reassessment dated 2026-11-02. Claude says it reviewed GitHub through commit `8553f64` but Issue #7 was inaccessible (403). ChatGPT subsequently fetched latest GitHub and Issue #7; verbatim Claude section 6 is preserved in Lee TIMELINE (2026-11-02).
- Claimed UG confirmations (not independently re-opened by ChatGPT): T-2022.03 p58/120 2D A/um, p193 Iterations, p871 Formula1/Fermi condition, p1003 activation, p1072 LED interface sheet example. Existing n2/n6 AreaFactor=1 and Wm4/Xs2 are confirmed from user server on 11/02, but native A/um semantics from the official UG remain **Claude-reported** and 4x4um pixel calibration/Full-Half are NOT proven.
- Claude DERIVED from pre-existing 10/23 QF table: QW barriers B0-B3 p/n~1e4–1e5, Ec−eQF~0.45–0.51eV, hQF−Ev~0.28–0.30eV; proposes inter-well **electron bottleneck hypothesis** behind n-side QW4 concentration. This interpretation is not independently confirmed by current distribution, raw CSV re-integration or controlled sensitivity. Claude retracts its prior ~1.6eV summed interface-loss claim and QF splitting-as-cause claim.
- QW4 QW-rad dominance remains n2 99.9687748%, n6 99.9929427% (existing PLT results). Baseline verdict B, physical FREEZE HOLD. Existing n1_msh minAngle 0.0167024°, minEdge 0.0195312nm warning unresolved; not proven cause.
- **NEXT FIRST (READ ONLY):** check existing CSV, signed interface `PE_Charge` to sheet-charge cm^-2 conversion, QW3/4 QF steps, active PAR Chi0/Eg0/mumax and runtime warning/source provenance. Do not execute unverified Claude script `server_readonly_cmds_20261102.sh` blindly.
- **NEXT OPTIONAL AFTER EXPLICIT LEE APPROVAL:** protected-copy `strain activation 0.5 -> 0` one-variable polarization sensitivity on same mesh, NtSide=0 and all else fixed. Confirm whether this controls piezo only or all polarization from exact installed T-2022.03 UG; it must not be presented as established total-polarization OFF. Claude's response thresholds QW4 80% / electron 100× are exploratory, not causal proof. NO code edits or device runs performed.

## 2026-10-31 — 이택규 n2/n6 area factor 1 + V2.1 Half geometry verified (OBSERVED/DERIVED; NO RUN)
- Actual n2 and n6 logs anode/cathode Ohmic contact `area factor : 1`. SDE Wm4→Xs2um half; edge Wedge0.1um, damage Wdmg0.005um, Xe1.895, Xd1.995, Xs2; Wshelf0, Bspan0, Cath0 bottom; anode across three segmented top edges per source.
- Sentaurus public tutorial says 2D native current A/um, default 1um out-of-plane. Assuming this convention, I2 at3.6V / 2e-8cm² =1.8236426A/cm²; I6 / 2e-8=0.4609854A/cm². **Conditional 2D-slice J**, not physical 4x4 square pixel calibration or Full/Half proof; T-2022.03 original UG not rechecked.
- QW4 OFF/ON >99.97% unresolved mechanism, Baseline physical FREEZE HOLD. NEXT read-only actual mesh/symmetry plus official 2D semantics before Full reference design or new controlled transport experiment. No source/run modifications.

## 2026-10-31 — 이택규 n2 actual log anode/cathode area factor 1 (OBSERVED; NO RUN)
- n2_des.log lines237/238 from direct user shell output: anode/cathode Ohmic `area factor : 1`. CMD/PAR grep previously yielded no explicit AreaFactor, but runtime contact factor now observed for **n2 only**; n6 still pending.
- `AreaFactor=1` at contacts does NOT independently validate actual 2D current/out-of-plane scaling or full-vs-half effective area. No SDE geometry text supplied in this turn. QW4 physical cause and baseline freeze HOLD unchanged. NEXT READ ONLY n6 area-factor + pp1_dvs.cmd half width/contact geometry + official UG.

## 2026-10-31 — 이택규 literal AreaFactor/current-unit grep: no match in 6 active files (OBSERVED; NO RUN)
- n2/n6 LOG+pp CMD/PAR grep only matched e/h/total CurrentDensity Vector plot requests and CurrentPlot IntegrationUnit=um. **No explicit AreaFactor/current-unit string** in inspected six files; implicit/default 2D terminal-current scaling remains UNRESOLVED and must not be inferred from absent literal. QW4 >99.97% at near-matched I and q*1e-12 current closure unchanged.
- NEXT READ ONLY inspect pp1_dvs.cmd real lateral width and electrode extent, check n2/n6 runtime log geometry/units, consult T-2022.03 UG current-unit/AreaFactor definitions; physical Baseline freeze HOLD and original TCAD untouched.

## 2026-10-31 — 이택규 current-bracket QW4 validation from existing PLT (OBSERVED + LINEAR DERIVED; NO NEW RUN)
- n6 3.6V I=9.21970771341943e−09, QW4 share=99.99294273758203%. Nearest n2 3.512V I=8.63290391977055e−09 QW4=99.97314950045252%; next 3.528V I=1.10599185065263e−08 QW4=99.9725752700292%; n6 I lies between.
- Linear-in-current n2 estimate at n6 I: alpha=0.2417800852, V~3.51586848V, QW4 share~99.97301066%; difference from n6 +0.01993207%p. Interpolation is not a new matched-current solver point. Both Trap OFF and ON maintain >99.97% QW4 Radiative localization. Trap-only causal claim unsupported.
- Physical QW4 mechanism, 2D/AreaFactor, experimental device calibration and Full/Half not validated; FREEZE HOLD. Next READ ONLY runtime current normalization/source provenance. Sensitivity RUN requires user approval.

## 2026-10-31 — 이택규 full PLT parser SUCCESS: QW4 99.9688% OFF, 99.9929% ON (OBSERVED; NO RUN)
- User executed in Bash read-only Python against existing 10/14 n2_des.plt/n6_des.plt. Final raw I: n2 3.64728524885323e-08, n6 9.21970771341943e-09. Four QW integrated Radiative QW4 fractions n2 **99.96877481383976%**, n6 **99.99294273758203%**. Thus OFF and ON both n-side QW4-dominated; not equal-current comparison.
- Global 4-channel raw rates captured: n2 Rad 1.52414203814656e23 / SRH 1.25722226677967e22 / Aug 6.26570284700597e22 / Trap 1.17883032026416e6; n6 Rad 2.55552035945039e22 / SRH 4.32337288643595e21 / Aug 7.83993596604716e21 / Trap 1.98258247754075e22. Derived Radiative four-channel share n2~66.9530%, n6~44.4096%; n6 Trap~34.4531%. Numeric conditional q*1e-12 current closure ~99.99904% in each, physical calibration & effective unit still unresolved.
- Previous tcsh heredoc quote prompt resolved via Bash and proper terminator. NO new model edit, solver run or outputs. Baseline physical FREEZE HOLD. Next READ ONLY compare at same current from PLT, 2D normalization/AreaFactor validation; QW4 physical cause UNRESOLVED.

## 2026-10-31 — Lee n2/n6 direct terminal and PLT confirmation (OBSERVED; NO NEW RUN)
- Original V2.1 n2_des.sta / n6_des.sta both done; at 3.600V anode currents n2=3.647e-08, n6=9.220e-09 (as displayed, native unit), ON/OFF ratio 0.25281 at **equal V, not equal current**.
- DF-ISE PLT metadata confirms per QW1-4 Clean/Edge/Dmg Rad/SRH/Auger and global channels/Trap-all; user pasted head25 & tail12, not the full label-to-final-row field mapping. Existing n2/n6 old 10/14 outputs; no new simulation or source edit. Old n6 total Trap-all 1.98258247754075e22 reappears in tail, consistent with October 21-22 documented audit.
- NEXT READ ONLY full PLT dataset-final-row extraction, global current budget including Trap, n2/n6 QW4 radiative shares, verify 2D unit/AreaFactor; baseline physical FREEZE HOLD, QW4~99.9688% cause unproven.

## 2026-10-31 — 이택규 pp2/pp6 deployed source grep (OBSERVED USER TERMINAL; NO RUN)
- Original V2.1 server pp2_des.cmd, pp6_des.cmd both show `Iterations=12` line174; separate Coupled initialization 200/100, not the main Iterations value. Earlier Claude SWB_PASTE 20 is *not* the verified preprocessed pp2/pp6 setting; full historic run-log linkage not independently rechecked.
- Both CMD: Piezo strain activation0.5, three material-interface Thermionic declarations, IntegrationUnit=um. Both PAR: ThermionicEmission Formula1. Old n2/n6 .plt & end .tdr remain on disk dated Oct14. No new simulation or modification. Terminal grep does not establish effective AreaFactor.
- PHYSICAL FREEZE HOLD. n-side QW4 ~99.9688% of QW radiative integral still UNRESOLVED. NEXT READ ONLY PLT/log structure + terminal/whole-device 4-channel current accounting, then matched-J comparison; no source edits/reruns.

## 2026-10-24 — JuSubin/Kou joint literature presentation plan (PROPOSED/WORKING SELECTION; NO TCAD RUN)
- User uploaded 2nd-week 19-slide CMP presentation and Kou et al. (2019) Optics Express full 11-page PDF. For 2026-10-26 Monday CMP progress and 10/29 Thursday joint review (7 min each), 이택규 will cover Kou 2019. 주수빈 requests a complementary paper selection and PPT plan.
- **Recommended working selection, not yet explicitly accepted by user:** Baek, W.J. et al., Nat Commun 14,1386 (2023), DOI 10.1038/s41467-023-36773-w. Updates earlier Zhao 2026 first-choice shortlist once Week-2 citations and uploaded Kou are considered. Joint narrative Kou sidewall problem -> Baek vertical QB/EBL mitigation -> CMP Project B lateral AlGaN edge is separate unvalidated design.
- Baek reported 6 InGaN/GaN QW, QB thickness 3.5/7.5/10.5nm and modified AlInGaN EBL; experimental 10–80um devices and SILVACO Atlas TCAD. 10um peak EQE QB3.5~2.90%, QB10.5~3.12%; Balanced EBL 10um 0.1A/cm² EQE 2.04% as-deposited, 3.00% passivated; JmaxEQE size shift 3.1 to 4.0A/cm², 80um to 10um. This study **does not test AlGaN material substitution in a mesa-sidewall Edge** or directly calibrate CMP 4um Sentaurus IQE. Prior Week-2 slides had cited Baek 2023, Chang 2020, Furtmayr 2011 in Project B rationale. Chang favors thinner QB in different circumstances; avoid universalizing sign of optimal thickness.
- Next presentation preparation: 6 slides Kou ~7min + 6 slides Baek ~7min using Baek Fig1 (device), Fig2 (surface current/EQE), Fig3 (TCAD carriers/energy), Fig4/5 (balanced EBL efficiency) and rigorous final comparison. 10/26 progress slides report completed Bspan node evidence only. No changes to baseline freeze HOLD, existing QW4 issue, or any code/runtime.

## 2026-10-23 — Lee n2 QW4 99.97% fine cutline CSV audit reported from old 10/14 TDR (OBSERVED-user / DERIVED / HYPOTHESIS; NO NEW RUN)
- **Source/provenance:** 2026-10-23 user-pasted Claude handoff says 이택규 used school-server SVisual batch qw4cut.tcl to export four CSVs (qw4_eq_depth.csv, qw4_36_depth.csv, qw4_36_qw4fine.csv, qw4_36_qw1fine.csv; ~17:27) from existing n2_eq_des.tdr and n2_end_des.tdr generated on 2026-10-14. All y=1.0um depth cuts, CSV X column 52 after header + SELECTED metadata row; data parsed with awk per report. **OBSERVED-user as relayed**, not directly inspected by GPT; no new device simulation or changes to active SDE/SDevice/.par.
- **Material/polarization report:** four sampled InGaN QW xMoleFraction=0.15 and BandGap=2.8569eV (vs EBL 3.7564eV, GaN 3.4376eV). n2 equilibrium PE_Charge interface values in cm^-3: pGaN/EBL -5.50e20; EBL/B0 +5.50e20; each QW p-side +1.23e21 and n-side -1.23e21; B4/nGaN~0. Claude calls expected Ga-polar charge-sign pattern. **Does not independently validate interface sheet charge cm^-2, polarization magnitude (PolAct=0.5), true crystal direction, or all spatial regions**.
- **Spatial carrier and rate report:** n2 end at V3.6 QW4 electron n peak 9.14e19 cm^-3 at x0.263um p-side interface, hole p peak 8.27e19 at x0.266um n-side interface, versus earlier center-only e/h O(1e18) values. Fine-cutline integration reported Rad~67.0%, Auger~27.6%, SRH~5.4% of QW4 3-channel total, QW4 Jrad~1.220 A/cm2, matching Claude's previous reported integral. Center radiative B=Rrad/(n*p)=2.000e-11cm^3/s. Local J at x0.14um~1.8236A/cm2 matches contact J normalized to 2um half width according to user/Claude, but this single check is not comprehensive current/recombination/2D area closure.
- **Quasi-Fermi:** report eQF/hQF eV at EBL(-0.973,-3.600), QW1(-0.969,-3.365), QW2(-0.735,-3.140), QW3(-0.485,-2.963), QW4(-0.245,-2.939); resulting ΔQF QW1/2/3/4 ~2.396/2.405/2.478/2.694eV (user table ~2.395 for QW1), QW4-QW1 ~0.298eV. Claude DERIVED ~0.97eV accumulated eQF steps and ~0.66eV hQF steps plus ~1.6eV interface energy cost. Their claim that this is direct cause of QW4 dominance and high Vf remains an **interpretation/hypothesis** not independently proven from transport sensitivities. Boltzmann np~exp(ΔQF/kT) approximation requires checking degeneracy and local Ec/Ev/QW effects.
- **Assessment:** reported composition match, bipolar Ga-polar-consistent field, successful per-QW fine integration and local J narrow earlier aggregate error candidates for these sampled slices. However **do NOT reclassify all geometry/setting/integration/polarity errors as universally excluded** without raw file verification. Claude hypothesis: polar heterointerfaces + Thermionic-only classical DD, lacking explicit interface tunneling/quantum correction, yields constrained flux and n-side first-well QW4 concentration. No experimental same 4um 4QW calibration. Claude's October 22 uniform-well n>>p inversion remains RETRACTED.
- **Open:** actual pp2/pp6 preprocessed Iterations=12 vs 20 uncertain, n6 not inspected this round, physical polarization sheet magnitude/PolAct0.5 appropriateness unverified, remaining full 2D current budget and mesh convergence unresolved. Baseline verdict B; PHYSICAL FREEZE HOLD. **Proposed sensitivity experiments require user approval and single-variable control**: compare continuous-QF heterointerface treatment vs Thermionic, or add tunneling separately only after Sentaurus T-2022.03 UG p.870/1070 verification. Original unchanged.
- Supersedes **only** previous NEXT stating "QW4 detailed TDR CSV cutline export still pending"; it is now user-reported completed. It does not supersede warning that original TDR/CSV and n6 remain unverified by GPT.

## 2026-10-23 — Lee Claude QW4 V2.1 independent audit handoff (PROPOSED; NO RUN)
- User delivered Claude's 2026-10-23 text review; no new simulation, code edit, or direct review of original n2/n6 PLT/TDR/deployed CMD/PAR. This is not physical validation. Original observed n2 n-side QW4 QW-radiation share ~99.9688% remains an UNRESOLVED blocker.
- Claude concludes summation artifact *less likely*, not ruled out, on reported non-overlapping SDE regions, QW4 centerpoint equal-B n*p proxy ~99.973%, and approximate 1.47 A/cm2 vs reported 1.22 A/cm2 QW4 radiative equivalence; the latter source data/units were not reverified here.
- RETRACTION (CLAUDE): old inferred n(QW4)~1.6e19,p(QW4)~8e16 cm-3 is withdrawn. Existing actual SVisual center n=1.35190e18,p=1.13508e18 cm-3 takes precedence. Claude's estimates center Auger/Rad=0.062 vs integrated 0.411; SRH/Rad=0.201 vs integrated 0.082; effective n+p~1.6e19, QW4/QW1 quasi-Fermi splitting difference ~0.30eV are DERIVED/ASSUMPTION-DEPENDENT claims only. Interface density peaks remain a hypothesis, not observed.
- Claude proposed but did NOT prove classical DD/Thermionic/no quantum correction leading to n-side QW4 accumulation. Confirm no actual model/concentration/charge error by xMoleFraction, BandGap and signed PE_Charge profile. Previous q*integrated QW Rad/I ~66.95% ~ QW 3-channel Rad~66.96% does not independently prove negligible leakage without 2D current units and complete budget.
- Claude reports source comparison: attached CMD line174 Iterations=12 versus Claude SWB_PASTE + LOG#02 Iterations=20, local diff confirmed to Claude; GPT lacks both originals and still needs actual pp2/pp6 deployed compare. No code change was made. The offered Claude-local scripts qw4_plt_audit.py (synthetic parser test only) and qw4cut.tcl have NOT been reviewed or executed by GPT.
- HOLD physical baseline freeze. NEXT READ ONLY: (1) deployed pp2/pp6 CMD/PAR source and physics + Iterations mismatch, (2) n2/n6 PLT matched J, full recombination and 2D unit budget using audited script, (3) old TDR quantitative QW1/QW4 inside-well carrier maps, composition/bandgap, PE_Charge sign, quasi-Fermi. Existing SWB original unchanged.

## 2026-10-23 — Lee n2 3.6V signed PE_Charge linear cutline resolved (OBSERVED SVisual; NO RUN)
- User switched PE_Charge Cutline_Y plot ordinate from Log Scale to Linear in existing n2_end_des, and screenshot now shows positive and negative sharp spikes on both sides of zero. Previous confirmed cutline X(depth)=0.14..0.29um at lateral Y=1.0um. Visible spike groups near nominal MQW interfaces x~0.19,0.215,0.24,0.265um, and EBL/barrier upstream. Plot ticks +/-1e21 cm^-3; approximate local spikes of order 1e21 cm^-3 only, NOT exported numeric maxima.
- Direct OBSERVED: nonzero signed PE_Charge spikes spatially associated with presumed QW/barrier heterointerfaces. QW mapping still rests on prior source-derived positions; screenshot alone does not establish which exact polarity sign belongs to each named interface or whether the sign matches correct Ga-polar microscopic orientation. Volumetric cm^-3 peaks are NOT interface sheet charge cm^-2.
- Thus visualization issue RESOLVED; signed numerical/polarity physics validation remains UNRESOLVED. Existing n2 QW4 ~99.9688% radiative share and ~300x center e/h vs QW1 remain unexplained. No device source change or new simulation.
- NEXT prioritize read-only normalization: actual SWB area/contact width and terminal current units, then full-device recombination and matched J n2/n6; validate detailed interface charge signs if needed from accurate region coordinates and exact numeric probes instead of repeated GUI curves.

## 2026-10-23 — Lee n2 3.6V PE_Charge Y=1.0um cutline screenshot (OBSERVED; READ ONLY)
- User SVisual screenshot of existing `n2_end_des` PE_Charge confirms Cutline Properties endpoints (x1,y1)=(0.14,1.0)um and (x2,y2)=(0.29,1.0)um. It is a depth cut across the MQW at lateral Y=1um; no new calculation.
- OBSERVED: narrow, tall PE_Charge plot spikes cluster around nominal heterointerface positions in active stack; 2D color legend displays positive and negative ranges of approximately 10^21 cm^-3. The Cutline_Y graph's vertical scale is logarithmic (tick labels 1e+21 down to tiny positive values), hence the signed interface charge cannot reliably be read from this 1D graph or attributed positive/negative by QW interface.
- LIMIT: plotting nonzero PE_Charge is not proof of correct polarization sign, true crystal polarity, interfacial sheet charge magnitude, QW4 carrier-accumulation mechanism, or calibrated 4um physics; the colorbar limits are not local peak values.
- NEXT SINGLE READ ONLY STEP: change vertical PE_Charge plot axis to Linear (disable Logarithmic), autoscale, and inspect positive vs negative spikes about zero at verified region interfaces before judging sign. Preserve the original deck and TDR.

## 2026-10-23 — Lee V2.1 actual lattice axis parameter declarations verified (OBSERVED SERVER OUTPUT; NO RUN)
- User ran read-only `grep -nEi -C 4 "LatticeParameters|Piezoelectric_Polarization|SpontaneousPolarization|Polarization" pp2_des.cmd pp2_des.par pp6_des.cmd pp6_des.par` in /user/semi/semi437/CMP_BASELINE_2.0.0_V2.
- OBSERVED in both `pp2_des.par:1-4` and `pp6_des.par:1-4`: `LatticeParameters { X = (0, 0, -1) Y = (1, 0, 0) }`; both command files line21: `Piezoelectric_Polarization( strain activation=0.5 )`. Prior pp1_dvs.cmd line14 says Ga-polar c-axis points to -x. Thus actual preprocessed parameter vectors match the design COMMENT and n2/n6 match on these inspected lines.
- LIMIT: the alignment of source comment with values does NOT independently verify true Ga-polar polarity, actual piezoelectric/spontaneous charge signs, magnitudes, physical correctness, or why n2 QW4 has concentrated e/h and ~99.97% QW radiation. Need inspect actual PE_Charge field at interfaces and active polarization constants/runtime log to establish effects; grep finds declarations, not resulting net charge.
- NEXT READ ONLY: use n2_end_des.tdr existing result to inspect `PE_Charge` near all four wells at lateral Y=1.0um, with well coordinate mapping X=[0.188-0.191,0.213-0.216,0.238-0.241,0.263-0.266]um as PRIOR SOURCE-DERIVED; verify legend sign/units and whether field is resolvable, no fresh simulation. Also audit current normalization/matched-J. No TCAD code change.

## 2026-10-23 — Lee V2.1 actual preprocessed Piezo/Thermionic source check (USER-OBSERVED; READ ONLY)
- School server path: /user/semi/semi437/CMP_BASELINE_2.0.0_V2. User ran Bash read-only grep/ls; pp1_dvs.cmd, pp2_des.cmd, pp2_des.par, pp6_des.cmd, pp6_des.par exist with Oct 14 timestamps.
- OBSERVED exact pp2_des.cmd:21 and pp6_des.cmd:21: `Piezoelectric_Polarization( strain activation=0.5 )`. Both command files at lines24–26 declare `Thermionic` for InGaN/GaN, AlGaN/GaN and AlGaN/InGaN material interfaces; lines65/67 request `PE_Charge PE_Polarization/Vector` and xMoleFraction output. Both par files lines166/169/172 include `ThermionicEmission { Formula = 1 }`.
- pp1_dvs.cmd line14 COMMENT claims Ga-polar c-axis points to -x and suggests `LatticeParameters X=(0,0,-1) Y=(1,0,0)`. This is a comment, not independent verification of the active lattice orientation or polarization charge sign. Piezo strain activation 0.5 is the confirmed code setting; spontaneous polarization and actual PE_Charge sign/value NOT YET VERIFIED. Presence of plot requests does not prove field values.
- n2/n6 code-line settings agree for these searched terms only; full-source equivalence and original run/gtree correspondence are still UNRESOLVED. No simulations or source edits.
- NEXT READ ONLY: inspect actual `LatticeParameters` and relevant polarization parameter blocks within pp2_des.par/pp6_des.par and device cmd, then compare computed PE_Charge sign at verified QW interfaces; only then discuss QW4 concentration mechanism.

## 2026-10-23 — Lee SVisual 3.6V Ec/Ev/eQF/hQF inspection closed (OBSERVED screenshot, NO RUN)
- Existing n2_end_des cutline depth X~0.14–0.29um (prior Y=1.0um setup) now overlays Ec magenta, Ev cyan, eQF red, hQF blue; n2_eq_des equilibrium eQF green near zero. Four well-associated band features and stepped biased quasi-Fermi profiles are visible.
- This is qualitative GUI evidence, not validation of polarization sign, injection barrier height, numerical band offsets, or reason for QW4 electron+hole crowding and ~99.9688% region QW radiation. QW4 center density products previously show strong correspondence, not causation or physical calibration.
- SVisual first-pass GUI task DONE; next READ ONLY source/parameter polarization sign + region mapping, 2D terminal J normalization, n2/n6 matched-J and recombination integrals; Full/Half still open. No model/file/run changes.

## 2026-10-22 — Lee n2 3.6V four-QW center density probes and Bnp check (OBSERVED + DERIVED; NO RUN)
- User-provided SVisual n2_end_des, Cut Y both hDensity(Curve_1) and eDensity(Curve_2) at lateral Y=1.0um. Nominal QW centers from existing V2.1 vertical source stack: x[um]=QW1 0.1895, QW2 0.2145, QW3 0.2395, QW4 0.2645. Probe readouts [cm^-3]: QW1 p=3.42849e15,n=4.46006e15; QW2 p=4.47871e15,n=4.99354e15; QW3 p=1.82582e16,n=2.04189e16; QW4 p=1.13508e18,n=1.35190e18. GUI numeric readout = OBSERVED screenshot; nominal material-center alignment = DERIVED from earlier verified preprocessed stack; not re-probed region labels.
- Derived center n*p [cm^-6]: QW1=1.52912711e31; QW2=2.23646175e31; QW3=3.72812360e32; QW4=1.53451465e36. QW4 center n*p / sum(QW1-3 center n*p) ≈ 3738.45. Equal-B point-product QW4 share ≈99.973258%, numerically close to prior actual 2D QW radiative-integral QW4 share ~99.9688%. QW4 p/pQW1≈331.07, n/nQW1≈303.11; n/p(QW4)≈1.191. Thus evidence supports a strong carrier-overlap correlation for QW4 radiative dominance; Claude's hypothesized n~1.6e19 and p~8e16 at QW4 is not reproduced at THIS x,y.
- CRITICAL CAUTION: single-point B*n*p surrogate is NOT 2D integrated spontaneous-radiative-recombination evidence, and cannot establish cause of carrier buildup or physical correctness. Full field, polarization sign, equilibrium/biased band profile, quasi-Fermi, actual net charge and 2D QW-region integrals are not fully validated. Avoid claiming numerical 99.973% as actual IQE or proof of model validity.
- NEXT READ ONLY (priority updated): stop repetitive spot-probing; compare QW1 vs QW4 equilibrium and biased Ec/Ev (and electron/hole quasi-Fermi), polarization charge sign and carrier profiles on same lateral Y=1.0um; confirm well region mapping. Then review existing full 2D QW radiative and current balance, matched-J n2/n6. NO code edits/new simulations.


## 2026-10-22 — Lee Claude independent V2.1 review received (USER-SUPPLIED PROPOSED, NO RUN)
- Claude reviewer proposes verdict B (retain structure, mandatory validation), medium-low confidence. This is NOT a frozen physically validated Baseline. User handoff only; server active deck and original n2/n6 PLT/TDR not inspected by reviewer.
- QW4 ~99.97% QW radiative share, low-J Auger~27.5%, n6 current about one-quarter of n2 remain unresolved diagnostics. Reviewer-derived QW4 n~1.6e19/p~8e16cm^-3, n_id~2.3, equivalent S~1e4cm/s are unreplicated, NOT confirmed observations.
- Primary next READ ONLY: inspect n2_eq_des.tdr and n2_end_des.tdr existence and SVisual fields, vertical y=1.0um cutline x=0–0.40um for polarization-related charge/Ec/Ev/eDensity/hDensity/QF; then check actual active deck/gtree, PLT current normalization, q*integrated QW radiation / I and matched-J comparisons. Do not change code or run new simulation yet.
- Claude UG references cited as pp.58–59,253,473,580 only; supplied original report, script and UG itself NOT independently accessed. See Lee TIMELINE and Issue #7 comment 6337013873.

## 2026-10-22 — Lee Project A: 4um Baseline reference framework and IQE metric audit (SOURCE-VERIFIED, MODEL_UNCALIBRATED)
- USER concern is scientifically valid: CMP V2.1 is a self-designed **hybrid representative 4um mesa** model, NOT Kou 2019 model reproduction (Kou laterals 20/60/100um). Kou's 4-QW In0.15/3nm, barrier22nm, EBL26nm and vertical GaN doping/thickness can serve as design-source EPI; Wu 2023 5nm acceptor sidewall is separate physical starting assumption. Neither supplies size-matched 4um TCAD efficiency benchmark, and 4um pitch JBD != verified mesa.
- DIRECT real-size literature: Chen et al ACS Applied Electronic Materials 2024 DOI 10.1021/acsaelm.4c01540 fabricated 4x4um² blue LEDs, nitrogen treatment light output +97.29% at J25A/cm² (relative optical output, NOT IQE). Wang et al Nature Communications 2023 DOI 10.1038/s41467-023-43472-z fabricated 3.5x3.5um² blue, **16 MQWs** and NBE, peak **EQE** 37.5% around J3A/cm² (NOT 4-QW IQE). Also Ryu&Geum Opt Express 2026 DOI 10.1364/OE.580848 gives size-dependent SRV/diffusion length IQE framework, no literal equal-parameter benchmark. Validated 4um physical existence/trends, not a single exact device/parameter ground truth.
- IQE definitions need precision: QW recombination internal efficiency `∫QW Rrad/(∫QW Rrad+SRH+Auger)` is a **QW-only three-channel** property; full-device current-normalized internal photon-generation yield `q∫QW Rrad / I_terminal` (with exact 2D width/conservation/leakage checked) accounts for sidewall/trap/carrier loss and is apt Project A comparison; whole-device `∫Rad/(∫Rad+SRH+Aug+Trap)` approximates same when full recombination current closes, but not external photon EQE or independently validated absolute IQE. EQE=η_injection×η_QW_rad×LEE under consistent definitions. Existing n2 QW-rad~66.9624%, n6 QW-rad~67.7744%, n6 global trap-inclusive rad fraction~44.4096%, n2 tentative current-normalized ~66.9506%; ALL model outputs not measured physical standards and ON/OFF at equal voltage 3.6V, different current.
- KEY CRITICAL GEOMETRY GAP: planar 2D full width 4um models an infinitely long stripe with two lateral sidewalls, P/A_eff =2/W=0.5 per um; physical square 4x4um has four walls P/A=4/W=1 per um, factor 2 geometry difference even at same width (assuming straight walls). Half2um doubling to planar Full4um checks numerical reflection/symmetry, NOT true square's sidewall P/A, edge/corner, nor real 3D leakage. Do not multiply Nt by 2 indiscriminately: space charge/current spreading nonlinear and calibration needed.
- PARAMETER BASIS CURRENTLY UNRESOLVED: 4um mesa representative hypothesis; 5nm sidewall damaged width from Wu; acceptor Nt1e18, Et Ev+.75eV, sigma1e-15 are **calibration starting choices**, not measured 4um C-device values. Active model PolAct0.5, mobility, pGaN hole activation, QW radiative B, Auger C, contact/AreaFactor need an explicit reference/provenance table and tests. n2 3.6V QW4 radiative ~99.9688% and Auger QW-3chan~27.53% remain red flags, not failed physics proof.
- **RESEARCH DECISION PROPOSED (NOT USER FINAL FREEZE):** Retain Kou EPI as documented representative design; add Chen 4um and Wang 3.5um as SIZE-SPECIFIC experimental phenotype/benchmark, Wu as 5nm sidewall mechanism, ABC/SRV size dependence as IQE modeling source, and GaN:C compensation source for Project A when separately validated. No paper offers exact "4um with Kou QWs plus Wu traps" IQE target. Treat n2/n6 as operational pilot, not publication-calibrated baseline; no need restart everything.
- NEXT first phase without sim edit: freeze/report **parameter provenance matrix** (DIRECT literature / adopted modeling assumption / numerically adjusted), **current normalization and 2D-vs-square P/A**, **IQE metric definitions**, then extract existing n2/n6 modeled radiative/trap metrics versus common J; check QW4/physics. Only afterwards compare GaN:C ON+carbon to same ON damage no-carbon control, not to unrealistic Trap OFF as primary experimental performance. Protect both workstreams' original projects.

## 2026-10-22 — 이택규 Project A 4um Kou EPI transferability review (DERIVED, NOT A FAILURE PROOF)
- Kou 2019 modeled lateral 20/60/100um while our representative CMP lateral 4um; same Kou EPI vertical layer thicknesses can be initial 4um research hypothesis (no proportional epi scaling rule). Kou 4um-wide damaged dead zone, contact arrangement, J20A/cm2 voltage, and EQE do NOT transfer quantitatively to our 4um Wu-inspired 5nm defect Sentaurus planar Half model. JBD pixel pitch4um != actual mesa dimension; planar 2D lacks real square corners/sidewall total perimeter.
- New size-matched experimental check: Wang Nature Communications (2023) 3.5x3.5um blue microLED, NBE 16QW, peak EQE near J~3A/cm2 (37.5% peak), https://www.nature.com/articles/s41467-023-43472-z; Chen 2024 ACS 4x4um treated device optical power +97.29% at J25, https://doi.org/10.1021/acsaelm.4c01540. Different epi and contact/trap methods mean qualitative feasibility only, not absolute comparison.
- **Prior warning corrected**: n2 V2.1 J~1.824A/cm2 at V3.6 versus Kou J20 at V~3.3 is unmatched geometry and should NOT be interpreted as proven deficient injection in 4um. Need verify 2D area normalization, current/contacts/band physics, QW4 99.97% radiation and 5nm Trap sensitivity. Existing Half code/data untouched.

## 2026-10-22 — JuSubin clarifies SWB staged serial execution for Project B (USER-REPORTED QUEUE INTENT)
- User clarifies copied SWB `/user/semi/semi437/CMP_B0/CMP_BASELINE_2.0.0_V2` is scheduled to run Bspan=0→1→3 sequentially. Earlier absence of `pp31_dvs.cmd` does NOT justify separately launching n31; likely next stage not yet reached. Do not claim live scheduler status or assured run from image alone; current actual n17 mesh and n24 iteration were observed.
- CORRECTED action: do not manually submit duplicate n31 or restart any SDevice. While SWB runs, **read-only inspect n17_msh.tdr in SVisual** for Bspan1 `Edge_QW1..4` AlGaN, `Clean_QW` & `Dmg_QW` InGaN, material/mesh and intact damage region. Prepare controlled comparison for Trap ON branches n6(Bspan0), n30(Bspan1), n44(Bspan3), and Trap OFF branches n2/n24/n38, with current-matched voltage, QW Rad/SRH/Auger, Dmg trap recomb, carrier/band profiles and changed QW active volume. No software/deck changes or new run by assistant.
- Pending user SVisual screenshot on existing `n17_msh.tdr`; no new TCAD results as of this note. Common Baseline physical freeze still provisional.

## 2026-10-22 — Kou full text Open Access and "no injection" wording corrected (SOURCE VERIFIED)
- User questioned Kou 4um size, paywall and meaning of "current injection not working." Independently opened Optica Publishing Group official full-text page https://doi.org/10.1364/OE.27.00A643; journal page explicitly marks **Open Access** and displays full Sections 1–4, figures/captions. No paid purchase required to read HTML full text; separate PDF direct-open not needed nor claimed.
- Kou 2019 Section2: nGaN **thickness**=4um; **4 quantum wells**; lateral chip sizes are 20x20,60x60,100x100 um², NOT 4um mesa. Our CMP intended representative mesa 4um (JBD pitch should not be equated to mesa width), Kou used as vertical epitaxy backbone; earlier reference-size correction stands.
- At **applied terminal voltage** V=3.6V, CMP V2.1 nonzero n2 current raw3.64728525e-8 and n6 raw9.21970771e-9; conditional planar J~1.824/0.461 A/cm². Kou Fig3 reports **20 A/cm²** at V3.23–3.48V for different-sized and different-model devices. Therefore at same order terminal bias CMP shows much lower normalized current; "전류 주입이 안 된다" wrongly suggests zero injection or a proven mechanism. Correct statement: model has measurable forward current and radiative recombination but **relative forward J is low**, while whether it reflects injection barriers, interface polarization, Mg hole activation, mobility/contact series resistance or geometric/trap-model differences remains **unresolved**.
- Distinguish terminal J(V) (total electrical conduction) from injection efficiency (portion of carriers entering/recombining in MQWs). Same terminal V need not result in same J if internal voltage drops/barriers/resistance and structure differ; terminal V is not direct voltage across wells. Lower terminal J alone is NOT direct evidence that carriers fail to enter wells nor proof of poor injection efficiency. Kou abstract and Sections3 indicate trap-caused carrier loss via sidewall SRH; their traps form leakage path (different direction than CMP ON current reduction), requiring matched current/physics audit.
- NEXT: compare same area-normalized J and evaluate injection through carrier currents/profile, bands/quasi-Fermi and per-QW radiative/sidewall traps; preserve V2.1 baseline. No simulations or code changed.
## 2026-10-22 — JuSubin Bspan3 pp31 preprocessed file absent in clone (USER OBSERVED, NOT TCAD FAILURE)
- User ran `bash -lc 'cd ... && grep -n "define Bspan" pp31_dvs.cmd && ls -lh n31_msh.tdr'` in `CMP_B0/CMP_BASELINE_2.0.0_V2`; grep reported **`pp31_dvs.cmd: No such file or directory`**. `&&` short-circuited `ls`, so n31 mesh not checked and SDE failure/run state remains unresolved.
- Earlier SWB n31 parameter cell was white, n17 yellow. NEXT look at actual live n31 SWB scheduler status; only run isolated n31 SDE if ready/not queued. Keep source and other running nodes untouched. No physics/code changes.

## 2026-10-22 — 이택규 Kou 2019 benchmark at J20 flags low V2.1 injection and trap-direction differences
- Worker reaffirmed: **이택규 Project A (carbon-induced high-resistivity GaN:C sidewall edge)**; 주수빈 Project B (AlGaN). Prevent mixing user ownership or claiming both are completed.
- Primary reference Kou et al., *Impact of the surface recombination on InGaN/GaN-based blue micro-light emitting diodes*, Optics Express 27 A643-A653 (2019), DOI https://doi.org/10.1364/OE.27.00A643. Paper Section 2 vertical epitaxy: nGaN 4um donor 5e18 cm^-3, 4×In0.15Ga0.85N QW 3nm, barrier 22nm, EBL 26nm Al0.15Ga0.85N, pGaN 120nm, p-layer holes 3e17 cm^-3, p+ cap20nm, ~445nm. Most of intended V2.1 stack matches design dimensions, BUT actual pGaN free hole profile and optical ~445nm emission unverified; ours has changed contact/half setup and 4um nominal mesa.
- Paper's size models are **20x20, 60x60, 100x100 um²**, not 4um. Kou damaged **dead zone width 4um**; sidewall electron trap Ec−0.24eV density1e13 cm^-3 sigma3.4e−17cm²; hole trap Ev+0.46eV density1.6e13 cm^-3 sigma2.1e−15cm². Their numerical method APSYS, Auger coefficient1e−30 cm^6/s, SRH lifetime1e−7s; ours Sentaurus V2.1 Wu-inspired **5nm** damaged region acceptor trap Ev+0.75eV Nt=1e18cm^-3 sigma_n/p=1e−15cm² calibration starting values and Auger 5e−31 (reported pp2_des.par). DO NOT claim Kou's IQE/Trap parameter numerical replication. Wu et al. 2023 DOI https://doi.org/10.1016/j.micrna.2023.207542 uses 5nm sidewall acceptor-like traps, representative example 10um with 4 QWs In0.08, GaN barrier8nm (different epi).
- **Direct numeric benchmark Kou Fig.3:** At J=20 A/cm², forward voltage Trap-free (sizes 100/60/20um) 3.48/3.37/3.33V; defective counterparts 3.47/3.33/3.23V. Existing school-server V2.1 at 3.6V, using provisional 2D planar 2um×1um area, J_n2_OFF=1.823642625 A/cm² and J_n6_ON=0.4609853855 A/cm². Compared with paper's benchmark 20 A/cm² at LOWER 3.23–3.48V, ours at higher 3.6V is ~10.967× (OFF), ~43.385× (ON) less than 20 A/cm². This is a material mismatch/check flag, NOT conclusive physical error due to major size, geometry, trap, contacts, models, normalization differences. Do not extrapolate paper I-V to precisely 4um without new data.
- **Trap direction flag:** Kou Fig.3 trap-affected 20um device achieves J20 at 3.23V vs no trap 3.33V (leakage channel effect); ours at equal 3.6V ON/OFF current ratio0.2528 (Trap ON suppresses terminal I). Not directly comparable bias or material; warrants verifying actual sidewall depletion, terminal current path, trap recombination and leakage. Matched-J IQE and Project A high-resistance edge mechanism cannot be concluded from terminal current alone.
- Existing V2.1 n2 PLT QW4 contributes ~99.9688% of QW total radiative; Kou/Wu retrieved text does not provide identical per-QW 4um metric for quantitative validation. e/h-density 1D cut peaks deepest-highest, but does not establish 2D physical plausibility. Under provisional J_n2~1.824A/cm², QW Auger three-channel fraction27.53%; literature typical lower-current Auger smaller (https://pmc.ncbi.nlm.nih.gov/articles/PMC8175512/) -> investigation priority, NOT automatic model error because local carriers can accumulate strongly.
- **VERDICT:** Structural epitaxy broadly matched; qualitative sidewall damage reduces recombination in Wu/Kou and n6 relative to n2 (same 3.6V) aligns; V2.1 is NOT QUANTITATIVELY BENCHMARKED to Kou-level forward injection, not an independent calibrated IQE/EQE or 445nm proof; may not safely freeze baseline for final Project A claim.
- NEXT READ-ONLY: 1) use existing n2/n6 PLT to extract J-V at equal J within common range and modelled radiative/trap balance; verify exact 2D contact/current scaling and target current injection. 2) Inspect current active physics, EBL/hole injection and transport, EPI material settings and polarization against Kou assumptions—no speculative code editing. 3) Check QW4 99.97% and Auger share physical reason with spatial integrated data. 4) independent protected Full-vs-Half run for symmetry once Half audit passes. Existing V2.1 source and finished runs untouched. Project A may advance as isolated exploratory pilot but cannot make calibrated performance/efficiency claims before benchmark.
## 2026-10-22 — JuSubin Bspan1 SDE mesh confirmed, n24 Newton underway in log, Bspan3 n31 not yet verified
- Read-only Bash diagnostic now works (previous login shell `for: Command not found` workaround confirmed). In copied project `CMP_B0/CMP_BASELINE_2.0.0_V2`, `pp17_dvs.cmd` Bspan1 and `n17_msh.tdr` 2.0MB Oct22 15:29 observed. `n24_des.log` last Newton entries RHS2.63e10→5.25e8→2e4; no solver completion proof. Logs n30,n38,n44 absent, n31 preprocess/mesh file not located; schedule status unresolved. No physical success claim.
- NEXT: inspect n31 SDE SWB status; run only if ready/not queued or running; verify Bspan3 new mesh/material first. Preserve n24 existing progress and original Baseline.

## 2026-10-22 — JuSubin Project B Bspan 0/1/3 node matrix screenshot and RUN reported (USER OBSERVED/REPORTED; COMPLETION UNVERIFIED)
- User SWB screenshot header: `/user/semi/semi437/CMP_B0/CMP_BASELINE_2.0.0_V2` (separate visible path from older root `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`; protect parent). User states already cloned, split and running Bspan=1/3; no proof of individual terminal solve success, so mark SWB setup OBSERVED and simulation launch USER-REPORTED.
- Screenshot shows one copied SWB project with 3 Bspan groups: `Bspan=0` SDE n1, SDevice Trap OFF n2 (NtSide=0), ON n6 (NtSide=1e18); `Bspan=1` SDE n17, OFF n24, ON n30; `Bspan=3` SDE n31, OFF n38, ON n44. `Wedge=0.1`, `PolAct=0.5`, `NCedge=0`, `V1=2.0`, `Vmax=3.6`, `NPlot=8` appear shared. Color cells in screenshot do NOT prove every run done; n31 SDE appears not yellow done; must verify actual preprocessed `pp17_dvs.cmd`, `pp31_dvs.cmd`, timestamp of `n17_msh.tdr`, `n31_msh.tdr`, and final SDevice logs n24/n30/n38/n44.
- **No source modification indicated/needed at first pass:** observed SDE in-Bspan? mapping prewires 1 & 3 lateral AlGaN replacements; SDevice AlGaN/GaN and AlGaN/InGaN Thermionic blocks and polarization already present. Don't edit protected original or copied *generated* pp*. If error occurs use actual log and minimal justified change in copied user project only. Do not launch duplicate RUN before inspecting jobs.
- NEXT: in screenshot-specific copied project folder read-only inventory + grep SDE parameter substitutions and n24/30/38/44 logs. Ensure Bspan1 and 3 use new meshes, verify region material/xMoleFraction/5nm Dmg and contacts. Once completed, current and matched-current QW/sidewall recombination analysis. Unresolved baseline physical freeze/2D current normalization and QW4 issue remain; result not publication-confirmed.

## 2026-10-22 — 이택규 total IQE proxy clarified
- User asks whole-device IQE from existing 3.6V n2/n6 PLT values. QW-only 3-channel radiative shares: n2~66.9624%, n6~67.7744% (do not label full IQE). n6 all-device Rad/(Rad+SRH+Aug+eGapStates trap)=44.4095889%, based on observed raw globals Rad2.55552035945039e22, SRH4.32337288643595e21, Aug7.83993596604716e21, Trap1.98258247754075e22. Trap 34.4531291% of all four channel rates. This is conditional modeled radiative recombination fraction, not calibrated actual IQE.
- n2 total-device Rad/SRH/Aug channels not completely extracted; trap negligible and QW 3-channel rad share~66.9624%, or conditional q×QW Rad*1e-12/I≈66.95058% are approximate full-radiative proxies only. Equal-voltage n2/n6 have different current, so cannot assert matched-current trap efficiency impact. QW4 99.97% spatial radiative share is distinct issue. No source/run edits.

## 2026-10-22 — Project B operational clone and pilot greenlit by JuSubin (PROPOSED, NOT RUN)
- User instructed proceeding to Project B implementation TODAY while assuming V2.1 Baseline completed. This is NOT confirmation of current-density/Full-Half/physical validation, and no original V2.1 source can be overwritten.
- Candidate new versioned project CMP_PROJECTB_1.0.0_ALBARRIER Save As parent; Bspan=3 in new SWB only, retain xAlB .15, Wedge .1um, damage .005um and same NtSide ON split. SDE geometry/mesh smoke then a single 3.6V ON pilot, preserving original parameters and source. NO ACTUAL SERVER RUN YET. Runbook CMP/members/JuSubin/PROJECT_B_IMPLEMENTATION_RUNBOOK_20261022.md.

## 2026-10-22 — Verified V2.1 epi stack implies QW positions matching h/eDensity cutline peaks (DERIVED)
- GitHub read of prior JuSubin pp1_dvs.cmd source observations: pCap.020, pGaN.120, EBL.026, B0..B4 .022, each QW .003um; with top X=0 yields QW1=.188-.191, QW2=.213-.216, QW3=.238-.241, QW4=.263-.266um. User plotted e/h density peaks ~.190/.215/.240/.265um coincide with these expected layer windows at graph resolution.
- Geometry alignment supports well-localized peaks qualitatively. It does not independently validate exact peak e/h values, full-domain electron-hole overlap, or cause of extreme QW4-integrated Radiative dominance. Leave Half code/run untouched; next meaningful step is physics benchmark/Full-Half reference as planned.

## 2026-10-22 — 이택규 n2 eDensity QW-range cutline observed; both carrier peaks deepest-highest qualitatively
- User screenshot `eDensity(C2(n2_end_des))` along lateral Y~1.3um with depth X~0.14–0.29um: four sharp electron-density peaks around ~0.19,0.215,0.24,0.265um, visually highest at deepest peak, with concentration rising toward n-side beyond it. Previous hDensity cutline had deepest peak highest.
- These are image-level qualitative patterns, not exported point values nor verified well-versus-barrier assignment. Extreme n2 QW4 integrated radiative fraction ~99.9688% remains unexplained quantitatively: local h/e peaks alone do not prove 2D recombination causality. Skip repeat zooming; next targeted physical plausibility/region-alignment check, then protected Full/Half validation. No source/runs changed.

## 2026-10-22 — 이택규 n2 eDensity existing Cutline_Y plotted; X depth zoom reset
- Screenshot `eDensity(C2(n2_end_des))` shows electron density on same lateral Cutline_Y C2 (~1.3um) as preceding hDensity analysis. Plot horizontal depth axis reset to X~0–4.288um after field switch; QW1–4 near depth X0.17–0.27um not yet individually resolved. No QW4 electron concentration or injection mechanism conclusion from screenshot.
- NEXT set right XY horizontal X depth fixed Min0.14 Max0.29um and inspect electron peaks. Preserve SDevice runs and source; do not claim causality yet.

## 2026-10-22 — 주수빈 Project B first nominal band-alignment preflight complete (OBSERVED+DERIVED; NO RUN)
- Actual V2.1 pp2_des.par: GaN Eg0/Chi0 = 3.4376/4.1000 eV, InGaN 2.8569/4.5065 eV; previous AlGaN 3.7564/3.8768 eV, all Tpar300K. Corresponding nominal affinity-rule GaN→AlGaN electron/hole barriers 0.2232/0.0956 eV; InGaN→AlGaN 0.6297/0.2698 eV. This ignores polarization, charge, actual bending, heterointerface effects and bias; not validated TCAD Ec/Ev.
- Initial Project B pilot geometry proposed after freeze: Bspan3, xAlB0.15, Wedge0.1um, Dmg0.005um unchanged; paired against same-Trap Bspan0 control at matched current. xAlB composition sweep deferred pending effective Eg/Chi model consistency. The 0.1um QW edge material-replacement portion is 5% of 2um half width.
- Project B design-preparation core inspection complete; next verify Lee's finished frozen-baseline source/mesh/provenance, then make separate versioned Project B clone → geometry/mesh/alloy smoke → 1 pilot electrical case and band/polarization/carrier/trap-region audit. Do not alter baseline. Detail in members/JuSubin/PROJECT_B_PLAN_20261022.md.

## 2026-10-22 — 이택규 n2 QW hole density 1D peaks resolved in Cutline_Y (OBSERVED GRAPH)
- SVisual screenshot `hDensity(C2(n2_end_des))`, Y lateral≈1.3um, depth X≈0.14–0.29um, log vertical axis 1e10..1e20 cm^-3 resolves 4 well-localized peaks around X~0.190, 0.215, 0.240, 0.265um. Rough screenshot estimates peaks ~9e18, 1e19, 2e19, 8e19 cm^-3 for QW1–4; graph reading only, not exported numeric values. QW4 highest hole-density peak on this line.
- This qualitative carrier localization is consistent with prior QW4 radiative integral ~99.97% but is not a causal proof: carrier overlap/electrons and 2D regional averaging still needed. NEXT plot n2 `eDensity` along same Cutline_Y and depth ROI, no TCAD edits/runs.

## 2026-10-22 — 이택규 hDensity Cutline_Y depth ROI achieved, high peaks clipped
- User SVisual screenshot: `n2_end_des` / `hDensity` vertical Cutline_Y C2 at lateral Y~1.3 µm; XY horizontal depth X fixed 0.14–0.29 µm, so QW-depth oscillations near X~0.17–0.27 µm are now visible. XY vertical density log axis top ~1e17 cm^-3 clips multiple peaks, bottom plotted very low. Neither QW-specific hole concentrations nor QW4 causal mechanism can be inferred from the present cropped peaks.
- NEXT adjust **right XY vertical density** log-axis to Min1e10 Max1e20 cm^-3, leave horizontal depth X unchanged; collect screenshot and assess peaks, optionally eDensity same cut. Existing code and simulations unchanged.

## 2026-10-22 — JuSubin Project B SDevice physical-model declaration observed (READ ONLY)
- In original V2.1 `pp2_des.cmd` (Bspan=0 baseline), user confirmed `Piezoelectric_Polarization(strain activation=0.5)` and `Thermionic` blocks for InGaN/GaN, AlGaN/GaN and AlGaN/InGaN material interfaces. `pp2_des.par` contains AlGaN Bandgap block and `ThermionicEmission { Formula = 1 }` entries; content of Bandgap and full interface context not yet checked.
- NEXT: `sed -n '1,34p' pp2_des.cmd` and `sed -n '108,176p' pp2_des.par`, read-only. Presence of declarations is NOT proof lateral Bspan>0 interface validity/polarization physics or performance. Keep baseline intact.

## 2026-10-22 — 이택규 hDensity Cutline_Y correctly created, awaiting graph X zoom
- User SVisual T-2022.03 screenshot explicitly shows vertical C2 cutline through `n2_end_des` at lateral Y approximately 1.3um, with right `Cutline_Y Plot` and `hDensity(C2(n2_end_des))`. XY graph horizontal X axis = full device depth 0..4.288um, compresses active MQW around X~0.17–0.27um. The Axis Properties left panel shows Min=0 Max=4.288, Fixed both.
- NEXT no more cutline setup: set that graph's horizontal axis Min0.14 Max0.29um to inspect each QW hole-density peak. Screenshot does not yet establish QW4 carrier accumulation or carrier mechanism. No TCAD source/run modification.

## 2026-10-22 — 이택규 n2 hDensity second zoom screenshot; QW4 concentration unresolved
- User zoomed n2_end_des hDensity map, legend still ~1e-30–8.279e19 cm^-3 (log). Four MQW strata visible at X depth~0.17–0.27um; lateral Y shown~1.0–1.65um, not sidewall Y~2.0um. Color is not an absolute per-well density diagnostic with vast auto range. QW4 radiative dominance from earlier PLT remains separate observation; carrier localization cause unknown.
- NEXT reduce back-and-forth zooming: SVisual Cut Y at constant lateral Y~1.3um for hDensity vs depth X crossing MQW, then eDensity if required. Official training https://ghzphy.github.io/Sentaurus_Training/sv/sv_5.html. No TCAD code/simulation modification.

## 2026-10-22 — 이택규 n2 hole density overview image observed; zoom required
- User screenshot SVisual T-2022.03 `n2_end_des` scalar `hDensity` (log legend about 1e-30..8.2788e19 cm^-3) entire lateral Y=0..2um; MQW vertical lines highly compressed in large X depth view.
- Field is accessible but screenshot insufficient to establish QW-by-QW carrier concentration, QW4 mechanism or actual final saved bias. NEXT: axes X 0.14–0.29um, Y 0–2um, capture enlarged hDensity then match eDensity as needed; no edits/reruns.

## 2026-10-22 — JuSubin Project B active V2.1 Bspan/Edge code hooks verified (OBSERVED USER TERMINAL)
- User ran READ-ONLY `grep -nEi 'Bspan|Wedge|Wdmg|AlGaN|Aluminum|Edge_|Dmg_' sde_dvs.cmd pp1_dvs.cmd | head -n 140` in actual school server directory `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`; source and preprocessed SDE printouts matched semantic definitions.
- OBSERVED `sde_dvs.cmd`: Wdmg=0.005um (line38); Wedge=`@Wedge@` line39; Bspan=`@Bspan@` line45; `Xd=Xs-Wdmg`, `Xe=Xd-Wedge` lines54–55. Actual `pp1_dvs.cmd` has Wedge=0.1um and Bspan=0 (lines39,45).
- OBSERVED documented mapping: `Bspan=0` baseline no new lateral AlGaN edge; Bspan1 -> Edge of QW1–4, Bspan2 -> Edge of QW1–4 plus B1–B3, Bspan3 -> Edge of QW1–4 plus B0–B4; explicit `in-Bspan?` function and conditional `AlGaN` material selection lines80–89. `MF_AlB` material profile for selected AlGaN edge referenced at line112; value/composition and actual geometric/electrical interpretation are UNVERIFIED. `Edge_`/`Dmg_` region dynamic names lines128–129; Edge keeps host doping by source comment at line133.
- INTERPRETATION: This is a PREWIRED lateral **material substitution** in QW and optionally GaN barrier EDGE regions, **not proof of a deposited outside coating**, unchanged active/emissive area, polarization consistency or viable physical performance. Baseline unchanged, no Bspan>0 preprocessing or RUN tested. Potential material-replacement/polarization/offset impacts are open review items.
- NEXT FIRST: read-only `sed -n '65,145p' pp1_dvs.cmd` to obtain `base-mat`, `in-Bspan?`, actual "MF_AlB" definition/use and `make-layer` region geometry; if Al mole fraction outside displayed block then grep `MF_AlB|MoleFraction|Aluminum|xAl` in pp1_dvs.cmd. Verify sidewall and vertical extents before choosing a Project B test condition. Do not edit V2.1 or start Project B runs pending frozen baseline.

## 2026-10-22 — 이택규 Xs formula, Wshelf0, Wedge0.1 actual preprocessed SDE observed; physical MQW gate next
- User pasted pp1_dvs.cmd lines37 39 53–56: `Wshelf=0.0`, `Wedge=0.1`, `Xs=Wm/2`, `Xd=Xs-Wdmg`, `Xe=Xd-Wedge`, `Xend=Xs+Wshelf`. Earlier SDE lines154–158 set top anode all Clean+Edge+Dmg segments; n1_msh.log actual 2um Half width. 4um Wm numeric was not in this grep, but mesh width corroborates target 2um.
- With no explicit AreaFactor/Cylindrical in n2/n6 processed files and published 2D default 1um depth, provisional planar J 3.6V=1.82364 A/cm2 (n2 OFF),0.460985 A/cm2 (n6 ON) from existing PLT currents. NOT validated circular-device J or any IQE. This minimal setup audit is sufficient to proceed rather than repeat greps.
- NEXT SVisual n2_end_des hDensity across four QW to assess QW4 dominant radiative spatial distribution; optionally eDensity; then physical plausibility benchmark and independent Full/Half. No TCAD edits or reruns.

## 2026-10-22 — JuSubin assigned Project B after Baseline freeze; starts preflight now (USER DECISION, DESIGN ONLY)
- Explicit user plan: after verified Baseline acceptance, Lee handles Project A GaN:C, JuSubin handles Project B AlGaN. Replaces earlier JuSubin dual-A/B preparation priority. Lee direct acceptance and final Baseline-freeze event not independently observed.
- Today's JuSubin B work: inspect active V2.1 `Bspan` / Edge material and sidewall 5nm boundary in SDE, define actual proposed AlGaN insertion ROI, validate polarization, Ec/Ev, electron/hole access, develop initial pilot and width/composition sweep conditional on source evidence. Plan: `members/JuSubin/PROJECT_B_PLAN_20261022.md`. No Sentaurus edits/runs or terminal access by this AI.

## 2026-10-22 — 이택규 actual V2.1 SDE anode contact segmentation observed
- User pasted `pp1_dvs.cmd` lines150–168. Anode explicitly assigned to three top p+ cap edges via midpoints in intervals [0,Xe], [Xe,Xd], [Xd,Xs] (comment: whole mesa top Clean+Edge+Dmg). Cathode active for prior observed Cath=0 on bottom edge centered Xs/2; outer shelf bottom extra only if Wshelf>0 (prior live Wshelf0).
- Supports geometry/source contact coverage, but numerical Xs span and actual mesh edge-length should be checked before treating 2um×1um as calibrated electrode area. Published 2D AreaFactor default 1um and current scaling: https://ghzphy.github.io/Sentaurus_Training/sd/sd_3.html.
- NEXT: read geometry-defining Xs/Xe/Xd (brief pp1 grep), then finish priority Half physical audit/Full vs Half. No TCAD modification or new run.

## 2026-10-22 — 이택규 n2/n6 AreaFactor override check negative, conditional planar J derived
- User reported zero output from `grep -niE 'AreaFactor|Cylindrical|CoordinateSystem' pp2_des.cmd pp6_des.cmd pp2_des.par pp6_des.par`: no explicit 2D area/cylindrical overrides in scanned two preprocessed decks.
- Prior n2/n6 logs `Use length unit of micrometer during currentplot integration` only describe integration convention. Published Sentaurus training describes 1um default depth in 2D; conditionally for 2um Half strip area A=2e-8cm²: I_n2=3.64728525e-8 -> J=1.82364 A/cm², I_n6=9.21970771e-9 -> J=0.460985 A/cm² at 3.6V.
- Conditional planar equivalence only; true circular-LED current density / full device equivalence / active anode full-span contact unverified. Next quick read-only contact boundary review, physical plausibility gate, independent 4um Full/Half comparator. TCAD unchanged.

## 2026-10-22 — JuSubin Project A/B preparation started (PROPOSED DESIGN; NO TCAD RUN)
- 주수빈의 사용자 결정: 이택규 Baseline V2.1 final checks와 중복 없이 Project A localized GaN:C resistive edge 및 Project B localized AlGaN lateral heterobarrier 사전 물리·설계 검토 시작. Lee's agreement to formal exclusive role assignment unconfirmed.
- Written design/preflight plan: `members/JuSubin/PROJECT_AB_PREPARATION_20261022.md`. NEXT: read-only audit V2.1 `sde_dvs.cmd` / `pp1_dvs.cmd` Wedge/Bspan/Wdmg, Edge/Dmg materials; verify C model and AlGaN interfaces before SWB pilot. Baseline freeze, 2D AreaFactor and Full/Half gate still pending. No SDE/SDevice source, simulation or parameter change.

## 2026-10-22 — 이택규 AreaFactor/current-unit first read-only grep (OBSERVED)
- User ran `grep -niE 'AreaFactor|current unit|length unit|A/cm|A/um' pp2_des.cmd pp2_des.par n2_des.log n6_des.log`; only n2/n6 log line297: `Use length unit of micrometer during currentplot integration.`
- No explicit AreaFactor or terminal-current units in searched files, so current normalization and absolute J remain UNRESOLVED. IntegrationUnit is not terminal current unit. Next verify both n2/n6 preprocessed cmd/par for AreaFactor/Cylindrical/CoordinateSystem and effective 2D z-thickness/contact width, using T-2022.03 reference before physical J assertion. TCAD unchanged.

## 2026-10-22 — 이택규 n6 Radiative SVisual spatial screenshot observed
- User screenshot from SVisual T-2022.03: title `n6_end_des`, `RadiativeRecombination` legend top about 5.02e24 cm^-3 s^-1, x depth~0–0.45um and y lateral~1.2–2um. Multiple MQW horizontal radiative bands including pronounced ~0.26um band; qualitative only.
- n2 SVisual screenshot had previously been observed, but shared plot legend and exact matched spatial ROI are not yet confirmed; do not quantify n2/n6 map comparison from colors. TDR bias, per-region QW integrals from image, absolute IQE, AreaFactor and physical causality still not proved. NEXT: matched plot scales/ROI + existing PLT quantitative interpretation; then current-normalization and Full/Half validation. No TCAD changes.

## 2026-10-21 — 이택규 n2 SVisual spatial radiative band screenshot (OBSERVED USER IMAGE)
- Screenshot of n2_des scalar RadiativeRecombination at X depth~0–0.45um, Y lateral~1.2–2um shows pronounced radiative bands near 4QW positions incl. strong QW4 ~0.263–0.266um. Consistent with independently calculated PLT QW4 share ~99.9688%; cannot infer numerical percentages or full-domain profile from cropped color plot, nor verify final 3.6V from dataset label n2_des alone.
- Next n6_end_des.tdr same field/view qualitative comparison. Avoid over-focus one mesh element; current normalization and Full/Half planned later. No source/run changes.

## 2026-10-21 — V2.1 n2/n6 final TDR/SAV presence observed
- User-provided `find . -maxdepth 1 -name '*end*' -print` listed both n2/n6 `end_des.tdr`, `end_des.sav`, `end_circuit_des.sav`; prior `ls cannot access 2` was malformed input, not missing output. Both PLT last points previously at 3.600V.
- Existence confirmed, not content/Save-Load restart. Next SVisual QW4 radiative spatial profile review; current units/AreaFactor still unresolved and must not claim calibrated J. Full 4um reference after Half audit; original files untouched.

## 2026-10-21 — 이택규 OFF Trap baseline numerically negligible (OBSERVED PLT)
- n2 `IntegrTrap_all eGapStatesRecombination` at 3.6V=1.17883032026416e6 raw; n6=1.98258247754075e22 raw, ratio 1.68e16. Under conditional q×1e−12 scaling n2 trap terminal-current-equivalent fraction ~5.18e−18 vs n6 ~34.4528%. n6 Rad/SRH/Auger/Trap whole-device accounting closes to ~99.99904% terminal. Supports intentional OFF/ON trap split actual effects, NOT unique current-suppression causality or validated absolute IQE.
- Next current unit/AreaFactor and broad physical benchmark, then Full/Half after Half audit. No code/run changes.

## 2026-10-21 — 이택규 n6 3.6V Trap-integral explains QW current-balance residual (OBSERVED)
- User provided n6 .plt final row: IntegrTrap_all=1.98258247754075e22 raw; full-device IntegrRad_all=2.55552035945039e22, IntegrSRH_all=4.32337288643595e21, IntegrAug_all=7.83993596604716e21. With previously numerically supported 1e−12 PLT-to-SVisual conversion and q, 3channel equivalent=6.04317e−09 (65.546% I), gap-state trap equivalent=3.17645e−09 (34.453% I), sum=9.21961925e−09 ≈99.9990% of terminal I=9.21970771e−09. Earlier QW 3channel balance residual ~34.48% is accounted for by trap plus minuscule non-QW channels.
- Conditional current-unit basis still unverified in UG/AreaFactor. Not a proven causal trap-current suppression mechanism or calibrated IQE. Next check n2 trap integral/current units, finish Half, Full later. TCAD unchanged.

## 2026-10-21 — V2.1 n6 3.6V 전체 재결합/Trap 전류 수지 99.9990% 확인 (USER-OBSERVED PLT; UNIT CONSISTENCY INFERRED)
- 작업자 이택규가 학교 서버 n6_des.plt 마지막 행에서 직접 추출해 제공: bias=3.6V; IntegrTrap_all eGapStatesRecombination = 1.98258247754075e22, IntegrSRH_all srhRecombination = 4.32337288643595e21, IntegrRad_all RadiativeRecombination = 2.55552035945039e22, IntegrAug_all AugerRecombination = 7.83993596604716e21 (raw PLT integral data).
- 이전 같은 행 Ianode=9.21970771e-09, Icathode=-9.21970771e-09, displacement=0. Earlier n6 four-QW 3-channel sum raw Rad=2.55545394e22 SRH=4.31092452e21 Aug=7.83986116e21.
- DERIVED using q=1.602176634e-19 C and PLT raw recombination x 1e-12 numerical SVisual 2D conversion (unit conventions still need formal confirmation): Trap equivalent current=3.17644732e-09, =34.4528% of terminal current; total-device Rad=44.4092%, SRH=7.5130%, Auger=13.6240%. Four-channel all-device sum equivalent=9.21961925e-09, =**99.99904%** terminal current, residual 8.85e-14 =0.000959%. QW-only 3-channel =65.5233% terminal current, Trap=34.4528%, other-than-QW normal channels ~0.02292%; residual ~0.00096%.
- INTERPRETATION: numerical charge/recombination balance closes very tightly in n6 at final steady-state-like 3.6V and eGapStates recombination is substantial, consistent with active SideTrap in Dmg regions (EdgeTrap Conc0); not proven that this alone causes reduced terminal current, not matched-current IQE, not device physical calibration, not independent unit/AreaFactor confirmation. No need to pursue tiny mesh-angle without new evidence. `IntegrTrap_all` area attribution to sidewall can be checked with regionwise integrated values if needed.
- NEXT: read n2 all-device trap/channel totals for control/balance, check current units/AreaFactor and QW4-dominant spatial recombination physical plausibility as part of broader Half validation; then prepare professor-requested 4um Full vs 2um Half run on protected separate project. Existing TCAD code/runs untouched.

## 2026-10-21 — 이택규 n2/n6 final 3.6V PLT extraction OBSERVED
- Both runs n2/6 reached exactly 3.600V; anode/cathode totals balanced, displacement=0. n2 raw I3.64728525e−08, n6 I9.21970771e−09; ratio 25.28%.
- QW total (raw PLT) n2 Rad1.52410078e23 SRH1.25388758e22 Aug6.26565608e22, n6 Rad2.55545394e22 SRH4.31092452e21 Aug7.83986116e21. QW three-channel Radiative fractions 66.96 vs 67.77%, though n6 radiative rate only 16.77% of n2. PLT ×1e−12 reproduces prior SVisual integrated magnitudes; conversion/A·area factor still conditional. q×(QW 3channel)×1e−12/I n2~0.99982, n6~0.65523, leaving n6 34.48% residual for trap/device-wide channels/current pathways; do NOT attribute until measured.
- Python NameError 'PY' after complete output is harmless. Next inspect PLT IntegrTrap_all + global Rad/SRH/Aug; no code changes/new runs; Full after Half.

## 2026-10-21 — 이택규 n2 PLT numeric block wrapping verified (OBSERVED)
- `sed -n '45,58p' n2_des.plt` shows scientific-notation floats in `Data {` starting line52; closing data block is visible at file tail. Values line-wrap; must parse by number of dataset labels rather than interpreting a tail line as one point. Numeric QW/terminal values have not yet been mapped or validated.
- Next: one-pass read-only extraction of existing n2/n6 PLT currents and 12-region QW Rad/SRH/Auger integrals for final target 3.6V, checking row shape/units and preserving original TCAD runs; avoid repeated header inspection.

## 2026-10-21 — 이택규 n2 .plt current/recombination fields found (OBSERVED HEADER, VALUES NOT YET CHECKED)
- n2_des.plt DF-ISE header contains anode/cathode currents/voltages and Clean/Edge/Dmg region-wise IntegrRad, IntegrSRH, IntegrAug for all four QWs plus EBL and eGapStatesRecombination. pp2_des.cmd main Physics includes Fermi, radiative/SRH/Auger, Mg/PDopant incomplete ionization, strain polarization0.5, 3 heterointerface Thermionic blocks. n6 runtime repeats Thermionic enabled Formula1. pp2/pp6 .par files remain equal.
- Next inspect .plt functions/units/values then programmatically recover matched final-bias current and summed QW channels n2 vs n6; actual IQE, unit normalization, physical calibration are not proven. Keep Half project intact, Full comparator later.

## 2026-10-21 — 이택규 V2.1 ON/OFF 물성 파일 동등성 확인 (OBSERVED)
- User-shared terminal `diff -u pp2_des.par pp6_des.par | head -n 80` returned no differences. Combined full .cmd diff: same mesh/electrode/global physics/solver/3.6V sweeps, only SideTrap Conc0 versus 1e18 across 13 Dmg regions, with node-specific file naming. Input split consistency gate passed, but calibration, 2D current normalization, TDR bias, and matched-current IQE remain unresolved.
- NEXT: inspect current .plt dataset metadata and current normalization; evaluate existing results first, then remaining QW checks. Original runs untouched; professor Full/Half comparison after Half verification.

## 2026-10-21 — 이택규 V2.1 n2/n6 command diff 검증 (OBSERVED)
- Full 76-line unified .cmd diff: both identical mesh, electrode, global physics/solver/voltage ramp; 13 Dmg SideTrap OFF0/ON1e18 and node-specific file references/prefixes differ. .par contents NOT yet compared.
- n2/n6 both show runtime Thermionic electron/hole Formula1; AreaFactor/2D current normalization unresolved. Next compare pp2/pp6 .par and electrical data, keeping Half unchanged before Full.

## 2026-10-21 — 이택규 V2.1 n2 Thermionic runtime 확인 (OBSERVED)
- n2_des.log 실제 `With Thermionic Emission at heterointerfaces for electrons and holes` (662/671/680), `ThermionicEmission: Formula = 1, instead of: 0 [1]` (1784/1790/1796) 확인. `pp2_des.cmd` vs `pp6_des.cmd` unified diff 전체 76줄, 내용 아직 미제공이므로 실제 차이/동등성 미확인. `AreaFactor`는 출력 검색 매치 없음, current density normalization unresolved.
- Next actual diff output and n6 runtime thermionic check, then AreaFactor current normalization. No mesh anomaly tunnel-vision; unchanged TCAD source/results.

## 2026-10-21 — 이택규 V2.1 n2/n6 SDevice preprocessed physics confirmed at keyword level (OBSERVED)
- User-provided grep of pp2_des.cmd/pp6_des.cmd: both `Recombination(SRH Radiative Auger)`, incompletely ionized Mg/PDopant, `Piezoelectric_Polarization(strain activation=0.5)`. n2 all 13 Dmg SideTrap conc 0, n6 13 Dmg SideTrap conc 1e18; both EdgeTrap conc0 across 13 Edge regions. SideTrap EnergyMid0.75 fromValBand, EdgeTrap0.9 fromValBand, cross sections e/h 1e-15 in shown lines.
- Only matched grep statements reviewed; full pp2/pp6 diff not yet run. No AreaFactor or ThermionicEmission keyword visible from this command; check effective model/defaults and terminal current normalization before physical conclusion.
- NEXT: full preprocessed deck diff; selected physics/math/log model validation then J-V/recombination gate. Maintain user's instruction to avoid tunnel vision on tiny mesh sliver. Do not run Full until Half verification. No code or server-run modifications.

## 2026-10-21 — 이택규 메시 생성 로그 경고 검색/균형 잡힌 검증 우선 (OBSERVED; NO CONFIRMED ERROR)
- `n1_msh.log` 경고/품질 grep 출력은 4개 통계 항목만 반환: minAngle 0.0167024deg, minEdge 1.95312e-05um, smallest region Dmg_QW3 1.5e-05um²; 별도 warning/error 텍스트는 없음. 이상치의 실제 물리 수치 영향 미확인.
- 이택규는 한 이슈에 과도한 집착을 피하고 구조, Mesh, physics, I-V, current normalization을 폭넓게 확인하길 요청. Mesh 최솟값은 기록된 주의사항으로 보관, 관련 수치오류 근거 전까지 추가 원인 추적 보류.
- 다음: pp2/pp6 실제 유효 물리 설정·AreaFactor·전류 정상성 간결 점검. Half 검증을 먼저 마친 뒤 Full 비교 run. 코드/서버 run 변경 없음.

## 2026-10-21 — 이택규 V2.1 half generated mesh quality flag; Full after verification (OBSERVED)
- SDE physical region/contacts: full mesa nominal 4um, implemented half lateral 2um, depth4.288um; QWs 4×3nm; sidewall damaged width5nm; top pCap anode, bottom nGaN cathode. `n1_msh.log` reports successful mesh saved, 62529 points/123917 elements, 4.288×2um bbox, 8.576um² total domain.
- Potential quality blocker (not confirmed solver error): minAngle 0.0167024deg and min edgeLength1.95312e-05um=0.0195312nm at (depth0.0041875,lateral1.89501)um, near computed Clean/Edge boundary Xe=1.895um. Examine SVisual local mesh/quality and warnings; source alone cannot prove mesh convergence. `42 regions`/nMats40 discrepancy observed but metadata semantics not resolved.
- 이택규 instructed: finish Half check before launching Full comparator. Existing V2.1 runs untouched. Next inspect near reported sliver and mesh log warnings.

## 2026-10-21 — 이택규 Full/Half 검증 게이트 추가 + PP1 실제 값 확인 (USER-REPORTED PROFESSOR FEEDBACK, OBSERVED)
- 교수가 절반 모델 활용 시 전체 4um Full과 2um Half 성능 재현성 비교를 요구했다고 이택규가 보고. 이는 실행/검증 완료가 아닌 **새 우선순위 게이트**. 기존 V2_Copy는 shelf 포함 half 소자이며 Full 아님.
- 실제 서버 `pp1_dvs.cmd`: `Wshelf=0`, `Wedge=0.1` um, `Bspan=0`, `Cath=0`; `n1_msh.tdr` 약 2.0MB Oct14 13:43 존재. Element stats/quality, symmetry, Full 결과 미확인.
- NEXT: read-only actual geometry & contacts `sde_dvs.cmd` 55–170 lines, `n1_msh.log`; then preserve Half and prepare independent mirrored Full project; preprocess/mesh/contact gate and compare off/on J-V, QW 3-channel ratio, profile with current normalization. No TCAD code/run changes.

## 2026-10-21 — 이택규 V2.1 활성 SDE mesh-size 설정 확인 (OBSERVED SOURCE, MESH VERIFICATION PENDING)
- 실제 서버 `CMP_BASELINE_2.0.0_V2/sde_dvs.cmd` 제공: x=depth/y=lateral; 4um full mesa, 2um half, damage width 5nm, `Wshelf=0`, `Cath=0`. Depth mesh maxima QW=0.3nm, EBL/MQW=1.5nm, interface=0.2nm; lateral damaged sidewall max 0.5nm, bulk default 250nm. `R_sh` shelf corner window remains active in source. Configuration only, actual elements/quality/convergence and preprocessed `Wedge/Bspan` not established.
- Next (read-only): mesh build log, preprocessed SWB variables, SVisual actual n1_msh.tdr geometry/contacts. Existing V2.1 n2/n6 3.6V results unchanged, n6 recombination integral still pending.

## 2026-10-15 — 주수빈 n6 분석 중 n2/8 QW 적분 출력 확인 (OBSERVED; n6 PENDING)
- 추가 SVisual Radiative 출력은 n6가 아닌 `n2_des`이며 Clean+Dmg 8개 QW ROI, Total 1.447895e11, Domain=0.02279999um². 과거 n2 12 ROI 1.524099e11과 차≈Edge_QW1..4 합. GUI Dataset과 Region selection을 수정한 뒤 n6 12ROI 측정 필요. n6 재결합 데이터는 아직 미확보.

## 2026-10-15 — 주수빈 V2.1 n2 MQW 재결합 3채널 적분 (OBSERVED)
- 동일 12 QW, 면적 0.02399999 um²: Radiative 1.524099e11, SRH 1.253894e10, Auger 6.265625e10 s^-1 um^-1. Radiative fraction 66.9624%, Auger 27.5285%, SRH 5.5091% (3채널 모델 내부 비율). QW4 방사 99.969%, SRH 98.644%, Auger 99.993% 집중. n6 동일 ROI 적분 대기. IQE 검증, AreaFactor, 공간 TDR bias, 물리 원인 미해결.

## 2026-10-15 — 주수빈 V2.1 n2 QW SRH integration 관찰 (OBSERVED)
- n2_des 12 QW ROI srhRecombination integral 1.253894e10 s^-1 um^-1, Domain 0.02399999 um². QW4가 약 98.6438% 담당. 이전 Rad=1.524099e11, 두 채널 rad share 92.40% (Auger 미포함, validated IQE 아님). 다음 n2 Auger 동일 ROI 후 n6 반복. TDR bias/AreaFactor 검증 잔여.

## 2026-10-15 — 주수빈 V2.1 n2 QW Rad integral OBSERVED
- 출처(OBSERVED): 주수빈이 2026-10-15 실제 Sentaurus Visual `Dataset: n2_des`, `Field: RadiativeRecombination`, `Regions of Dimension 2`의 Field Integration 출력 전체를 채팅에 제공. `Clean_QW1..4`, `Dmg_QW1..4`, `Edge_QW1..4` 총 12개 물리 영역이 확인됨. `Total Integral = 1.524099e+11 [s^-1*um^-1]`, `Total Domain = 2.399999e-02 [um^2]`; 12개 개별 값의 합 = 1.52409866249133e11 (출력 반올림과 일치).
- QW별 세 영역 합계(표시 정밀도): QW1=1.884852e6, QW2=2.718766e6, QW3=4.298663e7, QW4=1.52362276e11 [s^-1*um^-1]. QW4 비중 ≈99.9688%. 공간적 방사 재결합 분포일 뿐 IQE가 아님. QW4 우세의 수송/전자·정공 주입 물리 원인은 미확인.
- 각 Clean 합계≈1.44408491777e11, Edge≈7.62036249754e9, Dmg≈3.81011974593e8; 과거 `Dmg_QW14` 사용자 간략 표기와 달리 실제 적분에서 `Dmg_QW1..4` 개별 이름 확인. n6, SRH/Auger 및 3.6V에 대응하는 TDR 최종 저장점·물리 모델/AreaFactor 미검증.
- 다음: 동일한 12개 ROI로 **n2 SRH** 적분 (`Total Domain` 동일 확인), 이후 Auger 적분하고 n6 반복. `Radiative/(Radiative+SRH+Auger)`는 정의 한정의 QW 내 비율이며 전류/누설/Trap 생성·재결합 수지 별도 검증 전 물리적으로 확정된 IQE 또는 matched-current 성능 차이가 아님. 코드/시뮬레이션 변경 없음.

## 2026-10-15 — 주수빈 V2.1 n2 RadiativeRecombination field 시각화 확인 (OBSERVED)
- SVisual n2_des screenshot: RadiativeRecombination active, displayed maximum 3.07538e25 cm^-3 s^-1 (local field, NOT ROI integral); Edge_QW3/4 region labels visible. n2 QW 적분과 12 ROI 실제 선택 미수행. 다음: Field Integration Region/Material 탭에서 QW regions만 선택해 Total Integral 확보.

## 2026-10-15 — 주수빈 V2.1 QW ROI 생성 규칙 확인 (OBSERVED SDE EXCERPT)
- 실제 서버 `sde_dvs.cmd` grep은 각 QW1..4 thickness 0.003µm, `Wdmg=0.005` µm, `Wedge=@Wedge@`, `rE=(string-append "Edge_" name)`, `rD=(string-append "Dmg_" name)`을 보여줌. 기존 Clean_QW1..4 SVisual 확인과 합쳐 4 wells × 3 segments = 12 region ROI 구성이 예상됨. 실제 SVisual 12개 전체 선택 및 수치 적분은 아직 미수행.
- Edge/clean baseline 동질성 및 Dmg NtSide 적용은 SDE 주석 근거이며 활성 effective SDevice deck 검증 필요. 다음: GUI region+field 존재 확인 후 동일 QW ROI 방사/SRH/Auger 적분.

## 2026-10-15 — 주수빈 V2.1 region names differ from old 5V_TEST (USER-REPORTED; ROI NOT YET VERIFIED)
- SVisual `n2_des`에 기존 `DmgL_QW1~4` 대신 사용자 표기 `Dmg_QW14`, `Edge_QW1~4` 존재 보고. `Clean_QW1~4`는 이전 스크린샷으로 관찰. Dmg_QW14가 정확한 단일 region label인지, Clean/Edge/Dmg의 물리적 범위 및 QW 중복 여부 미확인.
- 다음: 활성 SDE 소스 read-only grep 후 동일 QW ROI 재결합 적분. 미확인 region을 합산하지 않음. 코드 수정/시뮬레이션 실행 없음.

## 2026-10-15 — 주수빈 n2 SVisual QW 표시 확인 (OBSERVED SCREENSHOT)
- `CMP_BASELINE_2.0.0_V2/n2_des` SVisual: Clean_QW1..4/EBL 지역과 AugerRecombination scalar 존재, DopingConcentration 현재 선택, Elements 129404 / Points 62529. DmgL_QW 및 Radiative/SRH는 현재 화면 스크롤 범위 밖으로 미확인. 공간 TDR의 최종 bias 및 실제 재결합 적분은 미검증.
- 다음: ROI/필드명 확인 → Rad/SRH/Auger 동일 영역 적분. 기존 소스/실행 변경 없음.

## 2026-10-15 — 주수빈 V2.1 실행 완료 직접 확인 (OBSERVED)
- 학교 서버 `CMP_BASELINE_2.0.0_V2`: n2/n6 status `done`, 각 최종 anode 3.600 V, raw total current n2=3.647e-08, n6=9.220e-09. n2 TDR 21M/PLT 293K, n6 TDR 23M/PLT 295K 실제 파일 존재(10/14 수정). 주수빈이 10/15 제공한 원본 터미널 텍스트 기준. **전압 목표/파일 존재 확인이며 물리 타당성, TDR 최종바이어스, AreaFactor는 미검증.**
- 다음: 읽기 전용으로 최종 TDR 저장 시점·SVisual QW 4개 영역/재결합 필드 확인 후 Radiative/SRH/Auger 적분. 소자 변경 없음.

## 2026-10-15 — 주수빈 V2.1 물리 검증 담당 전환 (PROPOSED / AWAITING SERVER READ-ONLY OUTPUT)
- 주수빈은 V2_Copy 수렴 실패 진단을 우선 수행하려던 계획을 변경하고, 이택규/Claude 보고의 `CMP_BASELINE_2.0.0_V2` 내부 V2.1 결과에 대해 **전류 I–V / MQW Rad·SRH·Auger / QW IQE 검증**을 시작하기로 함. 이전 V2_Copy 선택은 historical, 최신 할 일은 V2.1.
- 첫 단계는 n2/n6 파일 TDR/PLT/STA 존재 및 마지막 anode voltage/current를 서버 터미널에서 read-only 확인. 명령 안내는 완료되었지만 실제 출력·새 수치/실험은 아직 없음. 다음: 최종 bias 공간 TDR 검증 후 SVisual 4QW ROI 동일 적분.
- 이택규의 구조/solver 담당은 GPT 추천안이며 이택규의 실시간 진행 또는 두 연구원 간 확정 역할분담이 아님. 물리 baseline 정식 freeze는 여전히 미완료.

## 2026-10-15 — Baseline V2.1 shelf 제거 후 n2/n6 3.6V 도달 (USER-REPORTED RUN / GPT HAS NOT SEEN RAW SERVER LOG)
- **실행 보고:** 이택규가 Claude의 #02(2026-10-15)를 전달. `CMP_BASELINE_2.0.0_V2`를 shelf 없는 V2.1(`Wshelf=0`, shelf와 해당 하단 cathode 삭제, PolAct=0.5, 기본 solver Iterations20/NotDamped50)로 SDE부터 다시 실행. n2(NtSide0)와 n6(NtSide1e18) 모두 3.600V 도달, raw terminal I 3.647e-08/9.220e-09 A/µm; half 2µm 가정 J 1.8235/0.4610 A/cm², didn't converge 0/1회. **사용자가 인용한 서버 grep 수치이며 실제 로그 파일을 GPT가 직접 열어 검증하지는 않음.**
- **대조:** shelf 포함 V2+PolAct0 `CMP_BASELINE_2.0.0_V2_Copy` n2/n6 2.069/2.036V 정체 및 17/23 비수렴 출력. 분극 제거만으로 해결되지 않음. 정확한 수렴 원인은 shelf 자유표면/270도 모서리일 수 있지만 cathode 경계조건도 달라져 **원인 분리는 아직 미완료**.
- **의사결정:** 이택규/Claude가 **V2.1을 다음 단계 working Baseline geometry로 채택**했다고 보고; 물리적 Common Baseline final freeze 아님. 이 보고와 2026-10-13 구 V2 run3 기록은 *서로 다른 run*으로 취급.
- **blockers:** 명시적 SDevice log/.plt/pp·AreaFactor·contact 검증; QW/EBL/sidewall SRH/Rad/Auger 및 qR/I 의미/누설, IQE 후처리; NtSide1e18 전류가 NtSide0 25.3%로 감소하는 원인; 문헌 turn-on I–V와 mesh/full-half/cathode 변경 물리 영향. 순수 수치 국소 ideality n≈2.27 (3.576→3.600V)이 수송원인을 입증하지 않음.
- **next:** `bl2_check.py` 실 데이터/정의 검사 → J–V·지역별 적분/누설/전하 점유 검증 → 문헌 IV → S3(PolAct1) → Project A/B pilot (조건부), 4–5V Save/Load는 별도 검증한 복사본에서만. [상세 #02](../members/LeeTaekGyu/LOG_20261015_02_baseline_v2_1_shelf_removal.md).

## 2026-10-13 — 이택규 V2 independent analysis (ANALYSIS, not experimental result)
- User reports Claude already diagnosed and launched run3 in a copy with Blocked/ParDiSo, 4 threads, Iterations20, NotDamped50, ExtendedPrecision. Original pp/log not inspected; outcome unverified. QS stage 2.0-3.6 V MaxStep 0.01 means at most 0.016 V (normalized). Existing n2_des_min_des.tdr supports looking for automatic Newton/min-step diagnostics, but actual trigger unconfirmed.
- Priority: locate failing Newton equation/mesh vertex; check low-density HFS, polarization EBL barrier and Mg activation; avoid calling NotDamped50 an error. PARDISO+extended precision supported but potential threading slowdown. Small-bias n=1.6 extrapolation cannot validate 3.6V / QW injection. For A/B, prevent conflating C process with ideal traps and conformal AlGaN with QW-edge substitution. No solver/physics validation confirmed; protect existing runs.

## 2026-10-13 — Claude V2 n2 조기 종료 사용자 확인 (UNRESOLVED)
- n2 SDevice finished에도 3.6V Goal 미달, 사용자 조기 종료 확인; 마지막 보고 anode 2.070V/raw 1.781e-16. 원인 미확인. 다음 read-only n2 Solve block 및 종료 경고 검사. n6 실행 방해/수정 금지.

## 2026-10-13 — 이택규 Claude V2 SDE done / SDevice n2 정상 종료, n6 실행 중 (OBSERVED SERVER LOG)
- 근거: 사용자 제공 `CMP_BASELINE_2.0.0_V2` 실제 서버 `cat n1_dvs.sta n2_des.sta n6_des.sta`, `tail -n 35 n2_des.log`, `tail -n 20 n6_des.log`.
- Node1 SWB status `done`; `n1_msh.tdr` 파일 존재. 기하/접촉/메쉬 품질은 별도 검증 필요.
- **Node2 SWB `done` 및 `Sentaurus Device simulation finished (Tue Oct 13 18:51:50 2026 KST)`, `Good Bye !` 확인**. `n2_end_des.tdr`, `n2_end_des.sav`, `n2_des.tdr` 저장. wallclock 13107.96 s (3h38m27s), peak memory 2.41GB. **종료 확인 ≠ 물리적 Baseline 타당성 확인**; 최종 전압/전류 및 효과적인 physics는 아직 읽지 못함.
- Node6 SWB status `running`; 마지막 제공 로그에는 직전 완료 단계 anode V=2.018E+00, conduction current=9.514E-17 (solver raw unit), cathode opposite sign. 새 단계 t=0.0113234→0.0119577가 Newton iteration 4 시점까지만 보이며 아직 accepted/failed 여부 미확인. 로그가 이후에도 최신 진행 중인지는 미확인. `n6_des.tdr` 최종 파일은 아직 없던 목록.
- `grep -iE 'fatal|error|failed|simulation finished|good bye'`는 일반 Iteration 헤더와 `Error smaller than 1`까지 포함하여 끝부분 출력만으로 n6 fatal/종료 여부 판정 금지.
- 사용자 시간 제약 때문에 다음 최소 read-only 점검: `grep -E '^[[:space:]]*anode[[:space:]]' n2_des.log | tail -n 8`; `grep -nE 'Goal|Voltage|Vmax' pp2_des.cmd | tail -n 20`; `ps -p 93107 -o pid,stat,etime,pcpu,args`; `stat -c '%y %s bytes' n6_des.log`. n2 최종 bias/current 수치 확보 후 전류 정규화 및 physics validation. 원본 코드·SWB 런 변경 없음.

## 2026-10-13 — 이택규 Claude V2 서버 실행 산출물 최초 확인 (OBSERVED FILE INVENTORY / UNRESOLVED RUN STATUS)
- 사용자 제공 실제 학교 서버 Bash `ls -lh` 및 `find` 출력. 실 프로젝트 경로는 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2` (**`tmp/myproject` 아래가 아님**); 이전 경로 안내를 정정.
- SDE node1: `n1_bnd.tdr` 109,952 bytes, `n1_msh.tdr` 2,060,977 bytes, `n1_dvs.log` 8,046 bytes 및 `n1_msh.log` 2,992 bytes. 파일 생성 자체 확인, 메쉬 품질/접촉 검증 미완료.
- SDevice node2: `n2_des.log` 324,401 bytes, `n2_des.plt` 134,765 bytes, `n2_des.tdr` 20,661,842 bytes, `n2_end_des.tdr` 및 `n2_end_des.sav` 존재; `n2_eq_des.tdr` 존재. 이는 실제 실행 산출물의 존재를 확인하는 것이지 완료 성공/최종 전압/전류 검증은 아님.
- SDevice node6: `n6_des.log` 257,035 bytes, `n6_des.plt` 65,627 bytes, `n6_eq_des.tdr` 및 `n6_V1_des.sav` 존재; 보여준 목록에는 `n6_des.tdr` 없음. 실제 진행/실패/완료 미확인.
- 기존 정적 감사의 'NOT RUN'은 ZIP 배포 당시의 기록으로만 유지. 현 서버에는 2026-10-13 실제 출력 파일이 존재하므로 현재도 미실행이라고 말해서는 안 됨. 현재 상태는 **runtime artifacts observed; physics/electrical validation unresolved**.
- 사용자는 시간 제약으로 빠른 read-only 검증 요청. 다음 실행: 현재 V2 폴더에서 `cat n1_dvs.sta n2_des.sta n6_des.sta`, `tail -n 35 n2_des.log`, `tail -n 20 n6_des.log`, `grep -iE 'fatal|error|failed|simulation finished|good bye' n2_des.log n6_des.log | tail -n 25` 출력 확인. 성공이 입증되면 목표 전압, raw terminal current, contact balance, physics runtime 적용을 점검. 모델/원본 결과 무단 수정·재실행 금지.

## 2026-10-13 — CORRECTION: Claude V2 SRH activation + full audit (OBSERVED source / pending T-2022.03 run)
- **IMPORTANT ERRATUM**: previous V2 audit asserted doping-dependent Scharfetter τ(EBL)≈0.05ns. That conclusion was WRONG for current deck; `Recombination(SRH Radiative Auger)` omits `DopingDependence`. Older Sentaurus UG states τ=taumax (100ns from .par) in this mode; T-2022.03 run verification pending. Same proposed V2 ZIP, no simulator run. Literature confirmed Lu/Yin 50%/70:30 assumption and Baek 50%/50:50. Remaining postprocessing and model/calibration blockers as detailed in Lee TIMELINE. Next S0 after logging scheme/parameter and currentplot source checks; do not alter SRH due false-positive.

## 2026-10-13 — 이택규 Claude Baseline V2 ZIP static audit (OBSERVED code / PROPOSED run / UNRESOLVED physics)
- Independent audit of Claude ZIP (PROPOSED, README says NOT RUN; school server status unknown) found Scharfetter `taumin=0`, `taumax=1e-7`, `Nref=1e16`, γ=1 causing strong doping dependence, contrary to declared uniform τ=100ns; example nominal EBL τ≈0.05ns. Other open gates: 50% polarization is experimental assumption not CMP-calibrated; currentplot qR/I accounting is incomplete unless leakage/charge continuity and trap semantics verified. File integrity hash checks passed. **Do not promote V2** or claim corrected current. Existing CAL 1.2.0 and POL50 jobs unchanged. Next: resolve τ intent then minimal S0 parse/equilibrium smoke with preserved baseline controls.

## 2026-10-13 — 이택규 CAL 1.2.0 별도 4.207V 로그 검증 (OBSERVED / UNRESOLVED)
- 사용자 제공 실제 학교 서버 read-only 출력 `tail -n 20 ../CMP_BASELINE_1.2.0_CAL/n2_des.log`. CAL 1.2.0 마지막 표시된 완료 단계 anode Voltage `4.207E+00 V`, anode electron current `2.330E-17`, hole current `6.423E-14`, total current `6.429E-14` (raw solver output; 단위 정규화 미확정). 다음 계산 시도 `Computing BE-step from 0.841422 s to 0.841424 s (Stepsize 1.6305e-06 s)`; 뉴턴 반복 2 `|Rhs| = 1.39e-03`으로 threshold 1e-03 미달, 해당 단계의 성공/실패 아직 미확인. 직전 완료 단계 wallclock 8.03 s.
- 앞서 `/proc` cwd 실제 출력: PID 88354 -> `CMP_BASELINE_1.2.0_CAL`; PID 94012 -> `CMP_BASELINE_1.4.0_POL50`. POL50 이전 시도 시작 시각 0.572527s, ≈2.863V, stepsize 6.7501e-06 s, 반복 RHS 1.17e-03. 두 프로젝트 모두 매우 작은 adaptive step에서 느리게 진행함. 로그의 마지막 iteration 종료 여부만으로 job 실패/성공 판단 불가; 실제 CAL/POL50 log mtime 및 accepted step 후속 확인 필요.
- CAL 1.2.0 최근 완료 4.207V와 POL50 2.863V의 raw current를 공정한 민감도 비교로 취급하지 않음. 원래 CAL 1.2.0이 목표 5V인지, 현재 데이터를 보존하고 중단 가능한지 재확인 필요. 이미 독립 CAL4V 4V 결과는 GitHub에 user-reported 존재, 따라서 우선 목표는 POL50 동일 조건 4V 비교이지만 CPU 경합과 CAL 중단의 적절성은 UNRESOLVED.
- NEXT READ ONLY: `ps -p 88354,94012 -o pid,etime,time,pcpu,pmem,nlwp,stat,args` 와 `nproc` 출력으로 활성 프로세스의 자원 상태 파악; 필요시 `stat`와 `tail`로 각 로그의 실시간 시간 증가 검토. 원본 job의 무단 kill/restart 금지. 코드 수정 없음.

## 2026-10-13 — 이택규 POL50 PID 출처 확인 (OBSERVED)
- 사용자 제공 서버 `/proc` cwd 출력으로 PID 88354는 `CMP_BASELINE_1.2.0_CAL`, PID 94012는 `CMP_BASELINE_1.4.0_POL50`임을 확인. 두 SDevice 동시 실행은 사실이지만 CPU 경합이 지연 원인인지 미확인. 다음 단계: 각 로그 진행 상태 및 자원 사용량 읽기 전용 점검. 계산 중단 또는 코드 변경 없음.

## 2026-10-13 — 이택규 POL50 slow-step Newton pattern and two SDevice PIDs (OBSERVED / UNRESOLVED)
- Evidence: user-pasted live server `tail -n 40 n2_des.log`, `ps -fu semi437 | grep '[s]device'`, `stat -c '%y %s bytes' n2_des.log`, `tail -n 15 n2_des.log` in `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.4.0_POL50`. n2_des.log reported modified 2026-10-13 11:54:26.576373260 +0900; size 3,371,197 bytes.
- Earlier completed BE-step at t=0.572417s with RHS 4.97e-04 <1e-03 and anode V ~2.862V, raw total I=7.796e-14. Later snippet shows new attempt `Computing BE-step from 0.572527 s to 0.572534 s (Stepsize: 6.7501e-06 s)` at 5V/s. Thus log advanced from t=0.572417 to a new attempt starting t=0.572527 (difference 1.10e-4 s = 0.00055V). Latest attempt is NOT shown converged. RHS iterations 2–6 repeatedly 1.17e-03 > criterion 1e-03, with alternate reported error around 6.34e2/4.16e3: observed iteration plateau; future acceptance/cutback/termination unknown.
- Two observed `sdevice --max_threads 4 pp2_des.cmd` processes owned by semi437: PID 88354 (start Oct10, displayed CPU 99), PID 94012 (start Oct12, displayed CPU 99). The matching command alone does not establish which is POL50; need read-only `ls -l /proc/88354/cwd /proc/94012/cwd` to map cwd, and fresh n2_des.log tail/stat to confirm current liveness/progress. No proof of actual final POL50 completion. Existing CAL4V/5V_TEST results preserved.
- DERIVED: time 0.572527s ×5V/s ≈2.862635V; target 4V corresponds t=0.8s. If 6.7501e-6s step never grows, approximately (0.8−0.572527)/6.7501e-6 ≈33,699 more steps would be needed, but solver adaptive stepping makes elapsed-runtime extrapolation invalid. Do not claim estimated completion time, root cause or failure from this partial log. No TCAD code or run modifications.
- Next: map PID to project and check fresh accepted t/stepsize trend; then decide whether continuing the long run is justified. Avoid killing/restarting or changing physics before verifying.

## 2026-10-13 — 이택규 POL50 n2_des.log 직접 확인: 약 2.862 V, 작은 시간 간격 (OBSERVED / UNRESOLVED)
- 사용자 제공 학교 서버 터미널 `tail -n 40 n2_des.log` 출력. 경로: `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.4.0_POL50`.
- 마지막으로 단자 값이 출력된 수렴 단계: `Computing BE-step from 0.572412 s to 0.572417 s (Stepsize: 4.5285e-06 s)`; Newton iteration 2에서 `|RHS|=4.97e-04 < 1.0e-03`로 `Finished`. Anode Voltage 출력 `2.862E+00 V`, eCurrent `3.023E-17`, hCurrent `7.793E-14`, TotalCurrent `7.796E-14` (로그 원래의 전류 단위/AreaFactor는 아직 별도 확인 필요). Cathode TotalCurrent `-7.796E-14`. 직전 단계 시간 6.82 s wallclock.
- 다음 계산 **시작만 확인**: `Computing BE-step from 0.572417 s to 0.572422 s (Stepsize: 5.4342e-06 s)`; iteration table header에서 출력이 끝남. 이 다음 단계 수렴 여부, 현재 실제 프로세스 동작 및 최근 파일 갱신 여부 미확인.
- DERIVED: 5 V/s 램프 기준 0.572417 s → 약 2.862085 V, 4 V 목표의 약 71.55%; 다음 nominal time step의 bias 증가량 = 5×5.4342e-06 = 2.7171e-05 V (27.171 µV). 최근 매우 작은 stepsize 때문에 진행이 느릴 가능성 있으나 축소 원인과 미래 완료 시간은 예측/확정하지 않음.
- 현재 발췌에 MinStep/fatal/simulation complete 출력 없음; **정상 완주나 현재 살아 있는 프로세스의 증거는 아님**. 즉시 종료/재시작·코드/물성 변경하지 말고 `ps -fu semi437 | grep '[s]device'`와 로그 수정 시각 및 새 BE accepted t를 확인하여 진행/정체/실패 분류. CAL4V 4V 값과 POL50 2.862V 값은 동등 조건이 아니므로 성능 개선 결론 금지.

## 2026-10-13 — 이택규 POL50 약 15시간 경과 미완료 보고 (USER-REPORTED / UNRESOLVED)
- 사용자는 `CMP_BASELINE_1.4.0_POL50` 4V transient 계산이 시작된 지 약 15시간이 되었으나 아직 완료되지 않았다고 보고함. 경과 시간은 추정, 학교 서버 실제 `n2_des.log`/SWB 상태/프로세스는 ChatGPT가 직접 확인하지 못함. 오류·정체·진행 중 여부와 현재 accepted t/V/Stepsize는 불명.
- 우선 READ-ONLY `cd /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.4.0_POL50; tail -n 40 n2_des.log; ps -fu semi437 | grep '[s]device'`로 현재 계산 진행/반복 실패/프로세스 확인. 필요한 경우 반복 log snapshots로 accepted time과 Stepsize 비교.
- 오류 미확인 상태에서 잡 강제 종료/재실행, 물성·메쉬·분극 추가 변경 금지. 기존 CAL4V 원본/5V_TEST 보존. POL50 최종 4V 결과·민감도 개선은 계속 UNVERIFIED. 사용자 로그 확인 후 계속/중단/수정 여부 결정.

## 2026-10-12 — Lee CAL4V cutline audit and POL50 running report (USER-REPORTED / DERIVED / RUN NOT DIRECTLY VERIFIED)
- User provided Claude notes labeled 19:40 and 20:28 KST. Raw school-server cutline CSV / SWB job log not directly accessible to this ChatGPT. Claude reports completed CAL4V central y=2.0um x cutline: QW1 eQF=-1.4025eV, hQF=-3.017eV; anode hQF=-4, cathode eQF=0. Thus arithmetic exact 4.000=1.4025 electron difference +0.9830 hole difference +1.6145 QW splitting. Their alternative 1.397+0.983+1.615=3.995 is rounded/mismatched sampling, not proof of extra loss. QF drops localize especially B0 and QB interfaces, but heterojunction discontinuity alone does not identify tunneling absence.
- EBL Potential reported 2.3215 to 3.3274 over 0.026um: 1.0059V, mean field ~0.3869MV/cm. EBL Ev -3.995 to -5.041 means 1.046eV change, ~96.2% numerical slope consistent with electrostatic contribution within reported homogeneous EBL. Source of equilibrium polarization vs imposed bias UNRESOLVED.
- At QW1/B1 E fields QW +2.61 MV/cm, B1 -0.15 MV/cm, nominal epsilonr=9.5 each: epsilon0*epsilonr*deltaE/e = ~1.45e13 cm^-2. Caution: correct normal D boundary requires eps each side and can include mobile/free sheet charges; not direct proof of exact polarization sheet nor '100% of physical polarization'. External historical technical paper 'Material Properties of GaN in the Context of Electron Devices' explicitly cites In=0.15 Ppiezo=1.65e13 e/cm2 (Cambridge Core); Bernardini/Fiorentini/Vanderbilt Phys Rev B 56 R10024 (1997) spontaneous/piezo parameters. Exact CAL MaterialDB/strain/polarity unverified.
- Claude says WKB single-energy triangular spike estimate T~9e-3 and tunneling effect <=2x. The latter is NOT justified as an upper bound on energy-integrated current (unknown electron and hole distributions/masses/spike widths/transmission, possible assisted paths). MQW tunneling patch still ON HOLD.
- User forwarded Claude report that new independent version CMP_BASELINE_1.4.0_POL50 was generated by SWB Save As from 1.3.0_CAL4V, global Piezoelectric_Polarization(strain) changed to (strain activation=0.5) only; source/preprocessed pp2 diff line64, .par unchanged, no FixedCharge/override; isolated equilibrium smoke ran successfully and all user-reported PE_Charge interface samples halved 5.7719771e20 to 2.8859886e20 cm^-3. NtSide0 node2 same 4V 5V/s 0.8s run REPORTED STARTED, NOT reported completed. This is **source-level and smoke validation only**; entire 4V transport result not yet known. Preserve original CAL4V and JuSubin 5V_TEST.
- Critical prior inference: q*whole-domain recombination / anode I = 5.63% does NOT establish 94% transient charging. EBL SRH localization 99.77% by itself does not identify hole-injection cause; AlGaN SRH lifetime, electron leakage, current-continuity and net-generation remain checks.
- NEXT priority once POL50 finishes: paired 4V at same t and same normalized geometry: TotalCurrent anode/cathode, EBL total SRH, all QW Rad/SRH/Auger, B0 hole density, e/h QF, Potential and effective PE_Charge (smoke equilibrium separate), inspect if POL50 response supports sensitivity; a promising 50% is not a calibrated baseline and do not edit 100% control. If current 4V node run incomplete, inspect live job log first. Avoid additional long job before first comparison. Wiki/dash: https://taekgyu0801.github.io/GGYU/.

## 2026-10-12 — JuSubin confirms exact half contacts
Read-only SDE: yL=0.500um; yDL=0.505um; yC=2.500um (W_mesa=4um, W_domain=5um, W_damage=0.005um). Top anode DmgL 0.005um + Clean 1.995um = 2um; bottom cathode spans numerical base 0..2.5um. Conditional using default 1um depth: n2 5V J=7.24008e-4 A/cm2 and n4 5V J=3.52506e-4 A/cm2. Verify current unit/effective AreaFactor against installed T-2022.03 before declaring J validated. No TCAD changes. Next check physical normalization and injection/SRH; preserve prior runs.

## 2026-10-12 — JuSubin 5V_TEST SDE top/bottom electrode selection read-only (OBSERVED)
- Worker 주수빈, AI ChatGPT. Real server stdout `sed -n '415,495p' pp1_dvs.cmd`, unchanged source.
- SDE `sdegeo:define-contact-set` names "anode"/"cathode". Top p-contact `sdegeo:set-contact` assigns TWO distinct edges by `find-edge-id(position x0 ((yL+yDL)/2) 0)` and `find-edge-id(position x0 ((yDL+yC)/2) 0)` to anode, covering DmgL and Clean pieces of top half-mesa edge (provided edge geometry actually spans respective y ranges).
- Bottom n-contact assigns ONE edge at `position xb (yC/2) 0` to cathode; source comment explicitly says half-domain numerical n-GaN base spans y=0...yC. `y=yC` is artificial mirror-symmetry boundary, NOT etched sidewall.
- From previous observed W_mesa=4.0um and W_domain=5.0um for left-half symmetric model, predicted upper physical mesa span 2.0um and numerical bottom base 2.5um IF variable definitions satisfy yL=0.5, yC=2.5um; numerical values of yL,yDL,yC,x0,xb and exact edge lengths still to be read directly. Do not use bottom numerical-contact width as LED emission area.
- Previous `AreaFactor` literal text check had no matches in pp2_des.cmd, pp4_des.cmd, FASTC1_pp6_des.par, n2/n4 logs; still NO independently established effective 2D raw-current unit/default or verified physical current density. Prior conditional J n2 ~7.24008e-4 A/cm2 and n4 ~3.52506e-4 at 5V require unit and width verification.
- NEXT READ ONLY inspect `pp1_dvs.cmd` numeric definitions `yL,yDL,yC,x0,xb,W_mesa,W_domain` with grep and ensure SDE actual edge spans; no TCAD code/run/result edits.

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

## 2026-10-12 — 주수빈 5V_TEST n2/n4 equal-raw-terminal-current bias from n2 PLT (OBSERVED + LINEAR INTERPOLATION)
- Worker: 주수빈. Evidence: user terminal output of read-only 1023-point `n2_des.plt` scan against target `n4_des.plt` last 5V anode TotalCurrent=7.05011114486348e-12 (raw Sentaurus 2D values).
- n2 bracketing recorded points: (V=4.91836886499322, I=6.84313365428304e-12, t=0.983673772998644s) and (V=4.92336886499322, I=7.14463993632474e-12, t=0.984673772998644s). Nearest discrete n2 sample is V=4.92336886499322, I=7.14463993632474e-12 (absolute error=9.452879146125942e-14).
- Derived (LINEAR INTERPOLATION, NOT directly saved 2D result): n2 V at target raw I ≈ 4.921801256006416 V; n4 actual target voltage 5.0 V, so delta V=n4 minus n2≈+0.078198743993584 V = +78.20mV on 5 V/s transient sweep. Do not represent interpolation as an actually computed n2 spatial TDR or as validated steady-state series resistance.
- Only spatial TDR files in recursive project inventory are n2_des.tdr and n4_des.tdr at final nominal 5V. Thus the existing radiative/SRH/Auger eight-QW full-region 5V ratios 0.10947478% (n2) vs 0.04893717% (n4) CANNOT be compared as equal-current spatial recombination results. No intermediate-voltage TDR near ~4.9218V. Same raw electrode current doesn't yet mean calibrated physical current density (AreaFactor check pending) and n2 transient displacement at target bias is not yet checked.
- Next read-only n2 .plt nearest two points' DisplacementCurrent/eCurrent/hCurrent and current monotonicity; verify total-current definition / AreaFactor, decide what time and bias snapshots needed. Any new simulation/continuation requires explicit user decision; preserve completed files.

## 2026-10-12 — 이택규 Claude CAL4V 4V whole-domain recombination integration; interpretation correction (USER-REPORTED / DERIVED / UNRESOLVED)
- SOURCE: 이택규 전달 Claude 19:30 KST server-output summary; raw server .tdr / SVisual integration report not directly retrieved by this ChatGPT. Claude says CAL4V 4V `n2_4V_final_des.tdr` integrated whole-domain: SRH=12294.2, Radiative=2.43e-3, Auger=2.96e-4 [s^-1 um^-1]. Per reported named regions: Clean_EBL=12230.8, DmgL_EBL=34.8; Clean QW1 4.94, QW2 0.125, QW3 0.049, QW4 5e-5; previous 8-QW total SRH≈5.134. Anode TotalCurrent=3.498e-14 [A/um]. No source modifications or new simulations.
- DERIVED from transmitted values: EBL SRH subtotal 12265.6 / total 12294.2 = 99.76737% of modeled whole-domain SRH. 8-QW SRH fraction ≈0.04176%; Barrier1(19.6)+Barrier2(3.69)=0.18944%. Strong evidence for modeled EBL SRH localization **if** all region integrations are correct; NOT proof EBL hole barrier causes it. Check AlGaN actual SRH lifetime/Scharfetter parameters, electron/hole densities, field and region tags.
- DERIVED: q*(12294.2 + 0.00243 + 0.000296)=1.9697484e-15 [A/um]. Ratio to anode total=0.0563107=5.6311%. Under unverified normalization W=2um, equivalent J_rec=9.8487e-8 A/cm2. **CRITICAL CORRECTION**: the remaining 94.3689% is NOT demonstrated capacitive/transient current. q*net recombination is a bulk recombination sink, not independently the total DC conduction: it does not account for possible carrier through-current/leakage, carrier storage, generation, contact/boundary and terminal signs. Claim '94% charging and 5.6% true DC' is UNRESOLVED, not OBSERVED or CONFIRMED. Read-only anode Charge dQdt small (≈0.008 ratio 2.5–4 V) also does not prove or disprove total device charging since electrode charge scope differs from entire device; reported contact DisplacementCurrent ~1e-18 alone cannot classify the remainder.
- Claude ranks EBL/Barrier0/QW1 boundary hole transport candidate P1, intrawell NLM P2; both PROPOSED. Previous user-reported EBL hQuasiFermi flat complicates direct assignment of large hQF drop inside EBL; full cutline must resolve actual layer boundaries. Need both e/hCurrentDensity and n/p as well as QF, Potential, Ec/Ev, srhRecombination and PE_Charge.
- NEXT READ ONLY: (1) Verify entire integration spatial coverage/units, EBL effective SRH lifetime in actual `pp2_des.par` or effective SDevice material properties; (2) central verified CLEAN growth-direction x cutline from p-GaN through EBL–Barrier0–QW1 and MQW, with ElectrostaticPotential, Ec/Ev, e/hQF, e/hDensity, e/hCurrentDensity, SRH, PE_Charge; geometry lateral cutline to check y=2um clean position; (3) assess spatial current continuity/cathode currents and transient balance. No NLM/polarization/lifetime changes before verification. JuSubin 5V_TEST untouched.
- REFERENCE for general continuity/electrode-charge concepts: Sentaurus Device UG O-2018.06 Ch. 7 Electrode Charge Calculation and Ch. 8 Carrier Transport in Semiconductors, https://studylib.net/doc/27467177/sdevice-ug---%E5%89%AF%E6%9C%AC (older publicly viewable edition, NOT independent verification of T-2022.03 exact text).

## 2026-10-12 — JuSubin 5V_TEST all TDR/SAV inventory checked (OBSERVED)
- Read-only recursive `find . -type f ...` screenshot returns only 4 .tdr: n1_bnd.tdr, n1_msh.tdr, n2_des.tdr, n4_des.tdr; only 6 .sav: n2/n4 5V circuit/des checkpoint pairs plus n2_smoke_ckpt_0p3V circuit/des pair. No intermediate-bias spatial TDR observed. The smoke SAV filenames alone do not establish true 0.3V solved state (prior QS aborted near 0.019304636V; provenance uncertain). Existing 5V 4QW radiative fractions are not equal-current comparisons. Next read-only n2/n4 PLT full-I-V matched-current bias search; no new run or source edits.

## 2026-10-12 — 이택규 CAL4V Claude 19:30 재판단 전달 / ChatGPT 독립 검토 (USER-REPORTED / DERIVED / UNRESOLVED)
- SOURCE: 이택규가 Claude 작성 `CAL4V_LOWJ_LOWIQE_DIAGNOSIS.md` 텍스트를 현재 채팅에 제출. 이는 **Claude 보고서의 내용**이지 ChatGPT가 Sentaurus 학교 서버나 T-2022.03 원본 문서를 직접 검증한 결과가 아님. 기존 CAL4V 코드/실행 변경 없음.
- Reported CAL4V 4V: anode TotalCurrent=3.498e-14 A/um; QW integrals Rad=6.29e-4, SRH=5.13, Auger=2.13e-4 s^-1 um^-1. From these values, q*(Rad+SRH+Auger)=8.221e-19 A/um and ratio to anode total=2.350e-5 (0.002350%). This **does not itself prove** 98% charging current or hole-only starvation: QW-outside recombination, other leakage paths, transient charge and sign/normalization must be checked.
- Claude RETRACTED claims that 4V current is 98% charging, MQW QF jumps add up to 2V loss, or EBL band bending proves 1V electrostatic loss. Claude reported parent 5V displacement=3.29e-18 against total=1.448e-11 (different run/bias); cannot infer 4V CAL4V charging fraction from 5V parent electrode component. Earlier 4V I(V) plateau and tau-insensitive anode current are suggestive, not direct transient charging measurement.
- Claude also reported flat hQuasiFermi through EBL on user SVisual cutline, reducing evidential support for EBL as dominant **hole electrochemical potential drop**. QW1 radiative concentration alone cannot establish which carrier is limiting; inspect n, p, e/h current and QF across verified coordinates.
- Claude reported T-2022.03 UG text inspection: NonLocal keywords exist but proposed V2 has potential wrong mesh-side coverage and missing tunneling mass mt. Exact manual excerpts were not independently made accessible to this ChatGPT; no V2 deployment. Model choice (NLM/polarization/composition variation) UNRESOLVED, baseline protected.
- Important verification boundary: SDevice `anode Charge` is **electrode charge plus associated doping-well space charge**, not necessarily the device-wide stored-charge integral (O-2018.06 UG, Electrode Charge Calculation). Thus d(anode Charge)/dt / anode TotalCurrent near one is a diagnostic only, NOT a sufficient standalone confirmation that 90-100% of current is junction charging; require terminal signs/conservation, time/bias dependence and charge scope. 4V conduction-vs-charging remains unresolved.
- NEXT (READ-ONLY): inspect CAL4V `n2_des.plt` actual datasets and synchronized `anode/cathode Charge, TotalCurrent, DisplacementCurrent, eCurrent/hCurrent, time, bias`; estimate finite differences with units/signs and no sharp arbitrary thresholds. Then export verified central clean-region TDR cutline e/hQF, density, current, Ec/Ev, Potential, polarization fields; resolve actual NLM coverage/manual before any user-approved small-scale smoke. JuSubin 5V_TEST untouched.

## 2026-10-12 — JuSubin 5V_TEST n4 final anode current (OBSERVED)
- Parsed n4_des.plt 1023 records to final t=1s, 5V. Raw Total=7.05011114486348e-12, Displacement=3.38231191699972e-18, electron=7.53447212445082e-14, hole=6.97476304130706e-12. Versus n2 at same endpoint raw Total=1.44801646079583e-11, electron=2.78143237811134e-13, hole=1.42020180788235e-11, displacement=3.29132361382365e-18. n4 total -51.31194%, electron -72.91154%, hole -50.88893%. At last point displacement negligible in both. Does not establish physical J or steady-state; next n2/n4 full I-V matched-current check & available TDR. No TCAD edits.

## 2026-10-12 — JuSubin 5V_TEST n2 final-time current components (OBSERVED)
- `n2_des.plt` read-only parsed 1023 DF-ISE records. At time 1s, anode V=5V: raw TotalCurrent 1.44801646079583e-11; DisplacementCurrent 3.29132361382365e-18; eCurrent 2.78143237811134e-13; hCurrent 1.42020180788235e-11. Displacement/total 0.00002273%, negligible at last record. This does NOT establish time steady-state or validated 2D J normalization/QW injection. Next n4 PLT current decomposition and matched-J review. No TCAD source changes.

## 2026-10-12 — JuSubin 5V_TEST n2/n4 eight-QW three-channel recombination comparison (OBSERVED)
- Worker 주수빈. Evidence: Sentaurus Visual Field Integration pasted outputs for RadiativeRecombination, srhRecombination, AugerRecombination on 8 distinct 2D regions Clean_QW1..4 + DmgL_QW1..4 (avoid '+' interface labels). Total Domain 0.02400002 um² for each node, units for all integrals s^-1 um^-1.
- n2 NtSide0: Radiative 40072.82; SRH 36562940; Auger 1599.707; 3-channel total 36604612.527; Radiative fraction 0.10947478264%; SRH share 99.88615498397%; Auger share 0.00437023339%.
- n4 NtSide1e18: Radiative 7056.261; SRH 14411700; Auger 265.2578; 3-channel total 14419021.5188; Radiative fraction 0.04893716949%; SRH share 99.94922319250%; Auger share 0.00183963801%. n4 Auger detailed Clean region sum (display rounded)=264.6098086; DmgL region sum=0.6480449636; rounded sum 265.25785356 (within display rounding of stated total).
- n4 relative to n2 at nominal 5V: Radiative -82.3914%; SRH -60.5839%; Auger -83.4184%; radiative fraction relative decrease 55.2982% (absolute -0.0605376 percentage points).
- Grouped 3-channel radiative shares from region-rounded sums: n2 Clean ~0.10984%, DmgL ~0.05195%; n4 Clean ~0.04909%, DmgL ~0.02484%. Regional fractions represent spatially integrated model channel ratios only.
- CRITICAL INTERPRETATION: these are 4QW modeled 3-channel recombination fractions, NOT measured EQE or independently validated whole-device IQE. n2 raw 5V current=1.4480164608e-11 vs n4=7.050e-12 (different injection), so fixed-voltage difference is not matched-current trap causal proof. TCAD 2D current AreaFactor, time-dependent/displacement contribution, QW hole injection and physical calibration still require validation. Node2 explicit 12 DmgL sidewall traps Conc=0 while global SRH is active. Dominant SRH is an observation, its microscopic cause is not established.
- NEXT: review n2/n4 electrode TotalCurrent vs DisplacementCurrent and normalized J from saved .plt; examine whether equal-current comparison is possible with existing saved intermediate 2D TDRs, else mark additional snapshot requirements before any new run. Do not modify baseline/code or rerun until plan approved.

## 2026-10-12 — JuSubin n2 Auger OBSERVED
SVisual n2 eight-QW Auger integral 1599.707 s^-1 um^-1, domain 0.02400002 um^2. Prior n2 radiative 40072.82 and SRH 36562940 give 3-channel radiative share 0.10947478%, SRH 99.88615498%, Auger 0.00437023%. These are internal model ratios, not validated EQE. Next n4 Auger same ROI. No TCAD changes.

## 2026-10-12 — CAL4V MQW tunneling v2 still PROPOSED; Rahman FE/QB confirmed (OBSERVED user report / CRITICAL REVIEW / PROPOSED)
- 2026-10-12 18:23+ KST 이택규 supplied second Claude proposed CAL4V patch: SVisual center(? y=2.0um) x=0.10..0.30um QW band cutline shows sharp ~0.35-0.5eV jumps in electron/hole quasi Fermi across QW/Barrier interfaces, EBL bent Ev ~-4.0 to -5.05 and Ec~-0.3 to -1.55. Values are USER-REPORTED from SVisual, no raw screenshot/point data independently read; lateral y=2.0 may be edge depending half-device coordinate, so actual region/cutline must be checked. Critical physics review: across QWs BOTH eQF and hQF rise in same direction, so local F_n-F_p approximate QW1~1.95,QW2~1.90,QW3~1.75,QW4~1.45 eV; these splits are not voltage loss from 4V. QF jumps permitted at Thermionic heterojunction boundary, thus not proof of absent tunneling. EBL ~1eV band edge slope not equivalent direct electrostatic voltage drop without Potential/offset extraction. Capacitive equivalent thickness ~24nm near EBL26nm is NOT proof of voltage localization. Existing n2_des.plt true transient DisplacementCurrent not yet extracted; do not treat total as conduction nor 98% claim as verified. Important corrected external literature finding after reading primary full 11-page PDF: Rahman, Jamal-Eddine, Xia, Awwad, Armitage, Rajan, J Appl Phys 132:235702 (2022) DOI 10.1063/5.0125684 / arXiv 2211.05704 explicitly uses thermionic emission (TE), field emission (FE), and non-local quantum barrier tunneling (QB tunnel) across QWs/QBs in SILVACO TCAD (p3 lines 102-114); Fig3c p5 says including FE and QB transport improved forward-voltage trends; BUT even all relevant transport models uniform-well simulation overestimated turn-on, and actual key improvement was composition fluctuation low/high In lateral current path. Thus strong support to TEST a QB tunneling sensitivity as model physics, NOT proof Sentaurus T2022 source syntax or that QB tunneling alone fixes homogeneous CAL4V blue 4QWs. Older SDevice guide O-2018.06/H-2013.03 independently checked on web: global Math NonLocal named mesh supports reference MaterialInterface/RegionInterface/Electrode with Length/Permeation/Direction/MaxAngle; global Physics eBarrierTunneling meshname,hBarrierTunneling meshname; Plot eBarrierTunneling/hBarrierTunneling valid field rates (per cm3/s) with mesh dependence. The EXACT required T-2022.03 UG text reference/tcad_ug_text/sdevice_ug.txt is NOT present in connected CMP GitHub or available directly, so ALL EXACT VERSION SYNTAX compatibility explicitly unverified; user-reported T2022 line ranges 43563 etc cannot be independently crosschecked. Do not claim syntax has been verified T2022. New proposed NonLocal Math(MaterialInterface=InGaN/GaN Length=5e-7 cm Permeation=5e-7 cm Direction=(1 0 0) MaxAngle=5 degrees) may target material interfaces regardless clean/Dmg lateral branch if actual material identities appropriate; actual count 4 QW*2 vertical interfaces =8 vertical planes, each split into clean/damaged lateral segments. Count/lines require simulator log, not assumed. Direction x normal is conceptually consistent if actual mesh x growth (user-reported) but MaxAngle5 can suppress tilted paths. Length/Permeation 5nm are geometrical nonlocal mesh limits NOT necessarily physically calibrated spike thickness or tunnel through 22nm GaN quantum barriers; actual lines need inspect, potential risk double-count or unintended paths. Since QB22nm, 5nm likely insufficient as full interwell bridge, may still sample narrow interface spikes. e/h tunneling can increase compute time, user approval needed, no Run or code changed. Do not accept 'Goal3.5V total I>=1e-12A/um' as scientifically grounded pass/fail; if ramp same5V/s charging current may remain, total is not DC conduction; compare matched bias/current true conduction after ramp-hold/stationarity, QF discontinuity and QW n/p and recombination, inspect tunneling rates integrated/mesh dependence. Sequence: existing CAL4V PLT displacement current, QW band/charge/current cutlines in non-damaged central region; verify effective 2022.03 manual actual excerpts and NonLocal generated lines, THEN separate minimal test (1D-like 2D column not representative of sidewalls; prior QS failed); only after successful physics-sensitive trial consider versioned 2D half study and compare with saved untouched CAL4V. Polarization 50% literature-assumed sensitivity (Lu 2021 DOI 10.1186/s11671-021-03557-4; Yin 2024 DOI 10.1007/s12200-024-00111-9), not calibrated or a substitute for QB. No changes to JuSubin 5V_TEST and no scripts run. Scientific decision status: QB NLM is PROPOSED for independent test after proof of transport restriction, not baseline adopted. Main blocker physical low-J Gate0 remains.

## 2026-10-12 — JuSubin 5V_TEST n4 8-QW SRH integrated; 2-channel comparison (OBSERVED)
- Worker: 주수빈. User-provided Sentaurus Visual Field Integration exact result: dataset n4_des, field srhRecombination, 8 separate 2D QW regions Clean_QW1..4 and DmgL_QW1..4. Total Integral=1.441170e+07 s^-1 um^-1, Total Domain=2.400002e-02 um^2.
- n4 Clean_QW1=7.535253e4, QW2=2.335633e4, QW3=2.936031e5, QW4=1.392685e7; subtotal of region-rounded values=14,319,161.96. n4 DmgL_QW1=3.279025e2, QW2=8.810076e1, QW3=7.204654e2, QW4=9.139782e4; subtotal=92,534.28866. Rounded-entry sum=14,411,696.24866 vs displayed SVisual total=14,411,700, normal decimal rounding difference.
- Previously observed same 8-region n2 SRH total=3.656294e+07; n2/n4 Radiative totals=4.007282e4/7.056261e3 s^-1 um^-1. At nominal 5V, n4 SRH total lower by 60.5839%, while Radiative lower by 82.3914%.
- Two-channel Rad/(Rad+SRH) is n2 0.1094796%, n4 0.0489381% (n4 ~55.30% relatively lower). This is NOT final IQE; Auger integration incomplete, both 5V terminal currents differ and current-density normalization/physics remain unresolved. SRH falling with trap ON does not prove nonradiative trap effect absent: injection levels differ.
- NEXT: On n2 and n4 SVisual integrate AugerRecombination for same eight 2D QW regions, inspect signs, then calculate 3-channel radiative share; matched-current comparison separately. No solver rerun or TCAD code/mesh change.

## 2026-10-12 — JuSubin n2 4QW SRH observed
- n2_des srhRecombination over same eight 2D QW regions Total 3.656294e7 s^-1 um^-1, domain area 0.02400002 um^2; QW4 contributes ~98.0342%. n2 radiative=4.007282e4; two-channel Rad/(Rad+SRH)~0.10947957%, NOT IQE until Auger integration and physical validation.
- Next n4 SRH and n2/n4 Auger on same eight 2D ROI; no code/source/mesh changes.

## 2026-10-12 — CAL4V Claude audit and parameter-change caveats (REVIEW)
- 2026-10-12 18:23 KST, worker 이택규 shared Claude independent CAL4V low-J diagnosis for critical review. This is REVIEW, NOT actual new simulation evidence. 1. CAL4V 4V Transient ramp 5V/s, terminal total=3.498e-14 A/um. Claude says 98% displacement and conduction 0.7e-15 A/um. Actual charging fraction UNVERIFIED: plateau alone cannot decompose; inspect n2_des.plt anode DisplacementCurrent and TotalCurrent data at 4V. Current-density conversion remains conditional on 2D normalization. Output eCurrent~5.27e-20, hCurrent~3.498e-14, total~3.498e-14 should be identified carefully before claims. 2. With all current assumed capacitive, C'=I/(5V/s)=6.996e-15 F/um. eps_r 9.5 and 2um x1um assumed footprint give equivalent t~24.0nm near EBL 26nm; arithmetic correct but distributed capacitance cannot localize EBL voltage drop. Need actual Ec/Ev/Potential profile. 3. From Rrad/SRH ≈ B tau (n+p) with B=2e-10 cm3/s and tau=100ns, n+p≈6.12e12 cm-3 conditional on ideal Bnp, equal lifetimes, negligible SRH n1/p1, uniform carrier density; integrated 8-QW values and doping-dependent lifetime invalidate direct inference. Not proof of low hole density. 4. EBL hole barrier/polarization is scientifically plausible from published studies but causal ranking remains PROPOSED; alternative current normalization, contact injection, active hole doping, band offsets, distributed carrier density, missing calibrated transport physics remain. 5. Literature verified: Lu et al 2021 Nanoscale Research Letters 16:99 DOI 10.1186/s11671-021-03557-4 explicitly uses 50% polarization and 100ns SRH; Yin et al 2024 Frontiers of Optoelectronics 17:8 DOI 10.1007/s12200-024-00111-9 explicitly uses 50% polarization, 100ns and SRV=1e4 in different MIS microLED; Baek et al 2023 Nat Commun 14:1386 DOI 10.1038/s41467-023-36773-w is low-current QB/EBL engineering (not source for 50% polarization); Rahman et al 2022 JAP 132:235702 DOI 10.1063/5.0125684 explains composition fluctuations / limits 1D fixed-polarization models, not proof a specific Nonlocal tunneling keyword is mandatory. 6. Do not copy global eBarrierTunneling+hBarrierTunneling with NonLocal Barrier(Region=Clean_EBL Region=DmgL_EBL) Length=4e-6 into current model. Sentaurus documentation states Barrier(...) mesh configuration primarily for direct insulator barriers; AlGaN EBL is semiconductor, actual valid T2022.03 geometry and tunneling masses/method unknown. Turning polarization off only at AlGaN/GaN interfaces does NOT remove InGaN/GaN MQW QCSE. Polarization 0% and 50% allowed only as clear diagnostic/sensitivity hypothetical with original 100% controlled, no arbitrary recalibration. Next: inspect existing n2_des.plt dataset list for DisplacementCurrent/TotalCurrent and 4V values, then SVisual existing n2_4V_final_des.tdr vertical center cutline Ec/Ev, quasi Fermi, n/p, PiezoCharge and current density; ONLY then consider independently versioned 1D controlled stack or 2D half run. 1D loses mesa/sidewall and QS may not converge; no promise faster. Maintain JuSubin 5V_TEST split ownership. No simulation/TCAD source changed.

## 2026-10-12 JuSubin 5V_TEST radiative comparison (OBSERVED)
SVisual 8 2D QW regions: n2 total 40072.82 vs n4 total 7056.261 s^-1 um^-1 at nominal 5V, -82.3914%. Both total areas 0.02400002 um^2. Currents differ, not an IQE or equal-current comparison. NEXT JuSubin integrate same-QW SRH and Auger for n2/n4, then radiative fraction. No TCAD source edit.

## 2026-10-12 — CAL4V explicit sidewall traps are all zero (OBSERVED)
- 2026-10-12 이택규 read-only live CAL4V pp2_des.cmd grep confirms twelve explicit `Traps` blocks at 141/161/181/201/221/241/261/281/301/321/341/361, all corresponding `Conc=0` lines 145/165/185/205/225/245/265/285/305/325/345/365. Therefore 4V completed CAL4V n2 is **explicit NtSide trap OFF** (source preprocessing evidence), yet prior MQW 8-QW integrated recombination Rrad=6.286680e-4, SRH=5.134239, Auger=2.127778e-4 (s^-1 µm^-1), radiative fraction 0.01224261249% and SRH 99.98361378%. Those zero-concentration explicit sidewall traps cannot cause observed CAL4V SRH dominance, but unknown other SRV/interface or bulk SRH mechanisms cannot be excluded. Active global Physics contains SRH(), Auger(), Radiative, Fermi, Thermionic, Piezoelectric_Polarization(strain), custom referenced InGaN Scharfetter taumax=1e-7 s; physical carrier transport and 2D current normalization remain unverified. Hypotheses about bad contact, EBL/polarization or carrier imbalance remain UNRESOLVED, not findings. Next read-only inspect current-density normalization in SDevice output and available .plt or existing electron/hole densities in 4V final TDR, and possibly effective QW doping. No code or simulator change. Independent track from JuSubin 5V_TEST trap ON/OFF study.

## 2026-10-12 — CAL4V region Physics audit step (OBSERVED)
- 이택규 provided real CAL4V pp2_des.cmd read-only grep: global Physics line 50, Piezoelectric_Polarization(strain) 64, global SRH() 80; separate Physics(Region="Clean_pGaN") at 126 and 12 Physics(Region="DmgL_...") at 135,159,179,199,219,239,259,279,299,319,339,359. No separate Recombination/SRH declaration and no literal SurfaceRecombination, SurfaceTrap, Interface= matched in this search. Plot SRHRecombination et al at 398+ are output field names, not evidence of extra active recombination. IMPORTANT search omitted Traps, so region-specific explicit traps may still exist; absence of named surface keywords does not prove actual SRV=0. Existing CAL4V referenced InGaN Scharfetter taumax=1e-7s remains confirmed nominal. Root cause of low J/radiative fraction unresolved. NEXT perform read-only `grep -nEi 'Traps|Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/pp2_des.cmd | head -n 35` to check n2 trap concentrations. No model changes; separate JuSubin 5V_TEST split task unaffected.

## 2026-10-12 — CAL4V Scharfetter taumax=100ns effective param source confirmed (OBSERVED)
- 2026-10-12 이택규가 실서버 read-only grep 출력으로 CAL4V actual custom material parameter file `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/FASTC1_pp6_des.par`의 `Material="InGaN" { Scharfetter {...} }` 항목을 확인. pp2_des.cmd의 File Parameters가 바로 이 파일을 가리키고 Global Physics에서 SRH() 활성화. InGaN Scharfetter lines 47–53: `taumin = 0.0,0.0`, `taumax=1.0e-7,1.0e-7` seconds, `Nref=1.0e16,1.0e16` cm^-3, `gamma=1,1`, `Talpha=0.0,0.0`, `Tcoeff=0.0,0.0`. Therefore nominal maximum electron/hole lifetime 100ns actually PRESENT in referenced CAL4V custom .par, and missing-entry hypothesis weakens. Scharfetter is doping-dependent; 100ns is a maximum under this parametrization, NOT a verified spatially constant effective QW lifetime. QW doping/concentration and any Material/Region Physics/SRH overrides unknown. This does not solve extraordinarily low raw 4V terminal current or 8-QW 3-rate fraction 0.0122426%, and no rationale to tune params again. NEXT read-only inspect remaining pp2_des.cmd Physics blocks and interface SRV, QW doping and actual injection/2D current scaling, keeping JuSubin's separate NtSide 5V_TEST track untouched. OBSERVED source setting; effective per-point carrier lifetime and physical adequacy UNVERIFIED. No SDevice/model changes.

## 2026-10-12 — CAL4V File/Electrode/Physics 14-90 verified
- 2026-10-12 이택규 CAL4V의 실제 `pp2_des.cmd` lines 14–90 read-only sed 출력 제공. File: Grid=n1_msh.tdr; Parameters=FASTC1_pp6_des.par; Plot=n2_des.tdr; Current=n2_des.plt; Output=n2_des.log. Electrode anode/cathode both initial Voltage=0.0. Global Physics: Temperature=300.0, Fermi, Thermionic, Piezoelectric_Polarization(strain), DefaultParametersFromFile, EffectiveIntrinsicDensity(NoBandgapNarrowing), Recombination(SRH(), Auger(), Radiative). 이 블록은 세 재결합 모델 활성화의 직접 증거지만 InGaN 유효 SRH tau=100ns 또는 국소 재결합 수치의 근거 자체는 아니다. 이전 whole pp2 grep에는 AreaFactor 미표시; 단자 전류 단위, 2D normalization 미확인. 다른 per-material/per-region Physics overrides, 명시적 surface recombination 설정 존재 여부도 아직 미확인. NEXT 별도 CAL4V custom active par `FASTC1_pp6_des.par`에서 InGaN Scharfetter/SRH tau 및 active material blocks 읽기전용 검사; 이후 pp2 global/local Physics 범위와 current scaling 검증. 서버 파일이나 계산 결과 변경 없음. 주수빈의 5V_TEST split parity/QW integration과 다른 독립 track 유지.

## 2026-10-12 — CAL4V pp2 Grid/Parameters and polarization grep inspected (OBSERVED)
- 2026-10-12 ~17:xx KST 이택규가 CAL4V 전처리 입력 pp2_des.cmd에서 읽기전용 grep 실제 출력 제공: `20: Grid="n1_msh.tdr"`, `22: Parameters="FASTC1_pp6_des.par"`, `26: Current="n2_des.plt"`, `60: Thermionic`, `64: Piezoelectric_Polarization(strain)`, `462: PE_Polarization/vector`, `466: PiezoCharge`. 주어진 grep 정규식에 대한 `AreaFactor` 결과 없음. 이는 pp2_des.cmd 내 명시적 AreaFactor 항목이 없는 것으로 보인다는 관찰이며, 실제 terminal current A/µm/2D normalization 또는 활성 polarization 전하 크기가 정확하다는 뜻이 아님. Polarization 및 Thermionic 선언은 존재하나 정확한 Physics 범위, piezo activation, parameter value는 추가 확인 필요. 저주입/0.01224% 방사비율의 원인을 단정하지 않으며, 다른 연구원 주수빈이 맡도록 제안된 n2/n4 5V Trap-on/off 작업과 중복하지 않음. NEXT CAL4V pp2 `sed -n '14,90p'` 읽기 전용으로 File/Electrode/Physics/Math/계면 블록 범위 확인; 이후 active .par 및 n2_des.log 2D 단위/AreaFactor audit. 실행 코드 및 결과 변경 없음.

## 2026-10-12 — Worker coordination proposal; two nonoverlapping work tracks
- 2026-10-12 ~17:03 KST, current worker 이택규 says he is now working alongside 주수빈 and wants nonoverlapping tasks. Proposed coordination (not confirmed as accepted by 주수빈): 이택규 owns read-only physical Gate0/low-current audit in separate project `CMP_BASELINE_1.3.0_CAL4V` (2D terminal current units/AreaFactor, active InGaN SRH 100ns, QW injection/EBL/polarization) without source modifications; 주수빈 may own `JUSUBIN_FAST_HALF_5V_TEST` NtSide0 Node2 vs NtSide1e18 Node4 5V parity gate (pp2/pp4 deck and .par/mesh differ only trap) followed by paired MQW Rrad/SRH/Auger integrals, avoiding overlapping CAL4V. Both finished sources/results remain protected. Last user-provided `pp4_des.cmd` grep explicitly showed 12 Traps Conc=1e18, confirming planned NtSide1e18 actual preprocessing (pending pp2-vs-pp4 other-input parity). No fresh simulation or technical result here; this is a PROPOSED parallel work allocation. AI cannot directly send task to collaborator's separate chat; share via GitHub as a proposed handoff only.

## 2026-10-12 — 5V_TEST n4 finished and 5V terminal current shown
- 2026-10-12 현재 작업자 이택규가 SWB Node4 Explorer 실제 `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/n4_des.out` 마지막 화면 제공. 노드 n4: 5.000E+00 V, electron current 7.534E-14, hole current 6.975E-12, total terminal current 7.050E-12 (log raw values; 2D units/AreaFactor unverified), successful `n4_5V_ckpt_des.sav` and `n4_des.tdr` writes, `Curve trace finished`, `Sentaurus Device simulation finished`, `Good Bye`. Finished Mon 2026-10-12 00:12:02 KST; wallclock 29806.55s (~8h16m46.55s), CPU total 80172.55s, peak memory 3.11GB. **CONFIRMED 5V SDevice n4 completion**, but screenshot does not show NtSide parameter: intended n4 NtSide1e18 split condition NOT CONFIRMED until pp4_des.cmd actual DmgL trap `Conc` audit and parent n2 input comparison. Previous 5V_TEST NtSide0 n2 terminal raw I2D~1.4480164608e-11, so n4 raw current ratio ~0.487; no trap-only causal claim without pp2/pp4 parity. CAL4V 100ns 4V MQW radiative fraction=0.0122426% remains distinct simulation and bias; do not confuse n4 5V with CAL n2 4V. GitHub COMMON_BASELINE.md explicitly says blue InGaN/GaN, xIn=0.15 4QW, nominal ~445nm; desired color BLUE not red, spectral peak not verified by EL. Researcher asks whether normal efficiency '0.1': distinguish fractional 0.1=10%, 0.1%=0.001 as fraction, 0.1 A/cm2 current density not an efficiency. None is default expected at arbitrary J; literature (Kou 2019 10.1364/OE.27.00A643; Baek 2023 10.1038/s41467-023-36773-w; Wang 2023 10.1038/s41467-023-43472-z) confirms blue microLED efficiency depends on J, fabrication and sidewalls. CAL 0.01224% is modeled MQW 3-mechanism radiative share, NOT observed experimental EQE, and physical low-J Gate0/2D current normalization still open. NEXT read-only `grep -nE 'Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp4_des.cmd | head -n 16` to confirm actual trap concentrations. Further compare pp2/pp4 other physics/current and matched 5V QW recombination; preserve all existing outputs. No server code modified.

## 2026-10-12 — CAL4V 0.01224% physically unvalidated vs literature
- 2026-10-12 Research assessment (이택규 question whether CAL4V radiative fraction 0.01224% is typical): Treat result as unusually low vs peer-reviewed working MicroLEDs, NOT sufficient proof of a model defect. Evidence: CAL4V 4.000V 2D raw terminal current 3.498e-14 (assuming A/µm), conditional half width ≈2µm gives J=(3.498e-14/2)*1e8≈1.749e-6 A/cm²; current conversion/AreaFactor/actual injection/steady-state remains unverified. Thus this is ~0.01/1.749e-6 ≈5718x below a published low-J example 0.01 A/cm² and ~0.1/1.749e-6≈57176x below 0.1 A/cm² benchmark. Published 3.5µm NBE-etched blue MicroLED Nature Communications 2023 DOI 10.1038/s41467-023-43472-z reports peak EQE 37.5% around 3 A/cm² and at 0.01 A/cm² only ≈26% relative droop; Nature Communications 2023 DOI 10.1038/s41467-023-36773-w reports 10x10µm blue MicroLED EQE 3.00% at 0.1 A/cm². Neither EQE benchmark is directly comparable to this model's MQW three-rate radiative share due to injection, geometry, sidewall processing and extraction differences. SRH normally dominates extremely low-current regime (literature-supported), but here NtSide0 still high SRH implies bulk/volume SRH or injection bottleneck rather than explicit sidewall trap; cannot infer causal parameter without matching sample and checking effective par. Existing parent 1ns at 5V had 0.10947% integrated QW fraction; CAL100ns at 4V is NOT matched bias, so changing lifetime cannot be causally judged. Recommended PRIORITY: verify current units, 2D AreaFactor, actual working J, effective InGaN 100ns parameter overrides, p/hole-injection/EBL/polarization/quantum well carrier densities, compare QW rates at same current and bias before baseline freeze, and avoid unmotivated long reruns. This is literature-backed review/diagnostic recommendation; NO simulation/model edit or confirmation of a single root cause.

## 2026-10-12 — CAL4V all four QWs Clean+DmgL 4V recombination totals observed
- 2026-10-12 이택규가 Sentaurus Visual 캡처 3장으로 완료된 `CMP_BASELINE_1.3.0_CAL4V` `n2_4V_final_des` (4.000V; custom InGaN 100ns Scharfetter taumax model) 8개 **2D** QW 영역 `Clean_QW1..4 + DmgL_QW1..4` 적분 결과를 제공. 세 필드 모두 정확히 동일 영역, Total Domain=2.400002e-02 µm². 전체 적분값 [s^-1 µm^-1]: RadiativeRecombination=6.286680e-04; srhRecombination=5.134239; AugerRecombination=2.127778e-04. 합=5.1350804458. Radiative/(Rrad+SRH+Auger)=0.01224261249%; SRH share=99.98361378%, Auger=0.004143612%. 여기서 방사비율은 해당 세 재결합 필드의 **MQW spatial integrated radiative fraction**이며, 100ns 모델 소자/실험 검증 IQE 또는 EQE가 아님. QW1 Clean+DmgL accounts for approx 98.78% all-4QW Rrad. DmgL 4QW only radiative ≈5.35942e-05 and SRH≈0.020185 (subtract clean 4QW totals; rounded), not independent lifetime physics validation. Preexisting 1ns parent result (NtSide0, **5V**) 4-QW Clean+DmgL Rrad=40072.8158452, SRH=36562944.9075, Auger=1599.706168587 and radiative fraction=0.1094747566%; because these are at DIFFERENT biases (100ns 4V, 1ns 5V), cannot attribute change to lifetime or claim 100ns improves/worsens IQE. Parent 4V near-terminal-current PLT exists but 4V TDR spatial map not yet established. Low-J Gate0 and current-normalization/physical validity still UNRESOLVED. Next inspect other user-reported completed NtSide1e18 split normal-finish log; for IQE causality compare same J/voltage/regions/geometry and effective .par, ideally reuse saved checkpoints, avoid rushing new multi-day run. No code/server run changed.

## 2026-10-12 — CAL4V 4 Clean QW integrated recombination fractions observed
- 2026-10-12 이택규 provided THREE SVisual Field Integration screenshots for CAL4V final dataset `n2_4V_final_des`, 4.000V, selecting ONLY the four dimension-2 regions `Clean_QW1` through `Clean_QW4` (not damaged sidewall strips). Recombination integrals unit s^-1 um^-1, in QW1/QW2/QW3/QW4 order: Radiative [5.674131e-4, 7.202020e-6, 4.579290e-7, 8.117469e-10] (displayed total 5.750738e-4); srhRecombination [4.940556, 1.246185e-1, 4.882792e-2, 5.108214e-5] (displayed total 5.114054); Auger [2.045051e-4, 1.234635e-7, 1.495005e-8, 8.907546e-11] (displayed total 2.046436e-4). Four Clean QW total area 2.394002e-2 um2. With displayed rounded totals sum=5.1148337178 and eta_rad,clean=0.01124326%, eta_SRH,clean≈99.9848%; QW1 accounts ~98.67% of clean-QW Rrad, ~96.61% clean-QW SRH. This is CONFIRMED SCREENSHOT-BASED 4-CLEAN-QW regional recombination fraction, NOT the full MQW IQE: `DmgL_QW1..4` not selected, no 1ns matched bias / optical injection calibrated comparison. Do NOT compare raw 4V clean-QW value to earlier 1ns 5V full-Clean+DmgL MQW radiative fraction (0.10947%) as lifetime-causality. Next select the 4 additional `DmgL_QW1..4` true 2D regions (not `Clean_QW# + DmgL_QW#` interface rows), while keeping Clean_QW1..4, repeat three integrations, check exactly 8 regions and no other domains, then compare and validate AreaFactor/current. Low-J baseline gate remains UNRESOLVED; no model or server code modified.

## 2026-10-12 — CAL4V Clean_QW1 numerical integration, only one QW (OBSERVED)
- 2026-10-12 이택규 공유 SVisual `CMP_BASELINE_1.3.0_CAL4V/n2_4V_final_des` Field Integration 실제 결과: Dimension 2 region `Clean_QW1` 하나만 선택, Domain=5.985012e-03 um^2; RadiativeRecombination=5.674131e-04 s^-1 um^-1; srhRecombination=4.940556 s^-1 um^-1; AugerRecombination=2.045051e-04 s^-1 um^-1. 3항 합=4.9413279182 s^-1 um^-1. Clean_QW1에 한정한 radiative fraction =0.0114830084%, SRH fraction=99.9843783%. VERIFIED screenshot-based single-region integrations and ARITHMETIC; NOT entire four QWs, not total device IQE. Other QWs may differ substantially. Next integrate 2D volume Clean_QW1..4 AND DmgL_QW1..4 in all three fields (avoid `Clean_QW1+DmgL_QW1` interface rows if shown as Dimension 1). Compare 100ns 4V with 1ns at matched V/J and check current normalization. No TCAD source edits. NtSide1e18 split separate log verification remains.

## 2026-10-12 — CAL4V final SVisual recombination scalar fields present (OBSERVED)
- 2026-10-12 이택규 제공 Sentaurus Visual T-2022.03 screenshots for `CMP_BASELINE_1.3.0_CAL4V` loaded dataset `n2_4V_final_des` (saved final 4V field). Observed Scalars `RadiativeRecombination` visible, color range min -8.67029e-34 max 7.00132e13 cm^-3 s^-1; `srhRecombination` visible, min -6.57253e-06 max 2.98898e18 cm^-3 s^-1. Earlier screenshot showed `AugerRecombination` as available Scalar. Mesh status shows Elements=138194, Points=65513. These are MAXIMUM VALUES ACROSS DISPLAYED SPATIAL FIELD and may not be colocated / may be in different physical regions. DO NOT interpret ratios of maxima as IQE or whole-QW integrated recombination; maxima do not establish 100ns physical IQE improvement. Need use Regions tab to identify Clean_QW1..4 and DmgL_QW1..4 region names in current saved TDR, then integrate RadiativeRecombination, srhRecombination, AugerRecombination separately in matched QW regions, ensure geometry/units 2D and compare to prior 1ns at matched bias. Other NtSide1e18 split separately pending log verification. Data only displayed, no 3-rate integral or new run/code change.

## 2026-10-12 — CAL4V exact final anode 4.000V and last-column current 3.498e-14 (OBSERVED log)
- 이택규가 실제 `CMP_BASELINE_1.3.0_CAL4V/n2_des.log` grep 출력 공유. 마지막 `Computing BE-step from 0.799739 s to 0.8 s (Stepsize: 2.6098e-04 s)` 직후 `anode 4.000E+00 5.270E-20 3.498E-14 3.498E-14`가 표시됨. 직전 단계 0.798939→0.799739s에서는 anode 3.999V, 총전류 표기 3.496E-14. 앞서 확인된 동일 Node2 `Curve trace finished` / `Good Bye` 및 final `n2_4V_final_des.tdr`, `n2_4V_ckpt_des.sav` 저장과 연결되므로 100ns CAL4V에서 최종 time 0.8s / anode 4.000V, 로그 전류 마지막 열 3.498E-14 달성과 정상 완료 CONFIRMED. 로그 전류 물리 단위/2D AreaFactor 및 정상 DC상태는 독립 검증 미완료; 기존 기록의 2D A/um 관행에 따른 원시 수치이며 조건 없이 면적 전류밀도나 IQE로 간주하지 않는다. 참고: 기존 1ns 5V_TEST 가까운 4.003369V에서 I2D=3.505521343e-14였고 CAL4V 4.000V와 약 0.2% 원시 전류 차이이나 서로 완전한 동일 바이어스 아님. 100ns의 재결합 개선 여부 미확정. NEXT 이미 확보한 final TDR의 4QW별 Radiative/SRH/Auger 적분과 비교전류 정상화 후 연구 판단; 별도 NtSide1e18 split은 실제 로그 미검증. 원본 데이터 보존.

## 2026-10-12 — CAL4V n2 confirmed normal SDevice termination and final outputs (OBSERVED)
- Screenshot supplied by current worker 이택규 of SWB Node 2 Explorer in `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/n2_des.out` confirms `Curve trace finished.`, `Plot(FilePrefix="n2_4V_final")` written to `n2_4V_final_des.tdr` successfully, `Save(FilePrefix="n2_4V_ckpt")` wrote `n2_4V_ckpt_des.sav` and circuit .sav, `n2_des.tdr` written, `Sentaurus Device simulation finished`, `Good Bye !`. Completed on Mon Oct 12 01:12:13 2026 (KST); wallclock 29706.72s (~8h15m6.72s), total CPU 84070.27s (~23h21m10.27s), peak memory 4.05 GB. Status **OBSERVED/CONFIRMED NORMAL SDEVICE FINISH and saved spatial final state**, replacing prior RUN-CLICKED-ONLY uncertainty for this CAL4V n2. Important: screenshot tail does NOT show numeric final anode V/current, nor `pp2_des.cmd` active physics/Goal/FinalTime, so numerical 4.000V endpoint and current/IQE are NOT YET EXTRACTED/INDEPENDENTLY VERIFIED. Prior source Goal=4.0, FinalTime=0.8, InGaN Scharfetter taumax 100ns were reviewed in previous conversation. Other reportedly completed NtSide=1e18 split not yet supported by its own log. Baseline physical Gate0 (low J, radiative fraction ~0.1095% old 5V) remains open. Protect saved results and existing 5V parent. Next: read-only last bias/current in n2_des.log or n2_des.plt, inspect n2_4V_final_des.tdr, extract 4 QW integrated radiative/SRH/Auger and compare matched V/J to old 1ns; independently inspect NtSide1e18 node output.

## 2026-10-12 — 이택규 reports both JuSubin runs finished (USER-REPORTED; no endpoint logs yet)
- 이택규가 2026-10-12 대화에서 주수빈이 전날 실행해 두고 간 '두 개' 시뮬레이션이 모두 끝났다고 보고. 직전 인수인계상 대상은 (1) 기존 `JUSUBIN_FAST_HALF_5V_TEST` 기반 NtSide=1e18 split과 (2) `CMP_BASELINE_1.3.0_CAL4V` (100ns, 0→4V)로 추정되며 **어느 두 SWB node인지 실제 로그나 화면으로 확인하기 전까지 프로젝트/노드 매칭 미검증**. 사용자 보고는 완료 주장의 근거이나 actual SDevice `Good Bye`/final V/timestep/terminal current/PLT/TDR/SAV는 미제공. NtSide=1e18 case가 NtSide-only matched input인지도 재확인 필요. 새 런이나 baseline freeze를 의미하지 않음. 기존 5V_TEST NtSide0 및 5V CAL 보호. 다음: 두 SWB 노드 이름, `n*_des.log` 마지막 35~50행, `pp*_des.cmd` Goal/Trap, 생성 PLT/TDR/SAV 확인→주입 전류 및 4QW Rrad/SRH/Auger를 동일 바이어스/전류 조건에서 비교. Gate0 낮은 J, 물리적 IQE/Full-Half 검증은 계속 미해결.

## 2026-10-11 — CAL4V Run clicked (USER-REPORTED, actual solver status pending)
- 주수빈 confirmed cloned CAL4V source `FinalTime=0.8` and clicked SWB **Run** for `CMP_BASELINE_1.3.0_CAL4V`. Previous actual screenshot independently showed `Goal anode Voltage=4.0`, final Plot `n@node@_4V_final`, Save `n@node@_4V_ckpt`, cloned custom InGaN Scharfetter electron/hole `taumax=1e-7s`. Keeps 5V/s ramp.
- Status **RUN REQUESTED by researcher**, not yet independently OBSERVED SDevice process/preprocessed deck/accepted BE-step and certainly NOT completion. Current 4V TDR/SAV absent/unconfirmed. Do not interrupt running original 5V CAL or preserve-solved 5V_TEST parent. NtSide1e18 split run still unverified.
- NEXT read-only in new CAL4V folder: `ls -lt n*_des.log n*_des.err n*_des.out 2>/dev/null | head -n 12`, then actual nN_des.log tail, preprocessed ppN Goal/FinalTime/Plot/Save/Parameter. Check SWB SDevice node state. Initial failure/syntax errors before overnight run are high priority; do not claim CAL4V will finish today. Physical low-J Gate0 persists.

## 2026-10-11 — JuSubin CAL4V code edit observed
- User screenshot confirms new clone sdevice_des.cmd Goal anode Voltage4.0, preserved time-step math and final Plot n@node@_4V_final plus Save n@node@_4V_ckpt after Transient. Custom FASTC1_pp6_des.par InGaN Scharfetter taumax1e-7 electron/hole also confirmed. FinalTime0.8 cropped off the screenshot and still needs grep verification. No mid-3.8V output; optional, not needed to delay 4V run.
- Next read-only FinalTime/source check; SWB CAL4V Preprocess only, verify pp command/par, then Run. Running original 5V CAL and older 5V_TEST untouched. Not physically frozen due low-J Gate0.

## 2026-10-11 17:39 KST — CAL4V clone still 5V code; safe shell edits instructed (OBSERVED / NOT YET APPLIED)
- Screenshot read-only grep from new `CMP_BASELINE_1.3.0_CAL4V/sdevice_des.cmd`: FinalTime1.0 line587, Voltage5.0 line597, `n@node@_5V_ckpt` line608; no 4V or 3.8V output. Earlier heredoc script did not modify this file; SWB SDevice not run.
- Worker instructed short separate commands only within clone: `cd`, `cp -pn sdevice_des.cmd sdevice_des.cmd.bak_5V`, GNU `sed -i -E` change FinalTime1→0.8 and Goal Voltage5→4, save prefix5→4, and second `sed -i` insert a final `Plot(FilePrefix="n@node@_4V_final")` before the Save. This retains 5V/s ramp. Existing completed 5V_TEST and separately active 5V CAL must stay untouched.
- AFTER EDIT: use read-only `tail -n 40 sdevice_des.cmd` and custom InGaN Scharfetter `taumax` par check; consider separate 3.8V intermediate Plot/Save once actual modified source shown, not yet inserted by commands. SWB Preprocess validate effective Goal/FTime/Plot/Save/par, then RUN only after evidence. Not a validated physical baseline; low-J gate pending.

## 2026-10-11 17:20 KST — JuSubin CAL 4V source patch prepared (NOT RUN)
- Original source Solve confirmed 5V Goal, FinalTime1s, Save after Transient. Separate clone only: 4V Goal, FinalTime0.8s, 3.8V intermediate and 4V end Plot/Save; 100ns custom parameter unchanged. Await SWB clone/preprocess/run proof. Original live 5V CAL untouched.

## 2026-10-11 — JuSubin requests new 4V CAL run; code drafted, not yet executed
- Parallel jobs planned: (1) 5V_TEST NtSide=1e18 split using 1ns physical parent; (2) **separately cloned** 100ns CAL at 4V. Do NOT change running original 5V CAL or 5V_TEST parent. User did not ask to abort either run.
- Proposed clone project `CMP_BASELINE_1.3.0_CAL4V` (first verify name is unused on remote server). In cloned `sdevice_des.cmd` ONLY: keep existing transient physics/math, set `Goal{Name="anode" Voltage=4.0}` and `FinalTime=0.8` together to preserve original 5V/sec sweep, add post-transient `Plot(FilePrefix="n@node@_4V_final")` and `Save(FilePrefix="n@node@_4V_ckpt")`. Preserve existing InGaN Scharfetter `taumax=1e-7s` custom par and 2D geometry. Do not edit generated pp2_des.cmd.
- CAL live full Solve excerpt still required before copy-ready exact source; previously exposed grep confirms FinalTime1, post-Transient Save, but did not show `Goal`. Next READ-ONLY on source/pp: `sed -n '580,612p' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/pp2_des.cmd` and original `sdevice_des.cmd` Solve tail; verify original ramp. After making clone edit in SWB, PREPROCESS only and check exact new pp/outputs/custom 100ns before long RUN; confirm log + 4V TDR on completion. Low-J physical Gate0 still outstanding; no guarantee 4V completes today.
- No local server source edit or job start verified by AI. Original CAL last directly accepted ~4.179V.

## 2026-10-11 — JuSubin DECISION: 5V_TEST parent NtSide0 → NtSide1e18 split now (RUN UNVERIFIED)
- Due to very slow 100ns CAL, researcher chooses prior completed `JUSUBIN_FAST_HALF_5V_TEST` NtSide0 5V as **working numerical comparison parent** and NtSide=1e18 SDevice split; this does NOT certify physical common baseline or indicate new run already launched. CAL ongoing/unchanged, parent 5V outputs must stay preserved.
- Sep26 trap-on Node12 fail involved stale/nonidentical source or parameter revision, so only clean same-input `ppN_des.cmd/par` NtSide-only comparison passes the pre-run gate. First preserve n2 5V logs/PLT/TDR, add NtSide=1e18 parameter case with original 0 case intact; preprocess before costly RUN; verify all damaged-region Conc, no other Physics/Math/Solve/custom .par change, intended 5V Goal and no stale cached 0-case. Run trap-on only after checks. No new server actions confirmed yet.
- Gate0 physical low J and 0.10947% QW radiative fraction not resolved; Project A/B paper-grade baseline still not frozen. NEXT screenshot SWB split tree or ppN_des.cmd to validate then run.

## 2026-10-11 — Prior low-J audit already performed by LeeTaekGyu (HANDOFF CORRECTION)
- User JuSubin correctly pointed out historical sequence: Oct9 parent 5V_TEST 4QW regional Rrad/SRH/Auger integrals and actual InGaN.par Scharfetter 1ns maximum lifetime were inspected by LeeTaekGyu; excessive SRH from overly short lifetime became a **hypothesis**.
- Oct10 clone CAL custom .par **actually updated** to InGaN Scharfetter taumax=1e-7s (100ns both carriers) and saved on server (confirmed by tail; change should not be repeatedly questioned as though never made). Same geometry and numerics parent remained a numerical reference. 100ns max is not uniform effective lifetime or proof it fixes terminal low-J.
- At approx 4.0V, prior 5V_TEST I2D 3.505521343e-14 A/um at 4.003369V and CAL I2D 3.497895e-14 A/um at 3.999674V (~0.22% raw difference at slightly different bias), no observed improvement in electrical current at that comparison point. No CAL ~4V spatial QW IQE TDR yet; 5V CAL incomplete.
- Stop proposing to redo the **already completed** prior baseline SRH / MaterialDB investigation. Next question is whether 100ns affects recombination/IQE at matched injection, while isolating distinct carrier transport/current density normalization concern (Gate0). Preserve CAL and finished parent, no code/job action.

## 2026-10-11 — 주수빈 baseline strategy: preserve successful 5V_TEST as working reference (PROPOSED, NOT FROZEN)
- `JUSUBIN_FAST_HALF_5V_TEST` NtSide=0 completed 5V SDevice Oct9 14:29:52 KST; serves as a **numerical working/solver baseline candidate**, not validated/frozen Common Baseline.
- Physical Gate0 persists: 5V I2D~1.448e-11 A/um, conditional J~7.24e-4 A/cm2 under 2um half-width, low all-QW radiative share~0.1095% (not validated IQE); current normalization, operating J, QW recombination/transport and effective τ must be audited. NtSide1e18 and Half vs Full equivalence unverified.
- Do not wait idly for CAL 100ns result to analyze archived completed data. Preserve 5V_TEST and active CAL, no unauthorized Stop/Abort or edits. Next read-only I-V/current-component/geometry/TDR and material audit; new versioned calibration/pilot only once causal hypothesis and user approval established. A/B publication production stays NO-GO until Gate0 cleared.

## 2026-10-11 — 주수빈 4V diagnostic cutoff requested (PROPOSED, not adopted)
- User worries 100ns CAL 5V ramp costs too much time; asks whether 4V endpoint is acceptable and why 5V was originally chosen. GitHub `COMMON_BASELINE.md` documents initial forward sweep 0→5V but does not identify 5V as a mandatory physical turn-on or operating voltage.
- 4V can bound a **separate diagnostic pilot**, but 4V alone cannot validate the baseline while 5V_TEST low-J Gate0 remains unresolved. Current CAL PLT near 4V raw I2D 3.497895e-14 A/um (conditional J ~1.75e-6 A/cm² for 2um width, 2D normalization and displacement not validated). Existing nominal 5V_TEST J ~7.24e-4 A/cm² is already low under documented convention.
- Old 0→5V reference and running CAL protected; current CAL already accepted ~4.179V and post-transient `Save` cannot retrospectively yield a 4V TDR. Any new shortened run needs versioned copy, maintained comparison conditions, explicit 4V spatial `Plot/Save` and controlled validation. No server edits.
- NEXT read-only `sed -n '580,612p' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL/pp2_des.cmd` for goal/ramp; check effective 100ns par before claiming calibration, discuss user decision about new 4V pilot vs running CAL. NOT confirmed baseline freeze.

## 2026-10-11 ~16:46 KST — JuSubin CAL Plot/Save checkpoint review (OBSERVED)
- Actual screenshot of `CMP_BASELINE_1.2.0_CAL/pp2_des.cmd`: File Plot `n2_des.tdr`, Current `n2_des.plt`, Output `n2_des.log`; Parameters `FASTC1_pp6_des.par`. `Plot{...}` field list is not bias-time output. Transient from 0 to FinalTime 1.0, MaxStep 1e-3, MinStep 1e-9; `Save(FilePrefix="n2_5V_ckpt")` is **after** Transient closes. No in-transient Plot(Time=...) or Save(Time=...) in the matching grep output, so no confirmed ~4V spatial checkpoint despite available I-V PLT. Existing top-level TDR/SAV absent in prior inventory; deeper/alternate paths still unverified.
- `0->0.3V smoke` source comment likely stale compared to observed accepted 4.179V; inspect full `sed -n '580,612p' .../pp2_des.cmd` to see actual Goal. Verify 100ns lifetime override in active parameter file later; do not interpret file name alone as calibration proof.
- Preserve active CAL, don't abort while data retention uncertain; low-J Gate0 and 5V CAL completion unresolved. No server model/process edits.

## 2026-10-11 ~16:45 KST — JuSubin CAL node2 input file found (OBSERVED)
- CAL directory read-only listing confirmed `FASTC1_pp6_des.cmd`, `pp2_des.cmd`, and `sdevice_des.cmd`; node2 preprocessed `pp2_des.cmd` exists. Plot/Save contents not yet inspected; 4V spatial TDR still unverified.
- Previous accepted CAL 100ns ~4.179V unchanged by current screenshot; 5V ETA unknown; low-current Gate0 unresolved. Next read-only grep Plot/Save in `pp2_des.cmd`. No TCAD source/job changes.

## 2026-10-11 ~16:41 KST — JuSubin 100ns CAL accepted ~4.179V (OBSERVED screenshot)
- Actual `CMP_BASELINE_1.2.0_CAL/n2_des.out` screenshot: accepted BE 0.835804→0.835806s (`RHS=7.30e-04<1e-3`), anode voltage ~4.179V, total terminal current 5.555e-14 A/um in the documented 2D convention. About **83.58% of the 0→5V voltage sweep**, not compute time; prior Oct10 saved ~4.14965V -> +~0.029V.
- Next BE 0.835806→0.835808s trial Newton RHS ~1.03e-3–1.09e-3 (iterations 2-6), still above 1e-3; later acceptance/failure not in screenshot. 5V completion/ETA **UNRESOLVED**, no observed fatal termination.
- Gate0 remains **LOW-J UNRESOLVED**; 4V spatial TDR/Save currently not confirmed. Do NOT Stop/Abort CAL solely from terminal voltage. Next READ-ONLY inspect later n2_des.log/out, actual Plot/Save directives, and any alternate saved TDR paths; no SWB or simulation change.

## 2026-10-10 ~22:38 KST — JuSubin CAL 100ns folder n2* inventory read-only
- OBSERVED screenshot: top-level `CMP_BASELINE_1.2.0_CAL` n2-prefixed files only `n2_des.err` (12KB), `.job` (4KB), `.log` (5120KB), `.out` (5376KB), `.plt` (1416KB), `.sta` (4KB), `n2_local.err` (0KB). No `n2*.tdr` or `n2*.sav` at this level. This does NOT exclude snapshots in subdirectories/differently named paths.
- Existing near-4V transient `n2_des.plt` point V=3.99967374V, I=3.497895e-14 A/um is preserved, but 4V spatial state/QW recombination for IQE is NOT confirmed. Do not stop/abort CAL (may not preserve ~4V TDR). NEXT read-only inspect actual SDevice `Plot`/`Save` directives via `n2_des.cmd` or `pp2_des.cmd` and alternate output locations. Low-current Gate0 still active. No TCAD job/source changes.

## 2026-10-10 22:30 KST — JuSubin extracts real 100ns CAL 4V I–V record
- OBSERVED read-only parsing of live `CMP_BASELINE_1.2.0_CAL/n2_des.plt`: near-4V saved record time=0.79993475s, anode=3.99967374V, 2D TotalCurrent=3.497895e-14 A/um. Last PLT row in screenshot time=0.82993089s, anode=4.14965446V, TotalCurrent=4.839436e-14 A/um. Values directly displayed, not estimated. LAST PLT ROW does not prove currently running solver is still at the same point; no 5V completion.
- 4V transient current history obtainable without changing running CAL. But 4V point is low-current, not an established LED baseline or sufficient IQE test; verify displacement current / geometry normalisation and region-specific 4V TDR / save checkpoints before changing endpoint. Low-J Gate0 remains UNRESOLVED. 
- NEXT read-only `find` saved n2*.tdr/n2*.sav and inspect Plot/Save coverage. No TCAD code/process/source/CAL change.

## 2026-10-10 22:25 KST — CAL PLT data schema verified; 4V value not extracted yet
- OBSERVED read-only screenshot from JuSubin on `CMP_BASELINE_1.2.0_CAL/n2_des.plt`: `DF-ISE text`, `type=xyplot`, 17 stored datasets: time, 8 cathode fields, 8 anode fields including `anode OuterVoltage`, `anode TotalCurrent`, `anode DisplacementCurrent`. Numeric `Data {` present. Enables retrospective 4V I–V retrieval without stopping calculation, but the displayed first 30 lines alone do NOT verify an actual 4V datapoint nor TDR at 4V. Next read-only parse numerical rows; keep CAL running and Gate0 unresolved.

## 2026-10-10 22:21 KST — JuSubin confirms live CAL PLT exists (OBSERVED)
- Separate `CMP_BASELINE_1.2.0_CAL/n2_des.plt` confirmed by `ls -lh` at ~22:21 KST: 1.4M, mtime Oct10 21:30. The reported missing file was typo `n2_des.pltls`; correct file is present. Still no direct confirmation of 4V current data contents or 4V TDR snapshot/checkpoint. The last *accepted* CAL voltage in documented 22:11 log remains ~4.149V; mtime alone does not prove progress. Keep CAL running; next read-only `head -n 30 .../n2_des.plt` and check Save/Plot config. No SWB/TCAD files edited.

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

## 2026-10-10 — JuSubin independently confirms original 5V_TEST n2 finished log
- OBSERVED user-provided grep/tail of existing `JUSUBIN_FAST_HALF_5V_TEST/n2_des.log`: final BE step to t=1.0s, anode=5.000V, 2D total current=1.448e-11 A/um, `Sentaurus Device simulation finished` + `Good Bye!` on Oct 9 14:29:52 KST. Repeat screenshots are same observation. This confirms last accepted solver state reached 5V; still verify `n2_des.tdr` time/bias provenance if interpreting visualized point data as final 5V.
- Existing baseline low-J Gate0 remains blocker, J nominal ~7.24e-4 A/cm². `n1_msh.tdr: Permission denied` was attempted execution of data file, not TCAD crash. NEXT use existing data to diagnose low injected current without touching separate CAL or Baseline.

## 2026-10-10 — JuSubin pGaN vs EBL Ev/EFp probe
- OBSERVED same existing 5V_TEST n2_des SVisual: Clean_pGaN X=0.05,Y=1um Ev=-5.130097037559eV, EFp=-4.999999973858eV -> local 0.130097063701eV. Prior Clean_EBL X=0.13,Y=1um Ev=-5.252508407140eV, EFp=-4.999999939039eV -> 0.252508468101eV. Delta 0.1224114044eV. These are local energy separations NOT cross-interface barrier. Need confirm actual 5.0V recorded endpoint: an earlier n2_des.log screenshot showed anode 4.139V mid-ramp. Read-only check first. No TCAD/CAL changes.

## 2026-10-10 — EBL same-point energy difference
- OBSERVED (주수빈) 5V_TEST completed NtSide0 Clean_EBL at X=0.13um,Y=1.0um: Ev=-5.252508407140eV, EFp=-4.999999939039eV; EFp-Ev=0.252508468101eV. Previous hDensity=5.7879e15, acceptor=3e17, signed net doping=-3e17 cm^-3. Local EFp-Ev difference is not injection barrier height. Next read pGaN same-position values and compare regions. No code or CAL changes.

## 2026-10-10 21:43 KST — JuSubin upper-stack hole quasi-Fermi cutline now zoomed (OBSERVED)
- Completed NtSide0 5V n2_des: C1(Y≈1um) `hQuasiFermiEnergy` graph is displayed over X=0–0.4um. Plateau near -5eV in top segment and several marked steps X≈0.15–0.25um; approximate screenshot reading only, not energy barrier measurement. Previous Ev cutline also showed strong upper-stack structure. EBL low biased free-hole density cause remains unresolved.
- NEXT read-only: same-coordinate Probe Clean_EBL X=0.13um,Y=1.0um for Ev and hole quasi-Fermi, then layer-aligned band/transport check. Gate0 low-current and CAL prior status unchanged.

## 2026-10-10 21:29 KST — JuSubin Clean_EBL doping input correct; 5V holes remain low (OBSERVED)

- Completed `JUSUBIN_FAST_HALF_5V_TEST` NtSide0 5V SVisual Probe at X=0.13 µm/Y=1.0 µm (Clean_EBL, AlGaN): `AcceptorConcentration=3.000000e17`, `DonorConcentration=0`, `DopingConcentration=-3.000000e17`, `hDensity=5.787900714824e15 cm^-3`. Input effective acceptor and signed net doping agree; one-point free holes ~52 times smaller than acceptor under 5V. Potential hole-injection barrier/depletion/polarization cause NOT CONFIRMED.
- Next JuSubin step: use existing 5V TDR to inspect vertical `ValenceBandEnergy` and `hQuasiFermiEnergy` cutline around pGaN/EBL/MQW, without editing/rerunning. Separate MgMinus field semantics remain unresolved. Other team's low-J Gate0 and CAL watch remain ongoing/unmodified.

## 2026-10-10 — Claude v2 independent CMP audit submitted; low-current Gate 0 prioritized (DOCUMENT-BASED REVIEW / PROPOSED)

- 작업자 이택규가 Claude 작성 `CMP MicroLED TCAD — 독립 중간 기술감사 및 연구계획 재수립 (v2)` 전문을 채팅 업로드함. **Claude의 독립 감사 의견이며 이번 메시지는 새 실험/로그가 아님.** Claude는 GitHub 기록과 구 FAST 입력은 보았으나 5V_TEST/CAL 현재 실제 pp/log/TDR을 직접 읽지 못했다고 보고함.
- Claude의 핵심 의견: JUSUBIN_FAST_HALF_5V_TEST NtSide0 5V transient 성공(~10596.76s)에도 raw I2D=1.44801646e-11 A/um, half mesa width≈2um, assumed AreaFactor1이면 nominal J≈7.24e-4 A/cm²; QW Rrad share≈0.1095%. 충분한 구동 전류·주입·IQE 검증이 **Baseline freeze 이전 Gate 0**이 되어야 함. 수치는 기존 GitHub 감사 기반이며 새 측정 아님. `not turned on` 결론은 비교대상 J–V/전류 정규화 검증 전에는 물리 가설로 남김.
- 수용 가능한 점: 5V_TEST 계산 플랫폼 보존, high-bias FAST_C1 n6 ~4.801V step-size failure는 재실행 보류, CAL n2 100ns sensitivity current reported ~4.144V accepted unverified로 관찰·중단 사용자 승인 필수; A/B 동일 J·null controls, τ sensitivity, QW와 Cedge 총 비방사, transient trap DC check, stripe vs 3D 형상 한계 분리.
- 별도 검증 필수: Claude가 제시한 활성층 외 `2.9V drop`은 단일 QW n,p, ni 가정 기반 추정이지 밴드/준페르미 지도에서 측정된 전압 분배 아님. 분극 activation/thermionic/EBL를 저전류 확정 원인으로 판단 금지. FAST half/full ~1% 동일은 4.798 vs 4.801V 단일 단자전류의 근사 보정이므로 메쉬 수렴·공간발광 정확도는 미증명. 2D stripe perimeter/area가 4um square보다 2배 작은 기하학적 사실에서 실제 SRH 2배 과소평가를 단정할 수 없음. 1D pilot 분 단위/10월23일 초록 데드라인/수치 PASS 기준은 Claude의 제안이며 별도 확인 필요.
- 우선순위 제안: **S0 원본 5V_TEST 결과의 구동 전류/J 및 potential/band/quasi-Fermi 분포 점검(기존 TDR)** → **S1 EBL doping/polarization/thermionic interpretation 및 재결합 영역별 전류 회계** → 원인 가설이 분리되면 기존 소자 보존한 별도 소형 1D/pilot 설정 검토(사용자 승인 전 미실행) → NtSide0/1e18 동일 J → A/B. CAL은 보고서의 임의 시간·전압 임계치만으로 중단 결정하지 않음.
- 서버/SWB/코드/CAL 변화 없음. Claude에게 직접 메시지 보내지 않음.

## 2026-10-10 — CAL n2 ~4.144 V calculating (USER-REPORTED / ACCEPTANCE UNVERIFIED)

- 작업자 이택규 직접 보고: `CMP_BASELINE_1.2.0_CAL`이 현재 약 **4.144 V 계산 중**. 직전 실제 공유 n2 로그에서 확인된 accepted 전압은 4.142 V; 이번 보고는 이전보다 약 0.002 V 높은 시도/진행으로 보이지만 **새 n2_des.log 스텝 수렴 결과는 제출되지 않아 4.144 V accepted라고 확정할 수 없음**. 5V/100ns effective 적용 모두 미확인.
- 시간당 속도, 최종 종료 예상, 근본적인 고전압 수렴 문제의 동일성은 아직 판단 불가. 현재/목표 전압 비율은 ≈82.88% *스윕 구간*일 뿐 시간 진행률 아님.
- NEXT: 기존 CAL 작업 그대로 보존, 현재/이후 `n2_des.log`의 accepted t/V, Newton 컷백, timestep, 최소 간격 경고 비교하는 읽기 전용 감시. CAL 임의 Abort·Reset·파라미터 수정하지 않음. 최근 FAST_C1 4.801 V MinStep 실패는 별도 사례.

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

## 2026-10-10 ~19:02 KST — FAST_C1 NtSide0 n6 red failed UI; CAL 5V unverified (OBSERVED / UNRESOLVED)

- 이택규 SWB 캡처 선택 프로젝트 `GaN_PiN_Diode_FAST_C1`: `NtSide=0` SDevice n6 red (SWB default failed), n12 pale blue (default running), n1 yellow (default done). No n6 stderr/log or failure mechanism shown; cannot conflate this with another FAST test or CAL.
- `CMP_BASELINE_1.2.0_CAL` is listed but not selected; worker reports no finish. Latest actual CAL n2 evidence from 주수빈 at ~18:08 KST: ~4.138 V, Newton max iterations / timestep cutback. 5V, 100ns physical effect, CAL walltime ETA unresolved.
- NEXT READ ONLY: review `GaN_PiN_Diode_FAST_C1/n6_des.log` (+err/sta if needed), and `CMP_BASELINE_1.2.0_CAL/n2_des.log`; preserve jobs, no rerun/reset/edit until diagnosis. Existing JUSUBIN_FAST_HALF_5V_TEST 5V done result remains separate.

## 2026-10-10 ~18:07 KST — JuSubin screenshot CAL n2 progressed to ~4.138 V (OBSERVED / NOT FINISHED)

- 주수빈 SWB screen for `CMP_BASELINE_1.2.0_CAL/n2_des.out`: previous BE step shows `Finished, because |RHS| less than 1.0000E-03`, then contact anode `4.138E+00 V`. The next attempt `0.82766→0.827663 s` begins but acceptance is not shown. Prior observed 4.122 V is superseded as latest confirmed voltage.
- For an unchanged 0→5 V ramp, ≈82.76% of **voltage range** reached, NOT 82.76% of total runtime. 5 V finish and InGaN Scharfetter 100ns effective application NOT established. Visible vanOverstraetendeMan E0 isotropic/anisotropic mismatch output is a warning, not a confirmed fatal cause.
- Preserve the user's ongoing job and prior completed 5V reference. NEXT READ ONLY: compare future n2_des.log accepted t/V, cutbacks, Good Bye; inspect effective CAL .par only without editing. Worker 주수빈 observed/handed over 이택규's job; did not start or modify solver.

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

## 2026-10-10 — CAL SDevice user says Run pressed (REPORTED / NOT YET VERIFIED)

- 이택규 reports SWB SDEVICE Run launched for separate `CMP_BASELINE_1.2.0_CAL` NtSide0; original parent 5V run ~2h56m36s, but new InGaN SRH Scharfetter tau_max=100ns trial may change convergence and time. No live solver log or job PID from this new run reviewed yet, so cannot assert active computation, actual 100ns applied or finish. Next: request new project's actual `n2_des.log` tail and SWB node running/failed status, then diagnose/monitor and extract 5V I(V), QW SRH/radiative/Auger. Scientifically CAL remains a parameter sensitivity trial, not physical final baseline.

## 2026-10-10 — CAL 1.2.0 InGaN 100ns .par edit observed on server; preprocess NOT done

- 이택규 live `tail` confirms `CMP_BASELINE_1.2.0_CAL/FASTC1_pp6_des.par` now includes material-specific InGaN Scharfetter `taumax=1e-7,1e-7 s` plus other vendor default fields. This resolves the prior missing-override file-edit gate only.
- Input provenance: SDE/SDevice remain cloned from successful NtSide0 5V parent (previous SHA256 match). The SDevice source explicitly points to custom `FASTC1_pp6_des.par`, not auto-generated `sdevice.par`. No cloned SDE mesh, SDevice preprocess, or CAL numerical run has been verified.
- NEXT: read-only verify parameter path in cloned SDevice source; SWB preprocess and inspect model parse/effective 100ns override; build separate true short Transient BE smoke before 5V candidate. Preserve original 5V parent.

## 2026-10-10 — CAL clone source parity confirmed (OBSERVED)

- User checked three SHA256 hashes in new CMP_BASELINE_1.2.0_CAL. Each exactly matches independently audited successful 5V_TEST parent: SDE, SDevice, custom .par.
- New project has not received 100ns InGaN SRH candidate yet, and has not been preprocessed/run.
- Next: transfer private ZIP from chat via SFTP and verify it on server; then safely install only new .par in clone, preprocess, short transient smoke.

## 2026-10-10 — CMP_BASELINE_1.2.0_CAL new SWB project visible (OBSERVED)

- 이택규 SWB screenshot shows project `CMP_BASELINE_1.2.0_CAL` exists under `/user/semi/semi437/tmp/myproject/`, SDE→SDEVICE topology and one `NtSide=0` experiment. Both tool result cells are `--`, so no successful preprocess, mesh or SDevice runs evidenced. Completed parent JUSUBIN_FAST_HALF_5V_TEST remains listed.
- Next read-only verify new project's sde_dvs.cmd, sdevice_des.cmd and FASTC1_pp6_des.par exist; then apply private 100ns candidate files ONLY to the clone, inspect correct parameter path and conduct preprocess + truly short Transient smoke. No run started in this screenshot.

## 2026-10-10 — CMP_BASELINE_1.2.0_CAL input package prepared locally, not yet executed (PROPOSED / STATIC PASS)

- Worker 이택규 supplied live T-2022.03 MaterialDB/InGaN.par 855–925: explicit GaAs-origin warning, Scharfetter taumin=0/taumax=1e-9 both electrons/holes, Nref=1e16, gamma=1, Auger A=1e-30, Radiative C=2e-10. Consistent with private completed 5V TDR audit.
- AI locally created **private** downloadable `CMP_BASELINE_1.2.0_CAL_INPUT_CANDIDATE.zip` containing unchanged parent `sde_dvs.cmd`, only-comment-corrected parent `sdevice_des.cmd`, appended `Material="InGaN" { Scharfetter { taumin=0; taumax=1e-7 electron/hole; Nref=1e16; gamma=1; ... }}` custom `FASTC1_pp6_des.par` preserving lattice, thermionic, GaN Mg, and README. SDevice executable lines identical. ZIP verification PASS. Private candidate .par SHA256 adfe81ab03b8f0ca84b09b9a4373fdc8e71f7a5faa00ce01a7c0b82b7fb2f1ad. No new solver run or SWB preprocessing/clone yet.
- Material Scharfetter override syntax supported by Sentaurus training, but effectiveness with user's local T-2022.03 is UNTESTED. Do not write vendor MaterialDB or original parent; next recommended SWB `Project > Save As > Clean Project` into CMP_BASELINE_1.2.0_CAL, then copy candidate sources in cloned project only, preprocess, and create truly SHORT Transient-BE smoke by changing sweep Goal to <=0.3V in a second experimental copy; the distributed sdevice_des.cmd is a FULL 5V source, NOT a smoke.
- 100ns is literature-motivated sensitivity, not measured GaN/InGaN lifetime. Publication full/half, J normalization and injection gates remain open.

## 2026-10-10 — 5V parent code/HDF5 audit results (OBSERVED/DERIVED), CAL 1.2.0 NOT RUN

- Worker 이택규 uploaded 9-file private archive; independent source/log/PLT/HDF5 review documented in `CMP/reviews/BASELINE_1_2_0_CAL_AUDIT_20261010.md`. 5V Transient finished normally (~2h56m36s), mesh 65513 vertices. Actual Solve was single 0–5 V Increment1.2, Save only at 5V; contrary to source comments about staged 1.05 and intermediate saves.
- **Resolved computational Mg model check:** -DopingConcentration = MgActive*TrapOccupation_Mg per point across Clean/Dmg pGaN, max Mg occupancy ~3.1286% corresponding ~3.00033e17 effective acceptor. MgMinus raw-looking plot field should not be used alone to infer 100% ionization. This is numerical consistency, not physical calibration.
- **New decisive recombination finding:** all 8 Clean/Dmg InGaN QW regions of n2_des.tdr obey Rrad/(np)=2e-10, RAuger/[np(n+p)]=1e-30, RSRH(n+p)/(np)=1e9/s (effective tau=1ns). The uncalibrated recombination physics is ACTIVE in actual solved result, not just parsed; four-well radiation fraction 0.10947% modeled only.
- 5V anode I=1.44801646079583e-11 raw 2D current, provisional J≈7.24e-4 A/cm2 under A/um & 2um width (needs local manual validation); transient steady state/full-half not proven. CAL 1.2.0 still only PROPOSED, no source edit or simulation.
- NEXT: local InGaN.par exact Scharfetter/param override review -> distinct 1ns vs proposed literature 100ns sensitivity without other physics change -> short Transient smoke -> NtSide0/1e18 5V comparisons, same-current and mesh/Full gates. A/B production NO-GO.

## 2026-10-09 — CMP naming confirmed, next candidate CMP_BASELINE_1.2.0_CAL (DECISION / PROPOSED RUN)

- User confirmed naming standard `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>`, canonical policy `CMP/PROJECT_NAMING_CONVENTION.md`, replacing preliminary name `CMP_BASELINE_CAL_V1`. Version histories are independent per family; `CAL` denotes intended calibration scope, not completed validation.
- In live `JUSUBIN_FAST_HALF_5V_TEST`, user `ls -lh` confirmed presence of 9 private source/input/mesh/log/TDR/PLT files needed to inspect the completed 5V NtSide0 run, but original contents were not uploaded to this chat. No new project or simulation launched.
- Next: private input archive → active physics/material/current review → separated parameter-only pilot → short Transient BE smoke → NtSide0/1e18 5 V comparison; keep Full/Half+mesh equivalence and scientific calibration gates before baseline freeze.

## 2026-10-09 — 이택규 CMP_BASELINE_CAL_V1 preparation chosen (PROPOSED; NOT RUN)

- Keep 12 MB pre5V tar.gz backup in place per user decision. Preserve completed JUSUBIN_FAST_HALF_5V_TEST NtSide0 5V transient result and original full/fine reference.
- New private candidate proposed: CMP_BASELINE_CAL_V1, building from verified Half+Coarse 5V reference with 4 InGaN QWs, 5nm physical sidewall damage, protected Mg/EBL/nGaN doping, and known convergent Transient-BE. No SDE/SDevice edits or simulation launch yet.
- Critical gates: obtain exact private active SDE/SDevice/FASTC1 .par/pp-decks/mesh/log; verify applied InGaN SRH/Radiative/Auger and material mixing, provisional J/AreaFactor and injection before choosing evidence-backed parameter-only sensitivity updates; then NtSide0 pilot→5V, NtSide1e18 comparison. Full/Half/mesh convergence and matched-current quantities mandatory before final publication baseline/A/B production.
- Claude cannot be directly addressed in a separate chat through this session; questions recorded in CMP/.ai-sync/RELAY.md for later reader. Current team status remains A/B PRODUCTION NO-GO.

## 2026-10-08 — 주수빈 accelerated Half+coarse QS smoke deck prepared (PROPOSED)

- Half+coarse SDE mesh actually built successfully; 138,194 elements, 65,513 points.
- Current 0→0.3 V transient smoke is accepted but slow (~109.74s/step with ~90.20s linear solve).
- Private SWB SDevice alternative generated: `sdevice_des_JUSUBIN_HALF_COARSE_QS_SMOKE.cmd`, SHA256 `a7281c79e7e440c6192726f4ce6edefb58f8d76ed30ec921900fee5ff5a5ec01`.
- Steady QS anode 0→0.3 V; InitialStep=.03, MaxStep=.15, Increment=1.5, MinStep=1e-6, Decrement=2; original full device physics/traps and Math/ILS preserved.
- Static syntax/region checks PASS, actual QS preprocess/run NOT DONE. Original full FAST_C1 reference untouched.
- NEXT: user installs file in SWB after stopping only old Node2 smoke if desired; preprocess `pp2_des.cmd` and run QS 0.3V test.

## 2026-10-08 — cmp216 FAST_C1 test: apparent interruption, cause unresolved

- OBSERVED (user shell outputs): separate `cmp216@ssudisu2` run in `~/FAST_C1_ACCOUNT_TEST`. Last accepted Node6 0.9534 V; next BE-step logged header only. Log last modified Oct 7 17:47; PLT Oct 7 17:45; no `n*_des.tdr` found; no active `cmp216` SDevice process on checked host.
- `grep` search found license checkouts but no explicit fatal/killed/aborted/normal-completion marker.
- UNRESOLVED: why the run stopped producing output, including login/session termination or process failure. Cross-account performance effect beyond low bias unverified.
- NEXT: read-only process/session/job/launch history check; retain files and ongoing `semi437` references untouched.

## 2026-10-07 — Project A/B pre-run audit: Baseline parent OK; production A/B NO-GO until gates pass

- 작업자: 주수빈
- 상태: REVIEWED / PRE-RUN GATE
- FAST_C1/Common Baseline은 A/B parent로 유지 가능; physical baseline 재구축 필요 없음.
- same-current I-V + intermediate spatial TDR 기반은 유지되고 실제 FAST_C1 Node 6에서 intermediate TDR 생성 확인.
- broad multi-day A/B production은 아직 NO-GO.
- 필수 gate: active pp-deck audit, dataset/extraction test, J normalization, A Cedge geometry/mesh/physics/null control, B exact vertical span + AlBarrier geometry/mesh/null control, Save/Load smoke, representative A/B pilots.
- Project B가 QW edge를 AlGaN으로 치환하면 active QW volume이 달라질 수 있으므로 total recombination뿐 아니라 QW-volume normalization 및 injection/leakage metric을 함께 사용.
- 상세: `CMP/PROJECT_AB_PRE_RUN_AUDIT.md`.

## 2026-10-06 — D6 complete; Save-based C2 smoke next

- 기존 C1 `Plot(-Loadable)` intermediate는 restart state 정보가 없어 current Node 6 restart에 사용 불가.
- Option 3 폐기, Option 2만 유지.
- Node 6/12 reference run 계속.
- 다음: revised C2 smoke에서 `Save` checkpoint를 생성하고, 그 Save 파일에 대한 `Load` check 수행.
- 첫 common C2 정책: Iterations=15 유지, Increment=1.05 시험.

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

## 2026-10-06 — D2 complete: cap 8/10 not safe for common C2

- Node 6 accepted max Newton=4; cap 8 false_rej=0.
- Node 12 accepted max Newton=15; accepted 13-iteration and 15-iteration steps exist.
- Node 12 cap 8/10 each predict 2 false rejections; first divergence ~4.195 V.
- Decision: first common C2 keeps Iterations=15; test Increment=1.05 first.
- Original cap-8 C2 deck is provenance only and must not be executed as-is.
- Next: inspect Node 12 >8 accepted exceptions, then D3 current normalization/J-window.

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

## 2026-10-06 — Runtime-first half + coarse-mesh candidate prioritized

- 작업자: 이택규
- 상태: DECISION / DEADLINE ACCELERATION
- 기존 FAST_C1 full Node 6/12는 reference로 유지.
- 새 accelerated branch는 half-domain + coarse remote/global bulk mesh를 동시에 적용하여 10/23 전 preliminary result 확보를 우선.
- active physics/critical mesh는 유지: MQW, EBL, GaN/InGaN and GaN/AlGaN interfaces, 5 nm sidewall damage.
- first gate before long solve: SDE mesh build only -> element/point count + visual mesh sanity.
- half-domain current normalization: full-device total current 비교 시 2×I_half 또는 current density 사용; IQE ratio 자체는 ×2 하지 않음.
- branch classification: preliminary/screening until full-reference equivalence/mesh-convergence is demonstrated.

## 2026-10-06 — Oct 23 abstract deadline: runtime-first triage

- 작업자: 이택규
- 상태: CRITICAL DEADLINE / DECISION
- 논문 초록 마감: 2026-10-23.
- primary blocker: FAST_C1 Node 6/12가 multi-day runtime을 요구하고 Node 6은 ~4.68 V 부근 high-bias timestep collapse가 관찰됨.
- current full-reference runs는 가능하면 유지하되, 이들의 완주를 기다리는 것을 critical path에서 제거.
- immediate parallel task: same physics/mesh의 numerical-only accelerated branch short benchmark.
- first methods to audit: Quasistationary DC sweep vs current Transient ramp, staged continuation, Save/Load/restart, bias segmentation, thread/output overhead.
- publication constraint: physics/trap/geometry를 runtime 때문에 완화하지 않으며 acceleration은 reference-equivalence validation을 통과해야 함.
- abstract strategy: 10/23 전 모든 sweep 완료가 아니라 defensible baseline + 최소 mechanism-relevant preliminary result를 확보.

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

# 2026-10-04 — FAST_C1 exact source install PASS

- exact C1 source SHA-256 f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93 confirmed in separate FAST_C1 project.
- golden backup preserved.
- next: inspect copied Workbench status metadata, then preprocess only.
- no SDevice solve yet; live x6/x7/x8 untouched.

---

# 2026-10-04 — B0 COMPLETE; FAST C1 ready for preprocess

- updated Stepsize-based x8 CSV verified all 285 retry/rejection pairs.
- retry_dt / rejected_dt: min 0.499975805, max 0.500023337, mean 0.499999621.
- cutback factor = 0.5 to log-print precision.
- B0 is closed.
- C1 unchanged: Iterations=15, source SHA-256 f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93.
- next: separate FAST C1 project/copy -> source hash -> preprocess gate -> NtSide=0 B1.
- live x6/x7/x8 untouched.

---

# 2026-10-04 — Claude B0 review: C1 unchanged, A1'/A1'' added

- C1 source unchanged: SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`; `Iterations=15`.
- correction: ~4.33 V is the first rejected attempt where Newton count changes 50->15, not a trajectory divergence.
- A1': accepted-step sequence + rejection points should match over the observed overlap; unexplained mismatch = UNEXPECTED.
- A1'': every C1 rejection must show `#iterations larger than 15.`; 50 means cap not applied -> stop.
- A3/A4: printed-precision identity expected on observed overlap; 1e-3 / 1 mV are outer limits.
- new audit tool SHA-256 `9a935633e92bc55fa86849b6988b60a8a8ee55f637387ced62721d9f6267d281`; synthetic selftest passed.
- observed raw retry/rejected dt examples are ~0.5; full 285-event CSV ratio verification remains pending because the CSV was not included in the review package.
- patch-equivalent commit: `ace056fcb01d2e6e785dbee08a213e1148d6be35`.
- next: separate FAST C1 preprocess gate, then NtSide=0 B1 benchmark; live x6/x7/x8 untouched.

---

# 2026-10-04 — B0 PASS for C1 Iterations=15

- 1950 accepted x8 attempts, accepted max Newton=4.
- 285 rejected attempts, all 50 iterations.
- N=15 false_rej=0 through observed x8 progress (~4.643 V).
- rejected attempt wallclock fraction ~75%; idealized observed-path speedup estimate ~2.11x.
- next: separate FAST C1 preprocess gate -> NtSide=0 benchmark.
- live x6/x7/x8 untouched.

---

# 2026-10-04 — B0 parser patched for actual BE-step log format

- real T-2022.03 x8 step syntax identified and parser patched.
- next: re-download tool and rerun B0 audit; Iterations=15 remains unconfirmed until real accepted-step distribution is parsed.

---

# 2026-10-04 — B0-1 passed: no explicit transient Iterations in x8 pp6

- observed x8 pp6_des.cmd:
  - RHSMin=1e-3
  - CheckRhsAfterUpdate
  - Iterations=500 (initial Poisson)
  - Iterations=100 (equilibrium)
  - no transient Iterations
  - no NotDamped
- remaining blocker: interpret raw x8 n6_des.out and accepted/rejected Newton iteration distribution before confirming C1 Iterations=15.

---

# 2026-10-04 — FAST C1 reviewed; B0 audit required

- Claude C1 SHA: `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`
- golden Copy x8 SHA: `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`
- executable change: transient inner Coupled `Iterations=15` only
- C1 and prior ChatGPT v0.1 are executable-statement equivalent
- status: PROPOSED / REVIEWED / NOT EXECUTED
- blocker: B0 must resolve documented default 20 vs project-recorded ~50-iteration failures and verify no accepted x8 step needs >15
- Claude tools are synthetic-tested only; actual x8 format validation pending
- live x6/x7/x8 remain untouched
- guide: `CMP/FAST_BASELINE_C1.md`

---

# 2026-10-04 sequence correction — FAST coding starts now

Copy x8 golden reference has been frozen. The next task is to build a separate numerical-only FAST_BASELINE and benchmark the first solver change against Copy x8.

Clean-account reproduction remains mandatory before final FAST baseline freeze / Project A-B production, but it is not a blocker for writing and short-benchmarking the FAST code.

Priority:
1. obtain/use exact Copy x8 editable source
2. create separate FAST_BASELINE
3. first candidate = Newton iteration/cutback policy only
4. short benchmark against Copy x8
5. accept/reject by runtime + physical/numerical equivalence
6. reproduce the accepted FAST deck on both accounts before production

---

# 2026-10-04 Copy x8 golden reference frozen

Golden local snapshot completed and core hashes fixed.

- n1_msh.tdr: 762d2d57a352a00bb030b968985cbf3b71d53118c68e5c53b7586e613f392ea3
- pp1_dvs.cmd: 5685528bc3ec338ce104040b0503be43ef032094976d69995529eb5d6fb4e658
- pp6_des.cmd: 2dfcc98effe145ec944fb8ee5d6914f5f098e54d1bf2319c69acc76afe1692e6
- pp6_des.par: 60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039
- sd_fdiv_des.cmd: 56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c

Immediate next task: reproduce preprocessing in Lee Taek Gyu clean account before any full FAST solve.

---

# 2026-10-04 FAST baseline handoff

**Current task:** freeze Copy x8 as the golden local reference, then reproduce preprocessing in Lee Taek Gyu's clean account before any full FAST solve.

**Newest confirmed repository action:**
- `CMP/FAST_BASELINE_REPRO_PROTOCOL.md` added.
- `CMP/tcad/capture_reference_snapshot.sh` added.
- Public GitHub `CMP/tcad/CURRENT` is still not the authoritative Copy x8 running source.

**Immediate blocker:**
Existing local reference package `~/CMP_REFERENCE_20261004.tgz` is recorded as missing the exact editable SDevice source `sd_fdiv_des.cmd`. This source must be added locally and hashed before clean-account reproduction.

**Next:**
1. Complete Copy x8 local snapshot with exact source.
2. Generate SHA-256 manifest.
3. In clean account, preprocess only / early initialization.
4. Diff `pp1_dvs.cmd`, `pp6_des.cmd`, `pp6_des.par`; compare mesh hash/statistics.
5. Only after reproducibility gate passes, create numerical-only FAST branch.

**Do not change:** Common Baseline geometry, Nt/Et/sigma, 5 nm sidewall damage width, common A/B physics.

---

## 2026-09-29 — JuSubin active run direct evidence: Node 6 alive, high-bias convergence slowdown

- Direct file evidence: active output is `n6_des.out` (Node 6), superseding the earlier Node-19 inference.
- pseudo-time ≈0.93254, equivalent to ≈4.66 V on the known 0→5 V transient ramp.
- A BE step exceeded 50 Newton iterations, was rejected, then automatically retried with a smaller timestep (~8.67e-06).
- One failed attempt cost ~1244 s wallclock, dominated by solve time (~999 s).
- Status: RUNNING, not hung at the captured moment; repeated high-bias cutbacks are the present runtime bottleneck.
- Next check: confirm continued pseudo-time advance and timestep recovery before considering any restart or solver change.

## 2026-09-29 — JuSubin 3-day Workbench status screenshot

- OBSERVED: selected upper SDevice node reports `Status: waiting`; it has not started solving.
- Lower branch Node 19 appears running in Workbench, but actual solver progress is not proven from topology alone.
- Runtime blocker is now split into (1) scheduler/resource waiting for one branch and (2) unknown progress/hang status for the active branch.
- Next evidence: Node 19 Job Log + last lines/timestamps of `n19_des.out`.
- Do not abort/restart or modify baseline physics solely from this screenshot.

# LIVE AI STATE

## 2026-09-28 — CRITICAL SOURCE SYNC GAP FOUND

- GitHub Issue #7 and JuSubin timeline contain Final SDevice v1.2 progress.
- Actual `CMP/tcad/CURRENT/sdevice2_defect_on.cmd` is still an older stale deck and does NOT contain the v1.2 intermediate TDR save workflow.
- Gmail notifications are GitHub Issue #7 notifications and are consistent with the logged progress; they do not prove the actual code file was synchronized.
- Do NOT overwrite CURRENT from snippets or memory.
- Blocker: recover exact full user-provided Final SDevice v1.1/v1.2 source, then synchronize it.
- Current final-code provenance is therefore UNRESOLVED until that exact source is committed.



## 2026-09-26 — deadline mode

- User needs baseline + PPT today.
- Full 5 V NtSide=1e18 completion is not expected today based on historical multi-day runtime.
- Today deliverable: source/parameter freeze, clean preprocess comparison, successful trap-on initialization/early solve, and presentation-ready baseline evidence.
- Full same-revision NtSide=0 vs 1e18 electrical comparison remains pending and must not be presented as completed.


## 2026-09-26 — exact fix selected

- Proposed minimal edit: move Mg incomplete ionization from global Physics to p-GaN regions only.
- Do not alter Thermionic, trap parameters, Plot, Math, Solve, or geometry.
- After edit, rerun both NtSide=0 and 1e18 from the same frozen source/PAR revision for final comparison.


## 2026-09-26 — fair-comparison correction

- Node6 pp6_des.par and Node12 pp12_des.par are different revisions.
- Node6 uses generic P/N dopant ionization species; Node12 uses pMagnesiumActiveConcentration.
- Existing Node6 vs current/fixed Node12 is not a valid final NtSide-only comparison.
- Final baseline must freeze one source + parameter-file revision and rerun both NtSide=0 and 1e18.
- Node12-only fix remains diagnostic only.


## 2026-09-26 — Mg incomplete-ionization mismatch found

- pp12_des.par has Mg ionization parameters only under Material=GaN for pMagnesiumActiveConcentration.
- No InGaN ionization parameters are present.
- Node12 fails immediately after missing Mg incomplete-ionization parameter messages in InGaN QWs.
- Current source activates Mg incomplete ionization globally.
- Strong root-cause candidate: model/parameter material-scope mismatch.
- Proposed minimal fix: region-scope IncompleteIonization to Clean/DmgL/DmgR pGaN only; keep traps/Thermionic/Plot unchanged.
- Confirmation requires Node12 re-preprocess + initialization rerun.


## 2026-09-26 — full source inspection result

- Current SDevice source has no NtSide-dependent conditional preprocessing.
- NtSide only controls trap Conc.
- Current source always includes Thermionic + species-selected Mg IncompleteIonization + expanded Plot.
- Successful Node6 pp6 lacks those items, so Node6 is historical/stale relative to current source revision.
- Existing Node6 and current Node12 are not a clean same-source NtSide-only comparison.
- Node12 failure remains strongly tied to Mg incomplete-ionization initialization in InGaN.
- Next: inspect pp12_des.par Ionization/Magnesium/InGaN blocks before editing or rerunning.


## 2026-09-26 — Node 12 failure reproduced

- Node 12-only rerun fails again.
- Failure is reproducible.
- Same-source NtSide split is user-confirmed.
- Most likely next discriminators: NtSide-dependent preprocessing vs stale/cached Node 6 preprocess from an older source revision.
- Do not rerun or edit baseline physics until original source conditional logic/provenance is inspected.


## 2026-09-26 — correction: same source, NtSide-only split confirmed by user

- User states Node 6 and Node 12 used the same source; only NtSide=0 vs 1e18 was split.
- Prior proposed physics cleanup is retracted pending source inspection.
- pp6/pp12 differences may come from NtSide-dependent preprocessing or node/input version behavior.
- Do not edit Thermionic/IncompleteIonization/Plot yet.
- Next: inspect original sd_fdiv_des.cmd for parameter-dependent conditionals and source provenance.


## 2026-09-26 — Node 6/12 exact diff found

- Successful Node 6 and failed Node 12 are not NtSide-only decks.
- Extra Node12-only changes: `Thermionic`, species-selected `IncompleteIonization`, and four extra Plot fields.
- Intended difference: trap Conc 0 vs 1e18.
- Current failure therefore cannot yet be blamed on NtSide=1e18 alone.
- Proposed next: restore Node 6 Physics/Plot in original SDevice source, keep only NtSide=1e18, verify preprocessed diff, rerun.
- Status: PROPOSED FIX / UNCONFIRMED until rerun.


## 2026-09-26 — failed Node 12 deck captured

- Node 12 has `Thermionic` and `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`.
- Sidewall traps are 1e18 across pGaN/EBL/barriers/QWs/nGaN.
- Plot block is expanded with trap/SRH/Mg outputs.
- This differs from synchronized baseline record; possible deck drift beyond NtSide.
- Next: exact successful Node 6 pp6_des.cmd diff before any correction.


## 2026-09-26 — baseline branch comparison status

- NtSide=0 Node 6: CONFIRMED normal completion to 5 V; TDR written; wallclock ~65.4 h.
- NtSide=1e18 Node 12: SDevice exit(1) during initialization.
- Success log has no `mMagnesiumActiveConcentration` warning; failed log does.
- Strong correlated difference, but root cause not yet proven.
- Next action: diff `pp6_des.cmd/par` vs `pp12_des.cmd/par` before any physics change.


## 2026-09-26 — Node 12 des.log comparison needed

- Failed `n12_des.log` terminates immediately after InGaN Mg incomplete-ionization parameter messages, then returns licenses.
- No normal solver start is visible.
- Causality is unresolved.
- Highest-priority discriminator: compare the successful NtSide=0 node log for the exact same message.
- Do not alter baseline physics until this comparison is done.


## 2026-09-26 — Node 12 Find Error exhausted

- Find Error output reaches `**** End` with warnings only; no explicit fatal/root cause visible.
- The warnings concern E0 anisotropy and missing Mg incomplete-ionization parameters in InGaN.
- Their causal role is unproven.
- Highest-priority next evidence: `n12_des.log` bottom, then `n12_des.sta`.
- Status remains UNRESOLVED.


## 2026-09-26 — Node 12 failure location narrowed further

- Workbench preprocessing: successful.
- `pp12_des.cmd` / `pp12_des.par`: generated.
- SDevice command launched: `sdevice --max_threads 4 pp12_des.cmd`.
- SDevice returned `exit(1)` shortly after launch.
- Failure is therefore inside SDevice initialization/model setup, not SWB preprocessing/dependency.
- Root cause still UNRESOLVED.
- Next: use **Find Error** / explicit error search in `n12_des.err`.


## 2026-09-26 — Node 12 local.err result

- `n12_local.err`: `Job failed` / `child process exited abnormally` / `gjob exits with status 1`.
- This is a generic wrapper-level failure, not the root cause.
- Root cause remains UNRESOLVED.
- Next evidence: Node 12 Job Log bottom; then `n12_des.job` / `n12_des.sta`.
- Do not alter Common Baseline physics yet.


## 2026-09-26 — Ju Subin Node 12 failure narrowed

- `NtSide=1e18` failed Node = 12.
- `n12_des.err` visible messages are warnings; no fatal cause yet observed.
- `n12_des.out` ends during initialization/license return, without normal SDevice completion text.
- No TDR/PLT visible in Node 12 output list.
- Priority next evidence: `n12_local.err`, then Workbench Job Log.
- Status: UNRESOLVED; do not change baseline physical parameters yet.


## 2026-09-26 — 주수빈 baseline split-run 확인

- OBSERVED: `NtSide=0` run 정상 완료.
- OBSERVED: `NtSide=1e18` run failed.
- Cause: 아직 UNRESOLVED.
- Immediate next action: failed 1e18 SDevice node의 `*.err`와 `*.out` 마지막 구간을 확인해 최초 실패 원인을 식별.
- Do not change Common Baseline physical parameters before log-based diagnosis.


Last update: 2026-09-21
Primary worker: 이택규
Current phase: Phase 0 — Common Baseline validation
Current task: SDevice2 → SVisual2 TDR output/linkage debugging

## Parallel worker — 주수빈

**OBSERVED from shared project conversation:** 주수빈은 Common Baseline 관련 메인 SDevice 및 관련 코드를 최종 수정했다고 보고했고, 장시간 simulation 전에 Project A/B 공통 baseline 적합성을 마지막으로 검토 중이다.

Planned first runs:
- `NtSide=0`
- `NtSide=1e18`

Reported compute cost:
- 약 3일 / run

Verification boundary:
- 주수빈 측 최신 전체 코드와 새 simulation 결과는 이 sync 시점에 GitHub에서 직접 확인되지 않음.
- 따라서 코드 정확성/성공 여부는 아직 CONFIRMED 아님.

## One-line handoff

**SDevice2(Node 9)는 solver 종료까지 갔지만 SVisual2(Node 10)가 기대하는 `n9_des.tdr`이 Node 9 Output Files에서 보이지 않아 로드에 실패한 상태다. 다음 AI는 trap physics를 건드리지 말고 실제 preprocessed Plot filename부터 확인해야 한다.**

## Current blocker

SVisual2 error:

```text
File 'n9_des.tdr' could not be loaded.
```

SVisual2 currently constructs:

```tcl
set tdrfile n@previous@_des.tdr
load_file $tdrfile -name $dname2
```

Node 10 previous node = 9.

## OBSERVED evidence

1. Node 9 `n9_des.out` ends with:

```text
Sentaurus Device simulation finished
Good Bye !
```

Therefore the observed Node 9 run did not terminate with a solver fatal error.

2. Node 9 Explorer Output Files screenshot showed:

```text
n9_des.err
n9_des.job
n9_des.out
n9_des.sta
n9_local.err
pp9_des.cmd
pp9_des.par
```

`n9_des.tdr` was not visible in that screenshot.

3. The Node 9 output also displayed the Plot variable list, including:
- SRHRecombination
- RadiativeRecombination
- AugerRecombination
- TotalRecombination
- Current / eCurrent / hCurrent
- ElectricField
- DopingConcentration
- ConductionBandEnergy / ValenceBandEnergy
- xMoleFraction / yMoleFraction

4. Earlier SVisual2 Tcl mistakes already resolved:
- `create_plot -2d` invalid
- `@node|sdevice@` invalid in this flow
- SVisual2 must not contain an SDevice `Plot { ... }` block

## CURRENT GitHub code

Read these exact files before proposing edits:

- `CMP/tcad/CURRENT/sdevice2_defect_on.cmd`
- `CMP/tcad/CURRENT/svisual2_maps.tcl`
- `CMP/tcad/CURRENT/svisual1_iv.tcl`

SDE and SDevice1 latest full source are NOT yet synchronized.
JuSubin latest modified full code is also NOT yet synchronized.

## Next diagnostic — highest priority

Open `pp9_des.cmd` and inspect the preprocessed `File { ... }` block.

Need exact values of:

```text
Grid =
Parameters =
Plot =
Current =
Output =
```

Then compare the actual preprocessed `Plot = "..."` filename against Node 9 Output Files.

### Decision logic

- If a TDR exists under a different name → fix SVisual2 filename/reference only.
- If `Plot=` points to expected TDR but no TDR exists → diagnose why the SDevice run did not emit the device plot file.
- Do not modify Nt/Et/sigma/damage width while diagnosing this.

## Do NOT change

- Nt = 1e18 cm^-3 nominal Defect ON
- Et = Ev + 0.75 eV
- sigma_n = sigma_p = 1e-15 cm^2
- damage width = 5 nm
- Kou-based vertical epitaxy
- mesa = 4 µm representative modeling choice
- common contacts/physics for A/B comparison

## Known caution from previous ChatGPT attempts

Several trap-output keywords were previously proposed in bulk without confirming T-2022.03 support. Do not reintroduce unverified keywords by guess.

The original synchronized SDevice2 deck contains `SRHRecombination`; the fact that it was not visible in one SVisual scalar list does NOT by itself prove that the keyword is invalid.

## Goal after blocker is solved

1. Load Defect-ON TDR in SVisual2
2. Inspect actual available scalar names
3. Validate sidewall-localized recombination/trap effect
4. Compare Defect OFF vs ON
5. Continue Nt / mesa-size / mesh convergence validation


## 2026-09-22 parallel update — 주수빈 runtime

- Node 6 SDevice NtSide split run이 18시간 이상 실행 중.
- OBSERVED: 직전 BE step은 정상 수렴 완료, total wallclock 약 3563.68 s (~59 min/step).
- 다음 BE step은 약 0.0766738 → 0.0776738, Stepsize=1e-3로 계속 진행 중.
- 현재 증거만으로는 hang/fatal이 아니라 매우 느린 진행으로 판단.
- 주수빈 다음 우선 확인: pp6_des.cmd Solve block의 최종 목표와 step-control 설정을 읽어 총 step 수/예상 runtime 산정.


### 2026-09-22 runtime diagnosis confirmed
- pp6_des.cmd Transient: InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Goal anode=5.0 V.
- Log cross-check: pseudo-time ~0.0766738 corresponds to anode ~0.3834 V, matching 5*time.
- Therefore MaxStep=1e-3 corresponds to ~5 mV maximum bias increment.
- Current point leaves roughly 923–924 accepted steps minimum to reach 5 V.
- Using the latest observed ~3564 s/step as a crude extrapolation gives ~38 days remaining; actual cost can vary with bias.
- Treat current JuSubin blocker as numerical step strategy/computational cost, not SDE/SDevice dependency failure.


### Runtime diagnosis refinement
- User reports the pre-final-edit version of nearly the same deck completed in ~3 days.
- Therefore MaxStep=1e-3 explains a large step count but is not established as the new slowdown cause.
- If old/new step-control is the same, prioritize comparing per-step solve cost and rejected/cutback steps, then mesh size, Physics/Traps application scope, and Math solver settings.
- The prior ~38-day estimate is only a crude extrapolation from one slow step, not a reliable ETA.


### 2026-09-22 identical-bias comparison
- Old run at anode ~0.3834 V: Total 177.47 s (Assembly 64.84 s, Solve 108.74 s).
- Current run at same accepted anode ~0.3834 V: Total 3563.68 s (Assembly 598.77 s, Solve 2928.83 s).
- Current accepted-step cost is ~20.1x old at the same bias.
- Root cause is therefore narrowed to per-step computational cost, not merely MaxStep/step count.
- Next: compare mesh/grid/unknown statistics, Physics/Traps scope, and Math/solver settings old vs current.


### 2026-09-22 correction — same-file early vs late stage
- The 123–177 s logs around 0.30–0.3834 V are NOT verified as an old 3-day run; they are from the current Node 6 `n6_des.out` early section.
- Current run early: 0.0756738→0.0766738 reached ~0.3834 V in Total 177.47 s.
- A later screen from the same current run showed ~0.3834 V with Total 3563.68 s.
- Therefore prior "old vs current 20.1x" conclusion is invalid.
- Highest priority: determine whether the same pseudo-time/voltage ramp occurs in multiple Transient/Solve stages. Search all `Transient(` in pp6_des.cmd and locate `3563.68` / repeated `0.0766738` in n6_des.out.


### 2026-09-22 re-correction — old run confirmed by user
- User explicitly confirmed the 177.47 s / ~0.3834 V screenshot was from the older node that completed in ~3 days.
- Restore valid comparison:
  - old: Total 177.47 s (Assembly 64.84 s, Solve 108.74 s)
  - current: Total 3563.68 s (Assembly 598.77 s, Solve 2928.83 s)
  - current is ~20.1x slower per accepted step at the same anode voltage.
- Prior "same current run repeated stage" correction is retracted.
- Next: diff old vs current Math/solver, Physics/Traps scope, and mesh/unknown statistics.


### 2026-09-22 old 3-day full deck captured
- Old preprocessed `pp6_des.cmd` provided in full.
- All DmgL/R trap blocks have `Conc=0`; this is an NtSide=0 case.
- Old numerical stepping: InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Goal anode=5 V — same as the slow current Solve block already observed.
- Old Math signature: 4 threads, Digits=5, ErrRef=1e4, RHSMin=1e-3, BE, ExtendedPrecision(80), Blocked + ILS(22), gmres(100), tolrel=1e-10, ilut(1e-8,-1).
- Priority: verify current slow node's actual trap Conc. Only compare runtime directly if current is also NtSide=0.


## 2026-10-06 — FAST_C2 half-domain / selective-mesh direction accepted

- 작업자: 이택규
- 상태: DECISION / IMPLEMENTATION CANDIDATE
- user accepted a runtime-optimization branch using half-domain symmetry plus localized fine mesh.
- keep current Node 6/12 full-device runs as reference evidence.
- candidate only: half-domain is allowed only after confirming left-right symmetry of geometry, doping, contacts, traps and BCs in the actual SDE source.
- preserve fine resolution at the 5 nm sidewall-damage region and other solution-critical interfaces/high-field zones; coarsen only remote homogeneous bulk with graded transitions.
- publication gate: compare against full/fine reference at identical physics/bias, including current normalization and key spatial metrics, before adopting.
- immediate next step: recover/inspect exact running SDE source, then create separate FAST_C2 short benchmark.


## 2026-10-06 — Project B compatible with half-domain, but center active region remains mesh-critical

- Project B symmetric AlBarrier_L/R concept is compatible with half-domain if the actual SDE/contact/BC setup is mirror-symmetric.
- do not remove mesh from the retained center domain; only coarsen remote homogeneous bulk.
- Project B requires additional refinement at GaN/AlGaN lateral interfaces and barrier/MQW intersections, while the center MQW must remain adequately resolved for radiative/current-crowding metrics.
- adoption still gated by full/fine equivalence validation.


## 2026-10-06 — A/B half-domain + selective mesh formally recommended as validated candidate

- 작업자: 이택규
- 상태: REVIEWED / RECOMMENDED CANDIDATE
- A/B 모두 mirror symmetry가 actual SDE/contact/BC에서 확인되면 half-domain 적용 가능.
- retained center domain의 mesh는 제거하지 않고 remote homogeneous bulk만 graded coarsening.
- common fine zones: 5 nm sidewall damage, MQW, junction/heterointerfaces, high-field/depletion/contact edges.
- A-specific: refine Cedge/GaN:C boundary.
- B-specific: refine lateral AlGaN/GaN interface and barrier-MQW intersections; B has stricter interface-mesh need because band offsets/fields are primary mechanism.
- final adoption requires full/fine equivalence validation; current Node 6/12 reference runs remain preserved.


## 2026-10-06 — Half-domain preserves IQE ratio under mirror symmetry

- current CMP IQE metric: integrated Rrad / (Rrad + RSRH + RAuger) over an identical physical integration region.
- for an exactly mirror-symmetric device, each full-domain integrated recombination term is twice the half-domain term, so the factor of 2 cancels in IQE.
- half-domain is therefore valid for IQE comparison, provided symmetry and identical integration-region definitions hold.
- do not multiply IQE by 2; only absolute total current/recombination/power may require full-device symmetry scaling/2D normalization checks.


## 2026-10-06 — Recommended baseline strategy: physical 4 µm device, validated half-domain production model

- physical Common Baseline remains a 4.0 µm mesa.
- recommended computational representation, after validation: simulate only the 2.0 µm half-domain with centerline symmetry.
- retain full/fine runs as reference evidence; do not delete the full model from the methodology.
- validate symmetry-only change before mesh coarsening, then use the same validated half-domain mesh policy for Baseline/A/B production comparisons.
- IQE is compatible with the half-domain under exact symmetry; absolute totals still need normalization/symmetry scaling checks.


## 2026-10-09 11:30 KST update
- OBSERVED (user report): `JUSUBIN_FAST_HALF_SWB` run completed overnight.
- Previous blocker "half+coarse transient still running" is cleared at report level.
- Verification gate remains: confirm final 0.3 V, no fatal termination, output artifacts, and extract runtime/I-V before treating the run as a validated result.


## 2026-10-09 11:30 KST priority
1. Verify completed `JUSUBIN_FAST_HALF_SWB` terminal/log evidence: final 0.3 V, normal completion, no fatal/error, output files.
2. Extract total wallclock/runtime and I-V points from the completed half+coarse transient.
3. Check the `JUSUBIN_FAST_HALF_SWB_Copy` QS smoke status/result separately.
4. Compare Half+coarse transient vs QS Copy, then against full FAST_C1 reference before adopting the fast branch for production A/B.


## 2026-10-09 — QS Copy early termination verified; original transient complete
- Original `JUSUBIN_FAST_HALF_SWB` transient: CONFIRMED 0.300 V trace completion, 25019.43 s, 412K PLT / 15M TDR / 3.1M SAV. 0.3 V I-V examined but physically validated baseline not yet established.
- Separate `JUSUBIN_FAST_HALF_SWB_Copy` QS: UNRESOLVED — SDevice `Step-size less than MinStep (step-size = 8.3986e-07)`; 18417.09 s and `Good Bye`, SAV/TDR written. Goal 0.3 V NOT confirmed. No comparable QS speedup conclusion.
- Next: QS n2_des.plt last accepted anode bias + last log step/retries/err; do not modify baseline or solver yet.


## 2026-10-09 — QS Copy last accepted bias determined
- 작업자: 이택규. OBSERVED from user-provided `JUSUBIN_FAST_HALF_SWB_Copy/n2_des.plt` tail and `n2_des.log` grep.
- Last recorded QS pseudo-time: 6.43487876313307E-02; last anode OuterVoltage: 1.93046362893992E-02 V (0.0193046363 V; 19.3 mV, only ~6.435% of requested 0.3 V).
- Last log attempts at t=0.0643488 to 0.0643505 then terminated `Step-size less than MinStep (step-size = 8.3986e-07)`.
- QS runtime 18417.09 s but did NOT reach goal. Cannot compare as speedup to original transient that reached 0.3 V in 25019.43 s.
- Root numerical/physics trigger not yet established. Next: inspect QS log around lines 6900-7000 and `n2_des.err`; no blind MinStep or baseline modification.


## 2026-10-09 — QS Newton failure isolated
- Final attempted QS step `t=0.0643488→0.0643505`, Newton Poisson+electron+hole Bank/Rose hit Coupled limit 15, residual oscillated to ~1.26e8, final ~1.85e6; retry step 8.3986e-7 below MinStep 1e-6. Root numerical/physical trigger unresolved. Preserve completed transient and baseline. Next inspect actual active QS Math/Solve deck before any numerical-only pilot.


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


## 2026-10-09 — Filesystem copy exists; SWB open not yet checked
- 이택규 executed `cp -a JUSUBIN_FAST_HALF_SWB JUSUBIN_FAST_HALF_5V_TEST`, subsequent ls confirmed target directory and `cmp` between original/copied SDevice source produced no differences.
- Bash-style conditional produced `if: Expression Syntax.` in current C-shell-like terminal; standalone copy command worked.
- Next verify original/copied hidden `.project` file and project directory content, then open copied project in SWB Projects browser; preserve original, do not run simulations or edit high-bias deck yet.


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


### 2026-10-09 archive check
- 이택규 verified tar listing of JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz: C-shell status 0.
- 5V SDevice Node2 startup is now next; F7 launch not yet observed. Original projects preserved.


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

## 2026-10-09 14:29:52 KST — Half+Coarse 5V TEST Node2 COMPLETE (OBSERVED)

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

## 2026-10-09 — 5V SVisual radiative field (OBSERVED)

- 이택규 screenshot shows positive RadiativeRecombination in final n2_des.tdr; plot max 7.483e19 cm^-3 s^-1, min about zero (-7.512e-34). Mesh 138194 elements / 65513 points.
- The high-rate thin layers have not been mapped to named Clean_QW1-4, so MQW emission, integrated rates and IQE remain unverified.
- NEXT: SVisual Regions tab identify QWs and probe rates; then SRH/Auger and material radiative coefficient. Preserve results.

## 2026-10-09 — 5V_TEST four InGaN Clean_QW local RadiativeRecombination Probe measurements (OBSERVED; IQE NOT YET)

- 작업자: 이택규. User supplied four direct Sentaurus Visual Probe screenshots in `JUSUBIN_FAST_HALF_5V_TEST` / `n2_des`, with scalar `RadiativeRecombination`, explicit zone label, x/y coordinates and Magnitude (cm^-3 s^-1, unit grounded in preceding SVisual legend).
- `Clean_QW1(InGaN)`: x=0.169818746552, y=0.560459877538, z=0, `Rrad=1.836010164996e+13`.
- `Clean_QW2(InGaN)`: x=0.194326754006, y=0.556958733616, z=0, `Rrad=3.558921779790e+12`.
- `Clean_QW3(InGaN)`: x=0.22058533342, y=0.56571159342, z=0, `Rrad=8.395713573050e+14`.
- `Clean_QW4(InGaN)`: x=0.245093340874, y=0.58321731303, z=0, `Rrad=7.094266327897e+18`.
- Result: **each of four named InGaN QWs contains a positive local Rrad point**, beyond mere output declaration or plot-wide maximum. The QW4 sampled point exceeds sampled other QW values by several orders of magnitude. HOWEVER: points differ in both vertical and lateral coordinates (x/y), so local values are **NOT** region-integrated emission, per-well averages or a verified QW4 total-emission dominance. Do not treat local peak, photon escape, IQE or material radiative coefficient as validated.
- Remaining: check SRH and Auger at the *same probe coordinates*, map Rrad spatially through each QW and perform mesh/region correct integrals, confirm 2D current normalization, injection/current plausibility and half-vs-full correspondence; NtSide=0 branch only. No new solver or source changes.

## 2026-10-09 — QW4 SRH point confirmed; coordinate mismatch with Rrad

- User SVisual Probe: Clean_QW4(InGaN), srhRecombination = 1.681637512936e22 cm^-3 s^-1 at (x,y)=(0.244864017914, 0.599783903626).
- Previous Clean_QW4 Rrad=7.094266327897e18 was at (0.245093340874, 0.58321731303). Same region, different position; direct pointwise SRH/Rrad comparison and IQE are not valid.
- NEXT: Probe SRH and Auger at the exact previous Rrad coordinate and validate integrated QW rates before estimating IQE. No code or model change.

## 2026-10-09 — 5V_TEST co-located Clean_QW4 Probe shows dominant local SRH (OBSERVED; device IQE UNRESOLVED)

- Worker 이택규 provided three SVisual Probe screenshots on the completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des` final TDR. All three are the **same point**: zone `Clean_QW4(InGaN)`, x=`0.244864017914`, y=`0.651958341615`, z=0. This differs from earlier SRH y=0.599783903626 and initial Rrad y=0.58321731303; do not mix old and new point values.
- Same-point fields in cm^-3 s^-1 (screen values): `RadiativeRecombination=7.103015017104e18`; `srhRecombination=1.681575471039e22`; `AugerRecombination=1.238545872618e15`; `TotalRecombination=1.682285896396e22`. Sum agrees with displayed TotalRecombination within screenshot precision.
- Derived **LOCAL radiative fraction only**: `100*Rrad/(Rrad+Rsrh+RAuger)≈0.0422%`; local nonradiative fraction ≈99.9578%; SRH dominates at this sampled point. This is **NOT** full-QW or full-device IQE, nor proof of overall LED performance/failure. QW1–QW3 require corresponding SRH/Auger samples and integrated full-QW volumes for recombination-based IQE.
- Importantly `NtSide=0` disables parameterized damaged-edge traps in this reference branch but does NOT disable the generic `SRH()` bulk nonradiative recombination physics; high QW local SRH does not by itself prove sidewall damage or carbon-project effect. Need inspect active carrier lifetime, material parameters and field/region distribution before root-cause claims.
- NEXT: preserve outputs and avoid rerun; use read-only SVisual integrated QW Rrad/SRH/Auger workflow and compare QW1–4, inspect actual active SRH lifetime and material database, 2D current normalization/physical injection. Use same-bias/current full vs half/fine check before declaring Common Baseline. No TCAD code modified.

## 2026-10-09 — Corrected measurement priority: QW3 probes confirmed, per-region integration needed (OBSERVED / SCIENTIFIC DECISION)

- Worker: 이택규. User submitted SVisual Probe screenshots in the successful `JUSUBIN_FAST_HALF_5V_TEST/n2_des` 5V result. Clean_QW3(InGaN) same location x=0.219173763524, y=0.555622585194, z=0: `RadiativeRecombination=8.333611568957e14`, `srhRecombination=5.390114530106e19`, `AugerRecombination=5.79338765299e8` cm^-3 s^-1. Other captured fields include electron density 1.385821616728e14 and hole density 4.507709343047e11 (units of densities expected cm^-3, panel exact unit not shown). Numerical point checks are local only, no physical IQE claim.
- User correctly identified that publication analysis requires **integrating the recombination rate over each entire QW**, not further collecting isolated probes. Adopt `CMP/PROJECT_AB_PRE_RUN_AUDIT.md` G5 and metric definition: integrate Rrad, SRH, Auger over each QW region, sum integrals, THEN compute recombination-based IQE. Do not average or sum local fractional IQEs. The local QW3 and QW4 probes suggest large SRH at those sampled points but are not representative of whole-well rates.
- First non-destructive operational check: SVisual Tools > Integrate (∫dr right toolbar), field RadiativeRecombination, Region/Material filter Clean_QW3 only, complete spatial domain and Start Integration. Save/report raw integral AND domain units displayed; then integrate same QW's srhRecombination and AugerRecombination and expand QW1..4. Include DmgL_QW regions as appropriate for complete active-QW physical volume and matched full/half comparisons, explicitly avoid counting Clean-only as total QW losses. Two-dimensional SVisual integration produces an area integral with native geometrical units; out-of-plane depth/2D normalization and actual physical cm unit conversion MUST be verified for absolute recombination counts; a ratio of comparably normalized integrals cancels common factors.
- Older and newer Sentaurus Visual User Guides document Field Integration GUI and `integrate_field -field ... -regions {Clean_QW3}`; current environment T-2022.03-specific GUI behavior and output units still require a user screenshot before scripting/automation is treated as validated. No TCAD source or baseline changes or new solver runs.

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

## 2026-10-09 — MaterialDB inspection shell mismatch; corrected read-only action

- 이택규 observed `n2_des.log` physical model block around lines 330–350: SRH/Auger/Radiative active; SRH has no field/doping/temperature lifetime dependence, Surface-Recombination off; line `Use Si parameters` has **unresolved** material/device-scope meaning.
- Assistant provided Bash `DB=...` and `for ...; do` but user terminal is C-shell family (likely csh/tcsh); all those MaterialDB grep attempts failed with Command not found/Undefined variable, no parameter numbers obtained. This is a command-syntax guidance error, not Sentaurus failure; no files changed.
- NEXT: run `grep -niE 'SRH|Radiative|Auger|taun0|taup0|Scharfetter' /user/tools/synopsys/sentaurus/T-2022.03/tcad/current/lib/sdevice/MaterialDB/InGaN.par | head -n 70`; review actual values/sections and context, compare GaN/InN only as necessary; do not modify model until effective parameter check.

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

## 2026-10-09 — CRITICAL OBSERVED InGaN MaterialDB warning: GaAs-derived recombination parameters require calibration

- 작업자 이택규 provided direct terminal `sed -n '855,925p' /user/tools/synopsys/sentaurus/T-2022.03/tcad/current/lib/sdevice/MaterialDB/InGaN.par` for actual Sentaurus T-2022.03 environment. **Direct vendor material file warning** immediately before Scharfetter SRH / Auger / Radiative sections: `Parameters for the recombination models below were taken from GaAs and require calibration for accurate simulations`.
- The InGaN.par values documented in actual file: `Scharfetter taumin=0,0 [s]`; `taumax=1.0e-9,1.0e-9 [s]`; `Nref=1.0e16,1.0e16 cm^-3`; `gamma=1,1`; `Talpha=Tcoeff=0`; `Etrap=0`. `Auger A=1.0e-30,1.0e-30 cm^6/s`, `B=C=H=0`; `RadiativeRecombination C=2.0e-10 cm^3/s`. The radiative coefficient symbol in par is C (commonly referred to as B in LED ABC notation).
- This is ACTUAL MATERIAL FILE evidence, **not yet complete proof of effective per-In0.15Ga0.85N parameters at the active QWs** (material mixing/overrides and file-precedence audit pending). `n2_des.log` previously observed `DefaultParametersFromFile` for InGaN.par, and SRH/Rad/Auger enabled, without field/doping/temperature-dependent lifetimes. Never automatically infer effective SRH lifetime everywhere equals 1ns without inspecting enabled model and resolved coefficients.
- SCIENTIFIC STATUS: Existing 5V Half+Coarse NtSide=0 recombination-only 4-QW ratio=0.1094747566% with SRH 99.886155%. The GaAs-derived uncalibrated InGaN recombination parameters make physical validity an **explicit calibration blocker**, not proof of a geometrically incorrect Mesa/MQW or sole proven cause of low efficiency. NtSide=0 removes parameterized edge traps, but global SRH() persists. Deep-electrical injection/J normalization, polarization, band profiles, material mixing may also matter.
- DECISION / NEXT: preserve baseline and measured simulation outputs (do not silently tune lifetime to increase efficiency); first verify active log/model parameter precedence `sed -n '945,970p' n2_des.log` and `sed -n '270,310p' n2_des.log`, determine proper In0.15Ga0.85N interpolated/overridden Rrad/SRH/Auger coefficients, verify 2D current injection. Then establish literature-backed parameter calibration and sensitivity with unchanged geometry and documented alternate physics branch only after team approval. No TCAD source edited or rerun in this check.

## 2026-10-09 — Literature cross-check & Baseline rerun GO/NO-GO after 5V_TEST low MQW efficiency (REVIEWED, not new simulation)

- Worker 이택규 supplied actual n2_des.log sections. Observed DefaultParametersFromFile loads T-2022.03 MaterialDB/InGaN.par and InN.par, and ModelParameters FASTC1_pp6_des.par, Grid n1_msh.tdr, Current n2_des.plt; log says no separate Lifetime file. This does NOT mean SRH is off or there is no lifetime: active MaterialDB Scharfetter section provides it. The global default block 'Use Si parameters' / 'Without incomplete ionization' cannot be assigned to active InGaN wells or Mg settings without region context. No override coefficients or final mole-fraction interpolation verified yet.
- **Peer-reviewed basis**: Kou et al. Optics Express 2019 DOI 10.1364/OE.27.00A643 uses Auger 1e-30 cm6/s, SRH numerical lifetime 1e-7 (paper displays unit s^-1, which is inconsistent with lifetime and must be flagged as a likely notation error, not ignored); Baek et al. Nature Communications 2023 DOI 10.1038/s41467-023-36773-w simulation uses SRH 100ns, Radiative 1e-10 cm3/s, Auger 1e-31 cm6/s, with a DIFFERENT 6-QW epitaxy and fitted polarization/interface assumptions. Low-current SRH dominance also discussed in Nanoscale Research Letters 2021 https://pmc.ncbi.nlm.nih.gov/articles/PMC8175512/. None uniquely fixes our model values without calibration.
- **Existing vendor file**: InGaN.par explicitly warns GaAs-derived SRH/Auger/Radiative parameters require calibration; Scharfetter taumax 1e-9 s; Rrad C=2e-10; Auger A=1e-30. File values are not yet proven to be final effective xIn=0.15 parameters. Relative to published 100ns example the file taumax is 100 times shorter, potentially explaining large SRH but not a proved sole root cause.
- Existing 5V NtSide0 Half+Coarse integrated 4 QWs Clean+DmgL: Rrad 40072.8158452, SRH 36562944.9075, Auger 1599.706168587 [s^-1 um^-1], fraction 0.1094747566%. Source no user code changes. QW4 ~96.94% of Rrad integral. 2D PLT terminal current raw =1.44801646079583e-11, dimension and AreaFactor still unresolved. From 2D QW3 area 0.00600001202um2 and QW thickness 0.003um, inferred Half width approximately 2um: **CONDITIONAL** on no scaling and A/um terminal current, J_5V ≈ 1.448e-11 / 2 × 1e8 ≈ 7.24e-4 A/cm2, much less than literature 0.1 A/cm2 low-current example; this is NOT verified operating J.
- **Verdict**: No evidence the nominal four-QW Kou-based geometry itself must be rebuilt; no validation of a publishable absolute IQE/optical LED baseline. Need to resolve active material parameters, low current density, carrier injection/polarization, steady-state validity and Half-vs-Full reference. Current IQE issue **must be addressed or clearly bounded** before using baseline for credible Project A/B SRH/IQE improvement conclusions. Causality not established. No new long run now; original finished files protected.
- **Stage plan** (proposal only): (1) read-only pp2/log/material model precedence and QW In mole interpolation, 2D J and equivalent 2D Half area, carrier/hole density and interface traps; (2) literature-supported calibrated parameter *separate branch* including tau sensitivity 1ns/10ns/100ns as exploratory, not automatic performance tuning; compare at same J and keep nominal sidewall Trap; (3) Short NtSide0 QS/steady + checkpoint pilot, electrical/optical checks; (4) NtSide1e18 matched-current sidewall contrast; (5) Mesh convergence and Full-vs-Half, 4/10/20um and Nt sensitivity for paper; (6) only then freeze revised physical Baseline, Project A/B null-control/pilot and broader DOE. Must not silently alter original source.

## 2026-10-09 — Live 5V_TEST pp2 model audit evidence (이택규)

- OBSERVED actual pp2 shows Fermi, Thermionic, piezo polarization, default material files, SRH/Auger/Radiative. Region `IncompleteIonization` at lines 128/137; `Traps` region declarations 141–361; `Transient=BE` at 515, `Transient(` at 585. No AreaFactor/Quasistationary in pp2/par grep.
- Region-specific Mg incomplete ionization and actual Trap concentrations are UNVERIFIED until Physics-region blocks inspected; appearance of `Traps` does not contradict NtSide0 by itself. 5V normal finish is transient, not proven steady state. Need effective InGaN material parameters and verified J normalization before IQE publication claim.
- NEXT read-only `sed -n '112,175p' pp2_des.cmd` and `sed -n '505,615p' pp2_des.cmd`; do not modify original solver/results.

## 2026-10-09 — SWB Create Parameter File dialog and silicon-vs-GaN misconception; controlled baseline calibration plan (OBSERVED + REVIEWED)

- Worker 이택규 screenshot: SWB title shows **/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_SWB** (the *original branch*, NOT already-completed `JUSUBIN_FAST_HALF_5V_TEST`). Dialog `Create Parameter File`: **`Parameter file sdevice.par does not exist`**, radio choices `Silicon` default selected, `Choose Materials`, `Create Empty File`; scenario `NtSide=0`, SDE→SDEVICE.
- This is an **input-generation dialog** not an SDevice error or proof the existing 5V simulation used Silicon physics. Actual completed 5V_TEST n2_des.log lists `ModelParameters file: FASTC1_pp6_des.par`, `DefaultParametersFromFile` loading GaN/InGaN/InN MaterialDB, and a working 5V curve trace; that branch's `pp2_des.cmd` has region-specific incomplete ionization and `NtSide=0` ALL 12 sidewall `Conc=0` entries preprocessed (already earlier recorded in LIVE_STATE JSON). Do not confuse same old SWB input-file workflow with 5V_TEST source.
- Synopsys SWB User Guide (publicly accessible N-2017.09 pages 65–68, https://studylib.net/doc/28266667/swb-ug) documents `Tool > Edit Input > Parameter` then `Choose Materials` and selection, copies chosen release MaterialDB files into project and includes `Material="GaN" { #includeext ... }` etc in sdevice.par; Silicon default merely generates Silicon material file; `Create Empty File` possible. Tool properties can use common `sdevice.par` or per-tool .par. Sentaurus Device default physical parameters have builtin/material DB/custom parameter file precedence; blindly generating/using a new sdevice.par can overwrite working FASTC1_pp6_des.par customization (e.g., lattice/polarization/thermionic and Magnesium ionization), and merely copying the uncalibrated GaAs-derived InGaN.par does NOT improve recombination IQE.
- Intended mesh materials in Common Baseline: GaN, InGaN, AlGaN, Nitride (Si3N4); InN relevant as InGaN constituent and file-loader but not necessarily an explicitly meshed domain. Confirm exact mesh material names before choosing in a NEW clone. Danger: picking only GaN does not set all InGaN/AlGaN regions to GaN; material assignment is in SDE/TDR.
- **Immediate safe recommendation**: Cancel current parameter creation in original JUSUBIN_FAST_HALF_SWB, do NOT hit OK with Silicon or generate any .par there, do NOT rerun there yet. Clone known 5V_TEST to separate calibration sandbox after backing up existing source and results, audit `File{Parameters}` of active sdevice source and actual pp2_des.par/FASTC1_pp6_des.par before integrating a region/material-specific calibration par.
- As of 2026-10-08 JuSubin timeline (documented, not necessarily new actions today): Half+coarse mesh 138,194 elements/65,513 points versus Full 290,814; half+coarse equivalence to Full unverified; Mg/n-GaN doping-profile physical validation not complete; QS 0.3V pilot proposed; later LeeTaekGyu Oct9 run of QS Copy failed at **0.019304636 V** with Newton 15 iterations then MinStep; physical cause unresolved. Additional sidewall trap-ON NtSide=1e18 in accelerated Half branch unverified. C2 save/load reference gating remains separate.
- New blocker classification: P0 preserve original proven 5V_TEST source and metadata, establish exact active materials and .par custom overrides; P1 check doping/currents/2D AreaFactor and material B/SRH lifetime, NtSide0 region trap status; P2 conditional calibration branch and short smoke/QS/Transient checks; P3 NtSide1e18 at matched J; P4 Half+Coarse vs Full/mesh and no-project modification without explicit approval. Issue #7 append only.

## 2026-10-09 — 5V_TEST confirmed region-specific Mg and NtSide=0 trap excerpts

이택규 directly inspected the active completed 5V_TEST `pp2_des.cmd` (lines 112–175): `Clean_pGaN` and `DmgL_pGaN` explicitly enable `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`; `DmgL_pGaN` and `DmgL_EBL` trap entries are `Acceptor Conc=0, EnergyMid=0.75 eV from valence, e/h cross-section=1e-15 cm²`. This verifies local Mg ionization *model declarations* and two explicit trap-OFF regions, NOT actual Mg free-carrier/donor doping profile. All other trap region concentrations require complete deck grep (prior audit indicated 12 zero). Global log 'Without incomplete ionization' cannot override observation of region-specific code without scoping analysis. No files altered, 5V results preserved. NEXT READ-ONLY `grep -nE 'Physics \(Region=|IncompleteIonization|Traps|Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp2_des.cmd`, then SDE doping profile and physics/current density calibration. Publication-grade baseline validation still pending.

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
