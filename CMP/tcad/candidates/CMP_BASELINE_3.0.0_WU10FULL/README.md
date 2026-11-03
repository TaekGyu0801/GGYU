# CMP_BASELINE_3.0.0_WU10FULL — Wu-inspired candidate, **PROPOSED / NOT RUN**

**This code is an original clean-sheet structure and model-integration smoke-test candidate. It is NOT a verified reproduction of Wu et al. 2023 and NOT the adopted CMP Common Baseline.**

Paper: Wu et al., *Physical mechanisms on the size-effect in GaN-based Micro-LEDs*, Micro and Nanostructures 177, 207542 (2023), DOI https://doi.org/10.1016/j.micrna.2023.207542 .

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
