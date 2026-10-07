## 2026-10-07 — Project A/B production pre-run GO/NO-GO audit

- 작업자: 주수빈
- 상태: REVIEWED / TEAM GATE
- FAST_C1/Common Baseline은 Project A/B의 parent로 사용 가능하며 physical baseline을 다시 만드는 것은 불필요.
- 하지만 multi-day A/B production sweep은 즉시 시작하지 않기로 함.
- 시작 전 필수: 실제 active preprocessed deck 확인, 모든 spatial output 및 region-integral extraction 선검증, 2D current-density normalization, A/B parameterized geometry+mesh+null controls, Save/Load smoke, 대표 pilot.
- A는 same-material GaN Cedge 내부 경계에 명시적 mesh refinement가 필요.
- B는 AlBarrier의 exact vertical span을 먼저 확정해야 하며, QW edge를 치환하는 경우 active QW volume 변화가 comparison metric에 반영되어야 함.
- 상세 기준: `CMP/PROJECT_AB_PRE_RUN_AUDIT.md`.

## 2026-10-06 — Claude high-bias runtime analysis reviewed; FAST_C2 proposed

- 작업자: 이택규
- 상태: REVIEWED / PROPOSED / NOT EXECUTED
- Claude package `FAST_C2_strategy_for_GPT.zip` reviewed by ChatGPT.
- central diagnosis accepted as a working numerical model:
  - high-bias runtime is dominated by a local convergent-timestep ceiling (`dt*`) plus `Increment=1.2` growth -> expensive rejection -> ~0.5 cutback cycling.
  - Node 6 representative failure: dt=1.1842e-5, RHS ~1.41e-3 stagnates through Iteration 15; retry dt=5.9211e-6 converges in 2 iterations.
  - idealized cycle model reproduces current Node 6 speed (~2.24 mV/h model vs ~2.2 mV/h observed).
  - under the same idealized assumptions, Increment=1.05 + Iterations=8 gives ~5.24 mV/h; this is a model prediction, not measured C2 performance.
- FAST_C2 remains numerical-only PROPOSED:
  - staged global-time Transient
  - 4 V+ Increment 1.05
  - candidate Iterations 8 subject to D2 accepted-iteration audit
  - checkpoints at 4.0/4.4/4.6/4.8 V
  - RHSMin/physics/mesh/5 V endpoint unchanged
- important ChatGPT caveat:
  - changing iteration cap/timestep growth changes the transient step sequence; identical convergence criteria do not by themselves guarantee identical trap/transient state.
  - NtSide=1e18 C2 validation must include trap charge/occupancy, SRH, radiative/Auger and carrier distributions, not I-V alone.
  - Claude trap-emission estimate uses generic GaN assumptions and is not a confirmed active-deck timescale.
- current Node 6/12 runs MUST continue as reference evidence.
- syntax/manual gates remain unresolved: segmented InitialTime/FinalTime+Goal semantics, Save/Load syntax, and whether existing Plot(-Loadable) TDR can be loaded.
- Decision 0 is separate and pending team approval: whether production analysis endpoint may be defined by a validated current-density window instead of always requiring 5 V. Baseline 5 V endpoint is not changed.
- `iv_window.py` J values are provisional until AreaFactor/2D current normalization is verified.
- public files added:
  - `CMP/FAST_BASELINE_C2.md`
  - `CMP/tcad/tools/make_restart_deck.py`
  - `CMP/tcad/tools/iv_window.py`
- proprietary full C2 deck was NOT uploaded; recorded production deck SHA-256 = `b876f614424202e6deaf0655411d7bc15733095da297c1df9ca5ebaacbb578d1`.
- helper scripts passed Python syntax and synthetic-only tests; no live Sentaurus test yet.
- next: D1–D6 in order, then C2 smoke gate before any production C2 run.

## 2026-10-04 — B0 cutback-rule validation CLOSED

- 작업자: 이택규
- 상태: OBSERVED / B0 COMPLETE
- regenerated x8 CSV with the updated audit tool using explicit `Stepsize`.
- all 285 rejection/retry pairs were checked.
- `retry_dt / rejected_dt`:
  - pairs = 285
  - min = 0.499975805
  - max = 0.500023337
  - mean = 0.499999621
- interpretation: the retry timestep is effectively exactly 0.5 of the rejected timestep; remaining spread is consistent with printed Stepsize precision.
- this closes the B0 assumption that the transient cutback factor is independent of whether the rejected Newton attempt ran to 50 or is capped at 15.
- therefore C1 should preserve the x8 rejection points/accepted-step trajectory over the observed overlap; only the rejected-attempt Newton count changes 50 -> 15.
- C1 source remains unchanged: SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`, `Iterations=15`.
- next: separate FAST C1 Workbench project/copy -> source hash -> preprocess gate.
- live x6/x7/x8 untouched.

## 2026-10-04 — FAST C1 B0 review strengthened acceptance criteria

- **작업자:** 이택규
- **구현/검토:** Claude B0 review + ChatGPT verification
- **상태:** PROPOSED / READY FOR SEPARATE PREPROCESS
- C1 source remains `Iterations=15`; no physics/source change beyond the already-reviewed numerical cap.
- ~4.33 V interpretation corrected: first rejected attempt with changed Newton count, not trajectory divergence.
- A1'/A1'' added: preserve accepted/rejection trajectory over overlap and require C1 rejection message to show 15-cap.
- full CSV cutback-ratio constancy remains pending; observed examples are ~0.5.
- live x6/x7/x8 remain untouched.

## 2026-10-04 — FAST_BASELINE C1 selected as first numerical candidate (PROPOSED)

- **작업자:** 이택규
- **구현:** Claude / **검토:** ChatGPT
- **상태:** PROPOSED / REVIEWED / NOT EXECUTED
- Copy x8 golden 대비 유일한 executable change는 forward Transient inner Coupled `Iterations=15`.
- Common Baseline physics/traps/geometry/step controls는 유지.
- Synopsys 2022 training의 15–20 iteration 권고와 방향은 일치하지만, 프로젝트의 ~50-iteration failure 기록과 documented default 20 사이 불일치가 있어 B0 raw-log audit이 선행되어야 함.
- 최종 FAST 채택 전에는 numerical/physical equivalence + runtime 모두 검증.
- live x6/x7/x8은 보존.

## 2026-09-28 — Final SDevice v1.2 source-sync gap 발견

- **작성자:** ChatGPT
- **참여자:** 이택규 / 주수빈
- **구분:** 공용 동기화 점검
- **상태:** OBSERVED + UNRESOLVED
- **내용:** JuSubin의 Issue #7 및 개인 타임라인에는 Final SDevice v1.2 수정 이력이 기록되어 있으나, 실제 `CMP/tcad/CURRENT/sdevice2_defect_on.cmd`는 오래된 버전으로 남아 있어 최신 실행 코드와 GitHub source-of-truth가 불일치함.
- **주의:** Gmail에 도착한 내용은 Issue #7 알림이므로 연구 진행 로그 반영 여부는 확인할 수 있지만 실제 코드 파일 업로드 여부를 대신하지 않음.
- **다음:** exact Final SDevice 전체 원문을 회수하여 CURRENT에 동기화하고 provenance를 재검증.

---

## 2026-09-22 — CES2027 선발 발표 구성 착수

- **작성자:** ChatGPT
- **참여자:** 주수빈
- **구분:** 팀 발표 준비
- **상태:** PROPOSED
- **내용:** 15분 발표를 Common Baseline의 문헌 근거, baseline 구조 검증, Project A/B의 TCAD 구현/공정 비교 전략 중심으로 구성하기로 함.
- **발표 원칙:** 지난 1주차의 일반 배경은 최소화하고, baseline provenance와 검증 가능성 및 fair comparison design을 핵심으로 제시.
- **계획 파일:** `CMP/CES2027_PRESENTATION_PLAN.md`

---

## 2026-09-21 — CMP 프로젝트 내 의미 있는 작업 자동 저장 범위 재확정

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영 결정
- **상태:** CONFIRMED
- **내용:** 사용자가 CMP 프로젝트 안에서 수행하는 연구 작업은 작업자가 이택규/주수빈 누구든 별도 "저장해" 요청 없이 의미 있는 변경이 생길 때 GitHub에 자동 기록하도록 재확정.
- **포함:** 코드 수정, 오류/해결, simulation 결과, baseline/설계 판단, blocker, 다음 작업, 인수인계.
- **제외:** 단순 잡담, 일반 개념 질문, 연구에 반영하지 않은 사소한 아이디어.
- **경계:** AI가 보지 못하는 다른 비공개 채팅을 실시간으로 직접 읽는다고 가정하지 않으며, 각 채팅의 AI가 GitHub에 기록해야 장기 동기화가 보장됨.

---

## 2026-09-21 — 주수빈 Common Baseline 코드 최종화 / pre-run 검토 진행

- **작성자:** ChatGPT
- **참여자:** 주수빈
- **구분:** 병렬 연구 진행
- **상태:** OBSERVED — 공유 프로젝트의 주수빈 채팅 사용자 보고 기준
- **내용:** 주수빈이 메인 SDevice 및 앞서 검토된 관련 코드를 최종 수정했다고 보고했으며, Project A/B 공통 baseline으로 장기간 사용할 수 있는지 simulation 전에 최종 논리 검토 중.
- **실행 계획:** 계산 비용을 고려해 우선 `NtSide=0`과 `NtSide=1e18` 두 조건만 먼저 실행해 baseline 동작을 확인할 계획.
- **제약:** 한 조건 run이 약 3일 걸릴 수 있다고 보고되어, 전체 sweep 전 정적 코드/논리 검증이 중요함.
- **검증 수준:** 최신 전체 코드와 실행 결과는 이 기록 시점에 GitHub에서 직접 검증되지 않았으므로 성공/정확성을 CONFIRMED로 간주하지 않음.
- **다음:** 수빈 최신 코드 동기화 → 최종 검토 → 두 조건 실행 → 결과 기록.

---

## 2026-09-21 — Sentaurus T-2022.03 공식 매뉴얼/예제 참고자료 색인

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 참고자료 / 연구 인프라
- **내용:** 사용자가 제공한 SDevice/SDE/SMesh/SVisual T-2022.03 User Guide와 Sentaurus example 자료를 검토해 GitHub reference index와 file manifest로 기록.
- **중요 확인:** textured solar-cell 공식 example의 SDevice File block에서 `plot=@tdrdat@`, `grid=@tdr@`, `current=@plot@`, `output=@log@`, `parameter=@parameter@` Workbench macro 패턴 확인.
- **현재 blocker 관련 의미:** SDevice2 command macro를 임의 변경하기보다 `pp9_des.cmd`의 실제 preprocessing 결과를 우선 확인해야 한다는 기존 진단을 강화함.
- **보안/저작권:** Synopsys 원본 User Guide에는 proprietary notice가 있어 public GGYU에는 원문 PDF/전체 예제 코드를 업로드하지 않고 색인·요약·hash만 저장.
- **상태:** CONFIRMED

---

## 2026-09-21 — Claude용 GitHub 연동 작업 프롬프트 추가

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영
- **내용:** Claude가 GitHub의 현재 연구 상태를 우선 읽고, 실제 코드/로그를 기준으로 이어서 코드를 작성·디버깅하며, 의미 있는 결과를 다시 GitHub에 기록하도록 전용 시작 프롬프트를 추가.
- **파일:** `CMP/prompts/CLAUDE_GITHUB_WORK_PROMPT.md`
- **상태:** CONFIRMED

---

## 2026-09-21 — AI Shared Memory Protocol v2 구축

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영 결정
- **내용:** 이택규 GPT / 주수빈 GPT / Claude가 작업 시작 시 서로의 최신 GitHub 기록을 읽고, 의미 있는 작업 결과를 자동으로 GitHub에 쓰도록 최상위 공용 프로토콜을 구축함.
- **핵심:** READ-first → 작업 → 의미 있는 결과 WRITE → Issue #7 append → 필요 시 RELAY 인수인계.
- **추가:** 동시 수정 충돌 방지, 기록 실패 시 성공 주장 금지, 상태 라벨 표준화, 응답 종료 시 실제 동기화 항목 표시.
- **상태:** CONFIRMED

---

## 2026-09-21 — 새 채팅 시작 브리핑에 마지막 작업 + 대시보드 링크 추가

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영 결정
- **내용:** 새 채팅에서 `이택규` 또는 `주수빈`으로 시작할 때, 첫 답변에 현재 진행 상황뿐 아니라 가장 마지막으로 한 작업과 CMP 대시보드 링크를 항상 포함하도록 규칙 추가.
- **대시보드:** https://taekgyu0801.github.io/GGYU/
- **상태:** CONFIRMED

---

## 2026-09-21 — CMP AI 공통 협업 규칙 확정

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영 결정
- **내용:** 이택규 GPT, 주수빈 GPT, Claude가 같은 CMP 프로젝트에서 따를 세션 시작/자동 기록/코드 수정/충돌 방지/AI 인수인계 규칙을 `AI_COLLAB_RULES.md`로 통합.
- **상태:** CONFIRMED
- **목적:** 서로 다른 노트북과 AI 계정에서 작업해도 GitHub를 기준으로 동일한 연구 상태를 유지.

---

## 2026-09-21 — 주수빈 collaborator 권한 확인 완료

- **작성자:** ChatGPT
- **계정:** `soybeanmilk0514-jpg`
- **저장소:** `TaekGyu0801/GGYU`
- **확인 결과:** `write` 권한
- **상태:** CONFIRMED
- **의미:** 주수빈 계정은 GGYU 저장소를 읽고 수정할 수 있음.
- **다음 작업:** 주수빈 ChatGPT/Claude 계정에서 GitHub를 연결하고 GGYU 읽기/쓰기 테스트 수행.

---

## 2026-09-21 — 주수빈 GitHub collaborator 초대 전송

- **작성자:** ChatGPT
- **사용자 보고:** 이택규가 주수빈 GitHub 계정을 `TaekGyu0801/GGYU` collaborator로 초대함.
- **상태:** OBSERVED (사용자 보고 기준, 수락 여부/최종 권한은 아직 미확인)
- **다음 확인:** 주수빈이 초대를 수락한 뒤 collaborator permission 확인.
- **후속 작업:** 주수빈 ChatGPT/Claude 계정에서 GitHub 연결 후 `GGYU` 읽기/쓰기 테스트.

---

## 2026-09-21 — 주수빈도 CMP 프로젝트 내 이름 확인 방식으로 작업

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용 운영 결정
- **내용:** 주수빈도 CMP 프로젝트 안에서 새 채팅 시작 시 `주수빈`이라고 입력해 작업자를 식별하고, GitHub 최신 상태 브리핑 및 자동 기록 흐름을 사용하기로 함.
- **효과:** 별도 긴 시작 프롬프트를 매번 붙일 필요 없이, 프로젝트 공통 규칙 + GitHub sync를 통해 동일한 연구 상태에서 이어서 작업 가능.
- **조건:** 주수빈 계정에서 GitHub 저장소 읽기/쓰기 권한이 있어야 자동 기록 가능.

---

# CMP 팀 타임라인

이 파일은 이택규 / 주수빈 / ChatGPT / Claude의 **공용 작업 이력 요약**이다.

개인 세부 기록은:
- `members/LeeTaekGyu/TIMELINE.md`
- `members/JuSubin/TIMELINE.md`

를 사용한다.

## 2026-09-21 — 공동 연구 GitHub/AI 협업 구조 구축

- **작성자:** ChatGPT
- **참여자:** 이택규
- **구분:** 공용
- **내용:** GitHub를 ChatGPT ↔ Claude ↔ 연구자 간 Single Source of Truth로 사용하도록 구조 정리.
- **추가된 핵심:** Common Baseline, Current Status, Error Log, Next Actions, AI Handoff, .ai-sync, 연구 대시보드, Phase Issues.
- **현재 연구 상태:** Common Baseline validation 진행 중.
- **현재 난관:** SDevice2 → SVisual2 TDR output/linkage 문제.
- **다음 작업:** pp9_des.cmd의 preprocessed File/Plot output filename 확인.

---

새로운 의미 있는 작업이 생기면 최신 기록을 위쪽에 추가한다.
