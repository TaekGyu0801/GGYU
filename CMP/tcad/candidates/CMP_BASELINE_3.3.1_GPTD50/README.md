# CMP_BASELINE_3.3.1_GPTD50: independent full candidate bundle
Worker: JuSubin, 2026-11-19. Status: PROPOSED / NOT RUN on school Sentaurus T-2022.03.
**NOT verified byte-for-byte against the school successful Wu10um 5nm baseline.** Do not overwrite it.
Parent source: public repo GPT-authored Wu3.2 candidates. This is not the last finalized school SVisual, which remains unavailable.
Files in this candidate: sde_dvs.cmd; sdevice_des.cmd; sdevice.par; svisual1_iv.tcl; svisual2_maps.tcl.
Only intended SDE physical change relative to Wu3.2 is bilateral Wdmg 0.005→0.050 um, width Wm10um, preserving all 22 existing Dmg trap region names/physics and GaN QB8nm.
SDevice has macros NtSide=1e18, Vstop=5, TrapEt=0.75, TrapSigmaN=1e-15, TrapSigmaP=1e-15. **These must be created in SWB parameter columns.** Parameter editor must point to sdevice.par.
Flow: SDE -> SDevice, then BRANCH SVisual1 and SVisual2 DIRECTLY from SDevice so @previous@ refers to actual SDevice in both. Do not chain SVisual2 after SVisual1.
SVisual1 outputs both raw 2D IV and provisional normalized J based on ASSUMED A/um, AreaFactor1. Do NOT call J calibrated until log/area verified.
SVisual2 loads n@previous@_des.tdr from previous SDevice and can fail if actual filename/layout differs; validate PP output and predecessor mapping.
Mesh: original Ref.Edge 1nm/0.5nm lateral applied across 50nm instead of5nm; SDE element count may be big. Check mesh and 3nm QWs before SDevice.
**D50 1e18** means 10x nominal trap areal inventory vs original D5/1e18, not a calibrated actual 10um etch depth. First run only D50 reference 5V; A-D50 and B-D50 clones only from successful SAME D50; matched-current comparisons mandatory.
Important: these are **ready to paste as separate SWB editors**, not a guarantee of target-solver valid code, successful simulation, true Wu source fidelity, or confirmed actual final school baseline. Do not upload private proprietary school code or vendor manuals to public repo.
