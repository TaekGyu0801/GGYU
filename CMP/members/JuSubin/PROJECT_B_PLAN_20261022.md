## 2026-10-22 — 주수빈 Project B AlGaN material / interface parameter block read (OBSERVED; sweep model warning)
- Source: user terminal `sed -n '108,176p' pp2_des.par` at school-server `CMP_BASELINE_2.0.0_V2` (existing Bspan=0 baseline). `Material="AlGaN"`: Bandgap `Eg0=3.7564eV`, `Chi0=3.8768eV`, `alpha=1.043e-3`, `beta=925`, `Tpar=300K`; ConstantMobility `mumax=300,10`; Scharfetter `taumin=0,0`, `taumax=1e-7,1e-7`, `Nref=1e16`, `gamma=1`; Radiative `C=2e-11`; Auger `A=5e-31,5e-31`; PDopant and pMagnesium ionization species definitions, each `E_0=0.2eV`; ThermionicEmission Formula1 specified for InGaN/GaN, AlGaN/GaN, AlGaN/InGaN interfaces. User text, not project B runtime evidence.
- INTERPRETATION: `Eg0` at `Tpar=300K` is reference-temperature parameter according to older Sentaurus UG; actual polarization, band offsets (Ec/Ev), and carrier injection are NOT validated from these scalars. Doping-dependent Scharfetter lifetime reduction cannot be inferred from parameters alone without enabled recombination dependence. `xAlB=0.15` was observed in pp1_dvs.cmd previously, but this par block shows only scalar Eg0/Chi0 and no explicit mole-fraction interpolation terms; **do not sweep xAlB and assume the material bandgap/affinity follow x** without checking effective per-region material parameters and SDevice material DB/interpolation method. Prioritize x=.15 fixed for initial structural pilot and verify parameterization before Al-fraction DOE.
- NEXT READ-ONLY: `sed -n '1,85p' pp2_des.par` to view GaN/InGaN bandgap/electron affinity and determine nominal heterointerface offsets and material assumptions. Confirm actual effective Ec/Ev using SVisual *after separately versioned Project B has run*. Existing baseline untouched; Project B runs only after Baseline verified freeze.

## 2026-10-22 — JuSubin Project B SDevice material-interface model declarations observed (SERVER OUTPUT, NO B RUN)
- User provided read-only `grep -nEi 'AlGaN|Piezoelectric_Polarization|Thermionic|MoleFraction|BandOffset|Bandgap' pp2_des.cmd pp2_des.par | head -n 90` from actual server `CMP_BASELINE_2.0.0_V2`.
- OBSERVED: `pp2_des.cmd` line21 `Piezoelectric_Polarization( strain activation=0.5 )`; lines24-26 `Physics (MaterialInterface="InGaN/GaN") { Thermionic }`, `AlGaN/GaN`, `AlGaN/InGaN`. Lines59-67 requested `ConductionBandEnergy`, `ValenceBandEnergy`, `BandGap`, `ElectronAffinity`, `xMoleFraction` plot outputs. `pp2_des.par` line112 `Material = "AlGaN" { Bandgap {...}` start, lines166/169/172 `ThermionicEmission { Formula = 1 }` under relevant interface sections (verify exact headers via expanded excerpt).
- Inference limited: these are present in baseline preprocessed n2 deck with **Bspan=0**; they DO NOT confirm correctness or runtime application of newly introduced lateral AlGaN interfaces at Bspan>0, orientation-dependent polarization charge, model parameter suitability, or Project B performance.
- NEXT READ-ONLY: `sed -n '1,34p' pp2_des.cmd` and `sed -n '108,176p' pp2_des.par` to inspect effective AlGaN Bandgap, electron affinity, alloy interpolation and all Thermionic context. No code changes and no Project B simulation until verified Common Baseline freeze.

## 2026-10-22 — 주수빈 Project B actual Al mole fraction verified (OBSERVED USER TERMINAL; NO RUN)
- User ran grep on actual school-server V2.1 preprocessed SDE `pp1_dvs.cmd`. Some shell commands were concatenated (`pp1_dvs.cmdsed`) producing harmless grep No such file messages, but an independent `grep` returned actual line-number values: line32 `(define (P lat dep z) (position dep lat z))`; line39 `Wedge=0.1 um`; line42 `xIn=0.15`; line43 `xEBL=0.15`; line44 `xAlB=0.15`; line99 `MF_AlB` uses `xMoleFraction xAlB`. Existing Bspan=0 confirmed in prior `pp1_dvs.cmd` line45.
- OBSERVED design candidate means when changing Bspan to 1/2/3 in a *future cloned project*, selected 100nm-wide QW/Barrier Edge semiconductor material can become Al0.15Ga0.85N. Baseline remains Bspan=0 (no additional edge heterobarrier).
- DERIVED geometry under existing 2um Half width: Clean 1.895um, Edge 0.1um, Damage 0.005um; replacement of QW Edge InGaN by AlGaN for Bspan>0 corresponds to 5% of original lateral QW width (0.1/2.0); actual radiative volume, output IQE, carrier confinement, band profile and input equality still unverified. 5nm Damage stays host material in SDE, but carrier access can change. This change is not an exterior deposited passivation film.
- PROPOSED next gate: clone only after verified Baseline freeze; use Bspan=0 control and a single isolated Bspan candidate at xAlB=.15 Wedge=.1um, geometry/mesh and composition smoke first. Bspan3 provides the fullest uninterrupted QW+GaN barrier Edge material conversion among coded choices, but more AlGaN interfaces/injection impacts; neither mechanism nor improvement established. Need verify material parameters, potential interface polarization/strain, QW radius/effective width and trap partition. Do not execute on historical baseline.

## 2026-10-22 — JuSubin Project B material-substitution, region and mole-profile code observed (OBSERVED USER TERMINAL, NO RUN)
- 주수빈 학교 서버 실물 `CMP_BASELINE_2.0.0_V2/pp1_dvs.cmd` lines60–145 발췌: stack pCap0.020, pGaN0.120, EBL0.026, B0..B4(each0.022), QW1..4(each0.003), nMesa dEtch. base-mat: qw→InGaN, ebl→AlGaN, else→GaN.
- `in-Bspan?` is exact layer-selection logic: 1→QW1..4, 2→QW1..4+B1..B3, 3→QW1..4+B0..B4. `edge-mat` sets selected Edge layers to AlGaN. `mC=(base-mat role)`, `mE=(edge-mat name role)`, `mD=(base-mat role)`: selected Edge material changes but Clean and Dmg host material stay as baseline. `rect 0..Xe, Xe..Xd, Xd..Xs` creates all three regions at each layer; `dope-region` uses original role-based host dopant in Edge.
- `MF_AlB` constant `xMoleFraction=xAlB` in `mole-region` for AlGaN with role≠ebl; existing EBL uses separate `MF_EBL=xEBL`. **Actual numerical xAlB, xEBL, xIn and all other variables were NOT in lines60–145, still require earlier pp1_dvs.cmd header.**
- Verified geometry is in-mesa host semiconductor Edge replacement, NOT added exterior conformal sidewall coating. Existing InGaN QW Edge area becomes AlGaN, potentially changing emissive area, carrier injection, band interfaces/polarization; unchanged 5nm Dmg physical region does not mean recombination unchanged under applied bias. No performance conclusion.
- NEXT: READ-ONLY `sed -n '23,59p' pp1_dvs.cmd` plus `grep -nEi 'xAlB|xEBL|xIn|MF_AlB|define.*P' pp1_dvs.cmd` to verify active composition values and coordinate transform; no file edits, no Bspan>0 run until baseline freeze and isolated test. Bspan3 continuous MQW+all barriers is a **PROPOSED candidate**, not decided or demonstrated superior; Bspan1 limited-scope alternative.

# Project B — Localized AlGaN Lateral Heterobarrier: JuSubin Day-1 plan (2026-10-22)

- Worker: 주수빈 (ChatGPT-assisted)
- Ownership decision (user 2026-10-22): Upon Common Baseline freeze, 이택규 proceeds with Project A GaN:C and 주수빈 independently proceeds with Project B AlGaN. User specified team division; not represented as a direct message/approval from Lee.
- State: **PROPOSED, preparation started**. No new Sentaurus runs or code changes. **Baseline freeze not yet observed**.
- Shared source: GitHub TaekGyu0801/GGYU, Issue #4 (Project B) and Issue #5 (A/B comparison).
- Historical candidate project name (not yet created): `CMP_PROJECTB_1.0.0_ALBARRIER`; check actual SWB names and parent provenance before creation.

## Physical research hypothesis
Keep damage/defects and common baseline parameters unchanged while introducing a **spatially localized Al_xGa_(1-x)N lateral edge barrier** to reduce carrier access to the damaged mesa sidewall. Changes in electron and hole accessibility, lateral band profiles, polarization charge, and vertical carrier injection must be evaluated. Expected efficacy is a **testable hypothesis**, not an established outcome of simply adding AlGaN.

### Baseline constraints
- Reference for source inspection: `/user/semi/semi437/CMP_BASELINE_2.0.0_V2` active V2.1, not yet frozen production baseline.
- Existing user/server observations: planar 2um Half representing 4um mesa, 4×3nm QWs, 5nm sidewall damage; Edge/Clean/Dmg segmentation. Prior project status included `Wedge=0.1um` and `Bspan=0`, but verify active preprocessed value and definitions.
- `NtSide`, trap energy and capture cross sections, epitaxy, contacts, solver/physics and control geometry must be kept the same between B and final reference; Project B modifies only the specifically declared lateral barrier subregions and requisite interface physics.
- Baseline J uses **provisional** planar 1um effective depth; physical area scaling, contact width and Full/Half remain final acceptance gates. Numerical accounting != experimentally validated IQE.

## Today's concrete deliverables
1. **Region audit (read-only on server)**: identify where `Bspan` appears, if it actually creates a material subregion, which layers (GaN barrier, n/p GaN, EBL, QWs) it intersects, location relative to 5nm damaged sidewall and 0.1um Edge. Identify whether candidate AlGaN is inside semiconductor **before** damaged edge, and whether a vertical bypass remains. Do not overwrite source.
2. **First annotated design**: layer-by-layer table specifying region names, material baseline vs proposed B, spatial lateral/depth range, lateral junction normals, and which existing material/mesh region boundaries can be reused.
3. **Physics evidence check**: audit AlGaN composition notation, bandgap/bowing and conduction/valence offsets, spontaneous/piezo polarization at new lateral GaN/AlGaN interfaces (interface orientation matters), thermionic/transport handling, strain assumption and mesh near heterointerfaces. Review installed T-2022.03 User Guide or working project physics syntax before proposing edits.
4. **Minimal DOE proposal (not yet runs)**: baseline `Bspan=0` control; one conservative Al-containing pilot after physics check; subsequent nominal screening candidates `x_Al=0.05/0.10/0.15`, lateral width `0.05/0.10/0.20 um` are placeholders only and not verified feasibility, calibrated numbers or approved production ranges.
5. **Outputs**: match current density where properly normalized; I-V/Vf penalty; e/h density and e/h current density across edge/central QWs; Ec/Ev along lateral cutline, lateral potential/polarization; region-integrated damaged sidewall trap recombination and QW Radiative/SRH/Auger; current crowding. Use identical ROI and unmodified defect density against reference. Note QW4-heavy baseline and check against artifacts.

## Immediately executable read-only check (bash)
```bash
cd /user/semi/semi437/CMP_BASELINE_2.0.0_V2
pwd
grep -nEi 'Bspan|Wedge|Wdmg|AlGaN|Aluminum|Edge_|Dmg_|define.*(rE|rD)' sde_dvs.cmd pp1_dvs.cmd | head -n 140
```
Optional follow-up only after locating line numbers: `sed -n 'START,ENDp' sde_dvs.cmd` with the **actual** line range, plus active `pp1_dvs.cmd` processed values.

## GO/NO-GO for runs
- Today's **GO**: investigate geometry and design, prepare isolated future implementation instructions.
- **NO-GO** until explicitly verified Baseline freeze: editing existing V2.1, copying a purported final baseline with unverified provenance, changing shared material files/traps or launching long Project B sweeps.
- Upon freeze: make independently versioned Project B clone with exact parent source/hash; geometry, mesh and preprocess smoke; single split pilot vs unchanged baseline; check current continuity/band profiles; only then an Al/width DOE.
- If AlGaN creates poor hole injection/extra polarization charge or fails to reduce edge carrier density at comparable current, do not declare a sidewall improvement from a 3-channel radiative fraction alone.

## References for physics review
- CMP Issue #4 and shared AI protocol.
- Suemitsu (2026), Impact of Polarization Charges on Threshold Voltage and Band Offset in AlGaN/GaN Heterostructures, https://doi.org/10.1002/pssa.202501001 — general junction physics, **not a verified direct lateral microLED Project B process**.
- Weak polarization electric field III-N LEDs with enhanced efficiency and strong lateral carrier confinement (2026), https://pmc.ncbi.nlm.nih.gov/articles/PMC13324002/ — InGaN/AlGaN digital-alloy LED evidence, different design from proposed localized sidewall AlGaN.
- User-provided official Sentaurus T-2022.03 docs indexed in `CMP/references/TCAD_REFERENCE_INDEX.md` take precedence for syntax.
