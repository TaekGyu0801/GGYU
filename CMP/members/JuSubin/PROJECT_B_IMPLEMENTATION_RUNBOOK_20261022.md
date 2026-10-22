## 2026-10-22 — JuSubin Project B Bspan 0/1/3 node matrix screenshot and RUN reported (USER OBSERVED/REPORTED; COMPLETION UNVERIFIED)
- User SWB screenshot header: `/user/semi/semi437/CMP_B0/CMP_BASELINE_2.0.0_V2` (separate visible path from older root `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`; protect parent). User states already cloned, split and running Bspan=1/3; no proof of individual terminal solve success, so mark SWB setup OBSERVED and simulation launch USER-REPORTED.
- Screenshot shows one copied SWB project with 3 Bspan groups: `Bspan=0` SDE n1, SDevice Trap OFF n2 (NtSide=0), ON n6 (NtSide=1e18); `Bspan=1` SDE n17, OFF n24, ON n30; `Bspan=3` SDE n31, OFF n38, ON n44. `Wedge=0.1`, `PolAct=0.5`, `NCedge=0`, `V1=2.0`, `Vmax=3.6`, `NPlot=8` appear shared. Color cells in screenshot do NOT prove every run done; n31 SDE appears not yellow done; must verify actual preprocessed `pp17_dvs.cmd`, `pp31_dvs.cmd`, timestamp of `n17_msh.tdr`, `n31_msh.tdr`, and final SDevice logs n24/n30/n38/n44.
- **No source modification indicated/needed at first pass:** observed SDE in-Bspan? mapping prewires 1 & 3 lateral AlGaN replacements; SDevice AlGaN/GaN and AlGaN/InGaN Thermionic blocks and polarization already present. Don't edit protected original or copied *generated* pp*. If error occurs use actual log and minimal justified change in copied user project only. Do not launch duplicate RUN before inspecting jobs.
- NEXT: in screenshot-specific copied project folder read-only inventory + grep SDE parameter substitutions and n24/30/38/44 logs. Ensure Bspan1 and 3 use new meshes, verify region material/xMoleFraction/5nm Dmg and contacts. Once completed, current and matched-current QW/sidewall recombination analysis. Unresolved baseline physical freeze/2D current normalization and QW4 issue remain; result not publication-confirmed.

# Project B fast pilot implementation — 2026-10-22

Worker: **주수빈**. AI: ChatGPT.
Status: **USER-AUTHORIZED PROVISIONAL IMPLEMENTATION PLAN (PROPOSED/NOT RUN)**. User requested to operationally **assume** baseline frozen to advance Project B immediately. This is a schedule/engineering assumption, **NOT proof that Common Baseline freeze, current units, Full/Half validity, or QW4 physical audit passed**. Thus this is a provisional research pilot only; no definitive publication-grade claim.

## Immutable parent
School SWB parent project: `/user/semi/semi437/CMP_BASELINE_2.0.0_V2`.
Source-of-truth before edits: actual school-server SDE/SDevice and parameters, not stale public GitHub CURRENT.
Do **not** modify original SWB parent or its live output files.

## New project identity and source provenance
- Candidate new SWB project: `CMP_PROJECTB_1.0.0_ALBARRIER` (check name does not exist on school server; no recreation of existing output).
- In SWB, open parent `CMP_BASELINE_2.0.0_V2`, perform **File → Save As** to the new independent project name. Confirm the **new project** is active before parameter editing. Use the SWB parameter table for `Bspan` to preserve source macros and node graph.
- Record source project path, date, new project folder, hashes of user/private `sde_dvs.cmd`, `sdevice_des.cmd`, `sdevice.par` where present, and baseline job/run IDs. Do not publish proprietary source or generated TDR/PLT to public GitHub.
- Existing `sde_dvs.cmd` has `(define Bspan @Bspan@)`; the baseline preprocessed `pp1_dvs.cmd` has Bspan=0.
- In **new SWB only** set `Bspan=3` (first candidate), leave `Wedge=0.1um`, `xAlB=0.15`, `Wdmg=0.005um` and all other epitaxy/mesh/contact/doping/traps/physics/solvers identical. `xAlB` is a literal in SDE source in the original V2.1 case, not an SWB parameter; do not add an SWB parameter for it blindly.
- The prewired `in-Bspan?` logic in actually observed SDE maps 3 to QW1..QW4 + B0..B4 Edge regions; Clean and 5nm Dmg host materials remain original. This is host-semiconductor QW-edge material replacement, **not external coating**.
- Existing `Bspan=0` Trap ON baseline remains reference. Keep same `NtSide=1e18 cm^-3` trap branch as reference (historically node n6, but **check actual new-project split/node IDs**, never infer from copied files). Keep OFF control only if/when helpful, not in place of ON reference.

## Execution — shortest defensible path
1. **Save As** original SWB → new versioned project, visually check new path/name and SWB parameter table.
2. Change ONLY `Bspan=3` in new SWB; save. No direct edit of generated `pp1_dvs.cmd`, which SWB regenerates. Do not manually edit `n1_msh.tdr`, `pp2_des.par`, `pp6_des.par` or copied old outputs.
3. Run **SDE geometry/mesh node only**; if it fails, stop and capture SDE console and mesh log. Check new run completion and actual NEW mesh timestamp; ignore stale outputs copied by Save As.
4. In new project folder run read-only:
   ```bash
   pwd
   grep -nE 'define (Bspan|Wedge|xAlB|Wdmg)' pp1_dvs.cmd
   stat -c '%y %s %n' n1_msh.tdr
   ```
   Confirm Bspan 3, Wedge .1, xAlB .15, Wdmg .005 and actual new mesh. Compare timestamps against new SDE run.
5. Open **new-project** mesh TDR in SVisual/SDE. Validate AlGaN material in `Edge_QW1...4`, `Edge_B0..4`; Dmg_QW remain InGaN and width .005um; Clean_QW remain InGaN; sidewall at same coordinates; contacts unchanged. Validate mesh near 3nm QWs/new heterointerfaces and check mesh log; **do not infer region material from matching Scheme source alone**.
6. If passes, run only one **Trap ON Project B SDevice node** (use actual SWB parameter split: `NtSide=1e18`, previously n6 but might renumber). Keep same ramp/endpoint `3.6V`, no premature 5V sweep. Confirm new preprocessed SDevice cmd/par retain `Piezoelectric_Polarization(strain activation=0.5)`, three `Thermionic` interfaces with Formula1, equivalent contacts, defects, solver and material params. If SDevice errors/non-convergence, do not silently vary baseline physics. Capture `n*_des.log` and fail signature.
7. Report concrete result (not guaranteed on the day): completion status, mesh timestamp, 3.6 V current/convergence, AlGaN xMoleFraction/ConductionBandEnergy/ValenceBandEnergy lateral cutline, current density/charge balance, QW region Radiative/SRH/Auger, trap region recombination; compare with Bspan0 control at same (once normalized) current. Derive efficiency proxy with consistent ROIs and track QW Edge InGaN replacement (~5% of 2um lateral QW).

## Important scope/physics caveats
- `xAlB=0.15` with param block AlGaN Eg0=3.7564eV, Chi0=3.8768eV at Tpar300K; verify composition dependence in *actual SDevice interpolation*, do not do arbitrary xAlB sweeps using frozen Eg0/Chi0 without validity check.
- Nominal Anderson-electron-affinity offsets: GaN→AlGaN electron0.2232eV/hole0.0956eV; InGaN→AlGaN electron0.6297eV/hole0.2698eV. These are theoretical **zero-potential estimates**; not run bias/polarization or observed sidewall barrier heights.
- Previous n2/n6 3.6V 2D I/J calibration and Full/Half gate are unresolved. Final paper-grade A/B claims remain gated on baseline verification and same-current analysis. Engineering pilot under user-approved assumption may still proceed on isolated clone.
- `Bspan=3` could introduce additional material interfaces / strain / polarization effects, and changes QW-edge emission volume; a positive modeled IQE fraction alone is not proof of sidewall loss mitigation.
- Avoid killing/cleaning source-project processes, reusing stale results, or copying proprietary TCAD files to public GitHub.

## Status/next
State as of writing: **No user-reported SWB clone, Bspan3 preprocess, SDE mesh, or Project B device run yet.** Actual execution must be verified from user server outputs before marking OBSERVED.
First instruction to user: SWB `File -> Save As` as above; set new-project `Bspan=3`; run SDE node only; report new-path and preprocessed Bspan values/mesh log.
