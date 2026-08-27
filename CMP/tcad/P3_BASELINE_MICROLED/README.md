# P3 — Baseline Micro-LED / GaN PiN Reproduction

## Purpose

Establish a known-good Sentaurus III-N baseline before introducing the project-specific clean Micro-LED structure, InGaN/GaN MQW, sidewall damage, SRV, wet-treatment, and ALD-passivation models.

## Starting point

The server project was initialized from the installed Synopsys Sentaurus Applications Library example:

```text
/user/tools/synopsys/sentaurus/T-2022.03/tcad/T-2022.03/Applications_Library/GettingStarted/sdevice/GaN_PiN_Diode
```

The working server directory was:

```text
~/CMP_P3_BASELINE_MICROLED
```

A frozen successful copy of the untouched reproduced example is preserved as:

```text
~/CMP_P3_BASELINE_MICROLED_ORIGINAL_OK
```

A second frozen successful checkpoint containing the calibrated Mg model is preserved as:

```text
~/CMP_P3A_MG_BASELINE_OK
```

Its `n2_des.sta` records the Forward SDevice node as `done`.

## SWB node map

From `gtree.dat`:

```text
node 1 = SDE
node 2 = Forward SDevice
node 3 = Forward SVisual
node 4 = Reverse SDevice
node 5 = Reverse SVisual
```

## Verified original run status — 2026-08-27

- Node 1 / SDE: completed successfully with `exit(0)`.
- Node 2 / Forward SDevice: completed successfully with `exit(0)`.
- Forward SDevice wall-clock observed through gsub: approximately 176 s.
- Final SWB/SDevice status file recorded the job as `done`.

The original forward deck sweeps the anode from 0 V toward +10 V using a slow transient solution and includes III-N physics such as incomplete ionization, polarization, SRH, Auger, radiative recombination, and GaN/Nitride interface traps.

## P3A — calibrated Mg inserted into the reproduced GaN PiN

The first project-specific change was deliberately limited to the p-side Mg model so that failures could be isolated before removing passivation/interface-trap physics.

### SDE change

```text
PDopantActiveConcentration 1e19
→
pMagnesiumActiveConcentration 9.59e18
```

The actual preprocessed SDE deck (`pp1_dvs.cmd`) was checked and contained:

```text
pMagnesiumActiveConcentration 9.59e18
```

Other doping remained:

```text
i-side: NDopantActiveConcentration 1e15
n-side: NDopantActiveConcentration 1e19
```

### Mg incomplete-ionization parameters

The P2 calibrated model was transferred into `sdevice.par`:

```text
Species ("pMagnesiumActiveConcentration") {
  E_0   = 0.2
  alpha = 8e-9
  g     = 4.0
  Xsec  = 1e-14
}
```

The n-type species was kept unchanged.

### P3A run result

- Node 1 / SDE: `done: exit(0)`.
- Node 2 / Forward SDevice: `done: exit(0)`.
- gsub total run time: approximately 203 s.
- SDevice-reported wallclock: approximately 198.36 s.
- Final sweep reached `anode = 10.0 V` and finished with `Curve trace finished.`
- Final 10 V current reported by the log:
  - anode electron current: `2.239e-01 A`
  - anode hole current: `8.354e-03 A`
  - anode total current: `2.323e-01 A`
- Final plot `n2_des.tdr` written successfully.

This verifies that the P2 calibrated Mg concentration and incomplete-ionization model can be inserted into the reproduced GaN PiN structure without breaking the forward solution.

## P3B — clean GaN PiN baseline without original Nitride/interface trap

P3B removes the original example's Nitride passivation and `GaN/Nitride` interface-trap block while keeping the calibrated Mg model from P3A.

To preserve the mesa-cutting geometry operation without retaining a physical Nitride region, the original cutting polygon was temporarily changed to a `Gas` region named `tmp_mesa`, then deleted immediately after the Boolean geometry operation. Nitride-specific mesh refinement and offset rules were removed.

The actual preprocessed SDE deck was checked and contained:

```text
Gas "tmp_mesa"
delete-region ... "tmp_mesa"
pMagnesiumActiveConcentration 9.59e18
```

No `Nitride` or `Passivation` entry remained in the checked preprocessed SDE deck. The Forward SDevice deck also no longer contained `Physics(MaterialInterface="GaN/Nitride")` or its interface trap.

### P3B run result

- Node 1 / SDE: `done: exit(0)`.
- Node 2 / Forward SDevice: `done: exit(0)`.
- gsub total run time: approximately 86 s.
- SDevice-reported wallclock: approximately 80.63 s.
- Final sweep reached `anode = 10.0 V` and finished with `Curve trace finished.`
- Final 10 V current reported by the log:
  - anode electron current: `2.020e-01 A`
  - anode hole current: `8.298e-03 A`
  - anode total current: `2.103e-01 A`
- Final plot `n2_des.tdr` written successfully.

Compared with P3A at 10 V, the total current changed from `0.2323 A` to `0.2103 A`, a decrease of about `0.0220 A` or `9.47%`.

This comparison is useful as a checkpoint, but it should not yet be interpreted as a direct physical passivation benefit/penalty because P3A and P3B differ in both the presence of the Nitride region and the GaN/Nitride interface-trap model. P3B is the intended clean electrical reference for later MQW and sidewall/SRV work.

## Important interpretation

- Original example: reproduced Synopsys GaN PiN with original Nitride/interface physics.
- P3A: calibrated Mg + original Nitride/interface physics.
- P3B: calibrated Mg + clean bare-GaN reference without original Nitride/interface trap.

P3B is now the preferred baseline for the next structure-development step.

## Next modification sequence

1. Preserve the original verified reproduction state.
2. Preserve P3A as the verified `calibrated Mg + original passivation/interface` checkpoint.
3. Preserve P3B as the verified clean GaN PiN checkpoint.
4. Add InGaN/GaN MQW to the clean baseline.
5. Add polarization/heterointerface refinements only after the MQW baseline is stable.
6. Add sidewall/SRV and pixel-size DOE.
7. Map wet-treatment / ALD healing to reduced sidewall defect activity.

## Source-code policy

The actual Synopsys example input decks and generated outputs are retained in the user's private/local full backup and are intentionally not copied into this public repository. This file records the source location, node mapping, verified status, and project-specific modifications without redistributing licensed example material.
