# External GaN / MicroLED TCAD input-deck audit (2026-10-10)
Worker: 이택규. Status: LITERATURE / PUBLIC SOURCE AUDIT, NOT a successful replication. No school server code or running simulations changed.

## Main finding
A public **fully reproducible Synopsys Sentaurus InGaN/GaN multi-quantum-well MicroLED with lateral 5 nm sidewall defect, 2D SDE source, SDevice .cmd, appropriate InGaN/GaN .par, and calibrated I–V/IQE** was **not verified** in the repositories/pages inspected. This is a search-result boundary, NOT proof none exists anywhere. Do not claim MOSFET/Silicon/solar-cell decks are reusable LED physics.

## Priority A — vendor-provided GaN cases
1. Sentaurus Device training Chapter 16: https://ghzphy.github.io/Sentaurus_Training/sd/sd_16.html . Section 16.8 actual GaN p-i-n example with forward/reverse bias and SDE mesh. Section 16.6 numeric parameters and ILS, Section 16.2 GaN/AlGaN/InGaN MaterialDB location (`$STROOT/tcad/$STRELEASE/lib/sdevice/MaterialDB/`). This is closest available **Sentaurus III-nitride diode example**, but no MQW/5nm sidewall defect and material files may be licensed. Training mirror links source command viewing and actual installed Applications_Library likely best version-compatible option.
2. Silvaco vendor 2023 optical LED slides: https://silvaco.com/wp-content/uploads/content/presentations/Optical_Web-V1.0.pdf . `Blue_GaN_uLED_10Acm-2.str` example output, QW carrier density, SRH/current flowlines; evidence a vendor simulation exists, NOT that its ATLAS source deck or parameter file is public. Silvaco syntax is incompatible with Sentaurus.
3. Silvaco blue SQW LED `ledex01` tutorial copied/analyzed at https://icode.best/i/28115428358090 . Shows GaN/InGaN/AlGaN geometry/doping/mesh, optical recombination model, 1ns SRH, material values; belongs to Silvaco ATLAS, not Sentaurus, and blue **single** QW not our MQW. Respect upstream example copyright.
4. Baek et al., Nature Communications 14, 1386 (2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC10023660/ . 10x10um^2 fabricated microLED, Silvaco MQW numerical results; article **explicitly states that code is not publicly available because it includes proprietary Silvaco base code**. Exposed research-method *parameters* include effective interface polarization=50% theory, surface recombination velocity 1e5cm/s, SRH lifetime=100ns, B=1e-10cm^3/s, C=1e-31cm^6/s. Do not copy as calibrated parameters for our different geometry.
5. Le Maitre et al., JSID (2024): https://doi.org/10.1002/jsid.2012 . Silvaco quasi-3D half cylindrical GaN microLED/microPD; relevant evidence for half-structure speed strategy, different physical geometry from 2D Cartesian planar half.

## Priority B — publicly readable Sentaurus command files but NON MicroLED
A. https://github.com/fenning-research-group/sentaurus_ddd
   - [sde_dvs.cmd](https://github.com/fenning-research-group/sentaurus_ddd/blob/master/sde_dvs.cmd)
   - [sdevice_dark_des.cmd](https://github.com/fenning-research-group/sentaurus_ddd/blob/master/sdevice_dark_des.cmd)
   - [sdevice_light_des.cmd](https://github.com/fenning-research-group/sentaurus_ddd/blob/master/sdevice_light_des.cmd)
   - [sdevice.par](https://github.com/fenning-research-group/sentaurus_ddd/blob/master/sdevice.par) & [models.par](https://github.com/fenning-research-group/sentaurus_ddd/blob/master/models.par) (CAUTION: sampled models.par contains explicit proprietary Synopsys copyright; do **not** duplicate/relicense).
   - Silicon solar cell; e.g. SDevice `Extrapolate`, `Method=ParDiSo`, `Quasistationary`; not GaN or MQW. Useful File/Plot/solver structure only.
B. https://github.com/Alisama20/MOSFET-TCAD-Sentaurus
   - [sde_dvs.cmd](https://github.com/Alisama20/MOSFET-TCAD-Sentaurus/blob/master/sentaurus/sde_dvs.cmd), [sdevice_op_des.cmd](https://github.com/Alisama20/MOSFET-TCAD-Sentaurus/blob/master/sentaurus/sdevice_op_des.cmd), [sdevice_idvg_des.cmd](https://github.com/Alisama20/MOSFET-TCAD-Sentaurus/blob/master/sentaurus/sdevice_idvg_des.cmd), [sdevice_idvd_des.cmd](https://github.com/Alisama20/MOSFET-TCAD-Sentaurus/blob/master/sentaurus/sdevice_idvd_des.cmd), [mos_models.par](https://github.com/Alisama20/MOSFET-TCAD-Sentaurus/blob/master/sentaurus/mos_models.par), [REPRODUCIR.sh](https://github.com/Alisama20/MOSFET-TCAD-Sentaurus/blob/master/sentaurus/REPRODUCIR.sh).
   - 2D Si MOSFET, 2026, different release X-2025.09, code includes operating-point TDR and `Quasistationary`; not calibrated for T-2022.03 or GaN.
C. https://github.com/ananthakrishnan754/sentaurus-tcad-pn-diode
   - [sdevice_des.cmd](https://github.com/ananthakrishnan754/sentaurus-tcad-pn-diode/blob/main/sdevice/sdevice_des.cmd), [sdevice_dark_des.cmd](https://github.com/ananthakrishnan754/sentaurus-tcad-pn-diode/blob/main/sdevice/sdevice_dark_des.cmd), [sdevice_opt_des.cmd](https://github.com/ananthakrishnan754/sentaurus-tcad-pn-diode/blob/main/sdevice/sdevice_opt_des.cmd).
   - PIN photodiodes Si/Ge/GaAs/SiC, not GaN, shows Solve/Save logic but no LED physics.
D. https://github.com/sai1999gaurav/TCAD-Sentaurus-simulation
   - [pn_sde_dvs.txt](https://github.com/sai1999gaurav/TCAD-Sentaurus-simulation/blob/master/pn_sde_dvs.txt), [pn_sdevice_des.txt](https://github.com/sai1999gaurav/TCAD-Sentaurus-simulation/blob/master/pn_sdevice_des.txt); simple PN / transistor learning materials only.
E. https://github.com/rayid-mojumder/Sentaurus-TCAD-Modeling-and-Simulation (MIT educational MOSFET).
F. https://github.com/soybeanmilk0514-jpg/TCAD-MicroLED-Sidewall-Carrier-Confinement — teammate repo, **not an independent published validated MicroLED**, current public `source/` contains only README; CMP shared docs duplicate. Do not count as external verification.
G. https://github.com/nextnano-GmbH/nextnanopy-community-examples plus https://nextnano.com/nextnano3/tutorial/1Dtutorial11.htm — relevant GaN polarization/quantum heterostructure examples in another solver; **not directly executable Sentaurus .cmd/.par**.

## Runtime diagnosis from actual CMP history
Last GitHub verified school-server record (~22:30 KST): `JUSUBIN_FAST_HALF_5V_TEST` finished to 5V Oct9, but tiny nominal J~7.24e-4 A/cm2 remains **Gate0 unresolved**. Separate `CMP_BASELINE_1.2.0_CAL` 100ns InGaN *SRH lifetime* study has saved near-4V PLT current 3.497895e-14 A/um at 3.99967374V; latest recorded ~4.14965V with 4.839436e-14 A/um. Nonlinear Newton oscillation observed past 4.149V; later run status unknown. 100ns parameter IS NOT numerical timestep. Public stale `CMP/tcad/CURRENT/sdevice2_defect_on.cmd` uses `Transient(MaxStep=1e-3)`, `ExtendedPrecision(80)`, `Blocked+ILS`, 4 threads. **Must inspect live `pp2_des.cmd/par` before attributing active run slowdown to these precise entries.**

For a 1s ramp, if the actual deck used MaxStep=1e-3s, then a complete sweep needs at least 1s / 1e-3s = **1000 accepted steps**, not counting adaptive cutbacks/retries. At t~0.829862s an accepted step only 3.883e-6s was recorded; an attempted next step showed RHS oscillation. This suggests cutbacks/nonlinear difficulty may dominate high bias. Do not present an untested change as a guaranteed speedup.

## Next — READ ONLY active comparison
```bash
P=/user/semi/semi437/tmp/myproject/CMP_BASELINE_1.2.0_CAL
grep -nEi 'Transient|Quasistationary|InitialStep|MinStep|MaxStep|Increment|Iterations|ExtendedPrecision|Method|SubMethod|RHSMin|Digits' "$P/pp2_des.cmd" | tail -n 75
tail -n 65 "$P/n2_des.log"
ls -lh "$P"/pp2_des.par "$P"/n2_des.plt "$P"/n2_des.log
```
Do NOT interrupt running solver. After reading actual `Math/Solve`, compare with version-matched GaN p-i-n example rather than MOSFET defaults. Gate 0 low J and required same-current IQE extraction remains separate; don't equate faster convergence to physical validity.

## Scientific/software rights
Avoid publishing commercial/vendor proprietary PDF, material DB or code through CMP public GitHub. Store links + paraphrase and use installed licensed software/existing internal manual to verify syntax. Cross-simulator material coefficients/syntax are not interchangeable.
