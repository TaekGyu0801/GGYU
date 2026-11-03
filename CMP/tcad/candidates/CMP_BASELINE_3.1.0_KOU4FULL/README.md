# CMP_BASELINE_3.1.0_KOU4FULL — independent Kou-epitaxy CMP candidate

Status: **PROPOSED / NOT EXECUTED**. This is NOT exact reproduction of Kou et al. (2019), and not the selected common baseline.

Paper: Kou et al., *Impact of the surface recombination on InGaN/GaN-based blue micro-light emitting diodes*, Optics Express 27 A643–A653 (2019), https://doi.org/10.1364/OE.27.00A643 .

## Purpose and provenance
A separate **full 2D 4µm planar stripe** candidate to compare independently with `CMP_BASELINE_3.0.0_WU10FULL` under a future common evaluation protocol. Based on the previously recorded CMP Kou-derived epi (4 QWs of In0.15GaN at 3nm; five GaN barriers of 22nm; nGaN4um). **4µm is the CMP target, not asserted to be Kou's original simulated chip size**. Sidewall host layers are 5nm on both sides, a CMP experimental choice.

## Included now
- `sde_dvs.cmd`: geometry, 4 QWs, dual 5nm strips, provisional contacts, doping, and refinement windows. Static source derived by audited parameter adaptation of existing independent Wu structural generator, NOT from the original V2 shelf model.
- **No SDevice/par code yet**: geometry and mesh must first be inspected. Do not repurpose Wu SDevice as a published Kou model without checking per-region trap assignments and material parameters.
- SDE `Wm=4`, `tQW=0.003`, `tQB=0.022`, `tN=4`, `xIn=0.15`; provisional `tP=0.120`, EBL disabled, `ND=5e18`, `PMgActive=3e17`, `NBg=1e15`, full-width Ohmic contacts.
- Full-height 5nm trap-host strips are just geometry; Kou surface recombination model has **NOT** been reproduced. Later choose explicitly surface/interface SRH vs volumetric trap proxy and document units, Et, Nt or S.

## Must check
1. School server SWB name availability, SDE preprocess, log, mesh and contact/region identities. Input not validated in actual T-2022.03.
2. Whether Kou original EBL, layer thickness/doping, contacts, surface recombination formulation and numerical physics should replace placeholders.
3. Do not compare a 10µm Wu and 4µm Kou as proof of paper-physics superiority: first check each at its own reference scale, then compare at a **matched 4µm size**, with consistent defect representation, matched terminal current/current density after validated 2D area mapping, and clean vs damaged differences.
4. A clean 0.1V numerical smoke is only a syntax/solver smoke; physical baseline needs higher-bias transport, QW1–4 balance, current and trap budget, and damage loss.

## Naming / protection
`CMP_BASELINE_3.1.0_KOU4FULL` is a separate proposed candidate; protected original V2.1 Kou-source baseline and Wu candidate remain untouched. No new school-server run or solution result exists here.

## SDevice candidate (2026-11-03; code only)
- `sdevice_des.cmd` now exists; **NOT RUN** and not T-2022.03 parser-validated. Uses SWB node parameters `NtSide`, `PolAct`, `Vstop` and matching `DmgL_*/DmgR_*` SDE region names. Reuses an audited CMP/Wu pilot equation and solver scaffold, not Kou's calibrated physics.
- SDE → SDevice only is sufficient for first smoke; no separate SDevice2/SVisual2 required. Keep clean and damaged runs as separate parameter splits with preserved outputs.
- First only after SDE pass: `NtSide=0`, `PolAct=0`, `Vstop=0.1`. Physical run and ON/OFF comparison require literature-specific surface recombination mechanism, p/EBL/contact, material parameters, 2D area convention and QW injection audits. In particular 5nm **bulk** traps are not mathematically identical to a Kou surface recombination velocity condition.
- A missing `sdevice.par` is intentional for this syntax smoke; built-in MaterialDB values are **not validated**.
