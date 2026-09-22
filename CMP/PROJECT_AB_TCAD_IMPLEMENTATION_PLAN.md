# Project A/B TCAD Implementation Plan

Prepared: 2026-09-22
Worker: 주수빈
Status: PROPOSED — not yet frozen

## Purpose

교수진의 1차 발표 피드백에 답하기 위해 Project A(Carbon-Induced High-Resistivity Edge)와
Project B(Localized AlGaN Lateral Heterobarrier)를 Common Baseline 위에서
어떻게 실제 Sentaurus TCAD로 구현하고 무엇을 비교할지 구체화한다.

중요:
- Common Baseline의 5 nm DmgL/DmgR sidewall damage, Nt/Et/sigma, vertical epitaxy, contacts, physics는 고정한다.
- A/B에서는 sidewall defect를 지우지 않고 그 안쪽에 edge-engineering region을 추가한다.
- A/B 성능은 같은 전압이 아니라 같은 injected current/current density에서 우선 비교한다.
- 아래 C/AlGaN 치수와 농도 범위는 1차 DOE 제안이며 확정값이 아니다.

## Shared geometry principle

Outermost sidewall sequence:

DmgL(5 nm) | Edge-engineering region | Clean core | Edge-engineering region | DmgR(5 nm)

Baseline damage region is preserved so that the question is:
'같은 defect가 있을 때 carrier access를 줄이면 SRH가 얼마나 감소하는가?'

## Project A — Carbon-Induced High-Resistivity Edge

### Physical concept
Carbon-related deep acceptor/compensation in GaN can make GaN semi-insulating/high-resistivity.
A first device-level implementation should use an edge-localized GaN:C current-blocking/guard region,
preferably in the upper n-GaN immediately below the MQW edges rather than adding carbon traps inside the QWs.

### Candidate fabrication path
- Mask-defined selective edge region
- Candidate route A: C ion implantation / multi-energy implantation into edge current-blocking zones
- Candidate route B: selective-area regrowth of C-doped GaN
- Fabrication route is not yet frozen; TCAD first screens whether the current-blocking mechanism is beneficial.

### TCAD geometry
Add Cedge_L / Cedge_R inside the fixed 5 nm damage regions.
Material identity remains GaN.

Proposed first DOE:
- lateral width w_C: 0 / 0.05 / 0.10 / 0.20 / 0.30 um
- vertical position: upper n-GaN directly below MQW first
- later, if needed, vertical depth/location sweep

### SDevice physics
Do not model carbon by simply reusing the baseline sidewall trap values.
First-order mechanism screen:
- carbon-related deep acceptor in Cedge regions
- literature anchor: C_N around Ev + 0.9 eV
- concentration N_C and capture cross-sections are calibration/sweep parameters

Higher-fidelity stage:
- acceptor/donor compensation ratio or measured effective resistivity calibration

Pseudo-structure:
Physics(Region="Cedge_L/R") {
  Traps( Acceptor, Conc=@NC@, FromValBand, EnergyMid~0.9 eV, sigma=@calibrated@ )
}

### What must be observed
- Cedge local conductivity/resistivity decreases
- current streamlines/current density shift toward mesa center
- eDensity/hDensity at 5 nm sidewall damage regions decrease
- integrated sidewall SRH decreases
- MQW radiative recombination / IQE increases or is preserved
- penalty check: Vf rise, excessive center current crowding, Auger increase

## Project B — Localized AlGaN Lateral Heterobarrier

### Physical concept
Place a higher-bandgap AlGaN region between the clean active core and the damaged sidewall.
The lateral conduction/valence-band offsets should reduce carrier diffusion/access to the damaged edge.

### Candidate fabrication path
- mask-defined narrow edge window / recess
- selective-area MOCVD/MBE AlGaN regrowth in the lateral edge region
- exact manufacturable integration with the MQW is not yet validated; TCAD is used first as a device-level feasibility screen

### TCAD geometry
Add AlBarrier_L / AlBarrier_R immediately inside DmgL/DmgR, intersecting the active-region lateral path.
The first TCAD structure should make the barrier cross the MQW-active vertical span so carriers cannot bypass it laterally.

Proposed first DOE:
- x_Al: 0.05 / 0.10 / 0.15 / 0.20 / 0.30
- lateral width w_Al: 0.02 / 0.05 / 0.10 / 0.20 um
- vertical extent/position sweep only after first mechanism check

### SDevice/SDE principle
- Geometry/material change is defined in SDE: AlGaN regions + Al mole fraction as a parameter.
- Use the same global Fermi / SRH / Radiative / Auger / mobility / polarization physics as baseline.
- Refine mesh at the new GaN/AlGaN lateral interfaces.
- Do not add interface traps unless deliberately studying regrowth-interface damage.
- Examine lateral Ec/Ev band profiles across the QW plane to verify the intended heterobarrier.

### What must be observed
- lateral Ec/Ev barrier exists
- eDensity/hDensity in the outer damaged edge decrease
- integrated sidewall SRH decreases
- radiative recombination becomes more center-confined
- penalty check: Vf, carrier injection loss, center crowding, Auger, possible barrier over-confinement

## Fair-comparison protocol

At each current-density operating point:
- Baseline Defect-ON
- Project A
- Project B

Keep identical:
- mesa
- 5 nm sidewall damage
- Nt / Et / sigma
- vertical epitaxy
- contact definitions
- common physics
- comparable mesh quality

Primary outputs:
- I-V / Vf at same current density
- integrated sidewall SRH
- integrated MQW RadiativeRecombination
- integrated Auger
- IQE = Rrad / (Rrad + RSRH + RAuger), using identical integration region
- lateral eDensity/hDensity
- eCurrent/hCurrent/current-density maps
- current crowding metric (e.g. Jmax/Javg)
- lateral band diagrams through the active region

Success criterion:
Lower sidewall SRH + higher/preserved IQE with acceptable Vf/current-crowding/Auger penalty.

## Presentation framing

Do not say:
'Carbon/AlGaN 공정 조건이 이미 확정됐다.'

Say:
'Common Baseline을 freeze한 뒤, edge-engineering zone만 parameterized해서
A는 high-resistivity compensation mechanism, B는 lateral band-offset mechanism을 검증합니다.
TCAD에서는 먼저 carrier redistribution과 sidewall SRH suppression을 확인하고,
그 뒤 공정 가능한 parameter window를 좁힙니다.'
