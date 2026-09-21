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
