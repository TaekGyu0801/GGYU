# Claude FAST_BASELINE Implementation Prompt

작업자: 이택규  
상태: READY FOR IMPLEMENTATION  
구현 담당: Claude  
검토/검증: ChatGPT + 연구자

---

## 1. 작업 시작 전에 반드시 읽을 GitHub 문서

다음 순서로 최신 상태를 실제 GitHub에서 읽고 시작한다.

1. `CMP/AI_SHARED_MEMORY_PROTOCOL.md`
2. `CMP/AGENTS.md`
3. `CMP/CLAUDE_PROJECT_INSTRUCTIONS.md`
4. `CMP/.ai-sync/LIVE_STATE.md`
5. `CMP/.ai-sync/LIVE_STATE.json`
6. `CMP/.ai-sync/RELAY.md`
7. `CMP/CURRENT_STATUS.md`
8. `CMP/ERROR_LOG.md`
9. `CMP/NEXT_ACTIONS.md`
10. `CMP/TEAM_TIMELINE.md`
11. `CMP/members/LeeTaekGyu/TIMELINE.md`
12. GitHub LIVE LOG Issue #7 최신 comment
13. `CMP/references/TCAD_REFERENCE_INDEX.md`
14. 이 문서

중요:
`CMP/tcad/CURRENT/sdevice2_defect_on.cmd`는 active Copy x8 실행 원본과 일치하지 않는 stale source로 확인된 적이 있다.
FAST_BASELINE 구현의 기준 파일로 사용하지 않는다.

---

## 2. Claude가 실제로 맡을 일

Claude가 FAST_BASELINE의 Sentaurus 코드를 처음부터 끝까지 작성한다.

ChatGPT가 완성 patch를 넘기는 것이 아니다.
Claude가 exact Copy x8 source, T-2022.03 공식 자료, 실제 runtime evidence를 검토한 뒤 numerical-only 최적화 방안을 판단하고 complete source를 만든다.

최종 산출물은 부분 snippet이 아니라 바로 복붙 가능한 전체 코드여야 한다.

---

## 3. Claude에 별도로 첨부할 exact golden source

사용자가 Claude 채팅에 아래 파일을 직접 첨부한다.

`Copy_x8_sd_fdiv_des.cmd`

expected SHA-256:

`56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`

가능하면 코딩 전 hash를 확인한다.

첨부 파일이 이 hash/revision과 다르면 코딩을 시작하지 말고 mismatch를 먼저 보고한다.

이 full source는 public GitHub에 그대로 올리지 않는다.

---

## 4. Copy x8 golden reference hashes

다음은 freeze된 Copy x8 reference다.

- `n1_msh.tdr`
  - `762d2d57a352a00bb030b968985cbf3b71d53118c68e5c53b7586e613f392ea3`

- `pp1_dvs.cmd`
  - `5685528bc3ec338ce104040b0503be43ef032094976d69995529eb5d6fb4e658`

- `pp6_des.cmd`
  - `2dfcc98effe145ec944fb8ee5d6914f5f098e54d1bf2319c69acc76afe1692e6`

- `pp6_des.par`
  - `60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039`

- `sd_fdiv_des.cmd`
  - `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`

FAST implementation은 이 frozen reference를 기준으로 한다.

---

## 5. 연구 목적

이 프로젝트는 planar InGaN/GaN MicroLED의 damaged sidewall loss를 줄이는 연구다.

핵심 논문 프레임은 Defect-Access Engineering이다.

같은 damaged sidewall physics를 유지한 상태에서:

- Project A:
  localized GaN:C / carbon-induced high-resistance edge
  → resistive carrier blocking

- Project B:
  localized AlGaN lateral heterobarrier
  → band-offset carrier blocking

을 비교한다.

증명해야 하는 causal chain:

edge carrier/current access 감소
→ integrated sidewall SRH 감소
→ MQW radiative recombination / IQE 보존 또는 증가
→ Vf / current crowding / Auger penalty 정량화

따라서 FAST_BASELINE은 과학적 baseline을 바꾸는 작업이 아니라
동일 물리 해를 훨씬 짧은 시간에 재현하기 위한 numerical optimization이다.

---

## 6. 절대 임의 변경 금지

FAST runtime 최적화 과정에서 아래 baseline physics를 바꾸지 않는다.

- 2D Cartesian common baseline
- representative mesa width = 4 µm modeling choice
- sidewall damage width = 5 nm
- 300 K
- vertical epitaxy / geometry
- contacts
- Fermi
- Thermionic
- Piezoelectric_Polarization(strain)
- EffectiveIntrinsicDensity(NoBandgapNarrowing)
- SRH
- Auger
- Radiative
- 현재 mobility framework
- anisotropic Poisson
- p-GaN에 region-scoped된 Mg incomplete ionization
- generic sidewall acceptor trap
  - `Conc = @NtSide@`
  - `Et = Ev + 0.75 eV`
  - `eXsection = 1e-15 cm^2`
  - `hXsection = 1e-15 cm^2`
- Workbench NtSide DOE intent
  - 0
  - 1e17
  - 1e18 nominal
  - 1e19
- forward target = 5.0 V
- paper analysis에 필요한 spatial outputs

generic sidewall trap을 Project-A carbon defect라고 해석하지 않는다.

---

## 7. exact Copy x8 source에서 확인된 numerical baseline

### Math

- `NumberOfThreads = 4`
- `ParallelLicense(Wait)`
- `Wallclock`
- `Digits = 5`
- `ErrRef(electron) = 1.0e4`
- `ErrRef(hole) = 1.0e4`
- `RHSMin = 1e-3`
- `CheckRhsAfterUpdate`
- `Transient = BE`
- `ExtendedPrecision(80)`
- `TensorGridAniso(aniso)`
- `ComputeDopingConcentration`
- `Method = Blocked`
- `SubMethod = ILS(set=22)`

ILS set 22:

- `gmres(100)`
- `tolrel=1e-10`
- `tolunprec=1e-4`
- `maxit=200`
- `ilut(1e-08,-1)`
- symmetric ordering = nd
- nonsymmetric ordering = mpsilst
- `refineresidual=10`

### Solve

Initial Poisson:

- `Iterations = 500`
- `LineSearchDamping = 1e-2`

Equilibrium carrier solution:

- `Iterations = 100`

Forward Transient:

- `InitialStep = 1e-5`
- `MinStep = 1e-9`
- `MaxStep = 1e-3`
- `Increment = 1.2`
- anode `Goal Voltage = 5.0`
- inner `Coupled { Poisson Electron Hole }`
- golden source의 transient inner Coupled에는 explicit `Iterations`가 없음

Intermediate 2D saves:

- t=0.80
- 0.84
- 0.88
- 0.92
- 0.94
- 0.96
- 0.97
- 0.98
- 0.985
- 0.99
- 0.995

approximately 4.0–4.975 V 구간의 spatial state를 남기기 위한 출력이다.

---

## 8. 실제 관찰된 runtime 병목

현재 baseline은 물리적으로 쓸 수 있지만 계산시간이 너무 길다.

실제 관찰:

- high-bias 약 4.6–4.7 V 구간이 주요 병목
- 정상 accepted step은 소수 Newton iteration과 수십 초 수준일 수 있음
- 일부 step은 convergence threshold 부근에서 stagnation
- rejected step이 약 40–50 nonlinear iteration까지 소비
- rejected step 하나가 1000 s 이상 소모된 사례 존재
- 이후 timestep cutback/retry
- 이 반복 때문에 multi-day runtime 발생

필요한 sweep:

- NtSide
- mesa size
- mesh convergence
- Project A
- Project B

때문에 현재 runtime으로는 연구 진행이 비현실적이다.

---

## 9. 중요한 provenance

Copy x8이 현재 preferred v1.2 reference다.

Copy x7 vs x8 조사 결과:
- underlying device/physics/numerics는 같은 계열
- x8의 핵심 차이는 intermediate spatial TDR saves
- runtime slowdown을 새로운 physics 차이로 설명할 근거는 없음

historical Sep26 Node12 initialization failure는 current Sep28 deck 결과로 취급하지 않는다.

current baseline source는 Mg incomplete ionization을 p-GaN region에 한정한다.

public GitHub CURRENT SDevice source를 coding base로 사용하지 않는다.

---

## 10. 이전 ChatGPT 제안 처리

ChatGPT가 한때 transient inner Coupled에 `Iterations=15`를 넣는 아이디어를 제안했다.

이것은 **PROPOSED hypothesis**일 뿐, 확정 patch가 아니다.

Claude는 이를 반드시 독립적으로 검토한다.

아래를 기준으로 더 나은 첫 후보가 있으면 다른 numerical strategy를 선택해도 된다.

- exact attached source
- T-2022.03 공식 User Guide / example
- 실제 observed solver behavior
- 현재 installation에서 지원되는 syntax

Claude가 최종 코드를 결정한다.

---

## 11. 구현 원칙

첫 FAST candidate는 가능한 한:

- minimal
- numerical-only
- 한 번에 한 change group

으로 만든다.

우선 검토 영역:

1. nonlinear Newton iteration / early cutback behavior
2. transient stepping / staged ramp
3. ErrRef/tolerance sensitivity
4. linear solver settings
5. far-field mesh reduction

우선 solver-side optimization을 검토한다.

mesh를 건드릴 경우에도:
- MQW
- 5 nm sidewall damage
- heterointerface
- 중요한 current path

는 보호한다.

여러 numerical group을 동시에 바꿔야 한다면 이유를 명시한다.

---

## 12. output은 유지해야 한다

FAST candidate도 논문 분석이 가능해야 한다.

필수 분석 가능 항목:

- I–V
- sidewall SRH
- RadiativeRecombination
- AugerRecombination
- eDensity / hDensity
- Current / eCurrent / hCurrent
- band edges
- electric field
- polarization
- spatial state at representative high-bias / same-current comparison points

output schedule을 줄이거나 바꾸면:
- runtime gain 이유
- 잃는 정보
- 대체 저장 전략

을 명확히 설명한다.

---

## 13. Claude가 반드시 제출할 산출물

### 1. Complete FAST_BASELINE SDevice source

- 전체 코드
- copy-paste-ready
- snippet 금지

### 2. Change table

각 변경마다:

- original
- modified
- 이유
- 예상 runtime effect
- numerical/scientific risk

### 3. Unified diff

golden Copy x8 vs FAST candidate.

physics/trap이 바뀌지 않았는지 사람이 바로 확인 가능해야 한다.

### 4. Workbench 적용법

- 어떤 새 copy/project를 만들지
- 어느 source file을 교체할지
- NtSide variable/split을 어떻게 유지할지
- live x8을 건드리지 않는 방법
- preprocess 순서

### 5. Generated input 검증법

다음에서 무엇을 비교해야 하는지 작성:

- pp1_dvs.cmd
- pp6_des.cmd
- pp6_des.par
- mesh statistics
- node/workbench variable substitution

intentional diff와 unexpected diff를 구분한다.

### 6. Short benchmark plan

full 0→5 V multi-day run부터 시작하지 않는다.

현재 high-bias 병목을 최대한 빨리 드러내는 benchmark 방법을 설계한다.

기록할 것:

- accepted/rejected step
- pseudo-time
- anode voltage
- timestep
- Newton iterations
- linear iterations
- wallclock
- cutback 횟수

### 7. Acceptance criteria

Copy x8 reference와 matched bias/current에서 비교:

- current / I–V
- convergence
- timestep behavior
- Newton iteration
- wallclock
- spatial recombination/carrier/current 결과

### 8. Reject / rollback 조건

어떤 차이가 발생하면 candidate를 폐기할지 명시한다.

### 9. 상태

실행 전 코드는 반드시:

`PROPOSED`

로 표시한다.

실행하지 않은 코드를 CONFIRMED라고 쓰지 않는다.

---

## 14. FAST candidate 검증 철학

빠르기만 하면 채택하지 않는다.

다음 physical/numerical solution이 Copy x8과 paper-level comparison에 충분히 일치해야 한다.

- I–V
- sidewall SRH
- MQW radiative
- Auger
- carrier distribution
- current redistribution
- band/electric-field behavior where relevant

정확도를 몰래 완화하지 않는다.

equivalence는 실제 run 전에는 claim하지 않는다.

---

## 15. 작업 순서

현재 합의된 순서:

1. Copy x8 golden reference freeze — 완료
2. Claude가 separate FAST_BASELINE code 작성 — 현재 단계
3. short benchmark
4. numerical group을 하나씩 refine
5. final FAST candidate 선정
6. JuSubin / LeeTaekGyu clean-account reproduction
7. final FAST baseline freeze
8. Project A/B production runs

clean-account reproduction은 필수지만,
첫 FAST code 작성 전 blocker는 아니다.

---

## 16. GitHub 기록 규칙

이택규의 Claude는 GitHub를 READ할 수 있지만 WRITE/EDIT 권한이 없다.

따라서 Claude는 GitHub에 직접 기록했다고 주장하면 안 된다. 구현이 끝나면 아래 내용을 채팅 답변에 명확히 정리해 사용자/ChatGPT가 기록할 수 있게 한다.

- source hash
- FAST candidate hash
- numerical diff summary
- exact numerical settings
- benchmark plan
- benchmark result(실행한 경우만)
- status label
- 어떤 GitHub 파일에 어떤 내용을 기록해야 하는지 제안

실제 GitHub WRITE는 ChatGPT가 검토 후 수행한다.

public repository에는 proprietary full Sentaurus source를 commit하지 않는다.

---

## 17. Claude 첫 응답 형식

attached golden source와 GitHub를 모두 읽은 뒤 먼저 다음을 짧게 보고한다.

1. 현재 baseline 상태
2. 사용 중인 golden source hash
3. 실제 runtime bottleneck
4. 절대 변경하지 않을 physics
5. 선택한 첫 FAST numerical strategy와 근거

그 다음 complete code implementation으로 진행한다.

GitHub와 첨부 source가 충돌하면 코딩 전에 먼저 conflict를 보고한다.
