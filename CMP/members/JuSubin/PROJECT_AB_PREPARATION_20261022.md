# 주수빈 — Project A/B pre-implementation research plan (2026-10-22)

Status: PROPOSED / DESIGN PREPARATION ONLY. No Sentaurus code edits, no project creation, no simulation runs. Worker: 주수빈. AI: ChatGPT.
Context: 주수빈 agreed to focus on preparing Project A/B while 이택규 is currently checking Baseline V2.1. 이택규's acceptance of a formal exclusive ownership split is NOT confirmed.

## Grounded baseline and constraints
- Use current V2.1 `CMP_BASELINE_2.0.0_V2` as reference for READ-ONLY geometry study; final production baseline is NOT frozen.
- Current Half model: 2um simulated half of a nominal 4um mesa, four 3nm MQWs, damaged sidewall thickness 5nm, 12 QW ROI (Clean/Edge/Dmg × QW1–4).
- Existing `Wedge` and `Bspan` hooks are described in project history; actual active SDE code, preprocessing, and full material assignments MUST be inspected before any implementation. Historical active Wedge=0.1um and Bspan=0 are not confirmation for new A/B values.
- Keep the **same damaged sidewall NtSide/Et/sigma** across Common Baseline/A/B. `NtSide=0` is a separate control, not an altered A/B defect profile.
- A/B comparison at equal injected current and comparable device area; 2D AreaFactor/current-density semantics and Full/Half equivalence are open baseline blockers. No absolute IQE claims yet.
- Preserve all existing working SDE/SDevice/PLT/TDR; do not run or rename them.

## Project A — localized carbon-induced resistive blocking
Hypothesis: carbon compensation or modeled deep-level transport modification of localized *GaN* region adjacent to the damaged edge increases effective lateral electrical resistance, reduces carrier access to damaged sidewall, lowers integrated sidewall nonradiative recombination, without excessive extra recombination/voltage penalty.
1. Inspect actual clean/edge/damage region layout and GaN vs InGaN/AlGaN material maps. Initially scope to GaN edge portions only; do NOT place hypothetical GaN:C into InGaN QWs or claim ion implantation depth/feasibility without evidence.
2. Material evidence: Richter et al., Cryst Res Technol 2020, DOI 10.1002/crat.201900129 — bulk HVPE GaN:C semi-insulating at carbon concentration ~8.8e18 cm^-3, deep acceptor CN. This is NOT direct evidence that the same concentration makes LED sidewalls high-R. Lesnik et al., Phys Status Solidi B 2017, DOI 10.1002/pssb.201600708 — GaN carbon compensating acceptor evidence.
3. Model choice is a separate gate: nominal carbon concentration is not automatically equal to electrically active acceptor concentration, fixed resistivity, or a generic SRH trap density. Require C-defect level/charge-state/ionization/trap calibration and a diagnostic edge current/resistance check.
4. Proposed *sensitivity candidates only*, contingent on model: edge lateral width 0.05/0.10/0.20um; nominal C incorporation 1e17/1e18/1e19cm^-3. These are not fitted/verified or approved run values; a no-carbon control must be included.
5. Record actual changed layer extent, edge resistance, e/h current-density maps, edge carrier densities, affected QW recombination, sidewall SRH, leakage, Vf penalty and Auger.

## Project B — localized AlGaN lateral heterobarrier
Hypothesis: a physically defined lateral AlGaN region near sidewall generates band offsets and limits carrier diffusion toward damaged sidewall.
1. Inspect `Bspan` interpretation and specific layer(s) into which AlGaN is inserted; avoid replacing QW material, EBL or contacts inadvertently.
2. Proposed *screening candidates only*: xAl = 0.05/0.10/0.15 and width=0.05/0.10/0.20um, after physically grounded geometry/polarization/band-offset review. No numbers are confirmed model params.
3. Validate both electron and hole barriers, new interface polarization, strain and conduction/valence-band discontinuity; p-side injection, depletion, voltage penalty, unintended carrier crowding. An AlGaN label alone does not establish net suppression or better efficiency.
4. Maintain fixed baseline sidewall trap specification and same-current benchmarking as A.

## Comparison metrics and gates
- Absolute raw anode/cathode current and normalized J with documented 2D convention.
- Matched-current V_f shift and leakage, device-wide balance, full MQW Radiative/SRH/Auger, trap/channel partition, and QW4 dominance.
- Sidewall-damaged region SRH integrated rate and edge/center e/h carrier-density or current-density ratios on identical spatial ROIs.
- 3-channel MQW Radiative/(Radiative+SRH+Auger) only as a model internal proxy; account for trap recombination separately, do not equate to experimentally validated IQE.
- A/B sidewall suppression claim requires a verified decrease of edge-carrier access and trap-related recombination at same current, not just larger radiative *fraction* at smaller absolute terminal current.
- Publication/pilot gate: frozen baseline provenance + current normalization and Full/Half/mesh adequacy, then cloned separately versioned A and B programs.

## First concrete read-only task for 주수빈
On the Sentaurus server in existing V2.1 folder (no code changes):
```bash
cd /user/semi/semi437/CMP_BASELINE_2.0.0_V2
pwd
grep -nEi 'Wedge|Bspan|Wdmg|Edge_|Dmg_|NCedge|AlGaN|Carbon|define.*(rE|rD)' sde_dvs.cmd pp1_dvs.cmd | head -n 140
```
Send actual output for review. Determine existing region hooks and which layers can represent GaN:C or AlGaN BEFORE writing syntax or spawning SWB jobs.

## References / scope note
- CMP GitHub Issue #3 Project A, #4 Project B, #5 fair comparison, AI_SHARED_MEMORY_PROTOCOL.md.
- Richter et al. https://doi.org/10.1002/crat.201900129
- Lesnik et al. https://doi.org/10.1002/pssb.201600708
- Chang et al. https://doi.org/10.1002/jsid.2010 (ion implant high-R microLED edge; NOT direct carbon-implant evidence)
- Liu et al. 2025 review https://doi.org/10.1038/s41377-025-01751-y
- F-implant p-GaN edge microLED https://doi.org/10.1021/acsphotonics.5c02363 (fluorine process, distinct from carbon scheme)
