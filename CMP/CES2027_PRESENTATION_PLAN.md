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

## Week 1 deck reference — received 2026-09-22

Uploaded Week 1 deck has 7 slides and the following storyline:
1. CES 2027 / How can a smaller microLED stay efficient? + JBD target product
2. Pixel scaling -> sidewall impact -> SRH/leakage -> efficiency/reliability loss
3. Project evolution: F- implantation + ALD -> carrier-defect interaction control -> Carbon vs AlGaN
4. Current CMP strategy: Project A Carbon High-R Edge vs Project B AlGaN Heterobarrier; success criterion = lower SRH + higher IQE without unacceptable Vf/crowding/Auger penalty
5. CES 2027 validation framing: device-level result -> product constraints -> manufacturing reality
6. What to bring back from CES: connect CMP results with AR/XR product priorities
7. Q&A

### Consequence for Week 2 deck
- Do not repeat the generic scaling/sidewall problem in detail.
- Keep one short recap slide that visually bridges Week 1 -> Week 2.
- Preserve the clean blue/teal visual language and low-text style of Week 1.
- Move the center of gravity to evidence: baseline provenance, parameter rationale, TCAD geometry validation, and A/B implementation roadmap.
- Reuse the A/B mechanism concept from Week 1 only as a concise reference; Week 2 must add implementation detail and controlled-comparison logic.
- Preserve CES relevance at the end rather than spending early slides on product background.
- Do not upload/reproduce the original PPT in public GitHub because it contains student-identifying information; only presentation-planning notes are recorded here.

## Proposed Week 2 table of contents — 2026-09-22

Recommended deck length: 11 content slides + Q&A (15 min total).

### Part 1. From concept to a testable framework
1. Title — From Concept to a Literature-Grounded TCAD Baseline
2. Week 1 -> Week 2 — What changed this week?
3. Why one Common Baseline? — fair A/B comparison principle

### Part 2. Building and validating the Common Baseline
4. Literature Basis — role separation of JBD / Kou / Wu / Chen
5. Baseline Parameters — value + provenance + confidence category
6. TCAD Baseline Structure — final geometry, epitaxy, doping, sidewall-damage region
7. Baseline Validation — what is structurally confirmed vs electrical/optical validation still in progress

### Part 3. From Baseline to Project A and Project B
8. Project A — Carbon-Induced High-Resistivity Edge: mechanism + TCAD implementation
9. Project B — Localized AlGaN Lateral Heterobarrier: mechanism + TCAD implementation
10. Controlled Comparison Plan — Baseline vs A vs B; common metrics (SRH, IQE, Vf, current crowding, Auger, edge current)

### Part 4. CES2027 relevance and closing
11. Why this matters for CES2027 — connect device-level results to brightness/power/heat/reliability/yield questions already framed in Week 1
12. Q&A / optional closing summary

Recommended time allocation:
- Slides 1–3: 2.5 min
- Slides 4–7: 6.0 min
- Slides 8–10: 5.0 min
- Slide 11: 1.5 min
- Q&A excluded from 15 min talk body if possible

Rationale:
- Week 1 already covered scaling -> sidewall loss, project evolution, A/B concept, and CES product/manufacturing framing.
- Week 2 should therefore minimize repeated background and maximize evidence, implementation, and controlled-comparison design.

## 2026-09-26 — presenter-ownership / evidence taxonomy

이번 발표에서는 모든 baseline/A/B 요소를 다음 네 가지 provenance class로 명시한다.

- **DIRECT LITERATURE:** 논문에서 직접 가져온 구조/수치/물리.
- **LITERATURE-DERIVED MODELING CHOICE:** 여러 논문과 application scale을 바탕으로 연구팀이 선택한 representative modeling choice.
- **CALIBRATION / SENSITIVITY PARAMETER:** 문헌의 단일 정답값이 아니라 baseline을 보정/민감도 검증하기 위한 sweep 시작값.
- **PROJECT HYPOTHESIS:** 문헌의 물리를 바탕으로 연구팀이 새롭게 제안하고 TCAD로 검증할 A/B 구조.

핵심 발표 원칙:
- '논문에 그대로 있어서 넣었다'와 '우리가 연구목적에 맞게 선택했다'를 구분한다.
- JBD 4 µm pixel pitch를 mesa width로 등치하지 않는다.
- Project A의 Carbon edge와 Project B의 localized lateral AlGaN geometry는 그대로 복제한 문헌 구조가 아니라, 문헌에서 검증된 compensation / carrier-confinement physics를 microLED sidewall 문제에 적용하는 **연구 가설**로 설명한다.
- 교수 질문에 답할 때는 '근거 → TCAD 변수 → 관찰 지표 → 성공/실패 판정'의 순서로 설명한다.

## 2026-09-26 — condensed 15-minute deck structure

사용자 결정: 기존 Week 1 보완/왜 baseline이 필요한가/문헌 역할을 여러 장으로 나누지 않고, 초반 1장 안에서 빠르게 주제와 진행상황을 정리한 뒤 즉시 baseline 구축 과정으로 진입한다.

### Revised deck: 9 slides / 15 min
1. Title + project recap + what has been done
2. Literature-grounded baseline construction logic
3. Current Common Baseline structure
4. Parameter provenance + what is fixed vs swept
5. Baseline validation plan + current implementation status
6. Project A TCAD implementation: Carbon High-R Edge
7. Project B TCAD implementation: Localized AlGaN lateral heterobarrier
8. Fair comparison protocol and decision metrics
9. Conclusion + next milestones toward CES2027

### Time allocation
- Slide 1: 1.0 min
- Slides 2–5: 6.5 min
- Slides 6–7: 4.0 min
- Slide 8: 2.0 min
- Slide 9: 1.5 min

### Presentation priority
핵심 시간은 baseline 근거/구조/validation과 Project A/B의 실제 TCAD 수정 지점, 그리고 same-current comparison protocol에 사용한다. Week 1 한계 자체는 별도 슬라이드로 소비하지 않는다.
