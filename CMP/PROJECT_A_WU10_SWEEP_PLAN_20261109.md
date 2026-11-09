# Project A GaN:C 3-stage coarse-to-fine geometry sweep — 2026-11-09

Status: **PROPOSED scan plan**; user 이택규 proposed **50 nm coarse steps, 10 nm refinement near high-performance regions**. No TCAD source change, new SDE/mesh/solver run, or measured optimization result. Exact scan bounds below are **assistant suggestions**, NOT independently signed-off parameter freeze. The 2026-11-08 parent design freeze remains unchanged.

## Parent and physics
- School reference: `CMP_WU_Copy`, Wu-inspired 10 µm full lateral 2D stripe; n25 ON damaged NtSide=1e18 cm^-3, n21 OFF diagnostic. Preserve 5 nm each-side damaged semiconductor and existing sidewall trap model, contacts, polarization, n/p stack.
- Project A A1u: nGaN immediately below MQW, x from 0.172 um toward nGaN for depth d; left y from 0.005 um to 0.005 + width w; right y from 9.995 - w to 9.995 um (w,d in µm). Keep all C material within original Clean_nGaN (not damaged strips or QWs); regional local Si donor OFF.
- Fixed carbon electrical models from design freeze: CN acceptor 6e17 cm^-3 Ev+0.90 eV, CGa donor 3e17 cm^-3 Ec-0.11 eV, sigma_n/p each 1e-15 cm^2; nominal total C1e19 cm^-3 metadata only (not a third active defect). Do not mix carbon density and size scans at this stage.
- Historical reference w=d=200 nm stays a pilot center condition.

## Sequential three stages
1. **Lateral width (w) optimization:** d=200 nm fixed; assistant-proposed w in 50,100,150,200,250,300,350,400 nm, 8 points (50 nm step). Around the best coarse width, refine in 10 nm increments (example if w*=200 nm: 160,170,...,240 nm). Do not claim global optimum from boundary peak; expand scope only if justified.
2. **Vertical nGaN depth (d) optimization:** w=200 nm fixed; assistant-proposed d in 50,100,150,200,250,300,350,400 nm, 8 points. Fine 10 nm near best coarse depth; keep x-start exactly 0.172 um.
3. **Combined optimization:** choose two promising fine-scan widths and two promising fine-scan depths, test up to 2x2 combinations; inspect interactions, verify that independent 1D optima work in 2D; if their combination underperforms, select based on actual matched-current results, not assumption.

Counts under proposed ranges: coarse distinct A1u geometries 8+8-1=15 because (200,200) is shared. If each refinement visits nine points including one already present, up to 8+8=16 additional unique axial geometries. Combined 2x2 adds up to 4 more geometries. Thus 15+16+4 = **up to 35 unique A1u geometries**, excluding SDE-only tests and control runs; this is illustrative and may be reduced by overlapping points or early stopping.

## Control and evaluation
- Prior to sweep verify exact school effective SDE source and mesh, independent versioned Project A copy and 200x200 nm test. Verify geometry, material, doping, contacts and original damage strips.
- Controls: n25 parent, same-mesh A0m Si-on carbon-zero regression, and A0u Si-off carbon-zero comparator. A1u vs A0u measures carbon trap effect; A0u vs n25 measures donor-removal effect. Because meshed geometry and Si removal vary with w,d, at minimum matched A0u controls for all shortlisted/final candidate geometries and regression check; avoid claiming isolated carbon benefit from A1u vs n25 alone.
- Compare at *same absolute injected current* with conditional 2D normalized J=10 A/cm² first, 5 V secondary. Evaluation: absolute all-QW RadiativeRecombination integral, net sidewall trap pair loss counted once (avoid eGap+hGap double count), conventional SRH/Auger, terminal Vf, current distribution, mesh stability. Current suppression by itself is not proof of better IQE. Do not proclaim numeric optical gains until real runs.
- Scanning a 10 nm geometry feature requires mesh checks near the interfaces; adjust local refinement before judging small differences.
- No code/solver execution or performance outcome as of this plan entry.

Source: user conversation 2026-11-09, CMP/PROJECT_AB_WU10_DESIGN_FREEZE_20261108.md.