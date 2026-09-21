# Common Baseline v1 — Source of Truth

## 한 문장 정의

**JBD의 4-µm-pitch AR microdisplay를 application target으로 설정하고, Kou et al.의 blue InGaN/GaN epitaxy와 Wu et al.의 localized sidewall-damage physics를 결합한 literature-based representative 2D TCAD model.**

이 모델은 **JBD exact device replica가 아니다.**

---

## Source 역할

### JBD
- 역할: application/product scale
- 사용: 0.13-inch class, 640×480, 4 µm pixel pitch, AR/near-eye, III-V MicroLED + CMOS backplane
- 사용하지 않음: actual mesa width, fill factor, exact epitaxy, exact trap values
- 주의: **4 µm pixel pitch ≠ 4 µm mesa width**

### Kou et al. 2019
Vertical blue epitaxy backbone:
- n-GaN = 4.0 µm
- n-GaN donor = 5×10^18 cm^-3
- 4 QWs
- In0.15Ga0.85N
- QW = 3 nm
- GaN barrier = 22 nm
- 5 barriers
- p-Al0.15Ga0.85N EBL = 26 nm
- p-GaN = 120 nm
- ~445 nm blue scale

### Wu et al. 2023
Sidewall localized defect physics:
- etched sidewall 내부 약 5 nm damaged semiconductor region
- acceptor-like trap concept

Wu의 vertical epitaxy를 baseline에 혼합하지 않는다.

### Chen et al. 2024
- 4×4 µm-class blue microLED의 sidewall effect 중요성에 대한 experimental support
- 현재 4 µm mesa는 JBD 실제 mesa가 아니라 representative modeling choice

---

## Geometry

- Model: 2D Cartesian planar cross-section
- x: vertical growth direction
- y: lateral direction
- Cylindrical(yAxis=0): OFF
- W_mesa = 4.0 µm — literature-supported representative modeling choice
- W_domain = 5.0 µm — numerical
- W_damage = 0.005 µm = 5 nm — literature-supported
- t_nitride = 0.100 µm — numerical geometry
- t_nbase = 0.300 µm — numerical/contact base

Vertical stack:
- p-GaN 120 nm
- p-Al0.15Ga0.85N EBL 26 nm
- Barrier0 22 nm
- QW1 3 nm
- Barrier1 22 nm
- QW2 3 nm
- Barrier2 22 nm
- QW3 3 nm
- Barrier3 22 nm
- QW4 3 nm
- Barrier4 22 nm
- n-GaN 4.0 µm
- numerical n-GaN base 0.3 µm

---

## Doping

- n-GaN donor = 5×10^18 cm^-3 — Direct/Kou
- p-GaN effective active acceptor = 3×10^17 cm^-3 — literature-derived modeling approximation
- EBL effective active acceptor = 3×10^17 cm^-3 — modeling approximation
- GaN barrier background donor = 1×10^15 cm^-3 — numerical/modeling assumption

---

## Sidewall implementation

각 semiconductor layer를 lateral direction으로 나눈다:

```text
DmgL | Clean | DmgR
```

Material identity는 유지한다.
예: `DmgL_QW1`, `Clean_QW1`, `DmgR_QW1` 모두 InGaN.

DmgL/DmgR에만 explicit bulk trap을 적용한다.

현재 확인된 region family:
- Clean_Barrier0~4
- Clean_EBL
- Clean_QW1~4
- Clean_nGaN
- Clean_pGaN
- DmgL_Barrier0~4
- DmgL_EBL
- DmgL_QW1~4
- DmgL_nGaN
- DmgL_pGaN
- DmgR_Barrier0~4
- DmgR_EBL
- DmgR_QW1~4
- DmgR_nGaN
- DmgR_pGaN
- Nitride_L / Nitride_R

---

## Sidewall trap nominal values

- Type = Acceptor-like bulk trap — literature based
- W_damage = 5 nm — Wu-inspired literature support
- Et = Ev + 0.75 eV — literature-supported simplified deep acceptor
- Nt = 1×10^18 cm^-3 — **Calibration starting value**
- sigma_n = 1×10^-15 cm² — **Calibration/effective**
- sigma_p = 1×10^-15 cm² — **Calibration/effective**

Nt는 JBD measured value도 Wu direct value도 아니다.

---

## Common physics

- T = 300 K
- Fermi
- Piezoelectric_Polarization(strain)
- SRH
- Radiative
- Auger
- Mobility
- High-field saturation
- IncompleteIonization
- Cylindrical OFF
- Initial forward sweep 0 → 5 V

---

## Workbench flow

```text
SDE
→ SDevice1 (Defect OFF, NtSide=0)
→ SVisual1 (forward I-V)
→ SDevice2 (Defect ON, Nt=1e18 hard-coded)
→ SVisual2 (sidewall mechanism maps)
```

SDevice1과 SDevice2의 차이는 sidewall defect activation뿐이어야 한다.

---

## Validation gate before Baseline freeze

1. Geometry validation
2. Defect OFF normal LED behavior
3. Defect ON sidewall recombination increase
4. Radiative/IQE degradation 확인
5. Nt sensitivity: 0 / 1e17 / 1e18 / 1e19
6. Mesa size: 4 / 10 / 20 µm
7. Mesh convergence

Common Baseline이 freeze되기 전 Project A/B 성능 비교로 넘어가지 않는다.

---

## Project A constraint

Project A = Carbon-Induced High-Resistivity Edge.

변경 금지:
- sidewall damage width
- Nt
- Et
- sigma_n/p
- mesa
- vertical epitaxy
- contacts
- common physics
- mesh quality

Project A에서는 Carbon-related edge structure/parameter만 추가한다.

Expected causal chain:
Carbon → compensation → edge resistance ↑ → edge carrier/current access ↓ → SAME sidewall defect interaction ↓ → SRH ↓.
