# CMP_PROJECTB_2.0.0_QB6 — D50 GaN quantum-barrier 6nm screening pilot

Status: PROPOSED / SCHOOL UNRUN. Owner: 주수빈. Parent: GitHub unrun CMP_BASELINE_3.3.1_GPTD50. School-successful Claude D50 source not yet accessible; this is a reference, not a verified clone.
- Change exactly one numerical physical geometry variable in SDE: `tQB=0.008` -> `0.006` um, affecting all five GaN Barriers0..4.
- Unchanged: each 3nm InGaN QW (4 total), In fraction0.08, pGaN120nm, nGaN3.9um, nGaN Si5e18, pGaN active Mg2e19, barrier background NBg1e15, EBL0, left/right damage50nm, 22 Dmg Trap regions, physics, traps, SDevice Math/Solve, 300K 5V.
- Calculated x boundaries [um] from p-face: pGaN 0..0.120; B0 .120-.126; QW1 .126-.129; B1 .129-.135; QW2 .135-.138; B2 .138-.144; QW3 .144-.147; B3 .147-.153; QW4 .153-.156; B4 .156-.162; nGaN .162..4.062. Old nGaN starts .172, total4.072. This 10nm geometry change is intentional, not offset.
- SDevice and sdevice.par executable content copied from GitHub candidate, no physics/Solve change. SVisual1/2 math/extraction unchanged, identity/CSV prefixes changed. SVisual1 J normalization assumes raw A/um AreaFactor1, unverified.
- SWB macros NtSide=1e18, TrapEt=.75, TrapSigmaN/P=1e-15, Vstop=5. SDE -> SDevice -> sibling SVisual1 and SVisual2. Inspect pp, mesh, x coords, doping, all contacts and 22 trap names before single 5V TrapON run.
- Only use after Claude D50 run is validated; compare to exact matched D50 control at matched injected current. Don't overwrite school originals. Drift-diffusion QW treatment may not reproduce Chang2020 APSYS; 6nm is not a verified optimum.
- Source: `CMP/PROJECT_AB_REPLACEMENT_DESIGN_FREEZE_20261119.md`; Chang et al. Nanoscale Research Letters 15:160 (2020).
