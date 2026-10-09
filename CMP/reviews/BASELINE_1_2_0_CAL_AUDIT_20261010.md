# CMP_BASELINE_1.2.0_CAL — Successful 5 V parent archive audit

Reviewed: 2026-10-10  
Worker: 이택규  
Source: user privately uploaded `CMP_BASELINE_1.2.0_CAL_AUDIT.tar.gz` (11,130,290 bytes); nine tar members.  
Scope: **OBSERVED / computationally DERIVED**; literature-based candidate modifications are **PROPOSED, not simulated**.  
Confidentiality: no proprietary Synopsys command files, material parameter files, logs, meshes, TDRs or PLTs are embedded in this public report.

## 1. Provenance and status

Archive contained exactly nine files: `sde_dvs.cmd`, `sdevice_des.cmd`, `FASTC1_pp6_des.par`, `pp1_dvs.cmd`, `pp2_des.cmd`, `n1_msh.tdr`, `n2_des.log`, `n2_des.plt`, `n2_des.tdr`. Compared SDevice source and its preprocessed version. `n2_des.log` directly shows T-2022.03, actual Node2 0–5V successful Transient BE, final anode 5.000 V, SDevice wallclock 10596.76s (2h56m36s), `Sentaurus Device simulation finished`. Its final Save wrote `n2_5V_ckpt_des.sav` and `n2_5V_ckpt_circuit_des.sav`, but these checkpoint files are **not members of the nine-file archive**. Verify availability on server before planning a restart.

HDF5-formatted `n2_des.tdr` independently contains 65,513 vertices, x-coordinate range 0–4.568µm, y range 0–2.5µm, and named GaN/InGaN/AlGaN/Nitride regions. Actual SDE has 4×3nm In0.15Ga0.85N wells, five 22nm barriers, 26nm Al0.15GaN EBL, 120nm pGaN, 4µm nGaN + 0.3µm numerical base, 5nm physical left damaged strip plus artificial symmetry centerline. The design is half-domain with selective mesh coarsening. This is a literature-motivated 2D representative device, not verified replica of JBD.

## 2. Critical discrepancy: SDevice comments vs executed solve

Source header says segmented 0–4V Increment=1.2 then 4–5V Increment=1.05 and 'true Save checkpoints' at 4.0,4.5,4.8,5.0V. Source and preprocessed executable blocks **do NOT implement these promises**. They contain ONE 0–5V Transient (FinalTime=1, InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2), then ONE Save at 5V; stray comment says 'short 0–0.3V smoke' but Goal is 5V. No within-sweep saved intermediate TDRs/Save checkpoints are declared in these source files. This does NOT invalidate successful completion, but documentation and same-current spatial-coverage/checkpoint claims must be corrected BEFORE another long run.

## 3. Definitive effective 5 V quantum-well recombination parameters, extracted from actual TDR

For **each separate Clean and DmgL region of QW1–QW4** (the eight InGaN 2D regions), matched mesh vertex datasets were read: `eDensity`, `hDensity`, `RadiativeRecombination`, `srhRecombination`, `AugerRecombination`. With `n` and `p` in cm^-3, these per-point relations hold to numerical roundoff across all eight QW regions:

- `Rrad/(n*p) = 2.0e-10 cm^3/s`.
- `RAuger/[n*p*(n+p)] = 1.0e-30 cm^6/s`.
- `R_SRH*(n+p)/(n*p) = 1.0e9 s^-1` or equivalently `R_SRH = n*p/[1ns*(n+p)]` at this saved bias.

This provides direct numerical evidence that the **effective 5V solver field values** follow the uncalibrated vendor InGaN recombination parameters previously observed (radiative=2e-10, Auger=1e-30, SRH lifetime≈1ns), rather than merely verifying a parameter file was parsed. It does **not** prove these are experimentally calibrated In0.15Ga0.85N values, or that changing only SRH guarantees plausible light output. The previously independently observed four-QW Clean+DmgL 2D integration at 5V NtSide=0 yielded `Rrad=40072.8158452`, `RSRH=36562944.9075`, `RAuger=1599.706168587` [s^-1 µm^-1], so the modeled `Rrad/(sum)=0.1094747566%`. It is not measured or fully validated IQE/EQE.

## 4. Mg incomplete ionization: data-field interpretation clarified

Original `pp1_dvs.cmd`: `N_Mg_p=9.59e18 cm^-3`, `N_A_EBL=3e17`, `N_D_n=5e18`, `N_D_bar=1e15`. Region-specific `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")` on Clean_pGaN and DmgL_pGaN; the log confirms activation and custom GaN Mg `E_0=0.2eV`, `alpha=8e-9eV cm`, `g=4`, `Xsec=1e-14cm²`.

In the TDR, Clean_pGaN has 3,175 mesh-field values and DmgL_pGaN has 370. Across **all these matched records**, `-DopingConcentration = pMagnesiumActiveConcentration * TrapOccupation_pMagnesiumActiveConcentration(Ac,Le)` to <~3e-16 relative error. Max occupation 0.03128602892781 gives 9.59e18*0.03128603≈3.000330174e17 cm^-3 effective net acceptor at that location. Meanwhile exported `pMagnesiumMinusConcentration` is a **constant raw 9.59e18** across both regions. This name/dataset should NOT be interpreted on its own as proof Mg is fully ionized; actual net doping field is already reduced by calculated occupation. The model's **numerical consistency** is verified; external experimental Mg compensation/ionization model accuracy is NOT.

## 5. Terminal current and remaining critical gates

`n2_des.plt` has 1,023 samples, 17 data columns; final 5 V anode TotalCurrent `+1.44801646079583e-11` (SDevice 2D raw unit), anode hole component `+1.42020180788235e-11`, electron `+2.78143237811134e-13`; cathode total `-1.44801646079583e-11`. At approx 4.798 V total is `2.643189e-12`. The **standard assumed 2D A/µm and half-active-width≈2µm** conversion gives provisional 5V J≈7.24e-4 A/cm², but actual T-2022.03 width/AreaFactor convention has NOT been independently certified. Transient ramp completion is NOT rigorous steady-state validation, although final displacement current is much smaller than total current. High apparent SRH cannot be assigned to NtSide sidewall traps when 12 active DmgL traps have Conc=0.

Publication / full A/B broad sweep remains NO-GO pending material calibration evidence, realistic injection/J and polarization/band profile review, tested same-current intermediate TDR extraction, Full/Fine vs Half/Coarse error & mesh convergence, and matched-physics NtSide 0/1e18 controls.

## 6. Recommended next controlled experiment — PROPOSED ONLY

1. Preserve source/results and separately clone a `CMP_BASELINE_1.2.0_CAL` SWB branch; protect all prior work. No code edits or solver starts have occurred yet.
2. Before writing model .par, inspect local T-2022.03 official user guide and exact InGaN material parameter override section. Separate material-specific recombination from existing GaN Mg ionization/LatticeParameters/Thermionic definitions; avoid replacing the whole custom .par with a Silicon template or global blind values.
3. First controlled numerical sensitivity: **only InGaN SRH lifetime** (candidate 100ns vs current actual 1ns, possibly 10ns intermediate), held geometry, contacts, doping, polarization, Rrad/Auger, solver and NtSide=0 constant. 100ns is an explicitly documented *published simulation choice* in Baek et al., Nature Communications 2023 DOI 10.1038/s41467-023-36773-w, but it is a different 6-QW epitaxy and Silvaco simulation, not validated calibration for our 4-QW structure; do not market as experimentally fit. Kou 2019 DOI 10.1364/OE.27.00A643 is the morphology and sidewall-motivation reference. Do not alter user source until proposed numerical override is proven syntactically correct and scoped only to intended InGaN regions.
4. Verify active preprocessed .par and log, produce short **Transient BE** smoke, then run NtSide0 5V if numerical and physical checks pass. Add appropriate **intermediate spatial Plot/Save schedule** to permit same-current review; do not trust header promises.
5. Then NtSide=1e18 with identical calibration and numerical policy; compare full QW recombination and sidewall SRH at matched current, and validate Full/Half geometry + mesh separately before declaring final baseline.

Status: **AUDITED 5V reference / new version CANDIDATE NOT CREATED / NOT CALIBRATED / NOT RUN.**
