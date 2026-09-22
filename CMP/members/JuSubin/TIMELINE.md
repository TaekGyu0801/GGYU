# Ju Subin Timeline

## 2026-09-21 — Common Baseline 코드 최종 수정 보고 / 장시간 run 전 최종 검토

- **작성자:** ChatGPT (공유 프로젝트 대화 동기화)
- **작업자:** 주수빈
- **구분:** Common Baseline 검토 / simulation 준비
- **상태:** OBSERVED — 주수빈 채팅의 사용자 보고 기준
- **작업 내용:** 주수빈이 메인 SDevice 코드를 포함해 앞서 검토된 관련 코드들을 최종 수정했다고 보고함.
- **현재 판단 요청:** Project A와 Project B 모두에 사용할 Common Baseline으로 적합한지, 장시간 simulation을 시작하기 전에 코드와 논리를 마지막으로 꼼꼼히 검토하는 단계.
- **우선 실행 계획:** 전체 Nt sweep을 바로 돌리지 않고 먼저 `NtSide=0`과 `NtSide=1e18` 두 조건을 실행해 baseline 동작을 확인할 계획.
- **비용/제약:** 주수빈 보고 기준으로 한 조건의 simulation이 약 3일 소요될 수 있어, run 전 검증을 우선함.
- **주의:** 이 동기화 시점에는 주수빈 측 최신 전체 코드 원문과 실제 simulation 결과를 GitHub에서 직접 검증하지 못했으므로 코드 정확성/실행 성공은 CONFIRMED로 기록하지 않음.
- **다음:** 주수빈 측 최신 전체 코드 동기화 → baseline 최종 정적 검토 → `NtSide=0`, `NtSide=1e18` 실행 → 결과/로그 GitHub 기록.

---

## 2026-09-22 — NtSide split 실행 중 SWB 실행 순서 점검

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Common Baseline / Workbench dependency diagnostic
- **상태:** OBSERVED + UNRESOLVED
- **관찰:** 사용자가 Sentaurus Workbench 화면에서 NtSide=0, 1e18 두 split을 준비/실행하는 과정에서 SDE보다 SDevice가 먼저 동작하는 것처럼 보인다고 보고함.
- **해석:** NtSide가 SDevice에서만 사용되고 SDE geometry/mesh가 이미 유효한 upstream 결과라면 SWB가 SDE를 재실행하지 않고 같은 SDE 결과를 재사용해 SDevice split부터 실행하는 것은 정상일 수 있음.
- **주의:** 반대로 해당 experiment에서 SDE가 한 번도 성공적으로 실행되지 않았는데 SDevice가 시작된다면 SDE→SDevice dependency 또는 SDevice File/Grid 입력 연결을 확인해야 함.
- **다음 확인:** SDevice preprocessed `pp*_des.cmd`의 `File { Grid=... }`가 실제 SDE 생성 TDR을 가리키는지, 그리고 SDE output에 해당 mesh TDR이 존재하는지 확인.

---

## 2026-09-22 — SDE→SDevice dependency 정상 확인

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Workbench dependency diagnostic
- **상태:** CONFIRMED
- **근거:** Node 6 Explorer의 preprocessed `pp6_des.cmd`에서 `File { Grid = "n1_msh.tdr" }` 확인. 동일 Node 6 output 목록에 `n6_des.tdr`, `n6_des.plt`, `n6_des.log` 존재.
- **판단:** 현재 SDevice Node 6는 SDE에서 생성된 Node 1 mesh `n1_msh.tdr`을 정상 입력으로 사용 중이며, SDevice 자체 TDR도 정상 생성하고 있음.
- **결론:** NtSide split 실행에서 SDE가 다시 돌지 않고 SDevice부터 실행되는 현상은 기존 SDE mesh를 재사용하는 정상 동작으로 판단됨. NtSide가 SDE geometry를 바꾸지 않는 한 SDE 재실행은 필수 아님.

---


## 2026-09-22 — NtSide run 장시간 실행 상태 점검

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** SDevice runtime / convergence diagnostic
- **상태:** OBSERVED
- **관찰:** 사용자가 전날 밤부터 실행해 18시간 이상 지난 Node 6 SDevice output을 공유함. 화면상 계산은 정지하지 않았고 BE step을 계속 진행 중임.
- **근거:** `n6_des.out`에 직전 step이 `|Rhs| < 1.0000E-03`로 수렴 완료된 뒤, 다음 BE step이 약 `0.0766738 → 0.0776738`, `Stepsize = 1.0000E-03`로 진행 중. 직전 step 누적 wallclock은 Assembly 약 598.77 s, Solve 약 2928.83 s, Total 약 3563.68 s로 약 59분/step 수준.
- **판단:** 현재 화면만 보면 hang/fatal error라기보다 각 BE step 계산비용이 매우 큰 장시간 run 상태. 18시간 미완료 자체는 현재 step cost와 양립함.
- **추가 관찰:** `.err`의 vanOverstraetendeMan E0 isotropic/anisotropic 값 차이 메시지는 경고로 보이며, 현재 화면에서 run 중단 원인으로 관찰되지는 않음.
- **다음:** `pp6_des.cmd`의 Solve 블록에서 현재 transient/BE 구간의 최종 목표 시간(또는 ramp 목표), InitialStep/MinStep/MaxStep/Increment 설정을 확인해 예상 총 step 수와 총 wallclock을 산정. 코드 변경 전 최신 전체 deck 동기화 필요.

---

## 2026-09-22 — 장시간 run 원인 확인: Transient MaxStep=1e-3

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** SDevice runtime / step-control diagnosis
- **상태:** CONFIRMED (현재 preprocessed deck 및 log 기준)
- **근거:** `pp6_des.cmd`의 Transient block에서 `InitialStep=1e-5`, `MinStep=1e-9`, `MaxStep=1e-3`, `Increment=1.2`, `Goal { Name="anode" Voltage=5.0 }` 확인.
- **교차확인:** 실행 로그의 pseudo-time 약 0.0766738에서 anode voltage가 약 0.3834 V이며, `5.0 × 0.0766738 ≈ 0.38337 V`로 일치. 따라서 현재 transient coordinate가 0→1 동안 anode 0→5 V ramp에 대응함을 강하게 확인.
- **의미:** `MaxStep=1e-3`이면 최대 전압 증가량은 약 5 mV/accepted step. 현재 약 0.077 지점에서 5 V 목표까지 최소 약 923~924 accepted steps가 더 필요함.
- **runtime 추정:** 최근 관찰된 약 3563.68 s/step을 단순 적용하면 남은 시간이 약 38일 규모. 실제 step cost는 bias에 따라 달라질 수 있으므로 이는 거친 추정이지만 현재 설정이 매우 장시간인 원인은 분명함.
- **다음:** `pp6_des.cmd`가 아닌 원본 SDevice deck에서 numerical step strategy를 검토. Common Baseline physics(Nt/Et/sigma/5 nm damage 등)는 변경하지 않으며, A/B 및 Nt 비교에 동일한 numerical protocol을 적용해야 함.

---
