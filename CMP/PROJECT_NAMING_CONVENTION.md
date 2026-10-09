# CMP TCAD Project Naming and Versioning Convention

Status: CONFIRMED (naming policy only)  
Approved by: 이택규  
Adopted: 2026-10-09

## 1. Standard format

`CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>`

- `CMP`: the shared research project.
- `TYPE`: simulation/device family, e.g. `BASELINE`, `PROJECTA`, `PROJECTB`. Use uppercase ASCII without spaces.
- `MAJOR.MINOR.PATCH`: three dot-separated nonnegative integer version components. No redundant `v` or `V1` suffix.
- `TAG`: short uppercase ASCII description of what this branch changes (e.g. `REF`, `CAL`, `CEDGE`, `ALBARRIER`, `MESH`).

### Designated next candidate

`CMP_BASELINE_1.2.0_CAL`

This is an **intended new, independent literature-calibration test candidate**, not an existing SWB folder or scientifically validated baseline. The parent is the completed `JUSUBIN_FAST_HALF_5V_TEST` Half+Coarse NtSide=0 result. Do not rename/edit the old project or claim `CAL` means calibration has already been proven.

Possible future project names (examples, not created):
- `CMP_BASELINE_1.2.1_CAL`: patch-only correction that leaves intended numerical physics/result unchanged
- `CMP_BASELINE_1.3.0_CAL`: meaningful physics/parameter model revision or extra capability
- `CMP_PROJECTA_1.0.0_CEDGE`: first independently versioned Project A carbon-edge candidate
- `CMP_PROJECTB_1.0.0_ALBARRIER`: first independently versioned Project B AlGaN barrier candidate

## 2. Meaning of the version

- **MAJOR**: incompatible or fundamental changes in device geometry/epitaxy, core physical formulation, or scientific comparison definition, as assessed and documented.
- **MINOR**: meaningful but compatible modeled physics/parameter calibration, new physical mechanism, numerical-mesh/solver methodology changes requiring equivalence validation, or additional simulation capability. Recheck results; do not assume equivalence.
- **PATCH**: nonphysical corrections (file paths, metadata, naming, documentation, plot/extraction bug *only if verified not to change numerical results or scientific interpretation*). If a small change materially changes results, assign at least MINOR, and MAJOR if incompatible.

The version describes *declared changes*, not simulation quality. A high version number does not imply successful convergence, physical calibration or publication approval.

## 3. Independent lineages and provenance

- Compare versions **within the same TYPE** (e.g. BASELINE 1.3.0 succeeds BASELINE 1.2.1). Do not use version numbers alone to rank chronology or quality *across* BASELINE/PROJECTA/PROJECTB.
- Each new Project A/B lineage must record `PARENT_PROJECT`, parent revision/commit or SHA-256 of actual private input, `CHANGED_FILES`, exact physical parameter changes, state `PROPOSED/OBSERVED/CONFIRMED`, validation status, and date.
- The older SDevice source labeled `v1.2` is historical **deck-specific provenance** and must not automatically be treated as proof of the new project's semantic-version ancestry. Explicitly map source hashes and parent files.
- `NtSide=0` and `NtSide=1e18` are run/split conditions, not different code versions when all code is identical. Keep these conditions, bias, mesh, calibrated-parameter hash, date and run/job ID with results (for example in metadata or result folders) rather than inflating project versions.
- Preserve the existing Full/Fine FAST_C1 reference, completed `JUSUBIN_FAST_HALF_5V_TEST` and `JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz`. Do not rename or remove them to fit the new naming convention.
- A new project name must be checked for valid usage in the local SWB before committing to long jobs; naming changes never justify an unverified simulation.
- Actual proprietary Sentaurus scripts, output logs and MaterialDB copies must not be uploaded to the public GitHub; share private sources directly in the conversation when necessary.

## 4. New Baseline candidate preparation gate

Before any `CMP_BASELINE_1.2.0_CAL` code change or new 5 V run:
1. Inspect exact existing private `sde_dvs.cmd`, `sdevice_des.cmd`, `FASTC1_pp6_des.par`, `pp1_dvs.cmd`, `pp2_des.cmd`, `n1_msh.tdr`, `n2_des.log`, `n2_des.plt`, `n2_des.tdr`.
2. Validate effective InGaN recombination/material coefficients and 2D electrical current/AreaFactor/injection; do not tune to a chosen IQE.
3. Create only a separately named candidate; keep geometry/doping and successful Transient BE recipe unless justified.
4. Run preprocess and short smoke before NtSide=0/1e18 5 V pilot.
5. Keep Full-vs-Half+Coarse equivalence and physical model validity as publication prerequisites.
