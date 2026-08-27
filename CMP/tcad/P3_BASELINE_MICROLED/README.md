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

## SWB node map

From `gtree.dat`:

```text
node 1 = SDE
node 2 = Forward SDevice
node 3 = Forward SVisual
node 4 = Reverse SDevice
node 5 = Reverse SVisual
```

## Verified run status — 2026-08-27

- Node 1 / SDE: completed successfully with `exit(0)`.
- Node 2 / Forward SDevice: completed successfully with `exit(0)`.
- Forward SDevice wall-clock observed through gsub: approximately 176 s.
- Final SWB/SDevice status file recorded the job as `done`.

The original forward deck sweeps the anode from 0 V toward +10 V using a slow transient solution and includes III-N physics such as incomplete ionization, polarization, SRH, Auger, radiative recombination, and GaN/Nitride interface traps.

## Important interpretation

This official example is **not yet the clean project baseline**. In particular, the copied structure already contains Nitride passivation and a GaN/Nitride interface-trap model. Those features must not be mistaken for the project's final sidewall/passivation condition.

## Next modification sequence

1. Preserve this verified reproduction state.
2. Build a clean GaN PiN baseline.
3. Apply the P2 calibrated p-GaN Mg target (`NMg = 9.59e18 cm^-3`).
4. Use the calibrated Mg incomplete-ionization parameters.
5. Add InGaN/GaN MQW.
6. Add polarization/heterointerface refinements only after the simpler baseline is stable.
7. Add sidewall/SRV and pixel-size DOE.
8. Map wet-treatment / ALD healing to reduced sidewall defect activity.

## Source-code policy

The actual Synopsys example input decks and generated outputs are retained in the user's private/local full backup and are intentionally not copied into this public repository. This file records the source location, node mapping, verified status, and project-specific next steps without redistributing licensed example material.
