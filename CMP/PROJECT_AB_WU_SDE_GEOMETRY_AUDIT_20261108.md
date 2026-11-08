## 2026-11-08 RECOVERY ADDENDUM — GitHub candidate SDE **FOUND** after full Git tree scan (supersedes missing-candidate inference below)
- User at home asked to locate previously uploaded materials instead of school access. **FULL GITHUB TREE REST query** `GET /repos/TaekGyu0801/GGYU/git/trees/main?recursive=1` returned 124 entries, `truncated=false`, **only branch main**. It revealed the relevant historical source candidate which the initial filename search and limited path guesses missed:
  - `CMP/tcad/candidates/CMP_BASELINE_3.2.0_WU2023PHY/sde_dvs.cmd` (actual 5,123 UTF8 characters, fetched/READ in full): https://github.com/TaekGyu0801/GGYU/blob/main/CMP/tcad/candidates/CMP_BASELINE_3.2.0_WU2023PHY/sde_dvs.cmd
  - Same directory `sdevice_des.cmd`, `sdevice.par`, `README.md`, `svisual1_iv.tcl` all actually exist.
  - Older `CMP/tcad/candidates/CMP_BASELINE_3.0.0_WU10FULL/sde_dvs.cmd` exists but differs in active Mg assumption and Si field naming; 3.2 more closely matches school later post-Mg Wu generation.
  - `CMP/tcad/CURRENT` has ONLY `sdevice2_defect_on.cmd`, `svisual1_iv.tcl`, `svisual2_maps.tcl`; no Wu sde source.
  - **No** `CMP_WU_Copy` school live `sde_dvs.cmd`, generated `pp1_dvs.cmd`, `n1_msh.tdr` or mesh output anywhere in entire GitHub main tree. File_search over directly uploaded files this conversation also did not find those exact attached files; older chat transcripts have *excerpts* only. School live exact SHA/timestamp still unverified.
- **High-confidence candidate geometry:** `(define Wm 10.0)`, `Wdmg .005`, `tP .120`, `tEBL 0`, `tQB .008`, `tQW .003`, `tN 3.900`, `xIn .08`, `PMgActive 2e19`, `ND 5e18`, `NBg 1e15`. These coincide with archived actual school effective pp1 source observations. `seg-list` defines `DmgL Y[0,.005]`, `Clean Y[.005,9.995]`, `DmgR Y[9.995,10]`; `add-layer` loops 11 active semiconductor layers to create **33** `<segment>_<layer>` rectangles. **No EBL region** because tEBL0.
- Existing exact candidate names: `Clean_nGaN` and `DmgL_nGaN`/`DmgR_nGaN`, `Clean_QW1..4`, `Clean_Barrier0..4`, `DmgL/DmgR_QW1..4`, `DmgL/DmgR_Barrier0..4`, `Clean_pGaN` and damaged pGaN segments. Explicit 22 damaged-region trap declarations in companion SDevice correspond to 11 ×2 sides. This is **source candidate evidence**, with sampled region names previously seen from real school SVisual TDR.
- Candidate coordinates: x0-.120 pGaN; QB+QW x.120-.172; nGaN x.172..4.072. Pilot A x.172-.372 and Y [.005,.205], [9.795,9.995] is **inside `Clean_nGaN`**; B x.120-.172 and y [.005,.025], [9.975,9.995] falls inside **`Clean_QW1..4` and `Clean_Barrier0..4`**. Neither carbon nor AlGaN guard has an existing named region; both require controlled new segmentation in independently cloned SDE.
- **Actual candidate mesh declarations RECOVERED:** `Ref.All` `(.20,.35,.010,.020)µm` (max x200nm/y350nm; min x10nm/y20nm); `Ref.MQW` `(.0020,.15,.0004,.010)µm` (max x2nm/y150nm; min x0.4nm/y10nm) on x[.120,.172], all lateral; `Ref.Edge` `(.020,.0010,.002,.0005)µm` (max x20nm/y1nm; min x2nm/y0.5nm) ONLY Y[0,.005], [9.995,10]. This existing mesh prescription does **NOT** guarantee resolution of proposed inner 20nm AlGaN at y.005-.025 (outside `Ref.Edge`) or A carbon/Si-off interface at y.205 and x.372 (outside `Win.MQW`). Add refinement explicitly in isolated clones, check actual mesh statistics; no new mesh built here.
- Candidate `sde_dvs.cmd` sets full-width ideal planar top anode x0/bottom cathode x4.072 via three lateral partitions, not actual Wu patterned contact. `nSiliconActiveConcentration` for GaN n/base and barriers, MgActive for pGaN. Real school's final `datexcodes.txt` and effective SDevice may be local modifications not archived. 
- **CORRECTION:** initial audit below states relevant source unavailable; the **GitHub 3.2 candidate is AVAILABLE and closely aligned** but actual school `CMP_WU_Copy/sde_dvs.cmd` / generated `pp1_dvs.cmd` still not archived or current-accessible. Treat recovered code as **design reference**, not byte-identical, not final production source. No code modification or school execution performed.

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
