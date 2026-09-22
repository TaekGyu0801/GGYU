# CES2027 Selection Presentation Plan

Date prepared: 2026-09-22
Worker: 주수빈
Status: PROPOSED

## Presentation purpose

15분 CES2027 선발 발표. 심사위원은 CMP 교수진이며 1주차 발표에서 연구 주제/문제의식은 이미 공유됨.

이번 발표의 중심 메시지:

**Literature-grounded Common Baseline을 구축했고, 구조적 검증을 거친 동일 baseline 위에서 Project A/B를 공정하게 TCAD 비교하도록 설계했다.**

## Recommended storyline

1. Title / one-line thesis
2. Week 1 → Week 2: 이번 주에 새로 확보한 것
3. Why a Common Baseline is necessary for fair A/B comparison
4. Literature architecture: JBD / Kou / Wu / Chen의 역할 분리
5. Baseline parameter table with provenance labels
6. Final baseline device structure and TCAD geometry
7. Sidewall damage implementation: DmgL | Clean | DmgR + 5 nm trap region
8. What has been validated so far: geometry / regions / doping / linkage, and what is still running
9. Validation protocol: NtSide=0 vs 1e18 → I-V / SRH / radiative / IQE / size / mesh
10. Project A implementation: Carbon-Induced High-Resistivity Edge
11. Project B implementation: Localized AlGaN Lateral Heterobarrier
12. Fair-comparison matrix + expected decision criteria
13. Conclusion / next milestone toward CES2027

## Timing target

- Slides 1–3: ~2.5 min
- Slides 4–8: ~6.0 min
- Slides 9–12: ~5.5 min
- Slide 13: ~1.0 min

Total: ~15 min

## Important framing

- JBD 4 µm is product/application scale; do not claim 4 µm pixel pitch is exact mesa width.
- 4 µm mesa in the current TCAD is a literature-supported representative modeling choice.
- Kou 2019 supplies the coherent vertical blue InGaN/GaN epitaxy backbone.
- Wu 2023 supplies the localized ~5 nm sidewall damaged-region concept.
- Chen 2024 supports the importance of sidewall effects at ~4×4 µm-class blue microLED scale.
- Nt=1e18 and sigma=1e-15 are calibration/effective starting values, not direct JBD or Wu measurements.
- Structural baseline validation and electrical/optical validation must be clearly separated.
- Do not present incomplete long-running SDevice results as confirmed.
- Project A/B comparison must keep the Common Baseline fixed and modify only each project-specific edge concept.

## Visual priorities

- One literature-to-parameter provenance diagram
- One clean device cross-section with labeled dimensions/doping
- One DmgL | Clean | DmgR sidewall schematic
- One baseline validation screenshot/map montage
- One mechanism diagram for A
- One mechanism diagram for B
- One final A vs Baseline vs B comparison matrix
