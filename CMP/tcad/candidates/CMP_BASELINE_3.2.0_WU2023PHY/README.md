# CMP_BASELINE_3.2.0_WU2023PHY

**PROPOSED / NOT EXECUTED OR VALIDATED ON THE SCHOOL'S SENTaurus T-2022.03.**

Source: Wu et al. (2023), *Physical mechanisms on the size-effect in GaN-based Micro-LEDs*, Micro and Nanostructures 177:207542, DOI https://doi.org/10.1016/j.micrna.2023.207542

**Lineage:** copied and revised ONLY from `CMP_BASELINE_3.0.0_WU10FULL`. Parent and school `CMP_WU` n21/n25 output are untouched. Never confuse with other 2026 Wu paper or import CMP4/Kou epitaxy.

## Provenance
- PAPER: 10um device lateral, nGaN 3.9um / Si 5e18 cm^-3; four In0.08GaN 3nm wells, GaN barriers 8nm; pGaN Mg nominal 2e19 cm^-3; 5nm acceptor-like trap-host semiconductor strips on both sidewalls; piezoelectric polarization, Mg incomplete ionization, field-related trapping, Radiative/SRH/Auger.
- NEW modeling: `MagnesiumActiveConcentration=2e19` is ASSUMED to represent substitutional Mg prior to incomplete ionization. Wu reports Mg nominal, not a measured activated concentration or free-hole density. Official III-N example suggests `IncompleteIonization(Dopants="MagnesiumActiveConcentration")`, Mg `E_0=0.15 eV`, degeneracy 4. **These ionization constants are NOT Wu's reported values**. Verify runtime doping mapping!
- NEW modeling: `nSiliconActiveConcentration` species instead of generic SiliconActive; verify installed `datexcodes.txt`, TDR DonorConcentration and eDensity. The species mapping is a potentially breaking input change.
- NEW modeling: polarization full ON with crystal c-axis assumed -device x via `LatticeParameters` in par; confirm polarity / interface polarization actually generated. No `PolAct` SWB variable for this candidate.
- NEW modeling: Fermi-consistent `Thermionic` interfacial boundary condition for QW heterointerfaces (proposed, not explicitly Wu verified); `PooleFrenkel` trap cross section response as a PROXY for local field-related trapping (not necessarily Wu exact formula), `epsPF=9.5` provisional. Test against control later.
- UNVERIFIED PILOTS retained: p-GaN 120nm, EBL 0nm (Wu EBL presence/absence not established from available text), 5 GaN QB with 4 QWs, barrier background n=1e15, full-width top/bottom ideal Ohmic electrodes, trap depth `TrapEt=0.75` above Ev, `TrapSigmaN=TrapSigmaP=1e-15`, default material B/C/mobility/quantum transport. **No source-backed claim of exact Wu replica is justified.**
- 10um Cartesian stripe `J=|I|1e8/10` conditional on raw output unit A/um & `AreaFactor=1`, not a real 10x10um² pixel.
 
## SWB setup
Create **new** independent project `CMP_BASELINE_3.2.0_WU2023PHY`. Paste `sde_dvs.cmd` into SDE. Paste `sdevice_des.cmd` into SDevice tool command. Paste `sdevice.par` into the corresponding **SDevice parameter editor** so `@parameter@` maps to real `pp*_des.par`; verify after preprocess. Paste `svisual1_iv.tcl` into SVisual1.

Define SDevice parameter columns: `NtSide` (0 then 1e18), `Vstop` (0.1 syntax smoke then 5 only after inspection), `TrapEt=0.75`, `TrapSigmaN=1e-15`, `TrapSigmaP=1e-15`. **Remove inherited `PolAct` variable from this SWB candidate**; physics no longer references it.

## Explicit mandatory gates (none passed)
0. SDE preprocess/build mesh: verify region count 3 lateral segments x 11 vertical host layers = 33, layer widths/QW composition/5nm edges, contact attachment, donor and acceptor maps. Count note: pGaN1 + QB5 + QW4 + nGaN1 = 11 layers.
1. SDevice preprocess: inspect `pp*_des.cmd`, `pp*_des.par` for `LatticeParameters`, `Ionization`, `Thermionic`, `PooleFrenkel` and substituted parameter values; confirm `nSiliconActiveConcentration` and `MagnesiumActiveConcentration` are recognized by `datexcodes.txt`. Verify GaN/InGaN default material model warnings and real field orientation. STOP if pGaN `AcceptorConcentration` missing/zero.
2. Clean (NtSide=0) 0.1V smoke only to check parse, then 5V operating bias. Inspect eDensity, hDensity, BandEnergy, quasi-Fermi, e/h current density and QW1–QW4 radiative/SRH and actual terminal current. If near-zero current persists, diagnose doping/contact/heterointerface rather than modifying trap. Solver convergence alone NOT validation.
3. After clean LED behaves physically, use identical geometry/physics with NtSide=1e18; verify matching-current QW recombination and sidewall depletion, not just ratio of tiny terminal currents. Assess PooleFrenkel vs constant-cross-section control separately.
4. To claim Wu fidelity obtain Wu Fig.1 full stack/electrode geometry, full trap energy/density/cross-sections, field-trapping equation, p-GaN thickness/EBL status and MaterialDB/quantum details. Until then REPRODUCTION UNVERIFIED.

**No school code or run was changed here.** Prior n21 clean 5V raw I=3.025e-29 and n25 ON5V raw I=5.810e-19 are old geometry results and MUST NOT be relabeled as this candidate.

Refs: https://www.sciencedirect.com/science/article/abs/pii/S2773012323000390 ; https://ghzphy.github.io/Sentaurus_Training/sd/sd_16.html ; https://tcad.deartek.com/sentaurus/sd/sd_13.html ; CMP/references/TCAD_REFERENCE_INDEX.md.
