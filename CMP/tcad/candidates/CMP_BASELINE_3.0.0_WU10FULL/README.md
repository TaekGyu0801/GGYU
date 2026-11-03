# CMP_BASELINE_3.0.0_WU10FULL — Wu-inspired candidate, **0.1V NtSide0 solver smoke finish observed; physics unvalidated**

**This code is an original clean-sheet structure and model-integration smoke-test candidate. It is NOT a verified reproduction of Wu et al. 2023 and NOT the adopted CMP Common Baseline.**

Paper: Wu et al., *Physical mechanisms on the size-effect in GaN-based Micro-LEDs*, Micro and Nanostructures 177, 207542 (2023), DOI https://doi.org/10.1016/j.micrna.2023.207542 .

## 2026-11-03 — Wu10 SVisual1 geometry-normalization correction, SDE/SDevice source audit (PROPOSED POSTPROCESS FIX)

- **Code added:** `svisual1_iv.tcl` under this Wu10 candidate, commit `a504f60`. Derived from user-visible previously plotted SVisual1 v1.0, setting only the actual Wu10 `Wmesa=10.0 um` (the old CMP4 postprocessor erroneously used 4.0). Retains 1D IV/|JV| display, exact raw voltage/current CSV export, unique node names and low-voltage points including the `NtSide=1e18` near-0V spike for later investigation. Filenames explicitly indicate Wu10.
- **Test level:** Tcl syntax and formula tested with a mocked SVisual command interface and 4 synthetic points; no target T-2022.03 execution by GPT. `0.1V NtSide=0` SDevice/old SVisual has already been *observed on the school server*, but this NEW replacement is NOT yet server-tested.
- **Conditional units:** `J[A/cm2] = abs(I_2D[A/um])*1e8/10` applies only when `AreaFactor=1` and raw 2D current in A/um are actually verified in installed runtime. A 10um normalization rescale is ×0.4 vs erroneous 4um plots; DO NOT interpret as 10×10um² physical square pixel current-density calibration.
- **SDE static audit (no edit):** Wm=10um, Wdamage=0.005um each side, 4×3nm InGaN xIn0.08 QWs, 5×8nm GaN barriers, nGaN 3.9um, total vertical depth 4.072um, 3 lateral subregions per semiconductor layer. Contact, p=0.120um, EBL=0, MgActive3e17, barrier background1e15 and 5 barrier count remain **PILOT/partly assumed**. School mesh/region doping maps have NOT independently been audited. Full 2D stripe != 3D square.
- **SDevice source audit (no edit):** `DefaultParametersFromFile` added in earlier commit `066bbc3`. Global Fermi, mobility, SRH/Radiative/Auger and piezo with `PolAct`; every Dmg sidewall partition has assumed acceptor trap `Et=Ev+0.75`, `sigma_n=p=1e-15`, `NtSide`. Full SDevice `NtSide=0/PolAct=0/Vstop=0.1` completed per user log on Nov 3 20:30:09 KST; `NtSide=1e18` low-bias SVisual plot observed, but actual ON solver log still not inspected, and apparent near-zero-V spike remains unresolved. `PolAct=0` and omitted Mg incomplete ionization are **smoke-only choices**, not Wu physics. No evidence of true operating-voltage injection, IQE or calibrated Wu reproduction.
- **Decision:** Preserve SDE/SDevice source pending targeted parameter/mesh/physics audit, DO NOT declare physical baseline validated. Re-run only SVisual1 with proposed width fix; then inspect ON solver log, contact current unit/AreaFactor and 0V PLT points. Do not overwrite CMP4/Kou/Lee code.

## 2026-11-03 20:30:09 KST — confirmed SDevice low-bias completion (verified user terminal log)

`n2_des.log` final 35 lines supplied by user: step `t=0.984303 -> 1`, anode `0.1 V`, electron `7.544E-31`, hole `8.430E-32`, total current `+8.387E-31`, cathode `-8.387E-31` (raw output units); `Curve trace finished`; `n2_des.tdr` written; `Sentaurus Device simulation finished` Tue Nov 3 20:30:09 KST. Memory 632 MB; 423.72 s wallclock; 41.39 s CPU. This **confirms solver finished the clean 0.1V smoke**, but not LED injection, NtSide1e18, physical Wu reproduction or reliable J units.

SVisual1 screenshot displayed plotting; previously shared script used 4um normalization, which is incorrect for Wu10 10um width if A/um and AreaFactor=1 (needs 10um, and independent unit audit). School SVisual code update not yet independently confirmed.

## 2026-11-03 21:20 KST — school CMP_WU low-bias smoke observation

**OBSERVED (user screenshot, school SWB; not an independent server log audit):** `/user/semi/semi437/tmp/myproject/CMP_WU` with `NtSide=0, PolAct=0, Vstop=0.1` produced a plotted SVisual1 I–V and J–V curve to ~0.1 V after the school's SDevice command was re-preprocessed to include `DefaultParametersFromFile`. Screenshot shows `BaselineData 6`, a red `NtSide=0` curve, and ~8.5e-31 A/um output at 0.1 V (approximate visual reading). Initial `UNDEFINED model` and licence-checkout roadblocks no longer prevented **this** smoke stage. Full SDevice success/solver completion, physical validity, high-bias transport, matched-current trap loss, `NtSide=1e18` branch and valid IQE are **NOT established** by the plot alone. The low-bias ~zero current is expected to be uninformative for LED turn-on.

**Normalization problem (PROPOSED correction, no SWB file changed by GitHub):** the SVisual1 script shared earlier in chat uses `set Wmesa 4.0`, while Wu10 SDE mesa width is **10.0 um**. Under a validated `A/um` raw 2D current, `AreaFactor=1` and uniform stripe-depth convention, physical area-normalized J should use `Wmesa=10.0`: `J[A/cm2]=abs(I_2D[A/um])*1e8/10.0`. The currently displayed J curve (~2.1e-23 A/cm2 at 0.1V) scales like 4um normalization; if those assumptions hold it is 2.5x too high and corrected estimated J ~8.5e-24 A/cm2. Verify actual dimensional units/output/log before scientific use. Only SVisual postprocess requires update, not SDE or SDevice. This Wu-specific fix must **not** change the separately protected common CMP4um baseline's width. No Wu paper equivalence or Baseline Freeze claim.

NEXT: (1) check the school's SDevice log finish/0.1 V completion, (2) correct Wu SVisual1 `Wmesa` 4→10 and rerun **only SVisual** (no additional SDevice licence), (3) once relevant, run `NtSide=1e18` matched pilot smoke and gradual higher-bias physical validation, and inspect meaningful QW injection/recombination before adopting a baseline.

## 1. Files and SWB roles

- `sde_dvs.cmd`: new Full Cartesian 2D stack generator, 10µm lateral width, dual 5nm trap-host strips, refinement windows for 3nm wells / 5nm edges.
- `sdevice_des.cmd`: one common SDevice pilot for clean and damaged. Enter three **SDevice node parameters** in SWB: `NtSide`, `PolAct`, `Vstop`. Paste this same command into both nodes. SWB preprocess symbols: `@tdr@`, `@plot@`, `@tdrdat@`, `@log@`.
- No `.par` override file: the initial pilot deliberately relies on installed material parameter defaults, which have **NOT BEEN CHECKED**. A calibrated `sdevice.par` must be written only after verifying T-2022.03 MaterialDB and paper references.

## 2. Parameter provenance (critical)

| Field | Draft value | Status |
|---|---|---|
| Width, nGaN | 10µm, 3.9µm | Wu reported |
| n-GaN active donor | 5e18 cm^-3 | Wu reported Si doping; mapping to active assumed |
| QW In fraction | 0.08 | Wu reported |
| Four QWs / QW thickness | 4 / 3nm each | Wu reported |
| 5 GaN barriers | 8nm each | Wu reported barrier thickness; five for 4 wells is conventional **count assumption**, verify Wu figure |
| L/R local damaged strips | 5nm each | Wu reported localized trap-placement width |
| p-GaN Mg chemical source | 2e19 cm^-3 | Wu literature reports **chemical Mg**, NOT applied as active doping in draft |
| p-GaN thickness | 0.120µm | **PILOT choice from prior CMP context; NOT Wu verified** |
| Pilot pGaN active Mg | 3e17 cm^-3 | **PILOT model input; NOT Wu's 2e19 chemical dose; no incomplete ionization** |
| EBL | OFF, 0µm | **UNVERIFIED/UNSPECIFIED**, not evidence Wu lacks EBL |
| QB background donor | 1e15 cm^-3 | **PILOT** |
| Contacts | full-width top p & bottom n Ohmic | **PILOT geometry; NOT Wu exact contact structure** |
| Trap bulk acceptor, Ev+0.75eV, σn=σp=1e-15cm² | `NtSide`: clean0 / damaged1e18 | **CMP calibration PILOT; not established Wu exact trap** |
| Polarization `PolAct` | 0 first numerical smoke | **NUMERICAL SMOKE ONLY; not Wu physical model** |
| Device simulation | Quasistationary up to `Vstop` | **NUMERICAL pilot; Wu time/transport solver unverified** |
| MaterialDB / e–h transport / recombination B,C / quantum well physics | installed defaults | **NOT AUDITED** |

Do **not** report any pilot outcome as measured IQE, calibrated Wu device, or adopted 10µm reference. In particular, absence of EBL, provisional contacts and Mg ionization can strongly affect QW injection, QW4 concentration and leakage.

## 3. Staged execution gates

0. **Before entering code:** On the school server confirm the current SWB project naming and create a **new independent project** `CMP_BASELINE_3.0.0_WU10FULL`, do not clone an old shelf-containing copy. Keep current CMP4µm baseline untouched. Verify material `InGaN` and `xMoleFraction` resolve using installed T-2022.03 MaterialDB.
1. **SDE-only smoke:** paste `sde_dvs.cmd` into the new SDE node, preprocess and build. In SVisual verify every region, 4 QW widths0.003µm, QB widths0.008µm, 5nm DmgL/DmgR edge strips, both contacts, correct In0.08, effective doping and severe min-angle/tiny-edge artifacts. No SDevice run until geometry checks pass. Actual T-2022.03 syntax compatibility **NOT executed by author**.
2. **SDevice initial parse and low-bias test:** use `NtSide=0, PolAct=0, Vstop=0.1` on clean first. Verify preprocessed `pp*_des.cmd`, material/region names, final actual voltage, current signs and Newton convergence. Do not call this a physically functioning LED.
3. **Restore physical models:** obtain Wu full methods/figure and report exact p/EBL/cap thicknesses, contacts, Trap Et/Nt/sigma, InGaN/GaN polarization, p-Mg incomplete-ionization species parameters, thermal/optical/quantum transport assumptions and model output reference. Replace all pilot fields with verified originals or transparent model assumptions. Re-check material default parameter files and effective runtime.
4. **Clean physical model:** run to suitable forward operating point, inspect QW1–4 e/h density, quasi-Fermi levels, band energies and rates; any QW4 ~100% localization requires audit before fitting Trap.
5. **Damaged ON:** change only `NtSide` on same verified stack/mesh. Verify regionwise `eGapStatesRecombination`, current/recombination closure, and matched-current normalized QW radiative generation `q sum(QW Rrad)/I` using validated 2D integration unit.
6. **Full/Half:** only if symmetric electrode/trap/AlGaN/GaN:C interventions. Compare mirrored 5µm half numerically with full, accounting for area factors and current scaling.
7. **Project A/B:** only after common damaged parent freeze. Neither branch may silently change defect concentration, width, contacts or QW volume without explicit numerical accounting.

## 4. Important limitations

- Full **2D** represents two sidewalls of a stripe, not all four sides of a real 10×10 µm² square. Do not convert 2D raw A outputs to square J without confirmed out-of-plane width convention.
- Missing Wu source specifics prevent literal paper reproduction. The present deliverable is a **reviewable implementation starting point**, not a promise that Sentaurus solver will converge.
- `NtSide=1e18` and `Et=Ev+0.75` are calibration hypotheses from prior CMP, **not validated Wu parameters**.
- Source protections: original old Baseline and Lee's active server project untouched; no proprietary Synopsys UG or private third-party code copied.

## 5. Syntax references (not claims of local execution)

- T-2022.03 official UG indices: `CMP/references/TCAD_REFERENCE_INDEX.md`.
- Synopsys SDE public tutorial: https://ghzphy.github.io/Sentaurus_Training/sde/sde_2.html and /sde/sde_4.html .
- Synopsys SDevice public tutorial: https://ghzphy.github.io/Sentaurus_Training/sd/sd_1.html and /sd/sd_13.html .
