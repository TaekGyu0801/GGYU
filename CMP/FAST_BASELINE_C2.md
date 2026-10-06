# FAST_BASELINE C2 — high-bias runtime strategy

- 작업자: 이택규
- 원안: Claude, 2026-10-06
- ChatGPT 검토: 2026-10-06
- 상태: **PROPOSED / NOT EXECUTED**
- Claude 원안 기준 GitHub main: `cd5572e`
- 현재 full C2 deck은 public repository에 업로드하지 않는다.
- FAST_C2 production deck SHA-256: `b876f614424202e6deaf0655411d7bc15733095da297c1df9ca5ebaacbb578d1`
- C2 smoke deck SHA-256: `dd261ee4fb45b65cf2f5ae8b1a2d707b39b74e2bced61f4e1fac02de6bc414a4`
- Claude strategy source SHA-256: `da430b9ad385f4fac76ec0d94926075ad8b6b6dfd61e053386714601062b7164`
- Claude helper hashes:
  - `make_restart_deck.py`: `c0dc4d99176b27af53e798d6b6e60c59f37f367f8a7cd5475fbab5ee06b861ac`
  - `iv_window.py`: `4dbda566f9b30e0126fcbb65a45c94d1090fb5f7cd432d428daaf600893350a2`

## 1. ChatGPT review verdict

Claude의 중심 진단과 우선순위는 **합리적이며 FAST_C2 후보로 채택할 가치가 있다.** 다만 다음은 확정 사실이 아니라 validation gate를 통과해야 한다.

1. 관측된 `dt*`는 약 4.7 V 부근에서의 **운영상 local convergence ceiling 모델**로 취급한다. 수학적/물리적 hard limit로 확정하지 않는다.
2. `Increment` 및 `Iterations`를 바꾸면 accepted time-step sequence가 바뀐다. Transient + traps 문제에서는 동일한 `RHSMin`/physics만으로 동일 transient state가 자동 보장되지 않는다. 특히 NtSide=1e18은 I-V뿐 아니라 trap charge/occupancy, SRH, radiative/Auger, carrier distribution을 matched-bias에서 검증해야 한다.
3. Claude의 trap emission time 추정은 generic GaN `Nv` 및 thermal velocity 가정을 사용하므로 active SDevice parameterization의 확정값이 아니다. steady/QS cross-check 필요성을 제기하는 근거로만 사용한다.
4. `iv_window.py`의 J 환산은 2D current per 1 um depth + 4 um mesa width를 가정한다. 실제 `AreaFactor`/2D current normalization을 검증하기 전에는 논문/초록 수치로 사용하지 않는다.
5. `InitialTime/FinalTime`, segmented `Goal`, `Save/Load(FilePrefix=...)`, 기존 `Plot(-Loadable)` TDR의 Load 가능 여부는 T-2022.03 실제 실행 또는 manual 확인 전까지 미확인이다.
6. `make_restart_deck.py`, `iv_window.py`는 ChatGPT에서 Python syntax check 및 synthetic-only test를 통과했다. 실제 Sentaurus deck/PLT 검증은 아직 아니다.

## 2. 관측된 runtime 병목

### Node 6 — NtSide=0, FAST_C1

실제 로그의 대표 cycle:

- 큰 시도: `dt = 1.1842e-5`
- Iteration 2–15 동안 `|Rhs| ≈ 1.41e-3` 정체
- `#iterations larger than 15.`
- retry: `dt = 5.9211e-6` (약 정확히 1/2)
- retry는 Iteration 2에서 `|Rhs| = 4.58e-4`로 수렴
- 성공 step 약 21.8 s, 실패 step 약 150 s
- 이후 timestep은 ×1.2로 다시 증가하다가 임계 구간에서 재실패

최근 pseudo-time은 약 `0.9422`, 즉 0→5 V linear ramp 기준 약 4.711 V까지 실제 전진했다.

### Node 12 — NtSide=1e18

실제 로그에서도 동일한 패턴이 보인다.

예:
- `2.1922e-5 -> 1.0961e-5`
- `1.8941e-5 -> 9.4703e-6`
- `1.9638e-5 -> 9.8188e-6`

accepted step은 최근 대체로 2 Newton iterations, 약 18–19 s 수준이며 pseudo-time 약 0.8487, 즉 약 4.243 V까지 전진했다.

### 결론

현재 Node 6/12는 hard stall이나 syntax failure가 아니다. high-bias에서 허용 가능한 timestep이 매우 작아지고, `Increment=1.2`로 다시 키운 뒤 expensive failure와 1/2 cutback을 반복하는 것이 주요 병목이다.

## 3. 독립 cycle-model 재계산

가정:
- local `dt* = 1.1e-5`
- accepted cost ≈ 21.8 s
- Iterations=15 rejected cost ≈ 150 s
- cutback = 0.5

### 현재 C1-like: Increment=1.2, Iterations=15

half-cutback 이후 약 4 accepted steps 뒤 임계값을 다시 넘는다.

이상화 진행률:
- 약 **2.24 mV/h**

이는 실측 약 2.2 mV/h와 잘 맞는다.

### C2 candidate: Increment=1.05, Iterations=8

Iterations=8 rejected cost를 약 81 s로 두면 이상화 진행률:
- 약 **5.24 mV/h**

즉 tail에서 약 2.3× 수준의 모델상 개선 가능성이 있다. 단 이는 measured C2 result가 아니라 모델 추정이다.

## 4. 현재 run에 대한 판단

### 실행 중 설정 변경

현재 실행 중인 sdevice process에 Math/Solve 설정을 동적으로 바꾸는 방법은 확인되지 않았다. 현재 run은 건드리지 않고 reference로 유지한다.

### 현재 run의 즉석 checkpoint

C1 source에는 `Save`가 미리 들어가 있지 않으므로 현재 process에 새 Save를 주입할 수 있다고 가정하지 않는다.

### 기존 intermediate TDR 재시작

현재 C1 intermediate는 `Plot(-Loadable)`로 생성되었다. 실제 Load 가능 여부는 미확인이다.

따라서 Option 3은 D6 Load gate 통과 시에만 허용한다.

## 5. Transient vs Quasistationary

연구 목적은 주로 I-V, IQE, recombination, carrier distribution, sidewall effect 등의 steady/DC 비교다.

Quasistationary가 DC 목적에 더 직접적인 formulation일 수 있으나, 현재 high-bias `dt*` 문제가 QS에서 개선된다는 증거는 없다. 같은 nonlinear path 문제를 겪거나 더 어려워질 수도 있다.

따라서 QS는 현재 runtime 1순위가 아니라:

- C2 checkpoint에서 짧은 tail test
- Node 12 transient-lag / steady-state consistency check

용도로 제한해 검토한다.

NtSide=1e18의 deep trap 시간척도는 현재 deck parameter에서 직접 확인되지 않았으므로 transient result를 논문 DC로 사용할 때 representative bias에서 steady/QS cross-check가 필요하다.

## 6. FAST_C2 proposed solve strategy

동일 global time axis `V_anode = 5 t`를 유지하는 5개 구간 Transient 후보:

| Segment | global t | anode | policy |
|---|---|---|---|
| 1 | 0.00→0.80 | 0→4.0 V | C1 동일: Increment 1.2, Iterations 15 |
| 2 | 0.80→0.88 | 4.0→4.4 V | Increment 1.05, Iterations 8, InitialStep 1e-4 |
| 3 | 0.88→0.92 | 4.4→4.6 V | Increment 1.05, Iterations 8, InitialStep 5e-5 |
| 4 | 0.92→0.96 | 4.6→4.8 V | Increment 1.05, Iterations 8, InitialStep 2e-5 |
| 5 | 0.96→1.00 | 4.8→5.0 V | Increment 1.05, Iterations 8, InitialStep 1e-5 |

제안 checkpoint:
- 4.0 V
- 4.4 V
- 4.6 V
- 4.8 V

Unchanged:
- physics
- geometry
- mesh
- Nt/Et/sigma
- RHSMin=1e-3
- Digits / ErrRef
- ExtendedPrecision
- Blocked + ILS
- 5.0 V final endpoint
- global nominal 5 V/s ramp

단 segmented Transient가 실제로 동일 global time semantics를 유지하는지는 smoke test로 검증해야 한다.

## 7. Iterations=8 gate

기존 x8 audit에서는 accepted Newton iterations max=4가 확인되어 C1의 Iterations=15가 안전한 첫 후보였다.

C2의 high-bias Iterations=8은 다음 조건에서만 시험한다.

1. 현재 Node 6/12 전체 로그에서도 accepted max iteration을 audit
2. accepted max ≤4이면 8 후보 유지
3. 5–6 iteration accepted step이 나오면 8 대신 10 검토
4. C1 reference의 Iterations=15는 변경하지 않음

중요: Iterations cap 변화로 timestep sequence가 달라지므로 NtSide=1e18에서는 matched-bias trap/recombination validation까지 필요하다.

## 8. Candidate priority

### 결정 0 — 분석 범위를 current-density window로 정의할지 팀 결정

가장 큰 runtime 절감 가능성이 있으나 **자동 승인하지 않는다.**

먼저 running `.plt`에서 relevant current window가 어느 voltage에 도달하는지 확인한다.

주의:
- 0→5 V endpoint는 현재 protected baseline condition으로 유지
- production A/B의 분석 window를 J 기준으로 제한할지는 팀 결정
- J normalization은 AreaFactor/2D-depth 검증 전 provisional

### 1순위 — FAST_C2 staged Transient

목표:
- high-bias failed-step frequency 감소: Increment 1.2→1.05
- failed-step cost 감소: Iterations 15→8
- checkpoint 확보

현재 full Node 6/12는 계속 reference로 실행한다.

### 2순위 — half-domain, 이후 remote homogeneous bulk coarsening

조건:
- geometry/doping/contact/trap/BC가 exact mirror symmetry
- physical sidewall 한쪽 + center symmetry boundary
- active/MQW/EBL/heterointerface/5 nm damage는 fine 유지

검증:
- full vs half 같은 bias에서 current normalization
- 2×I_half vs full
- IQE ratio는 ×2 하지 않음
- integrated SRH/Rrad/RAuger
- carrier/current/E-field maps
- Project B는 lateral Ec/Ev 추가

half-domain과 mesh coarsening은 step당 cost를 줄이는 방법이고 timestep-collapse 자체를 해결한다고 가정하지 않는다.

### 3순위 — checkpoint 기반 dt* 원인 실험

D1 로그 진단 후 하나씩:
- linear solver candidate
- QS tail
- RHSMin sensitivity

publication baseline에서 RHSMin을 바로 완화하지 않는다.

## 9. Validation gates

FAST_C2는 다음을 통과하기 전 baseline replacement가 아니다.

### Syntax / execution
- smoke preprocess 성공
- segmented time/voltage trajectory 확인
- Save checkpoint 실제 생성
- Load gate 확인

### Numerical equivalence
- 0–4 V C1과 trajectory/equivalence 확인
- 4 V 이상 matched-bias I-V
- same-current ΔVf
- trap charge/occupancy
- sidewall SRH
- QW radiative / Auger
- QW carrier density
- representative field/current maps

기존 제안 tolerance:
- same-bias I relative difference ≤1e-3
- ΔVf ≤1 mV
- 주요 integrated metric ≤1e-3

이 tolerance 자체도 final publication acceptance 전에 결과 규모와 numerical noise에 맞는지 재검토한다.

## 10. Practical options

### Option 1 — C1 Node 6/12만 그대로 완주

현재 reference를 유지하는 데는 필요하지만 deadline strategy로 단독 사용은 비권장.

### Option 2 — current C1 유지 + FAST_C2 병렬

**현재 추천.**

순서:
1. D1–D5
2. C2 smoke
3. smoke checkpoint Load check
4. C2 preprocess equivalence gate
5. NtSide=1e18 C2 우선
6. 가능하면 NtSide=0 C2
7. 4.0 V까지 C1과 비교
8. 4.4/4.6 V checkpoint에서 DC/QS 및 dt* diagnostic
9. 이후 validated half-domain branch

### Option 3 — 기존 C1 intermediate에서 restart

D6에서 existing `n6_inter_0004_des.tdr` load가 실제 성공할 때만 허용.

Node 6 4.7 V restart가 가능하면 큰 시간 절감 여지가 있다. Node 12는 low/mid bias 구간 비용이 상대적으로 작아 clean C2 restart가 더 단순할 수 있다.

## 11. Immediate D1–D6

### D1 — Newton table diagnosis

```sh
cd /user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1
grep -n -A 25 "Computing BE-step from 0.942217 s to 0.942229 s" n6_des.out | head -40
```

실패 및 성공 retry의 `factor`, `|step|`, `error`, `#inner`, `#iterative`, time 확인.

### D2 — accepted iteration audit

Node 6/12 로그를 copy 후 `sdevice_newton_audit.py` 사용.

보고:
- accepted histogram
- cap 8 false rejection estimate
- rejected count
- rejected wallclock fraction

### D3 — J(V) window

`iv_window.py` 사용 전:
1. `.plt`가 현재 run 중 실제 갱신되는지 확인
2. AreaFactor / 2D current normalization 확인
3. 그 후에만 J 값을 연구 결정에 사용

### D4 — measured progress

1–2시간 간격으로:
```sh
date ; grep "Computing BE-step" n6_des.out | tail -1
```

Node 12도 동일.

### D5 — resource/license availability

```sh
nproc ; uptime ; ps -u semi437 -o pid,etime,pcpu,args | grep sdevice
```

C1 reference를 해치지 않고 C2 smoke/parallel run이 가능한지 판단.

### D6 — existing intermediate Load gate

`make_restart_deck.py`로 scratch deck 생성 후 실제 T-2022.03에서 Load 여부 확인.

Load syntax나 `-Loadable` semantics가 실패하면 Option 3은 즉시 보류하고 manual/official example을 확인한다.

## 12. Helper tools

Public repository에 추가 가능한 proposed helpers:
- `CMP/tcad/tools/make_restart_deck.py`
- `CMP/tcad/tools/iv_window.py`

두 도구는 ChatGPT에서 synthetic-only test를 통과했으며 실제 Sentaurus production data 검증 전까지 **PROPOSED**이다.

Full proprietary C1/C2 SDevice deck 원문은 public GitHub에 commit하지 않는다.

## 13. Final recommendation

**Option 2를 우선한다.**

- 현재 Node 6/12는 그대로 유지한다.
- D1–D5를 먼저 확인한다.
- C2 smoke로 segmented time/Save syntax를 검증한다.
- checkpoint Load가 검증되면 Node 6에 한해 Option 3 tail restart도 병행 검토한다.
- current-density analysis endpoint는 **Decision 0 / TEAM DECISION PENDING**으로 별도 유지한다.
- half-domain + bulk coarsening은 C2와 곱으로 runtime을 줄일 수 있으나 반드시 full/fine equivalence validation 후 채택한다.
