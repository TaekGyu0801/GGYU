## 2026-10-04 — sequence correction: FAST coding precedes final clean-account freeze gate

- 작업자: 이택규
- Copy x8 golden reference freeze는 완료.
- 지금부터 separate numerical-only FAST_BASELINE 코드를 작성하고 short benchmark한다.
- clean-account reproduction은 최종 FAST deck freeze 및 Project A/B production 전에 반드시 수행하되, FAST 코드 작성 자체의 선행 blocker로 두지 않는다.
- 첫 benchmark 변수는 Newton iteration/cutback policy.
- x8 live directory는 수정 금지.

---

## 2026-10-04 — clean-account reproducibility requirement before FAST baseline freeze

- 작업자: 이택규
- 사용자 목표: 최종 baseline은 주수빈 계정과 이택규 계정에서 동일 source로 독립 재현되어야 함.
- 과거 경험: 동일 코드/파라미터를 다른 계정에 복사했을 때 실행되지 않은 사례가 있었음. 원인을 단순한 "계정에 축적된 상태"로 확정하지 않음.
- Claude/ChatGPT는 working account의 exact source뿐 아니라 preprocessed outputs와 project/runtime context를 함께 비교해야 함.
- 필수 비교 대상:
  - original SDE/SDevice source
  - pp1_dvs.cmd
  - pp6_des.cmd / pp6_des.par
  - mesh statistics and reference n1_msh.tdr hash
  - Workbench variables/tree/scenario files where relevant
  - n6_des.job/sta/err/out/log
  - Sentaurus version/path and thread settings
- 재현 절차:
  1. working semi437 Copy x8를 immutable reference로 보존.
  2. new account에서 source를 새 project로 import.
  3. full solve 전에 preprocess only / early initialization 단계까지 실행.
  4. pp1_dvs.cmd, pp6_des.cmd, pp6_des.par를 working account와 exact diff.
  5. mesh vertex/element statistics 비교.
  6. 차이가 있으면 full multi-day solve를 시작하지 않고 먼저 원인을 해결.
- FAST_BASELINE은 이 clean-account reproducibility gate를 통과할 수 있게 설계한다.

---

## 2026-10-03 — baseline execution split plan

- 최종 baseline 구현 단계에서는 동일한 검증 baseline을 주수빈 계정 1개, 이택규 계정 1개에 각각 실행할 계획.
- 두 계정에서 동일 조건을 재현한 뒤, 각자 맡은 후속 작업을 병렬로 진행.
- 향후 실행/코드 인수인계 시 이 병렬 운용 계획을 전제로 한다.

---

## 2026-10-03 — Claude handoff: active baseline runtime source needed

작업자: 이택규
상태: PROPOSED

현재 약 7일간 실행 중인 baseline run의 runtime 최적화 전에 주수빈 측에서 실제 실행 자료를 GitHub에 동기화해야 한다.

필요 자료:
- 실제 실행에 사용한 원본 SDevice 전체
- active node의 pp*_des.cmd
- active node의 pp*_des.par
- 최신 *_des.out 마지막 구간
- 가능하면 node 번호, NtSide 조건, pseudo-time, timestep, elapsed time, log/sta

Claude 작업 원칙:
- GitHub CURRENT의 기존 sdevice2_defect_on.cmd를 현재 active run과 동일하다고 가정하지 않는다.
- 실제 실행 원문을 기준으로 lineage를 확인한다.
- Common Baseline geometry/physics/Nt/Et/sigma는 유지한다.
- runtime 최적화는 numerical-only branch에서 수행한다.
- MaxStep/staged bias, Newton iteration, ErrRef, high-bias cutback, far-field mesh를 우선 검토한다.
- full multi-day run 전에 short benchmark로 기존 설정과 비교한다.

---

# AI RELAY

## 2026-09-28 — Lee Taek Gyu session: Final SDevice source-sync blocker

### Exact problem
JuSubin's Issue #7 / timeline say Final SDevice v1.2 was prepared, but `CMP/tcad/CURRENT/sdevice2_defect_on.cmd` is still an older deck and lacks the v1.2 intermediate TDR saves.

### Confirmed evidence
The current GitHub file still has hard-coded `Conc=1e18`, global `IncompleteIonization`, and no intermediate transient Plot/Time saves.

### Do next
Recover the exact full user-provided Final SDevice v1.1/v1.2 source from the JuSubin chat/file and sync that exact source to CURRENT.

### Do not do
Do not reconstruct v1.2 from Issue #7 snippets or from memory. The stale CURRENT deck is not a safe base for a final-code overwrite.

---



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
