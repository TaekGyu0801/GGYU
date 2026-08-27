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
- P2 Mg calibration 완료
  - Target hole concentration: `3.0e17 cm^-3`
  - Calibrated Mg concentration: `9.59e18 cm^-3`
  - Simulated hole concentration: `3.00033017418e17 cm^-3`
  - Temperature: `300 K`
  - Mg incomplete ionization: `E_0=0.2 eV`, `alpha=8e-9`, `g=4`, `Xsec=1e-14`
- P3 baseline Micro-LED 구축 시작
  - Synopsys `GaN_PiN_Diode` 예제를 `~/CMP_P3_BASELINE_MICROLED`로 복사함
  - SDE node 1 정상 완료 확인
  - Forward SDevice node 2 실행 중이며 원본 예제 재현 검증 단계
- 서버 계정 사용 가능 기간이 이번 달 말까지일 가능성이 있어, CMP 관련 TCAD 작업물의 GitHub 백업을 최우선 과제로 둔다.

---

## 4. CURRENT TASK

현재 우선순위:

1. `~/CMP_P3_BASELINE_MICROLED` 원본 GaN PiN Forward simulation 재현 완료 여부 확인
2. P3 clean baseline으로 개조
   - p-GaN Mg `9.59e18 cm^-3` 적용
   - P2에서 사용한 Mg incomplete ionization model 반영
   - 초기 clean baseline 단계에서는 불필요한 Nitride/interface trap 제거 여부 검토
3. 이후 InGaN/GaN MQW baseline 추가
4. Sidewall SRV 및 pixel size DOE로 확장
5. 서버 계정 만료 전에 CMP TCAD 관련 프로젝트 폴더, 코드, 파라미터, 로그, 결과를 GitHub `CMP/` 아래에 백업

---

## 5. IMPORTANT DECISIONS

- Sidewall damage가 프로젝트의 핵심 문제이다.
- Wet Chemical Treatment + ALD Passivation을 핵심 개선 공정으로 사용한다.
- Reverse Leakage Current, EQE, EL Image, Reliability를 주요 평가 지표로 본다.
- 검증되지 않은 공정 조건이나 최적값을 확정 사실처럼 기록하지 않는다.
- 논문 근거, 실험 결과, 추정/가설을 명확히 구분한다.
- CMP 프로젝트 진행에 의미 있는 활동은 사용자가 매번 따로 요청하지 않아도 `AI_HANDOFF.md`에 자동 기록한다.
- P2 Mg calibration 최종 기준값은 현재 `NMg = 9.59e18 cm^-3`로 사용한다.
- P3는 복잡한 MQW/sidewall 구조를 한 번에 만들지 않고, 공식 GaN PiN 예제 재현 → clean baseline → MQW → sidewall 순서로 단계적으로 확장한다.
- 서버 계정 만료 전에 재현 가능한 형태로 원본 input deck, parameter file, extraction script, 결과 요약을 GitHub에 남긴다.

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

### 2026-08-27 — ChatGPT

작업 내용:
- P2 p-GaN Mg incomplete-ionization calibration 수행
- 실제 전처리 파일(`pp6_dvs.cmd`)에 Mg 농도가 반영되는지 검증하면서 calibration 진행
- `NMg=9.75e18 cm^-3`에서 `hDensity=3.03103549868e17 cm^-3` 확인
- 최종 `NMg=9.59e18 cm^-3`에서 `hDensity=3.00033017418e17 cm^-3` 확인
- P3용 `CMP_P3_BASELINE_MICROLED` 프로젝트 생성 및 Synopsys `GaN_PiN_Diode` 예제 복사
- P3 node map 확인: node 1=SDE, node 2=Forward SDevice, node 3=Forward SVisual, node 4=Reverse SDevice, node 5=Reverse SVisual
- node 1 SDE 정상 완료 확인
- 원본 Forward SDevice node 2 재현 실행 시작
- 서버 계정 만료 전 GitHub 전체 백업을 우선 과제로 등록

결과:
- P2 Mg calibration 최종값을 `9.59e18 cm^-3`로 확정하여 이후 p-GaN baseline 입력값으로 사용할 수 있음
- P3 baseline 구축의 공식 예제 출발점 확보

관련 서버 경로:
- `~/CMP_P2_MG_CALIBRATION`
- `~/CMP_P3_BASELINE_MICROLED`

생성/수정 파일:
- `CMP/AI_HANDOFF.md`

다음 작업:
- P3 node 2 실행 완료 여부 확인
- clean baseline 개조
- 서버 프로젝트 파일을 GitHub `CMP/tcad/` 구조로 백업

---

## 8. AI HANDOFF

### Last Worker
ChatGPT

### What was just done
- P2 Mg calibration을 완료하여 `NMg=9.59e18 cm^-3`에서 목표 hole density `3.0e17 cm^-3`를 사실상 재현함.
- P3 baseline Micro-LED 구축을 시작하고 Synopsys GaN PiN 공식 예제를 복사하여 node 1 SDE 정상 실행을 확인함.
- 서버 계정 만료 가능성 때문에 현재부터 GitHub 백업을 최우선 병행 작업으로 설정함.

### Next AI should do
- P3 node 2 Forward SDevice가 완료되었는지 먼저 확인한다.
- 완료되면 원본 파일을 보존한 상태에서 P3 clean baseline 개조를 시작한다.
- 동시에 `~/CMP_P2_MG_CALIBRATION`, `~/CMP_P3_BASELINE_MICROLED` 및 그 밖의 CMP 관련 TCAD 폴더를 GitHub `CMP/tcad/` 아래로 복사/백업하도록 사용자를 단계적으로 안내한다.
- input deck과 parameter file은 반드시 보존하고, 대용량 중간 산출물은 저장 필요성을 구분한다.

### Important warnings / unresolved questions
- ALD 최적 material 및 thickness는 아직 확정되지 않음.
- Wet chemical treatment 최적 조건도 아직 확정되지 않음.
- 원본 `GaN_PiN_Diode`에는 Nitride passivation 및 `GaN/Nitride` interface trap이 포함되어 있으므로 clean baseline으로 바로 간주하지 말 것.
- P3 Forward SDevice 원본 재현은 아직 최종 `done: exit(0)` 확인 전 상태임.
- 서버 만료 전 백업이 필수이므로 TCAD 개발과 백업을 병행할 것.

---

## 9. RECOMMENDED FILE MAP

```text
CMP/
├─ README.md
├─ AI_HANDOFF.md
├─ docs/
├─ research/
├─ tcad/
│  ├─ P2_MG_CALIBRATION/
│  └─ P3_BASELINE_MICROLED/
└─ results/
```

### File Roles
- `CMP/README.md`: 프로젝트 전체 개요 및 최종 정리
- `CMP/AI_HANDOFF.md`: ChatGPT ↔ Claude 현재 작업 상태 및 인수인계
- `CMP/research/`: 논문 조사 및 기술 분석
- `CMP/tcad/`: Sentaurus TCAD 코드, 조건, 시뮬레이션 노트
- `CMP/results/`: 실험/시뮬레이션 결과 및 분석
- `CMP/docs/`: 발표, 보고서, 포스터용 내용
