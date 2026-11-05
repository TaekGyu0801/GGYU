## 2026-11-05 Lee n25 Trap ON 5V terminal freshly reconfirmed alongside n21 OFF — OBSERVED BOTH; current ratio not IQE
- Worker 이택규 ran school read-only `grep -E '^[[:space:]]*anode[[:space:]]+[0-9.E+-]+' n25_des.log | tail -n 1` from `CMP_WU_Copy`; output `anode 5.000E+00 1.690E-04 2.397E-03 2.566E-03`. Previously same session n21 OFF at 5V yielded `anode 5.000E+00 1.695E-04 2.399E-03 2.569E-03`. Both terminal rows are now **directly user OBSERVED**.
- OFF→ON relative total-current change from rounded printed data = ((2.566e-3-2.569e-3)/2.569e-3)*100 = -0.11678%; absolute difference = -3.0e-6 raw SDevice output units. Equal voltage, not independently validated equal-current-density condition or a measured IQE reduction. Need 2D z-unit normalization and independently integrated trap-inclusive net recombination for physical sidewall loss/QW IQE analysis.
- No new SDevice runs, source edits, parameter changes or canceled hGap restart. Next evaluate archived n21/n25 region-integrated Radiative/SRH/Auger and correctly defined net trap pair-rate (not simple electron+hole gap-state sum) before GO on Wu vs protected 4um Kou Common Baseline.

## 2026-11-05 Lee n21 OFF 5V terminal current reread and prior n25 ON comparison — OBSERVED OFF, ON historical; trap loss UNRESOLVED
- Worker 이택규 directly pasted school terminal from `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`. The read-only command `grep -E '^[[:space:]]*anode[[:space:]]+[0-9.E+-]+' n21_des.log | tail -n 1` was executed twice; both returned exactly `anode 5.000E+00 1.695E-04 2.399E-03 2.569E-03`. This is **one repeated Trap OFF n21 5V reading**, not a newly executed ON result.
- Prior school `n25_des.log` Trap ON 5V output, previously OBSERVED in earlier session: anode electron 1.690e-4, hole 2.397e-3, total 2.566e-3. OFF→ON total difference = -3.0e-6 in simulator-reported terminal-current units; relative = (2.566e-3 / 2.569e-3 -1)*100 = -0.1168% (rounded source rows). Electron -0.2950%; hole -0.08337%. **This is a raw electrode current comparison at nominal 5V**, not a physical IQE reduction or proof of negligible sidewall loss. Numerical convergence/equal solver settings and 2D absolute units/J normalization still require validation.
- No new simulator run or source code modification. NEXT: execute exactly once `grep -E '^[[:space:]]*anode[[:space:]]+[0-9.E+-]+' n25_des.log | tail -n 1` in same school directory to freshly reconfirm ON. Then proceed to region-integrated radiative, SRH and net trap recombination and defensible IQE definition; preserve canceled hGap and protected 4um Common Baseline.

## 2026-11-05 Lee Wu publisher Figure 1 vs Figure 11 source check — OBSERVED text; original figure pixels UNAVAILABLE
- Worker 이택규 requested assistant to independently locate Wu et al. 2023 original source and determine EBL/contact fidelity. Official publisher article: https://www.sciencedirect.com/science/article/pii/S2773012323000390 (DOI 10.1016/j.micrna.2023.207542) explicitly describes 10 um example and identifies **Fig. 1(a)** as basic TCAD device structure. The accessible excerpt expressly reports n-GaN 3.9 um, Si=5e18 cm^-3, 4x In0.08Ga0.92N QW 3 nm, GaN barriers 8 nm, p-GaN Mg=2e19 cm^-3, and acceptor-like traps within 5 nm of both sidewalls.
- Publisher article excerpt separately identifies proposed **C-shaped anode in Fig. 11**, NOT the basic Fig. 1(a) geometry; do not copy it as standard basic contact. This does not imply a specific Fig. 1(a) electrode shape.
- The exact Fig. 1(a) image/full PDF could not be accessed during public web verification; ResearchGate page https://www.researchgate.net/publication/368792350_Physical_mechanisms_on_the_size-effect_in_GaN-based_Micro-LEDs explicitly says no full-text available/request PDF. Therefore **paper Fig. 1(a) EBL presence, p-GaN thickness, exact standard electrodes remain UNRESOLVED**, not 'no EBL' or 'full width electrodes verified'. Source material text alone cannot determine these.
- Current school Wu pilot (10um, tP 0.12um provisional, tEBL=0, full-width planar Ohmic contacts) is still NOT verified as exact paper replica and must not replace protected 4um Kou-based Common Baseline. No school run, code edit or physics decision in this check.
- NEXT: obtain legitimate full original Fig. 1(a) when accessible, or treat Wu as explicitly parameterized pilot and independently validate J/current units and trap-inclusive IQE. Preserve n21/n25 and canceled hGap.

## 2026-11-05 Lee Wu n25 actual pp25 device header inspected — OBSERVED; stale proposed banner possible
- Worker 이택규 pasted school `sed -n '1,33p' pp25_des.cmd`. First accidental concatenation (`pp25_des.cmdsed`) produced only a shell sed file-not-found error; second command still returned the actual source and needs no repeat.
- Actual effective source header reads `CMP_BASELINE_3.2.0_WU2023PHY — PROPOSED/NOT RUN ON SCHOOL T-2022.03`. This banner conflicts with separately user-observed n25 5V solver terminal-current log; likely stale source comment, but version/provenance not proven from header alone. Do NOT treat the comment as proof of not-run or the source as complete verified Wu replication.
- `File`: Grid n1_msh.tdr, Current n25_des.plt, Plot n25_des.tdr, Output n25_des.log, Parameter pp25_des.par. `Electrode`: anode/cathode Voltage=0.0. Global `Physics`: Temperature=300, DefaultParametersFromFile, Fermi, Mobility(DopingDependence HighFieldSaturation), Recombination(SRH Radiative Auger), Piezoelectric_Polarization(strain), IncompleteIonization(Dopants="MagnesiumActiveConcentration"), Thermionic. No explicit global `AreaFactor` in this displayed block, consistent with earlier full source keyword grep and electrode log factor=1.
- Header says Thermionic and PooleFrenkel numerical proxies, not independently exact Wu interface/trap method; `pp25_des.par` orientation/params and full structural fidelity remain unresolved. No new run or edits. NEXT prioritize Wu pilot vs protected Kou 4um Common Baseline suitability, 2D J normalization and QW IQE; do not repeat area-factor grep or canceled hGap rerun.

## 2026-11-05 Lee Wu n25 source AreaFactor grep verified — OBSERVED, 2D J still UNRESOLVED
- Worker 이택규 pasted actual school `CMP_WU_Copy` terminal read-only grep: `grep -nEi 'AreaFactor|Physics|Electrode' pp25_des.cmd | head -n 35` lists `Electrode {` at line 18 and global `Physics {` at line 22, with region Physics blocks through line 203; **no explicit AreaFactor occurrence in this effective source grep**. Earlier `n25_des.log` showed anode/cathode electrode area factor=1. This establishes no explicit AreaFactor in this inspected pp25 source, not complete validation of units or geometry.
- Repeated user n25 terminal rows: 4.804V Ie=1.364e-4 Ih=2.100e-3 total=2.236e-3; 4.904V Ie=1.525e-4 Ih=2.251e-3 total=2.403e-3; 5.000V Ie=1.690e-4 Ih=2.397e-3 total=2.566e-3. 5V hole share=(2.397e-3/2.566e-3)*100=93.41% of electrode conduction current, NOT IQE.
- Current-density units/effective z width and projected area are still unresolved; conditional planar 10um stripe J is NOT a verified 4um physical pixel J. NEXT READ ONLY inspect `sed -n '1,33p' pp25_des.cmd` for electrode global physics and `sed -n '1,32p;80,94p' pp1_dvs.cmd` for geometry/contacts if needed; resolve unit convention before any physical J/IQE GO. Do not rerun or modify protected models; canceled hGap run stays canceled.
- No new simulator run or school source edit. Source: user-pasted 2026-11-05 command outputs.

## 2026-11-05 Lee n25 5V terminal electron hole total current and electrode AreaFactor reconfirmed — OBSERVED; physical current-density normalization UNRESOLVED
- Worker 이택규 school `CMP_WU_Copy/n25_des.log` grep returns electrode initial entries `anode` Ohmic area factor 1 and `cathode` Ohmic area factor 1 (lines 236–237). Last terminal current table entries: anode at 4.804V electron 1.364e-4, hole 2.100e-3, total 2.236e-3; 4.904V electron 1.525e-4, hole 2.251e-3, total 2.403e-3; 5.000V electron 1.690e-4, hole 2.397e-3, conduction total 2.566e-3 (Sentaurus 2D terminal-current output convention needs exact-version confirmation). 5V component check electron+hole=2.566e-3; hole fraction 2.397e-3/2.566e-3 = ~93.4% of electrode conduction current, **not** an IQE or QW pair-recombination fraction.
- Historical official Synopsys Sentaurus Device UG N-2017.09 states 2D terminal current default unit A/um, and 2D default missing-direction width 1um unless physics/electrode AreaFactor modifies it. The team's school T-2022.03 UG observation says AreaFactor multiplies currents and charges and may represent missing z width. Under the **conditional** assumptions 2D A/um output, global AreaFactor=1, nominal contact width=10um across stripe, simple planar projected J = (2.566e-3 A/um)/(10um) * 1e8 um2/cm2 = 2.566e4 A/cm2. This number is a *conditional model-stripe J*, NOT verified 10x10um real pixel J or 4um Common Baseline J. Recheck live `pp25_des.cmd` Physics/global AreaFactor and SDevice actual effective unit/geometry and log output before reporting it as validated.
- NOTE: user provided only electrode log and last current entries; **did not yet provide previous requested source grep**. Next READ ONLY single step `grep -nEi 'AreaFactor|^[[:space:]]*Physics[[:space:]]*\\{|^[[:space:]]*Electrode[[:space:]]*\\{' pp25_des.cmd | head -n 35` to check global current scaling. No rerun, no source changes. This raw current should not be labeled as physical measured current or published IQE.

## 2026-11-05 Lee Wu pp1 header and provisional planar contacts verified — OBSERVED source, paper replication blocker UNRESOLVED
- Worker 이택규 actually ran `sed -n '1,32p;80,94p' pp1_dvs.cmd` from school `/user/semi/semi437/tmp/myproject/CMP_WU_Copy` and pasted output. Header labels `CMP_BASELINE_3.2.0_WU2023PHY — PROPOSED/UNRUN` but this header is **stale** relative to observed successful n21 OFF / n25 ON 5V solver logs, so do NOT mistake old source comment for runtime status. It says source-proven Wu data only for Wmesa10um, nGaN3.9um Si5e18, 4x QW3nm In0.08, GaN barrier8nm, Mg2e19 nominal, 5nm damaged; expressly lists pGaN thickness, EBL, barrier count, electrode locations, background QB doping and Mg substitutional fraction UNVERIFIED. The actual definitions include Wm10um, tP0.120um PILOT, tEBL0, ND5e18, PMgActive2e19 (nominal-to-active assumption), NBg1e15 pilot, and four QWs.
- Direct contact code comments: `Boundary contacts: provisional full-width planar Ohmic geometry only!` and `original Wu electrode sizes/placements must be sourced before freeze`. `sdegeo:define-contact-set "anode"/"cathode" 4.0 ...` defines visualization contact sets; its 4.0 must NOT be misread as 4um mesa width or physics AreaFactor. `for-each (seg-list)` sets anode via `find-edge-id(position 0.0 ymid 0)` and cathode via `find-edge-id(position Xend ymid 0)` for each DmgL, Clean, DmgR y section, supporting full-width planar boundary contacts (subject to generated geometry verification). This is NOT evidence that original Wu Fig1 electrode is modeled.
- External corroboration: official publisher Wu 2023 `https://www.sciencedirect.com/science/article/pii/S2773012323000390` states sidewall trap depletion/lateral current dispersion and a separately proposed C-shaped anode, and disclosed methods from 10um width/nGaN3.9um/QW xIn0.08 3nm/ GaN barriers 8nm; publisher text available so far does NOT identify Fig1 exact basic-contact geometry or pGaN thickness/EBL. Do NOT equate proposed C-shaped anode automatically with Fig1 basic anode.
- SCIENTIFIC GATE: current school Wu model remains a distinct 10um pilot; NOT protected Kou-based 4um Common Baseline, not publication-accurate Wu replica, not yet normalized 2D current density/J or validated trap-inclusive IQE. NEXT READ ONLY inspect `pp25_des.cmd` actual AreaFactor and `n25_des.log` electrode area factors and last terminal current; then determine whether defensible current-density conversion is possible. No rerun, no source edit, preserve canceled hGap.

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

## 2026-11-04 — Wu pp25 22-region trap settings verified (OBSERVED)
- 이택규 actual school `CMP_WU_Copy/pp25_des.cmd` grep: all 22 DmgL/DmgR sidewall region trap blocks (pGaN, Barrier0–4, QW1–4, nGaN) share `Acceptor Level FromValBand EnergyMid=0.75`, `Conc=1e18`, `eXsection=1e-15`, `hXsection=1e-15`, `PooleFrenkel`. This verifies declared settings, not every output value or paper fidelity. No new simulation/code edit. Duplicate pasted grep command caused a harmless missing file error, but subsequent correct matches listed all 22.
- NEXT: review actual T-2022.03 e/h trap versus SRH accounting; 12-QW 5V proxy is not validated IQE. Preserve n21/n25 and do not restart canceled hGap rerun. Issue #7 comment 6625502078.

## 2026-11-04 — Lee Wu actual pp25 Physics/Trap grep and remaining validation gates (OBSERVED / UNRESOLVED)
- Worker 이택규; direct school CMP_WU_Copy command: `grep -nEi '^[[:space:]]*Physics|Recombination[[:space:]]*\(|Traps[[:space:]]*\(|PooleFrenkel|Tunneling|TrapFilling|AreaFactor' pp25_des.cmd | head -n 90`.
- OBSERVED: `Physics {` line22, global `Recombination( SRH Radiative Auger )` line27; 22 separate regional `Physics (Region="DmgL/R_*") { Traps( ... PooleFrenkel)` groups for pGaN, Barrier0..4, QW1..4, nGaN (11 left/right pairs). Representative lines DmgL_QW4 163–167; DmgR_QW4 171–175. Header line7 itself states Thermionic and PooleFrenkel are motivated numerical proxies, not evidence of exact paper fidelity; full header not yet read.
- The grep output has no matched `Tunneling`, `TrapFilling`, `AreaFactor` lines, but grep is not a proof of total absence of related physics elsewhere. It does not expose complete trap type/energy/Conc/capture cross sections or establish trap net pair recombination and IQE; actual T-2022.03 manual remains unverified in current context.
- Current gate: distinguish bulk `SRHRecombination` from explicit trap e/h rates, validate full trap spec and electron-versus-hole net accounting, ensure reportable QW-only proxy vs physical IQE, and assess Wu approximation and QW4 radiative concentration (~91% OFF). No new simulation, solver failure, source change or user-approved model alteration. Canceled rerun remains canceled.
- NEXT READ ONLY, one short terminal command: `sed -n '1,48p;159,177p' pp25_des.cmd` (source header, global Physics, representative QW4 trap); then if needed exact installed T-2022.03 reference and existing logs. Avoid redundant 12-QW integrations.

## 2026-11-04 — Wu Trap/SRH rate accounting literature audit and provisional IQE sensitivities (DOCUMENTED / DERIVED; NO RUN)
- Worker 이택규, ChatGPT read-only research. Historical official Synopsys Device User Guide O-2018.06, chapters 16 (SRH) and 17 (Traps), distinguishes SRH lifetime-based field and trap-level electron/hole recombination output. Official guide K-2015.06 chapter 9 rate/heat terms writes separate SRH net rate and electron/hole trap net rates. Synopsys Sentaurus Training sdevice/13.9 defines eGapStatesRecombination as electron trap recombination and hGapStatesRecombination as hole trap recombination. Sources: https://studylib.net/doc/27467177/sdevice-ug---%E5%89%AF%E6%9C%AC ; https://studylib.net/doc/27205378/synopsis-sentaurus-user-manual ; https://ghzphy.github.io/Sentaurus_Training/sd/sd_13.html .
- FINDING (DOCUMENTED, not T-2022.03 confirmed): `SRHRecombination` and explicit trap-level e/h rates are distinct model/output terms in earlier official guides, so complete overlap is not presumed; cannot equate electron trap rate alone to net electron-hole trap recombination without confirming steady-state e/h balance, relevant model options and exact installed-version definitions. Source index `CMP/references/TCAD_REFERENCE_INDEX.md` says actual T-2022.03 sdevice_ug.pdf was uploaded to another chat but is not stored in public repo. We have not inspected that original PDF here. Local school `pp21/25_des.cmd` Plot excerpt lists eGap but omits hGap. No solver rerun or source change.
- Conditional illustrative QW-only proxies from saved same-5V 12-QW totals [s^-1 um^-1]: OFF Rad 9.902518e15, SRH 6.102184e14, Auger 4.442221e15; ON Rad 9.869850e15, SRH 6.086824e14, Auger 4.424524e15, eGap 4.148388e13. Formula `Rad/(Rad+SRH+Auger)` gives OFF 66.2156216%, ON 66.2270190%; purely illustrative `Rad/(Rad+SRH+Auger+eGap)` gives ON 66.0431824%, a difference -0.172439 percentage points versus OFF 3-channel value. This is NOT validated IQE, the OFF all-QW eGap integral was not measured, other areas not included and ON hGap not saved. Electron-only trap rate may not equal net pair loss.
- NEXT (READ-ONLY) validate exact T-2022.03 reference and inspect actual Wu `pp21_des.cmd`/`pp25_des.cmd` global Physics/Traps and saved log for capture/tunneling/steady-state assumptions. Do not modify source or rerun previously canceled hGap case. Only then select supported rate equation and QW-only IQE proxy.

## 2026-11-04 — Wu n25 Trap ON 12-QW Radiative/SRH/Auger/eGap batches complete (OBSERVED / DERIVED)
- Worker 이택규, source actual SVisual screenshots from saved `CMP_WU_Copy/n25_des` (5 V); each Field Integration selected the exact 12 Clean_QW1–4 / DmgL_QW1–4 / DmgR_QW1–4 regions without composite '+' entries. Auger screenshot duplicated, counted once. Integral units for all fields: s^-1*um^-1; total domain 1.199999e-01 um2.
- n25 OBSERVED RadiativeRecombination, [QW1,QW2,QW3,QW4]:
  Clean [7.378876e11,1.065895e12,8.757452e14,8.982859e15]; DmgL [3.361238e8,5.199892e8,4.222072e11,4.297888e12]; DmgR [3.363697e8,5.197135e8,4.222218e11,4.297459e12]. SVisual Total=9.869850e15.
- n25 OBSERVED srhRecombination:
  Clean [6.387366e11,5.972817e11,1.193145e14,4.875343e14]; DmgL [3.195595e8,2.945850e8,5.846074e10,2.397133e11]; DmgR [3.195690e8,2.944301e8,5.846283e10,2.396849e11]. Total=6.086824e14.
- n25 OBSERVED AugerRecombination:
  Clean [1.542005e11,1.427702e11,2.000612e14,4.219999e15]; DmgL [6.835321e7,6.674554e7,9.525221e10,1.988205e12]; DmgR [6.842993e7,6.680390e7,9.525406e10,1.988158e12]. Total=4.424524e15.
- n25 OBSERVED eGapStatesRecombination:
  Clean [0,0,0,0]; DmgL [6.802490e11,6.973104e11,5.709345e12,1.365525e13]; DmgR [6.804959e11,6.975201e11,5.709368e12,1.365435e13]. Total=4.148388e13.
- Prior n21 OBSERVED totals: Radiative 9.902518e15; SRH 6.102184e14; Auger 4.442221e15. n21 eGapStates total over all 12 QW regions has NOT been sampled (only DmgL/R_QW4 individually). DERIVED displayed-total change percentages n25 ON vs n21 OFF: Radiative -0.329896%, SRH -0.251713%, Auger -0.398382%. n25 eGapStates QW distribution shares: QW1 3.2802%, QW2 3.3623%, QW3 27.5257%, QW4 65.8318%.
- These are 5-V comparisons of 12-QW saved field integrals, not whole-device recombination sums, calibrated current density, measured IQE or full trap-mediated loss. `SRHRecombination` vs `eGapStatesRecombination` overlap/definitions, `hGapStatesRecombination` absence, and other non-QW recombination remain unresolved. No new solver execution or code modifications. NEXT prioritize authoritative T-2022.03 rate-field definitions and non-double-counting audit; then decide supported conditional IQE proxy, with no previously canceled overnight hGap rerun.

## 2026-11-04 — Lee Wu n21 12-QW SRH and Auger field integrations completed (OBSERVED / DERIVED)
- Worker: 이택규. SVisual screenshots of saved `CMP_WU_Copy/n21_des` Trap OFF (5 V); selected 12 non-composite QW regions Clean_QW1..4, DmgL_QW1..4, DmgR_QW1..4, no "+" unions.
- OBSERVED `srhRecombination` integrals [s^-1*um^-1], by QW1/QW2/QW3/QW4:
  - Clean: 6.418660e11 / 6.053790e11 / 1.200834e14 / 4.882756e14
  - DmgL: 3.211880e8 / 3.029955e8 / 6.041855e10 / 2.450705e11
  - DmgR: 3.211945e8 / 3.028743e8 / 6.042168e10 / 2.450456e11
  - SVisual Total Integral=6.102184e14 [s^-1*um^-1]; Total Domain approximately 1.199999e-01 um2.
- OBSERVED `AugerRecombination` integrals [s^-1*um^-1], QW1..4:
  - Clean: 1.544212e11 / 1.440866e11 / 2.027492e14 / 4.234775e15
  - DmgL: 7.726844e7 / 7.095381e7 / 1.022639e11 / 2.096926e12
  - DmgR: 7.727060e7 / 7.099971e7 / 1.022650e11 / 2.096875e12
  - SVisual Total Integral=4.442221e15 [s^-1*um^-1]; total domain not fully visible in Auger screenshot.
- Previously n21 12-QW `RadiativeRecombination` SVisual Total Integral=9.902518e15 [s^-1*um^-1].
- DERIVED (using rounded region values): QW4 share SRH = 80.09684%; Auger = 95.42453%; Radiative = 91.03408%. These fractions describe spatial distribution of each saved rate field, not IQE. No valid trap-inclusive IQE yet: SRH/eGap overlap, missing hGapStates, full rate accounting and current normalization unresolved.
- User requested efficient workflow: n21 Radiative/SRH/Auger 12-QW batches now finished; next switch to n25 ON once and repeat three fields over exact same 12 QW regions, preserving existing n25 DmgL_QW4 measurements.
- No new SDevice run or code edit; canceled optional hGapStates rerun remains canceled.

## 2026-11-04 — Lee Wu n21 12 QW region RadiativeRecombination batch (OBSERVED, DERIVED)
- Worker: 이택규. School SVisual n21_des Trap OFF (5 V) Field Integration RadiativeRecombination, 12 *distinct* regions (Clean/DmgL/DmgR QW1–4; no composite '+' regions).
- OBSERVED integrals [s^-1*um^-1] by QW, in Clean / DmgL / DmgR order:
  - QW1: 7.388587e11 / 3.697408e8 / 3.697496e8
  - QW2: 1.079961e12 / 5.392654e8 / 5.390042e8
  - QW3: 8.851380e14 / 4.465055e11 / 4.465253e11
  - QW4: 9.005734e15 / 4.466154e12 / 4.465761e12
- OBSERVED Total Integral 9.902518e15 [s^-1*um^-1], Total Domain 1.199999e-01 um2. Displayed clean domain areas near 2.997e-02 um2 each and each damaged area near 1.5e-05 um2.
- DERIVED using displayed rounded regional values: summed 9.90251758326e15 s^-1 um^-1; QW4 sum 9.014665915e15; QW4 share 91.03408% and QW3 share 8.94753%. These are fractions of integrated *radiative field over all twelve QWs*, NOT IQE. Wu model is distinct from prior V2.1 baseline with its own QW4 concentration observation.
- No rerun/source edit. User asked to complete saved n21 before switching to n25; next batch n21 srhRecombination in same 12 distinct regions, then AugerRecombination, followed by corresponding n25. Before any IQE interpret rate overlap/term definitions and missing hGapStates.

## 2026-11-04 — Wu n21 OFF DmgL_QW4 RadiativeRecombination (OBSERVED / DERIVED)
- Worker 이택규; saved school SVisual n21_des (Trap OFF), RadiativeRecombination for DmgL_QW4 only: Integral +4.466154e12 [s^-1*um^-1], Domain 1.500003e-05 [um^2]. Earlier n25_des Trap ON identical region/field: +4.297888e12, same Domain. DERIVED ON-OFF=-1.68266e11, relative ON change -3.77% versus OFF at 5 V. This is a single-region radiative-field change, not IQE. No simulation or code modifications. User requested efficient data collection: finish remaining n21 saved-file fields before switching back to n25. Next collect per-region n21 radiative integrals for exact QW regions using multi-select, not combined region names containing '+'.

## 2026-11-04 — Wu ON n25 DmgL_QW4 radiative field integration (OBSERVED)
- Worker: 이택규. School SVisual saved n25_des (Trap ON, 5 V), Field RadiativeRecombination, selected only DmgL_QW4 (InGaN): Integral +4.297888e12 s^-1 um^-1, Domain 1.500003e-05 um2 (screenshot).
- Same saved dataset/region previously: srhRecombination +2.397133e11 and eGapStatesRecombination +1.365525e13 s^-1 um^-1. These are three separately displayed output fields; valid total recombination and double-counting rules are NOT yet established, so no IQE or trap-loss percentage should be derived from their naive sum.
- No new simulation, code change or experimental physics interpretation. NEXT read-only measure n21 OFF RadiativeRecombination for DmgL_QW4 at saved 5 V; then verify rate term definitions and validity of any IQE accounting.

## 2026-11-04 — Lee Wu n21 OFF versus n25 ON DmgL_QW4 SRH field (OBSERVED / DERIVED)
- Worker: 이택규. Direct school SVisual screenshot: saved n21_des (Trap OFF), Field srhRecombination, DmgL_QW4 only; Integral +2.450705e11 s^-1 um^-1, Domain 1.500003e-05 um2. Earlier screenshot of saved n25_des (Trap ON), same field/region/domain: +2.397133e11 s^-1 um^-1.
- DERIVED ON minus OFF = -5.3572e9 s^-1 um^-1, relative to OFF about -2.186%. This is a lower displayed SRH field integral at fixed 5.0 V, not evidence that total nonradiative recombination or trap-mediated IQE loss decreased. In this same region the eGapStatesRecombination field changes from about 1.387832e-05 OFF to 1.365525e13 ON; field overlap and complete hole-trap contribution remain unresolved.
- Both were saved 5-V results; n21/n25 anode total currents differ approximately 0.0856%. No new solver run or code edit. NEXT read-only check official T-2022.03 definitions of SRHRecombination and eGapStatesRecombination and identify double-counting risks; use saved Radiative/Auger fields if needed, do not compute IQE from unverified sums or rerun the canceled case.

## 2026-11-04 — Wu n25 ON DmgL_QW4 srhRecombination integral (OBSERVED / DERIVED)
- 이택규 SVisual Field Integration screenshot of existing CMP_WU_Copy/n25_des: field `srhRecombination`, only region `DmgL_QW4 (InGaN)` selected. Integral +2.397133e11 s^-1 um^-1, Domain 1.500003e-05 um2 (OBSERVED).
- In the same saved dataset/region, prior `eGapStatesRecombination` Integral was +1.365525e13 s^-1 um^-1. Their numerical ratio is approximately 56.96 (DERIVED), but field definitions and overlap are unverified. Do NOT assert trap physical loss exceeds SRH by 57x or sum them into IQE without accounting verification. No new solver run or code change.
- NEXT read-only compare n21_des (Trap OFF) `srhRecombination` in DmgL_QW4 using same Field Integration, then consult T-2022.03 references for field meanings and double-counting before computing IQE.

## 2026-11-04 — Wu OFF/ON QW4 left/right eGapStates comparison complete (OBSERVED / DERIVED)
- Worker: 이택규. School SVisual saved n21_des screenshot: eGapStatesRecombination, DmgR_QW4 (InGaN) exclusively selected; integral +1.387717e-05 s^-1 um^-1, domain 1.500037e-05 um2. This is the OFF/right measurement, not a rerun.
- Prior saved n21 OFF/left DmgL_QW4: +1.387832e-05, domain 1.500003e-05. Prior n25 ON/left: +1.365525e13, same left domain; ON/right: +1.365435e13, same right domain. All integrals in s^-1 um^-1.
- DERIVED left+right OFF sum 2.775549e-05, ON sum 2.730960e13 s^-1 um^-1. ON values much larger, both left/right similar. ON/OFF ratios are unstable physical metrics because OFF is extremely close to zero. This eGapStates field alone is NOT total net trap recombination or trap-inclusive IQE; do not infer IQE drop or add to SRH without validating definitions and double counting.
- QW4 bilateral sampled comparison finished; no new solver run or code edits. NEXT read-only examine actual saved SRH/Radiative/Auger rate integrals, bias and the physical model definitions. Respect cancellation of overnight hGap rerun. Keep n21/n25 intact.

## 2026-11-04 — Wu OFF n21 left QW4 eGapStates integral (OBSERVED / DERIVED)
- Worker 이택규. School SVisual screenshot saved n21_des Trap OFF, eGapStatesRecombination, exclusively DmgL_QW4 (InGaN): Integral +1.387832e-05 s^-1 um^-1 and Domain 1.500003e-05 um2.
- Prior ON n25 same selected DmgL_QW4: +1.365525e13 s^-1 um^-1 and identical Domain. DERIVED ON/OFF about 9.84e17 times, but OFF is a tiny nonzero value and multiplier does NOT represent measured IQE deterioration or full trap nonradiative recombination.
- Prior screenshot ON right QW4: DmgR_QW4 Integral +1.365435e13 s^-1 um^-1, Domain 1.500037e-05 um2. QW4 sides ON sum 2.730960e13 s^-1 um^-1, with 0.00659 percent left-right difference in integrals.
- No SDevice rerun or code edits. Next n21 OFF DmgR_QW4 read-only, then total rate accounting and double-counting verification before IQE.

## 2026-11-04 — Lee Wu n25 DmgL_QW4 eGapStates integration (OBSERVED)
- Worker 이택규. Screenshot SVisual n25_des, Field eGapStatesRecombination, only DmgL_QW4 selected: Integral +1.365525e13 s^-1 um^-1; Domain 1.500003e-05 um2. Prior Clean_QW4 same field integral 0. Positive left-side damaged-region electron gap-state recombination integral observed, but not proof of whole trap nonradiative loss or IQE. No new simulations or code changes. Next read-only measure DmgR_QW4 in same saved n25 TDR.

## 2026-11-04 — Lee Wu pp21/pp25 Plot and Math block spot check (OBSERVED)
- Worker: 이택규. School CMP_WU_Copy terminal `sed -n '210,230p' pp21_des.cmd` and `sed -n '210,230p' pp25_des.cmd` provided directly. Two excerpts are text-identical: `Plot` lists eDensity/hDensity, potentials, currents, quasi-Fermi/bands, doping, and RadiativeRecombination, SRHRecombination, AugerRecombination, eGapStatesRecombination, eTrappedCharge, TotalTrapConcentration. `hGapStatesRecombination` is not in the Plot block. Visible Math block parameters are also identical through `NotDamped=100`; no claim about omitted Math lines.
- This proves identical output requests for selected fields and shown solver Math settings, not that every requested field was written to each saved TDR, nor that eGapStates equals full trap net recombination or is nonoverlapping with SRH. Previous command/parameter comparisons still need physical interpretation.
- Next OBSERVATION: inspect already saved n25_des.tdr in SVisual, choose eGapStatesRecombination, Field Integration only DmgL_QW4, capture Integral/Domain/units and sign. No rerun or source changes; do not calculate trap-inclusive IQE before rate accounting verification.

## 2026-11-04 — Lee Wu recombination Plot declarations inspected (OBSERVED, read-only)
- Worker 이택규. User school `grep -niE 'eGapStatesRecombination|hGapStatesRecombination|SRHRecombination|RadiativeRecombination|AugerRecombination|CurrentPlot|Integr' pp21_des.cmd pp25_des.cmd | head -n 80` in CMP_WU_Copy.
- OBSERVED: both preprocessed CMDs line 218: `RadiativeRecombination SRHRecombination AugerRecombination`; line 219: `eGapStatesRecombination eTrappedCharge TotalTrapConcentration`. No `hGapStatesRecombination`, `CurrentPlot`, or `Integr*` appeared in the grep output. Both have the same listed rate output requests, but this does not itself confirm each field exists in saved TDR or establish correct recombination accounting.
- INTERPRETATION: `eGapStatesRecombination` alone must not be treated as full trap-inclusive nonradiative loss; `SRHRecombination` plus `eGapStatesRecombination` may not be summed for an IQE calculation until definitions and double-counting are verified. No school rerun or code change. Respect cancellation of extra hGap rerun.
- NEXT read-only: inspect full Plot block context and saved n21/n25 TDR fields in SVisual. Identify availability/units before region-integrating and assessing trap contributions, with no code changes.

## 2026-11-04 — Lee Wu n21/n25 5.0 V PLT final-row current comparison (OBSERVED / DERIVED)
- Worker: 이택규. Direct school CMP_WU_Copy terminal evidence: `tail -n 12 n21_des.plt`, `tail -n 12 n25_des.plt`. Both files end at `time=1` and `anode OuterVoltage=5.00000000000000 V` with 17-column DF-ISE datasets including time and anode/cathode terminal values.
- OBSERVED OFF n21 (5 V): anode TotalCurrent=2.56859586549120e-03, eCurrent=1.69539310159551e-04, hCurrent=2.39905655533165e-03; corresponding cathode TotalCurrent=-2.56859586549119e-03.
- OBSERVED ON n25 (5 V): anode TotalCurrent=2.56639709344131e-03, eCurrent=1.68952709999954e-04, hCurrent=2.39744438344136e-03; corresponding cathode TotalCurrent=-2.56639709344130e-03.
- DERIVED: 5V fixed-voltage absolute TotalCurrent reduction OFF-ON=2.19877204989e-6, relative reduction 100*(OFF-ON)/OFF=0.085602%. Data are raw 2D PLT terminal-current numbers; physical current-density scaling/units not validated. 5 V near-equal current is not an exact matched-current extraction, and low total-current change does not validate IQE or trap-mediated recombination.
- PLT dataset list lacks recombination integrals (IntegrRad, IntegrSRH, IntegrTrap). Further rate accounting needs saved TDR and authoritative definitions. No new runs, no source edits. Respect JuSubin's cancellation of an overnight hGap rerun; next is read-only review of existing fields and recombination definitions.

## 2026-11-04 — Lee Wu n21/n25 PLT headers verified (OBSERVED; read-only)
- Worker: 이택규. Actual school shell in CMP_WU_Copy: `ls -lh n21_des.plt n25_des.plt; head -n 15 n21_des.plt; head -n 15 n25_des.plt`.
- OBSERVED: n21_des.plt exists (41K, Nov 3 23:58); n25_des.plt exists (70K, Nov 4 01:00). Both are DF-ISE text xyplot with the visible complete `datasets` list of time, cathode/anode voltage, potentials, displacement/electron/hole/total currents, and charge. Neither listed recombination integration columns such as IntegrRad/IntegrSRH/IntegrTrap in its displayed dataset header.
- INTERPRETATION: these PLTs can support inspection of bias and terminal currents, but alone cannot provide trap-inclusive IQE or recombination-rate decomposition. No simulation rerun, source edit, current values, or current-overlap proof in this step.
- NEXT: inspect saved PLT ending/data syntax and terminal current-vs-voltage overlap read-only, then source recombination integrals from saved TDR/other verified datasets. Keep original files unchanged.

## 2026-11-04 Lee Wu right Barrier4 observation
- User SVisual n25 ON TotalTrapConcentration, DmgR_Barrier4: Integral 3.996092e+01 um^-1, Domain 4.000092e-05 um2. Mean 9.990e17 cm^-3 (about 0.1 percent below ON nominal 1e18). Left Barrier4 had similar average. Representative QW1/QW4 left and right traps and clean QW centers had already been checked. This is not a complete IQE or full 22-region uniformity proof. No new runs or source edits. Next investigate recombination accounting and trap-inclusive IQE with saved data only.

## 2026-11-04 — Lee Wu n25 DmgL_Barrier4 trap regional mean (OBSERVED / DERIVED)
- Worker: 이택규. Saved `CMP_WU_Copy/n25_des` Field Integration screenshot, `TotalTrapConcentration` selected only `DmgL_Barrier4 (GaN)`. OBSERVED Integral = `3.996001e+01 [um^-1]`, Domain = `4.000001e-05 [um^2]`. DERIVED regional mean = (39.96001 / 4.000001e-5) * 1e12 = approx `9.990e17 cm^-3`, 0.1% below nominal ON NtSide=1e18 cm^-3. Reason for difference NOT confirmed; avoid exact-equality claims.
- The ON left Barrier4 has near-target local average trap concentration, extending prior QW1/QW4 trap spot checks. This does NOT prove within-region uniformity, all 22 regions, or trap-inclusive IQE. No solver rerun or school code edit.
- NEXT read-only: saved n25 DmgR_Barrier4 regional Integral/Domain; afterward stop repetitive trap placement checks and focus on trap vs SRH rate accounting and current normalization.

## 2026-11-04 — Lee Wu n25 Clean_QW4 trap concentration zero (OBSERVED / DERIVED)
- Worker: 이택규. Screenshot of school saved `CMP_WU_Copy/n25_des` Field Integration, `TotalTrapConcentration`, only `Clean_QW4 (InGaN)` selected. Integral = **0.000000e+00 [um^-1]**; Domain = **2.997006e-02 [um^2]**. Regional mean = 0 cm^-3.
- Alongside previously measured `DmgL_QW4` mean=1e18 and `DmgR_QW4` mean=1e18 cm^-3, the measured **QW4 left-damaged / clean-center / right-damaged regional averages** match the intended ON trap placement. Earlier QW1 left/right and clean spot checks agree. Other damaged layers, within-region uniformity and full trap-inclusive IQE remain unverified.
- No school code edit or SDevice rerun. Next saved n25 `DmgL_Barrier4` and `DmgR_Barrier4` spot checks (if still needed), then focus on rate accounting, matched-current and model fidelity.

## 2026-11-04 — Lee Wu ON DmgR_QW4 trap density checked (OBSERVED / DERIVED)
- Worker: 이택규. Actual saved `CMP_WU_Copy/n25_des` SVisual Field Integration, Field `TotalTrapConcentration`, selected region `DmgR_QW4 (InGaN)`. Screenshot shows Integral=1.500037e+01 [um^-1], Domain=1.500037e-05 [um^2]. Mean = 15.00037 / 0.00001500037 = 1e6 [um^-3] = **1e18 cm^-3**, matching ON NtSide. Earlier DmgL_QW4 region also 1e18 cm^-3; both left and right QW4 regional averages verified. This does NOT establish uniformity inside each region, all 22 damaged regions, recombination loss, or trap-inclusive IQE.
- No rerun or school code edit. NEXT read-only `Clean_QW4` in same n25 TotalTrapConcentration to confirm clean center vs both sidewalls; then sample Barrier4 and review trap-rate accounting.

## 2026-11-04 — Lee Wu Trap ON DmgL_QW4 average Nt verified in saved SVisual (OBSERVED / DERIVED)
- Worker 이택규, school saved `CMP_WU_Copy/n25_des` Trap ON. User screenshot of Sentaurus Field Integration: Field `TotalTrapConcentration`, only Region `DmgL_QW4 (InGaN)` selected. OBSERVED Integral = 1.500003e+01 [um^-1]; Domain = 1.500003e-05 [um^2].
- DERIVED mean = 15.00003 / 1.500003e-5 = 1.000000e6 um^-3 = **1.000000e18 cm^-3**, consistent with target `NtSide=1e18`. This extends earlier direct ON QW1 left/right region checks to ON QW4 LEFT. It is an area-average; no proof of region-wise uniformity beyond this average. QW4 right / clean and Barrier4 remain unmeasured in this turn. This is trap CONCENTRATION evidence, not proof of trap-caused net recombination or complete IQE.
- No SDevice rerun, input edit or output modification. NEXT read-only SVisual saved n25 `DmgR_QW4` `TotalTrapConcentration` Integral/Domain; optionally `Clean_QW4` and `DmgL/R_Barrier4` before moving to rate accounting.

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

2026-11-03 (Claude 독립 검토, 새 실행 없음) PolAct=0 결과 판정과 Baseline/Project A 결정
- 유효성 단서: POL0NOSHELF는 GPT 전체 SDevice 코드를 붙여 넣은 덱(activation 줄이 원본 21행 → 새 22행). 원본 대비 pp/par/메시 diff 미실시 → 단일 변수 실험으로 확정 불가. 아래 판정은 조건부.
- 조건부 판정: 분극은 주입·Vf를 지배(3.6V 전류 132x/493x, J≈240/227 A/cm2)하지만 QW4 집중의 필요조건은 아님(99.89/99.96%). 우물 간 감소비 OFF: QW3/QW4 1.1e-3, QW2/QW3 2.3e-2, QW1/QW2 1.7e-2(DERIVED).
- H1(분극이 분포 원인): 대부분 반증(조건부). H1(분극이 Vf 원인): 강하게 지지. H2(고전 DD): 강화됐지만 직접 검증 없음. 구체화 가설: 양자 보정 없는 고전 DD가 3 nm 우물의 전자 깊이를 과대평가(ΔEc≈0.41 eV) → 첫 우물 포획.
- 정정: 11/02 Claude 문턱값(1%, 80%, ±25%)은 작업 기준이지 물리값 아님. 분포가 안 바뀌었으므로 ±25% 비교는 "QW 분포 민감도"가 아니라 "분극·Vf 민감도"만 시험함.
- 같은 전압 Trap 손실(POL0 3.3% vs PolAct0.5 약 34%)은 전류가 100배 이상 달라 비교 불가 → 같은 전류 비교 필수.
- 권고: 선택지 B(제한사항 명시, PolAct 0.5 임시 Baseline으로 Project A 병행). Project A = CONDITIONAL GO: 덱 준비는 지금, 해석·보고는 (1) 유효성 게이트 통과 (2) 같은 전류 Trap 손실이 PolAct 0.5/0에서 같은 부호·±25% 이내 (3) QW4 집중을 모델 한계로 명시 후.
- 다음 하나: 유효성 게이트(읽기 전용, bash): 메시 md5, pp1_dvs diff, pp2/pp6 par diff, pp2/pp6 cmd diff -w -B. 통과 시 polact_compare.py로 같은 전류 비교(우물 간 감소비, IQE_sim, Trap 손실).
- 나중(승인 필요): H2 직접 시험으로 밴드 오프셋 비율 단일 변수. FREEZE HOLD, 판정 B 유지.

## 2026-11-03 — PolAct=0 both PLTs parsed: QW4 still >99.88% while current rises strongly (OBSERVED + DERIVED)
- **작업자:** 이택규. **Source:** user pasted real Bash/Python DF-ISE `n2_des.plt`/`n6_des.plt` final-row extraction in `/user/semi/semi437/CMP_BASELINE_2.1.0_POL0NOSHELF` (2026-11-03, pp previously verified `activation=0`, global Iterations12, both runs finished). Final `anode OuterVoltage=3.600000 V` for both.
- **OBSERVED PolAct=0, Trap OFF n2:** native anode current `4.80713937e-06`; total QW integrated radiative rates: QW1 `7.53686944e18`, QW2 `4.48979847e20`, QW3 `1.98055890e22`, QW4 `1.82316579e25`; QW4 fraction `99.88898644%`.
- **OBSERVED PolAct=0, Trap ON n6:** native anode current `4.54183989e-06`; rates: QW1 `4.28900936e17`, QW2 `5.25004116e19`, QW3 `5.92590845e21`, QW4 `1.66646275e25`; QW4 fraction `99.96413545%`.
- **OLD OBSERVED reference:** original PolAct=0.5 3.6V n2 current `3.64728524885323e-08`, QW4 share `99.96877481383976%`; n6 current `9.21970771341943e-09`, share `99.99294273758203%` (prior 2026-10-31 PLT audit).
- **DERIVED at same voltage, NOT matched current:** change QW4 share n2 `-0.07978837384 percentage points`, n6 `-0.02880728758 pp`; current ratios n2 `131.8004774×`, n6 `492.6229802×`. Formula QW4 share = 100×QW4 Rad / sum(QW1..QW4 Rad). PolAct=0 changes total transport/current dramatically yet QW4 radiative localization remains >99.88%: simple 'polarization-only' cause is **not supported** as sole explanation. NOT proof of classical-DD capture as root cause, since local QW1 JnX/J and matched-current distribution not yet assessed.
- **INTERPRETATION LIMITS:** `strain activation=0` is global (including EBL) and not a physical baseline. Old/new are same-V, very different-I; raw 2D current not independently calibrated as square-pixel A/cm². QW4 fraction ≠ IQE. Need fresh shelfless geometry, SDE/par/mesh, source/PP diff except polarization verified before claiming a strict one-variable sensitivity. Physical Baseline B/FREEZE HOLD; no device code changed.
- **NEXT priority:** using existing PLT histories, compare QW shares and IQE_sim proxy at **matched anode current** where interpolation overlap exists, plus verify geometry/input provenance. If no current overlap, state cannot compare. No further blind re-runs.

## 2026-11-03 — POL0NOSHELF n2 PLT DF-ISE header/footer confirmed (OBSERVED READ ONLY)
- 이택규 사용자 제공 학교 서버 출력, 현재 Bash 셸에서 `/user/semi/semi437/CMP_BASELINE_2.1.0_POL0NOSHELF` 경로로 이동한 뒤 `head -n 28 n2_des.plt; tail -n 8 n2_des.plt` 성공. `DF-ISE text`, `Info {type=xyplot, datasets=[...]}` 구문과 마지막 데이터 구간 `Data` 숫자 및 `}` 닫힘 확인.
- 헤더에 `anode OuterVoltage`, `anode TotalCurrent`, `IntegrRad_Clean_QW1`/Edge/Dmg 등 QW1–4 별 세 영역 방사재결합 필드, `IntegrSRH_*`, `IntegrAug_*`, `IntegrTrap_*` 실제 존재 확인. 이전 홈 디렉터리에서의 No such file 오류는 경로 문제였고 파일 부재나 TCAD 오류가 아니었음.
- **아직 QW1–4 비율, 전류값 미산출.** 해당 PLT의 전체 컬럼 이름과 `Data` 숫자 갯수 나눗셈이 일치하는지 검증하며 마지막 레코드 합산하도록 Bash heredoc 파서 제안. 사용자 실행 및 출력 대기. 원본 TCAD 변경 없음. Baseline physical FREEZE HOLD.

## 2026-11-03 — POL0NOSHELF Python here-document failed in tcsh prompt (OBSERVED; GPT INSTRUCTION ERROR)
- **OBSERVED:** 이택규는 `/user/semi/semi437/CMP_BASELINE_2.1.0_POL0NOSHELF` 에서 GPT가 준 `python3 - <<'PY'`와 다중행 Python 코드를 그대로 붙여넣었고, `tcsh/csh` 스타일 `?` continuation prompt가 모든 줄과 종결 `PY` 후에도 지속됨. 따라서 Python PLT 파서 **실행 완료/결과 출력 증거 없음**. 이는 SDevice solver 오류 또는 PLT 파일 손상 증거가 아님.
- **CAUSE/RESPONSIBILITY:** 과거 동일 `?`/here-doc 입력 문제를 기록했는데도 GPT가 Bash 셸 진입 확인 없이 Bash 지향 heredoc을 제공한 안내 오류. Python 구문 자체의 오류로 단정할 수 없음.
- **FIX GUIDANCE (NOT YET USER-VERIFIED):** `Ctrl+C`로 dangling shell 입력 취소, `bash` 단독 입력 후 Bash prompt를 확인. 다시 복잡한 parser를 무작정 실행하기 전에 `head -n 28 n2_des.plt; tail -n 8 n2_des.plt`로 실제 DF-ISE PLT 형태 확인하여 올바른 파서를 제공. 이후 Bash에서 heredoc 사용하거나 단순 호환 명령 제공.
- **NO TCAD CHANGE:** 기존 PolAct=0의 n2/n6 종료·pp activation=0/Iterations12 OBSERVED 상태 유지. QW 수치 아직 새로 얻지 않음.

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

## 2026-11-03 — Lee reports PolAct=0 simulation runs finished (USER-REPORTED, RESULTS UNVERIFIED)
- 작업자: 이택규. 사용자 직접 보고: "그 우리 polact 0 했던거 다 돌아갔어". 전날 shelf-free `CMP_BASELINE_2.0.0_V2`로부터 새 복사하고 PolAct=0 / SDevice Iterations=12 적용했다고 보고한 진단 시험을 가리킴.
- **검증 수준:** USER-REPORTED run completion. 현재 세션에서 학교 서버 `n2/n6` 로그/PLT, 실제 복사본 이름, shelf-free 메시 형상, 실효 pp activation=0 및 Iterations=12 직접 확인하지 못함. 정상 수렴/3.6V 도달/재결합 분포/결과 수치는 아직 미확정.
- **NEXT (read-only):** 새 프로젝트 루트에서 `pwd; ls -lh n2_des.log n6_des.log n2_des.plt n6_des.plt 2>&1; grep -iE 'finished|good bye|didn.t converge|error' n2_des.log n6_des.log | tail -25` 실행 결과 받아 완료 여부 확인. pp2/pp6의 activation=0, Iterations=12 및 shelf-free 구조를 검증한 후 0.5 대 0의 QW1–QW4 재결합 비율, 단자 전류 및 동일 전류 IQE_sim 비교.
- baseline physical FREEZE HOLD 유지. 원본 소자/코드 변경 없음.

## 2026-11-02 — Lee reports new shelf-free clone PolAct parameter change; full SDevice source requested (USER-REPORTED, PRE-RUN)
- 이택규는 잘못된 shelf-retained Copy를 중단 후 원본 V2.1 복사본의 SWB 파라미터를 변경했다고 보고; **새 복사본 코드/실효 pp/메시 검증 및 solver 실행은 미확인**.
- ChatGPT가 요청에 따라 전체 `sdevice_des.cmd` 교체용 실행 코드 전달. 기존 사용자-provided V2 입력과 이전 원본/복사본 diff에 근거하여 분극 `activation=@PolAct@`, global Math Iterations12, 나머지 물리모델/Trap/Plot/CurrentPlot/Solve 제어를 원본 V2.1과 맞춘 버전; 독립적으로 새 프로젝트 디스크 파일의 정확한 byte equivalence를 검증한 것은 아님. SWB PolAct=0이면 자동 치환되므로 별도의 polarization 키워드 수정 불필요.
- 다음: 실제 적용·shelf-free mesh·preprocessed pp 활성값/Iterations 검증 후 실행. 이전 물리 모델 판정 B/FREEZE HOLD 유지.

## 2026-11-02 — Lee halted shelf clone and duplicated intended V2.1 (USER-REPORTED PROGRESS)
- 사용자가 기존 shelf 포함 `CMP_BASELINE_2.1.0_POL0DIAG`을 멈추고, `CMP_BASELINE_2.0.0_V2_Copy`가 아닌 원본 `CMP_BASELINE_2.0.0_V2`를 다시 복사했다고 설명. 실제 SWB 새 프로젝트는 아직 rename/parameter/mesh 검증 전. 중단된 실행 결과/완료 상태 미제공, 과학적 결과 없음.
- GPT 다음 제안: 별도 이름 `CMP_BASELINE_2.1.0_POL0NOSHELF`(제안, 미확인), 원본 코드/물성 보존, 양 노드 PolAct 0.5→0 파라미터만 변경 후 Parameters 화면, shelf 없는 n1_msh, pp activation=0/Iterations=12 확인. 원본 보호, Baseline B/FREEZE HOLD.

## 2026-11-02 — Lee catches wrong shelf geometry lineage in POL0DIAG (USER-REPORTED + IMAGE; NO VALID PHYSICS RESULT)
- 이택규가 SVisual `n1_msh` 캡처 후 lateral 오른쪽 돌출 '턱'이 있음을 지적. 화면은 2um half mesa 경계를 넘어 약 2.5um까지 red n-GaN-like 영역이 연장되는 shelf-like shape (Elements=124583, Points=60163); 이런 형상은 이전 작업용 V2.1 원본 `Wshelf=0`과 맞지 않음.
- 사용자 본인 추정/설명: POL0DIAG을 제대로 된 `CMP_BASELINE_2.0.0_V2`가 아닌 예전 `CMP_BASELINE_2.0.0_V2_Copy`에서 복사한 것 같음. 기존 원본 V2.1이 shelf 제거 구조로 채택된 것은 이전 2026-10-15 보고/2026-10-22 실측 파일에 기록되어 있음. 정확한 clone SDE/mesh 경로는 아직 재검증 전.
- GPT의 앞선 '해당 mesh 정상' 주장은 **정정/철회**. PolAct 물리 변수 변경과 구조 shelf 문제는 별개. 현재 복사본을 PolAct-only one-variable 대조의 유효 실험으로 간주하지 않고 중단 권고. 새로 *올바른 원본에서* 보호 복사본 제작 및 `Wshelf=0`, 메시/실효 pp 확인 후 재시작. 기존 프로젝트 삭제/덮어쓰기 금지. 새 SDevice run completion/result 미확인.

## 2026-11-02 — POL0DIAG stored SDevice grep confirms PolAct macro and Iterations12 (OBSERVED READ ONLY; NO RUN)
- User terminal in `~/CMP_BASELINE_2.1.0_POL0DIAG` after manually pasting complete SDevice: `grep -nE 'Piezoelectric_Polarization|^[[:space:]]*Iterations[[:space:]]*=' sdevice_des.cmd` output: **line39** `Piezoelectric_Polarization( strain activation=@PolAct@ )`; **line276** `Iterations = 12`. This confirms saved SDevice source contains the macro and the restored global Math iteration count (previous copy 20 vs original 12).
- **Not yet verified:** effective new preprocessed `pp2_des.cmd` / `pp6_des.cmd` activation=0; clone SDE/PAR/mesh equivalence; original vs clone effective input diff; same-current prior IQE_sim; user threshold lock; actual solver result. No new solver run reported. Baseline B physical FREEZE HOLD.
- NEXT read-only: check whether `pp2_des.cmd`/`pp6_des.cmd` exist in new project (`ls -l`), then inspect effective activation and Iterations, using SWB preprocess-only if absent. Run not yet authorized from these checks.

## 2026-11-02 — Lee reports applying full POL0DIAG SDevice replacement with Iterations12 (USER-REPORTED; NOT VERIFIED; NO RUN)
- 이택규가 ChatGPT가 제공한 `sdevice_des.cmd` 전체 복붙 버전(기존 업로드 SDevice를 기준으로 Math `Iterations=20`을 `12`로 수정, 기타 Physics/Trap/Plot/CurrentPlot/Solve 구문 유지)을 새 `CMP_BASELINE_2.1.0_POL0DIAG` 프로젝트에 **직접 바꿨다**고 보고. 서버 실제 저장 내용, preprocessed `pp2_des.cmd`/`pp6_des.cmd`, 변경 diff는 아직 다시 관찰되지 않음.
- 기존 사용자 스크린샷에서 clone 두 SWB 행 `PolAct=0` 확인, source 매크로 `activation=@PolAct@` 존재. **No solver run/result reported**. 원본 `CMP_BASELINE_2.0.0_V2`은 변경하지 않는 통제 조건 유지, Baseline B physical FREEZE HOLD.
- NEXT READ ONLY: clone 실제 `sdevice_des.cmd`의 `Piezoelectric_Polarization`과 global `Iterations` 조회하여 저장 확인. 그 다음 SDevice preprocess/effective `activation=0`, `Iterations=12` 및 원본 대비 의도하지 않은 차이가 없는지 검증; 기존 n2/n6 .plt 동일 전류 IQE_sim 검토와 사전 해석 기준 확정 전 solver 시작 금지.

## 2026-11-02 — POL0DIAG actual source diff confirms Math 20 vs original 12 (OBSERVED / NO RUN)
- 이택규가 실제 학교 서버에서 `diff -u ~/CMP_BASELINE_2.0.0_V2/sdevice_des.cmd ~/CMP_BASELINE_2.1.0_POL0DIAG/sdevice_des.cmd` 및 clone grep을 실행해 출력 제공. 원본 global `Math Iterations=12`, 복제본 `Math Iterations=20`인 **실제 차이 확인**. 나머지 diff는 표시된 범위에서 주석/줄바꿈/압축된 Trap 블록의 포맷 차이이며, `Piezoelectric_Polarization(strain activation=@PolAct@)` 실행 구문은 양쪽 동일. 복제본 헤더의 2026-10-13 `PROPOSED / NOT RUN` 설명은 현재 원본 출처를 나타내지 않음.
- **제안(아직 미실행):** 새 프로젝트 SDevice 파일을 백업한 후 원본 `sdevice_des.cmd`를 복제본에 `cp -p`로 교체해 byte-identical `cmp` 확인. 이때 변경되는 파일은 새 복제본 SDevice뿐이고, 원본은 유지. SWB 파라미터 `PolAct=0` 유지 및 이후 pp activation=0, Iterations=12 확인 필수. 복사본 SDE/PAR/나머지 파라미터 일치 및 같은전류 IQE_sim, 기준값 lock 미완료. 새 solver run/수정 실행 증거 없음. Baseline B / FREEZE HOLD.

## 2026-11-02 — Lee uploaded SDevice candidate code: PolAct binding verified, Math iteration discrepancy (OBSERVED, NO RUN)
- User uploaded a 303-line text file presented as V2 `sdevice_des.cmd` for examination. Directly inspected: header says `Status: PROPOSED / NOT RUN (written 2026-10-13)`; executable `Piezoelectric_Polarization( strain activation=@PolAct@ )` at uploaded line 38; global `Math { Iterations = 20 }` at uploaded line 275.
- **CORROBORATION FROM PRIOR ACTUAL SERVER OUTPUT:** GitHub 2026-10-31 Lee read-only `pp2_des.cmd`, `pp6_des.cmd` both reported global `Iterations = 12` at preprocessed line 174 and effective `activation=0.5`. Therefore the uploaded text has a confirmed **20 vs 12 mismatch compared with previously observed deployed pp files**; it is NOT proven to be the presently copied project's live editable SDevice input. Do not infer new solver was run or the project changed from this pasted file.
- **CONCLUSION:** Binding syntax is already parameterized; if copied SWB `PolAct=0` is truly active, no manual polarization-line code edit is required. But before running, inspect actual original and clone `sdevice_des.cmd` and preprocessed files; confirm `Iterations=12` in clone and no unintentional changes. Do NOT blindly paste the older 2026-10-13 PROPOSED deck into clone. Baseline B / FREEZE HOLD, no new simulation.

## 2026-11-02 — Lee SWB diagnostic PolAct=0 parameter table verified by screenshot (OBSERVED, NO RUN)
- User sent SWB Parameters screenshot for copied project `CMP_BASELINE_2.1.0_POL0DIAG`, stating only PolAct changed. **Screenshot OBSERVED:** two rows; `PolAct=0` in both, row 1 `NtSide=0` (Trap OFF) and row 2 `NtSide=1e18` (Trap ON), both `Wedge=0.1`, `Bspan=0`, `NCEdge=0`, `V1=2.0`, `Vmax=3.6`; `NPlot=8` (row1), `0` (row2). This verifies displayed UI values ONLY, not original-to-copy full comparison or actual processed SDevice activation.
- New progress: PolAct displayed as zero in both SWB parameter rows. **UNVERIFIED:** whether `@PolAct@` is bound inside actual SDevice source, preprocessed `pp2_des.cmd`/`pp6_des.cmd` values, other input/PAR/SDE diff, run results, same-current IQE_sim, and Claude proposed gate adoption. No new solver execution reported.
- NEXT READ ONLY: inspect new `sdevice_des.cmd` for actual `Piezoelectric_Polarization` and activation references; verify SWB preprocessing and source/pp diff before solver. Keep source `CMP_BASELINE_2.0.0_V2` untouched, physical Baseline B/FREEZE HOLD. PolAct=0 remains diagnostic only (global EBL interface effect).

## 2026-11-02 — Lee creates manual SWB PolAct diagnostic copy (USER-REPORTED, NOT RUN)
- 이택규 보고: 학교 서버 SWB에서 기존 `CMP_BASELINE_2.0.0_V2` 프로젝트를 복사한 다음 이름을 `CMP_BASELINE_2.1.0_POL0DIAG`으로 지정하여 신규 프로젝트를 만들었음. SWB 프로젝트 실제 생성은 **사용자 보고 OBSERVED**, GPT가 서버 폴더/덱 SHA/파라미터를 직접 확인한 것은 아님.
- 현재까지 확인 가능한 범위: 프로젝트 복사 및 명명 단계. 실제 `PolAct=0` 적용, 노드/소스/물성/mesh 원본과 동일성, preprocess pp diff, 새 TCAD solver run, 결과 **미확인/NOT RUN**.
- NEXT: 복제 프로젝트 SWB Parameters 표에서 `PolAct` 기존 0.5 → 0만 변경하고 `NtSide` 등 타 변수를 보존하는지 화면으로 확인. 실행 전 원본/복사본 입력 및 pp diff, 기존 n2/n6 동일 전류 IQE_sim, 사전 판정 게이트를 확인. 원본 `CMP_BASELINE_2.0.0_V2` 보호; Baseline B/FREEZE HOLD 유지.

## 2026-11-02 — Claude 독립 의사결정 기록 (사용자 전달 원문; NO RUN)

2026-11-02 밤 (Claude 독립 의사결정, 새 실행 없음) V2.1 Baseline 판정과 다음 작업
- 판정 B 유지: 수치 일관성(2D A/um UG p.58/120, 재결합 수지 99.999%, ΔJn=q∫R 99.99%, Rad/np=2e-11 QW1=QW4, x=0.15) 충족. MQW 캐리어 분포는 물리 미검증. 정상 선언도 폐기도 아님.
- 분극 크기(DERIVED): QW Px +8.216e-7, 장벽 Px +3.4e-6 C/cm2, UG 식1085 q_PE=-activation·∇P → 우물 계면 sheet ≈ 0.5×2.578e-6/q ≈ 8.0e12 cm^-2, 부호 Ga-polar 일치. MaterialDB 상속 추적 중단 권고(런타임 값이 출력 Px로 결정됨).
- 직접 원인(OBSERVED): QW1 중심 JnX 8.85e-5 = 전체 1.82 A/cm2의 0.005%. 전자는 QW4를 거의 못 넘고 정공은 QW4까지 전 전류 운반 → 만나는 곳이 QW4뿐. 실험 경향(정공 병목, p쪽 발광)과 반대.
- 기전(가설): H1 분극 sheet 8e12가 장벽 전도대 상승 / H2 고전 DD 즉시 포획 + 70:30 오프셋으로 깊은 전자 우물. 미구분.
- 결정: 선택지 B. 보호 복사본에서 PolAct 0.5→0 단일 변수, n2·n6 조건 두 노드(여력 없으면 n2 먼저). 주의: global activation이라 EBL 계면 전하도 0이 됨. PolAct=0은 진단용, Baseline 후보 아님.
- 판정 기준(Claude 작업 기준): QW1 JnX/J ≥1% & QW4<80% → 분극 주원인 / JnX/J<0.1% & QW4>99% → 고전 DD 포획 주원인.
- Project A 진행 조건: 동일 전류 IQE_sim의 Trap 감소율이 PolAct 0.5와 0에서 같은 부호, 상대 차이 사전 허용범위(제안 ±25%) 이내 → 제한사항 명시 임시 Baseline(C)으로 진행. QW 분포·절대 IQE·Vf는 주장 금지. Project B는 별도 확인.
- 실행 전 읽기 전용 2개: (1) 기존 n2/n6 plt로 동일 전류 IQE_sim (2) 복사본 pp diff가 21행뿐인지.
- FREEZE HOLD 유지.

## 2026-11-02 — Lee requests independent Claude decision review before next TCAD run (HANDOFF PROPOSED, NO RUN)
- Worker Lee requested a concise independent Claude reassessment because extensive read-only QW4 audits have become repetitive. ChatGPT proposes STOP additional data-gathering for now, classify physically-verified vs unexplained evidence, and request Claude to decide whether a single controlled sensitivity test is actually informative and whether provisional Project A work can proceed.
- Evidence already available: n2 QW4 fraction of four QW radiative ~99.9688%; n6 ~99.9929% (not IQE). Existing n2 3.6V Y=1um QW1 vs QW4 pointwise n ratio~208.95, p ratio~481.26, n*p~100558; Rad/(n*p) both ~2e-11 cm3/s. Fine CSV electron-current-versus-q-integrated-recombination consistency QW1~99.9994% and QW4~99.9921% across well+adjacent barrier ranges. QW4 focusing causal physics remains unresolved. B2 broad-window ΔeQF=0.25042766eV cannot alone prove bottleneck.
- PROPOSED Claude independent review, NOT YET SENT: Read live GitHub state/protocol, independently triage hypothesis/data gaps, state minimal go/no-go physical validity requirements for Project A, critique candidate protected-copy n2 same-mesh Trap-OFF interface-polarization activation 0.5→0 diagnostic and its interpretation, propose at most one decisive authorized run with predeclared metrics. No authorization for any new simulation, baseline modification, or suggested Claude result. Baseline B physical FREEZE HOLD.

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

## 2026-11-02 — InN piezo coordinate transform documentation inspected (OBSERVED; NO RUN)
- 이택규 user-pasted installed T-2022.03 MaterialDB/InN.par lines 570–600 (read-only): documentation says stress tensor is transformed from stress-system to crystal-system, polarization computed using strain/stress model, then polarization vector transformed crystal-system to simulation-system. Excerpt displays an illustrative LatticeParameters example, NOT n2-specific active geometry; previous source-based n2 LatticeParameters X=(0,0,-1), Y=(1,0,0) must be used for interpreting Px sign.
- These lines do NOT contain a numerical Piezoelectric_Polarization formula assignment; previous suggestion to read 570–600 for formula was incorrect. Do not conclude formula absent from all InN.par or infer active model solely from sample documentation.
- NEXT READ ONLY inspect assignments within actual InN.par Piezoelectric_Polarization block lines 525–645 (formula, a0, a, relax) with line numbers. If no explicit formula, verify installed T-2022.03 default/model source before quantitative InGaN polarization prediction. No simulator run, no source/library edits; QW4 localization cause UNRESOLVED, Baseline B FREEZE HOLD.

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

## 2026-11-02 — Lee T-2022.03 GaN polarization coefficients confirmed; InGaN still open (OBSERVED, NO NEW RUN)
- OBSERVED USER SERVER grep (read only, no solver run): GaN.par Piezoelectric_Polarization block lines 793–869: formula=1 (793), relax=0.0 (795), psp_z=-3.4000e-06 C/cm^2 (820), e31=-5.2740e-05 C/cm^2 (861), e33=+8.9460e-05 C/cm^2 (863), piezo block a0=3.189 Å and a=3.189 Å (868–869). Distinguish from other GaN.par a0 lines 366/428 outside this block and unrelated model formula 1,1 line530. InGaN.par output only a0(0)=3.5480e-10 m (270), a0(1)=3.1890e-10 m (271), formula=2,2 (356; owning model block NOT established); grep yielded no anchored psp_z/e31/e33/relax assignments for InGaN. This does NOT prove InGaN lacks effective polarization coefficients or that formula=2,2 is polarization formula. AlGaN.par previously observed polar formula=1/relax=0 and psp_z(0)=-3.4e-06 etc.
- DERIVED / LIMITED: archived n2 3.6V GaN barrier center Px=+3.4e-06 C/cm^2 has same magnitude as GaN.par psp_z=-3.4e-06 and sign is compatible with source lattice orientation X=(0,0,-1); this supports but does not independently prove effective runtime coefficient origin or all interface sheet charges. QW1–4 center Px previously matched +8.2162955e-07 and xMoleFraction 0.15, so a QW4-only DIFFERENT BULK polarization coefficient is not supported by center data. Physical QW4 ~99.97% radiative concentration causality remains UNRESOLVED. Baseline verdict B, physical FREEZE HOLD, no source/library edits.
- NEXT READ ONLY: inspect complete InGaN.par context to determine whether Piezoelectric_Polarization block/psp/e31/e33 data actually exist and how InGaN coefficients are inherited/interpolated; suggested grep -nEi -C 2 'Piezoelectric_Polarization|psp_|relax|e31|e33|d31|d33' .../MaterialDB/InGaN.par (no head) and targeted file section context. Only then compare QW center Px and runtime parameter inheritance; do not run source changes or 0.5→0 activation test without approval.

## 2026-11-02 — Lee installed AlGaN polarization coefficients observed (OBSERVED, NO RUN)
- Worker 이택규 actual school-server read-only grep of installed T-2022.03 MaterialDB *GaN.par (output truncated by head -n 120): AlGaN.par Piezoelectric_polarization block line1017; formula=1 line1076; relax=0.0 line1078; psp_z(0)=-3.4000e-06, psp_z(1)=-9.0000e-06, B(psp_z(1))=-2.10e-06, C(psp_z(1))=0; e31(0)=-5.2740e-05, e33(0)=8.9460e-05 C/cm^2. GaN.par polarization section heading line737 observed but numeric coefficients not within pasted output; InGaN.par numeric coefficients not within pasted output.
- Previous n2 3.6V barrier-center Px=+3.4e-06 C/cm^2 equals magnitude of AlGaN.par psp_z(0). Known lattice orientation plausibly reverses sign, but effective runtime source, InGaN polarization, activated interface sheet and QW4 cause remain UNVERIFIED. No new solver run or any source/mesh/material library edits; Baseline B physical FREEZE HOLD.
- NEXT READ ONLY: grep assignment lines for psp_z, e31, e33, a0, a, relax and formula in GaN.par, InGaN.par, AlGaN.par WITHOUT head truncation; check InGaN x=0.15 and runtime provenance. No physics perturbation without approval.

## 2026-11-02 — MaterialDB GaN/InGaN/AlGaN file names confirmed (OBSERVED, NO RUN)
- User school server `find /user/tools/synopsys/sentaurus/T-2022.03/tcad/T-2022.03/lib/sdevice/MaterialDB -maxdepth 1 -type f \( -iname '*gan*' -o -iname '*ingan*' -o -iname '*algan*' \) -print` returned four actual files: `AlGaN.par`, `InGaN.par`, `GaN.par`, `AlInGaN.par`. Directory path previously verified as `/user/tools/synopsys/sentaurus/T-2022.03/tcad/T-2022.03/lib/sdevice/MaterialDB`.
- OBSERVED confirms file existence **only**; actual `Piezoelectric_Polarization`, psp_z, e31/e33, relax constants and effective runtime inherited values NOT YET inspected. NEXT READ ONLY grep relevant polarization constants in three GaN/InGaN/AlGaN files, preserve all files. No SDevice run/edits; Baseline physical FREEZE HOLD.

## 2026-11-02 — T-2022.03 MaterialDB real directory found (OBSERVED USER SHELL; NO RUN)
- 이택규 school server `which sdevice` confirmed twice: `/user/tools/synopsys/sentaurus/T-2022.03/bin/sdevice`. `find /user/tools/synopsys/sentaurus/T-2022.03 -maxdepth 8 -type d -name MaterialDB -print` returned exactly `/user/tools/synopsys/sentaurus/T-2022.03/tcad/T-2022.03/lib/sdevice/MaterialDB`. This establishes actual directory existence, not yet GaN/InGaN files, coefficient values, or effective run-time parameter provenance.
- **NEXT READ ONLY (PROPOSED, NOT YET RUN):** `find /user/tools/synopsys/sentaurus/T-2022.03/tcad/T-2022.03/lib/sdevice/MaterialDB -maxdepth 1 -type f \( -iname '*gan*' -o -iname '*ingan*' -o -iname '*algan*' \) -print`, then read actual material polarization coefficient blocks and compare with n2 CSV polar data without editing installed library or baseline. No new simulation, baseline physical FREEZE HOLD.

## 2026-11-02 — Sentaurus executable real installation path confirmed, MaterialDB location next (OBSERVED, NO RUN)
- 이택규 학교 서버 `which sdevice` 실제 출력: `/user/tools/synopsys/sentaurus/T-2022.03/bin/sdevice`. 이전 환경변수 조회 `env | grep -E '^(STROOT|STRELEASE)='`는 출력 없었지만, 실행 파일의 위치는 PATH를 통해 확인됨. 이 결과는 설치된 실행 파일 위치만 확인하며 MaterialDB 실제 경로 또는 해당 파일 내용까지 증명하지 않음.
- NEXT READ ONLY: `find /user/tools/synopsys/sentaurus/T-2022.03 -maxdepth 8 -type d -name MaterialDB -print`. 검색 결과 후 해당 GaN/InGaN/AlGaN 기본 분극 물성 파일명·값을 읽고 기존 n2 PE_Polarization-X와 물성 관계 검토. Sentaurus 원본/시뮬레이션/mesh 수정 없음. Baseline physical FREEZE HOLD.

## 2026-11-02 — STROOT/STRELEASE 환경변수 읽기 시 shell syntax 오류 (OBSERVED, NO RUN)
- User terminal in CMP_BASELINE_2.0.0_V2: prior assistant command with Bash-style fallback for environment variables failed with `Bad : modifier in $ (-).`.
- Diagnosis: this shell error is consistent with csh/tcsh treating Bash fallback expansion as invalid. Exact shell not independently identified. This is not a Sentaurus solver error or evidence that MaterialDB is missing.
- Corrective command PROPOSED, NOT YET EXECUTED: `env | grep -E '^(STROOT|STRELEASE)='`. This reads environment only; if no match, use executable path checks. Baseline unchanged and no simulation run.

## 2026-11-02 — n2 PAR polarization coefficients not explicitly overridden; default MaterialDB provenance NEXT (OBSERVED + PUBLIC SOURCE, NO RUN)
- 이택규 user actual server cmd: `grep -nEi -C 2 'Piezoelectric|Strain|e31|e33|Psp|Relax|Lattice|Polarization|a0' pp2_des.par | head -n 100` returned only `LatticeParameters{X=(0,0,-1),Y=(1,0,0)}` lines 1–3. Thus **this n2 preprocessed PAR does not explicitly specify e31/e33/psp/a0/relax/Piezoelectric_Polarization parameter block under the searched terms**. Does NOT mean polarization was disabled: cmd has `DefaultParametersFromFile` and `Piezoelectric_Polarization(strain activation=0.5)`; TDR cutline contains Px and bipolar interface PE_Charge values.
- Public Sentaurus Training Ch16 §16.4.4 (https://ghzphy.github.io/Sentaurus_Training/sd/sd_16.html) documents GaN/AlGaN/InGaN polarization coefficients in default MaterialDB `$STROOT/tcad/$STRELEASE/lib/sdevice/MaterialDB/`, activated via Physics `DefaultParametersFromFile`. Public guide explains psp_z, e31/e33, a0/a and relax. Effective exact installed T-2022.03 MaterialDB coefficients and parameter-override precedence for this n2 run NOT directly verified yet.
- NEXT READ ONLY: check `STROOT` and `STRELEASE` server environment and actual `GaN.par`, `InGaN.par`, `AlGaN.par` MaterialDB locations; verify actual default polarization parameter blocks and n2_des.log path/parameter warnings. Do not create `sdevice -P` outputs in the original project directory (risk overwriting models.par). QW4 anomalous preference still causally UNRESOLVED, no deck edits/solver run, FREEZE HOLD.

## 2026-11-02 — n2 active GaN/InGaN/AlGaN band offset 70:30 정량 확인 (OBSERVED SRC + DERIVED; NO RUN)
- 학교 서버 실제 `grep -nEi -C 3 'Chi0|Eg0|mumax|Piezoelectric_Polarization|psp|relax|a0|Bandgap' pp2_des.par | head -n 140` 사용자 출력: Material GaN Bandgap `Eg0=3.4376eV`, `Chi0=4.1000eV`, ConstantMobility `mumax=300,10` (lines6–16); InGaN `Eg0=2.8569eV`, `Chi0=4.5065eV`, `mumax=300,10` (lines59–69); AlGaN `Eg0=3.7564eV`, `Chi0=3.8768eV`, `mumax=300,10` (lines112–123). No material parameter edits/solver run.
- DERIVED from electron-affinity model for nominal **flat-band GaN/InGaN interface**: bandgap difference 3.4376−2.8569=0.5807eV; conduction step Chi_InGaN−Chi_GaN=0.4065eV (electron well depth); valence offset ΔEg−ΔEc=0.1742eV (hole well depth); ratio ≈70.00%/30.00%. This confirms Claude-reported 70:30 from supplied active PAR numbers. `mumax 300,10` is model parameter, not directly measured effective field-dependent mobility in device.
- CAUTION: ΔEc=0.4065eV **must not be conflated** with previously observed barrier interior `Ec−eQF`~0.445–0.5144eV: the former is nominal heterojunction material discontinuity; latter is occupancy/quasi-Fermi relative local band edge. Actual biased heterojunction transport also depends on bending/polarization/thermionic assumptions. Presence of 70:30 does not prove root cause of QW4 99.97% four-QW radiative concentration.
- User terminal `[1] + Done svisual n1_msh.tdr` indicates background viewer job exited, not new TCAD solver run or simulation failure.
- NEXT READ ONLY: examine actual `pp2_des.par` polarization/strain parameter inheritance (and source `pp2_des.cmd` transport conditions) before any protected-copy `activation .5→0` diagnostic. Baseline physical FREEZE HOLD.

## 2026-11-02 — n2 실제 Fermi/Thermionic/Polarization 활성화·결정 방향 소스 확인 (OBSERVED; PUBLIC UG CONTEXT; NO RUN)
- 이택규 학교 서버에서 `grep -nEi -C 3 'Piezoelectric_Polarization|activation|Thermionic|Fermi|LatticeParameters|Formula|Polarization' pp2_des.cmd pp2_des.par | head -n 100` 실행. 실제 `pp2_des.cmd` global Physics: `Fermi`(line15), `DefaultParametersFromFile`(line16), `Recombination(SRH Radiative Auger)`(line19), `IncompleteIonization`(line20), `Piezoelectric_Polarization(strain activation=0.5)`(line21). `MaterialInterface="InGaN/GaN"`, `"AlGaN/GaN"`, `"AlGaN/InGaN"`에서 각각 `Thermionic`(lines24–26). Plot fields `PE_Charge PE_Polarization/Vector` requested (line65).
- `pp2_des.par`: `LatticeParameters` X=(0,0,-1), Y=(1,0,0) (lines1–4); each of three MaterialInterface blocks with `ThermionicEmission{Formula=1}` (lines165–173). This source-level Fermi+Formula1 pairing matches public Sentaurus Training Chapter16 §16.7.5: https://ghzphy.github.io/Sentaurus_Training/sd/sd_16.html. Orientation matches §16.3 recommended UCS downward x orientation.
- IMPORTANT CORRECTION TO EARLIER UNCERTAINTY: Public training §16.4.3 explicitly describes `activation` scaling **polarization-induced interface charge at abrupt polarization discontinuities**, not merely the strain-derived piezoelectric term. Thus 0.5→0 can be designed as sensitivity of scaled interface polarization charge, NOT necessarily 'turn off piezo only'; current actual active interface charge from `PE_Charge` must still be reconciled with activation, model output and exact T-2022.03 UG.
- Earlier conditional full Px jump |ΔP|/q=1.6092922561e13cm^-2. **Only if** activation multiplies the entire jump by 0.5 uniformly at the QW4 interface, nominal scaled charge magnitude would be 8.04646128e12cm^-2; this is NOT a measured integrated sheet charge or verified simulator effective applied charge. Global source pattern vs overrides not yet fully checked.
- NOT YET VERIFIED: actual material band offset Chi0/Eg0 and low-field mobility `mumax`, independent tunnel mechanisms, full transient runtime settings/log warnings; no assertion that Formula1 or polarization choice caused QW4 focusing. Baseline physical FREEZE HOLD, no source edits/new solver run.
- NEXT READ ONLY: inspect `pp2_des.par` regions Material and alloy `Chi0|Eg0|mumax` and `Piezoelectric_Polarization` parameters, `pp2_des.cmd` other transport keywords before any protected-copy single-variable experiment approval.

## 2026-11-02 — B0–B4 및 QW1–QW4 중심 분극 값 동일: QW4 고유 Px 가설 약화 (OBSERVED; NO RUN)
- 사용자 `qw4_36_depth.csv` Y=1um read-only 최근접 중심 샘플 직접 제공: B0 x=.17692187, B1=.20204687, B2=.22717187, B3=.25229686, B4=.27742186um 모두 `PE_Polarization-X=3.4e-06`, `xMoleFraction=0`; QW1 x=.18948437, QW2=.21460937, QW3=.23947266, QW4=.26459765um 모두 `PE_Polarization-X=8.2162955e-07`, `xMoleFraction=0.15`.
- PE_Charge center values: B0=0, QW1=0, B1=0, QW2=5755.116, B2=0, QW3=0, B3=-5953.4439, QW4=-5758.722, B4=5953.4439; 이들은 계면 피크 ±1.2297757e21와 비교할 국소 residual 표본이지 sheet 적분 결과가 아님. Near-equal centers **does not** prove all eight interface effective sheet charges are numerically equal (not sampled), nor rule out polarization-induced transport differences due to global band bending.
- Derived nominal center-based |ΔP|=3.4e-06−8.2162955e-07=2.57837045e-06 (Px reported unit requires exact source check); QW4-only larger bulk polarization or different In mole fraction hypothesis contradicted by sampled bulk center values. However QW4 electron/hole accumulation vs others persists, cause still UNSOLVED. Physical Baseline FREEZE HOLD; no new run/code edit.
- NEXT READ ONLY: confirm actual runtime model settings in `pp2_des.cmd` / `pp2_des.par`: polarization activation, lattice orientation, Fermi, Thermionic, band-offset parameterization. Then inspect signed peaks at all QW interfaces if necessary. Do not run PolAct diagnostic without approval.

## 2026-11-02 — QW4 양계면 signed PE_Charge와 분극 불연속 확인 (OBSERVED + CONDITIONAL DERIVED; NO RUN)
- 이택규 학교 서버에서 기존 `qw4_36_qw4fine.csv` Y=1um 자료를 read-only `python3 -c`로 `abs(PE_Charge)` 상위 12점 추출. 실제 X=.26300001um B3/QW4에서 `PE_Charge=+1.2297757e21` **동일 X 두 표본**, `PE_Polarization-X=3.4e−06` 및 `8.2162955e−07`. X=.266um QW4/B4에서 `PE_Charge=−1.2297757e21` **동일 X 두 표본**, `PE_Polarization-X=8.2162955e−07` 및 `3.4e−06`. 주변 B3/B4 여러 X 값에서 PE_Charge는 ±~1e5 등 큰 spike에 비해 미소한 표본 값.
- `P_x`가 depth X=.263에서 GaN 값 3.4e−6→InGaN 값 8.2162955e−7로 낮아지고 X=.266에서 다시 올라감. `ρ_pol =−div P` 일차원 표면 점프 부호로 예상되는 + sheet (B3/QW4)와 − sheet (QW4/B4)가 실제 PE_Charge 부호와 일치. 공식 교육자료: https://ghzphy.github.io/Sentaurus_Training/sd/sd_16.html (polarization strain model, interface activation, units).
- CONDITIONALLY DERIVED `ΔP=2.57837045e−6 C/cm²`; `ΔP/q=1.609292256099648e13 cm^-2` (q=1.602176634e−19C), equal magnitude and opposite sign nominal interface-equivalent sheet charges. **This is polarization-vector jump equivalent, not directly the actually applied effective sheet charge**. Effective activation scaling, 2D discretization, PE_Charge unit and interface area/charge bookkeeping must be checked against actual pp2_des.cmd/par and installed T-2022.03 UG before claiming 'physical sheet charge confirmed'. Exact duplicate X discontinuity makes naïve trapezoid of PE_Charge susceptible to severe sampling error.
- QW4 full-depth recombination/current closure from previous turn remains: ΔJn=1.8216831695 vs q∫TotalR=1.8215397088 A/cm², 99.9921% local closure. Polarization spikes are now **observed**, but their causal role in 4QW QW4 99.9688% dominance is still UNRESOLVED; check if QW1–QW3 have matching ΔP before concluding QW4-specific force.
- NEXT READ ONLY: sample actual `PE_Polarization-X`, `PE_Charge`, `xMoleFraction` at B0/QW1/B1/QW2/B2/QW3/B3/QW4/B4 center X values in `qw4_36_depth.csv`, then inspect `pp2_des.cmd` polarization activation and lattice orientation. NO new simulation/deck edits, verdict B/FREEZE HOLD.

## 2026-11-02 — n2 3.6V QW4 내부 ΔJn 및 q∫Rdx 99.9921% 폐합 확인 (OBSERVED + DERIVED; NO NEW RUN)
- 이택규 실제 학교 서버에서 기존 `qw4_36_qw4fine.csv`(Y=1µm)을 Python DictReader로 read-only 분석. 숫자 sample X=[0.26300001,0.266] µm(실제 데이터 경계, 총 N=24개), 정상상태 n2 3.6V 조건. q×1e−4=1.602176634e−23 (길이 µm를 cm로 변환) 적용, trapezoid로 q∫Rdx 계산.
- USER OBSERVED ΔJnX = 1.8216831695 A/cm². q∫Radiative dx=1.2205564144284573, q∫Auger dx=0.5018975294245672, q∫SRH dx=0.09908575891169007, q∫TotalRecombination dx=1.8215397088407301 A/cm². 채널 합=1.8215397027647144 (total−sum=6.0760157e−9 A/cm²).
- DERIVED continuity closure q∫TotalRdx / ΔJnX = 99.99212482929678%, absolute residual ΔJnX−q∫Rdx=0.00014346065926984508 A/cm², relative residual=0.007875170703214047%. Local QW4 integrated totalR channel proportions Radiative=67.0068518684804%, Auger=27.553477258202975%, SRH=5.439670539751808%.
- IMPORTANT interpretation: For this **single Y=1µm depth cutline**, QW4 electron-current variation is nearly explained by local net total-recombination rate. This is strong internal numerical-consistency evidence for intense QW4 recombination sink. It does **not prove physical origin** of 4QW QW4 99.9688% radiative share (distinct denominator), rule out carrier transport bottleneck, validate 2D full-area integration, or prove exact global 2D continuity: lateral JnY divergence not independently measured; residual may also reflect interpolation/rounding/numerical sampling. Baseline verdict B; physical FREEZE HOLD.
- NEXT READ ONLY: inspect signed `PE_Charge` / `PE_Polarization-X` near QW4 x≈0.263 and 0.266µm; verify quantity/unit interpretation and integration support before deriving interface sheet cm^-2. Independently inspect pp2_des.cmd/par polarization, thermionic and band offsets. No source/mesh edit, no simulator run, no approval for PolAct perturbation.

## 2026-11-02 — QW4 fine CSV 3.6V에서 B3→QW4→B4 전류 재분배 직접 확인 (OBSERVED + DERIVED; NO RUN)
- 이택규 사용자 실제 학교 서버 `qw4_36_qw4fine.csv` read-only `python3 -c` 출력(Y=1um) 7개 cutline depth 표본:
  - X=0.26014844 (B3): JnX 0.0017772979, JpX 1.8218264, Jtotal 1.8236037, Ec−eQF 0.3734eV, Rad 1.3475925e15.
  - X=0.26250389 (B3): JnX 0.0017779541, JpX 1.8218258, Jtotal 1.8236037, Ec−eQF 0.3520eV, Rad 9.6067543e14.
  - X=0.26355079 (QW4): JnX 0.33616893, JpX 1.4871776, Jtotal 1.8233466, Ec−eQF 0.0008eV, Rad 2.4382434e25.
  - X=0.26459765 (QW4): JnX 0.96137367, JpX 0.86228261, Jtotal 1.8236563, Ec−eQF 0.0856eV, Rad 3.075366e25.
  - X=0.26551366 (QW4): JnX 1.5101376, JpX 0.31358008, Jtotal 1.8237176, Ec−eQF 0.1603eV, Rad 2.4777785e25.
  - X=0.26656055 (B4): JnX 1.8234614, JpX 0.0003014948, Jtotal 1.8237629, Ec−eQF 0.3675eV, Rad 7.4700005e18.
  - X=0.27009374 (B4): JnX 1.8234663, JpX 0.00029702933, Jtotal 1.8237634, Ec−eQF 0.3054eV, Rad 8.5527203e18.
- DERIVED between near-QW boundaries: B4 Jn−B3 Jn =1.8216834459 A/cm²; fraction relative to B4 Jn 99.90249565%. This is **local depthwise Jn change across QW4 at Y=1um**, NOT QW4 99.9688% of QW radiative PLT-integrals. Total Jx near ~1.8236. In-well Rad ~(2.4–3.1)e25 cm^-3s^-1 versus adjacent barrier local rates much smaller. Compatible with severe QW4 electron-hole recombination sink and near-total electron flux attenuation toward p side.
- CAUSALITY NOT CONFIRMED: 2D electron continuity includes lateral derivative ∂JnY/∂Y; center-line ∆JnX alone cannot be assigned 100% to recombination, nor prove that B3 potential barrier, polar sheet or thermionic transport caused it. Strong QW4 recombination may explain low upstream electron current. Must distinguish flux-consumption observation from root cause.
- NEXT READ ONLY: from all numeric rows of `qw4_36_qw4fine.csv`, evaluate QW4 X=.263–.266um approx `q∫ TotalRecombination dx` (µm→cm 1e-4), compare to ∆JnX and channel decomposition Rad/Auger/SRH with Y-current caveat; then PE_Charge signed sheet integration & exact model parameter checks. Existing V2.1 source/mesh and solver not modified, Baseline B physical FREEZE HOLD.

## 2026-11-02 — 3.6V B0–B3/QW1–QW4 장벽 중심 전자·정공 수송 수치 직접 검산 (OBSERVED USER TERMINAL + DERIVED; NO NEW RUN)
- 이택규가 기존 `qw4_36_depth.csv`를 read-only Python DictReader로 열고 SDE `pp1_dvs.cmd` layer-center 인근 최근접 좌표의 `eDensity`, `hDensity`, `Ec-eQuasiFermiEnergy`, `hQuasiFermiEnergy-Ev`, `eCurrentDensity-X`, `hCurrentDensity-X`를 추출해 실제 터미널 결과 제공. 실제 X (µm): B0=.17692187, QW1=.18948437, B1=.20204687, QW2=.21460937, B2=.22717187, QW3=.23947266, B3=.25229686, QW4=.26459765; 공통 cutline Y=1µm.
- 장벽별 n/p (cm^-3), Ec−eQF (eV), hQF−Ev (eV), JnX/JpX (CSV 출력): B0 n6.8108774e9 / p4.0180313e14 / 0.5070 / 0.3012 / Jn3.7401938e-9 / Jp1.8236277; B1 n5.1276315e9 / p5.1389714e14 / 0.5144 / 0.2948 / Jn0.00019612255 / Jp1.8234322; B2 n1.3421744e10 / p5.4166135e14 / 0.4895 / 0.2935 / Jn0.0004408187 / Jp1.8231819; B3 n7.5388606e10 / p1.0746482e15 / 0.4449 / 0.2758 / Jn0.0017767865 / Jp1.8218269. DERIVED p/n≈58994,100221,40357,14255. Claude 10/23 'p/n~1e4–1e5, Ec−eQF~.45–.51' broadly matches (B1 .5144 slightly beyond rounded .51).
- QW3 near x=.23947266 n=2.3390056e16, p=1.5939417e16, Ec−eQF=.1833, hQF−Ev=.1958, JnX=.0010522837, JpX=1.822569. QW4 x=.26459765 n=1.0123225e18, p=1.5189656e18, Ec−eQF=.0856, hQF−Ev=.0776, JnX=.96137367, JpX=.86228261. DERIVED QW4/QW3 density: n~43.28×, p~95.30×.
- Local total current crosscheck: B3 Jn+Jp=1.8236036865; QW4 midpoint=1.82365628 (A/cm² under existing CSV density convention), approximately preserved. At B3 e current fraction=.09743%, QW4 center e current fraction=52.71682%; Jn(QW4center)/Jn(B3center)≈541.07. This is consistent with QW4 **strong net recombination** consuming electron flux en route toward p side, but DOES NOT isolate barrier-limited electron transport: a recombination sink itself causes a steep Jn spatial gradient. Single cutline center samples do not quantify full-QW integral or prove polarization/thermionic root cause.
- Confidence: **Observed numeric profile validates Claude's barrier carrier deficit pattern**, not its causal 'electron bottleneck' diagnosis. QW4 99.9688% radiative share remains earlier *integrated* PLT result, distinct from present local Jn/Jp. No new solver run, source modification, or model parameter adjustment; physical FREEZE HOLD.
- NEXT READ ONLY: inspect `qw4_36_qw4fine.csv` around B3→QW4→B4 with nearest X≈0.260,0.2625,0.2635,0.2645,0.2655,0.2665,0.270 for electron/hole current and Ec/eQF, to resolve where Jn shifts. Quantify signed PE_Charge sheet only after confirmed units and ordering.

## 2026-11-02 — V2.1 cutline 네 CSV 수치 범위 및 MQW 깊이 배치 직접 검증 (OBSERVED; NO NEW RUN)
- 이택규 학교 서버에서 `sed -n '60,100p' pp1_dvs.cmd` 확인: 적층 top→bottom pCap 0.020, pGaN 0.120, EBL 0.026, B0 0.022, QW1 0.003, B1 0.022, QW2 0.003, B2 0.022, QW3 0.003, B3 0.022, QW4 0.003, B4 0.022 µm. `P(lat dep z)=(position dep lat z)`로 깊이는 CSV X, 가로는 CSV Y. 적층이 X=0부터 누적된다는 소스 정의에 따라 QW1 X=0.188–0.191, QW2=0.213–0.216, QW3=0.238–0.241, QW4=0.263–0.266 µm, B0=0.166–0.188, B1=0.191–0.213, B2=0.216–0.238, B3=0.241–0.263, B4=0.266–0.288 µm (DERIVED FROM SOURCE).
- 사용자 실제 `python3 -c` CSV DictReader 출력: `qw4_eq_depth.csv` N=392 X=0.13988867–0.2973125 Y=1.0, `qw4_36_depth.csv` N=392 X=0.13988867–0.2973125 Y=1.0, `qw4_36_qw1fine.csv` N=66 X=0.1800625–0.19995312 Y=1.0, `qw4_36_qw4fine.csv` N=62 X=0.25543749–0.27428126 Y=1.0. 각 fine 범위는 해당 QW와 양옆 B 영역 일부를 포함한다. CSV 행 수는 메타데이터/빈 값 필터 후 실제 숫자 행 수.
- 첫 긴 Python 구문은 입력 세 번이 붙어 `SyntaxError`가 발생했으나 바로 재입력해 정상 수행. **터미널 입력 오류이며 물리 시뮬레이션 오류 아님.** 원본 파일 수정/새 run 없음.
- 과거 일부 보고의 QW 좌표(~0.168/0.243um)는 현재 source-derived QW1~4보다 0.020um 앞에 있으므로 동일 구조/좌표계인지 비교 시 주의. 현재 출처는 `pp1_dvs.cmd` 실제 스택; CSV composition과 연관 확인 필요. **이 차이를 원인 규명으로 단정하지 않음.**
- NEXT READ ONLY: 현재 `qw4_36_depth.csv`에서 B0–B3/QW1–QW4 중심점 실제 X와 e/h density, Ec-eQF, hQF-Ev, e/h current-X를 함께 추출해 Claude 전자 interwell bottleneck 가설 검토; 이후 PE_Charge 단위/계면 적분 검증. FREEZE HOLD.

## 2026-11-02 — 기존 QW4 cutline CSV 헤더/3.6V 표본 직접 검증 (OBSERVED SERVER OUTPUT; NO RUN)
- `wc -l qw4_*.csv`: `qw4_36_depth.csv`=395, `qw4_36_qw1fine.csv`=69, `qw4_36_qw4fine.csv`=65, `qw4_eq_depth.csv`=395, total 924 lines. 각 파일은 SVisual 첫 행 변수 헤더와 둘째 `none`/SELECTED 메타데이터 행을 포함하므로 실제 자료행은 각 393/67/63/393으로 추산(빈 줄 여부 등 전체 파일 미검증).
- `head -n 6`의 eq/3.6V depth CSV에서 `PE_Charge`, `PE_Polarization-X`, `ConductionBandEnergy`, `ValenceBandEnergy`, `eQuasiFermiEnergy`, `hQuasiFermiEnergy`, `eDensity`, `hDensity`, `eCurrentDensity-X`, `hCurrentDensity-X`, `TotalCurrentDensity-X`, `X`, `Y`, `Distance` 열 확인. 실제 n2 3.6V depth cutline 표본 `X=0.14,Y=1`에서 `TotalCurrentDensity-X≈1.8236326`; 이전 2D 조건부 J=1.8236426244 A/cm²와 수치적으로 거의 같아 내부 교차검증을 지지하지만 공식 단위/4×4um 해석 별도.
- eq와 3.6V CSV 첫 표본 `PE_Charge=-5.5020169e20` (출력 열의 **미적분된 국소 값**, 계면 sheet cm^-2 아니므로 직접 사용 금지). 계면 signed charge density 분석은 `X` 좌표의 물리적 단위·순서, 급변 영역 구간 및 volumetric PE_Charge 단위 확인 후에만 시도.
- CURRENT BLOCKER: QW4 Rad n2 99.9688%/n6 99.9929% 물리 원인 UNRESOLVED. Claude 전자 수송 병목 가설 NOT CONFIRMED. PROPOSED `PolAct 0.5→0` 수정/실험 승인·실행 없음.
- NEXT READ ONLY: 네 CSV 데이터행 좌표 X/Y min-max와 sample position, SDE QW stack 위치 확인 → 같은 위치 Ec/Ev/e/h QF/current 및 PE 계면 적분의 유효성 확인. 서버 파일 변경 없음.

## 2026-11-02 — QW4 cutline CSV 4개 실제 서버 파일 존재 확인 (OBSERVED USER TERMINAL; NO RUN)
- 이택규가 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`에서 `find . -maxdepth 4 -type f -name 'qw4*.csv' -print` 실행: `./qw4_eq_depth.csv`, `./qw4_36_qw1fine.csv`, `./qw4_36_depth.csv`, `./qw4_36_qw4fine.csv` 네 파일 **존재 확인**. 이 결과만으로 열 구성, 출처 TDR, 변수 단위, 계면 전하 적분 결과, 내용 무결성은 검증되지 않음.
- `find . -maxdepth 4 -type f -name 'server_readonly_cmds_20261102.sh' -print` 출력이 비어 있어 **해당 프로젝트 디렉터리의 탐색 깊이 4까지** 스크립트 발견되지 않음. 서버 전체에 없다는 의미가 아님. 클로드 제공 스크립트를 실행했다고 가정하지 말 것.
- **NEXT READ ONLY:** `wc -l qw4_*.csv`, `head -n 6 qw4_eq_depth.csv`, `head -n 6 qw4_36_depth.csv` 로 CSV 레이아웃/데이터 열·단위 확인. 이후에만 PE_Charge→interface sheet density, 장벽 Ec/eQF 검토. Baseline physical FREEZE HOLD, 수정/새 시뮬레이션 없음.

## 2026-11-02 — Claude 독립 재평가 인계 수신 (PROPOSED, 새 RUN/수정 없음)

아래 코드 블록은 사용자가 전달한 **Claude 인계 6절을 원문 그대로 보존**한다. 별도 인용으로, 이번 ChatGPT가 해당 CSV/UG 원본을 직접 재검산했다는 의미가 아니다. 클로드가 주장한 전자 수송 병목·원인 순위·`PolAct` 조절 후 예측 결과는 검증되지 않은 해석/작업 가설이다.

```text
2026-11-02 (Claude 독립 재평가, PROPOSED, 새 실행 없음) V2.1 QW4 99.97% 집중 검증 계획
- GitHub 8553f64까지 열람, Issue #7 미열람(403). UG p.58/120(2D 전류 A/um), p.193(Iterations), p.871(Formula=1은 Fermi 전제, 덱에 Fermi 있음), p.1003(activation), p.1072(LED 예제 QW sheet ±1e12) 재확인.
- 새 관찰(DERIVED): 장벽 B0-B3에서 p가 n보다 1e4-1e5배 많음(Ec-eQF 0.45-0.51 eV vs hQF-Ev 0.28-0.30 eV). 이 모델의 우물 간 병목은 전자 → n쪽 QW4 집중을 직접 설명. 실험 경향(정공 병목, p쪽 우세)과 반대.
- Claude 10/23 정정: "1.6 eV 계면 손실"은 이중 계산(올바른 qV-ΔQF: QW4 0.91, QW1 1.20 eV), "QF 분리가 원인"은 동어반복, "정공은 잘 통과"는 단순화.
- 우선순위: 분극 sheet 크기 = Thermionic+깊은 전자 우물 > 터널링 부재 > 나머지(주입/메시/Half/집계는 반대 증거).
- 다음: (1) 읽기 전용 CSV로 계면 sheet 면밀도(cm^-2) 적분, QF 강하 위치, par 오프셋·이동도 (2) 승인 후 PolAct 0.5→0 단일 변수 진단 run(복사 프로젝트, 같은 메시).
- 판정 B 유지, FREEZE 보류.
```

검토 메모 (ChatGPT, PROPOSED): `strain activation=0`의 효과가 압전 분극만인지 전체 계면 분극인지 공식 T-2022.03 UG 및 실제 전처리 덱을 대조해야 한다. `Iterations=12`가 수렴 한계인지 여부는 solver convergence log 검증과 별개다. QW4 80%·전자 100배 기준은 Claude가 제안한 탐색적 임계값이며 물리적 입증 기준이 아니다. 기존 소스/메시/실행 변경 없고 FREEZE HOLD 유지.

## 2026-11-02 — 기존 V2.1 Mesh 최소각/최소 Edge 위험 재확인 (OBSERVED SERVER READ ONLY; NO RUN)
- 사용자 학교 서버에서 `grep -niE 'minAngle|maxAngle|edgeLength|warning|vertices|elements' n1_msh.log | tail -n 50` 실행: `62533 vertices`, `123917 elements`, `minAngle: 0.0167024`, `maxAngle: 128.367`, `min edgeLength: 1.95312e-05 [near (0.0041875 1.89501)]` (units um from V2.1 mesh context). 최소 Edge 길이 산술 환산 `0.0195312 nm`.
- 사용자가 제공한 메시 로그는 기존 2026-10-21 `ERROR_LOG.md`의 동일 결과와 일치하는 **재확인**, 새로운 메시 생성/소스 변경/solver 오류 발견 아님. near 좌표는 SDE x(depth)=0.0041875um, y(lateral)=1.89501um; Xe=1.895um Clean/Edge 경계 인접. 최소 **각도**의 위치가 최소 **길이**의 위치와 같다는 증거는 없음.
- 극단적 최소 각도·짧은 Edge는 메시 품질 검사 대상으로 유지하지만 QW4 99.97% 집중 원인 또는 계산 수렴 문제의 직접 원인이라 단정하지 않음. Full/Half 수치적/물리적 동등성 아직 미검증, Baseline freeze HOLD.
- NEXT: 기존 `n1_msh.tdr` SVisual 시각화에서 중심 절단선 및 Clean/Edge 전이 구간의 실제 triangle/경계 라벨 읽기 전용 점검. 필요 시 메시 품질 민감도는 후속 보호된 별도 실험으로만 수행.

## 2026-11-02 — V2.1 Half 중심선/전극 소스 및 메시 파일 존재 직접 확인 (OBSERVED; NO RUN)
- 이택규 실제 서버 출력: `sed -n '20,68p' pp1_dvs.cmd` 및 `sed -n '145,170p' pp1_dvs.cmd`. `P(lat dep z)=(position dep lat z)`이므로 SDE x=depth, y=lateral; `Wm=4.0um`, `Xs=2.0um`, `Wshelf=0`, `Cath=0`, `Wdmg=0.005um`, `Wedge=0.1um`. 상단 anode는 Clean/Edge/Dmg 세 구간 각각 `set-contact`, 아래 cathode는 yBot에서 가로 위치 `Xs/2`를 선택해 지정; 중심선 측면 y=0의 contact 선언은 출력된 전체 contacts 블록에 없음.
- `ls -lh n1_msh.tdr`: 기존 파일 `-rw-r--r-- ... 2.0M Oct 14 13:43` OBSERVED. **파일 존재가 메시 형상, 경계 라벨, 품질 또는 Full/Half 동등성 검증을 뜻하지 않음.**
- 공개 Sentaurus training의 2D 기본 1um 면외 폭 및 구버전 Device UG의 비접촉 외곽 Neumann 설명은 참고 근거에 한함. 실제 설치 T-2022.03의 유효 경계조건/전류 단위 및 mesh의 경계는 별도 확인 필요.
- NEXT READ ONLY `n1_msh.log` mesh quality 및 실제 `n1_msh.tdr` SVisual의 중심 y=0 경계, 전극 라벨을 확인. 기존 mesh minimum triangle angle 경고(10/21 기록)의 소자 품질 영향 미해결. 모델/메시/출력 변경 없음, Baseline HOLD.

## 2026-11-02 — 2D Half 전류밀도 정규화 산술 재현 (OBSERVED USER TERMINAL + CONDITIONAL DERIVED; NO RUN)
- 이택규가 실제 학교 서버 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`에서 n2_des.log, n6_des.log를 grep하여 anode/cathode 모두 runtime `area factor : 1` 재확인. 첫 grep은 명령어 두 개가 붙어 `n6_des.loggrep` 오류가 났지만 동일 명령의 나머지 출력으로 두 노드 결과 정상 확보. TCAD 오류 아님.
- 실제 `pp1_dvs.cmd` grep에서 Wm=4.0um, Wshelf=0, Wdmg=0.005um, Wedge=0.1um, Xs=Wm/2=2.0um, Xd=Xs-Wdmg, Xe=Xd-Wedge 및 상단 세 anode/하단 cathode 소스 정의 재확인.
- 본인이 터미널에서 `python3 -c`로 기존 3.6V PLT 원시 anode I를 대입해 직접 계산: 면외 폭 1um 가정 시 A=2.0e-8 cm2, n2 J=1.8236426244266148 A/cm2, n6 J=0.4609853856709715 A/cm2, 동일 전압 감소율=74.72172565521639%. 이는 **기존 수치의 산술 재현**이며 새로운 시뮬레이션이나 새로운 PLT 추출이 아님.
- 교육용 Sentaurus 2D 기본 면외 폭 1um 설명과 일치하나 공식 T-2022.03 원문 대조, 실제 mesh 대칭 경계 및 Full/Half 동등성, 4x4um 실제 정사각형 pixel 물리 calibration은 미완료. 위 J는 CONDITIONAL 2D slice J임.
- 다음은 기존 `pp1_dvs.cmd` 대칭 절단선/접점 경계 및 mesh의 실제 형상 읽기 전용 확인. Baseline freeze HOLD; 소스/메시/시뮬레이션 변경 없음.

## 2026-10-31 — n2 로그에서 contact AreaFactor=1 확인 (OBSERVED, NO RUN)
- 실제 학교 서버 `n2_des.log` lines237–238: anode (Ohmic) `area factor : 1`, cathode (Ohmic) `area factor : 1`. 기존 CMD/PAR `AreaFactor` grep 미검출과 상충하지 않음: 현재 **n2 런타임 접점 스케일 값**을 직접 확인했음.
- n6는 이 출력에서 확인되지 않음. 출력에 pp1_dvs.cmd geometry/contact 정의가 없어 Half 폭/전류밀도 환산은 미완료. QW4 99.97% 집중의 물리적 원인과 Baseline freeze는 여전히 UNRESOLVED/HOLD.
- 신규 SDevice RUN/코드 변경 없음. 다음 읽기 전용: n6 로그 `area factor`, SDE half lateral geometry/contacts 원문 검증.

## 2026-10-31 — V2.1 전류 AreaFactor/단위 키워드 검색 (OBSERVED; 미해결)
- 원본 학교 서버 터미널에서 n2/n6 LOG, pp2/pp6 CMD/PAR 6파일 검색. 검색 결과는 `eCurrentDensity/Vector`/`hCurrentDensity/Vector`/`TotalCurrentDensity/Vector` Plot 요청과 `CurrentPlot(IntegrationUnit=um)`뿐이며 `AreaFactor`, `A/cm`, `A/um`, `CurrentUnit` 직접 표기는 검출되지 않음.
- 의미: 두 노드에서 동일한 출력 설정을 재확인했지만 `AreaFactor` 기본값/2D 유효 단자 전류 단위와 실제 전극 면적 **확정 불가**. QW4 집중 원인 및 Full/Half/물리 확정 보류. RUN/코드 수정 없음.
- NEXT는 pp1_dvs.cmd 실제 half lateral 폭/접점 길이 읽기와 로그 헤더/공식 T-2022.03 UG 전류 스케일링 의미 검토. 플롯 요청을 물리적 면적 검증으로 오인하지 말 것.

## 2026-10-31 — 기존 PLT로 동일 전류 범위 n2/n6 QW4 비교 (OBSERVED + DERIVED, NO RUN)
- 사용자 직접 실행 `n2_des.plt`/ `n6_des.plt` 읽기 전용 Python: n6 3.6V target 9.21970771341943e−09, QW4 99.99294273758203%; n2 3.512V I=8.63290391977055e−09, QW4=99.97314950045252%; 3.528V I=1.10599185065263e−08, QW4=99.9725752700292%. n2의 목표 전류 대비 오차 각각 −6.36467%, +19.95954%; target을 감쌈.
- **수학적 보간(실제 계산점 아님)**: alpha=0.2417800852, n2 추정 동일전류 V=3.51586848V, QW4 방사 집중=99.97301066%. n6 실제 99.99294274%, 차이 약 +0.01993207%p. 동일 native current 기준 근사 비교에서도 양쪽 모두 QW4 >99.97%. Trap이 현상의 유일한 원인이라는 설명과 불일치, 특정 전압에만 국한된 결과 아님.
- Baseline 물리적 원인/절대 IQE/AreaFactor/Full-Half는 미검증. 원본 소스/계산 변경 없이 기존 PLT만 확인; 다음엔 반복 비율 확인보다 물리 설정/정규화 출처 및 단일 변수 민감도 설계에 집중.

## 2026-10-31 — PLT 정확한 최종 행 추출 성공, n2/n6 QW4 수치 확정 (OBSERVED USER SERVER + DERIVED; NO RUN)
- 앞선 tcsh `Unmatched '`/here-doc 문제를 `bash` 진입→`cd`→`python3 - <<'PY'` 정확한 종료로 해결. 원본 n2_des.plt와 n6_des.plt 읽기 전용 분석 수행.
- 사용자 원본 파싱 결과: n2 3.6V `I_anode=3.64728524885323e-08`; Rad_all 1.52414203814656e23, SRH_all 1.25722226677967e22, Aug_all 6.26570284700597e22, Trap_all 1.17883032026416e6. QW1/2/3/4 Rad=1.88484712e18/2.71876253e18/4.29867210e19/1.52362488e23. QW4 비율 **99.96877481383976%**.
- n6 3.6V `I_anode=9.21970771341943e-09`; Rad_all 2.55552035945039e22, SRH_all 4.32337288643595e21, Aug_all 7.83993596604716e21, Trap_all 1.98258247754075e22. QW1/2/3/4 Rad=2.52601416e15/5.97947823e16/1.74113011e18/2.55527360e22. QW4 비율 **99.99294273758203%**.
- 연산: n6/n2 동전압 전류비 0.25278274; 글로벌 채널 재결합 비율 n2 Rad 66.9530%, SRH 5.5228%, Aug 27.5242%, Trap ~0%; n6 Rad 44.4096%, SRH 7.5131%, Aug 13.6242%, Trap 34.4531%. 조건부 `q×1e−12`을 적용하면 단자 전류 대비 4채널 합 n2=99.99904025%, n6=99.99904051%. 절대 IQE/2D 단위/AreaFactor 실증 아님.
- 판정: QW4 지배는 Trap OFF에서도 존재하여 Trap만을 원인으로 볼 수 없음. 여전히 물리적 집중 원인 미해결; 실험 실행 없음, 물리 Baseline freeze HOLD. NEXT 기존 PLT에서 두 노드 동일 I 대상 비교, 이어 AreaFactor/모델 물리 민감도 결정.

## 2026-10-31 — PLT parser 실행 중 tcsh 따옴표/Here-document 종료 문제 (OBSERVED, SHELL ONLY)
- 사용자 터미널에서 외부 `bash -lc '` 명령이 닫히지 않아 `Unmatched '.` 표시. 이어 `python3 - <<"PY"`를 셸에서 입력하고 종료에 `PY'`를 사용하여 `?` continuation 프롬프트에서 멈춤. 실제 PLT 파싱 결과 없음.
- ChatGPT가 `Ctrl+C` → Bash 진입(`bash`) → 프로젝트 디렉터리 이동 → `python3 - <<'PY'`와 종결 `PY`만 단독 입력하는 방법 제안. **실행 성공 아직 미확인**. 원본 n2/n6 PLT/TDR 및 소스 변경 없음; QW4 물리적 원인 미확정. Read-only PLT 감사 예정.

## 2026-10-31 — n2/n6 실제 3.6V 완료·PLT 헤더/꼬리 재확인 (OBSERVED, NO RUN)
- 학교 서버 터미널에서 `n2_des.sta`, `n6_des.sta` 둘 다 `done` 및 SDevice anode 최종 3.600V n2 `3.647E-08`, n6 `9.220E-09` 출력. 같은 전압의 원시 단자 전류는 ON/OFF=0.25281, 74.72% 감소. 전류 정규화/동일전류 IQE와 혼동 금지.
- DF-ISE n2/n6 PLT 헤더에 12개 QW Clean/Edge/Dmg 방사·SRH·Auger 적분 및 global/Trap 데이터셋 존재. `head -25`·`tail -12`만으로 전체 마지막 값 위치를 독립 재매핑할 수 없으므로 다음엔 파일 자체를 읽기 전용으로 파싱해야 함. 꼬리에 n6 Trap-all `1.98258247754075e22`, n6 SRH-all `4.32337288643595e21`, n6 Aug-all `7.83993596604716e21`가 포함되어 이전 GitHub 연구 기록과 수치 일치. n2 SRH-all `1.25722226677967e22`, Aug-all `6.26570284700597e22`, Trap-all `1.17883032026416e6`도 기존 기록과 부합.
- 기존 10/14 PLT 재확인, 새 시뮬레이션/수정 없음. QW4 ~99.97% 원인 여전히 검증되지 않음. NEXT 읽기 전용 정확한 PLT dataset별 최종 행 추출(2D 단위 확인), n2/n6 whole-device/QW 수지와 matched-current 타당성 검토.

## 2026-10-31 — V2.1 pp2/pp6 설정 원문 재확인 (OBSERVED USER TERMINAL; READ-ONLY)
- 본인이 2026-10-31 학교 서버 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`에서 Bash 읽기 전용 검사를 실행하여 출력 제공. `pp2_des.cmd:174`와 `pp6_des.cmd:174` 모두 `Iterations = 12`. 별도 초기화 Coupled 반복값 200 및 100과 구분. 이전 Claude SWB_PASTE의 20이라는 기록과 달리 **현재 확인 가능한 pp2/pp6 전처리 CMD 설정은 12**이며, 당시 solver LOG와의 이력 대조는 아직 남음.
- 공통 CMD: 분극 strain activation=0.5, InGaN/GaN·AlGaN/GaN·AlGaN/InGaN Thermionic 선언, CurrentPlot IntegrationUnit=um. 공통 PAR: ThermionicEmission Formula=1. 물리적 정당성/최종 로그 모델은 이 grep만으로 확정 불가.
- 기존 n2/n6 PLT 및 end TDR 네 파일 모두 존재(10/14 생성 시각, 크기 293K/295K/21M/23M). 새 RUN/소스 수정 없음. `AreaFactor` 검색 결과 없음; 실제 유효 전류 단위와 geometry scaling 미검증.
- QW4 방사 비중 ~99.9688% 원인 여전히 UNRESOLVED; 물리적 Baseline freeze HOLD. NEXT는 로그/PLT 원자료(헤더와 최종 행) read-only 확인, full-device recombination·trap·전류 수지 및 matched-J 분석. 보호된 원본 파일 변경 금지.

## 2026-10-23 — V2.1 n2 QW4 fine cutline results (이택규 OBSERVED-user + Claude DERIVED/HYPOTHESIS; NO NEW RUN)

> **아래는 사용자가 요청한 Claude 인계 원문 7절을 그대로 수록한 것임.** 서버 SVisual TDR→CSV 출력과 awk 판독은 사용자/Claude 보고이며, 원본 TDR·CSV·분석 스크립트 자체를 이 GPT 세션에서 확보하여 재계산하지 않았음. 원문의 "배제", "원인 특정", "집계 오류 아님" 등은 **Claude의 판정**으로 기록하며 독립적인 CONFIRMED 검증으로 격상하지 않음.

```text
2026-10-23 (이택규 서버 출력 + Claude 해석, 새 시뮬레이션 없음) V2.1 n2 QW4 99.97% 집중 원인 특정
- 방법: SVisual batch qw4cut.tcl로 n2_eq / n2_end TDR의 y=1.0um depth cutline을 csv로 export, awk로 판독.
- 배제: 4 QW 모두 xMole 0.15, Eg 2.8569 eV. 평형 PE_Charge 부호는 Ga-polar 패턴. 우물 중심 Rad/np = 2.000e-11(=B). local J 1.8236 = 단자 J.
- QW4 내부: n 9.1e19(p쪽 계면), p 8.3e19(n쪽 계면). 직접 적분 Rad 67.0 / Auger 27.6 / SRH 5.4%, Jrad 1.220 A/cm2 → 보고값 재현. 집계 오류 아님.
- 3.6V QF: eQF가 장벽→우물 진입마다 ~0.24 eV 강하(합 0.97), hQF 0.23/0.22/0.18/0.02 eV(합 0.66). QF 분리 QW1-3 2.40-2.48 vs QW4 2.69 eV → QW4 집중의 직접 원인. ~1.6 eV가 계면에서 소모 → 높은 Vf와 같은 원인.
- 해석(가설): 분극 계면 + Thermionic-only 고전 DD(터널링·양자보정 없음)의 결과. 설정 오류 미발견.
- 10/22 Claude의 "QW4 n>>p" 역산 철회.
- 판정 B 유지, Baseline 고정 보류. 미해결: 실행 덱 Iterations 12 vs 20 출처, n6 미확인, 분극 크기 적정성.
- 다음(승인 필요): 계면 수송 모델 1변수 민감도(Heterointerface UG p.870 / 터널링 UG p.1070).
```

**후속 검증 경계:** 네 QW의 동일 조성/BandGap은 보고된 1D cutline 지점들의 비교 결과임. PE_Charge 부호가 설계한 Ga-polar 패턴과 일치한다는 보고는 분극 시트 크기·절대 물성의 검증을 뜻하지 않음. 접점 J와 단면 local J 일치는 보고된 검사점의 정규화 일치를 나타낼 뿐 모든 2D 전하수지를 증명하지 않음. QF 분리와 재결합 집중 사이 연관성 및 interface Thermionic 제약은 설명 가설로 유지하고, 실제 실행 데크 Iterations 12/20 차이와 n6 미확인 보존. 기존 n2 TDR은 10/14 생성물이며 **새 SDevice RUN 없음, 코드 변경 없음**.

## 2026-10-23 — Claude V2.1 QW4 99.9688% independent review handoff (USER-PROVIDED CLAUDE REPORT; PROPOSED, NO RUN)
- Source: 2026-10-23 user-pasted Claude handoff. This is Claude's source/derivation/literature review, not independently re-executed TCAD or independently checked server output. Report/proposed tools live in Claude-local `cmp/QW4_REVIEW_20261023/` and were NOT provided to GPT; file SHA prefixes are Claude-reported only.
- Claude reports attached SDevice 199-line text (`File {` line 1) differs from its `SWB_PASTE/sdevice_des_compact.cmd` only in line 174 `Iterations = 12` vs SWB_PASTE and LOG #02 setting 20. Claude says diff confirmed; GPT has NOT compared SWB file or actual preprocessed `pp2_des.cmd` / `pp6_des.cmd`. Runtime deck provenance UNRESOLVED.
- QW4 n-side QW radiation region share ~99.9688% (earlier project-observed) remains PHYSICALLY UNRESOLVED. Claude assesses region-summation artifact less likely because non-overlap (Claude-reported SDE), centerpoint np equal-B proxy ~99.973%, approximate centerpoint radiative-current proxy ~1.47 A/cm² vs reported modeled ~1.22 A/cm² (~20.5% discrepancy relative to 1.22, not independently re-evaluated). These are corroborative *proxies*, not proof of model validity or full spatial agreement.
- RETRACTION: Claude's 2026-10-22 reverse-inferred QW4 n~1.6e19 cm^-3/p~8e16 cm^-3 is WITHDRAWN. Existing user-observed n2 3.6V QW4 center eDensity=1.35190e18, hDensity=1.13508e18 cm^-3 take precedence. Claude reports using centerpoint estimates Auger/Rad~0.062 vs earlier integrated ~0.411 and SRH/Rad~0.201 vs earlier integrated ~0.082. These ratios/method were not independently audited; suggest nonrepresentative centerpoint and possible interface accumulation, a HYPOTHESIS only. Claude's inferred effective n+p ~1.6e19 cm^-3 depends on assumed models and integrated ratios, NOT an observation.
- Claude notes existing recorded q×∫QW Rad/I ~66.95% versus QW three-channel Radiative fraction ~66.96%; interprets as mostly QW recombination, not leakage dominated. This is tentative DERIVED and does NOT demonstrate total-current continuity without confirming 2D current/integration units, full-device and trap accounting, current/steady-state conventions.
- Claude reports ~0.30 eV between QW4 and QW1 quasi-Fermi splitting via Boltzmann inversion, NOT directly measured energy profile; clarify model/assumptions and Fermi statistics before treating it quantitatively.
- CLAUDE HYPOTHESIS (UNRESOLVED): classical DD with Thermionic and no explicit tunneling/quantum correction may trap electrons in n-side first well QW4, while holes traverse to it; investigate effective well depths (`xMoleFraction`, `BandGap`), PE_Charge interface signs, e/h QF differences, local n/p peaks. Comparison studies David 2008/Bojarska 2025 p-side, Casu 2022 n-side but different In wells were sourced per Claude; Claude did not access Han 2018 or Kou in this review. Literature says neither that n-side same-composition 4-QW 99.97% is normal nor that it is impossible.
- Claude source-based claims pending direct source/UG verification: Edge=Clean material/doping (SDE), Edge carbon effect implemented as Ev+0.9eV acceptor trap only (not physically verified carbon doping); Dmg/Edge disjoint; total integrals not summed twice; separate SRH vs gap-state traps (Claude UG p.253,473,580); 2D IntegrationUnit=um and UG p.169; Thermionic interface quasi-Fermi discontinuity (UG p.870–871); no explicit Density Gradient/quantum model (UG p.362+). Do not copy restricted UG text.
- Status: no new RUN, no updated 3.6V numerics in this handoff, no SWB source modifications. Baseline physical freeze remains HOLD. Read-only NEXT in order: (1) grep Iterations and compare active pp2/pp6 CMD/PAR and B/Auger/tau/bandgap values; (2) run Claude-proposed `qw4_plt_audit.py` only after source availability and validation with genuine n2/n6 PLT (claimed parser smoke on synthetic data only); (3) review existing n2 TDR xMoleFraction/BandGap, PE_Charge signed interfaces, quasi-Fermi and intra-QW n/p via Claude-proposed `qw4cut.tcl` after verifying script. Files/scripts in Claude folder NOT verified present on school server.
- Keep original Baseline and current SWB n2/n6 untouched. The proposed decision gate is potential 'operational relative-comparison baseline only' after read-only checks and errors ruled out, NOT publication-calibrated baseline or absolute IQE claim.

## 2026-10-23 — Uploaded SDevice code static audit / Claude handoff (OBSERVED SOURCE, NO RUN)
- User provided 198-line SDevice .cmd text. Not verified identical to deployed n2/n6 pp2_des.cmd/pp6_des.cmd. Contains Physics SRH+Radiative+Auger, IncompleteIonization, Piezoelectric_Polarization(strain activation=@PolAct@), and Thermionic heterointerface declarations.
- Parsed: 13 Dmg trap regions (Acceptor Ev+0.75eV @NtSide@) and 13 Edge trap regions (Acceptor Ev+0.9eV @NCedge@), no duplicate names. CurrentPlot integrates QW1..4 each Clean/Edge/Dmg for Radiative/SRH/Auger, and eGapStates over 26 Dmg/Edge regions plus Trap_all. No missing region names can be established without SDE/mesh.
- 2D Math CurrentPlot IntegrationUnit=um requires precise dimensional conversion to electrical current and total recombination current before IQE claims. Explicit trap eGapStates vs SRH/Total definitions and rate-sign accounting need source+official UG verification.
- Different code: old repo CMP/tcad/CURRENT/sdevice2_defect_on.cmd does NOT match this user-uploaded deck (lacks Edge_QW4/@PolAct@); do not treat it as server current V2.1 code or overwrite original.
- QW4 n-side ~99.9688% QW-radiative fraction, previous e/h ~300x QW1 center remains physical-validation blocker; cannot infer root cause from .cmd alone. Missing SDE/par, SWB macro values, runtime logs, I-V/PLT/TDR, actual model parameters; no simulations or code edits.
- Prepared standalone Claude independent audit prompt for user delivery (NOT transmitted to Claude). Priorities: deployed source match, QW mapping, polarization polarity, thermionic/band injection, 3nm quantum treatment, B/C/SRH/trap budget, 2D current units, mesh, matched J.

## 2026-10-23 — Literature audit correction: QW4 is n-side, not p-side (SOURCE-VERIFIED; UNRESOLVED)
- Existing CMP/CURRENT_STATUS.md states V2.1 QW4 is the n-side QW (nominal centers x QW1=0.1895, QW4=0.2645um with p/EBL at lower x). Prior general literature about the p-side well dominating emission (David et al. 2008 DOI 10.1063/1.2839305; Bojarska-Cieślińska et al. 2025 DOI 10.1038/s41598-025-86774-6) **cannot** be used as validation of n-side QW4 dominance in CMP. Any earlier conditional discussion assuming QW4 could be p-side must not be treated as resolved.
- New PRIMARY research evidence: Casu et al. Micromachines 2022 DOI 10.3390/mi13081266 demonstrates an n-side 495nm QW stronger than a p-side 405nm QW by EL and Apsys modeling; mechanism attributed to weak electron supply to p-side well. IMPORTANT: wells have different In fractions (20% vs 10%), so it does NOT calibrate our four nominally equal-In QWs or 99.9688% value.
- 2025 Scientific Reports study varied barrier 2.5–20nm: 20nm leads p-side concentration; 5nm more equal. CMP ~22nm GaN barrier resembles thickness but has a different well stack and device type (laser-type samples). Marcinkevičius et al. APL 2019 DOI 10.1063/1.5092585 supports thermionic-hole transport as possible factor. Han et al. IEEE JQE 2018 DOI 10.1109/JQE.2018.2790440: recombination kinetics also influence carrier balance.
- DECISION: Literature supports that dominant single-QW or even n-side dominance is possible, but **not** that n2 n-side QW4 ~99.9688% is normal/calibrated. Baseline physical-validation blocker remains UNRESOLVED. No new server execution, code changes, or experimental observations.
- NEXT: read-only verify stack/contact orientation/QW integrals, charge sign by interface, current units and whole-device balance, compare matched-current conditions; do not claim model validation or change common baseline to force agreement.

## 2026-10-23 — QW4 ~99.9688% radiation literature plausibility audit (ANALYSIS; NO RUN)
- Existing n2 3.6V QW4 QW-radiative integral share ~99.9688%; QW4 n/p center ~303x/~331x QW1 are previously OBSERVED/DERIVED values, not new results.
- Independently sourced literature: Ji et al., Optics Letters 38, 202 (2013), DOI 10.1364/OL.38.000202: low injection emission mainly from QWs near p-GaN due to limited hole penetration. Liu et al., J. Appl. Phys. 109, 093117 (2011), DOI 10.1063/1.3587176: EL recombination predominantly in p-side QWs. Ryu, Curr. Appl. Phys. 20, 1351 (2020), DOI 10.1016/j.cap.2020.09.005: MQW inhomogeneity can worsen droop.
- Assessment: p-side-dominant QW is physically plausible if QW4 is p-side, but no cited benchmark establishes ~99.97% as normal for THIS 4um 4-QW V2.1 device; physical validity UNRESOLVED. QW4 fraction is NOT IQE. No code changes, simulation or calibrated validation.
- NEXT: read-only check QW ordering relative to p-GaN, integrated radiative QW region mapping, exact current normalization and full-device recombination; then matched-current n2/n6 and targeted sensitivity tests only if justified.

## 2026-10-23 — Signed PE_Charge cutline verified (OBSERVED)
- Existing n2_end_des SVisual, Cutline X=0.14..0.29um Y=1um: after disabling Log Scale on the graph y-axis, positive and negative PE_Charge spikes became visible across nominal MQW heterointerfaces. Graph ±1e21 cm^-3 range; precise numbers and physical sign correctness not established.
- Visualization issue resolved. QW4 carrier accumulation cause, polarization sign validation, current-normalization and matched-J remain unresolved. No TCAD code/run changes. Next read-only existing results and actual current normalization.

## 2026-10-23 — Lee PE_Charge linear-axis visualization appears flat (OBSERVED screenshot; no run)
- On existing n2_end_des PE_Charge Cutline_Y Plot after user unchecked y-axis Log.Scale, plot no longer shows large spikes and instead displays an almost horizontal red trace with no readable numeric y ticks in provided screenshot. Plot Properties Main was visible, not the axis min/max dialog. Prior logarithmic rendering showed narrow vertical spikes and 2D legend global range approximately ±1.23e21 cm^-3.
- This is an axis/rendering limitation observation; do NOT interpret the flat line as zero polarization charge or validated polarity, nor assume the spikes have disappeared physically. Actual axis min/max and region-resolved signed cutline charge have not been verified.
- NEXT READ ONLY: open graph Y Axis Properties and explicitly set Linear with Fixed Min=-1.5e21 Max=+1.5e21 (encompasses previous 2D legend), inspect whether signed spikes are visible. If still flat, stop repetitive plotting and use numeric probe/export of interface charge or field mapping for a signed verification. No code changes or new simulation.

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

## 2026-10-23 — Lee completed 3.6V Ec/Ev/eQF/hQF visual audit (OBSERVED; NO RUN)
- User SVisual screenshot: existing n2_end_des final 3.6V shows four overlaid 1D Cutline_Y traces versus depth X~0.14–0.29um: ConductionBandEnergy (magenta), ValenceBandEnergy (cyan), eQuasiFermiEnergy (red), hQuasiFermiEnergy (blue). Also n2_eq_des equilibrium quasi-Fermi reference (green near 0eV). Cutline nominal lateral Y=1.0um from preceding user setup, though screenshot itself does not show per-curve coordinate dialogs.
- OBSERVED: Ec/Ev show four well-associated notch/step features consistent visually with V2.1 four QWs; biased e/h quasi-Fermi energy profiles change in stair-step fashion near well interfaces. The curves are qualitative screenshot evidence only, not extracted barrier energies, polarization charge or a quantitative transport validation.
- CONTEXT from prior direct SVisual probes at nominal four QW centers: QW4 versus QW1 electron density ~303x and hole density ~331x; previous QW4 2D QW-radiative integral share ~99.9688% remains an unresolved physical-credibility warning. Center-local n*p correlation does NOT establish the cause or prove a valid calibrated 4um device.
- CONCLUSION: the planned SVisual Ec/Ev/QF first-pass GUI inspection is complete; do not request more redundant curve screenshots now. V2.1 remains OPERATIONALLY RUNNING, PHYSICALLY UNVALIDATED; QW4 carrier concentration mechanism, polarization sign, band offsets/injection physics, exact 2D current normalization, matched-J trap comparisons and full-vs-half remain unresolved. Existing server decks and runs unchanged; no new runs.
- NEXT READ ONLY: inspect active preprocessed deck material and polarization parameter/sign/orientation against QW region mapping, verify 2D contact/current units and existing n2/n6 whole-device current/recombination balance and matched-J; then decide whether targeted validation/sensitivity run is necessary. Do not freeze publication-grade baseline or change model speculatively.

## 2026-10-23 — Lee 3.6V valence band versus hole quasi-Fermi overlay (OBSERVED screenshot; NO RUN)
- In SVisual, user added the biased n2_end_des ValenceBandEnergy trace (cyan) to the same Cutline_Y plot carrying n2_end_des hQuasiFermiEnergy (blue), eQuasiFermiEnergy (red) and n2_eq_des equilibrium quasi-Fermi reference (green). Nominal depth X ~0.14–0.29 um; prior lateral Cutline Y=1.0 um, not reverified in shown properties.
- OBSERVED visually: cyan valence-band trace exhibits four well-related upward features and varies with depth, while blue hole quasi-Fermi shows corresponding step-like changes. Vertical proximity between cyan/blue varies by position. No quantitative local energy gaps, layer labels, offsets or carrier concentrations can be extracted reliably from screenshot alone.
- QW4 n/p ~300x QW1 observation and ~99.97% radiative concentration are not causally explained by this overlay; polarization correctness still UNRESOLVED. No simulation rerun or source edits.
- User requested to limit repeated GUI checks. NEXT short read-only visual check: add biased n2_end_des ConductionBandEnergy to this graph to compare Ec/Ev/eQF/hQF at same Y and X, then summarize observations versus unresolved physics. Full calibration, current normalization, matched-J and Full/Half validation remain separate gates.

## 2026-10-23 — Lee hole quasi-Fermi SVisual (OBSERVED; NO RUN)
- In SVisual, hQuasiFermiEnergy blue cutline was added beside prior 3.6V red eQuasiFermiEnergy and green equilibrium reference. At depth x approx 0.14–0.29 um, blue is visually around -3.6 to -3.0 eV and red around -1 to 0 eV, both showing step-like changes. Previous lateral cutline was Y=1.0 um; exact current curve properties are not displayed.
- This confirms visually distinct electron/hole quasi-Fermi profiles, not the physical cause of QW4 carrier accumulation or correctness of polarization/band alignment. No numerical values exported. No code or simulation changes.
- Next read-only: compare end-state conduction and valence band energies with both quasi-Fermi curves at identical coordinates; validate well and interface locations.

## 2026-10-23 — Lee n2 eq/final electron quasi-Fermi energy cutline (OBSERVED SCREENSHOT; NO NEW RUN)
- User SVisual screenshot shows plots for n2_end_des (left, previously completed 3.6 V) and n2_eq_des (right, equilibrium) with electron quasi-Fermi energy color maps; lower Cutline_Y Plot overlays a red biased profile and green equilibrium profile across depth X about 0.14–0.29um. Previous cutline setup was lateral Y=1.0um; individual cutline-property dialogs are not displayed in this screenshot.
- OBSERVED visually: equilibrium green eQuasiFermiEnergy nearly horizontal at approximately 0 eV in the displayed frame; 3.6V red curve climbs stepwise from approximately −1 eV on p-side to 0 eV toward n-side, with multiple sharp changes near nominal four-QW stack. These are rough readings from an image, not exact exported numbers.
- INTERPRETATION LIMIT: this alone does not verify band alignment, correct polarization sign, quasi-Fermi continuity across heterointerfaces, cause of QW4 99.97% radiative share, or the validity of physical injection. Need proper field-reference and local band/QF comparison before claiming an electron-injection barrier.
- NEXT READ ONLY: inspect hQuasiFermiEnergy in n2_end_des on same X 0.14–0.29um, Y~1.0um; then align with eQuasiFermiEnergy and Ec/Ev at same Y and check well regions. No code changes or new simulations.

## 2026-10-23 — Lee n2_eq vs n2_end valence-band cutline overlay (OBSERVED SCREENSHOT; NO RUN)
- SVisual screenshot shows ValenceBandEnergy for n2_eq_des (green, equilibrium) and n2_end_des (red, previously completed final 3.6 V) in the same depth plot x~0.14–0.29um. This follows the existing matched cutline setup nominally lateral Y=1.0um, but per-curve coordinate property windows are not separately shown in screenshot.
- OBSERVED: equilibrium valence-band curve drops strongly as depth increases, with four well-associated upward notches; 3.6V curve is much flatter, with four upward step/notch features. Plot broadly consistent with four QWs in existing nominal stack; exact barrier heights and polarization sign cannot be verified by this screenshot alone.
- LIMIT: different energy reference/voltage offsets can affect cross-state curve positioning. No claim of physically validated injection, no inference of QW4 high carrier cause or correct polarization from visible curves alone.
- NEXT READ ONLY: inspect electron and hole quasi-Fermi energy profiles at 3.6V on the same lateral Y~1.0um cut and compare to Ec/Ev locally, then investigate polarization/band offsets/region labels. Preserve all existing TCAD deck and results.

## 2026-10-23 — Lee n2_eq vs n2_end Ec cutline overlay (OBSERVED SCREENSHOT; NO NEW RUN)
- User SVisual screenshot shows two existing datasets `n2_eq_des` (green) and `n2_end_des` (red; prior run final 3.6 V), both ConductionBandEnergy plotted together versus depth X about 0.14–0.29um. Two 2D view cutline traces appear near lateral Y~1.0um; prior user setting was Y=1.0um for both. This screenshot alone does not display exact numeric cutline properties for both traces.
- Both plots show multiple narrow/notched conduction-band features near nominal QW x~0.1895/0.2145/0.2395/0.2645um, broadly consistent with known 4-QW stack. Equilibrium and biased band profiles are visibly different, but band-energy reference/offset, polarization sign, and carrier accumulation mechanism cannot be determined from this Ec screenshot alone.
- Physical baseline still UNRESOLVED: especially why QW4 n and p densities increase relative to QW1. No values digitized from image; no new simulation, source or parameter modification.
- NEXT READ ONLY: keep same X 0.14–0.29um and Y 1.0um; overlay `ValenceBandEnergy` for `n2_eq_des` and `n2_end_des` and inspect QW1–QW4; then examine electron/hole quasi-Fermi levels and polarization if available. Preserve original V2.1.

## 2026-10-22 — Lee n2 3.6V four-QW center density probes and Bnp check (OBSERVED + DERIVED; NO RUN)
- User-provided SVisual n2_end_des, Cut Y both hDensity(Curve_1) and eDensity(Curve_2) at lateral Y=1.0um. Nominal QW centers from existing V2.1 vertical source stack: x[um]=QW1 0.1895, QW2 0.2145, QW3 0.2395, QW4 0.2645. Probe readouts [cm^-3]: QW1 p=3.42849e15,n=4.46006e15; QW2 p=4.47871e15,n=4.99354e15; QW3 p=1.82582e16,n=2.04189e16; QW4 p=1.13508e18,n=1.35190e18. GUI numeric readout = OBSERVED screenshot; nominal material-center alignment = DERIVED from earlier verified preprocessed stack; not re-probed region labels.
- Derived center n*p [cm^-6]: QW1=1.52912711e31; QW2=2.23646175e31; QW3=3.72812360e32; QW4=1.53451465e36. QW4 center n*p / sum(QW1-3 center n*p) ≈ 3738.45. Equal-B point-product QW4 share ≈99.973258%, numerically close to prior actual 2D QW radiative-integral QW4 share ~99.9688%. QW4 p/pQW1≈331.07, n/nQW1≈303.11; n/p(QW4)≈1.191. Thus evidence supports a strong carrier-overlap correlation for QW4 radiative dominance; Claude's hypothesized n~1.6e19 and p~8e16 at QW4 is not reproduced at THIS x,y.
- CRITICAL CAUTION: single-point B*n*p surrogate is NOT 2D integrated spontaneous-radiative-recombination evidence, and cannot establish cause of carrier buildup or physical correctness. Full field, polarization sign, equilibrium/biased band profile, quasi-Fermi, actual net charge and 2D QW-region integrals are not fully validated. Avoid claiming numerical 99.973% as actual IQE or proof of model validity.
- NEXT READ ONLY (priority updated): stop repetitive spot-probing; compare QW1 vs QW4 equilibrium and biased Ec/Ev (and electron/hole quasi-Fermi), polarization charge sign and carrier profiles on same lateral Y=1.0um; confirm well region mapping. Then review existing full 2D QW radiative and current balance, matched-J n2/n6. NO code edits/new simulations.


## 2026-10-22 — Lee QW4 center X0.2645 hDensity and eDensity direct probe (OBSERVED screenshot; NO NEW RUN)
- User SVisual n2_end_des final at 3.6V, Cut Y lateral Y=1.0um user-confirmed, used Probe At X=0.2645um (nominal QW4 center from previously verified V2.1 stacking X0.263–0.266um). Probe GUI Curve_1 hDensity=1.13508e18 cm^-3 and Curve_2 eDensity=1.3519e18 cm^-3; ratio n/p ~1.191. Both are comparable at this center point.
- Claude-proposed electron-rich n~1.6e19 and hole-poor p~8e16 cm^-3 is NOT reproduced by this one-point sample; it may refer to a different derivation or location and was never verified. No QW4 integrated radiative mechanism conclusion; 2D location sample not QW-wide distribution or optical IQE.
- NEXT read-only: at same Y=1.0um acquire numerical e/h at nominal QW1/2/3 centers X=0.1895, 0.2145, 0.2395um respectively, compare across wells; later cross-check QW-resolved RadiativeRecombination integrals and source geometry. Server source/runs unchanged.

## 2026-10-22 — Lee n2_end QW4 boundary probe X0.266 (OBSERVED screenshot + DERIVED alignment, NO RUN)
- At user-verified lateral Y=1.0um, n2_end_des 3.6V SVisual Probe At depth X=0.266um: red hDensity 8.27385e19 cm^-3, green eDensity 7.7108e15 cm^-3 (user screenshot). Prior X=0.265um gave h=4.96786e18, e=3.00217e17 cm^-3. Across 1nm to the deeper location, hole rises ~16.7x and electron drops ~38.9x. This is local point variation near a narrow interface; cause and 2D-integrated radiative consequence UNRESOLVED.
- IMPORTANT GEOMETRY CROSS-CHECK: Existing GitHub source-derived V2.1 stack contains 0.020um pCap, 0.120um pGaN, 0.026um EBL, 0.022um barriers, 0.003um QWs; predicts QW1 0.188–0.191, QW2 0.213–0.216, QW3 0.238–0.241, QW4 0.263–0.266um (X vertical). Thus X0.266 is nominal QW4/bottom-barrier interface, not reliable bulk-well-centered sample. QW4 nominal center X0.2645um. This differs from older CAL4V x~0.2445 center because V2.1 additionally has a 0.020um pCap. Actual region coordinates in current SVisual not separately probed, so mapping DERIVED from prior verified stack.
- NEXT read-only exact SVisual Probe At X=0.2645um on both n/p curves at matched lateral Y1.0um; then nominal QW1–3 centers for side-by-side local density comparison. Do not infer QW4 99.97% integral solely from pointwise concentrations. No code changes or new simulation.

## 2026-10-22 — n2_end probe X=0.265um hDensity 4.96786e18 (OBSERVED screenshot; NO RUN)
- 이택규가 SVisual Probe At 창에 X=0.265um를 입력, Apply하여 n2_end_des 3.6V의 Y=1.0um Cut Y 두 곡선 동일 깊이에서 측정함. hDensity(Curve_1)=4.96786e18 cm^-3, eDensity(Curve_2)=3.00217e17 cm^-3 (user screenshot). Pointwise h>e; this location by itself does not confirm or reject any QW4-averaged carrier-imbalance hypothesis. True QW4 center/region bounds are not independently verified. Data values from GUI probe, not newly run simulation.
- NEXT: verify QW4 actual X bounds using Regions/material/mesh, then probe at verified center and several QW centers at same lateral Y; compare region-integrated recombination. No deck/model modification.

## 2026-10-22 — Lee narrow QW4-adjacent probe x0.262955 observation (OBSERVED, no new run)
- User clicked near green electron-density peak in n2_end_des 3.6V Cut Y at Y=1.0um. Probe shows X=0.262955um, hDensity=1.3111e13 cm^-3, eDensity=3.20976e12 cm^-3. This sample is near/before narrow spike, not verified QW4 peak or well center. Mouse selection is inadequate for peak extraction until exact region coordinate established. Next inspect SVisual Probe At dialog for precise X probing. No TCAD changes. Issue #7 comment 6337912698.

## 2026-10-22 — Probe x0.26177 n2_end 3.6V density (OBSERVED USER SCREENSHOT; NO NEW RUN)
- Sentaurus Visual n2_end_des, Cut Y at user-confirmed lateral Y=1.0um, numerical Probe depth X=0.26177um: red hDensity(Curve_1)=2.63775e13 cm^-3; green eDensity(Curve_2)=2.11675e12 cm^-3; h/e=~12.46 at THIS coordinate. Probe screenshot directly shows these numerical values.
- WARNING: the selected vertical probe appears left of the rightmost narrow carrier peak; no demonstrated exact QW4 material center. Therefore values cannot yet confirm/refute Claude-derived QW4 carrier densities or explain QW4 ~99.97% radiative integral. Numeric readout reflects a single lateral cut, not the QW region-integrated recombination.
- NEXT read-only: use Probe at highest rightmost peak, then verify against QW region boundary/center; retain both n/p values at identical x,y. No TCAD edits or new runs.

## 2026-10-22 — Both n2_end carrier Cut Y coordinates confirmed Y=1.0um (USER-REPORTED; NO NEW RUN)
- 이택규가 Sentaurus Visual n2_end_des의 hDensity(C1) 및 eDensity(C2) Cut Y를 모두 lateral Y=1.0um로 맞추었다고 명시함. 스크린샷에 두 곡선이 QW 영역 depth X~0.14–0.29um에서 겹쳐 보이며, 네 개 well-adjacent carrier peaks가 시각적으로 확인됨. 정확한 QW별 전자/정공 숫자 및 방사 재결합 분포의 인과는 아직 미확인.
- NEXT: SVisual data probe/export로 같은 Y=1.0um, 각 QW 중심의 n/p 숫자를 확인하고 원래 QW 방사 적분과 대조. 독립 시뮬레이션, 코드/파라미터 수정 없음.

## 2026-10-22 — Lee 3.6V n2_end dual-carrier Cut Y plot observation (OBSERVED screenshot; NO RUN)
- n2_end_des SVisual 3.6V Cutline_Y screenshot: red hDensity(C1), green eDensity(C2) plotted against depth X~0.14–0.29 um in log units cm^-3. Four well-adjacent peaks visible; electron background increases and hole background decreases with depth toward n side. Exact sample Y positions for distinct C1 and C2 are not yet verified; no per-well numerical values, band/polarization conclusions or explanation of 99.97% QW4 radiative share established.
- Next: verify C1 and C2 have identical fixed Y near 1um, then extract n/p at QW1–4 with numerical probe and reconcile with QW radiative integrals. Existing deck/results unchanged. Issue #7 comment 6337505672.

## 2026-10-22 — Lee V2.1 n2_eq SVisual Cut Y conduction band (OBSERVED USER SCREENSHOT; NO RUN)
- User opened n2_eq_des and n2_end_des in Sentaurus Visual, selected ConductionBandEnergy in equilibrium n2_eq and generated Cutline Y plot. Screenshot's horizontal depth X~0.145–0.285um, displayed energy trend with four repeated notches/well-like band features near X~0.19, 0.215, 0.24, 0.265um. These appear consistent with four QWs, but exact Cut Y coordinate and region labels are not visible in the 1D screenshot and therefore remain UNVERIFIED.
- A tilted/sawtooth-looking Ec under equilibrium is NOT proof of correct polarization sign, band offsets or physical calibration. It does NOT explain the 3.6V QW4 99.97% radiative share on its own.
- NEXT READ ONLY: in n2_end_des (biased final state), select hDensity and make Cut Y at the same fixed Y~1.0um, depth X~0.14–0.29um; then eDensity, preferably logarithmic density axis. Check y coordinate in cutline properties. No TCAD source, run or parameters changed by AI.

## 2026-10-22 — Claude V2.1 독립 검토 인계 (USER-SUPPLIED, PROPOSED, 새 RUN 없음)
- 작업자 이택규, Project A. Claude 판정 B: 구조 유지 + 필수 검증, 확신 중간 이하. 이는 검토 의견이지 검증 완료/베이스라인 확정 아님.
- Claude 주장 근거: SWB_PASTE SHA256 prefix SDE 907d267c, SDevice c01ab2c1, PAR 826b63c7, LOG #01/#02, T-2022.03 UG pp.58–59,253,473,580. 서버 active 덱 동일 여부 및 n2/n6 PLT/TDR 원문 Claude 미확인; Wang 2023 원문만 접근 보고. 이번 인계에서 원 보고서와 원시 로그를 별도 검증하지 않음.
- 다른 크기의 Kou J=20A/cm2 사례로 우리 3.6V 저전류를 injection failure라 단정하는 과거 해석 기각 제안. n_id~2.3은 Claude 보고값으로 독립 재계산 전.
- QW4 전체 방사 기여 약 99.97%, Auger QW 3채널 약 27.5%는 기존 결과; Claude는 QW4가 n측 우물이며 n~1.6e19, p~8e16cm^-3이라고 DERIVED 제시하나 유도 원문 미제공, 독립 검증 전. CAL4V QW1 98.7% 비교도 reviewer-reported.
- QW 3채널 rad/(rad+SRH+Auger)은 gap-state trap loss를 직접 포함하지 않음. Claude UG pp.253/473/580에 SRHRecombination 및 eGapStates/hGapStatesRecombination 구분을 인용(페이지 자체 재검증 안함). 전류와 적분 단위, 보존 확인 후 같은 J에서 q×QW 방사 적분 / 단자 전류 지표 비교 제안; 실측 IQE로 표현 금지.
- 5nm Dmg는 2um Half 폭의 0.25%지만 n6 전류 1/4은 gtree 및 수치/비선형 depletion 검증 필요. 폭만으로 전류 감소가 불가능하다고 단정하지 않음. 2D stripe P/A 0.5/um vs 4x4 square 1.0/um. Equivalent S~1e4cm/s는 가정 v_th=2e7cm/s에 의존한 도출값이며 보정 전.
- READ ONLY 다음: 기존 n2_eq_des.tdr 및 n2_end_des.tdr 존재/필드명 확인 후 y=1.0um x=0~0.40um cutline으로 polarization charge sign, Ec/Ev, hDensity/eDensity, 우물별 n/p, QF 검증. 이어 n2/n6 PLT와 bl2_check.py 전류 수지/동일 J 검증; gtree 차이 및 full I-V; 필요하면 승인받고 단일 변수 민감도. 논문 전 2D geometry 보정 검토. Claude cutV21.tcl 스크립트는 인계에만 언급, 원문 제공 안됨.
- 판정 변경 조건은 제안: polarization 부호 또는 밴드 오프셋 확정 오류면 C 재평가. Claude의 qR/I<0.9 조건은 보편적 leakage 임계값이 아니므로 자동 C 판정 금지. 기존 코드/서버 런 변경 없음.

## 2026-10-22 — Lee Project A: 4um Baseline reference framework and IQE metric audit (SOURCE-VERIFIED, MODEL_UNCALIBRATED)
- USER concern is scientifically valid: CMP V2.1 is a self-designed **hybrid representative 4um mesa** model, NOT Kou 2019 model reproduction (Kou laterals 20/60/100um). Kou's 4-QW In0.15/3nm, barrier22nm, EBL26nm and vertical GaN doping/thickness can serve as design-source EPI; Wu 2023 5nm acceptor sidewall is separate physical starting assumption. Neither supplies size-matched 4um TCAD efficiency benchmark, and 4um pitch JBD != verified mesa.
- DIRECT real-size literature: Chen et al ACS Applied Electronic Materials 2024 DOI 10.1021/acsaelm.4c01540 fabricated 4x4um² blue LEDs, nitrogen treatment light output +97.29% at J25A/cm² (relative optical output, NOT IQE). Wang et al Nature Communications 2023 DOI 10.1038/s41467-023-43472-z fabricated 3.5x3.5um² blue, **16 MQWs** and NBE, peak **EQE** 37.5% around J3A/cm² (NOT 4-QW IQE). Also Ryu&Geum Opt Express 2026 DOI 10.1364/OE.580848 gives size-dependent SRV/diffusion length IQE framework, no literal equal-parameter benchmark. Validated 4um physical existence/trends, not a single exact device/parameter ground truth.
- IQE definitions need precision: QW recombination internal efficiency `∫QW Rrad/(∫QW Rrad+SRH+Auger)` is a **QW-only three-channel** property; full-device current-normalized internal photon-generation yield `q∫QW Rrad / I_terminal` (with exact 2D width/conservation/leakage checked) accounts for sidewall/trap/carrier loss and is apt Project A comparison; whole-device `∫Rad/(∫Rad+SRH+Aug+Trap)` approximates same when full recombination current closes, but not external photon EQE or independently validated absolute IQE. EQE=η_injection×η_QW_rad×LEE under consistent definitions. Existing n2 QW-rad~66.9624%, n6 QW-rad~67.7744%, n6 global trap-inclusive rad fraction~44.4096%, n2 tentative current-normalized ~66.9506%; ALL model outputs not measured physical standards and ON/OFF at equal voltage 3.6V, different current.
- KEY CRITICAL GEOMETRY GAP: planar 2D full width 4um models an infinitely long stripe with two lateral sidewalls, P/A_eff =2/W=0.5 per um; physical square 4x4um has four walls P/A=4/W=1 per um, factor 2 geometry difference even at same width (assuming straight walls). Half2um doubling to planar Full4um checks numerical reflection/symmetry, NOT true square's sidewall P/A, edge/corner, nor real 3D leakage. Do not multiply Nt by 2 indiscriminately: space charge/current spreading nonlinear and calibration needed.
- PARAMETER BASIS CURRENTLY UNRESOLVED: 4um mesa representative hypothesis; 5nm sidewall damaged width from Wu; acceptor Nt1e18, Et Ev+.75eV, sigma1e-15 are **calibration starting choices**, not measured 4um C-device values. Active model PolAct0.5, mobility, pGaN hole activation, QW radiative B, Auger C, contact/AreaFactor need an explicit reference/provenance table and tests. n2 3.6V QW4 radiative ~99.9688% and Auger QW-3chan~27.53% remain red flags, not failed physics proof.
- **RESEARCH DECISION PROPOSED (NOT USER FINAL FREEZE):** Retain Kou EPI as documented representative design; add Chen 4um and Wang 3.5um as SIZE-SPECIFIC experimental phenotype/benchmark, Wu as 5nm sidewall mechanism, ABC/SRV size dependence as IQE modeling source, and GaN:C compensation source for Project A when separately validated. No paper offers exact "4um with Kou QWs plus Wu traps" IQE target. Treat n2/n6 as operational pilot, not publication-calibrated baseline; no need restart everything.
- NEXT first phase without sim edit: freeze/report **parameter provenance matrix** (DIRECT literature / adopted modeling assumption / numerically adjusted), **current normalization and 2D-vs-square P/A**, **IQE metric definitions**, then extract existing n2/n6 modeled radiative/trap metrics versus common J; check QW4/physics. Only afterwards compare GaN:C ON+carbon to same ON damage no-carbon control, not to unrealistic Trap OFF as primary experimental performance. Protect both workstreams' original projects.

## 2026-10-22 — 4um transferability of Kou EPI and size-matched benchmark reconsidered (SOURCE VERIFIED; VALIDITY UNRESOLVED)
- User flagged that Kou 2019 simulations use 20/60/100um chips and questioned transplanting all parameters into 4um. Decision: copying **vertical epitaxial thickness/composition** as an initial representative 4um model is physically defensible (epitaxial layers do not scale proportional to lateral mesa), but paper's lateral contact/spreading/damage/SRH, J-V and EQE cannot be directly transferred or treated as calibrated outcomes. JBD 4um pixel pitch is NOT experimental 4um mesa width. 2D planar Half/Full does not exactly reproduce 4-sided square (or circular) mesa geometry and corner/surface-area effects.
- From Kou official Open Access full text, Fig1/Table context: damaged dead zone was **4um lateral width** in its 20/60/100um models; this is not rescalable as a literal 4um dead-zone width into a 4um mesa. Our 5nm Wu-inspired damage region is a separate sidewall model; 5nm physical region width does not imply capture/depletion influence is confined to 5nm. Square 4x4um perimeter/area=1um^-1 versus 20x20um=0.2um^-1, i.e. 5x geometry sensitivity, even if vertical layer thicknesses match.
- New size-matched references: Wang et al. Nature Communications 2023 open access https://www.nature.com/articles/s41467-023-43472-z (actual 3.5x3.5um blue microLED, 16 QWs, neutral beam etch/passivation, EQE peak near **3A/cm2**, EQE peak ~37.5%; different epitaxy and treatments). Chen et al. ACS Applied Electronic Materials 2024 https://doi.org/10.1021/acsaelm.4c01540 (4x4um mesa, nitrogen plasma sidewall treatment, optical power enhancement 97.29% at 25A/cm2; different experiment). These demonstrate 3.5-4um feasibility but ARE NOT same-device J-V or absolute-IQE numerical ground truth for CMP.
- **Correction to prior overstrong warning**: provisional CMP n2 3.6V J~1.824A/cm2 vs Kou J20A/cm2 at lower voltage is a structurally confounded contrast and **does not prove serious injection failure** in a 4um device; Wang 3.5um study demonstrates that ~few A/cm2 is a meaningful operating regime. The question should be whether CMP internal physics, contacts, 2D normalization, recombination and traps are self-consistent and benchmarked to size-appropriate cases; current QW4 99.97% + conditional Auger~27.5% remain unresolved flags.
- NEXT: keep 4um representative size, Kou vertical epi, Wu inspired 5nm damage as PROVISIONAL; validate area/current definition, contact/vertical GaN geometry, 2D-vs-square limitations and physically reasonable QW recombination/trap effect before calling Baseline frozen. Prefer matched-current n2/n6 and 3.5/4um size papers for **qualitative** trends; no blanket need to rescale EPI, no code or simulation modified.

## 2026-10-22 — Kou full text Open Access and "no injection" wording corrected (SOURCE VERIFIED)
- User questioned Kou 4um size, paywall and meaning of "current injection not working." Independently opened Optica Publishing Group official full-text page https://doi.org/10.1364/OE.27.00A643; journal page explicitly marks **Open Access** and displays full Sections 1–4, figures/captions. No paid purchase required to read HTML full text; separate PDF direct-open not needed nor claimed.
- Kou 2019 Section2: nGaN **thickness**=4um; **4 quantum wells**; lateral chip sizes are 20x20,60x60,100x100 um², NOT 4um mesa. Our CMP intended representative mesa 4um (JBD pitch should not be equated to mesa width), Kou used as vertical epitaxy backbone; earlier reference-size correction stands.
- At **applied terminal voltage** V=3.6V, CMP V2.1 nonzero n2 current raw3.64728525e-8 and n6 raw9.21970771e-9; conditional planar J~1.824/0.461 A/cm². Kou Fig3 reports **20 A/cm²** at V3.23–3.48V for different-sized and different-model devices. Therefore at same order terminal bias CMP shows much lower normalized current; "전류 주입이 안 된다" wrongly suggests zero injection or a proven mechanism. Correct statement: model has measurable forward current and radiative recombination but **relative forward J is low**, while whether it reflects injection barriers, interface polarization, Mg hole activation, mobility/contact series resistance or geometric/trap-model differences remains **unresolved**.
- Distinguish terminal J(V) (total electrical conduction) from injection efficiency (portion of carriers entering/recombining in MQWs). Same terminal V need not result in same J if internal voltage drops/barriers/resistance and structure differ; terminal V is not direct voltage across wells. Lower terminal J alone is NOT direct evidence that carriers fail to enter wells nor proof of poor injection efficiency. Kou abstract and Sections3 indicate trap-caused carrier loss via sidewall SRH; their traps form leakage path (different direction than CMP ON current reduction), requiring matched current/physics audit.
- NEXT: compare same area-normalized J and evaluate injection through carrier currents/profile, bands/quasi-Fermi and per-QW radiative/sidewall traps; preserve V2.1 baseline. No simulations or code changed.
## 2026-10-22 — Project A Kou 2019 / Wu 2023 benchmark audit
- Worker reaffirmed: **이택규 Project A (carbon-induced high-resistivity GaN:C sidewall edge)**; 주수빈 Project B (AlGaN). Prevent mixing user ownership or claiming both are completed.
- Primary reference Kou et al., *Impact of the surface recombination on InGaN/GaN-based blue micro-light emitting diodes*, Optics Express 27 A643-A653 (2019), DOI https://doi.org/10.1364/OE.27.00A643. Paper Section 2 vertical epitaxy: nGaN 4um donor 5e18 cm^-3, 4×In0.15Ga0.85N QW 3nm, barrier 22nm, EBL 26nm Al0.15Ga0.85N, pGaN 120nm, p-layer holes 3e17 cm^-3, p+ cap20nm, ~445nm. Most of intended V2.1 stack matches design dimensions, BUT actual pGaN free hole profile and optical ~445nm emission unverified; ours has changed contact/half setup and 4um nominal mesa.
- Paper's size models are **20x20, 60x60, 100x100 um²**, not 4um. Kou damaged **dead zone width 4um**; sidewall electron trap Ec−0.24eV density1e13 cm^-3 sigma3.4e−17cm²; hole trap Ev+0.46eV density1.6e13 cm^-3 sigma2.1e−15cm². Their numerical method APSYS, Auger coefficient1e−30 cm^6/s, SRH lifetime1e−7s; ours Sentaurus V2.1 Wu-inspired **5nm** damaged region acceptor trap Ev+0.75eV Nt=1e18cm^-3 sigma_n/p=1e−15cm² calibration starting values and Auger 5e−31 (reported pp2_des.par). DO NOT claim Kou's IQE/Trap parameter numerical replication. Wu et al. 2023 DOI https://doi.org/10.1016/j.micrna.2023.207542 uses 5nm sidewall acceptor-like traps, representative example 10um with 4 QWs In0.08, GaN barrier8nm (different epi).
- **Direct numeric benchmark Kou Fig.3:** At J=20 A/cm², forward voltage Trap-free (sizes 100/60/20um) 3.48/3.37/3.33V; defective counterparts 3.47/3.33/3.23V. Existing school-server V2.1 at 3.6V, using provisional 2D planar 2um×1um area, J_n2_OFF=1.823642625 A/cm² and J_n6_ON=0.4609853855 A/cm². Compared with paper's benchmark 20 A/cm² at LOWER 3.23–3.48V, ours at higher 3.6V is ~10.967× (OFF), ~43.385× (ON) less than 20 A/cm². This is a material mismatch/check flag, NOT conclusive physical error due to major size, geometry, trap, contacts, models, normalization differences. Do not extrapolate paper I-V to precisely 4um without new data.
- **Trap direction flag:** Kou Fig.3 trap-affected 20um device achieves J20 at 3.23V vs no trap 3.33V (leakage channel effect); ours at equal 3.6V ON/OFF current ratio0.2528 (Trap ON suppresses terminal I). Not directly comparable bias or material; warrants verifying actual sidewall depletion, terminal current path, trap recombination and leakage. Matched-J IQE and Project A high-resistance edge mechanism cannot be concluded from terminal current alone.
- Existing V2.1 n2 PLT QW4 contributes ~99.9688% of QW total radiative; Kou/Wu retrieved text does not provide identical per-QW 4um metric for quantitative validation. e/h-density 1D cut peaks deepest-highest, but does not establish 2D physical plausibility. Under provisional J_n2~1.824A/cm², QW Auger three-channel fraction27.53%; literature typical lower-current Auger smaller (https://pmc.ncbi.nlm.nih.gov/articles/PMC8175512/) -> investigation priority, NOT automatic model error because local carriers can accumulate strongly.
- **VERDICT:** Structural epitaxy broadly matched; qualitative sidewall damage reduces recombination in Wu/Kou and n6 relative to n2 (same 3.6V) aligns; V2.1 is NOT QUANTITATIVELY BENCHMARKED to Kou-level forward injection, not an independent calibrated IQE/EQE or 445nm proof; may not safely freeze baseline for final Project A claim.
- NEXT READ-ONLY: 1) use existing n2/n6 PLT to extract J-V at equal J within common range and modelled radiative/trap balance; verify exact 2D contact/current scaling and target current injection. 2) Inspect current active physics, EBL/hole injection and transport, EPI material settings and polarization against Kou assumptions—no speculative code editing. 3) Check QW4 99.97% and Auger share physical reason with spatial integrated data. 4) independent protected Full-vs-Half run for symmetry once Half audit passes. Existing V2.1 source and finished runs untouched. Project A may advance as isolated exploratory pilot but cannot make calibrated performance/efficiency claims before benchmark.
## 2026-10-22 — QW-only 3-channel ratio versus all-device trap-inclusive radiative share clarified (DERIVED)
- User asked for "전체 IQE" using existing 3.6 V PLT results. Important distinction: n2 QW-only 3-channel Radiative/(Rad+SRH+Aug) = 66.9623837%; n6 QW-only = 67.7744% (excludes gap-state trap). Both are NOT verified absolute device IQE.
- n6 all-device raw PLT integrals Rad=2.55552035945039e22, SRH=4.32337288643595e21, Aug=7.83993596604716e21, Trap eGapStates=1.98258247754075e22. Derivation Rad/(Rad+SRH+Aug+Trap)=44.4095889%; trap fraction=34.4531291%. This is a trap-inclusive full-device radiative recombination CHANNEL FRACTION, which is useful as a conditional model-based IQE proxy, NOT a calibrated/external IQE measurement. Prior conditional q×1e-12 current closure~99.99904% supports consistency, not independent physics confirmation.
- n2 `IntegrTrap_all` 1.17883032e6 raw negligible; QW-only Rad/(QW Rad+SRH+Aug)=66.9623837% is an approximate proxy for full-device radiative fraction, because n2 ALL-DEVICE Rad/SRH/Aug integral values were not independently extracted. Alternative q×QW Rad×1e-12/I_anode ≈66.95058% conditional on numerical unit convention. Do not falsely label 66.96% as an exact all-device integral result.
- Same-voltage n2/n6 compare at different currents, so 66.96%-44.41%=~22.55 percentage-point proxy difference is NOT matched-current trap causality. QW4 99.97% localization is separate distribution concern, not itself evidence of IQE reduction. Original simulator/code unchanged.

## 2026-10-22 — QW depth mapping derived from verified V2.1 epitaxy (DERIVED, not separately probed)
- Cross-checked GitHub RELAY and CURRENT_STATUS: user-observed actual pp1_dvs.cmd stack pCap 0.020um, pGaN 0.120um, EBL 0.026um, B0..B4 each 0.022um, QW1..QW4 each 0.003um, depth X from 0 at top. Arithmetic: QW1 X 0.188–0.191um; QW2 0.213–0.216; QW3 0.238–0.241; QW4 0.263–0.266. These predicted QW depths closely match visually read h/eDensity peaks around 0.190/0.215/0.240/0.265um.
- This supports localization of the four peaks to the well intervals at plotted resolution, stronger than unlocated peak inference; still NOT precise numeric electron-hole overlap or explanation for integrated QW4 radiative ~99.9688%. Source references: CMP/.ai-sync/RELAY.md and CMP/CURRENT_STATUS.md (2026-10-22 JuSubin SDE stack review). No new TCAD simulation, read-only derived result.

## 2026-10-22 — n2 QW eDensity Cutline_Y depth zoom observed (IMAGE; CAUSALITY UNRESOLVED)
- User SVisual screenshot of `eDensity(C2(n2_end_des))` at existing lateral Y≈1.3um, graph depth X≈0.14–0.29um: four sharp eDensity peaks around X≈0.19/0.215/0.24/0.265um; the deepest peak looks highest and subsequent n-side concentration rises. Precise peak values/region attribution are NOT extracted; maxima may lie at QW interfaces/barriers, not proven inside wells.
- Earlier same-cut hDensity also has highest deep peak. This supports qualitatively correlated deep-side electron/hole accumulation, not proof that QW4 dominates due to carrier overlap. Independent integrated n2 QW4 Radiative share ~99.9688% (QW4 about 3.2e3 times QW1–3 combined) remains unusually extreme and merits quantitative physics validation. Do not equate local cut peaks with 2D integrals or calibrated IQE.
- To save time, do not repeat visual zoom. Next audit alignment with exact QW region boundaries and quantitative recombination/current benchmark; then protected independent Full/Half comparison. Original SDE/SDevice/run unchanged.

## 2026-10-22 — n2 eDensity cutline started
- Observed SVisual eDensity(C2(n2_end_des)) on the existing Y~1.3um cutline. Right graph X-depth range reset to 0..4.288um on field change; QW peaks not yet resolved. Next set plot X fixed min0.14 max0.29um. No TCAD files/runs changed.

## 2026-10-22 — n2 Cutline_Y hDensity 4QW peaks resolved (OBSERVED IMAGE, PEAK VALUES ESTIMATED)
- User Sentaurus Visual Cutline_Y plot screenshot `hDensity(C2(n2_end_des))`, lateral Y~1.3um, depth X~0.14–0.29um, log density Y-axis ~1e10–1e20 cm^-3.
- Four local hDensity peaks correspond spatially to QW depths ~X0.190, 0.215, 0.240, 0.265um (assignments based on prior V2.1 epitaxy). Approximate plot-read peak values QW1 ~9e18, QW2 ~1e19, QW3 ~2e19, QW4 ~8e19 cm^-3. These are graphical estimates, NOT numerically extracted SVisual data; actual per-region integrals/peak measurements remain unverified. Visible increasing hole-density trend and highest QW4 peak at this interior Y cut.
- Previous independent n2 PLT QW4 radiative integral ~99.9688% of four-QW total; high QW4 hole peak is consistent with, but does not uniquely explain, such strong integrated radiative localization. Radiative rate depends also on electrons, overlap, material coefficients and spatial integration; one lateral line cannot establish whole-area mechanism.
- NEXT: same Y~1.3um and depth X~0.14–0.29um plot `eDensity`; compare e/h spatial peak localization without touching source/solver. No simulation edits.

## 2026-10-22 — Cutline hDensity peaks clipped
- User SVisual screenshot: n2_end_des hDensity(C2) Cutline_Y at lateral Y~1.3um. Right plot X-axis fixed 0.14–0.29um displays MQW-related peaks, but log hole-density vertical axis max 1e17cm^-3 clips several peaks. QW4-relative hole levels and mechanism remain unresolved.
- NEXT: Set right XY vertical axis min1e10 max1e20cm^-3 (log), keep depth X range; inspect new screenshot. No simulation or source changed.

## 2026-10-22 — n2 hDensity Cutline_Y plot established
- OBSERVED SVisual screenshot: a Cutline_Y Plot showing hDensity(C2(n2_end_des)) at lateral Y~1.3um is present. Graph depth X range 0..4.288um compresses the MQW peaks; left Axis Properties shows Min=0 and Max=4.288 as fixed. No per-QW hDensity values can yet be inferred.
- NEXT: Set depth X axis Min=0.14 Max=0.29um for a QW-resolved hole-density line plot, then examine eDensity on the same cut if needed. TCAD sources/runs unchanged.

## 2026-10-22 — n2_end_des hDensity MQW enlarged image: color map insufficient for QW4 carrier causality
- OBSERVED user SVisual image: n2_end_des hDensity color map, log color legend ~1e-30 to 8.279e19 cm^-3, four fine MQW layer strata resolved at X(depth)~0.17–0.27um. Displayed lateral Y only ~1.0–1.65um, not entire device or damaged sidewall near 2.0um; plot depth X~0–0.45um. Colors mostly orange in MQW with yellow lower n-GaN region.
- QW-specific hDensity magnitudes or QW4 accumulation cannot be inferred from this nearly 50-decade legend. Previous PLT QW4 radiative ~99.97% remains OBSERVED; carrier mechanism UNRESOLVED. Do not repeat zoom, switch to read-only SVisual 1D Cut Y at lateral Y~1.3um (constant Y) for hDensity vs depth X crossing QW1–4, then optionally eDensity same cut. Plot action only, no source or simulations changed.
- Synopsys Sentaurus Visual Training section 5.3 Cutlines: https://ghzphy.github.io/Sentaurus_Training/sv/sv_5.html defines Cut Y as orthogonal cut at selected constant Y.

## 2026-10-22 — n2_end_des hDensity overview SVisual screenshot observed; QW-specific interpretation pending
- User provided Sentaurus Visual T-2022.03 screenshot: dataset `n2_end_des`, scalar `hDensity` selected; logarithmic color legend approximately 1.0e-30 to 8.2788e19 cm^-3. Plot shows full 2um lateral width (Y horizontal) and excessive X vertical span with MQW layers compressed around X~0.17–0.27um.
- OBSERVED: hDensity output exists and is visualized, but this full-depth overview is too coarse to quantify/compare hole densities in each QW or diagnose extreme QW4 Radiative localization. Legend global max is not QW-specific.
- NEXT: SVisual plot axes adjust X(depth)~0.14–0.29um, Y(lateral)0–2um; retain log hDensity, capture enlarged QW1–QW4. Then same ROI eDensity or quantitative cutline as needed. No code/run change.

## 2026-10-22 — pp1_dvs.cmd Half/contact lateral geometry relationships checked (OBSERVED TERMINAL)
- User provided actual preprocessed SDE `pp1_dvs.cmd` grep: line37 `(define Wshelf 0.0)`; line39 `(define Wedge 0.1)`; line53 `(define Xs (/ Wm 2.0))`; line54 `(define Xd (- Xs Wdmg))`; line55 `(define Xe (- Xd Wedge))`; line56 `(define Xend (+ Xs Wshelf))`.
- Earlier same source lines154–158 map 3 anode contacts to top Clean+Edge+Dmg segments covering [0,Xs] (conditional on valid nonzero segments). Previously observed n1_msh.log bbox lateral span 2.0um and mesh succeeded. These are consistent with 4um target Wm→2um Half, but this grep did NOT separately print `Wm` or `Wdmg` numerical literal. Geometrical 2um span already independently observed from actual mesh log, so repeated micro-greps not necessary for current next task.
- In absence of explicit AreaFactor/Cylindrical overrides in pp2/pp6 decks and using documented planar 2D default 1um effective width (Synopsys Training https://ghzphy.github.io/Sentaurus_Training/sd/sd_3.html), nominal Half-model area=2um×1um=2e-8cm². With prior measured n2/n6 terminal currents at 3.6V conditional planar J_off=1.823642625 A/cm² and J_on=0.4609853855 A/cm². This is NOT experimentally validated current density for 4um circular mesa nor proof of comparable Full 3D physics.
- Next prioritize read-only physical plausibility of extreme QW4 radiative localization: inspect `hDensity` and if needed `eDensity` in SVisual `n2_end_des.tdr` over active MQW; no new half run. Preserve baseline and plan protected separate Full/Half reference. No TCAD source edit.

## 2026-10-22 — V2.1 실제 pp1_dvs.cmd anode/cathode contact code examined (OBSERVED)
- User-provided school server `grep -n -A 35 -B 8 'sdegeo:set-contact' pp1_dvs.cmd | head -n 100` shows lines 150-168. Anode is explicitly assigned in 3 top-edge segments midpoint at 0.5Xe, 0.5(Xe+Xd), 0.5(Xd+Xs), with code comment "whole mesa top (Clean + Edge + Dmg top edges of the p+ cap)". Cathode when Cath != 1 uses bottom-edge contact at midpoint 0.5Xs; if Wshelf>0 also outer bottom edge. Prior observed live parameters Cath=0 and Wshelf=0 make this bottom-contact branch the intended active branch.
- Actual numerical extent Xs, edge coordinates and resulting geometry still must be read to independently verify effective 2um anode contact length. Neither this source fragment nor negative AreaFactor grep proves physically calibrated 4um circular mesa current density. AreaFactor 2D default 1um supported by Synopsys Training (https://ghzphy.github.io/Sentaurus_Training/sd/sd_3.html), but resulting J=1.82364 (OFF), 0.46099 (ON) A/cm2 at 3.6V are conditional planar-Half values until area/contact confirmed.
- NEXT: get one read-only short `pp1_dvs.cmd` geometry-definition block giving Xs/Xd/Xe (and parameter definitions) to close width check; then prioritize holistic Half physics and protected Full/Half validation. No deck edit or rerun.

## 2026-10-22 — AreaFactor/Cylindrical/CoordinateSystem 검색 무출력 (USER-REPORTED OBSERVED) 및 잠정 2D J 계산
- 사용자: `grep -niE 'AreaFactor|Cylindrical|CoordinateSystem' pp2_des.cmd pp6_des.cmd pp2_des.par pp6_des.par` 실행 후 검색 결과가 없었다고 보고함. 직전의 `CurrentPlot` 로그 'length unit of micrometer'만 출력된 사실과 별도로, 유효 두께를 명시적으로 바꾼 설정은 검사 대상 전처리 덱에서 확인되지 않음.
- Sentaurus Device 2D 기본 out-of-plane 1um 유효 폭은 공개 Synopsys Sentaurus training 설명과 부합 (https://ghzphy.github.io/Sentaurus_Training/sd/sd_3.html). 단, 최신 T-2022.03 runtime/전체 프로젝트 경로 전부를 독립 검증한 것은 아님.
- Half planar y폭 2um과 1um 유효 두께, 전체 2um 상단 anode 접촉 및 native current가 1um depth 대응이라는 가정하에 A=2×10^-8 cm². 기존 3.6V raw I_n2=3.64728525e-8, I_n6=9.21970771e-9에서 조건부 J_n2=1.823642625 A/cm², J_n6=0.4609853855 A/cm².
- 이 값은 planar-half의 conditional equivalent current density; circular 4um device에서의 calibrated J, AreaFactor 완전 입증, physical IQE 검증이 아님. 다음 최소 단계: 원본 SDE에서 anode 접촉 span 확인, 이후 Half 물리 모델 우선순위 검토 및 별도 Full/Half gate. 시뮬레이션/코드 변경 없음.

## 2026-10-22 — V2.1 n2/n6 AreaFactor grep 결과 (OBSERVED SERVER OUTPUT)
- 학교 서버 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`에서 `grep -niE 'AreaFactor|current unit|length unit|A/cm|A/um' pp2_des.cmd pp2_des.par n2_des.log n6_des.log` 실행. 결과는 `n2_des.log:297: Use length unit of micrometer during currentplot integration.` 및 `n6_des.log:297: ...` 2줄뿐.
- 명시적 `AreaFactor`/terminal current unit 표기는 위 검색 파일에서 발견되지 않음. `CurrentPlot` integration length 단위 µm는 terminal current 단위 검증이 아님.
- 이전 3.6V 원시 전류 값에서 J를 물리적 보정/정규화 완료로 선언하지 않음. 다음: n2/n6 전체 전처리된 cmd/par에서 AreaFactor/Cylindrical/CoordinateSystem 확인, 2D 평면 깊이와 effective 1um default 두께가 실제 적용되는지 공식 T-2022.03 매뉴얼/로그와 대조; 그 후만 조건부 J 계산. TCAD 무변경.

## 2026-10-22 — V2.1 n6 RadiativeRecombination SVisual 화면 관찰 (OBSERVED USER SCREENSHOT)
- 사용자 제공 Sentaurus Visual T-2022.03 화면: plot title `n6_end_des`, field `RadiativeRecombination` (legend `cm^-3 s^-1`), 표시 최고치 약 5.02e24. 표시 범위 x(depth) 대략 0~0.45 um, y(lateral) 대략 1.2~2.0 um.
- MQW 위치에 복수의 수평 방사재결합 띠가 관찰되고, x 약 0.26 um 부근 강한 띠는 기존 n2 QW4-dominant 정량 관찰 및 n6 QW PLT 적분과 정성적으로 양립. 이 이미지 단독으로 QW별 적분값, 전역 profile, Trap의 인과효과, n2/n6 절대 강도 차이 또는 실제 TDR 저장 바이어스는 확정할 수 없음.
- 화면의 auto/color legend 최대치만으로 n2 그림과 강도 비교 금지. 다음 n2/n6 동일 ROI, 동일 scaling/legend로 비교하고 기존 PLT의 정량 차이는 별도로 제시; 이어 2D current/AreaFactor 검증 후 Full/Half 별도 비교. TCAD 파일/solver/run 변경 없음.

## 2026-10-21 — n2 QW Radiative SVisual 이미지 확인 (OBSERVED)
- 사용자가 n2_des 화면에서 RadiativeRecombination 선택한 스크린샷 제공. 측벽 인접 lateral Y~1.2–2.0um, 깊이 X~0–0.45um 범위의 MQW 및 QW4 부근 강한 밴드가 보임. 이전 PLT QW4 방사 재결합 1.523625e23 / 전체 1.52410078e23 = 약 99.9688%와 정성적 일치.
- 화면은 전체 폭이 아닌 측벽 근처 부분만 나타내고, 제목 n2_des만으로 최종 TDR 바이어스는 확인 불가. 물리적 모델 타당성 검증 완료 아님.
- 다음: n6_end_des.tdr에서 동일 Radiative field/시야 확인 후 전류 단위와 Half/Full 비교 단계로 진행. 소자 변경/계산 재실행 없음.

## 2026-10-21 — V2.1 n2/n6 최종 TDR·체크포인트 파일 실제 존재 확인 (OBSERVED FILE LIST)
- Worker 이택규가 학교 서버 `CMP_BASELINE_2.0.0_V2`에서 `find . -maxdepth 1 -name '*end*' -print` 결과를 제공. `n2_end_circuit_des.sav`, `n6_end_circuit_des.sav`, `n2_end_des.sav`, `n6_end_des.sav`, `n2_end_des.tdr`, `n6_end_des.tdr` 여섯 파일 존재.
- 이전 `ls ... 2>/dev/null`에서 나왔던 `cannot access 2`는 터미널 리다이렉션 입력 문제였고 실제 파일 부재 증거가 아님. 파일 목록은 TDR/체크포인트 **존재**만 확인, TDR 내부 최종 바이어스 또는 정상 재시작(Save/Load)을 독립적으로 검증하지는 않음.
- 앞서 n2/n6 PLT 최종 3.600V 및 전류 수지 확인; 현 기존 half run 재실행 불필요. 다음 가장 짧은 확인은 `n2_end_des.tdr` / `n6_end_des.tdr` SVisual에서 MQW 위치/방사재결합 분포와 QW4 집중 현상 검사 후 2D 전류 정규화 메모, 이어 교수 요청 4um Full reference 별도 제작 및 비교 run. 현재 작업은 소스/결과 파일 무수정.

## 2026-10-21 — V2.1 final-output lookup: shell redirection input issue (USER-REPORTED, NO TCAD ERROR)
- Worker: 이택규. Command intended `ls -lh n2_end* n6_end* 2>/dev/null`, terminal emitted `ls: cannot access 2: No such file or directory`; likely malformed handling/pasting of `2>/dev/null` resulting in literal filename `2`. Not evidence that `n2_end` or `n6_end` checkpoint files are absent and not a device/solver failure. File existence still UNRESOLVED.
- `grep -niE 'AreaFactor|current unit|unit.*current|A/um|A/cm' n2_des.log pp2_des.cmd pp2_des.par` produced only `n2_des.log:297: Use length unit of micrometer during currentplot integration.`. Confirms currentplot integration length choice, NOT terminal current density units or an AreaFactor setting.
- Immediate next read-only command without shell redirection: `find . -maxdepth 1 -name '*end*' -print`. Continue broad physical and full-vs-half workflow once results confirmed; no TCAD files or runs modified.

## 2026-10-21 — V2.1 3.6V n2 Trap OFF residual cross-check 완료 (OBSERVED)
- 이택규 실제 학교 서버 `n2_des.plt` 3.6V 마지막 행 `IntegrTrap_all eGapStatesRecombination` = 1178830.32026416 (PLT raw). 앞서 n6 같은 항목 = 1.98258247754075e22. ON/OFF integral ratio = 1.68182e16. OFF raw 값은 정확히 0은 아니지만 ON에 비해 사실상 무시할 수 있음.
- 이전 관찰 수치 n2 Ianode = 3.64728525e-08, n6 Ianode = 9.21970771e-09 (PLT native unit). `q*1e-12` 환산 **가정 하에** n2 Trap equivalent current =1.88869439458e-25, fraction I=5.17836e-18; n6 Trap equivalent current =3.17644732049e-09, fraction I=34.4527985%. n6 전체-device Rad+SRH+Aug+Trap equivalent 9.21961925167e-09 vs measured I=9.21970771e-09 (99.99904% balance closure).
- Verdict: 코드 split SideTrap OFF0/ON1e18이 QW/Trap 재결합 결과에도 일관되게 반영됐음을 정량적으로 지지. 소자 물리 정확도, 전류밀도 AreaFactor, 효율, 74.72% 전류감소의 단일 원인은 입증하지 않음. 필요 이상의 단일 문제 추적 대신 전류 정규화/결과 적절성 검증으로 이동. 기존 시뮬레이션 수정 및 재실행 없음. 교수 피드백 Full/Half 검증은 Half 검토 후.

## 2026-10-21 — V2.1 n6 3.6V Trap 적분으로 QW 미설명 전류 수지 해소 (OBSERVED; PHYSICAL CAUSATION NOT PROVEN)
- 이택규 실제 서버 `n6_des.plt` 마지막 PLT 데이터 행(3.6V)의 `IntegrTrap_all eGapStatesRecombination`=1.98258247754075e22, `IntegrSRH_all srhRecombination`=4.32337288643595e21, `IntegrRad_all RadiativeRecombination`=2.55552035945039e22, `IntegrAug_all AugerRecombination`=7.83993596604716e21 raw DF-ISE CurrentPlot integral output.
- Previous same final row `anode TotalCurrent=9.21970771e-09` (raw 2D terminal-current units). From prior observed PLT×1e−12/SVisual matching and `q=1.602176634e−19 C`, derive whole-domain standard recombination equivalent `q*(Rad+SRH+Aug)*1e−12=6.04317193118e−09` (65.54624% I); trap electron gap-state equivalent `q*IntegrTrap_all*1e−12=3.17644732049e−09` (34.45280% I). Sum `9.21961925167e−09` = 99.9990406% of terminal current; residual `8.84583e−14` (0.000959%).
- This quantitatively resolves the earlier ~34.48% QW 3-channel-only gap via explicit measured trap channel (plus tiny outside-QW Rad/SRH/Auger), subject to current/unit normalization convention; **not** proof of single physical mechanism of current suppression or experimentally validated IQE. Global Rad / (global Rad+SRH+Aug+Trap) ≈44.4096% is a computed conditional recombination-channel ratio, not a calibrated absolute device IQE; n6 QW-only 3channel Rad fraction≈67.77% excludes trap channel.
- NEXT fast read-only: confirm n2 `IntegrTrap_all` near zero; n2 whole-domain channels; check PLT current units/AreaFactor. Then finish Half audit and professor Full-vs-Half validation. Existing SDE/SDevice/run unchanged.

## 2026-10-21 — V2.1 n6 3.6V 전체 재결합/Trap 전류 수지 99.9990% 확인 (USER-OBSERVED PLT; UNIT CONSISTENCY INFERRED)
- 작업자 이택규가 학교 서버 n6_des.plt 마지막 행에서 직접 추출해 제공: bias=3.6V; IntegrTrap_all eGapStatesRecombination = 1.98258247754075e22, IntegrSRH_all srhRecombination = 4.32337288643595e21, IntegrRad_all RadiativeRecombination = 2.55552035945039e22, IntegrAug_all AugerRecombination = 7.83993596604716e21 (raw PLT integral data).
- 이전 같은 행 Ianode=9.21970771e-09, Icathode=-9.21970771e-09, displacement=0. Earlier n6 four-QW 3-channel sum raw Rad=2.55545394e22 SRH=4.31092452e21 Aug=7.83986116e21.
- DERIVED using q=1.602176634e-19 C and PLT raw recombination x 1e-12 numerical SVisual 2D conversion (unit conventions still need formal confirmation): Trap equivalent current=3.17644732e-09, =34.4528% of terminal current; total-device Rad=44.4092%, SRH=7.5130%, Auger=13.6240%. Four-channel all-device sum equivalent=9.21961925e-09, =**99.99904%** terminal current, residual 8.85e-14 =0.000959%. QW-only 3-channel =65.5233% terminal current, Trap=34.4528%, other-than-QW normal channels ~0.02292%; residual ~0.00096%.
- INTERPRETATION: numerical charge/recombination balance closes very tightly in n6 at final steady-state-like 3.6V and eGapStates recombination is substantial, consistent with active SideTrap in Dmg regions (EdgeTrap Conc0); not proven that this alone causes reduced terminal current, not matched-current IQE, not device physical calibration, not independent unit/AreaFactor confirmation. No need to pursue tiny mesh-angle without new evidence. `IntegrTrap_all` area attribution to sidewall can be checked with regionwise integrated values if needed.
- NEXT: read n2 all-device trap/channel totals for control/balance, check current units/AreaFactor and QW4-dominant spatial recombination physical plausibility as part of broader Half validation; then prepare professor-requested 4um Full vs 2um Half run on protected separate project. Existing TCAD code/runs untouched.

## 2026-10-21 — V2.1 3.6 V 실제 PLT 전류/QW 재결합 동시 추출 (OBSERVED, PHYSICAL INTERPRETATION LIMITED)
- 이택규가 기존 시뮬레이션 PLT의 값을 파싱한 실제 학교 서버 출력을 제공. Python EOF 처리 중 마지막 `NameError: name 'PY' is not defined`는 숫자 **전부 출력 이후** 발생한 추가 입력 처리 오류이며, 앞서 인쇄된 계산값에 영향 없고 파일 변경 없음.
- n2 OFF: DF-ISE datasets=100, 123 points, selected final #122 3.600000V. anode total 3.64728525e-08, cathode -3.64728525e-08, displacement0. QW1–4 Clean/Edge/Dmg sum: Rad 1.52410078e23, SRH 1.25388758e22, Auger 6.26565608e22 raw PLT integral units. Three-channel shares: Rad 66.9624%, SRH 5.5090%, Auger 27.5286%.
- n6 ON: datasets=100, 124 points, selected final #123 3.600000V. anode total 9.21970771e-09, cathode -9.21970771e-09, displacement0. QW sums: Rad 2.55545394e22, SRH 4.31092452e21, Auger 7.83986116e21 raw; shares Rad 67.7744%, SRH 11.4332%, Auger 20.7925%.
- Equal-bias I_n6/I_n2 = 0.2527827 (−74.72%), QW Rad_n6/Rad_n2=0.1676696; three-channel Rad proportion INCREASES ~0.812 percentage points for n6; *not proof of device IQE improvement*. Terminal anode/cathode currents exactly balance at printed precision; displacement=0.
- Numerical SVisual cross-check: Prior 주수빈 n2 SVisual 12 QW integrals Rad~1.524099e11/s/um, SRH~1.253894e10/s/um, Auger~6.265625e10/s/um; PLT raw QW totals ×1e-12 numerically align. Multiplying 2D assumed converted rates by electron charge q gives (q×QW3channel/I) n2~0.9998237 and n6~0.6552333. n6 ~34.48% gap may reflect trap outside QW/other device recombination/leakage/normalization; **not yet proven mechanism**. Verify AreaFactor and unit conventions before interpreting physically.
- NEXT READ ONLY: extract n6 `IntegrTrap_all eGapStatesRecombination`, `IntegrSRH_all srhRecombination`, `IntegrRad_all RadiativeRecombination`, `IntegrAug_all AugerRecombination` from last PLT row; compare with missing q equivalent and n2. Later check QW4-dominant distribution and full J–V. Keep old Half, professor Full/Half after Half validation. No code modifications/run.

## 2026-10-21 — V2.1 DF-ISE PLT numerical values exist and multiline wrapping confirmed (OBSERVED)
- Worker: 이택규. Actual school-server output `sed -n '45,58p' n2_des.plt` shows end of `functions` block, `Data {` at line 52, followed by full-precision scientific-notation numerical samples beginning from zero. `tail -n 5 n2_des.plt | cut -c1-180` shows numeric data continues to closing `}` without separate row labels; values wrap across lines. Both n2/n6 Data start at line52 (confirmed earlier).
- **Interpretation:** `tail` numerical lines must not be treated as individual rows; need count of quoted names in `datasets=[...]` then group all data tokens accordingly. Header shows QW1..4 Clean/Edge/Dmg integrated Radiative/SRH/Auger. Actual final 3.6V current/region totals and units still unextracted/unverified.
- NEXT READ ONLY: use local `python3` heredoc to parse quoted dataset labels, all floats within Data block, check complete row divisibility, select latest row nearest 3.6V, print electron/hole/displacement/total currents and all 12 QW region-integral sums for n2/n6; no modification to Sentaurus project. Do not label three-channel fraction calibrated device IQE or assume J normalization.

## 2026-10-21 — V2.1 n2/n6 DF-ISE PLT numeric data section 위치 확인 (OBSERVED METADATA)
- 사용자 실 서버 출력 `sed -n '28,45p' n2_des.plt`: functions 배열에 Time/OuterVoltage/InnerVoltage/QuasiFermiPotential/DisplacementCurrent/eCurrent/hCurrent/TotalCurrent/Charge 그리고 RadiativeRecombination, srhRecombination, AugerRecombination, eGapStatesRecombination 항목 존재 (values 아직 미확인).
- `grep -nE '^(Data|Values|Info|[[:space:]]*functions|[[:space:]]*units)' n2_des.plt n6_des.plt`: 양쪽 `Info {` line3, `functions = [` line28, `Data {` line52. numeric values/units/block layout 아직 미확인.
- `sed -n '1,28p' pp2_des.cmd`의 Fermi, NoBandGapNarrowing, HighFieldSaturation, SRH/Radiative/Auger, Mg/PDopant incomplete ionization, polarization activation0.5 and interface Thermionic settings 재확인. New runs/code changes none.
- NEXT: `sed -n '45,58p' n2_des.plt` plus abbreviated tail to inspect actual DF-ISE Data representation before constructing read-only n2/n6 extraction of 3.6V currents and QW integrated radiative/SRH/Auger, including units and final-bias verification. Avoid claiming IQE/absolute J from metadata alone.

## 2026-10-21 — V2.1 terminal current and MQW integral datasets verified in n2_des.plt header (OBSERVED METADATA)
- User actual server `head -n 28 n2_des.plt` shows DF-ISE text xyplot `datasets` with anode/cathode OuterVoltage, InnerVoltage, QuasiFermiPotential, DisplacementCurrent, eCurrent, hCurrent, TotalCurrent, Charge, plus region-wise current plot integral datasets for RadiativeRecombination, srhRecombination, AugerRecombination over Clean/Edge/Dmg QW1..4, EBL etc, and Trap gap-state eGapStatesRecombination for 13 Dmg/Edge regions.
- `sed -n '1,28p' pp2_des.cmd` confirms Grid=n1_msh.tdr; File Parameter=pp2_des.par, Current=n2_des.plt, Plot=n2_des.tdr, Output=n2_des.log; Electrode anode/cathode initial 0.0V; Physics Fermi, DefaultParametersFromFile, EffectiveIntrinsicDensity(NoBandGapNarrowing), Mobility(HighFieldSaturation), Recombination(SRH Radiative Auger), IncompleteIonization Mg/PDopant, Piezoelectric_Polarization strain activation 0.5; interface Thermionic for InGaN/GaN, AlGaN/GaN, AlGaN/InGaN.
- n6 runtime thermionic electron/hole Formula1 again observed; pp2_des.par vs pp6_des.par no diff again observed.
- IMPORTANT: dataset existence ≠ populated numeric series, correct final bias, units or validated IQE. But it may eliminate manual SVisual summation if current-plot integrals are populated. Need inspect DF-ISE `functions`/`Data`/units and then programmatically extract last-bias terminal currents and QW 3-channel integrated signals from n2 and n6 with correct sign/unit handling.
- NEXT READ ONLY: `sed -n '28,48p' n2_des.plt`; `grep -nE '^(Data|Values|Info|[[:space:]]*functions|[[:space:]]*units)' n2_des.plt n6_des.plt | head -n 30` to determine parsing layout/units. Then compare n2/n6 3.6V J-V, QW rad/srh/auger; AreaFactor validation pending. Do not change source/run. After Half verified, independently run professor-requested Full comparator.

## 2026-10-21 — V2.1 NtSide OFF/ON 물성 파라미터 동일성 확인 (OBSERVED SERVER DIFF)
- 이택규가 학교 서버 `CMP_BASELINE_2.0.0_V2`에서 `diff -u pp2_des.par pp6_des.par | head -n 80` 실행 후 출력 없이 정상 프롬프트 복귀한 내용을 제공. 따라서 두 preprocessed parameter 파일에서 표시되는 차이가 없음(동일 내용으로 판정; 직접 해시 미확인).
- 이전 전체 76행 `diff -u pp2_des.cmd pp6_des.cmd`에서 `SideTrap Conc=0` (n2) vs `1e18` (n6)의 13개 Dmg 영역 외에는 노드별 Parameter/Current/Plot/Output 및 Save/Plot prefix만 달랐고, 양쪽 Grid `n1_msh.tdr`, global Physics, thermionic runtime model Formula1, Math/Solve/3.6V 목표는 일치.
- 판정 범위: **OFF/ON의 명령+물성 입력 조건 일관성 확인** (Intentional one-factor `SideTrap Conc` split). 런타임 물리 보정/전류 밀도 단위, TDR 최종 bias, 3.6V/QW IQE의 물리 타당성, matched-current trap 효과는 별도의 미해결 검증 항목.
- NEXT: 원본 변경 없이 `n2_des.plt`/`n6_des.plt` 전류 dataset/단위 및 AreaFactor 확인 → J–V 일관성, final saved TDR bias → n6 QW 3채널 적분. 교수 요청 Full/Half는 Half 검증 마친 뒤.

## 2026-10-21 — V2.1 n2/n6 preprocessed SDevice full diff + runtime Thermionic 비교 (OBSERVED)
- 학교 서버 diff -u pp2_des.cmd pp6_des.cmd 전체 76행 제공. 실질적인 명령 파일 차이는 13개 Dmg regions의 SideTrap Conc=0 (n2) versus 1e18 (n6)와 n2/n6 입출력 파일명/저장 prefix. 두 노드 Grid=n1_msh.tdr 동일, global physics, electrode, solver, bias sweep 동일. pp2_des.par / pp6_des.par 실제 내용은 아직 미대조.
- n6_des.log 662/671/680행에서 With Thermionic Emission at heterointerfaces for electrons and holes, 1784/1790/1796에서 ThermionicEmission: Formula = 1, instead of: 0 [1] 확인. n2도 동일 로그 출력 확인됨. Model enabled is confirmed in both logs, physical accuracy not proven.
- AreaFactor and 2D current normalization unresolved. n2/n6 equal-voltage current difference does not prove matched-current trap efficiency.
- NEXT READ ONLY: diff -u pp2_des.par pp6_des.par | head -n 80; current scaling, final TDR bias, then n6 QW recombination. No code/run edits.

## 2026-10-21 — V2.1 실제 n2 SDevice Thermionic 적용 확인, n2/n6 diff 길이만 확보 (OBSERVED)
- 이택규 실제 서버 출력: `diff -u pp2_des.cmd pp6_des.cmd | wc -l` = 76. 76은 unified diff 전체 줄수(헤더/문맥 포함)이며 설정 변경 76개를 뜻하지 않음. 실제 hunk 내용은 사용자가 아직 제공하지 않았으므로 ON/OFF 차이가 trap만인지 UNRESOLVED.
- `grep -niE 'Thermionic|AreaFactor' n2_des.log | head -n 25`: 662/671/680행 `With Thermionic Emission at heterointerfaces for electrons and holes`, 1784/1790/1796행 `ThermionicEmission: Formula = 1, instead of: 0 [1]`. 따라서 n2 runtime이 thermionic emission with Formula1을 인식한 것은 OBSERVED. n6 동일 실행 문맥은 아직 미확인.
- 출력에서 AreaFactor 검색 매치가 없었으나 이는 기본값/유효 단위/2D normalization의 입증도, 설정 오류의 증거도 아님. 후속 확인 필요.
- NEXT READ ONLY: `diff -u pp2_des.cmd pp6_des.cmd | head -n 110` 실제 차이 확인, `grep -niE 'Thermionic|AreaFactor' n6_des.log | head -n 25` 후 결과 기준 필요한 전류단위/AreaFactor/물리 설정만 추가 검증. 원본 SDevice/SDE 및 run 변경 없음.

## 2026-10-21 — V2.1 n2/n6 전처리 SDevice 물리 설정 직접 대조 (OBSERVED PASTED PP, RUNTIME UNVERIFIED)
- 사용자 서버 실행 `grep -nEi 'AreaFactor|Piezoelectric_Polarization|IncompleteIonization|ThermionicEmission|Recombination|Traps|Conc[[:space:]]*=' pp2_des.cmd pp6_des.cmd | head -n 100` 결과 제공.
- `pp2_des.cmd` n2와 `pp6_des.cmd` n6 모두 L19 `Recombination(SRH Radiative Auger)`, L20 `IncompleteIonization(Dopants="pMagnesiumActiveConcentration PDopantActiveConcentration")`, L21 `Piezoelectric_Polarization(strain activation=0.5)` 존재. L62-63에 SRH/Radiative/Auger/Total 및 e/hGapStatesRecombination plot 명령 관련 항목 존재.
- n2 Dmg_pCap, Dmg_pGaN, Dmg_EBL, Dmg_B0, Dmg_QW1..4, Dmg_B1..4, Dmg_nMesa (총 13 Dmg regions) `SideTrap` Acceptor, `fromValBand EnergyMid=0.75`, `Conc=0`, `eXsection=hXsection=1e-15`. n6 대응 13개 Dmg regions에는 `Conc=1e18`; 다른 표시된 Trap 파라미터는 동일.
- n2/n6 각각 Edge 13개 `EdgeTrap` `fromValBand EnergyMid=0.9` `Conc=0`, `eXsection=hXsection=1e-15`. Thus **shown effective settings** form NtSide OFF vs ON split, but full-deck `diff -u` pending to rule out other differences.
- `AreaFactor` 및 `ThermionicEmission` string은 이 user-shared grep 결과에서 등장하지 않음; effective absence/default/runtime interpretation and 2D current normalization are **UNRESOLVED**. No basis yet to call model disabled/incorrect. `activation=0.5` is an active command value, NOT measured polarization sheet charge.
- Next read-only: `diff -u pp2_des.cmd pp6_des.cmd` to isolate all changes, check beginning of Physics/File/Math and SDevice runtime model summary, AreaFactor normalization; later J-V, qR/I limitations, sidewall ON/OFF at matched current. No Sentaurus code/run changes.

## 2026-10-21 — V2.1 mesh-log warning 검색 완료, 과도한 단일 쟁점 추적 지양 (OBSERVED / RESEARCH PRIORITY)
- 사용자 실제 명령: `grep -niE 'warning|error|bad|small|quality|angle|edgeLength' n1_msh.log | tail -n 40`. 출력은 `tri-grid quality`, `minAngle: 0.0167024`, `min edgeLength: 1.95312e-05 [near (0.0041875 1.89501)]`, `Smallest region: Dmg_QW3 Total volume: 1.5e-05` 4줄뿐임. 검색 패턴에 걸리는 별도 warning/error 문구 없음. 이는 모든 mesh 문제 부재 증명도 아니고 수치 정확도 통과도 아님.
- 사용자의 명시적 검증 원칙: 한 가지 mesh 이상치에 과도하게 매달리지 말고 중요 항목 전체를 빠르고 정확하게 균형 있게 검증. Minimal angle/edge는 **미해결 관찰사항**으로 남기되 계산 영향 증거가 생기기 전에는 장시간 원인 규명을 우선하지 않음.
- NEXT: 실제 전처리 SDevice의 physics, trap, polarization, contacts/AreaFactor 검증과 기존 I-V, 공간 field, carrier/recombination을 우선 점검. Full/Half 비교는 앞선 요청대로 Half 검증 후 진행. 코딩/시뮬레이션 변경 없음.

## 2026-10-21 — 이택규 V2.1 Half 소자 구조/생성 mesh log 검증 진전 (OBSERVED, QUALITY WARNING)
- 사용자 서버 `sde_dvs.cmd` 55–170행과 `n1_msh.log` 마지막 35행 직접 제공. 활성 `pp1_dvs.cmd` 변수는 Wshelf=0, Wedge=0.1um, Bspan=0, Cath=0. 2um half 측방 폭(0..2um), 총 depth 4.288um, QW 4개(각 0.003um), 5nm damaged sidewall 확인. 구체적 epitaxy: pCap 0.020, pGaN 0.120, EBL 0.026, B0..B4 각 0.022, QW1..QW4 각 0.003, nMesa 0.5, bulk nGaN 3.5um; depth 합 4.288um. top anode Clean/Edge/Dmg pCap, bottom cathode under nGaN. Code-level topology/contacts only, mesh placement visualization not yet independently inspected.
- `n1_msh.log` OBSERVED: 62529 points, 123917 elements, log 42 regions, nMats=40, minAngle=0.0167024deg, maxAngle=128.367deg, min edgeLength=1.95312e-05um =0.0195312nm [near (xdepth=0.0041875um, ylateral=1.89501um)], total 2D area=8.576um², bbox xdepth 0..4.288um, ylateral 0..2um; generated n1_msh.tdr saved/done and generation time 4.84s.
- Derived `Xd=2.0-0.005=1.995um`, `Xe=1.995-0.1=1.895um`; extreme shortest edge near Clean/Edge transition at pCap depth 4.1875nm. `4.288um*2um=8.576um²` exactly matches log. Layer split count expected 13 layers*3+bulk=40 physical material regions, whereas log reports 42 regions and nMats=40; difference may be mesh metadata convention and needs investigation, not assert geometry error.
- **UNRESOLVED:** extreme 0.0167deg minimum angle / 0.0195nm tiny edge suggests possible sliver/near-degenerate triangles; mesh successfully built and n2/n6 previous calculations finished, so not proof of solver error. Investigate min edge location in SVisual actual mesh and log warnings before claiming accuracy. No Full simulation yet. User explicitly chose to complete current verification **before** preparing/running Full vs Half comparison. No TCAD sources/runs changed.
- NEXT READ ONLY: inspect actual `n1_msh.tdr` SVisual mesh near depth 0.0042um and lateral 1.895um; inspect `n1_msh.log` warnings/quality; check exact contact and interface visualization. Only then decide about controlled mesh refinement and separate full 4um comparison.

## 2026-10-21 — 교수 피드백에 따른 V2.1 Full/Half 대칭 검증 필요 및 활성 SDE 파라미터 확인 (USER-REPORTED REQUIREMENT + OBSERVED SERVER OUTPUT)
- 교수 피드백(사용자 전달): half-domain 결과를 연구/발표에 활용하려면 원래 4um full geometry와 2um half geometry 결과의 정량 일치 근거가 있어야 설득력이 있음. 이는 교수 피드백으로 기록하며 Full/Half 동등성은 현재 **미검증**.
- 실제 서버 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2/pp1_dvs.cmd` grep: `Wshelf=0.0`, `Wedge=0.1` um, `Bspan=0`, `Cath=0`. `n1_msh.tdr` 파일 존재, 크기 약 2.0MB, mtime 2026-10-14 13:43 KST. 이는 mesh가 생성된 증거이지 mesh 요소 품질/수렴성 검증 아님.
- 현재 `CMP_BASELINE_2.0.0_V2`와 `_Copy`는 앞선 기록상 모두 half-domain 계보이며 Copy를 Full reference라고 혼동하지 않는다.
- **PLAN/PROPOSED, NOT RUN:** 실제 half SDE 영역/접촉/좌우대칭 조건 검토 → 기존 V2.1 half 결과 보존 → 독립 Full 4um symmetric geometry (양쪽 동일 측벽, contact/physics/Mg/trap/polarization/Wedge/Bspan/mesh nominal spacing 유지) 생성 및 preprocess/mesh gate → NtSide OFF를 먼저 동일 전압/solver 조건으로 run → 전류 정규화, J-V, QW 지역 적분 비율, 대칭 field, 이후 Trap ON matched-condition 비교 → mesh convergence 별도.
- 비교 가정: 동일 2D out-of-plane 및 AreaFactor 정의일 때만 `I_full≈2 I_half`; J와 3-channel QW 방사 비율은 일치 기대. 근접 오차 허용값은 수치 mesh 정확도와 연구 목적 근거로 사전 정해야 하며 임의 성공 판정 금지.
- NEXT READ-ONLY: `sed -n '55,170p' sde_dvs.cmd`, `tail -n 35 n1_msh.log`; mirror boundary/contacts/region mapping, 실제 mesh 및 symmetry를 확인한 뒤 별도 Full 구조 제작. 기존 SDE/SDevice/run 수정 없음.

## 2026-10-21 — 이택규 V2.1 활성 SDE Mesh 설정 원문 확인 (OBSERVED SERVER SOURCE, GENERATED MESH NOT YET VERIFIED)
- 작업자 이택규가 서버 `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`에서 `sed -n '25,55p;170,270p' sde_dvs.cmd` 실제 출력을 제공. SDE coordinate helper `P(lat,dep)=(x=dep,y=lat)`, `RS(mxl,mxd,mnl,mnd)=(maxDepth,maxLateral,minDepth,minLateral)` 확인.
- `Wm=4.0 um`, half `Xs=2.0 um`, `Wdmg=0.005 um`, `Wshelf=0`, `Cath=0`; `Wedge=@Wedge@`와 `Bspan=@Bspan@`의 실제 SWB 값은 pp1 전처리에서 추가 확인 필요.
- Mesh **설정값(생성된 실제 요소값 아님)**: R_all lateral/depth max 0.25/0.25 um; R_top depth max 0.005 um; R_ntop depth max 0.01 um; R_act depth max 0.0015 um; R_qw1..4 depth max 0.0003 um (0.3nm); R_if1 depth max 0.0002 um; R_if2 depth max 0.0006 um; R_x4 damaged 5nm band lateral max 0.0005 um (0.5nm), min 0.0002 um; R_xe lateral max 0.0008 um. SDE comments report QW 3nm; 3nm/0.3nm≈10, 5nm/0.5nm≈10 are **nominal estimates**, not observed actual cell count.
- OBSERVED: `R_sh` refinement window/placement remains in source even though `Wshelf=0`; cannot yet infer it is erroneous or that removal will save runtime.
- Mesh adequacy/convergence, element quality, exact geometry, contact placement, active SWB macro values, mesh element statistics and n1_msh.tdr visual inspection all **UNRESOLVED**. No deck edits/run/restarts.
- NEXT READ-ONLY: `tail -n 35 n1_msh.log`; `grep -nE 'define Wedge|define Bspan|define Wshelf' pp1_dvs.cmd` or inspect pp1 macros and SVisual `n1_msh.tdr` QW/sidewall region mesh; do not promote mesh to verified convergence without a controlled refinement comparison.

## 2026-10-15 — 이택규 V2.1 현재 SDE 실제 소스 RS mesh wrapper 확인 (OBSERVED SERVER SOURCE FRAGMENT)
- 사용자 학교 서버 실제 터미널: `cd /user/semi/semi437/CMP_BASELINE_2.0.0_V2`; `grep -n -A 8 -B 2 -E 'define-refinement-size|define-refinement-function|BulkFac|MaxLenInt' sde_dvs.cmd`.
- Source L31–33: `(define (P lat dep z) (position dep lat z))`; `(define (RS name mxl mxd mnl mnd) (sdedr:define-refinement-size name mxd mxl mnd mnl))`. RS는 순서상 lateral/depth 인수를 SDE x=depth/y=lateral로 바꾸는 wrapper. L37: `(define Wshelf 0.0)` 및 V2.1 shelf removed 주석 직접 확인.
- **근거의 한계:** 위 grep은 직접 `sdedr:define-refinement-size` 호출인 wrapper 정의만 출력하므로 실제 `(RS ...)` 호출의 Global/MQW/EBL/sidewall 최대·최소 mesh 숫자는 미확인. 과거 FAST_C1 Global 0.05/0.10 um 및 BulkFac1.5를 현 V2.1에 적용했다고 주장하지 않는다. 개별 size 및 V2.1 mesh elements/points는 현재 미확인.
- 다음 READ ONLY: 현 경로에서 `grep -n -E '\\(RS[[:space:]]' sde_dvs.cmd` 실행해 실제 영역별 수치를 채집; 각 RS 인수 maxLat/maxDep/minLat/minDep를 올바르게 변환한 후 기존 FAST_C1과 비교. SDE 코드/시뮬레이션 무수정.

## 2026-10-15 — 이택규/Claude Baseline V2.1 shelf 제거 3.6V 도달 보고 (USER-REPORTED RUN; GPT 미검증)
- Claude의 학교 서버 실행 보고: `CMP_BASELINE_2.0.0_V2`에 V2.1 `Wshelf=0`, shelf region 및 바닥 cathode 제거, SDE 재실행, PolAct=0.5, 기본 solver(Iterations20, NotDamped50, PARDISO 없음). n2(NtSide=0)와 n6(NtSide=1e18)가 모두 **3.600V** 목표 도달. `I_total`은 n2=3.647e-08, n6=9.220e-09 A/µm; half mesa 2µm 기준 조건부 J=1.8235, 0.4610 A/cm². `didn't converge` 출력 각각 0회/1회.
- shelf 유지 `CMP_BASELINE_2.0.0_V2_Copy` + PolAct=0 대조군은 n2 2.069V, n6 2.036V에 정체. 분극 비활성화만으로 정체 미해결. shelf 제거와 cathode 경계조건이 함께 변해 모서리 단독 원인은 확정할 수 없음.
- n6 전류/n2 전류=25.3% (같은 3.6V); 음전하 공핍 가설은 **UNRESOLVED**. n2 마지막 두 점 국소 n≈2.27은 유도값. 사용자는 **V2.1을 검증용 기준 구조로 채택**했다고 보고; 물리적 Baseline freeze는 아님.
- **원본 서버 로그/코드 독립 열람하지 않음**. 상세 수치·대조 해석: [#02 보존 기록](../../members/LeeTaekGyu/LOG_20261015_02_baseline_v2_1_shelf_removal.md).
- 다음: 활성 pp/log/.plt, J 정규화/접촉 확인 → `bl2_check.py` 재결합 적분 및 정의 점검 → 문헌 I-V 대조 → S3 PolAct1.0 → A/B pilot. 코드/학교 서버 run 수정 없음.

## 2026-10-13 — 이택규 Claude V2 독립 수치·물리 검토 (GPT ANALYSIS / USER-REPORTED RUN3)
- 사용자 전달 Claude 설명: run1 2.31V 도달 후 QS Newton 진동, run2 2.070V 조기 종료, **run3는 Claude가 수정한 복사본**에서 `Method=Blocked, SubMethod=ParDiSo, NumberOfThreads=4, Iterations=20, NotDamped=50, ExtendedPrecision` 설정으로 실행 중이라고 보고됨. **새 복사본의 원본 pp*/log 및 성공/개선은 직접 검증되지 않음**.
- 독립 검토(해석, 결과 아님): QS MaxStep는 V가 아닌 정규화된 t에 작용하므로 stage 2.0→3.6V의 MaxStep 0.01은 최대 0.016V, 0.02는 0.032V, MinStep 1e-6은 1.6 microV. 2.3V 수렴은 스텝 크기/수치 stiff 문제 가능성 높으나 물리 원인 미확정. `NotDamped=50>Iterations=20`은 기본적으로 Bank–Rose damping을 지연시키지만 Sentaurus 교육자료는 QS에서 작은 스텝을 일반적으로 우선하므로 '오류'로 단정 금지.
- Sentaurus 교육자료 `sd_6`에 따라 CNormPrint/NewtonPlot 좌표로 실패 방정식/영역을 확인. 사용자 서버 n2 파일 목록에는 `n2_des_min_des.tdr` 존재하므로 near-MinStep 자동 진단과 관계 있을 가능성(확정 전 로그 확인). 저밀도 `HighFieldSaturation` driving-force smoothing은 **실제 electron/hole 저밀도 수치 불안정이 확인되는 경우만** 제안.
- `Method=Blocked, SubMethod=ParDiSo`는 mixed-mode에 적합; standalone device면 `Method=ParDiSo`가 교육자료 예시. `ExtendedPrecision`은 III-N에서 권장되지만 PARDISO 4-thread와 조합 시 병렬 성능이 저하될 수 있음. `Iterations=20` 일반적으로 합리적. T-2022.03 UG p221/1070 사용자 인용은 원문 직접 미대조.
- 2.31V J≈1.3e-6 A/cm2 및 국소 이상계수≈1.6이 3.6V에서 J>1A/cm2 증거는 아님: 300K/고정 n=1.6 가정의 **순수 수학적** 외삽에서 J=1A/cm2는 V≈2.871V이며 높은 주입/직렬저항/수송 변화로 물리적 예측 불가. 2D J/AreaFactor 실제 설정 확인 필요.
- A/B 보류사항: 50% polarization/70:30 offset calibration 없음; p+Mg/EBL PDopant 실제 활성 정공 및 thermionic interface 확인; sidewall uniform 5nm Nt1e18 cm-3→조건부 5e11cm-2 등가 면밀도, C implant의 실측 프로파일 아님; Project B edge-QW AlGaN replacement는 QW 부피/밴드·계면을 동시에 바꾸며 conformal barrier와 다름; equal-current QW IQE/transport, symmetry/full-vs-half/mesh convergence 검증 필요.
- 근거: 사용자 메시지+앞서 제공된 n2/n6 실제 파일 목록/로그, GitHub 기존 V2 감사 및 Synopsys 교육자료 웹 미러 sd_6/sd_8/sd_9/sd_16, 학술 microLED 문헌. **코드 수정 또는 run 재시작 없음.**
- 다음: 복사본 실제 전처리 Solve/Math, 최근 마지막 accepted voltage/current 및 CNormPrint/MinStep 메시지 확인. 실행 중인 원본 n6 및 복사본 무단 종료 금지.

## 2026-10-13 — 이택규 V2 n2 조기 종료 사용자 확인 (USER-REPORTED / UNRESOLVED CAUSE)
- 사용자가 Claude Baseline V2 n2 계산이 3.6V 목표 전에 조기 종료됐다고 확인함. 이전 직접 제공 로그에서 n2는 'simulation finished' 및 SWB done이었지만, 마지막 표시된 anode 2.070V, raw conduction 1.781e-16이고 pp2_des.cmd Goal은 2.0V와 3.6V. 조기 종료 원인은 미확인. 성공 종료 메시지로 최종 바이어스 충족을 주장하지 말 것.
- 재실행/원본 변경 없이 pp2_des.cmd 175–215행, n2_des.log 종료 조건/수렴 경고 및 마지막 65행을 확보해 원인을 식별. n6는 실행 중이므로 건드리지 않음.

## 2026-10-13 — 이택규 Claude V2 n2 최종 출력 anode 2.070V / 1.781e-16, 목표 3.6V와 불일치 (OBSERVED / UNRESOLVED)
- 근거: 사용자 실제 서버 `grep -E '^[[:space:]]*anode[[:space:]]' n2_des.log | tail -n 8` 및 `grep -nE 'Goal|Voltage|Vmax' pp2_des.cmd`. n2 마지막 표시 단자 anode voltage 2.070E+00 V, electron 6.437E-45, hole 1.781E-16, conduction current 1.781E-16 (**raw solver 값; 2D 정규화 미검증**). 로그는 n2 SDevice Simulation finished/Good Bye 및 SWB done이므로 프로그램 정상 종료는 확인됐으나, 최종 물리 bias가 3.6V 도달했다는 증거는 아님.
- 실제 전처리 `pp2_des.cmd`에는 `Goal { Name="anode" Voltage=2.0 }` (L188), `Goal { Name="anode" Voltage=3.6 }` (L194) 둘 다 존재. 최종 *출력된* 전압은 목표 3.6V의 57.5%; 어떤 이유로 2.070V 이후 목표로 진행하지 않았는지는 **UNRESOLVED**. BreakCriteria/최종 PLT voltage/solve blocks 등 미확인. `2.070V`의 1.781e-16을 기존 4–5V 데이터와 비교하여 전류 문제를 악화/개선됐다고 단정하지 말 것.
- Node6 서버 `ps -p 93107`: PID 93107 `gjob` wrapper (S-state, CPU 0.0%, elapsed 01:27:43), **실제 sdevice 자식 PID 생존 여부를 뜻하지 않음**. `n6_des.log` mtime `2026-10-13 20:18:51.645 +0900`, 259,459 bytes. SWB 상태는 running; 현 진행/정체 여부는 실제 SDevice process 및 로그 추세 확인 필요.
- Next READ ONLY: `sed -n '170,210p' pp2_des.cmd`; `grep -niE 'break|stop|abort|fail|converg|quasistationary|goal|simulation finished' n2_des.log | tail -n 35`; `tail -n 20 n2_des.plt` (binary 여부 주의) 또는 2.070V 이후 log; `ps -fu semi437 | grep '[s]device'`, `tail -n 10 n6_des.log`. 기존 실행/코드 건드리지 않음.

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
- **Correction supersedes prior 2026-10-13 audit**: `SWB_PASTE/sdevice_des.cmd` L35 is `Recombination( SRH Radiative Auger )` without `SRH(DopingDependence)`. Sentaurus UG SRH Doping Dependence chapter (verified older UG H-2013.03 and O-2018.06; local T-2022.03 not directly executable) states Scharfetter doping dependence applies *only* when explicitly selected; otherwise lifetime τ=taumax. In `.par`, `taumax=1e-7s` all GaN/InGaN/AlGaN; thus expected intended constant τn=τp=100ns. Previous claim current EBL τ≈0.05ns was INCORRECT; value only a conditional hypothetical IF DopingDependence were enabled. Keep current SRH command for desired fixed 100ns and inspect n2 effective physics in S0 before definitive claim.
- 50% polarization and 70:30 offsets are precedent as *model assumptions*: Lu et al Nanoscale Res Lett 16:99 (2021) 50%/70:30; Yin et al Front Optoelectron 17:8 (2024) 50%/70:30; Baek et al Nature Commun 14:1386 (2023) used 50% and **50:50** offset, plus SRH100ns/B1e-10/C1e-31. Vurgaftman & Meyer 2003 bowing InGaN1.4eV and AlGaN0.7eV; V2 numerical 300K bandgaps 2.85686eV (In0.15GaN) and 3.75641eV (Al0.15GaN) correct. 70:30 offsets only assumed, not measured.
- Mg neutral bulk approximate inversion with Nv=4.6e19 cm^-3,g=4,T=300K,p=3e17: GaN EA0.17 => NA=5.9159e18; Al0.15GaN EA0.20 => NA=1.8222e19. Close to 6e18/2e19 but actual carrier/ionization in 26nm strained EBL not proven. Prior AlGaN activation interpolation GaN0.17/AlN0.47 gives EA(x=0.15)=0.215eV; 0.20eV is model assumption requiring check. p+cap20nm/new contact & geometry require provenance/control.
- Critical postprocessing: `bl2_check.py` treats IQE as QW rad/whole-device recombination and qR/I≈1 as universal steady-state pass, both invalid in presence of leakage; EBL share excludes EBL Auger/trap; trap electron `eGapStatesRecombination` may require accounting for corresponding hole trap rates and not double count SRH; stdout .plt units/column names need real T-2022.03 validation. Extra QW effective IQE and radiative current efficiency must be distinguished. No simulator execution/experiment in ZIP.
- QS previous 0.0193V Newton failure cannot be attributed to RHSMin=1e-3 alone: loose residual threshold can prematurely accept a solution if used, but cause unproven without accepted-step history, Newton norms, Jacobian/method, actual initial states. V2 `Math` has ErrRef(e/h)=1e7, no explicit `Method=Super` nor `RHSMin`; log must show effective solver and accepted step. `ExtendedPrecision` is not guaranteed cost-free. S0 proposed stage2 V1=0.1→Vmax=0.2 with `MaxStep=0.02` normalized implies at least 50 QS increments if full stage runs; main stage 2.0→3.6 implies at least 50 (normalized MaxStep .02), regardless of convergence retries.
- Null control same coordinate-window mesh design is good intention but B changes materials and heterointerfaces; must compare mesh node coordinates/topology, region maps, area/sidewall length from actual SDE mesh, not assume exact hash equality. Project B substitutes QW edge with AlGaN (and shrinks QW volume), distinct from externally grown conformal AlGaN barrier. Project A traps in every Edge layer up to cap/nMesa, not an experimentally confirmed implanted carbon profile. Surface shelf floor damage omitted.
- Run gate: S0 parse/build contacts and 0V solution, material/ionization/polarization orientation/charge, QW potential and electron+hole density; threshold J>1A/cm2 by 3.6V only heuristic, measured microLED regimes can be below; matched J for NtSide comparison; convergence and current balance via contact I + electron/hole flux & leakage independent of recombination; mesh refinement convergence before publication. Quantum confinement / Schrödinger/QCSE radiative overlap not explicitly in drift-diffusion+constant B baseline. T-2022.03 exact `MaterialInterface=AlGaN/InGaN` with absent interface, CurrentPlot eGapStates Integrate, Plot(Intervals), build-mesh dual argument remain actual preprocess/runtime checks, not proven syntax.

## 2026-10-13 — 이택규 Claude Baseline V2 ZIP static audit (OBSERVED code / PROPOSED run / UNRESOLVED physics)
- Evidence: user-uploaded `CMP_BASELINE_V2_20261013.zip` SHA256 `8f26d1d17fb24ba4528dc51daf0bb9edf3f95c6c984ceb942e02e5882099bde8`; README marks `PROPOSED / NOT RUN`; contains bl2_dvs.cmd, bl2_des.cmd, bl2_des.par, bl2_check.py, SWB_PASTE variants and guides. Internal SHA256SUMS match. No school server run/log/TDR in ZIP; user opening statement mentions run, therefore actual server execution status remains UNVERIFIED pending logs.
- **Critical OBSERVED source inconsistency**: `bl2_des.par` Scharfetter all 3 materials: `taumin=0`, `taumax=1e-7 s`, `Nref=1e16 cm^-3`, `gamma=1`. This is doping-dependent, NOT globally constant τ=100ns as README claims. At nominal chemical doping N, standard model τ=1e-7/(1+N/1e16): pGaN 6e18 =>0.1664ns; EBL 2e19=>0.04998ns; nGaN 5e18=>0.1996ns; pCap 5e19=>0.019996ns; QW 1e15=>90.91ns. Actual effective lifetimes require T-2022.03 runtime confirmation. Do not claim V2 physical recombination calibrated.
- Literature consistency check: VM2003 recommended InGaN bowing 1.4eV and AlGaN bowing 0.7eV; nominal 300K gaps in .par are arithmetically plausible. 50% polarization used in simulation literature but **not calibrated for CMP** and changes protected Common Baseline parameter (requires separate candidate/control). The README's 94% CAL charging attribution and causal polarization/EBL interpretation are NOT confirmed by existing GitHub audit; do not repeat as observed proof.
- `bl2_check.py` uses `tot=Rad_all+SRH_all+Aug_all+Trap_all`, qR/I ≈1 pass band, J geometry conversion and QW Rad/tot labeled IQE; need verify actual currentplot field semantics, trap bookkeeping/no double count, current units/AreaFactor, leakage/contact current and SDevice output. A universal qR/I=1 steady-state pass gate is invalid if current escapes recombination volume. No physical output or script execution validated.
- Geometry/SWB variant inspection: 13 mesa layers x3 +2 nGaN=41 intended regions; Clean/Edge/Dmg and Project A carbon-off/B Bspan0 are a useful null-control design, but `same mesh` across material-changing Project B requires actual node/coordinate comparison. SWB_PASTE variants intentionally fix most parameters and keep only Wedge/Bspan, NtSide/PolAct/NCedge/V1/Vmax/NPlot variables.
- Priority before any baseline promotion: (1) reconcile requested 100ns vs actual Scharfetter model; (2) keep POL50/CAL/5V control untouched and run new independent SDE/preprocess smoke; (3) verify 0V contacts/orientation, exact species/ionization and par model loading, field/charge, mesh, AreaFactor, field names and CurrentPlot; (4) test QS ramp/continuity, separately quantify leakage & recombination; (5) matched-current NtSide splits, then Project A/B pilot. Do not call S0/S1/S2 completed without server outputs.

## 2026-10-13 — 이택규 CAL 1.2.0 별도 4.207V 로그 검증 (OBSERVED / UNRESOLVED)
- 사용자 제공 실제 학교 서버 read-only 출력 `tail -n 20 ../CMP_BASELINE_1.2.0_CAL/n2_des.log`. CAL 1.2.0 마지막 표시된 완료 단계 anode Voltage `4.207E+00 V`, anode electron current `2.330E-17`, hole current `6.423E-14`, total current `6.429E-14` (raw solver output; 단위 정규화 미확정). 다음 계산 시도 `Computing BE-step from 0.841422 s to 0.841424 s (Stepsize 1.6305e-06 s)`; 뉴턴 반복 2 `|Rhs| = 1.39e-03`으로 threshold 1e-03 미달, 해당 단계의 성공/실패 아직 미확인. 직전 완료 단계 wallclock 8.03 s.
- 앞서 `/proc` cwd 실제 출력: PID 88354 -> `CMP_BASELINE_1.2.0_CAL`; PID 94012 -> `CMP_BASELINE_1.4.0_POL50`. POL50 이전 시도 시작 시각 0.572527s, ≈2.863V, stepsize 6.7501e-06 s, 반복 RHS 1.17e-03. 두 프로젝트 모두 매우 작은 adaptive step에서 느리게 진행함. 로그의 마지막 iteration 종료 여부만으로 job 실패/성공 판단 불가; 실제 CAL/POL50 log mtime 및 accepted step 후속 확인 필요.
- CAL 1.2.0 최근 완료 4.207V와 POL50 2.863V의 raw current를 공정한 민감도 비교로 취급하지 않음. 원래 CAL 1.2.0이 목표 5V인지, 현재 데이터를 보존하고 중단 가능한지 재확인 필요. 이미 독립 CAL4V 4V 결과는 GitHub에 user-reported 존재, 따라서 우선 목표는 POL50 동일 조건 4V 비교이지만 CPU 경합과 CAL 중단의 적절성은 UNRESOLVED.
- NEXT READ ONLY: `ps -p 88354,94012 -o pid,etime,time,pcpu,pmem,nlwp,stat,args` 와 `nproc` 출력으로 활성 프로세스의 자원 상태 파악; 필요시 `stat`와 `tail`로 각 로그의 실시간 시간 증가 검토. 원본 job의 무단 kill/restart 금지. 코드 수정 없음.

## 2026-10-13 — 이택규 CAL/POL50 active SDevice PID provenance confirmed (OBSERVED)
- 사용자 제공 live school server command `ls -l /proc/88354/cwd /proc/94012/cwd` 실제 결과: PID `88354` -> `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL`; PID `94012` -> `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.4.0_POL50`. 앞선 `ps -fu semi437`는 두 프로세스가 각각 Oct10, Oct12 시작, 각각 `sdevice --max_threads 4 pp2_des.cmd`라고 표시했다. 이 PID 매핑은 직접 관찰된 사실이며 PID 88354는 CAL4V가 아니라 **1.2.0_CAL** 임을 유의.
- 최신 POL50 로그 발췌 t≈0.572527s (5V/s 기준 V≈2.862635V) 및 작은 Stepsize(~6.75e-06s), 반복 RHS 1.17e-03>1e-03은 이전 별도 기록. POL50 4V 완료는 미확인. 두 SDevice 프로세스의 동시 실행이 CPU/메모리 성능에 미치는 효과는 **미검증 가설**, 느린 원인을 확정하지 않는다.
- 다음 READ ONLY: 확인된 각 프로젝트의 log accepted time 변화와 `ps -p 88354,94012 -o pid,etime,pcpu,pmem,nlwp,stat,args`, `nproc` 등으로 현재 진행/자원 여부 점검. 기존 CAL이나 POL50 어느 프로세스도 임의 중단·재실행하지 않고 담당자 판단 후 조치. 소스 변경 없음.

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

## 2026-10-12 — 이택규 CAL4V polarization 50% one-variable experiment (DECISION / PROPOSED; not yet run)
- User explicitly chooses an immediate isolated sensitivity test: clone current completed CAL4V, change ONLY effective polarization-charge activation 1.0 to 0.5 (after verifying the actual active Sentaurus T-2022.03 syntax/parameter scope). No assumption this is experimentally calibrated.
- Verify actual server parent input, pp2_des.cmd/.par, Physics scope, interface polarization charge and absence of independent overriding FixedCharge; clone and preserve parent TDR/log/mesh/results. Nominal Goal 4V, FinalTime 0.8s, 5V/s transient, contacts, geometry, doping, NtSide=0, SRH lifetime, traps, all other physics, material parameters, mesh, solver held fixed.
- Candidate name CMP_BASELINE_1.4.0_POL50, subject to server name collision and version policy check (physics change needs MINOR not PATCH). SWB native filenames unchanged; check original model actually applies activation 1 and where.
- Claude may prepare/run isolated clone after preprocessed one-factor diff and quick syntax smoke. No second factor or additional bias hold. Compare parent/new exact bias/time, anode/cathode currents, EBL/QW SRH+Radiative, e/h QF/density, actual PE_Charge distribution, geometry and unit consistency. Improvement proves sensitivity only, not polarization as sole cause.
- No school server execution or code edit by ChatGPT. JuSubin 5V_TEST unchanged; Claude/user must report actual simulation outcome and GitHub sync according to protocol. Prior CAL4V 99.77% EBL SRH user-reported, cause UNRESOLVED.

## 2026-10-12 — 이택규 CAL4V time-critical validation strategy (PROPOSED, not executed)
- Worker: 이택규. Decision-support review: sequential read-only diagnosis alone is too slow for deadline; propose parallel, versioned short *one-factor* physics sensitivity tests, with intact baseline and preserved parent outputs. These are diagnostic experiments, not baseline adoption.
- Preferred controlled variants after checking active material parameters and source lineage: (0) unchanged CAL4V 4V ramp then bias-hold to check temporal stability, (A) EBL AlGaN SRH lifetime only increased by 10x as an explicitly arbitrary sensitivity test, (B) polarization activation 1.0 vs 0.5 as a literature-motivated sensitivity, not a calibrated model. Separate NLM line/mass/syntax review and smoke test only after valid definition. Clone project and compare same bias/time/ramp/geometry/mesh/ROI; if resource/lifetime constraints run reference+EBL sensitivity first, polarization later. Save outputs QW Rad/SRH, EBL SRH, anode/cathode conduction/total, QF, densities, terminal charge, signs, and spatial currents. Do not use current increase alone as acceptance or claim the whole current residual is charging.
- Evidence: Claude user-reported whole domain 4V CAL4V EBL accounts for 99.767% of SRH, cause unproven; scientific examples show EBL/polarization influence injection (Physica E 77 2016 DOI 10.1016/j.physe.2015.10.036; JJAP 51 09MK03 DOI 10.1143/JJAP.51.09MK03). NLM V2 still held, missing mass/mesh concerns.
- No TCAD code or server run performed or authorized as completed by ChatGPT; plan PROPOSED. Need confirm compute licensing/simultaneous jobs and possible restart checkpoint provenance before initiating.

## 2026-10-12 — 이택규 CAL4V 전영역 EBL SRH 결과 (USER-REPORTED, DERIVED)
Claude 보고 수치: SRH 총 12294.2, EBL 12265.6, QW 5.134 [s^-1 um^-1]. EBL은 SRH의 99.7674%. q(R_SRH+R_rad+R_Auger)=1.96975e-15 A/um은 단자 total 3.498e-14의 5.6311%. **나머지 94.37%가 charging이라는 결론은 미확정**: 재결합 적분은 총 DC 단자 전류와 동일하지 않음. 사용자 제공 Claude 요약에 근거, 학교 raw TDR/PLT는 이 AI가 확인하지 못함. 다음: AlGaN SRH lifetime 파라미터·중앙 clean EBL/QW1 cutline e/hDensity/e/hCurrentDensity/QuasiFermi/Potential/SRH/PE_Charge 검증. 기존 소자 및 주수빈 5V_TEST 변경 없음.

## 2026-10-12 — 이택규 CAL4V Claude 19:30 재판단 전달 / ChatGPT 독립 검토 (USER-REPORTED / DERIVED / UNRESOLVED)
- SOURCE: 이택규가 Claude 작성 `CAL4V_LOWJ_LOWIQE_DIAGNOSIS.md` 텍스트를 현재 채팅에 제출. 이는 **Claude 보고서의 내용**이지 ChatGPT가 Sentaurus 학교 서버나 T-2022.03 원본 문서를 직접 검증한 결과가 아님. 기존 CAL4V 코드/실행 변경 없음.
- Reported CAL4V 4V: anode TotalCurrent=3.498e-14 A/um; QW integrals Rad=6.29e-4, SRH=5.13, Auger=2.13e-4 s^-1 um^-1. From these values, q*(Rad+SRH+Auger)=8.221e-19 A/um and ratio to anode total=2.350e-5 (0.002350%). This **does not itself prove** 98% charging current or hole-only starvation: QW-outside recombination, other leakage paths, transient charge and sign/normalization must be checked.
- Claude RETRACTED claims that 4V current is 98% charging, MQW QF jumps add up to 2V loss, or EBL band bending proves 1V electrostatic loss. Claude reported parent 5V displacement=3.29e-18 against total=1.448e-11 (different run/bias); cannot infer 4V CAL4V charging fraction from 5V parent electrode component. Earlier 4V I(V) plateau and tau-insensitive anode current are suggestive, not direct transient charging measurement.
- Claude also reported flat hQuasiFermi through EBL on user SVisual cutline, reducing evidential support for EBL as dominant **hole electrochemical potential drop**. QW1 radiative concentration alone cannot establish which carrier is limiting; inspect n, p, e/h current and QF across verified coordinates.
- Claude reported T-2022.03 UG text inspection: NonLocal keywords exist but proposed V2 has potential wrong mesh-side coverage and missing tunneling mass mt. Exact manual excerpts were not independently made accessible to this ChatGPT; no V2 deployment. Model choice (NLM/polarization/composition variation) UNRESOLVED, baseline protected.
- Important verification boundary: SDevice `anode Charge` is **electrode charge plus associated doping-well space charge**, not necessarily the device-wide stored-charge integral (O-2018.06 UG, Electrode Charge Calculation). Thus d(anode Charge)/dt / anode TotalCurrent near one is a diagnostic only, NOT a sufficient standalone confirmation that 90-100% of current is junction charging; require terminal signs/conservation, time/bias dependence and charge scope. 4V conduction-vs-charging remains unresolved.
- NEXT (READ-ONLY): inspect CAL4V `n2_des.plt` actual datasets and synchronized `anode/cathode Charge, TotalCurrent, DisplacementCurrent, eCurrent/hCurrent, time, bias`; estimate finite differences with units/signs and no sharp arbitrary thresholds. Then export verified central clean-region TDR cutline e/hQF, density, current, Ec/Ev, Potential, polarization fields; resolve actual NLM coverage/manual before any user-approved small-scale smoke. JuSubin 5V_TEST untouched.

## 2026-10-12 — MQW NonLocal v2 proposal physics/source audit (OBSERVED user report / CRITICAL REVIEW / PROPOSED)
- 2026-10-12 18:23+ KST 이택규 supplied second Claude proposed CAL4V patch: SVisual center(? y=2.0um) x=0.10..0.30um QW band cutline shows sharp ~0.35-0.5eV jumps in electron/hole quasi Fermi across QW/Barrier interfaces, EBL bent Ev ~-4.0 to -5.05 and Ec~-0.3 to -1.55. Values are USER-REPORTED from SVisual, no raw screenshot/point data independently read; lateral y=2.0 may be edge depending half-device coordinate, so actual region/cutline must be checked. Critical physics review: across QWs BOTH eQF and hQF rise in same direction, so local F_n-F_p approximate QW1~1.95,QW2~1.90,QW3~1.75,QW4~1.45 eV; these splits are not voltage loss from 4V. QF jumps permitted at Thermionic heterojunction boundary, thus not proof of absent tunneling. EBL ~1eV band edge slope not equivalent direct electrostatic voltage drop without Potential/offset extraction. Capacitive equivalent thickness ~24nm near EBL26nm is NOT proof of voltage localization. Existing n2_des.plt true transient DisplacementCurrent not yet extracted; do not treat total as conduction nor 98% claim as verified. Important corrected external literature finding after reading primary full 11-page PDF: Rahman, Jamal-Eddine, Xia, Awwad, Armitage, Rajan, J Appl Phys 132:235702 (2022) DOI 10.1063/5.0125684 / arXiv 2211.05704 explicitly uses thermionic emission (TE), field emission (FE), and non-local quantum barrier tunneling (QB tunnel) across QWs/QBs in SILVACO TCAD (p3 lines 102-114); Fig3c p5 says including FE and QB transport improved forward-voltage trends; BUT even all relevant transport models uniform-well simulation overestimated turn-on, and actual key improvement was composition fluctuation low/high In lateral current path. Thus strong support to TEST a QB tunneling sensitivity as model physics, NOT proof Sentaurus T2022 source syntax or that QB tunneling alone fixes homogeneous CAL4V blue 4QWs. Older SDevice guide O-2018.06/H-2013.03 independently checked on web: global Math NonLocal named mesh supports reference MaterialInterface/RegionInterface/Electrode with Length/Permeation/Direction/MaxAngle; global Physics eBarrierTunneling meshname,hBarrierTunneling meshname; Plot eBarrierTunneling/hBarrierTunneling valid field rates (per cm3/s) with mesh dependence. The EXACT required T-2022.03 UG text reference/tcad_ug_text/sdevice_ug.txt is NOT present in connected CMP GitHub or available directly, so ALL EXACT VERSION SYNTAX compatibility explicitly unverified; user-reported T2022 line ranges 43563 etc cannot be independently crosschecked. Do not claim syntax has been verified T2022. New proposed NonLocal Math(MaterialInterface=InGaN/GaN Length=5e-7 cm Permeation=5e-7 cm Direction=(1 0 0) MaxAngle=5 degrees) may target material interfaces regardless clean/Dmg lateral branch if actual material identities appropriate; actual count 4 QW*2 vertical interfaces =8 vertical planes, each split into clean/damaged lateral segments. Count/lines require simulator log, not assumed. Direction x normal is conceptually consistent if actual mesh x growth (user-reported) but MaxAngle5 can suppress tilted paths. Length/Permeation 5nm are geometrical nonlocal mesh limits NOT necessarily physically calibrated spike thickness or tunnel through 22nm GaN quantum barriers; actual lines need inspect, potential risk double-count or unintended paths. Since QB22nm, 5nm likely insufficient as full interwell bridge, may still sample narrow interface spikes. e/h tunneling can increase compute time, user approval needed, no Run or code changed. Do not accept 'Goal3.5V total I>=1e-12A/um' as scientifically grounded pass/fail; if ramp same5V/s charging current may remain, total is not DC conduction; compare matched bias/current true conduction after ramp-hold/stationarity, QF discontinuity and QW n/p and recombination, inspect tunneling rates integrated/mesh dependence. Sequence: existing CAL4V PLT displacement current, QW band/charge/current cutlines in non-damaged central region; verify effective 2022.03 manual actual excerpts and NonLocal generated lines, THEN separate minimal test (1D-like 2D column not representative of sidewalls; prior QS failed); only after successful physics-sensitive trial consider versioned 2D half study and compare with saved untouched CAL4V. Polarization 50% literature-assumed sensitivity (Lu 2021 DOI 10.1186/s11671-021-03557-4; Yin 2024 DOI 10.1007/s12200-024-00111-9), not calibrated or a substitute for QB. No changes to JuSubin 5V_TEST and no scripts run. Scientific decision status: QB NLM is PROPOSED for independent test after proof of transport restriction, not baseline adopted. Main blocker physical low-J Gate0 remains.

## 2026-10-12 — Claude CAL4V diagnosis independently challenged (REVIEW)
- 2026-10-12 18:23 KST, worker 이택규 shared Claude independent CAL4V low-J diagnosis for critical review. This is REVIEW, NOT actual new simulation evidence. 1. CAL4V 4V Transient ramp 5V/s, terminal total=3.498e-14 A/um. Claude says 98% displacement and conduction 0.7e-15 A/um. Actual charging fraction UNVERIFIED: plateau alone cannot decompose; inspect n2_des.plt anode DisplacementCurrent and TotalCurrent data at 4V. Current-density conversion remains conditional on 2D normalization. Output eCurrent~5.27e-20, hCurrent~3.498e-14, total~3.498e-14 should be identified carefully before claims. 2. With all current assumed capacitive, C'=I/(5V/s)=6.996e-15 F/um. eps_r 9.5 and 2um x1um assumed footprint give equivalent t~24.0nm near EBL 26nm; arithmetic correct but distributed capacitance cannot localize EBL voltage drop. Need actual Ec/Ev/Potential profile. 3. From Rrad/SRH ≈ B tau (n+p) with B=2e-10 cm3/s and tau=100ns, n+p≈6.12e12 cm-3 conditional on ideal Bnp, equal lifetimes, negligible SRH n1/p1, uniform carrier density; integrated 8-QW values and doping-dependent lifetime invalidate direct inference. Not proof of low hole density. 4. EBL hole barrier/polarization is scientifically plausible from published studies but causal ranking remains PROPOSED; alternative current normalization, contact injection, active hole doping, band offsets, distributed carrier density, missing calibrated transport physics remain. 5. Literature verified: Lu et al 2021 Nanoscale Research Letters 16:99 DOI 10.1186/s11671-021-03557-4 explicitly uses 50% polarization and 100ns SRH; Yin et al 2024 Frontiers of Optoelectronics 17:8 DOI 10.1007/s12200-024-00111-9 explicitly uses 50% polarization, 100ns and SRV=1e4 in different MIS microLED; Baek et al 2023 Nat Commun 14:1386 DOI 10.1038/s41467-023-36773-w is low-current QB/EBL engineering (not source for 50% polarization); Rahman et al 2022 JAP 132:235702 DOI 10.1063/5.0125684 explains composition fluctuations / limits 1D fixed-polarization models, not proof a specific Nonlocal tunneling keyword is mandatory. 6. Do not copy global eBarrierTunneling+hBarrierTunneling with NonLocal Barrier(Region=Clean_EBL Region=DmgL_EBL) Length=4e-6 into current model. Sentaurus documentation states Barrier(...) mesh configuration primarily for direct insulator barriers; AlGaN EBL is semiconductor, actual valid T2022.03 geometry and tunneling masses/method unknown. Turning polarization off only at AlGaN/GaN interfaces does NOT remove InGaN/GaN MQW QCSE. Polarization 0% and 50% allowed only as clear diagnostic/sensitivity hypothetical with original 100% controlled, no arbitrary recalibration. Next: inspect existing n2_des.plt dataset list for DisplacementCurrent/TotalCurrent and 4V values, then SVisual existing n2_4V_final_des.tdr vertical center cutline Ec/Ev, quasi Fermi, n/p, PiezoCharge and current density; ONLY then consider independently versioned 1D controlled stack or 2D half run. 1D loses mesa/sidewall and QS may not converge; no promise faster. Maintain JuSubin 5V_TEST split ownership. No simulation/TCAD source changed.

## 2026-10-12 CAL4V NtSide=0 confirmed in active preprocessed deck
- 이택규가 CAL4V `pp2_des.cmd` 12개 `Traps` 블록의 `Conc=0` 모두 실제 grep으로 확인 (line 145 through 365). 따라서 완료된 CAL4V 4V 계산에서 이 explicit sidewall bulk-trap mechanism은 비활성. 그럼에도 이전 8-QW 적분 SRH 99.9836%, 방사비율 0.0122426%; 다른 벌크 SRH/캐리어 주입 문제 또는 surface mechanisms는 아직 가설. Next read-only inspect transport/current-density normalization and existing QW electron/hole densities. 서버 모델 변경 없음.

## 2026-10-12 — CAL4V region Physics audit step (OBSERVED)
- 이택규 provided real CAL4V pp2_des.cmd read-only grep: global Physics line 50, Piezoelectric_Polarization(strain) 64, global SRH() 80; separate Physics(Region="Clean_pGaN") at 126 and 12 Physics(Region="DmgL_...") at 135,159,179,199,219,239,259,279,299,319,339,359. No separate Recombination/SRH declaration and no literal SurfaceRecombination, SurfaceTrap, Interface= matched in this search. Plot SRHRecombination et al at 398+ are output field names, not evidence of extra active recombination. IMPORTANT search omitted Traps, so region-specific explicit traps may still exist; absence of named surface keywords does not prove actual SRV=0. Existing CAL4V referenced InGaN Scharfetter taumax=1e-7s remains confirmed nominal. Root cause of low J/radiative fraction unresolved. NEXT perform read-only `grep -nEi 'Traps|Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/pp2_des.cmd | head -n 35` to check n2 trap concentrations. No model changes; separate JuSubin 5V_TEST split task unaffected.

## 2026-10-12 — CAL4V active InGaN Scharfetter custom par 100ns verified (OBSERVED)
- 2026-10-12 이택규가 실서버 read-only grep 출력으로 CAL4V actual custom material parameter file `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/FASTC1_pp6_des.par`의 `Material="InGaN" { Scharfetter {...} }` 항목을 확인. pp2_des.cmd의 File Parameters가 바로 이 파일을 가리키고 Global Physics에서 SRH() 활성화. InGaN Scharfetter lines 47–53: `taumin = 0.0,0.0`, `taumax=1.0e-7,1.0e-7` seconds, `Nref=1.0e16,1.0e16` cm^-3, `gamma=1,1`, `Talpha=0.0,0.0`, `Tcoeff=0.0,0.0`. Therefore nominal maximum electron/hole lifetime 100ns actually PRESENT in referenced CAL4V custom .par, and missing-entry hypothesis weakens. Scharfetter is doping-dependent; 100ns is a maximum under this parametrization, NOT a verified spatially constant effective QW lifetime. QW doping/concentration and any Material/Region Physics/SRH overrides unknown. This does not solve extraordinarily low raw 4V terminal current or 8-QW 3-rate fraction 0.0122426%, and no rationale to tune params again. NEXT read-only inspect remaining pp2_des.cmd Physics blocks and interface SRV, QW doping and actual injection/2D current scaling, keeping JuSubin's separate NtSide 5V_TEST track untouched. OBSERVED source setting; effective per-point carrier lifetime and physical adequacy UNVERIFIED. No SDevice/model changes.

## 2026-10-12 — CAL4V global Physics syntax directly inspected (OBSERVED)
- 2026-10-12 이택규 CAL4V의 실제 `pp2_des.cmd` lines 14–90 read-only sed 출력 제공. File: Grid=n1_msh.tdr; Parameters=FASTC1_pp6_des.par; Plot=n2_des.tdr; Current=n2_des.plt; Output=n2_des.log. Electrode anode/cathode both initial Voltage=0.0. Global Physics: Temperature=300.0, Fermi, Thermionic, Piezoelectric_Polarization(strain), DefaultParametersFromFile, EffectiveIntrinsicDensity(NoBandgapNarrowing), Recombination(SRH(), Auger(), Radiative). 이 블록은 세 재결합 모델 활성화의 직접 증거지만 InGaN 유효 SRH tau=100ns 또는 국소 재결합 수치의 근거 자체는 아니다. 이전 whole pp2 grep에는 AreaFactor 미표시; 단자 전류 단위, 2D normalization 미확인. 다른 per-material/per-region Physics overrides, 명시적 surface recombination 설정 존재 여부도 아직 미확인. NEXT 별도 CAL4V custom active par `FASTC1_pp6_des.par`에서 InGaN Scharfetter/SRH tau 및 active material blocks 읽기전용 검사; 이후 pp2 global/local Physics 범위와 current scaling 검증. 서버 파일이나 계산 결과 변경 없음. 주수빈의 5V_TEST split parity/QW integration과 다른 독립 track 유지.

## 2026-10-12 — CAL4V pp2 physics and current-file declarations checked (OBSERVED)
- 2026-10-12 ~17:xx KST 이택규가 CAL4V 전처리 입력 pp2_des.cmd에서 읽기전용 grep 실제 출력 제공: `20: Grid="n1_msh.tdr"`, `22: Parameters="FASTC1_pp6_des.par"`, `26: Current="n2_des.plt"`, `60: Thermionic`, `64: Piezoelectric_Polarization(strain)`, `462: PE_Polarization/vector`, `466: PiezoCharge`. 주어진 grep 정규식에 대한 `AreaFactor` 결과 없음. 이는 pp2_des.cmd 내 명시적 AreaFactor 항목이 없는 것으로 보인다는 관찰이며, 실제 terminal current A/µm/2D normalization 또는 활성 polarization 전하 크기가 정확하다는 뜻이 아님. Polarization 및 Thermionic 선언은 존재하나 정확한 Physics 범위, piezo activation, parameter value는 추가 확인 필요. 저주입/0.01224% 방사비율의 원인을 단정하지 않으며, 다른 연구원 주수빈이 맡도록 제안된 n2/n4 5V Trap-on/off 작업과 중복하지 않음. NEXT CAL4V pp2 `sed -n '14,90p'` 읽기 전용으로 File/Electrode/Physics/Math/계면 블록 범위 확인; 이후 active .par 및 n2_des.log 2D 단위/AreaFactor audit. 실행 코드 및 결과 변경 없음.

## 2026-10-12 — LeeTaekGyu independent CAL4V physical Gate0 track (PROPOSED)
- 2026-10-12 ~17:03 KST, current worker 이택규 says he is now working alongside 주수빈 and wants nonoverlapping tasks. Proposed coordination (not confirmed as accepted by 주수빈): 이택규 owns read-only physical Gate0/low-current audit in separate project `CMP_BASELINE_1.3.0_CAL4V` (2D terminal current units/AreaFactor, active InGaN SRH 100ns, QW injection/EBL/polarization) without source modifications; 주수빈 may own `JUSUBIN_FAST_HALF_5V_TEST` NtSide0 Node2 vs NtSide1e18 Node4 5V parity gate (pp2/pp4 deck and .par/mesh differ only trap) followed by paired MQW Rrad/SRH/Auger integrals, avoiding overlapping CAL4V. Both finished sources/results remain protected. Last user-provided `pp4_des.cmd` grep explicitly showed 12 Traps Conc=1e18, confirming planned NtSide1e18 actual preprocessing (pending pp2-vs-pp4 other-input parity). No fresh simulation or technical result here; this is a PROPOSED parallel work allocation. AI cannot directly send task to collaborator's separate chat; share via GitHub as a proposed handoff only.

## 2026-10-12 — User-supplied four hypotheses for very low MQW radiative fraction (PROPOSED, not verified)

- Worker 이택규 shared external suggestions for causes of low microLED radiative efficiency: (1) high sidewall surface recombination velocity (SRV) and surface/interface trap concentration; (2) full spontaneous/piezoelectric polarization and QCSE, with proposed polarization sensitivity scaling 0.3–0.5; (3) excessive Auger coefficient or ineffective SRH taumax/taumin/current-density interpretation; (4) too-coarse MQW/sidewall mesh.
- All four remain **PROPOSED / UNVERIFIED** rather than established faults, prescriptions, or baseline changes. No source provided verifying universal SRV=10³–10⁴ cm/s, polarization Scale 0.3–0.5, or generic operating J=0.1–10 A/cm² for this particular model.
- Existing direct evidence constrains their priority: for completed NtSide=0 5V_TEST all 12 explicit DmgL trap concentrations were 0 in preprocessed deck, so this parameterized sidewall trap family cannot by itself explain its large SRH (a different surface/interface model remains to be checked). 100ns CAL4V full-MQW SRH share ≈99.9836%, Auger ≈0.00414%, making Auger **not the dominant observed rate channel** at 4V. Effective active polarization/QCSE, current normalization and full-vs-half/coarse mesh equivalence are unverified.
- NEXT unchanged: await user's pp4_des.cmd grep and verify Node4 NtSide=1e18, compare effective pp2/pp4 input; separately audit normalized J, active physics / existing QW fields. Do not alter SRV/traps, polarization Scale, Auger or mesh without controlled hypothesis and user approval.

## 2026-10-12 — Node4 5V normal finish and blue-MicroLED clarification
- 2026-10-12 현재 작업자 이택규가 SWB Node4 Explorer 실제 `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/n4_des.out` 마지막 화면 제공. 노드 n4: 5.000E+00 V, electron current 7.534E-14, hole current 6.975E-12, total terminal current 7.050E-12 (log raw values; 2D units/AreaFactor unverified), successful `n4_5V_ckpt_des.sav` and `n4_des.tdr` writes, `Curve trace finished`, `Sentaurus Device simulation finished`, `Good Bye`. Finished Mon 2026-10-12 00:12:02 KST; wallclock 29806.55s (~8h16m46.55s), CPU total 80172.55s, peak memory 3.11GB. **CONFIRMED 5V SDevice n4 completion**, but screenshot does not show NtSide parameter: intended n4 NtSide1e18 split condition NOT CONFIRMED until pp4_des.cmd actual DmgL trap `Conc` audit and parent n2 input comparison. Previous 5V_TEST NtSide0 n2 terminal raw I2D~1.4480164608e-11, so n4 raw current ratio ~0.487; no trap-only causal claim without pp2/pp4 parity. CAL4V 100ns 4V MQW radiative fraction=0.0122426% remains distinct simulation and bias; do not confuse n4 5V with CAL n2 4V. GitHub COMMON_BASELINE.md explicitly says blue InGaN/GaN, xIn=0.15 4QW, nominal ~445nm; desired color BLUE not red, spectral peak not verified by EL. Researcher asks whether normal efficiency '0.1': distinguish fractional 0.1=10%, 0.1%=0.001 as fraction, 0.1 A/cm2 current density not an efficiency. None is default expected at arbitrary J; literature (Kou 2019 10.1364/OE.27.00A643; Baek 2023 10.1038/s41467-023-36773-w; Wang 2023 10.1038/s41467-023-43472-z) confirms blue microLED efficiency depends on J, fabrication and sidewalls. CAL 0.01224% is modeled MQW 3-mechanism radiative share, NOT observed experimental EQE, and physical low-J Gate0/2D current normalization still open. NEXT read-only `grep -nE 'Conc[[:space:]]*=' /user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST/pp4_des.cmd | head -n 16` to confirm actual trap concentrations. Further compare pp2/pp4 other physics/current and matched 5V QW recombination; preserve all existing outputs. No server code modified.

## 2026-10-12 — CAL4V extremely low radiative share literature review
- 2026-10-12 Research assessment (이택규 question whether CAL4V radiative fraction 0.01224% is typical): Treat result as unusually low vs peer-reviewed working MicroLEDs, NOT sufficient proof of a model defect. Evidence: CAL4V 4.000V 2D raw terminal current 3.498e-14 (assuming A/µm), conditional half width ≈2µm gives J=(3.498e-14/2)*1e8≈1.749e-6 A/cm²; current conversion/AreaFactor/actual injection/steady-state remains unverified. Thus this is ~0.01/1.749e-6 ≈5718x below a published low-J example 0.01 A/cm² and ~0.1/1.749e-6≈57176x below 0.1 A/cm² benchmark. Published 3.5µm NBE-etched blue MicroLED Nature Communications 2023 DOI 10.1038/s41467-023-43472-z reports peak EQE 37.5% around 3 A/cm² and at 0.01 A/cm² only ≈26% relative droop; Nature Communications 2023 DOI 10.1038/s41467-023-36773-w reports 10x10µm blue MicroLED EQE 3.00% at 0.1 A/cm². Neither EQE benchmark is directly comparable to this model's MQW three-rate radiative share due to injection, geometry, sidewall processing and extraction differences. SRH normally dominates extremely low-current regime (literature-supported), but here NtSide0 still high SRH implies bulk/volume SRH or injection bottleneck rather than explicit sidewall trap; cannot infer causal parameter without matching sample and checking effective par. Existing parent 1ns at 5V had 0.10947% integrated QW fraction; CAL100ns at 4V is NOT matched bias, so changing lifetime cannot be causally judged. Recommended PRIORITY: verify current units, 2D AreaFactor, actual working J, effective InGaN 100ns parameter overrides, p/hole-injection/EBL/polarization/quantum well carrier densities, compare QW rates at same current and bias before baseline freeze, and avoid unmotivated long reruns. This is literature-backed review/diagnostic recommendation; NO simulation/model edit or confirmation of a single root cause.

## 2026-10-12 — CAL4V full 8-QW recombination integrated (OBSERVED)
- 2026-10-12 이택규가 Sentaurus Visual 캡처 3장으로 완료된 `CMP_BASELINE_1.3.0_CAL4V` `n2_4V_final_des` (4.000V; custom InGaN 100ns Scharfetter taumax model) 8개 **2D** QW 영역 `Clean_QW1..4 + DmgL_QW1..4` 적분 결과를 제공. 세 필드 모두 정확히 동일 영역, Total Domain=2.400002e-02 µm². 전체 적분값 [s^-1 µm^-1]: RadiativeRecombination=6.286680e-04; srhRecombination=5.134239; AugerRecombination=2.127778e-04. 합=5.1350804458. Radiative/(Rrad+SRH+Auger)=0.01224261249%; SRH share=99.98361378%, Auger=0.004143612%. 여기서 방사비율은 해당 세 재결합 필드의 **MQW spatial integrated radiative fraction**이며, 100ns 모델 소자/실험 검증 IQE 또는 EQE가 아님. QW1 Clean+DmgL accounts for approx 98.78% all-4QW Rrad. DmgL 4QW only radiative ≈5.35942e-05 and SRH≈0.020185 (subtract clean 4QW totals; rounded), not independent lifetime physics validation. Preexisting 1ns parent result (NtSide0, **5V**) 4-QW Clean+DmgL Rrad=40072.8158452, SRH=36562944.9075, Auger=1599.706168587 and radiative fraction=0.1094747566%; because these are at DIFFERENT biases (100ns 4V, 1ns 5V), cannot attribute change to lifetime or claim 100ns improves/worsens IQE. Parent 4V near-terminal-current PLT exists but 4V TDR spatial map not yet established. Low-J Gate0 and current-normalization/physical validity still UNRESOLVED. Next inspect other user-reported completed NtSide1e18 split normal-finish log; for IQE causality compare same J/voltage/regions/geometry and effective .par, ideally reuse saved checkpoints, avoid rushing new multi-day run. No code/server run changed.

## 2026-10-12 — CAL4V 4 Clean QWs Radiative/SRH/Auger integrals computed (OBSERVED)
- 2026-10-12 이택규 provided THREE SVisual Field Integration screenshots for CAL4V final dataset `n2_4V_final_des`, 4.000V, selecting ONLY the four dimension-2 regions `Clean_QW1` through `Clean_QW4` (not damaged sidewall strips). Recombination integrals unit s^-1 um^-1, in QW1/QW2/QW3/QW4 order: Radiative [5.674131e-4, 7.202020e-6, 4.579290e-7, 8.117469e-10] (displayed total 5.750738e-4); srhRecombination [4.940556, 1.246185e-1, 4.882792e-2, 5.108214e-5] (displayed total 5.114054); Auger [2.045051e-4, 1.234635e-7, 1.495005e-8, 8.907546e-11] (displayed total 2.046436e-4). Four Clean QW total area 2.394002e-2 um2. With displayed rounded totals sum=5.1148337178 and eta_rad,clean=0.01124326%, eta_SRH,clean≈99.9848%; QW1 accounts ~98.67% of clean-QW Rrad, ~96.61% clean-QW SRH. This is CONFIRMED SCREENSHOT-BASED 4-CLEAN-QW regional recombination fraction, NOT the full MQW IQE: `DmgL_QW1..4` not selected, no 1ns matched bias / optical injection calibrated comparison. Do NOT compare raw 4V clean-QW value to earlier 1ns 5V full-Clean+DmgL MQW radiative fraction (0.10947%) as lifetime-causality. Next select the 4 additional `DmgL_QW1..4` true 2D regions (not `Clean_QW# + DmgL_QW#` interface rows), while keeping Clean_QW1..4, repeat three integrations, check exactly 8 regions and no other domains, then compare and validate AreaFactor/current. Low-J baseline gate remains UNRESOLVED; no model or server code modified.

## 2026-10-12 — 이택규 CAL4V Clean_QW1 three-rate integration (OBSERVED)
- 2026-10-12 이택규 공유 SVisual `CMP_BASELINE_1.3.0_CAL4V/n2_4V_final_des` Field Integration 실제 결과: Dimension 2 region `Clean_QW1` 하나만 선택, Domain=5.985012e-03 um^2; RadiativeRecombination=5.674131e-04 s^-1 um^-1; srhRecombination=4.940556 s^-1 um^-1; AugerRecombination=2.045051e-04 s^-1 um^-1. 3항 합=4.9413279182 s^-1 um^-1. Clean_QW1에 한정한 radiative fraction =0.0114830084%, SRH fraction=99.9843783%. VERIFIED screenshot-based single-region integrations and ARITHMETIC; NOT entire four QWs, not total device IQE. Other QWs may differ substantially. Next integrate 2D volume Clean_QW1..4 AND DmgL_QW1..4 in all three fields (avoid `Clean_QW1+DmgL_QW1` interface rows if shown as Dimension 1). Compare 100ns 4V with 1ns at matched V/J and check current normalization. No TCAD source edits. NtSide1e18 split separate log verification remains.

## 2026-10-12 — CAL4V full bias and terminal-current readout verified (OBSERVED)
- 이택규가 실제 `CMP_BASELINE_1.3.0_CAL4V/n2_des.log` grep 출력 공유. 마지막 `Computing BE-step from 0.799739 s to 0.8 s (Stepsize: 2.6098e-04 s)` 직후 `anode 4.000E+00 5.270E-20 3.498E-14 3.498E-14`가 표시됨. 직전 단계 0.798939→0.799739s에서는 anode 3.999V, 총전류 표기 3.496E-14. 앞서 확인된 동일 Node2 `Curve trace finished` / `Good Bye` 및 final `n2_4V_final_des.tdr`, `n2_4V_ckpt_des.sav` 저장과 연결되므로 100ns CAL4V에서 최종 time 0.8s / anode 4.000V, 로그 전류 마지막 열 3.498E-14 달성과 정상 완료 CONFIRMED. 로그 전류 물리 단위/2D AreaFactor 및 정상 DC상태는 독립 검증 미완료; 기존 기록의 2D A/um 관행에 따른 원시 수치이며 조건 없이 면적 전류밀도나 IQE로 간주하지 않는다. 참고: 기존 1ns 5V_TEST 가까운 4.003369V에서 I2D=3.505521343e-14였고 CAL4V 4.000V와 약 0.2% 원시 전류 차이이나 서로 완전한 동일 바이어스 아님. 100ns의 재결합 개선 여부 미확정. NEXT 이미 확보한 final TDR의 4QW별 Radiative/SRH/Auger 적분과 비교전류 정상화 후 연구 판단; 별도 NtSide1e18 split은 실제 로그 미검증. 원본 데이터 보존.

## 2026-10-12 — CAL4V n2 정상 완료 확인 (OBSERVED screenshot; 공유/검증 이택규)
- Screenshot supplied by current worker 이택규 of SWB Node 2 Explorer in `/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.3.0_CAL4V/n2_des.out` confirms `Curve trace finished.`, `Plot(FilePrefix="n2_4V_final")` written to `n2_4V_final_des.tdr` successfully, `Save(FilePrefix="n2_4V_ckpt")` wrote `n2_4V_ckpt_des.sav` and circuit .sav, `n2_des.tdr` written, `Sentaurus Device simulation finished`, `Good Bye !`. Completed on Mon Oct 12 01:12:13 2026 (KST); wallclock 29706.72s (~8h15m6.72s), total CPU 84070.27s (~23h21m10.27s), peak memory 4.05 GB. Status **OBSERVED/CONFIRMED NORMAL SDEVICE FINISH and saved spatial final state**, replacing prior RUN-CLICKED-ONLY uncertainty for this CAL4V n2. Important: screenshot tail does NOT show numeric final anode V/current, nor `pp2_des.cmd` active physics/Goal/FinalTime, so numerical 4.000V endpoint and current/IQE are NOT YET EXTRACTED/INDEPENDENTLY VERIFIED. Prior source Goal=4.0, FinalTime=0.8, InGaN Scharfetter taumax 100ns were reviewed in previous conversation. Other reportedly completed NtSide=1e18 split not yet supported by its own log. Baseline physical Gate0 (low J, radiative fraction ~0.1095% old 5V) remains open. Protect saved results and existing 5V parent. Next: read-only last bias/current in n2_des.log or n2_des.plt, inspect n2_4V_final_des.tdr, extract 4 QW integrated radiative/SRH/Auger and compare matched V/J to old 1ns; independently inspect NtSide1e18 node output.

## 2026-10-12 — 이택규가 주수빈의 두 시뮬레이션 완료를 보고 (USER-REPORTED; LOG UNVERIFIED)
- 이택규가 2026-10-12 대화에서 주수빈이 전날 실행해 두고 간 '두 개' 시뮬레이션이 모두 끝났다고 보고. 직전 인수인계상 대상은 (1) 기존 `JUSUBIN_FAST_HALF_5V_TEST` 기반 NtSide=1e18 split과 (2) `CMP_BASELINE_1.3.0_CAL4V` (100ns, 0→4V)로 추정되며 **어느 두 SWB node인지 실제 로그나 화면으로 확인하기 전까지 프로젝트/노드 매칭 미검증**. 사용자 보고는 완료 주장의 근거이나 actual SDevice `Good Bye`/final V/timestep/terminal current/PLT/TDR/SAV는 미제공. NtSide=1e18 case가 NtSide-only matched input인지도 재확인 필요. 새 런이나 baseline freeze를 의미하지 않음. 기존 5V_TEST NtSide0 및 5V CAL 보호. 다음: 두 SWB 노드 이름, `n*_des.log` 마지막 35~50행, `pp*_des.cmd` Goal/Trap, 생성 PLT/TDR/SAV 확인→주입 전류 및 4QW Rrad/SRH/Auger를 동일 바이어스/전류 조건에서 비교. Gate0 낮은 J, 물리적 IQE/Full-Half 검증은 계속 미해결.

## 2026-10-10 ~23:00 KST — External GaN/MicroLED TCAD deck search and numerical speed review (OBSERVED/PROPOSED)
- User requested independent Github/other sources for full MicroLED TCAD `.cmd` / `.par` because present simulation extremely slow.
- OBSERVED: closest official Sentaurus analogue is GaN p-i-n diode in training Chapter16.8 with GaN/AlGaN/InGaN MaterialDB location and Chapter16.6 numeric settings; vendor Silvaco has Blue_GaN_uLED_10Acm-2 plot but input deck unverified public; Silvaco blue LED ledex01 (SQW) exposed as ATLAS not Sentaurus source. Nature Communications 2023 Baek explicitly disclaims code public availability. Inspected external Sentaurus repositories fenning solar cells, Alisama silicon MOSFET (`*.cmd`/`*.par`), ananthakrishnan photodiode, sai1999gaurav PN; none verified as ready-to-run III-nitride 4MQW microLED with sidewall trap. Public teammate repository only has source/README.md; not independent.
- PROPOSED only: audit latest actual CAL `pp2_des.cmd/par` for solve ramp, numerical precision and nonlinear cutbacks; note stale published source Transient MaxStep=1e-3s imposes >=1000 accepted steps over 1s if used, PLUS high-bias rejected attempts, but this is not yet verified as CAL active setting. No code/run modified, do not stop 100ns CAL. Existing low-J Gate0 stays unresolved.
- Detailed source links and caveats: CMP/reviews/EXTERNAL_GAN_MICROLED_TCAD_SOURCES_2026-10-10.md.

## 2026-10-10 ~22:39 KST — Follow-up F-ion implanted MicroLED paper retrieval (OBSERVED literature; no code changes)
- Retrieved official ACS Photonics Yuzhu Pan et al. 2026 DOI 10.1021/acsphotonics.5c02363: F- implanted high-resistivity **p-GaN passivation ring** surrounds active areas and steers current from damaged mesa sides in 6/8/10um blue MicroLED arrays.
- Also retrieved Jinyu Ye et al., Journal of Luminescence 2023 DOI 10.1016/j.jlumin.2023.119903: F- implant into p-GaN for pixel isolation, energy/dose dependent lateral spread.
- Crucial distinction: Hsu et al. Next Nanotechnology 2025 DOI 10.1016/j.nxnano.2024.100101 uses **As**, not F, after ICP-RIE sidewall etching. Project A Carbon upper-n-GaN mechanism remains proposed; papers cannot be substituted for a direct Carbon MicroLED verification. Project plan literature appendix updated; no running jobs/files modified.

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
