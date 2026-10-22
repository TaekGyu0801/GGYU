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
