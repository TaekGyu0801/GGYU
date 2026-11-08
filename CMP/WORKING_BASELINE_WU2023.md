# CMP A/B Working Comparison Baseline — Wu-inspired 10 µm (decision 2026-11-08)

**Decision owner:** 주수빈 (user explicitly: "일단 지금확정한 baseline으로 projectA와 B를 이어나가자.")  
**State:** USER-APPROVED WORKING COMPARISON PARENT (A/B engineering GO), **NOT** paper-exact Wu reconstruction, full scientific IQE validation or publication-grade baseline freeze.  
**Actual active school project:** `/user/semi/semi437/tmp/myproject/CMP_WU_Copy`. **Do not modify this parent or its existing outputs.**  
**Source of fact:** existing real school pp1_dvs.cmd/pp25_des.cmd/.par and n21/n25 solver/TDR/PLT readings documented in CURRENT_STATUS/TIMELINE, plus Wu et al. 2023 original PDF directly supplied 2026-11-08. **This markdown is a comparison decision**, not a new runnable deck.

## Important relationship to legacy protected baseline
- Existing `CMP/COMMON_BASELINE.md` is the **previous protected Kou-epitaxy 4 µm representative v1** (EBL 26 nm, In0.15, barrier 22 nm), preserved as a historical lineage. Do not overwrite, erase or silently mix it into Wu working experiments.
- This **2026-11-08 explicit user choice** selects the active Wu 10 µm school pilot as the **new common working comparison parent for Project A and Project B**. It does **not** imply the 4 µm document or prior Kou-run results have been physically disproven or removed.
- Both A and B must derive from exactly the same `CMP_WU_Copy` source/mesh/parameters/reference and preserve changes strictly isolated to the intended intervention, with differences documented. Legacy 4 µm Bspan and A prototype runs are **not directly comparable** to Wu 10 µm results.

## Working model / paper provenance
| Item | Current school working value | Evidence status |
|---|---|---|
| Width | 10 µm full 2D stripe | school OBSERVED / Wu Sec.1.1 explicit |
| n-GaN | 3.9 µm; Si input 5e18 cm^-3 | school OBSERVED / Wu explicit |
| MQW | 4 In0.08GaN wells, 3 nm; GaN barriers 8 nm | school OBSERVED / Wu explicit; barrier-count implementation inspect effective school code |
| p-GaN | 120 nm, nominal Mg input 2e19 cm^-3 | 120 nm school PILOT assumption; Mg input Wu explicit, actual activation not identical to chemical doping |
| EBL | 0 nm | **school PILOT assumption**; original Wu Fig.1(b) depicts AlGaN but does not specify thickness/composition; never claim Wu literally specified EBL0 |
| Sidewall damage | left and right 5 nm; acceptor-like localized traps | school OBSERVED / Wu 5 nm explicit |
| Trap nominal | school n21 OFF / n25 ON (`NtSide` nominal ON configuration and exact Et/sigma to be confirmed from effective pp25_des.cmd before changing) | school previous read; numbers beyond 5 nm are calibration/implementation assumptions, not Wu-direct |
| Physics/contact | preserve exact school current polarization, Mg incomplete-ionization, radiative/SRH/Auger, field-related trapping, contacts, solver and mesh | no automatic adjustment from Wu, Kou or another study |
| Simulation tool | school Sentaurus T-2022.03 | Wu paper Sec.2.2 uses Silvaco TCAD, physical implementation equivalence not established |

## Frozen comparison methodology
1. **Damaged baseline reference = current n25 Trap ON** using exact saved school source/geometry/mesh/physics; **n21 Trap OFF** is a clean diagnostic reference. Both original datasets and input hashes preserved.
2. **Project A — 이택규:** user's earlier chosen **A-u n-side GaN:C edge with locally removed Si** is the primary design hypothesis; A-n Si-retained at 1–2 sensitivity points. Controls A0m(Si present/C0), A0u(Si removed/C0) separate Si-removal from carbon effects. Exact school geometry, damage region and dose not validated for runnable coding. Proposed A edge implantation/traps must not inadvertently change baseline Nt or MQWs.
3. **Project B — 주수빈:** historical Bspan=3 / Wedge0.1 µm / xAlB0.15 is a **legacy Kou-v2 lateral AlGaN material-replacement concept**, not an already implemented Wu-10 µm device. For Wu parent: first define physical new edge barrier cross-section and target regions; no blind copy of old `Bspan` macros/geometry/material parameters. Preserve original 5 nm damage and 4 MQWs; avoid calling internal InGaN replacement an external passivation coating.
4. **Project layout:** source snapshots/checksums and versioned isolated SWB working copies (candidate family `CMP_PROJECTA_...`, `CMP_PROJECTB_...`; check collision/name policy before creation), never direct edits to parent `CMP_WU_Copy` or historical Kou project.
5. **Single-condition study initially:** compare B and A with baseline at common injected **2D stripe current-density normalization / same current**, not raw fixed bias. Extract **absolute QW radiative integral**, intrinsic SRH, Auger, one net defect electron-hole pair-loss channel (avoid counting eGap and hGap twice), local edge current, band/carrier profiles, and `ΔV` at a matched current. Use the same integration regions and properly account for changed active semiconductor volume under B.
6. **Scientific limits:** prior successful 5V OFF(n21)/ON(n25) solves and stored PLT low-current electrical trend do **not** establish low-J optical IQE reduction. Existing matched-low-J spatial TDR existence/G3 completion not verified; quantitative IQE/sidewall-suppression performance must not be claimed without adequate evidence. Wu AlGaN in Fig1(b), ITO/SiO2 and contact details are not faithfully reproduced by the current pilot.

## Immediate next work, preserving schedule
- **Read-only first:** inventory actual school `CMP_WU_Copy` full live SDE source and preprocessed SDevice/param/mesh/target outputs; check any saved G3 OFF/ON low-J TDRs; do not repeat solved 5V n21/n25 or canceled n29/hGap jobs.
- **Then two isolated design branches:** A-u geometry mapping on school Wu source; Project B independently maps lateral AlGaN barrier to Wu edge/QWs after defining which regions remain active/damaged. Only generate runnable SDE/SDevice from exact source, official T-2022.03 examples and separately established version provenance.
- **First engineering action:** SDE-only new-copy geometry/mesh validation, check all regions and contacts. New SDevice executions and quantitative A/B claims require real run/evidence and appropriate user authorization; nothing was actually run or coded in this 2026-11-08 decision.
- **Avoid extra gate proliferation:** defer broad Nt, size, QW4 mechanism, n29, and mesh sweeps until they materially affect final comparison/publication claims.

**Last event:** original Wu PDF review 2026-11-08; no source or solver edits in that review or in this decision.
