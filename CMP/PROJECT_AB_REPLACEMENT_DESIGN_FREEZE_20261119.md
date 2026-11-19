# CMP Project A/B replacement — implementation design freeze v0.1 (2026-11-19 KST)

**User decision:** 주수빈 said "좋아. 이걸로 해보자" to two replacement topics. Assign 이택규 to Project A (selective p-GaN Mg deactivation) and 주수빈 to Project B (GaN QB thinning). **Direction adopted; numerical inputs are first-run proposals only (PROPOSED/UNRUN).** Old Carbon A and lateral AlGaN B analyses preserved as historical data; **not** marked scientifically rejected, only deferred for deadline. Previously proposed F-inspired project plan is superseded as immediate priority; do not delete it.

## 0. Parent verification and protected invariants

Original working Wu-based **school** baseline (user-confirmed complete) is authoritative. GitHub `CMP/tcad/candidates/CMP_BASELINE_3.2.0_WU2023PHY` is **PROPOSED/UNRUN** and must NOT be copied over verified school source as if exact. Source candidates and prior Wu design document were read, not school file bytes. Verify actual school `sde_dvs.cmd`, `sdevice_des.cmd`, `sdevice.par`, current `pp*_dvs/des.cmd`, `n*_msh.tdr`, output `.log/.plt/.tdr`, contact boundary, AreaFactor and 2D current units first. Create separate projects with naming policy `CMP_PROJECTA_2.0.0_HEDGE` and `CMP_PROJECTB_2.0.0_QB6` (candidate names; check school collisions).

Shared baseline **from design repository** (some values are pilot implementations, not Wu-paper measurements):
- x=vertical p-to-n, y=lateral; `Wm=10.000um`, `pGaN x0..0.120um`, `EBL=0um` (baseline implementation assumption), `4× QW In0.08Ga0.92N each3nm`, `5× GaN QB each8nm`, `nGaN3.900um`, `Si nGaN=5e18cm^-3`, pGaN nominal Mg input `2e19cm^-3`, barrier background donor `1e15cm^-3` implementation pilot.
- Both 5nm Dmg left/right regions and their 22 original SDevice Trap Physics untouched (trap NtSide=1e18cm^-3, E_v+0.75eV, capture sigma electron/hole1e-15cm2, inherited PooleFrenkel), existing full-width Ohmic contacts, polarization, incomplete Mg ionization, recombination, mobility, 300K, original SDevice Math/Solve and 5V target are unchanged except when a real source audit demands a strictly comparable model.
- Use existing successful baseline Trap ON as F0 reference; Trap OFF available as diagnostic only. No whole baseline physics swap, solver mass-change, global mesh relaxation, unrelated F/C/AlGaN species, or fabrication claims.

## 1. Project A (이택규) — selective H-inspired Mg-acceptor deactivation at pGaN edges

**Primary paper:** Pavel Kirilenko et al., `InGaN-based green micro-LED efficiency enhancement by hydrogen passivation of the p-GaN sidewall`, Applied Physics Express 15, 084003 (2022), DOI https://doi.org/10.35848/1882-0786/ac7fdc ; publisher-open original via KAUST. For green 20 and 100um square LEDs, 16 MQW, 300nm p-GaN, H plasma at 250W, 300°C, 4min; lateral H diffusion estimate ~1.7um, c-axis diffusion under comparable process ~100nm; pGaN sheet resistance up to 10× reported via *other* studies; 20um peak EQE ~1.34→1.86%, other H/nGaN/TMAH treatment effects may contribute. **None of these process conditions or measured ratios are direct inputs or predictions for a 10um blue Wu-based pilot.**

**A1 one-shot electrical proxy (initial design, not literature-calibrated or physical H profile):**
- pGaN x=[0,0.120]um, left y=[0,0.200]um, right y=[9.800,10]um.
- Within these perimeter strips, use only effective `MagnesiumActiveConcentration=2e16cm^-3` (1000× reduction relative to core); *nominal chemical Mg/H content is not modeled*. Original central pGaN stays `2e19cm^-3`.
- Existing `DmgL_pGaN` y0-.005 and `DmgR_pGaN` y9.995-10 have the same reduced Mg **but original sidewall Traps remain**, to prevent an unaffected conducting 5nm-edge bypass under the full-width anode.
- Partition original `Clean_pGaN` into `HEdgeL_pGaN` y.005-.200, `Clean_pGaN` y.200-9.800, `HEdgeR_pGaN` y9.800-9.995. Original 33 region count becomes nominal 35 only if school original matches archived model. Preserve all non-pGaN layers and their 22 region trap names. Use no explicit H species, extra trap, fixed charge, p-contact truncation or SiO2.
- Ring x-depth120nm is a uniform full-pGaN simplifying assumption, though paper c-axis diffusion only ~100nm. Ring width200nm is small compared with paper's ~1.7um lateral H diffusion and represents just 4% of 10um 2D stripe lateral width. Large 1000× Mg-input suppression far exceeds quantitative support of ~10× sheet-R in other literature; **do not claim 1000× conductivity**. These two numbers are the old CMP first-pilot screening parameters, NOT physics-validated optimum. To make an actual hydrogen-fabrication claim would require a calibrated H spatial profile and transport measurements.
- SDE: split and retarget Mg only, all other geometry and doping unchanged. Add local coarse first-pass mesh maxX/Y0.020um, minX/Y0.005um near new pGaN interface, **never weaken** existing finer Dmg/MQW meshes. SDevice global Mg IncompleteIonization remains same if active school source supports; check actual PP and region names before touch. `sdevice.par` unchanged.
- Interpret if p-contact ideal-Ohmic edge artificially bypasses, and analyze local hDensity, hCurrentDensity, acceptor ionization, ElectrostaticPotential, edge versus center path. If no measurable high-R/current detour or big Vf penalty, do not claim success.

## 2. Project B (주수빈) — thin *GaN* QB vertical transport vs sidewall losses

**Primary paper:** Le Chang et al., `Alternative Strategy to Reduce Surface Recombination for InGaN/GaN Micro-light-Emitting Diodes—Thinning the Quantum Barriers to Manage the Current Spreading`, Nanoscale Research Letters 15:160 (2020), DOI https://doi.org/10.1186/s11671-020-03372-3 . A/B/C QB 6/9/12nm, 4x In0.18GaN wells, 26nm Al0.15GaN EBL, 10x10um planar blue chips, APSYS Schrödinger+Poisson+drift diffusion, defected edge width0.5um; surface defects electron/hole traps different from Wu model. Simulated ideal no-sidewall EQE28.8/24.0/22.2% at40 A/cm2. Their results cannot transfer numerically to Wu `In0.08`, EBL=0, 5nm-Dmg, different contacts/physics and 2D area.

**B1 one-shot geometry (initial proposal, NOT known optimum):**
- Change only `tQB=0.008`→`0.006um` (GaN all **five** QB regions Barrier0..Barrier4). Keep `tQW=0.003um`, four In0.08 wells, QW count, nGaN doping, trap concentrations, damage width, 0 EBL, p/n layer nominal thickness, all materials and SDevice physics unchanged.
- Old stack: pGaN0..0.120; active0.120..0.172um (5*8nm+4*3nm =52nm); nGaN0.172..4.072um.
- New boundaries in um: Barrier0 .120-.126, QW1 .126-.129, Barrier1 .129-.135, QW2 .135-.138, Barrier2 .138-.144, QW3 .144-.147, Barrier3 .147-.153, QW4 .153-.156, Barrier4 .156-.162; nGaN .162..4.062 if n thickness remains3.900um.
- The overall device height becomes shorter by10nm; QW total thickness stays12nm and projected *radiative QW volume* constant, while GaN barrier total40→30nm. Do NOT surreptitiously force fixed total height by changing nGaN thickness or contacts in first test; acknowledge ~0.25% change in total device depth and ~10nm contact shift as minor geometric confound.
- Regenerate full SDE mesh, check fine vertical QW3nm and QB6nm resolved, contact locations and region names, plot extraction ROI positions updated (avoid hardcoded old QW depths), including all 22 Dmg Trap region definitions. Reuse school working SDevice/PAR (no imported APSYS Schrödinger, no fabricated heterostructure or modified BPR).
- Current SDevice deck may lack quantum-confined-state transport, so quantitative match to Chang paper cannot be claimed; treat as drift-diffusion+polarization *geometry sensitivity* unless official T-2022.03 manual and effective deck confirm quantum models. Keep the numerical settings identical to baseline on first pilot.

## 3. Comparison, interpretation and risks

- Run only baseline existing F0 reference and A1/B1 independent 5V TrapON one-shot (do not run 4 p-contact prescreens). Verify last anode5.000E+00 V AND `Curve trace finished` plus read PP, mesh, no fatal warnings; "Sentaurus finished" alone inadequate.
- Controlled scientific comparison requires SAME actual total injected I / same **original** fixed device area (and confirmed school 2D `AreaFactor`), not just same5V. Interpolate archived .plt at matched J (target10 A/cm² only after units defined). Compare `Vf(I)`, **absolute** summed-all-4-QW `∫R_rad dA`, net sidewall `eGapStatesRecombination`/SRH loss, current/h/e density maps, QW hole uniformity (per-well central vs edge), `ElectricField` / band energy; account for other recombination, no double count e/h trap channels or label surrogate IQE as measured IQE/EQE.
- Existing Wu baseline original NtSide ON vs OFF 5V log raw current2.566e-3 vs2.569e-3 (difference ~0.12% under condition equivalence assumed). Therefore A/B may yield weak sidewall-specific signature at5V; lower current may be more revealing.
- B primary paper's damaged region width 500nm is 100x baseline 5nm and In and EBL differ; even improved hole supply may increase overall current but show no reduced absolute sidewall recombination. B-thin OFF extra control would be needed to fully separate intrinsic QB improvement from sidewall-specific benefit if time allows; no such run assumed completed.
- If 5V current simply declines, or there is high voltage penalty at same current, or QW absolute radiative falls, classify inconclusive/failure; avoid claiming surface passivation or measured WPE/EQE improvement.
- Results are UNRUN; this spec is a scientifically bounded first-run design plan, not code or validated outcome.

## 4. Handoff / next steps

1. Workers read matching *school-run* Wu baseline source and compare actual PP/mesh/AreaFactor and available bias-point TDR/PLT; protect source with separate versioned clone.
2. Worker A patch **SDE pGaN only**; worker B patch **SDE tQB only**, both retain school-working CMD/PAR. Any syntax patch must consult CMP/references/TCAD_REFERENCE_INDEX.md and installed official Sentaurus T-2022.03 UG and always provide directly pasteable full file/one-line shell-safe command where requested.
3. One SDE preprocess/mesh audit then one SDevice 5V on each branch; only if complete compute matched-current QW/sidewall plots; record errors and go/no-go in GitHub per CMP/AI_SHARED_MEMORY_PROTOCOL.md.

**No school simulation files have been read, modified or executed by ChatGPT.**
