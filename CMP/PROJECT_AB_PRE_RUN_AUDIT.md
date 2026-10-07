# Project A/B Pre-Run Audit — Multi-day Simulation GO/NO-GO

Date: 2026-10-07  
Worker: 주수빈  
Status: **REVIEWED / NO-GO for production A/B until mandatory gates below pass**

## 1. Executive verdict

The current FAST_C1/Common Baseline is a valid parent candidate for Project A/B. The physical baseline does **not** need to be rebuilt.

Confirmed foundations:
- 4 um representative mesa, 5 nm DmgL/DmgR sidewall damage, Kou-based epitaxy, baseline Nt/Et/sigma and common contacts/physics are protected.
- FAST_C1 changes the golden v1.2 family numerically by adding transient-inner `Iterations=15`; the spatial intermediate Plot schedule is retained.
- FAST_C1 Node 6 has actually generated intermediate TDR snapshots at 4.0/4.2/4.4/4.6/4.7 V.
- Current files contain anode voltage and TotalCurrent, so same-current V extraction is possible.
- A/B fair-comparison principle is same injected current/current density, not same applied voltage.

However, **Project A/B production runs are currently NO-GO** until the mandatory pre-run gates below are completed. The reason is not a known fatal baseline physics defect; it is that several A/B-specific implementation and extraction items are not yet frozen or directly verified in the active preprocessed decks.

## 2. Mandatory common gate before any multi-day A/B run

### G1 — Active-deck provenance
Directly inspect the actual server files that will be run:
- preprocessed SDE: `pp1_dvs.cmd`
- preprocessed SDevice: `ppN_des.cmd`
- parameter file: `ppN_des.par`
- mesh: `n1_msh.tdr`

Do not use stale public `CMP/tcad/CURRENT/sdevice2_defect_on.cmd` as the production source.

Require:
- source/hash provenance recorded
- no unexpected absolute-path dependency
- T-2022.03 executable documented
- mesh/parameter revision identical to the intended parent baseline

### G2 — Common physics/output fields present in the active pp deck
Before long run, verify the active deck contains the fields required for later analysis:
- SRH recombination
- Radiative recombination
- Auger recombination
- electron/hole density
- electron/hole current (or equivalent current-density vector)
- conduction/valence band energy
- electric field
- electron/hole mobility
- doping / space charge
- polarization output needed for Project B interpretation
- Al mole fraction output for Project B
- trap concentration / trapped-charge or occupancy diagnostics needed for FAST/trap validation and Project A interpretation

Also verify:
- Thermionic/heterojunction treatment expected by the final v1.2 lineage is present in the actual active deck
- Mg incomplete ionization remains restricted to the intended p-GaN regions and is not reactivated globally in InGaN

### G3 — Same-current spatial-state coverage
The existing v1.2/FAST_C1 snapshot grid is:
4.0, 4.2, 4.4, 4.6, 4.7, 4.8, 4.85, 4.9, 4.925, 4.95, 4.975 V plus final 5.0 V.

This is sufficient only if the selected operating-current points map close enough to those saved voltages for Baseline/A/B.

Before production:
1. define target current/current-density operating points;
2. obtain Baseline V(I) / V(J);
3. estimate expected A/B voltage shift from pilot runs;
4. increase snapshot density if a target state could fall too far from the saved grid.

Do not assume a 5 V map is a valid same-current map.

### G4 — 2D current normalization
No explicit AreaFactor is present in the checked FAST_C1 pp cmd/par.

Standard Sentaurus 2D semantics use 1 um out-of-plane width by default, so terminal current is interpreted per 1 um width. For a 4 um planar mesa, the working conversion is:
`J = I_2D / (4 um × 1 um)`.

Before publication use:
- confirm this against the local T-2022.03 User Guide / installed environment;
- ensure no hidden electrode/global AreaFactor exists;
- define whether reported J uses full 4 um mesa area for Baseline, A and B.

Raw same-current comparison remains valid only when geometry and width normalization are treated consistently.

### G5 — Extraction workflow must be tested before long run
At least one already-existing Baseline intermediate TDR must be used to prove that the full post-processing chain works **before** A/B production:
- integrate total sidewall SRH
- integrate MQW Radiative
- integrate MQW Auger
- compute recombination-based IQE
- extract lateral carrier/current profiles
- compute current-crowding metric
- extract lateral Ec/Ev line
- obtain trap/polarization diagnostics where applicable

If the field is missing or the region selection is wrong, fix the output deck now, not after a multi-day A/B run.

## 3. Metric definitions to freeze now

Use the same definitions for Baseline, A and B.

### Sidewall recombination
Record at least:
1. total SRH integrated over all 5 nm DmgL + DmgR semiconductor regions;
2. active-stack sidewall SRH separately, so a design cannot look better merely by moving recombination into another sidewall layer.

### MQW recombination / IQE
Integrate over the complete physical QW volume remaining in the device:
- `Rrad_QW`
- `RSRH_QW`
- `RAuger_QW`

Working recombination IQE:
`IQE_rec = Rrad_QW / (Rrad_QW + RSRH_QW + RAuger_QW)`.

Also report:
- total integrated radiative recombination;
- QW-volume-normalized radiative rate where Project B changes active-region volume.

This prevents a narrower active QW volume from being mistaken for a pure confinement improvement.

### Injection/leakage
Recombination IQE alone is insufficient if a design changes injection efficiency.

Add:
- electron leakage/current after the MQW/EBL region relative to terminal current;
- optional hole-injection/current-balance metric.

This is especially important for Project B.

### Current crowding
Freeze one definition before DOE, e.g.
`C_J = Jmax / Javg`
over a specified lateral cut/region at the matched-current state.

## 4. Project A — Carbon high-resistance edge: required code before production

### A1 — Geometry
Add symmetric GaN region tags:
- `Cedge_L`
- `Cedge_R`

They must be immediately **inside** the 5 nm Dmg regions, not overlapping or replacing DmgL/DmgR.

First mechanism-screen location remains upper n-GaN directly below the MQW unless the team explicitly changes the hypothesis.

Parameterize at minimum:
- enable/disable A
- `w_C`
- vertical start/end or depth
- left/right symmetry

### A2 — Carbon physics
Do not reuse the baseline sidewall trap as the carbon model.

Parameterize from the beginning:
- carbon acceptor concentration `N_C,A`
- acceptor energy, nominal literature anchor near Ev + 0.9 eV
- electron/hole capture cross sections

Because GaN:C can self-compensate at high carbon concentration, reserve an optional donor/compensation parameter in the production code even if Stage-1 sets it to zero. This avoids structural code rewrites when Stage-2 compensation is tested.

Literature boundary:
- C_N deep acceptor near Ev+0.9 eV and semi-insulating GaN:C are literature-supported.
- exact localized microLED Cedge geometry is the project hypothesis.

### A3 — Mesh
Cedge is GaN next to GaN, so a material-interface rule alone may not refine its internal region boundary.

Add explicit region/window refinement at:
- Dmg/Cedge lateral boundary
- Cedge/Clean lateral boundary
- vertical top/bottom of the Cedge zone

Run SDE only first and inspect the mesh before SDevice.

### A4 — Required outputs
In addition to common outputs:
- trap charge/occupancy in Cedge
- e/h density in Cedge
- e/h mobility and electric field, so local conductivity can be reconstructed
- current density through Cedge and adjacent clean core

### A5 — Null control
Include an A-null case that retains the same region partition/mesh but disables carbon physics (`N_C,A=0` and optional donor=0).

The null case must reproduce the Baseline within numerical/mesh tolerance before attributing an effect to carbon.

## 5. Project B — localized AlGaN lateral heterobarrier: required code before production

### B1 — Geometry is not yet fully frozen
Add symmetric:
- `AlBarrier_L`
- `AlBarrier_R`

Parameterize:
- enable/disable B
- `w_Al`
- `x_Al`
- vertical start/end

**Mandatory scientific decision before coding the production DOE:** decide the exact vertical span.

A barrier that crosses the QW stack can replace part of the InGaN QW edge and therefore changes active QW volume in addition to producing a band barrier. That is a real design option, but it must be intentional and reflected in the IQE/radiative normalization.

Do not start a multi-day B run with an ambiguous vertical span.

### B2 — Heterojunction physics
Keep the common transport/recombination/polarization framework.

Verify in the actual pp deck:
- AlGaN material/mole fraction is correctly generated
- heterojunction transport treatment is active
- polarization model does not create an unintended lateral-interface artifact
- no artificial interface trap is added unless it is a separate study variable

### B3 — Mesh
Require explicit confirmation of mesh resolution at the new lateral GaN/AlGaN boundaries.

The existing GaN/AlGaN material-interface refinement may help, but do not assume it is sufficient. Generate the SDE mesh and inspect the new lateral interfaces before SDevice.

### B4 — Required outputs
In addition to common outputs:
- xMoleFraction
- ConductionBandEnergy / ValenceBandEnergy
- polarization vector/charge
- lateral electron/hole density
- lateral current density
- radiative distribution through all QWs

### B5 — Null control
Create a B-null configuration that preserves the intended region/mesh partition but removes the barrier effect as cleanly as the Sentaurus material setup allows.

The null-control strategy must be preprocessed and checked for absence of spurious heterointerface/polarization effects before using it as a baseline-equivalence test.

## 6. Run architecture recommended before the expensive DOE

### Mode 0 — Preprocess only
For Baseline/A/B:
- SDE build
- mesh inspection
- SDevice preprocess
- exact diff against the frozen parent

No long solve.

### Mode 1 — Short smoke
Use the same physics but a short low-bias endpoint/checkpoint to catch:
- region name errors
- missing material parameters
- trap syntax/material-scope errors
- heterojunction initialization errors
- output/TDR field omissions
- Save/Load failures

Do not treat smoke results as research data.

### Mode 2 — Representative pilot
Run one representative A case and one representative B case before the full DOE.

Measure:
- convergence/cutback behavior
- runtime
- V(I)
- whether target same-current snapshots are covered
- whether all extraction scripts work

### Mode 3 — Screening DOE
Only after pilot:
- use validated operating-current/bias window
- parameter points may run independently/in parallel
- keep the same physics and extraction definitions

### Mode 4 — Publication validation
Full reference / best / representative / worst cases:
- full protected endpoint as required
- mesh/convergence check
- same-current metrics
- full spatial mechanism evidence

## 7. Restart protection

The existing intermediate `Plot(-Loadable)` files are visualization snapshots, not validated restart checkpoints.

Before launching many multi-day A/B cases:
- complete the C2 Save/Load smoke;
- add true loadable Save checkpoints only after syntax/mechanics are proven in T-2022.03;
- verify that restart preserves state for the defect-on/trap case.

A/B production should not depend on an untested restart path.

## 8. Baseline validation still separate from code completeness

The Common Baseline source-of-truth lists additional publication gates:
- Nt sensitivity
- mesa-size sensitivity
- mesh convergence

These are scientific validation tasks, not proof that the A/B code contains the right outputs.

For schedule management, representative A/B pilots can only be promoted to publication evidence after the Baseline validation requirements relevant to the claimed conclusions are satisfied.

## 9. GO/NO-GO summary

### GO already
- Common physical parent concept
- NtSide=0 / 1e18 split concept
- same-current I-V extraction
- intermediate spatial snapshots in FAST_C1 lineage
- numerical C1 reference framework
- A/B causal hypotheses and fair-comparison metrics

### NO-GO until completed
1. active pp-deck audit (not stale GitHub CURRENT)
2. exact output-field/dataset verification on an existing TDR
3. tested region-integral/IQE/current-crowding/band-profile extraction
4. 2D current-density normalization final confirmation
5. Project A parameterized Cedge + explicit mesh + carbon physics + null control
6. Project B exact vertical-span decision + parameterized AlBarrier + interface mesh + null control
7. Save/Load checkpoint smoke for production robustness
8. representative A/B short pilot before any broad multi-day sweep

**Do not launch the broad A/B production sweep until all eight NO-GO items pass.**
