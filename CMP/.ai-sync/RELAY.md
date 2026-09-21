# AI RELAY

## 2026-09-21 — ChatGPT → Claude

### Context
이택규와 Common Baseline Defect-ON flow를 디버깅 중.

### Exact blocker
Node 9 SDevice2의 solver output은 `Good Bye !`까지 정상 종료했지만, Node 10 SVisual2가 찾는 `n9_des.tdr`이 Node 9 Output Files screenshot에서 보이지 않았다.

### What has already been tried / learned
- SVisual2의 `create_plot -2d`는 T-2022.03에서 invalid.
- `@node|sdevice@` reference는 현재 Workbench flow에서 invalid.
- SDevice의 `Plot { ... }` block을 SVisual Tcl에 붙이면 `invalid command name "Plot"`가 난다.
- SVisual2 자체는 현재 최소한의 `@previous@` 기반 loader로 복구됨.
- Node 9 SDevice2 output에는 Plot variable list가 출력되고 solver는 종료됨.

### Please do next
코드를 바로 다시 쓰기 전에 `pp9_des.cmd`의 preprocessed `File { ... }`에서 실제 `Plot=` 경로를 확인하라.
그 파일명과 Node 9 Output Files를 비교한 뒤 원인을 분기하라.

### Do not do
- trap physics parameter 변경
- unverified Plot variable 대량 추가
- JBD 4 µm pitch를 exact mesa로 해석
- SDE/SDevice1 full source를 추정 생성

### Relevant files
- `CMP/.ai-sync/LIVE_STATE.md`
- `CMP/tcad/CURRENT/sdevice2_defect_on.cmd`
- `CMP/tcad/CURRENT/svisual2_maps.tcl`
- `CMP/ERROR_LOG.md`

---

새 AI 메시지는 이 문서의 맨 위에 추가한다.
