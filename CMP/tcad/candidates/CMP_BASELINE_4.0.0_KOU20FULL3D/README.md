# CMP_BASELINE_4.0.0_KOU20FULL3D — 20 µm Kou geometry candidate

**PROPOSED CODE / NOT RUN.** The previous `CMP_BASELINE_3.1.0_KOU4FULL` was a mistaken paper-reproduction candidate using the CMP 4 µm goal instead of Kou's published 20 µm chip. Preserve the earlier files as separate CMP-sized exploratory code; do not run them as Kou-paper baseline.

## Reference
Kou et al., *Impact of the surface recombination on InGaN/GaN-based blue micro-light emitting diodes*, Opt. Express 27 A643–A653 (2019), DOI https://doi.org/10.1364/OE.27.00A643, Section 2 / Fig. 1.

## Published inputs implemented geometrically
- Paper chip sizes 20×20, 60×60, 100×100 µm². Implement smallest **20×20 µm²** for LED III (clean) and LED C (damaged).
- 4 µm damaged border on all **four** sides (NOT 5 nm), leaving 12×12 µm² clean planar core = **36%** usable area. Therefore SDE uses **full 3D**, not a 2D stripe whose clean fraction would be 60%.
- nGaN 4 µm, Si 5e18 cm^-3, 4 In0.15Ga0.85N QWs each 3 nm, GaN barriers 22 nm, pAl0.15Ga0.85N EBL 26 nm, pGaN cap 120 nm, heavily doped pGaN cap 20 nm. Paper specifies pGaN/EBL **hole concentration** 3e17 cm^-3 rather than actual Mg doping input.
- Code assumes **five GaN barriers** for four wells; paper text does not explicitly enumerate barrier count or exact sequence. Resulting modeled total vertical stack thickness **4.288 µm**. Confirm Fig. 1 stack before claiming exact reproduction.

## Explicit pilot assumptions — NOT Kou data
- `pActiveApprox=3e17` MgActive as proxy for 3e17 hole concentration (not physically identical), and top `pPlusPilot=1e19` MgActive since paper does not specify contact-region heavy doping numerically.
- Full top/bottom Ohmic contacts are provisional and **not** Kou's contact footprint (Fig. 7 shows a 4 µm p-contact). Electrode placement/n-side shelf not reproduced.
- No material DB calibration or polarization, 70:30 heteroband offset, SRH, Auger, quantum/Schrodinger solution, or two-species trap model; APSYS paper ≠ Sentaurus.
- Text for Kou hole trap energy internally inconsistent between '0.6 eV above VB' and 'Ev+0.46 eV'; do not assume either until checked. Kou surface-defect recombination not implemented just by marking the 4 µm border.
- **Do not reuse** `CMP_BASELINE_3.1.0_KOU4FULL/sdevice_des.cmd`: incompatible region names and physical specifications. New 3D SDevice follows a verified SDE mesh.

## SDE-only validation gate
1. Create separate SWB project `CMP_BASELINE_4.0.0_KOU20FULL3D`; check server project-name availability.
2. Use only `sde_dvs.cmd` as SDE node input. Verify 117 geometric region cuboids, in-plane clean area 12×12 and damage ring, 3 nm wells, p+ and EBL, two contacts, and `pp1_dvs.cmd`/mesh logs. Actual Sentaurus parser not tested.
3. 3D 20×20 µm² with 3 nm QWs could produce a very large mesh. Inspect memory, element count and mesh minimum angle before launching SDevice. Do not claim successful simulator run.
4. Verify contacts and Mg interpretation against paper/UG, write a **new Kou-specific SDevice** with separate clean and damaged trap cases, then compare at matched 20 A/cm² after validating 3D current normalization. Legacy protected CMP common baseline and Wu candidate unchanged.
