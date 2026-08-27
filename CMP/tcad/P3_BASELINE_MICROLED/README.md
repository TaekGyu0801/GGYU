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

## Important interpretation

P3A is **still not the clean project baseline**. The copied structure still contains Nitride passivation and a GaN/Nitride interface-trap model. Those features must not be mistaken for the project's final sidewall/passivation condition.

## Next modification sequence

1. Preserve the original verified reproduction state.
2. Preserve P3A as the verified `calibrated Mg + original passivation/interface` checkpoint.
3. Remove/exclude the original Nitride passivation and GaN/Nitride interface trap to establish a clean GaN PiN reference.
4. Re-run SDE and Forward SDevice and compare against P3A.
5. Add InGaN/GaN MQW.
6. Add polarization/heterointerface refinements only after the simpler baseline is stable.
7. Add sidewall/SRV and pixel-size DOE.
8. Map wet-treatment / ALD healing to reduced sidewall defect activity.

## Source-code policy

The actual Synopsys example input decks and generated outputs are retained in the user's private/local full backup and are intentionally not copied into this public repository. This file records the source location, node mapping, verified status, and project-specific modifications without redistributing licensed example material.
