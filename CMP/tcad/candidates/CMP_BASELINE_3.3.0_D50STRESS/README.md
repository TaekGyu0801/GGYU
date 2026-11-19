# CMP_BASELINE_3.3.0_D50STRESS — PROPOSED/UNRUN school reference

**Worker:** 주수빈 (shared D50 basis for Lee A and Ju B), 2026-11-19 KST.
**Decision:** User explicitly says implement a sidewall Damage 50nm trial. The **original successful school 5nm Wu baseline MUST remain unmodified**. This repo folder is only an independently derived example from GitHub's **unrun** `CMP_BASELINE_3.2.0_WU2023PHY`, not a verified copy of the school's actual working SDE.

## File
- `sde_dvs.cmd`: Derived from `CMP/tcad/candidates/CMP_BASELINE_3.2.0_WU2023PHY/sde_dvs.cmd`, SHA blob `965ed9f29fa4f6db4166a9707ce02d34f2422f74` at review. Exactly one physical input changed: `(define Wdmg      0.005)` to `(define Wdmg      0.050)` in µm. All other executable lines kept byte-equivalent; header and mesh-comment text updated to label the 50nm hypothesis and no-run status.
- `seg-list` computes bilateral `DmgL` as y0..0.05, `Clean` y0.05..9.95, `DmgR` y9.95..10um across all 11 included layers (33 regions), conditional on unchanged original layer list.
- `Win.EdgeL/Win.EdgeR` reference `Wdmg` dynamically; the original fine `Ref.Edge` mesh (maxX .020, maxY .001, minX .002, minY .0005, all um) was **left unchanged initially**, which makes the 50nm edge mesh much larger than the 5nm model. Inspect `n*_msh.tdr` mesh node counts and SVisual edge/QW triangles **BEFORE** SDevice. Don't run 12 nodes or loosen MQW mesh indiscriminately.
- Contact positioning in this candidate uses midpoints from `seg-list`; school code may use hard-coded coordinates and MUST be audited independently.
- Only SDE is included here. The active school baseline `sdevice_des.cmd`, `sdevice.par` and exact SWB settings should be **copied unchanged into the private independent D50 project**, not recreated from a GitHub unrun template. Do not commit proprietary school codes or logs to public repo.

## Preserved physics and comparisons
- Planned 10µm 2D stripe, pGaN120nm, EBL0 pilot, four InGaN3nm QWs, five GaN8nm QB, nGaN3.9µm, p Mg2e19 and n Si5e18cm^-3; no design change other than Dmg width. Always defer to actual school parent for resolved dimensions.
- Baseline Trap ON nominal NtSide=1e18cm^-3, Et=Ev+0.75eV, electron/hole capture sigma1e-15cm²; all 22 region traps preserved by name. D50 y0..0.05 and9.95..10 plus unchanged original trap concentration makes nominal areal trap inventory increase 10x over D5; NOT a pure damaged-depth-only comparison. D50 NtSide1e17 would preserve 5nm model's nominal sheet inventory but is a different experiment and **not** the initial run.
- Existing Wu D5 reference is preserved. For fair A/B D50 test, run **D50 baseline first**, then A-D50 pGaN Mg edge-deactivation and B-D50 QB8->6nm, each compared with D50 at matched total injected current. Missing D50 reference invalidates attributing A/B effects.

## Required school checks
1. Locate actual successful school Wu baseline and its source. Read-only grep for `Wdmg`, `0.005`, `9.995`, `DmgL`, `DmgR`, `Win.Edge`, `Ref.Edge`, `set-contact`, plus any `CurrentPlot` explicitly naming Dmg regions.
2. Clone into separate SWB project named under `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>` with a new unused name; do not replace working baseline. Apply the **single** Wdmg change to the school copy **only if its functions/mesh/contact are actually parameterized identically**. If not, patch each hard-coded location in the clone after seeing complete school SDE.
3. SDE preprocess/build mesh; audit region counts, no overlaps, dopants, surface contacts, 3nm QWs, 50nm damage, near-interface mesh, node count, PP macro/grid paths.
4. Run **one** D50 Trap ON SDevice node Vstop5, ensure final log anode5.000E+00 AND `Finished, because... Curve trace finished`. No school run has occurred in this ChatGPT turn.
5. Compare D50 vs original D5 as separate damage sensitivity; for A/B conclusions compare each new A-D50/B-D50 to D50 at same total current, same normalized area; examine absolute QW radiative and net sidewall trap losses, never 5V current alone.

**Status:** GitHub reference code was created and static checked; school source and numerical correctness still UNRESOLVED.
