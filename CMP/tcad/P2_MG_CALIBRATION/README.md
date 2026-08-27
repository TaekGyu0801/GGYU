# P2 — p-GaN Mg Calibration

## Objective

Calibrate Mg concentration in p-GaN at 300 K so that the equilibrium free-hole concentration is approximately:

`hDensity = 3.0e17 cm^-3`

with incomplete ionization enabled.

## Final calibrated result

- Target hole concentration: `3.00000000000e17 cm^-3`
- Calibrated Mg concentration: `9.59e18 cm^-3`
- Simulated hole concentration at X = 0.05: `3.00033017418e17 cm^-3`
- Relative deviation from target: approximately `+0.011%`
- Temperature: `300 K`

## Mg incomplete-ionization model used

```text
Species ("pMagnesiumActiveConcentration")
type  = acceptor
E_0   = 0.2 eV
alpha = 8e-9
g     = 4
Xsec  = 1.0e-14
```

## Verified calibration points

See `CALIBRATION_RESULTS.csv`.

Key points:

- `5.0e18 cm^-3` → `2.02293281515e17 cm^-3`
- `9.59e18 cm^-3` → `3.00033017418e17 cm^-3`
- `9.75e18 cm^-3` → `3.03103549868e17 cm^-3`
- `1.0e19 cm^-3` → `3.07868172959e17 cm^-3`

## Important debugging note

The SWB parameter tree did not reliably persist the attempted `9.75e18` value. The calibration was therefore verified using the preprocessed SDE deck (`pp6_dvs.cmd`) and, for final points, the Mg concentration was temporarily hardcoded in the SDE input. Always confirm the actual value used in the preprocessed file before interpreting a run.

For the final point, the preprocessed deck contained:

```text
pMagnesiumActiveConcentration = 9.59e18
```

## Execution mapping used during final calibration

For the branch used to generate the final `n62` result:

- SDE: node 6
- SDevice: node 62
- SVisual extraction input: `n62_des.tdr`

The extraction script samples the mesh point closest to `X = 0.05`.

## Public-repo source policy

The original project also contains licensed Synopsys material/model files and generated output. Those files remain in the private/local full archive and are not duplicated into this public repository. The equilibrium SDevice deck and extraction scripts in this folder are project-authored calibration artifacts.
