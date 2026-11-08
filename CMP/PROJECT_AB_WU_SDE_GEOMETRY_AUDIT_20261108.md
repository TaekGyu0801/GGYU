# Read-only source and geometry compatibility audit for proposed Wu10um Project A/B
Date 2026-11-08 KST | Worker 주수빈 | Evidence status: **HISTORICAL SCHOOL OUTPUTS RECHECKED, LIVE SCHOOL FILES NOT DIRECTLY ACCESSIBLE**

## What was actually accessed
- Connected GitHub `TaekGyu0801/GGYU` files `CMP/CURRENT_STATUS.md`, `CMP/.ai-sync/LIVE_STATE.md`, `CMP/members/JuSubin/TIMELINE.md`, `CMP/WORKING_BASELINE_WU2023.md`, `CMP/PROJECT_AB_LITERATURE_PARAMETERS_REVIEW_20261108.md`.
- Exact paths attempted `CMP/tcad/CURRENT/sde_dvs.cmd`, `CMP/tcad/CURRENT/pp1_dvs.cmd`, `CMP/tcad/CMP_WU_Copy/sde_dvs.cmd`: **404 NOT_FOUND**. GitHub code search returned no school-copy source file. GitHub repository `CMP/tcad/CURRENT` exists as directory, but GitHub connector `fetch_file` cannot list directories; that is **not** a direct current school deck.
- Browser tabs only ordinary remote desktop session page, no direct access to remote school shell/files in available actions. Therefore **not verified live/latest school sde_dvs.cmd / pp1_dvs.cmd or actual mesh**; do not claim current live consistency. The following are retained archive read-outs explicitly reported from user's actual school shell earlier.

## Archived school pp1_dvs.cmd/meshes, evidenced previously
- Actual school `CMP_WU_Copy/pp1_dvs.cmd` user previously pasted lines 1–140 (record in `CMP/CURRENT_STATUS.md`): Wm10.0um, Wdmg .005um each lateral edge, tP .120um, tEBL0, tQB .008um, tQW .003um, four In0.08 QWs, five barriers, tN3.900um. x is vertical, y lateral. Parent x stack: pGaN0-.120; B0 .120-.128; QW1 .128-.131; B1 .131-.139; QW2 .139-.142; B2 .142-.150; QW3 .150-.153; B3 .153-.161; QW4 .161-.164; B4 .164-.172; nGaN .172-4.072; full y0..10um. Xend=4.072um. Source geometry provenance is historic prior user output, **not new live read**.
- Observed `n21/n25` Grid references `n1_msh.tdr`. `n25` SVisual directly showed `DmgL_QW1`, `DmgR_QW1`, `Clean_QW1`, `DmgL_QW4`, `DmgR_QW4`, `Clean_QW4`, `DmgL_Barrier4`, `DmgR_Barrier4`; selected sidewall QWs Trap 1e18cm^-3 when ON, central QWs 0. Mesh exists and SDevice reached 5 V, but **does not prove adequate refinement for NEW carbon/AlGaN interfaces**.
- Earlier historical comments mention `DmgL|Clean|DmgR` region family; full current school source region-name enumeration needed. Some Region families like `DmgL_nGaN` or `Clean_nGaN` are *plausible* but not newly verified from source in this audit.

## Compatibility of proposed geometry (PROPOSED, not yet user frozen)
- Project A Si-off GaN:C **inside existing n-GaN**: x=.172..372um, left y=.005..205um, right y=9.795..9.995um. This is *geometrically within* archived nGaN x=.172..4.072 and non-damage y=.005..9.995. Need to verify exact region composition, dopant parameter scope and maintain mesh/contacts, ensure no host/damage boundary overlap.
- Project B internal lateral Al0.15Ga0.85N material-replacement guard: x=.120..172um, left y=.005..025um, right y=9.975..9.995um. This crosses B0..B4 and QW1..QW4 but leaves original 5nm Dmg strips. On archived 10um stripe, two 20nm edges remove 40nm of **InGaN lateral width** from each QW, around 0.4% of original active QW projected width. Material substitution *will add new InGaN/AlGaN, GaN/AlGaN and horizontal boundaries* and require new local mesh/material interpolation/polarization validation; no prior mesh passes this new test.
- Source suitability depends on exact p→n X polarity and y positions. A lateral y widths separate from depth; right coordinate is 10um−.005um−width.

## Missing exact source / mesh items blocking definitive code-level review
1. School path `/user/semi/semi437/tmp/myproject/CMP_WU_Copy/sde_dvs.cmd`: check actual full source, `add-layer` and `create-rectangle` Scheme, contacts, doping, refinement/mesh functions, region naming.
2. Same dir `pp1_dvs.cmd`: effective SWB substitutions and differences vs `sde_dvs.cmd`; file timestamps/sha and region geometry. Also confirm current `n1_msh.tdr` is generated from this source.
3. Actual mesh region list / min element size near 3nm QWs / 5nm sides and intended new A/B interfaces using existing `n1_msh.tdr` and mesh log/SVisual. Existing `n1_msh.tdr` is not a Project A/B mesh.
4. No SDE, SDevice, project clone, code edit or new solver run performed.

## Single read-only school check (user can paste output or upload two files)
```bash
cd /user/semi/semi437/tmp/myproject/CMP_WU_Copy
pwd
stat -c '%n | %s bytes | %y' sde_dvs.cmd pp1_dvs.cmd n1_msh.tdr
sha256sum sde_dvs.cmd pp1_dvs.cmd
grep -nE 'Wm|Wdmg|tP|tEBL|tQB|tQW|tN|xIn|add-layer|DmgL|DmgR|Clean|nGaN|sdegeo:|sdedr:|sde:build-mesh|anode|cathode' sde_dvs.cmd pp1_dvs.cmd
```
Need **whole files**, not grep only, to verify region coordinates and mesh refinement call ordering. Review only, do not modify protected parent.
