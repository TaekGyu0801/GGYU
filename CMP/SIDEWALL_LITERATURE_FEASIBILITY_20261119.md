# CMP sidewall-defect mitigation literature and easy TCAD proposals — 2026-11-19
Worker: 주수빈. Status: PROPOSED RESEARCH REVIEW ONLY; user has NOT selected to replace F-inspired Project F yet; no school code edited or simulation run.

## Primary literature and direct transfer constraints
1. Zhu et al., Improved Optical and Electrical Characteristics of GaN-Based Micro-LEDs by Optimized Sidewall Passivation, Micromachines 14,10 (2023), DOI 10.3390/mi14010010: KOH/H3PO4/SiO2 passivation; optimized device IQE 85.4%, -5V reverse leakage ~1e-13 A. Does not establish numerical trap concentration after passivation.
2. Ultra-high brightness Micro-LEDs with wafer-scale uniform GaN-on-silicon epilayers, Light Sci Appl (2024), DOI 10.1038/s41377-024-01639-3: KOH + ALD-Al2O3 and HRTEM evidence covering MQW sidewall.
3. Sidewall Interface Nitrogen Treatment for Improving GaN-Based Micron-Scale Light-Emitting Diode Efficiency, ACS Appl Electron Mater 6,8277-8285 (2024), DOI 10.1021/acsaelm.4c01540: N2 plasma at 250°C; 4x4um2 LED optical power +97.29% at J25 A/cm2, studies pGaN and MQW interfaces; not a TCAD trap-density calibration.
4. Interplay of sidewall damage and light extraction efficiency of micro-LEDs, Opt Lett 47,2250-2253 (2022), DOI 10.1364/OL.456993: TMAH treatment ~4x reduced nonradiative surface recombination estimated; this does NOT mean a 4x reduction in trap density.
5. Role of Sidewall Conditions in the External Quantum Efficiency of InGaN-Based Micro-LEDs, Phys Status Solidi RRL (2025), DOI 10.1002/pssr.202500042: 10nm ALD-Al2O3 vs 1nm shows low-J EQE variation; cannot directly map to fixed volumetric trap density.
6. Wu et al. Physical mechanisms on the size-effect in GaN-based Micro-LEDs (2023), DOI 10.1016/j.micrna.2023.207542: current working Baseline publication already sweeps sidewall trap density and size => all-sidewall global Nt sweep is redundant research.
7. Lee et al., Mitigating sidewall damage effects in GaN-based multi-quantum-well micro-LEDs prepared by top–down fabrication (2026), DOI 10.1088/1361-6463/ae553e: review of TMAH, sulfur, plasma, ALD and damage length scale, cautions 5nm pilot damaged zone is simplified.

## Relative implementation effort
A. Global sidewall partial passivation: lowest effort, change only SWB NtSide from nominal 1e18 to pilot 1e17 cm^-3; no mesh/SDevice edits, but already covered by Wu and baseline Trap ON/OFF checks.
B. MQW-selective partial passivation (preferred smallest nontrivial experiment): keep original baseline mesh, contacts, pGaN/nGaN/doping/physics and all 5nm damaged host regions. Independently clone school-verified SDevice, alter ONLY the 8 DmgL_QW1..4 and DmgR_QW1..4 region trap Conc from original 1e18 to proposed pilot 1e17 cm^-3; leave other 14 Dmg trap regions at 1e18, TrapEt .75, sigmaN/P 1e-15. Candidate is hypothetical region-specific trap suppression, not a verified selective ALD/N2/TMAH process or calibrated trap concentration. Actual school deck must be checked before code patch.
C. Damage width shrink (5nm to 2nm): SDE geometry + remesh, changes integrated trap count and active width; more effort and confounding.
D. Selective pGaN high-R ring: SDE split/doping/mesh and preprocessed checks, more effort than trap-only, previously USER-SELECTED F-inspired idea but school UNRUN.
E. Explicit dielectric sidewall layer or F implant dose: high effort, new interfaces/charge/process calibration.

## Minimal diagnostic before claims
Check SWB PP effective conditions / AreaFactor, 5V Curve trace finished, local net eGapStates/SRH vs same-current absolute all-QW radiative and forward-voltage penalty. Raw 5V baseline Trap OFF last current ~2.569e-3 vs ON ~2.566e-3 in historical school records; only 0.12% difference under provisional comparable conditions, so even easier trap repair may show almost no measurable 5V benefit. Low-current response may be more sensitive. Do NOT equate leakage/current reduction to IQE or optical output improvement, and do NOT claim experimental F/ALD/N2 passivation reproduced.
Existing Project F plan stays unchanged until user explicitly chooses an alternative.
