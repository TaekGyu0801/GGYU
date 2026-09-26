# Next Actions

## Ju Subin — Node 12 SDevice exit(1) next step (2026-09-26)

Preprocessing succeeded and SDevice itself returned `exit(1)`.

Immediate diagnostic:
1. In Node 12 Job Log, click **Find Error**.
2. Capture the exact file/line/message Workbench jumps to.
3. If it does not jump to a useful line, search `n12_des.err` for: `Error:`, `Fatal`, `Unsupported`, `invalid`, `not found`, `cannot`.
4. Only after the first explicit error line is identified should code be changed.


## Ju Subin — Node 12 wrapper exit follow-up (2026-09-26)

`n12_local.err` only reports a generic child-process abnormal exit with status 1.

Next diagnostic order:
1. Node 12 **Job Log** tab → capture bottom ~30–50 lines including exit status/command.
2. If still generic, open `n12_des.job`.
3. Check `n12_des.sta` for last stage/status.
4. Search `n12_des.err` and `n12_des.out` for: `Fatal`, `Error`, `Segmentation`, `Killed`, `signal`, `memory`, `license`, `abort`.
5. Do not rerun or change baseline physics until the actual process-exit reason is found.


## Ju Subin — Node 12 immediate diagnostic refinement (2026-09-26)

The provided `n12_des.err` view contains warnings but no explicit fatal cause, while `n12_des.out` terminates before normal completion and no TDR/PLT is visible.

Immediate order:
1. Open `n12_local.err` and capture all contents.
2. If empty/non-diagnostic, open the Node 12 **Job Log** tab and capture the bottom section with exit status.
3. If still unclear, open `n12_des.job` and inspect wrapper/exit code.
4. Only after the exact exit reason is identified, modify the minimum necessary numerical/model setting.


## Priority 0 — Ju Subin NtSide=1e18 failure diagnosis (2026-09-26)

1. Workbench에서 `NtSide=1e18` failed scenario의 SDevice node를 선택.
2. 해당 node의 `*.err`를 열어 전체 또는 첫 error/fatal message를 확보.
3. `*.out` 맨 아래 50~100줄을 확보.
4. error가 convergence인지 syntax/parameter인지 resource/solver인지 분류.
5. 실제 원인에 맞는 최소 수정만 적용.
6. 수정 전 `NtSide=0` 성공 조건과 동일한 geometry/physics baseline은 유지.


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


## Ju Subin — identical-bias slowdown follow-up

1. old/current `.out` 시작부의 mesh/grid/unknown statistics를 비교.
2. old/current `pp*_des.cmd`에서 Physics/Traps와 Math/Solver block을 diff.
3. 동일 0.3834 V step의 Newton iteration 수 및 linear iterative count/time을 비교.
4. 차이가 확인되기 전 numerical step size를 먼저 변경하지 않음.


## Ju Subin — identify slow stage inside current run

1. `pp6_des.cmd` 하단 검색창에서 `Transient(`를 검색하고 Search Fwd를 반복해 등장 횟수를 센다.
2. `n6_des.out`에서 `3563.68`을 검색해 느린 step 위치로 이동한다.
3. 그 위치에서 위로 20~40줄 정도 올려 다음을 함께 확인한다:
   - `Computing BE-step from ... to ...`
   - 직전/다음 contact voltage
   - 해당 solve stage 시작을 알리는 문구
   - `NewCurrentPrefix`, `Set`, `Load`, 다른 ramp/Transient 전환 여부
4. `0.0766738`을 검색해 같은 숫자가 output에 여러 번 등장하는지도 확인한다.
5. 이 stage 식별 전에는 MaxStep, mesh, physics를 변경하지 않는다.


## Ju Subin — corrected next action after old/current confirmation

1. 과거 3일 완료 run과 현재 run의 `pp*_des.cmd`를 1:1 비교한다.
2. 우선순위:
   - Math / linear solver block
   - Physics / Traps 적용 범위
   - mesh/grid/unknown statistics
   - 동일 0.3834 V step의 Newton/linear iteration 세부 비용
3. step-control 자체는 두 run에서 동일한지 확인하되, 현재 20.1× 차이는 per-step 비용 차이로 먼저 설명해야 한다.
4. 기존 "same-run repeated Transient stage" 확인은 우선순위에서 제외.


## Ju Subin — immediate old/current deck comparison

1. 현재 slow Node 6의 `pp6_des.cmd`에서 `Conc =`를 검색해 실제 NtSide가 0인지 1e18인지 확인.
2. current도 Conc=0이면 old/current full `pp6_des.cmd`를 diff:
   - Math / ILS
   - Physics / Mobility / Recombination
   - trap region list 및 syntax
3. old/current `.out` 시작부의 grid/vertex/element/equation/unknown 통계를 비교해 mesh 변화 여부 확인.
4. current가 Conc=1e18이면 old fast deck과 직접 속도 비교를 중단하고, current NtSide=0 node와 old NtSide=0을 비교.
