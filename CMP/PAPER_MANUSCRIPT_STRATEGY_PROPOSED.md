# Proposed Manuscript Strategy — Edge-Access Engineering for InGaN MicroLEDs

Date: 2026-10-03
Worker: 이택규
Status: PROPOSED

## Central manuscript thesis

Use one frozen sidewall-damaged InGaN/GaN microLED Common Baseline and compare two edge-engineering mechanisms without removing the sidewall defects:

- Project A: localized GaN:C high-resistivity edge -> resistive blocking
- Project B: localized AlGaN lateral heterobarrier -> band-offset blocking

Core question:
Can carrier access to the same damaged sidewall be reduced enough to suppress integrated sidewall SRH while preserving MQW radiative recombination, without unacceptable forward-voltage, current-crowding, or Auger penalties?

## Proposed title direction

Defect-Access Engineering in InGaN MicroLEDs: Comparative TCAD Study of Carbon-Induced Resistive Edges and Lateral AlGaN Heterobarriers

## Proposed paper structure

1. Introduction
   - size-dependent microLED sidewall loss
   - limitations of defect removal/passivation-only framing
   - carrier-path control as complementary strategy
   - gap: mechanism-controlled comparison of resistive vs heterobarrier edge blocking on one baseline

2. Device model and numerical method
   - literature-grounded vertical epitaxy
   - 4 µm representative mesa
   - fixed 5 nm damaged sidewall
   - sidewall trap model and calibration/sensitivity status
   - common physics, mesh, contacts
   - same-current comparison protocol

3. Common Baseline validation
   - NtSide OFF/ON
   - NtSide sweep
   - mesa-size scaling
   - mesh convergence
   - electrical and spatial validation

4. Project A: Carbon high-resistivity edge
   - Cedge geometry
   - carbon-related acceptor/compensation model
   - width/concentration sweep
   - edge carrier/current suppression
   - sidewall SRH vs Vf/crowding/Auger tradeoff

5. Project B: Localized AlGaN lateral heterobarrier
   - barrier geometry
   - Al mole fraction/width sweep
   - lateral Ec/Ev verification
   - carrier confinement
   - sidewall SRH vs injection/crowding/Auger tradeoff

6. Direct mechanism comparison
   - Baseline vs A vs B at identical injected current/current density
   - normalized sidewall SRH
   - MQW radiative/Auger
   - IQE
   - Vf penalty
   - current-crowding metric
   - Pareto/design-window analysis

7. Scaling and robustness
   - mesa 4/10/20 µm
   - NtSide sensitivity
   - parameter/mesh sensitivity
   - identify where each mechanism is useful

8. Discussion
   - resistive blocking vs band-offset blocking
   - fabrication interpretation and limitations
   - model limitations and experimental validation needs

9. Conclusion

## Novelty assessment

Potentially strongest:
- Localized GaN:C high-resistivity edge applied specifically as sidewall-defect-access blocking in planar InGaN microLED.
- Controlled head-to-head comparison of resistive blocking vs heterobarrier blocking while retaining identical damaged-sidewall physics.
- Same-current, mechanism-resolved evaluation including SRH, radiative, Auger, carrier density, current crowding, and Vf penalty.

Moderate:
- Localized lateral AlGaN edge-wall geometry in a planar blue microLED. AlGaN-based lateral/radial carrier confinement is established in other nitride structures, so novelty should be claimed at the device geometry/use-case/comparison level, not as discovery of AlGaN confinement itself.

Not novel by itself:
- microLED sidewall SRH degradation
- sidewall trap TCAD
- generic current confinement
- generic AlGaN carrier confinement
- generic carbon-induced high resistivity in GaN

## Required result logic

Baseline:
- increasing sidewall defect strength should increase edge SRH and degrade radiative efficiency
- smaller mesa should show greater sidewall sensitivity

Project A:
- increasing effective edge resistance should reduce edge carrier/current access and integrated sidewall SRH
- an optimum window should appear before excessive Vf/current-crowding/Auger penalties dominate

Project B:
- lateral Ec/Ev barrier must be visible first
- barrier strengthening should reduce edge carrier access and sidewall SRH
- excessive barrier strength should eventually cause injection/crowding or radiative penalties, producing an optimum window

Comparative result:
- at identical injected current, A and/or B must provide lower normalized edge SRH than baseline while preserving or increasing IQE
- performance gains must be explained by spatial carrier/current redistribution, not only I-V shifts
- benefit should ideally become stronger at smaller mesa sizes / stronger sidewall defects
- a Pareto plot should identify the useful design region rather than only one hand-picked point

## Recommended quantitative metrics

- Sidewall SRH suppression:
  S_SRH = 1 - R_SRH,edge(design) / R_SRH,edge(baseline)
- IQE:
  IQE = integral_MQW(Rrad) / integral_MQW(Rrad + RSRH + RAuger)
- Voltage penalty:
  DeltaVf = Vf_design(J0) - Vf_baseline(J0)
- Edge carrier-access ratio:
  A_edge = integral_Dmg(n+p) / integral_Dmg(n+p)_baseline
- Current-crowding metric:
  fixed-mesh Jmax/Javg or a robust percentile-based equivalent
- Radiative preservation:
  P_rad = Rrad_MQW(design) / Rrad_MQW(baseline)

All comparisons must use the same current/current density and identical integration regions.

## Evidence boundary

This is a proposed manuscript direction, not a claim that novelty is legally or exhaustively proven. A full novelty claim requires a broader literature and patent search and ultimately experimental validation.
