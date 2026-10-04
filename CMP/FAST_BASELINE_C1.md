# FAST_BASELINE C1 — reviewed implementation record

Status: **PROPOSED / REVIEWED / NOT EXECUTED**  
Worker: Lee Taek Gyu  
Implementation author: Claude  
Review: ChatGPT, 2026-10-04

## Golden reference

- Copy x8 editable SDevice source SHA-256:
  `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`
- Claude FAST C1 source SHA-256:
  `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`
- Public GitHub does **not** store the full Sentaurus source.

ChatGPT rechecked the attached files. The golden source hash and FAST C1 hash match the package claims.

## Executable change

After removing comments, blank lines and formatting, the only executable change versus Copy x8 is:

```diff
-Coupled {
+Coupled (
+Iterations = 15
+) {
 Poisson
 Electron
 Hole
```

Physics, sidewall traps, Math convergence tolerances, ILS settings, transient step controls, 5 V goal, and spatial Plot schedule are otherwise unchanged at statement level.

Claude C1 and the earlier ChatGPT FAST v0.1 candidate are also executable-statement equivalent. Their different SHA-256 values come from comments/formatting, including `Coupled(` versus `Coupled (`. C1 is the canonical candidate going forward.

## Review of Iterations=15

The first-candidate direction is technically reasonable.

Synopsys Sentaurus Training (copyright 2022) states that for Quasistationary/Transient:
- `Iterations` is the maximum Newton iteration count per step;
- the documented default is 20;
- usually 3–6 iterations are sufficient;
- if convergence is not found after about 15–20 iterations, it is often faster to fail the step and retry at a smaller step size;
- `Coupled(Iterations=15){...}` is a supported pattern.

Therefore `Iterations=15` is a defensible first numerical-only candidate.

However, CMP records also describe failed high-bias attempts reaching about 50 Newton rows/iterations. That conflicts with the documented default 20 when the golden source leaves the transient inner Coupled `Iterations` unset.

**This 20-vs-50 discrepancy is UNRESOLVED.** Do not infer that Copy x8 has a default limit of 50. Before launching C1, inspect the exact preprocessed x8 deck and raw x8 log.

## Mandatory B0 gate before C1 run

B0 does not run a new simulation.

First inspect the exact x8 preprocessed numerical settings:

```bash
grep -n -i "Iterations\|RHSMin\|CheckRhsAfterUpdate\|NotDamped" pp6_des.cmd
```

Then analyze a copied x8 `n6_des.out` using the Claude-provided `sdevice_newton_audit.py`, but verify the parser against raw log lines on its first use.

B0 must answer:
1. What is the actual/effective Newton cap in x8?
2. Are any **accepted** x8 steps above 15 Newton iterations?
3. Does the reported ~50 count really represent Newton iterations?
4. How much wallclock is actually spent in rejected attempts?
5. What do the final RHS and error columns do in the stalled attempts?

Decision:
- no accepted step needs >15 and raw-log parsing is verified → C1 `Iterations=15` may proceed;
- accepted steps need >15 → raise the cap based on the observed distribution before running;
- 50-iteration interpretation is wrong → recompute the expected speedup before running.

## Scientific boundary

C1 does **not** loosen Digits/ErrRef/RHSMin or change physical models. This means it does not directly relax the local convergence criteria.

It does **not** guarantee an identical physical solution. Earlier cutback can change the accepted time-step/bias trajectory. Physical/numerical equivalence must still be measured.

Do not modify:
- geometry / vertical epitaxy;
- 4 um representative mesa;
- 5 nm sidewall damaged width;
- NtSide / Et / capture cross sections;
- contacts;
- SRH / Radiative / Auger;
- transport framework;
- polarization / heterojunction physics;
- Mg incomplete-ionization region scope;
- 0 to 5 V endpoint.

Live Copy x6/x7/x8 directories remain untouched. Do **not** stop x7 merely to make room for C1. If compute-resource pressure becomes a real blocker, re-check the live process state and make a separate researcher-approved decision.

## Preprocess gate

Before any full C1 solve:
- new separate Workbench project/copy;
- verify FAST source hash;
- preprocess;
- verify `pp1_dvs.cmd`;
- verify `pp<N0>_des.par`;
- compare normalized `pp<N0>_des.cmd` against golden `pp6_des.cmd`;
- verify exactly one intended `Iterations=15` insertion;
- verify all intended NtSide substitutions;
- verify mesh hash or semantic mesh statistics.

Golden reference hashes:
- `n1_msh.tdr`: `762d2d57a352a00bb030b968985cbf3b71d53118c68e5c53b7586e613f392ea3`
- `pp1_dvs.cmd`: `5685528bc3ec338ce104040b0503be43ef032094976d69995529eb5d6fb4e658`
- `pp6_des.cmd`: `2dfcc98effe145ec944fb8ee5d6914f5f098e54d1bf2319c69acc76afe1692e6`
- `pp6_des.par`: `60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039`

Known reference mesh statistics:
- 138137 vertices
- 274946 elements
- 41 regions reported in the C1 package guide; confirm against the actual reference log when B0 evidence is collected.

## Acceptance criteria — provisional

Accuracy/equivalence is mandatory; speedup alone cannot validate C1.

Initial engineering targets from the Claude package:
- same-voltage high-bias current relative difference: <= 1e-3;
- |Delta Vf| at matched current: <= 1 mV;
- integrated snapshot quantities target: <= 1e-3;
- bottleneck speedup >= 2x: strong accept for runtime;
- 1.2x to 2x: conditional/useful, continue diagnosis;
- <1.2x: ineffective as a runtime optimization.

ChatGPT review:
- I-V <= 1e-3 and |Delta Vf| <= 1 mV are reasonable **provisional strict targets**.
- The integrated spatial <= 1e-3 threshold may be too strict before baseline repeatability and same-current interpolation error are measured. Treat it as provisional, not a universal scientific cutoff.
- Runtime thresholds are engineering prioritization thresholds, not proof of numerical correctness.
- Final tolerances should be substantially smaller than the smallest Project A/B effect the paper intends to interpret.

## Package tool review

Claude package provides:
- `fast_preprocess_check.py`
- `sdevice_newton_audit.py`
- `plt_compare.py`

ChatGPT sandbox checks:
- all three pass Python syntax compilation;
- `sdevice_newton_audit.py --selftest` passes on its synthetic log;
- `plt_compare.py --selftest` passes on its synthetic DF-ISE file;
- none has yet been validated against the actual semi437 x8 SDevice log/PLT format.

Therefore the tools remain **PROPOSED**. The raw x8 log must be used to validate the parser before any B0 conclusion is accepted.

Package hashes:
- `fast_preprocess_check.py`: `9dce0e82948c60785e6c83c7a195b03e6e7cdd011926c0ea2b5ae8ff75dc08d9`
- `sdevice_newton_audit.py`: `fe546166c589c5302b8abaabf7d3be0479ed476281df33ccbbab17143022ee02`
- `plt_compare.py`: `d12fcfef0b3c07a006dc6db1c950c9ac5fc4d29787a25889205d08b96cc2b5a1`

The full proposed tools are not treated as verified production tools until actual-format validation.

## Immediate next action

1. Copy the live x8 `pp6_des.cmd` and `n6_des.out` to a safe analysis location.
2. Run B0 read-only audit.
3. Manually verify the parser against raw lines.
4. Resolve the documented default-20 versus recorded ~50-iteration discrepancy.
5. Confirm or revise `Iterations=15`.
6. Only then create/preprocess the separate `GaN_PiN_Diode_FAST_C1` project and run NtSide=0 first.
