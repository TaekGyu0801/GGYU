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
- P3 baseline Micro-LED 구축 진행 중
  - Synopsys `GaN_PiN_Diode` 예제를 `~/CMP_P3_BASELINE_MICROLED`로 복사함
  - 원본 성공 상태를 `~/CMP_P3_BASELINE_MICROLED_ORIGINAL_OK`로 동결 보존함
  - 원본 SDE node 1 정상 완료
  - 원본 Forward SDevice node 2 정상 완료: `done: exit(0)`
  - P3A 단계에서 p-side를 `pMagnesiumActiveConcentration=9.59e18 cm^-3`로 변경
  - P2 Mg incomplete-ionization model을 `sdevice.par`에 반영
  - `pp1_dvs.cmd`에서 실제 Mg 값 `9.59e18` 반영 확인
  - P3A SDE node 1 정상 완료
  - P3A Forward SDevice node 2 정상 완료: `done: exit(0)`
  - P3A Forward sweep가 10 V까지 완료되고 `n2_des.tdr` 생성 확인
  - P3A 성공 상태를 `~/CMP_P3A_MG_BASELINE_OK`로 동결 보존함
  - P3B 단계에서 원본 Nitride passivation, Nitride 전용 mesh 조건, `GaN/Nitride` interface trap을 제거
  - mesa cut 형상은 임시 `Gas` 영역 `tmp_mesa`를 생성 후 즉시 삭제하는 방식으로 유지
  - P3B 전처리 파일에서 `Nitride`/`Passivation`이 사라지고 Mg `9.59e18`이 유지됨을 확인
  - P3B SDE node 1 정상 완료
  - P3B Forward SDevice node 2 정상 완료: `done: exit(0)`
  - P3B Forward sweep가 10 V까지 완료되고 `n2_des.tdr` 생성 확인
  - P3B 10 V total current: `2.103e-01 A`
- P2/P3 전체 서버 스냅샷을 `CMP_TCAD_BACKUP_20260827.tar.gz`로 생성 및 로컬 보존
  - SHA256: `c8bc05d0bbb86415859bddd544ccf2a8b5a8f8abdebb1ee9b571ae1b2371c3dc`
  - 공개 GitHub에는 라이선스 이슈를 피하기 위해 Synopsys 원본 전체 대신 프로젝트별 재현 기록, 사용자 작성 코드, 결과 요약을 업로드함

---

## 4. CURRENT TASK

현재 우선순위:

1. P3B clean GaN PiN 성공 상태를 별도 checkpoint로 복제/보존
2. P3B를 clean electrical reference로 사용하여 InGaN/GaN MQW baseline 추가
3. MQW baseline 안정화 후 polarization/heterointerface 조건을 단계적으로 정리
4. Sidewall SRV 및 pixel size DOE로 확장
5. Wet chemical treatment / ALD passivation을 sidewall defect activity 또는 effective SRV 감소로 연결
6. 서버 계정 만료 전 새로 생성되는 프로젝트별 checkpoint를 계속 로컬/GitHub에 보존

---

## 5. IMPORTANT DECISIONS

- Sidewall damage가 프로젝트의 핵심 문제이다.
- Wet Chemical Treatment + ALD Passivation을 핵심 개선 공정으로 사용한다.
- Reverse Leakage Current, EQE, EL Image, Reliability를 주요 평가 지표로 본다.
- 검증되지 않은 공정 조건이나 최적값을 확정 사실처럼 기록하지 않는다.
- 논문 근거, 실험 결과, 추정/가설을 명확히 구분한다.
- CMP 프로젝트 진행에 의미 있는 활동은 사용자가 매번 따로 요청하지 않아도 `AI_HANDOFF.md`에 자동 기록한다.
- P2 Mg calibration 최종 기준값은 현재 `NMg = 9.59e18 cm^-3`로 사용한다.
- P3는 복잡한 MQW/sidewall 구조를 한 번에 만들지 않고, 공식 GaN PiN 예제 재현 → P3A calibrated Mg → P3B clean baseline → MQW → sidewall 순서로 단계적으로 확장한다.
- 서버 계정 만료 전에 재현 가능한 형태로 input deck, parameter file, extraction script, 결과 요약을 GitHub에 남긴다.
- Synopsys Applications Library 원본/복사본은 공개 저장소에 그대로 재배포하지 않고 private/local archive에 보존한다.
- P3 공식 GaN PiN 원본 성공 상태는 `CMP_P3_BASELINE_MICROLED_ORIGINAL_OK`로 동결 보존한다.
- P3A는 `calibrated Mg + original Nitride/interface trap` 상태로 정의하며, clean baseline과 구분한다.
- P3B는 `calibrated Mg + original Nitride/interface trap 제거` 상태이며 이후 MQW/sidewall 연구의 clean reference로 사용한다.
- P3A와 P3B의 10 V total current 차이는 checkpoint 비교로만 해석하며, passivation 효과 하나로 단정하지 않는다. 두 단계는 Nitride geometry와 interface-trap physics가 동시에 다르다.

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

### 2026-08-27 — ChatGPT

작업 내용:
- P3 Synopsys `GaN_PiN_Diode` 원본 Forward SDevice(node 2)를 재실행하여 완료 여부 확인

결과:
- `job 2 <sdevice> done: exit(0)` 확인
- 전체 실행 시간 약 176초
- SDE node 1과 Forward SDevice node 2 모두 현재 서버 환경에서 정상 재현됨
- P3 clean baseline 개조 전에 사용할 검증된 기준 상태 확보

생성/수정 파일:
- `CMP/AI_HANDOFF.md`

다음 작업:
- P2/P3 서버 파일을 먼저 GitHub에 백업
- 이후 P3 clean baseline 개조 시작

---

### 2026-08-27 — ChatGPT

작업 내용:
- P2/P3 전체 프로젝트를 `CMP_TCAD_BACKUP_20260827.tar.gz`로 압축하여 로컬 백업
- SHA256 무결성 확인
- GitHub `CMP/tcad/`에 public-safe 재현 기록과 P2 사용자 작성 calibration artifact 업로드
- 원본 성공 상태를 `~/CMP_P3_BASELINE_MICROLED_ORIGINAL_OK`로 복제 및 `n2_des.sta=done` 확인

결과:
- 서버 계정이 사라져도 P2/P3 현재 상태를 복구할 수 있는 full local archive 확보
- 공개 GitHub에는 라이선스 원본을 재배포하지 않고 재현 가능한 project metadata/결과를 남김

생성/수정 파일:
- `CMP/tcad/README.md`
- `CMP/tcad/BACKUP_MANIFEST_20260827.md`
- `CMP/tcad/P2_MG_CALIBRATION/README.md`
- `CMP/tcad/P2_MG_CALIBRATION/CALIBRATION_RESULTS.csv`
- `CMP/tcad/P2_MG_CALIBRATION/equilibrium_mg_calibration_des.cmd`
- `CMP/tcad/P2_MG_CALIBRATION/extract_hdensity.tcl`
- `CMP/tcad/P2_MG_CALIBRATION/extract_hdensity_n62.tcl`
- `CMP/tcad/P3_BASELINE_MICROLED/README.md`
- `CMP/AI_HANDOFF.md`

다음 작업:
- P3A calibrated Mg 단계 진행

---

### 2026-08-27 — ChatGPT

작업 내용:
- P3A 단계로 p-side dopant를 generic `PDopantActiveConcentration 1e19`에서 `pMagnesiumActiveConcentration 9.59e18`로 변경
- P2 calibration의 Mg incomplete-ionization model(`E_0=0.2`, `alpha=8e-9`, `g=4`, `Xsec=1e-14`)을 P3 `sdevice.par`에 반영
- `pp1_dvs.cmd`를 확인하여 실제 전처리된 SDE에 `pMagnesiumActiveConcentration 9.59e18`이 들어갔음을 검증
- P3A node 1 SDE 실행
- P3A node 2 Forward SDevice 실행

결과:
- node 1: `done: exit(0)`
- node 2: `done: exit(0)`
- gsub 총 실행 시간 약 203초
- SDevice wallclock 약 198.36초
- 10 V까지 Forward sweep 완료 및 `Curve trace finished.` 확인
- `n2_des.tdr` 정상 생성
- 최종 10 V total current 약 `2.323e-01 A`
- P2에서 보정한 Mg 농도/ionization model을 GaN PiN baseline에 이식해도 Forward solution이 정상 수렴함을 검증

생성/수정 파일:
- `CMP/tcad/P3_BASELINE_MICROLED/README.md`
- `CMP/AI_HANDOFF.md`

다음 작업:
- P3A 성공 상태 checkpoint를 보존
- 원본 Nitride passivation 및 GaN/Nitride interface trap을 제거한 clean baseline 구성

---

### 2026-08-27 — ChatGPT

작업 내용:
- P3A 성공 상태를 `~/CMP_P3A_MG_BASELINE_OK`로 동결 보존
- P3B clean baseline을 위해 원본 Nitride passivation geometry와 Nitride-specific mesh 조건 제거
- mesa 형상은 임시 `Gas` 영역 `tmp_mesa`를 생성 후 삭제하는 방식으로 유지
- Forward deck의 `GaN/Nitride` interface trap block 제거
- 전처리 파일에서 `Nitride`/`Passivation`이 제거되고 Mg `9.59e18`이 유지되는지 검증
- P3B node 1 SDE와 node 2 Forward SDevice 실행

결과:
- node 1: `done: exit(0)`
- node 2: `done: exit(0)`
- gsub 총 실행 시간 약 86초
- SDevice wallclock 약 80.63초
- 10 V까지 Forward sweep 완료 및 `Curve trace finished.` 확인
- `n2_des.tdr` 정상 생성
- 최종 10 V total current 약 `2.103e-01 A`
- P3A의 `2.323e-01 A` 대비 약 `0.0220 A`, `9.47%` 감소
- 단, 이 차이는 Nitride geometry와 interface trap이 함께 제거된 결과이므로 단일 passivation 효과로 해석하지 않음
- P3B를 이후 MQW/sidewall 개발의 clean electrical reference로 채택

생성/수정 파일:
- `CMP/tcad/P3_BASELINE_MICROLED/README.md`
- `CMP/AI_HANDOFF.md`

다음 작업:
- P3B 성공 상태를 별도 checkpoint로 복제/보존
- 이후 InGaN/GaN MQW baseline 추가

---

## 8. AI HANDOFF

### Last Worker
ChatGPT

### What was just done
- P3A 성공 상태를 `CMP_P3A_MG_BASELINE_OK`로 동결 보존함.
- 작업본에서 original Nitride passivation 및 `GaN/Nitride` interface trap을 제거하여 P3B clean GaN PiN baseline을 구성함.
- P3B node 1 SDE와 node 2 Forward SDevice가 모두 `exit(0)`으로 완료되었고 10 V forward sweep까지 정상 종료됨.
- P3B 10 V total current는 `2.103e-01 A`이며 P3A `2.323e-01 A`보다 약 9.47% 낮음.
- 이 전류 차이는 passivation 단일 효과로 해석하지 않고 checkpoint 차이로만 기록함.
- P3B를 다음 MQW 단계의 clean reference로 사용하기로 함.

### Next AI should do
- 현재 `~/CMP_P3_BASELINE_MICROLED` 성공 상태를 `~/CMP_P3B_CLEAN_BASELINE_OK` 같은 별도 checkpoint로 복제하고 `n2_des.sta=done`을 확인한다.
- 그 후 작업본에서 InGaN/GaN MQW baseline을 한 단계씩 추가한다.
- p-side `pMagnesiumActiveConcentration=9.59e18 cm^-3`와 P2 Mg incomplete-ionization parameter는 유지한다.
- MQW 구조 추가 시 geometry → mesh → material/physics → SDevice 순으로 단계적으로 검증한다.
- clean baseline 이후 sidewall/SRV와 pixel-size DOE로 확장한다.

### Important warnings / unresolved questions
- P3A와 P3B의 전류 차이는 Nitride region과 interface trap이 동시에 달라졌기 때문에 passivation 효과 하나로 단정하면 안 된다.
- ALD 최적 material 및 thickness는 아직 확정되지 않음.
- Wet chemical treatment 최적 조건도 아직 확정되지 않음.
- Reverse leakage를 defect-assisted transport까지 정량적으로 맞추려면 추후 추가 물리모델/calibration이 필요할 수 있음.
- Synopsys Applications Library 원본은 공개 GitHub에 그대로 복사하지 않는다.

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
