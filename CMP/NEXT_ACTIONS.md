# Next Actions

## Priority 0 — 현재 blocker 해결

### Goal
SDevice2(Node 9)의 실제 TDR output을 확인하고 SVisual2(Node 10)가 정확히 그 파일을 읽도록 연결한다.

### Steps
1. Node 9 Explorer에서 `pp9_des.cmd` 열기
2. 맨 위 `File { ... }` 블록 확인
3. 특히 preprocessed:
   - `Grid =`
   - `Plot =`
   - `Current =`
   - `Output =`
   값 기록
4. Node 9 Output Files 전체 목록에서 `.tdr` 파일명 확인
5. 실제 TDR이 존재하면 `svisual2_maps.tcl`의 `tdrfile`을 그 이름에 맞춤
6. 실제 TDR이 없다면 SDevice2의 output 생성 조건을 별도로 진단

## Parallel track — Ju Subin Common Baseline pre-run validation

### Current state
공유 프로젝트의 주수빈 채팅에서, 메인 SDevice와 관련 코드를 최종 수정했다고 사용자 보고가 있었음. 아직 최신 전체 코드 및 실행 결과는 GitHub에서 직접 검증되지 않음.

### Next steps
1. 주수빈 측 최신 전체 코드 원문을 CMP에 동기화
2. Project A/B 공통 baseline 조건에 맞는지 정적/논리 검토
3. 계산 비용을 고려해 우선 `NtSide=0` 실행
4. 우선 `NtSide=1e18` 실행
5. 두 run의 로그/결과를 비교하고 GitHub에 기록
6. 이후에만 더 넓은 Nt sweep 여부 결정

## Priority 1 — mechanism validation

TDR linkage 해결 후 SVisual2에서:
- SRH / trap-assisted recombination 관련 실제 available scalar 확인
- RadiativeRecombination
- AugerRecombination
- eDensity
- hDensity
- Current / TotalCurrentDensity
- ConductionBandEnergy
- ValenceBandEnergy
- trap occupation / concentration 관련 실제 available field 확인

**필드 이름은 SVisual 실제 목록을 기준으로 사용. 추측 금지.**

## Priority 2 — Defect OFF vs ON

동일 bias에서:
- edge recombination OFF vs ON
- radiative recombination OFF vs ON
- carrier distribution OFF vs ON
비교.

## Priority 3 — Baseline validation completion

- Nt sweep: 0 / 1e17 / 1e18 / 1e19
- mesa sweep: 4 / 10 / 20 µm
- mesh convergence
- IQE definition/volume integration 검증
- 2D Cartesian current-density normalization 확인

## Priority 4 — Freeze then branch

Common Baseline Final 통과 후에만:
- Project A Carbon High-R Edge
- Project B Localized AlGaN Lateral Heterobarrier
로 분기.


## Ju Subin immediate runtime diagnostic

1. 현재 Node 6은 화면상 진행 중이므로 18시간 경과만으로 hang으로 판정하지 않음.
2. `pp6_des.cmd`의 `Solve { ... }`에서 현재 BE/transient 구간의:
   - 최종 목표 시간 또는 ramp goal
   - `InitialStep`
   - `MinStep`
   - `MaxStep`
   - `Increment`
   - 해당 구간의 bias/ramp 설정
   을 확인.
3. 현재 관찰된 약 3564 s/step과 실제 남은 step 수로 예상 총 runtime 계산.
4. 코드 최적화/step 조정은 전체 최신 deck 확인 뒤에만 제안. Nt/Et/sigma/5 nm damage width 등 Common Baseline physics는 runtime 문제 때문에 임의 변경하지 않음.


## Ju Subin — next numerical action after runtime diagnosis

1. 현재 `pp6_des.cmd` 자체를 수정하지 말고 원본 SDevice deck의 `Transient` block을 확인한다.
2. DC baseline I–V가 목적이라면, 5 mV 고정 수준의 최대 bias increment가 실제로 필요한지 검토한다.
3. `MaxStep` 확대 또는 DC용 `Quasistationary` 전환 여부는 최신 전체 deck과 원하는 I–V 해상도/수렴 안정성을 함께 검토한 뒤 결정한다.
4. numerical stepping을 바꾸면 NtSide=0/1e18 및 이후 Project A/B 모두에 동일하게 적용하고, coarse/fine step 비교로 결과 민감도를 검증한다.
5. Nt/Et/sigma/damage width/epitaxy/doping 등 Common Baseline physics는 runtime 때문에 변경하지 않는다.


## Ju Subin — compare against prior 3-day run

현재 코드를 바로 바꾸기 전에 과거 3일 run과 아래를 1:1 비교한다.
1. old/new `Transient`: InitialStep / MinStep / MaxStep / Increment / Goal
2. old/new mesh statistics: vertices/elements 또는 total grid points/unknowns
3. old/new Physics 및 Traps: 추가 모델, 적용 region, trap density/cross section 자체가 아니라 **적용 범위와 coupling 변화**
4. old/new Math: linear solver, Iterations, Method, damping/derivative 관련 옵션
5. old/new `.out`: accepted step 당 Newton iteration 수와 failed/retry/cutback 횟수

이 비교 전에는 MaxStep 확대를 확정 조치로 적용하지 않는다.
