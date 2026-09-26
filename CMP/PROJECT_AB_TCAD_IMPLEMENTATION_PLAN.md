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

## 2026-09-26 — CES 발표용 구현 방식 정밀화

### Project A — Carbon High-Resistance Edge

**1차 TCAD mechanism screen에서는 SProcess implantation을 사용하지 않는다.**
현재 Common Baseline의 SDE→SDevice flow를 유지하고, SDE에서 upper n-GaN edge에 `Cedge_L/R`라는 **GaN region tag**를 추가한 뒤 SDevice에서 해당 region에만 carbon-related deep acceptor/compensation physics를 적용한다.

중요:
- `Cedge`는 별도의 "Carbon material"이 아니라 **GaN:C를 나타내는 GaN region**이다.
- baseline의 5 nm `DmgL/R`은 그대로 유지한다.
- Carbon physics를 QW에 직접 넣지 않는다. 첫 mechanism screen은 MQW 바로 아래 upper n-GaN edge에서 current-access blocking을 본다.
- Stage 1: C_N-like deep acceptor (literature anchor Ev+~0.9 eV) + N_C sweep.
- Stage 2: 필요하면 compensating donor/acceptor pair 또는 effective resistivity calibration으로 확장.

**왜 implantation을 1차 모델로 쓰지 않는가:** C implantation의 high-resistivity isolation은 implantation-induced lattice damage 자체의 영향이 매우 크므로, Carbon compensation mechanism과 implantation damage mechanism이 섞일 수 있다. CES 발표에서는 "device-level effective GaN:C region"을 먼저 검증하고, 공정-realistic implantation profile은 후속 단계로 분리한다.

Fabrication analogue는 selective localized GaN:C formation (예: selective-area regrowth/local C incorporation)을 우선 설명하되, exact process route는 아직 검증 전이다.

### Project B — Localized AlGaN Lateral Heterobarrier

**Project B는 implantation이 아니라 실제 material/geometry modification으로 구현한다.**
SDE에서 fixed 5 nm damaged sidewall 안쪽에 `AlBarrier_L/R`라는 AlGaN region을 추가하고, Al mole fraction `xAl`과 lateral width `wAl`을 parameterize한다. 첫 mechanism screen에서는 barrier가 MQW lateral path를 가로질러 carrier가 sidewall로 bypass하지 못하도록 active-region vertical span을 커버하게 설계한다.

- SDE: AlGaN region + xAl + geometry + interface mesh refinement.
- SDevice: common Fermi/SRH/Radiative/Auger/mobility/polarization/heterojunction physics 유지; 별도의 artificial trap으로 barrier를 만들지 않는다.
- 확인 1순위: lateral Ec/Ev profile에서 intended band offset이 실제 형성되는지.
- 이후: edge e/h density, current map, integrated sidewall SRH, IQE, Vf/Auger/crowding penalty.

Fabrication analogue는 local recess/etch 후 selective-area AlGaN regrowth이다. AlGaN selective regrowth 자체는 GaN heterostructure literature에서 demonstrated 되었지만, 이 microLED lateral-barrier integration geometry 자체는 아직 project hypothesis이며 fabrication feasibility가 검증된 구조로 주장하지 않는다.

### 발표용 한 줄 구분

- **A:** same GaN material + localized carbon compensation → **resistive blocking**.
- **B:** new AlGaN material region + band offset → **heterobarrier confinement**.

### Command-file split

- `SDE`: geometry/region/material/mole-fraction/mesh 변경.
- `SDevice`: region-specific traps/compensation and outputs/physics.
- `SProcess`: 현재 1차 A/B mechanism screen에는 사용하지 않음. Implantation/regrowth process realism이 필요해질 때 별도 후속 단계로 추가.

## 2026-09-26 — Project A/B literature evidence map for CES

### Project A — Carbon High-Resistance Edge

Key literature and what it directly supports:

1. E. Richter et al., **Growth and Properties of Intentionally Carbon-Doped GaN Layers**, Crystal Research and Technology 55 (2020), 1900129, DOI 10.1002/crat.201900129.
   - Experimentally carbon-doped GaN showed semi-insulating behavior.
   - Maximum reported specific resistivity: ~2×10^10 Ω·cm at [C] = 8.8×10^18 cm^-3.
   - C_N deep acceptor electrical activation energy ~0.94 eV.
   - At higher carbon concentration up to 3.5×10^19 cm^-3 conductivity rose slightly, attributed to self-compensation/passivation.

2. M.R. Ramdani et al., **Effect of carbon doping on crystal quality, electrical isolation and electron trapping in GaN based structures grown silicon substrates**, Solid-State Electronics 75 (2012) 86–92, DOI 10.1016/j.sse.2012.04.034.
   - Several 10^18 cm^-3 carbon strongly increased GaN resistivity.
   - Carbon addition also produced electron trapping and could degrade crystal quality.

3. W. Cao et al., **Numerical simulation analysis of carbon defects in the buffer on vertical leakage and breakdown of GaN on silicon epitaxial layers**, Scientific Reports 13 (2023) 14820, DOI 10.1038/s41598-023-41678-1.
   - Sentaurus TCAD explicitly modeled GaN:C.
   - Used C_N acceptor level Ev+0.9 eV, C_Ga donor level Ec−0.11 eV, capture cross sections 1e-15 cm^2.
   - Simulations showed carbon-defect charge can block electron conduction at the UID-GaN/GaN:C interface; effect depends on defect concentrations/occupancy.

4. L. Chang et al., **Alternative Strategy to Reduce Surface Recombination for InGaN/GaN Micro-light-Emitting Diodes—Thinning the Quantum Barriers to Manage the Current Spreading**, Nanoscale Research Letters 15 (2020) 160, DOI 10.1186/s11671-020-03372-3.
   - In microLEDs, managing current spreading so fewer carriers reach sidewall defects reduced sidewall nonradiative recombination and improved EQE.
   - Their method was thinner QBs / reduced vertical resistance, not carbon; it supports the carrier-path principle, not our exact geometry.

5. A. Taube et al., **Ion implantation for isolation of AlGaN/GaN HEMTs using C or Al**, physica status solidi (a) (2015), DOI 10.1002/pssa.201431724.
   - C-ion implantation produced high-resistance isolation.
   - XRD/Raman/PL evidence showed implantation-induced crystal damage is a major source of the insulating behavior.
   - Therefore implantation is not a clean first test of 'carbon compensation only'.

Project-A inference/hypothesis:
- Literature proves GaN:C can become high-resistivity and that C_N deep acceptors/compensation can block conduction.
- Separate microLED literature proves reducing carrier access to sidewall defects can reduce nonradiative loss.
- **No identified paper directly demonstrates our exact localized Carbon High-R edge in an InGaN blue microLED.** That geometry is our project hypothesis.
- Stage-1 TCAD therefore isolates the material/electrical mechanism using a GaN Cedge region + C-related traps/compensation, not SProcess implantation.

### Project B — Localized AlGaN Lateral Heterobarrier

1. W.J. Baek et al., **Ultra-low-current driven InGaN blue micro light-emitting diodes for electrically efficient and self-heating relaxed microdisplay**, Nature Communications 14 (2023) 1386, DOI 10.1038/s41467-023-36773-w.
   - Quantum-barrier thickness and p-AlGaN EBL composition were engineered to control carrier confinement/injection.
   - Thicker QBs lowered tunneling and reduced surface-current contribution; the study links excessive lateral carrier diffusion to sidewall recombination.
   - Fabricated 10×10 µm^2 devices achieved 3.00% EQE at 0.1 A/cm^2 in the optimized epitaxial design.
   - This supports barrier engineering / lateral diffusion control, but not our exact lateral AlGaN wall.

2. F. Furtmayr et al., **Carrier confinement in GaN/Al_xGa_1−xN nanowire heterostructures (0 < x ≤ 1)**, Physical Review B 84 (2011) 205303, DOI 10.1103/PhysRevB.84.205303.
   - HRTEM observed a lateral AlGaN shell around GaN nanodiscs.
   - 3D numerical simulations showed the lateral AlGaN shell must be included to explain carrier confinement / optical behavior.
   - Confinement and radial internal fields depended strongly on Al composition; very high Al content could reduce emission through large radial fields.
   - This is direct evidence for lateral GaN/AlGaN heterobarrier physics, but in nanowires, not planar microLEDs.

3. L. Chang et al. (2020), same paper above.
   - Directly supports the microLED-level causal goal: suppress lateral carrier transport to the damaged edge to reduce surface SRH and improve efficiency.

4. **Wafer-scale crack-free AlGaN on GaN through two-step selective-area growth for optically pumped stimulated emission**, Journal of Crystal Growth 445 (2016) 78–83, DOI 10.1016/j.jcrysgro.2016.04.021.
   - Demonstrated two-step selective-area growth of crack-free Al0.2Ga0.8N on GaN over a 2-inch wafer and subsequent GaN/AlGaN MQW growth.
   - This supports selective AlGaN-on-GaN growth as a process capability, not the exact proposed microLED edge-wall geometry.

Project-B inference/hypothesis:
- Literature shows AlGaN/GaN heterostructures can provide lateral/radial carrier confinement and microLED barrier engineering can reduce surface-related carrier loss.
- Selective-area AlGaN growth on GaN has been demonstrated in other geometries.
- **No identified paper directly demonstrates the exact narrow lateral AlGaN edge-wall geometry proposed here for a planar InGaN microLED.** This geometry is our project hypothesis.
- Stage-1 TCAD therefore inserts a real AlGaN material region in SDE and verifies Ec/Ev barrier formation before evaluating sidewall SRH/IQE.

### CES evidence boundary

For both A and B, distinguish:
- **Published fact:** material/defect/barrier physics demonstrated in cited literature.
- **Published microLED principle:** controlling lateral carrier access to sidewalls reduces nonradiative loss.
- **Our hypothesis:** localized Carbon High-R edge vs localized lateral AlGaN barrier on the same baseline.
