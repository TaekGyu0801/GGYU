# CMP AI Handoff

> ChatGPT와 Claude가 CMP 프로젝트 작업 내용을 공유하기 위한 공용 인수인계 문서.
> CMP 관련 작업 시작 전 반드시 이 파일을 먼저 읽고, 실제 작업이 끝난 뒤 최신 상태로 갱신한다.

---

## 1. PROJECT OVERVIEW

### Topic
**AR/VR용 Micro-LED의 Sidewall Damage Healing 공정 최적화**

발표/보고서용 제목:

**초소형 Micro-LED의 Sidewall Damage Healing 공정을 통한 발광효율 및 신뢰성 개선**

### Core Problem
Micro-LED mesa 형성을 위한 Dry Etching 과정에서 발생하는 sidewall defect / plasma damage가 초소형 Micro-LED의 전기적·광학적 특성을 저하시킨다.

Micro-LED 크기가 작아질수록 perimeter-to-area ratio가 증가하여 sidewall damage의 영향이 커질 수 있다.

주요 영향:
- Non-radiative recombination 증가
- Reverse leakage current 증가
- EQE 감소
- EL 특성 저하
- Reliability 저하

### Process Direction
**Dry Etching → Wet Chemical Treatment → ALD Passivation**

### Main Variables
- Wet Chemical Treatment 조건
- ALD Material
- ALD Thickness

### Main Evaluation Metrics
- Reverse Leakage Current
- EQE
- EL Image
- Reliability

---

## 2. RESEARCH LOGIC

```text
Micro-LED Scaling
        ↓
높은 Perimeter / Area Ratio
        ↓
Dry Etching Sidewall Damage
        ↓
Surface State / Defect 증가
        ↓
SRH Non-radiative Recombination 증가
        ↓
Leakage Current 증가 / EQE 감소
        ↓
Wet Chemical Treatment
        +
ALD Sidewall Passivation
        ↓
Defect Density 감소
        ↓
Leakage 감소 / EQE 향상 / Reliability 향상
```

---

## 3. CURRENT STATUS

- CMP 프로젝트 주제 확정
- Sidewall damage를 핵심 문제로 설정
- Wet Chemical Treatment + ALD Passivation을 핵심 개선 공정으로 설정
- 주요 공정 변수 및 평가 지표 설정
- ChatGPT ↔ Claude 공용 인수인계 파일 운용 시작
- 의미 있는 CMP 작업은 `AI_HANDOFF.md`에 자동 기록하는 운영 규칙 적용
- 관련 논문 조사 및 TCAD 적용 가능성 검토 진행 예정

---

## 4. CURRENT TASK

현재 우선순위:

1. Sidewall damage mechanism 관련 핵심 논문 정리
2. Wet chemical treatment 후보 공정 및 효과 비교
3. ALD passivation material / thickness 후보군 정리
4. 실제 평가 가능한 실험·시뮬레이션 구조 구체화

---

## 5. IMPORTANT DECISIONS

- Sidewall damage가 프로젝트의 핵심 문제이다.
- Wet Chemical Treatment + ALD Passivation을 핵심 개선 공정으로 사용한다.
- Reverse Leakage Current, EQE, EL Image, Reliability를 주요 평가 지표로 본다.
- 검증되지 않은 공정 조건이나 최적값을 확정 사실처럼 기록하지 않는다.
- 논문 근거, 실험 결과, 추정/가설을 명확히 구분한다.
- CMP 프로젝트 진행에 의미 있는 활동은 사용자가 매번 따로 요청하지 않아도 `AI_HANDOFF.md`에 자동 기록한다.

---

## 6. AI COLLABORATION RULES

ChatGPT와 Claude는 서로 직접 대화할 수 없으므로 이 파일을 공용 기억장치처럼 사용한다.

### 작업 시작 전
1. `CMP/AI_HANDOFF.md`를 읽는다.
2. `CURRENT STATUS`, `CURRENT TASK`, `IMPORTANT DECISIONS`, `AI HANDOFF`를 확인한다.
3. 이전 AI가 수행한 작업을 존중하고 중복 작업을 피한다.
4. 관련 파일이 있다면 먼저 읽은 후 작업한다.

### 자동 기록 원칙
사용자가 매번 "기록해줘"라고 말하지 않아도 다음과 같은 **프로젝트 진행에 의미 있는 CMP 활동**은 작업 종료 시 자동으로 WORK LOG와 AI HANDOFF에 기록한다.

- 논문/기술 자료 조사 및 핵심 결론 도출
- 실험 설계, 변수 설정, 공정 조건 비교
- TCAD 코드 작성·수정·해석 및 시뮬레이션 조건 변경
- 데이터, 그래프, 결과 분석 및 해석
- 프로젝트 방향, 우선순위, 가설, 의사결정 변경
- GitHub 파일 생성·수정·삭제
- 보고서, 발표, 포스터 등 프로젝트 산출물 작성 또는 구조 변경
- ChatGPT 또는 Claude가 다음 작업자에게 반드시 알려야 하는 중요 사항

다음과 같은 내용은 기본적으로 자동 기록 대상에서 제외한다.

- 단순 용어 질문
- 일반적인 개념 설명만 한 경우
- CMP 진행 상황을 바꾸지 않는 짧은 확인/잡담
- 이미 기록된 내용의 단순 반복 설명

단, 위 항목이라도 향후 실험/연구 판단에 중요한 내용이 생기면 기록한다.

### 작업 완료 후
1. 의미 있는 작업이면 아래 WORK LOG에 작업 내용을 자동 추가한다.
2. CURRENT STATUS가 바뀌었으면 최신 상태로 수정한다.
3. 다음 작업자가 해야 할 일이 있으면 AI HANDOFF에 남긴다.
4. 자신이 생성/수정한 GitHub 파일 경로를 기록한다.
5. 사용자가 명시적으로 "이번 작업은 기록하지 마"라고 하면 해당 작업은 기록하지 않는다.

### 금지 사항
- 다른 AI의 기존 WORK LOG 삭제 금지
- 근거 없이 기존 결정사항 변경 금지
- 미검증 내용을 확정된 사실처럼 기록 금지

---

## 7. WORK LOG

### 2026-08-24 — ChatGPT

작업 내용:
- ChatGPT ↔ Claude 공용 CMP 인수인계 구조 설계
- `CMP/AI_HANDOFF.md` 최초 생성

결과:
- 프로젝트 기본 맥락, 협업 규칙, 현재 상태, 다음 작업 구조를 정리함

생성/수정 파일:
- `CMP/AI_HANDOFF.md`

다음 작업:
- CMP 관련 실제 연구 자료 및 파일 구조를 단계적으로 추가

---

### 2026-08-24 — ChatGPT

작업 내용:
- CMP 관련 의미 있는 활동을 `AI_HANDOFF.md`에 자동 기록하는 상시 운영 규칙 추가
- 자동 기록 대상과 제외 대상을 구분함

결과:
- 향후 사용자가 매번 기록을 요청하지 않아도 조사, 분석, TCAD, 실험 설계, 결과 해석, 의사결정, GitHub 변경 사항 등을 자동으로 인수인계 문서에 남기도록 규칙화함

생성/수정 파일:
- `CMP/AI_HANDOFF.md`

다음 작업:
- ChatGPT와 Claude 모두 이후 CMP 작업에서 본 자동 기록 규칙을 적용

---

## 8. AI HANDOFF

### Last Worker
ChatGPT

### What was just done
- CMP 프로젝트용 ChatGPT ↔ Claude 공용 인수인계 파일을 생성함.
- 프로젝트 핵심 주제, 연구 논리, 주요 변수, 평가 지표 및 협업 규칙을 초기화함.
- 의미 있는 CMP 활동은 별도 요청 없이 `AI_HANDOFF.md`에 자동 기록하도록 운영 규칙을 추가함.

### Next AI should do
- 사용자의 다음 CMP 요청을 수행하기 전 이 파일을 먼저 읽을 것.
- 조사, 분석, TCAD, 실험 설계, 결과 정리, 파일 수정 등 의미 있는 작업을 수행한 뒤 자동으로 WORK LOG를 갱신할 것.
- 단순 개념 질문/잡담은 프로젝트 상태를 바꾸지 않는 한 불필요하게 기록하지 않을 것.

### Important warnings / unresolved questions
- ALD 최적 material 및 thickness는 아직 확정되지 않음.
- Wet chemical treatment 최적 조건도 아직 확정되지 않음.
- 논문 또는 실험 근거 없이 특정 조건을 최적값으로 단정하지 말 것.

---

## 9. RECOMMENDED FILE MAP

```text
CMP/
├─ README.md
├─ AI_HANDOFF.md
├─ docs/
├─ research/
├─ tcad/
└─ results/
```

### File Roles
- `CMP/README.md`: 프로젝트 전체 개요 및 최종 정리
- `CMP/AI_HANDOFF.md`: ChatGPT ↔ Claude 현재 작업 상태 및 인수인계
- `CMP/research/`: 논문 조사 및 기술 분석
- `CMP/tcad/`: Sentaurus TCAD 코드, 조건, 시뮬레이션 노트
- `CMP/results/`: 실험/시뮬레이션 결과 및 분석
- `CMP/docs/`: 발표, 보고서, 포스터용 내용
