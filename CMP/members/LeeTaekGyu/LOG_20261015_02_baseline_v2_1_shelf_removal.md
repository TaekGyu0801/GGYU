# CMP microLED TCAD — Baseline V2 작업 기록 #02 (2026-10-15)

- 작업자: **이택규** (Claude 연구 스레드에서 실행 보고, ChatGPT에 전달)
- 출처: 사용자가 채팅에 전달한 Claude 보고서 `Baseline V2 작업 기록 #02`
- 이전 기록: `LOG_20261014_01_stall_diagnosis.md` (이 파일의 GitHub 존재는 본 기록에서 확인되지 않음)
- 구분: **USER-REPORTED RUN** — Claude가 실제 서버 실행과 `grep "anode " n*_des.log | tail -3` 결과를 보고. 이 GitHub 기록을 작성한 GPT는 서버 원본 `.log`, `.plt`, 활성 `pp*.cmd` 또는 코드 diff를 직접 열어 검증하지 못함.
- 상태: **전압 목표 도달은 보고됨**, 물리적 Baseline/수지/동일전류 성능은 **UNRESOLVED**

## 1. 실험 구성 (사용자 전달 내용)

| 서버 프로젝트 | 구조 | PolAct | solver | 실행 조건 |
|---|---|---:|---|---|
| `CMP_BASELINE_2.0.0_V2` | **V2.1**: `Wshelf=0`, shelf region 삭제 및 shelf 바닥 cathode 삭제, SDE 재실행 | 0.5 | 기본 solver, `Iterations=20`, `NotDamped=50`, PARDISO 미사용 | n2(`NtSide=0`), n6(`NtSide=1e18`) |
| `CMP_BASELINE_2.0.0_V2_Copy` | 기존 V2: shelf 유지 | 0 | 동일 solver 설정 | n2, n6 |

**중요:** V2.1과 V2_Copy 간에는 *shelf 형상뿐 아니라 PolAct 및 cathode 구성*도 다르다. 과거 shelf+PolAct0.5 정체 보고와 이번 shelf+PolAct0 대조군의 정체가 분극 억제만으로는 해결되지 않음을 지지하지만, 정확한 수치적 실패 원인을 특정 모서리/표면 하나로 확정한 A/B 격리 실험은 아니다.

## 2. 보고된 실행 결과

2D half-domain 전류밀도 정규화는 사용자 정의 `J = (I [A/µm] / 2 µm) × 1e8`를 **전제로** 계산. Half mesa 폭 2 µm, out-of-plane 1 µm, 숨은 `AreaFactor` 없음 여부는 활성 deck/UG에서 후속 확인 필요.

| run | 마지막 V [V] | I_total [A/µm] | 보고/재계산 J [A/cm²] | `didn't converge` 출력 횟수 |
|---|---:|---:|---:|---:|
| V2.1 n2 (`NtSide=0`) | **3.600** | 3.647e-08 | **1.8235** | 0 |
| V2.1 n6 (`NtSide=1e18`) | **3.600** | 9.220e-09 | **0.4610** | 1 |
| V2_Copy n2 (shelf, PolAct=0) | 2.069 (정체/종료 보고) | 1.764e-16 | 8.82e-09 | 17 |
| V2_Copy n6 (shelf, PolAct=0) | 2.036 (정체/종료 보고) | 1.235e-16 | 6.175e-09 | 23 |

V2.1 n2 마지막 세 점: (3.576V, 2.424e-08 A/µm), (3.592V, 3.180e-08 A/µm), (3.600V, 3.647e-08 A/µm).

- 재계산 `n2 J=3.647e-08 / 2 × 1e8=1.8235 A/cm²`; `n6 J=9.220e-09 / 2 × 1e8=0.4610 A/cm²`.
- `I_n6/I_n2=9.220e-09 / 3.647e-08=0.2528` (동일 3.6V, 약 25.3%).
- 마지막 두 점의 단순 국소 `n = ΔV / [(kT/q) ln(I_2/I_1)]`, 300K, `ΔV=0.024V`, `I_2/I_1=3.647/2.424` → `n ≈ 2.27`. **두 점의 수학적 유도값이며 지배 수송 메커니즘 증거는 아님**.

## 3. 판정과 미해결 사항

1. **보고된 RUN 성과:** shelf를 없앤 V2.1 n2/n6 모두 목표 3.6V 도달. 이전 기본 solver의 2.0–2.3V 수렴 정체와 구분되는 중요한 해결.
2. **대조군의 의미:** shelf를 유지한 채 PolAct=0으로 바꾼 n2/n6는 각각 2.069/2.036V에서 정체 보고. *분극을 끄는 것만으로는 해결되지 않음*이 지지됨.
3. **원인 해석 한계:** shelf 제거·자유표면/메사 모서리 변화·cathode 경계조건이 함께 바뀜. 국소 캐리어 농도/전기장/메쉬 조건 중 정확한 불안정 메커니즘은 **확인되지 않음**. `PolAct=0` 대조군만으로 모든 분극의 역할을 일반적으로 기각하는 것은 과도함.
4. **NtSide=1e18에서 I 감소:** 동일 전압 전류가 `NtSide=0`의 약 1/4. acceptor trap 음전하에 의한 측벽 공핍은 **가설**; 전하/점유/재결합·전류선 데이터 없이 메커니즘 확정 불가.
5. **물리 검증 미완료:** 3.6V에서의 전류밀도만으로 turn-on 전압이 높은지 문헌 대비 판단 불가. `bl2_check.py` QW/EBL/측벽 적분, 전자·정공 유출입, qR/I 해석 필요. **q∫R/I≈1을 누설과 경계 플럭스 검증 없이 절대 통과조건으로 쓰면 안 됨**. IQE는 동일 QW 영역의 `Rrad/(Rrad+RSRH+RAuger)` 등 정의 구분 필요.
6. **A/B 구현 영향:** shelf 제거와 cathode 0–2µm 구성 변경은 lateral spreading/전류 경로에 영향을 줄 수 있음. 영향이 '작다'는 가설은 미검증. half/full·mesh·contact 민감도 검증 필요.

## 4. 작업자 의사결정 (2026-10-15)

- **V2.1 (Wshelf=0)을 다음 검증의 작업용 기준 구조로 채택**한다는 Claude/이택규 보고.
- shelf 포함 V2는 이 스윕에서 사용하지 않는 것으로 보고. 향후 lateral LED `Cath=1` 옵션 재사용 시 수렴 문제를 별도로 다뤄야 함.
- 이 결정을 **전체 팀의 물리 검증 완료 또는 Common Baseline final freeze**라고 표현하지 않는다.
- 명명/계보 유의: 서버 디렉터리 `CMP_BASELINE_2.0.0_V2`가 V2.1 내용을 갖는다고 보고됨. 유효한 `pp*`/SDE/파라미터 해시를 기록하기 전 단순 파일명으로 버전 동일성을 주장하지 않는다.
- 보고된 소스: `SWB_PASTE/sde_dvs.cmd` (`Wshelf=0`), `sdevice_des.cmd` (기본 solver 설정). **GitHub 활성 코드 파일이 그 상태라고 가정하지 않음**.

## 5. 다음 단계 (우선순위)

1. V2.1 n2/n6 실제 `n*_des.log`, `n*_des.plt`, effective `pp*.cmd/par` 및 메쉬/접촉/AreaFactor 확인; 두 n의 3.6V 종료 및 물리 모델을 읽기 전용 재검증.
2. `bl2_check.py` 후처리 검증/실행: J–V; QW Radiative/SRH/Auger, EBL·sidewall 재결합, current balance (leakage·flux 고려), Trap 점유/공핍 및 동일 전류 비교. 예전 스크립트의 IQE 및 qR/I 판정 오류 우선 확인.
3. 기준 논문 I–V와 정량 비교, turn-on 전압·물성/수송 물리 검증.
4. 검증 통과 시 S3 (`PolAct=1.0`) 대조군 → Project A `GaN:C` / Project B `AlGaN` 파일럿(동일 전류, 보호된 공통 baseline).
5. 필요 시 검증된 `n@node@_end` 재시작 checkpoint에서 4–5V 확장(run/Save–Load 유효성 확인 후 별도 복사본에서 실행).

## 6. 교훈

- 대조군과 실패 Newton 최대오차 좌표로 불안정 위치를 좁혔다는 Claude의 보고는 실무상 유익함. 다만 좌표가 가리킨 영역이 곧 단일 확정 원인은 아님.
- 본 문서는 **사용자 전달 외부 AI/서버 결과의 투명한 기록**이며, GPT가 직접 학교 서버를 실행/검증했다는 주장이 아님.
