# 주수빈 — Common Baseline clean-sheet redesign proposal (2026-11-03)

**Status: USER-PROPOSED / DESIGN REVIEW ONLY. NOT YET APPROVED AS TEAM BASELINE. NO NEW SDE/SDevice CODE, SERVER RUN, OR SIMULATION RESULT.**

## User direction and provenance
- 2026-11-03 주수빈: existing Baseline code and construction may not serve the CMP research purpose; intends to create **new code from first principles aligned to the project reference-device constraints**.
- ChatGPT assessment: a separate clean-sheet candidate merits review, while currently observed QW4 localization and current-normalization blockers do NOT by themselves prove a source-code defect; copying the same material/transport assumptions may reproduce them.
- The original `CMP_BASELINE_2.0.0_V2`, `CMP_BASELINE_2.1.0_POL0NOSHELF`, JuSubin's Project B `CMP_B0/CMP_BASELINE_2.0.0_V2`, and all results are **protected and unchanged**. No suggestion of deleting previous projects.

## Scientific question
For a **common, damaged-sidewall blue InGaN/GaN 4-QW micro-LED**, determine whether Project A (locally resistive GaN:C region) or Project B (localized lateral AlGaN barrier) reduces sidewall carrier access and nonradiative recombination **at matched injected current** without unacceptable forward-bias penalty. Clean reference (Nt=0) is a diagnostic control; common damaged-sidewall device (nominal Nt=1e18) is the A/B comparison parent.

## Non-negotiable frozen specification from CMP/COMMON_BASELINE.md
- JBD 4 um *pitch* is an application reference, **not evidence that the physical mesa is 4 um**. A representative model **4.0 um mesa** and **5.0 um domain** are explicit modeling choices.
- Primary target 2D Cartesian, x vertical and y lateral, cylindrical OFF. Prefer a **full 4 um** sidewall pair for design verification; Half-domain may be used after quantitative Full/Half equivalence check.
- Kou-based vertical stack: p-GaN 120 nm / p-Al0.15Ga0.85N EBL 26 nm / GaN Barrier0 22 nm / In0.15Ga0.85N QW1 3 nm / B1 22 nm / QW2 3 nm / B2 22 nm / QW3 3 nm / B3 22 nm / QW4 3 nm / B4 22 nm / n-GaN 4.0 um; numerical n-base +0.3 um is separately documented.
- n-GaN donor 5e18 cm^-3; nominal *effective active* p-GaN/EBL acceptor 3e17 cm^-3 as model approximation. Do not conflate activated acceptor with chemically introduced Mg or hole density; validate actual incomplete-ionization implementation.
- Etched-sidewall damaged host-semiconductor region 5 nm on both sides. Damaged QWs retain InGaN; damaged GaN remains GaN; damaged EBL remains AlGaN.
- Sidewall acceptor-like bulk trap **starting model**: Et=Ev+0.75 eV, Nt=1e18 cm^-3, sigma_n=sigma_p=1e-15 cm2; test Nt=0 as control, with 1e17/1e18/1e19 sensitivity only when ready. The model is not JBD's measured trap density.
- Final fair A/B physics must be identical and consistently checked (Fermi, polarization, SRH, Radiative, Auger, mobility, high-field saturation, incomplete ionization, 300 K). Stepwise model isolation is for diagnostics, not silent modification of the agreed final baseline.

## Why redesign is under consideration — separate evidence from hypothesis
- OBSERVED: previous 3.6 V 4-QW radiative share on QW4 ~99.97/99.99% at PolAct0.5 and ~99.889/99.964% at PolAct0; input equivalence remains unverified; this is QW radiation *share*, not IQE.
- OBSERVED: at same 3.6 V native current changes by ~132x / ~493x with the PolAct diagnostic; cannot call that a matched-current comparison.
- UNRESOLVED: uncalibrated 2D current-to-4um-square J mapping; Full/Half+mesh equivalence; cause of QW4 carrier localization; actual contact/area effects; classical drift-diffusion assumptions/3 nm quantum-well transport; experimental calibration.
- OBSERVED prior Project B geometry: Bspan>0 **replaces selected 100 nm lateral QW-edge semiconductor with AlGaN**, rather than simply adding an exterior coating; the physical B concept (inserted internal barrier vs deposited surface film) requires an explicit agreed process cross-section before coding. Not yet evidence the model is wrong, but no direct equivalence has been established.

## Proposed new-device build sequence (all PROPOSED)
1. **Design gate:** create a single-layer-by-layer device specification with reference, material, thickness, doping, orientation, contacts, mesa/etch/n-contact, damage coordinates and intended A/B region mapping. Resolve 4um pitch-vs-mesa and Project B geometry upfront. Compare every deviation against COMMON_BASELINE and record approval.
2. **Geometry-only SDE:** define full cross-section with exactly four InGaN QWs and five GaN barriers, correct materials/composition, p-/n-contacts, no unintended shelf. Check mesh minimum near 3nm QW and 5nm damage and list/visualize all actual region names.
3. **Clean LED SDevice pilot:** no extra sidewall traps (Nt=0); verify 0V equilibrium, contacts and injection, 0–3.6V forward sweep initially and 5V only after convergence. Validate effective material properties, electron/hole profiles and every QW, not just solve termination; document raw 2D I unit/AreaFactor/physical normalization.
4. **Damaged-sidewall baseline:** on same geometry and physical models only change Nt=0→1e18; check localized trap activation, matched-current full-QW radiative/SRH/Auger and damaged-region losses, current conservation and expected directional effect. If clean LED behavior is anomalous, fix underlying transport/model first, not trap concentrations to force an IQE number.
5. **Adequacy gates:** mesh convergence, Full/Half agreement, QW4 root-cause limitation, perturbation sensitivity (polarization, band alignment or quantum corrections only with documented one-variable evidence), literature-reasonable I–V and carrier distribution.
6. **A/B branches:** only after a credible common parent is frozen, clone into individually versioned Project A and Project B with matched contacts, contacts/areas, source physics, geometry and Nt/Et/sigma; vary the intended edge mechanism only. Compare at matched current, including injection penalty and radiative *absolute* output with consistent active volumes.

## Provenance / constraints
- Actual school-server private source and run logs take priority over historical GitHub `CMP/tcad/CURRENT` (currently partial/older legacy paths).
- For any executable Sentaurus SDE/SDevice syntax, consult `CMP/references/TCAD_REFERENCE_INDEX.md` and original **T-2022.03** UG/examples; do not invent unsupported keywords; verify exact preprocessed pp*.cmd/par and actual solver logs.
- New SWB project name follows `CMP/PROJECT_NAMING_CONVENTION.md`; **tentative** `CMP_BASELINE_3.0.0_REBUILD`, not created, must first check real server for collisions and finalize version as a separate lineage.
- No proprietary full Sentaurus source/logs/manual PDFs uploaded to public repository.
- No change yet to `CMP/COMMON_BASELINE.md`, existing team Baseline FREEZE HOLD, Project A/B performance claims or project-wide `NEXT_ACTIONS`.

## First concrete deliverable
Agree a concise device specification and reference cross-section before any runnable code. Then author only the geometry SDE candidate in an isolated new SWB project; validate geometry and material map before SDevice. Obtain the official T-2022.03 manual source in the active chat/session if exact new syntax is needed.
