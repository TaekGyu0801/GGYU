# Project B literature-to-TCAD parameter provenance / controlled first-run specification (2026-11-16)

- Worker: **주수빈**; reviewed by ChatGPT.
- **Status:** DESIGN RECOMMENDATION grounded in prior user-approved `CMP/PROJECT_AB_WU10_DESIGN_FREEZE_20261108.md`; **NOT** a new school source edit, verified T-2022.03 compile, numerical solution, optimized geometry, or fabrication-verified process. Existing baseline and Bnull/B1 freeze values are retained.
- This document is a **parameter-provenance guardrail**, not a replacement for the school's authoritative successful `/user/semi/semi437/tmp/myproject/CMP_WU_Copy` source/PP/mesh/.par/log. Compare that actual source before writing or running any new deck. GitHub candidate `CMP/tcad/candidates/CMP_BASELINE_3.2.0_WU2023PHY` says PROPOSED/UNRUN, and must not be assumed byte-equivalent to school's working parent.
- Single-source principle: **Wu 2023 working Baseline = entire unchanged base physical/numerical system**; Yuanpeng Wu 2022 = candidate Al fraction/motivational heterojunction mechanism only; Furtmayr 2011 = lateral field/confinement caution only. Never merge whole parameter sets or nanowire crystal orientation/growth/polarization-doping results into planar source.

## Source papers and directly transferable claims

1. **Zhuang Wu et al.** *Physical mechanisms on the size-effect in GaN-based Micro-LEDs*. Micro and Nanostructures **177**, 207542 (2023). DOI https://doi.org/10.1016/j.micrna.2023.207542 . 10um device; 3.9um nGaN, Si5e18 cm^-3; 4x In0.08GaN 3nm QWs, GaN 8nm barriers; nominal pGaN Mg2e19 cm^-3; acceptor-like traps within 5nm of sidewalls; carrier depletion + lateral current dispersion reduce radiative recombination. Applicable as planar damaged working baseline only. The exact school model uses implementation assumptions beyond the paper.
2. **Yuanpeng Wu et al.** *InGaN micro-light-emitting diodes monolithically grown on Si: achieving ultra-stable operation through polarization and strain engineering*. Light: Science & Applications **11**, 294 (2022). DOI https://doi.org/10.1038/s41377-022-00985-4 . N-polar bottom-up nanowires, six InGaN/AlGaN QWs, ~12nm QWs, In ~26-30%, AlGaN barrier Al ~15% (EDS), AlGaN/GaN side shell **with vertical Al composition gradient**; polarization doping/strain compensation affect QCSE and emission. **Only ~15% Al is a literature-anchored candidate composition for our INITIAL test**. Do NOT copy 12nm QW, In30%, 3e17 cm^-3 induced electrons, vertical Al grading, N-polarity, QCSE improvement, shell mechanism, or Zn/other material values into existing Wu2023 planar model. In Fig4 this paper describes ~20nm **vertical strain penetration** into adjacent barriers, not evidence for our **lateral 20nm** guard width. Top-down post-etch passivation is distinct from bottom-up nanowire shell.
3. **Furtmayr et al.** *Carrier confinement in GaN/AlxGa1−xN nanowire heterostructures (0<x≤1)*. Physical Review B **84**, 205303 (2011). DOI https://doi.org/10.1103/PhysRevB.84.205303 . 3D GaN nanodiscs + lateral AlGaN shell; x~0.30 nanowire emission energy maximum corresponds to lowest radial field; larger x can enhance radial fields and suppress light. Qualitative mechanism/caveat only; x0.30 is NOT a transferable optimum and PL/radial-field values are NOT planar TCAD calibration data.

## Frozen first-run values and provenance

| Parameter | B0 | Bnull | B1 | Provenance / constraint |
|---|---|---|---|---|
| 2D full lateral width `Wm` | 10.000 um | same | same | Wu2023 + school working baseline; NOT a 10x10um square area |
| Vertical pGaN thickness | 0.120 um | same | same | Current school pilot **not verified Wu2023 paper value** |
| EBL thickness | 0 um | same | same | Current school pilot **NOT a claim Wu2023 has no EBL**; distinct baseline question |
| nGaN thickness | 3.900 um | same | same | Wu2023 |
| nGaN Si nominal donor | 5.0e18 cm^-3 | same | same | Wu2023; keep active species and activation mapping from actual school deck |
| pGaN nominal Mg input | 2.0e19 cm^-3 | same | same | Wu2023; actual ionized acceptor depends on school incomplete-ionization configuration |
| QWs | 4 x In0.08GaN, 3nm | central retained | central retained | Wu2023 |
| Barriers | GaN 8nm each | central retained | central retained | Wu2023; actual stack implemented as Barrier0..4 (5 barriers) in 2023 candidate, count an implementation choice to verify in live school deck |
| Background barrier donor | `NBg=1e15 cm^-3` | unchanged in barrier-origin segments | unchanged in barrier-origin segments | School candidate pilot, **not sourced as Wu2023 measured value** |
| 5nm original Damage both sides | preserved | preserved | preserved | Wu2023 + current baseline y[0,0.005], [9.995,10] um; material and trap unchanged |
| Damage trap density main comparison | n25 `NtSide=1e18 cm^-3` | same | same | Existing school model/calibration nominal, NOT Wu2023 uniquely measured density |
| Damage TrapEt, sigma, PooleFrenkel, 22 trap blocks | original school | exactly original | exactly original | Resolve exact effective source/PP; don't invent new numerical trap energies/cross sections |
| New guard thickness per side (lateral `y`) | none | 0.020 um | 0.020 um | **CMP first-run hypothesis**, not article measurement; two sides remove 40nm/10000nm=0.4% projected InGaN width |
| Guard vertical extent `x` | none | 0.120..0.172 um | same | CMP design: all 9 barrier/QW layers; not an external coating |
| Guard lateral left/right `y` | none | [0.005,0.025], [9.975,9.995] um | same | CMP design; direct interior neighbor of original 5nm Damage |
| Guard QW-origin host | original InGaN QW | GaN, intentional dopant=0 | Al0.15Ga0.85N, intentional dopant=0 | Bnull controls lost InGaN active volume; B1 minus Bnull isolates Al alloy |
| Guard barrier-origin host | original GaN | GaN with same `NBg` | Al0.15Ga0.85N with same `NBg` | Retain original source doping for barrier-origin sections |
| Guard `xMoleFraction(Al)` | n/a | 0 | 0.15 | B1 initial anchor from Yuanpeng Wu2022 barrier Al content; **not validated planar optimum** |
| New trap/extra Mg/extra Si/shell gradient | none | none | none | Don't introduce unrelated physics, `C` traps, Al composition gradient, induced donors or surface passivation in current B1 |
| Original global material/physics | existing school | identical | identical except AlGaN region interpolation | Retain school contacts, mobility, Fermi, recombination, polarization, temperature, orientation, thermionic and quantum settings |

Coordinates are in um and use historical school x=vertical p->n, y=lateral. Nominal stack x: pGaN [0,0.120]; Barrier0 [0.120,0.128]; QW1 [0.128,0.131]; Barrier1 [0.131,0.139]; QW2 [0.139,0.142]; Barrier2 [0.142,0.150]; QW3 [0.150,0.153]; Barrier3 [0.153,0.161]; QW4 [0.161,0.164]; Barrier4 [0.164,0.172]; nGaN [0.172,4.072]. New guard partitions nine original Clean layers into left/center/right; expected 33 original regions -> 51 regions, **not a proved generated mesh**.

### Physics implementation integrity rules

- **No hardcoded `Eg`, `Chi`, `ΔEc`, `ΔEv`, mobility, masses, polarization constants or strain data from Wu2022/Furtmayr.** For `xAl=0.15`, use the **same versioned school Sentaurus AlGaN library/default/interpolation mechanism** in B1 and record the actual .par/effective pp; extract local `ConductionBandEnergy`, `ValenceBandEnergy`, `ElectricField` from the run. The physical band offset, hole barrier and carrier response are **not known a priori** from xAl alone.
- **Polarization orientation matters.** For mostly c-axis polarization along vertical x, the bound sheet charge at a purely lateral y-normal interface is `sigma_b=(P2-P1)·n_y` and is zero if P has no y-component. Additional polarization/strain interfaces along x and geometry-dependent effects remain possible. Do not assume Wu2022's N-polar graded-shell doping or Furtmayr nanowire radial fields appear automatically in this uniform planar 2D guard.
- **Model scope matters.** If school B1 requires region-scoped Mg incomplete-ionization (to avoid AlGaN species error), apply the same material-consistent fix across all compared cases including a **B0-regression copy**, validate B0-regression matches old B0 before interpreting B0/Bnull/B1. Never compare B1 with changed common solver/Physics against an unmodified B0 as if only Al changed.
- **Do not silently adopt prior GPT FIX1 proposed solver change** (QS inner Iterations50/LineSearchDamping0.1) as a new physical model or successful numerical fix. First compare actual successful school's solver and B candidates; if controlled numerical stabilization is essential, use the **same** numerical settings for B0-regression, Bnull and B1 and document convergence/stability.
- **Quantum/strain claims:** school classical or quantum models must be inspected before interpreting QCSE/wavefunction overlap; no claim of 2022 nanowire QCSE screening or growth-induced strain compensation from a planar uniform Al fraction.
- This structure is an **idealized TCAD semiconductor replacement** inside the QW edge; it is not an experimentally demonstrated post-etch external AlGaN passivation shell or proven feasible fabrication flow.

### Local mesh specification already proposed in the November 8 freeze (UNVALIDATED)

- Preserve original Wu QW 3nm vertical refinement and original Damage 5nm mesh.
- On x[0.120,0.172] at both 20nm guards **plus 10nm lateral neighbor and 3nm x collars around interfaces**, first-run candidate local `maxX=0.001um`, `minX=0.0004um`; `maxY=0.002um`, `minY=0.0005um`. Local only, no whole-device fine mesh.
- This is **numerical resolution choice**, not literature-measured thickness and **not guaranteed to converge**. Check minimum mesh angles, geometry, region count, freshness, and a single 5V case before any broad sweep. Do not attribute a changed outcome to Al if mesh/solver/physics also differ across controls.

## Comparison matrix and diagnostics (first-run gate)

- **B0 reference:** historically successful school damaged `n25` (`NtSide1e18`) with unchanged real school source; make matching **B0-regression** if common deck changes are needed for the new AlGaN run.
- **Bnull:** same 20nm-per-side internal guard regions, GaN instead of original InGaN in guard QW-origin regions, SAME control deck as B1. Tests QW-volume removal / geometry-partition effect.
- **B1:** Bnull identical source/geometry/mesh/doping/physics/solver except `GaN -> Al0.15Ga0.85N` in guard material and the mandatory per-material alloy interpolation. `B1-Bnull` isolates alloy-barrier effect, `Bnull-B0` isolates structural/QW-volume effect, `B1-B0` is full intervention.
- Use **matched injected terminal current** (and same 2D normalization), NOT just matched applied voltage; 5V can additionally be reported. Avoid claiming J=10A/cm2 until actual school 2D AreaFactor/area convention is verified. Need successful 5V run and IV interpolation/state at matched current.
- Required quantities: (1) voltage cost at matched I; (2) absolute total InGaN QW `RadiativeRecombination` integral with changed QW volume stated, and secondarily radiative density normalized by remaining QW volume; (3) original 5nm Dmg region net trap / SRH loss with nonoverlapping rate accounting, no naive `eGapStates+hGapStates` addition; (4) lateral electron/hole current, densities, field, and bands at edge; (5) material region/trap/active-QW volume checks. No IQE/EQE improvement claim unless all relevant net loss rates and injection/optical factors validated.
- **Success gate (conditional):** relative to valid B0-regression at matched I, sidewall trap loss falls, **absolute InGaN QW radiative output is maintained or improves**, and forward-voltage penalty is acceptable. Merely suppressing all injection or numerically increasing a ratio after removing QW volume is **NOT** success.
- If first run is physically/numerically trustworthy but difference inconclusive, explore **one-factor-at-a-time** sensitivity on Al mole fraction `0.10/0.15/0.20` while lateral width stays20nm; afterward widths `10/20/40nm` at fixed x0.15 only if justified. These are **optional CMP test points**, not literature-specific optimal values and not all simultaneously run.

## Unresolved school-verification blocker and next action

1. Read actual live school successful Wu10 full `sde_dvs.cmd`, `sdevice_des.cmd`, `sdevice.par`, SWB inputs and effective `pp21/pp25` and check real Mg, PooleFrenkel, trap, mobility, polarization/material parameters, contact/AreaFactor, QW and EBL structure, solver and mesh. DO NOT overwrite the protected school Wu parent or mistake GitHub Wu3.2 PROPOSED for executed baseline.
2. Diff school live Bnull/B1 and/or GPT FIX1/Claude candidates against same source. Ensure the only deliberate B1-Bnull physics change is AlGaN material/xAl, and all comparisons use a matched common solver and any Mg scope corrections.
3. Run isolated SDE/mesh/preprocess and **single** n25 target5V. Read actual .log/.out/.err/TDR for convergence, material parsing, band/field and normalized rate integrals. Only after this declare numerical/physical validity.
4. Known prior Bnull Newton/MinStep near 1.892V and B1 source/PP/material issues remain historical blockers; prior offline candidate static PASS is NOT a school solver PASS.

**Status label:** first-run parameter provenance LOCK for literature review / code audit, numerical conclusions UNRESOLVED. No observed simulation result or school code modification in this record.
