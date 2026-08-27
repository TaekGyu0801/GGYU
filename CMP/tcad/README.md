# CMP TCAD Backup

This directory tracks the reproducible, user-authored parts of the CMP Sentaurus TCAD work.

## Backup snapshot — 2026-08-27

A full server snapshot was archived locally as:

- `CMP_TCAD_BACKUP_20260827.tar.gz`
- SHA256: `c8bc05d0bbb86415859bddd544ccf2a8b5a8f8abdebb1ee9b571ae1b2371c3dc`
- Archive entries: 122
- Included server projects:
  - `~/CMP_P2_MG_CALIBRATION`
  - `~/CMP_P3_BASELINE_MICROLED`

The full archive is intentionally **not committed to this public repository** because the server projects contain Synopsys Sentaurus example/source material and generated files that may be governed by the Synopsys license. Keep the full `tar.gz` backup in private/local storage.

## Public reproducibility pack

```text
CMP/tcad/
├─ README.md
├─ BACKUP_MANIFEST_20260827.md
├─ P2_MG_CALIBRATION/
│  ├─ README.md
│  ├─ CALIBRATION_RESULTS.csv
│  ├─ equilibrium_mg_calibration_des.cmd
│  ├─ extract_hdensity.tcl
│  └─ extract_hdensity_n62.tcl
└─ P3_BASELINE_MICROLED/
   └─ README.md
```

## Current project sequence

1. P2 — p-GaN Mg incomplete-ionization calibration: complete.
2. P3 — official GaN PiN baseline reproduction: SDE + forward SDevice complete.
3. Next — create a clean baseline, then add InGaN/GaN MQW, then sidewall/SRV DOE.

## Important

Do not treat Synopsys example decks copied from the installed Applications Library as redistributable source code. This public repository stores project-specific results, user-authored scripts/decks, parameter values, node maps, and reconstruction notes instead.
