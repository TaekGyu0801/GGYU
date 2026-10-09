## 2026-10-08 — 주수빈 Half+coarse SDevice QS 가속 시험 후보

- 작업자: 주수빈; 상태: PROPOSED / CODE STATIC PASS; 런타임 미검증.
- Half+coarse mesh (138,194 elements) 생성/visual gate 통과 후, SDevice Transient 0→0.3V smoke 한 step 약 109.74s 중 solve 약 90.20s를 관찰.
- steady-state I-V/IQE 목적에 더 적합하고 adaptive step 수를 줄일 수 있는 Quasistationary 0→0.3V 별도 시험 deck 작성. 원래 Physics/Trap/Math/ILS 및 initial Poisson/Coupled 유지, QS ramp 설정만 신규.
- 원본 full FAST_C1/Project A/B 기준 모델은 변경하지 않음. 짧은 smoke와 full-reference 동등성 시험 전 production 채택 금지.

## 2026-10-08 — Fast pilot direction: half-domain + relaxed remote bulk mesh

- 작업자: 이택규; 상태: PROPOSED / NOT IMPLEMENTED.
- Time-constrained request: run a **separate experimental branch** applying both half-domain symmetry and modest remote bulk/numerical n-GaN coarsening to investigate runtime, without stopping existing FAST_C1 or changing frozen physical baseline parameters.
- Must verify exact active SDE contacts/doping/geometry symmetry and retained-side 5nm physical damage; preserve MQW, EBL, heterointerfaces and damage/edge refinement; avoid changing tolerance/traps/polarization simultaneously.
- One combined pilot provides feasibility data, not independent attribution of speedup. Requires SDE mesh review + actual preprocessed region/physics scope review + short solver smoke before longer run.
- Exact active SDE/SDevice code is not publicly synced, so implementation pending obtaining originals. No simulation result yet.

## 2026-10-08 — First Node 6 QW local Probe observations (not emission validation complete)

- 이택규 SVisual screenshots from `n6_inter_0004_des`: `Clean_QW1`–`Clean_QW4` are confirmed InGaN zones. Selected field is horizontally clipped (`...bination`); tentatively `RadiativeRecombination`, pending fully visible name confirmation.
- Local values [cm^-3 s^-1 if radiative]: QW1 5.531972320698e12, QW2 9.346620224854e14, QW3 4.188264170176e13, QW4 6.069760269935e14.
- Positive point values cannot prove total QW emission, normal LED operating current or IQE. Continue active-material radiative parameter + actual QW volume/area integration + e/h and terminal-current checks before accepting normal LED baseline.

## 2026-10-08 — Half-domain / injection sanity review (not an approved baseline change)

- 작업자: 이택규 / Claude proposal reviewed by ChatGPT; 상태: REVIEWED / PROPOSED.
- Baseline Node6 at 4.7128 V has I=2.8954e-12 A/um; under nominal 4 um lateral area, J≈7.24e-5 A/cm2. Arithmetic matches SDevice T-2022.03 2D-current convention, but low injection and high-bias IV require physical sanity check; no assertion of LED failure until terminal current composition, live input/contacts and existing TDR band/current/recombination are verified.
- Half-domain has conditional symmetry rationale and may reduce degrees of freedom, but is NOT yet implemented or validated; current full/fine FAST_C1 remains reference. Do not co-change mesh and domain without isolating effects.
- RhsMin L2 sqrt(2) argument is a model-dependent hypothesis; changing convergence threshold needs separate validation, not automatic adoption.
- Existing A/B GO/NO-GO gates remain. Reference: LIVE LOG Issue #7 review dated 2026-10-08.

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


## 2026-10-09 11:30 KST — JUSUBIN_FAST_HALF_SWB completion reported

- 작업자: 이택규
- 상태: OBSERVED (user report; terminal/log not yet re-verified in this session)
- 이택규가 주수빈이 전날 실행한 `JUSUBIN_FAST_HALF_SWB`가 모두 완료되었다고 보고함.
- 이 보고로 Half+coarse transient branch는 "running"에서 "completion reported" 상태로 이동.
- 단, 최종 bias 도달, fatal/error 부재, 산출물 존재, elapsed time, I-V/IQE 유효성은 아직 로그로 재확인하지 않았으므로 CONFIRMED로 승격하지 않음.
- 다음: project terminal에서 n2_des.log/out/err와 최종 .plt/.tdr 존재를 확인하고, final 0.3 V 도달/normal termination/accepted final step을 검증. 그 후 QS Copy 결과와 runtime·I-V를 비교하고 full FAST_C1 reference 대비 half+coarse validation을 진행.


## 2026-10-09 — Transient pass, QS Copy MinStep stop
- User-provided logs: JuSubin half+coarse original transient completed to anode 0.3V (25019.43 s), I-V file exists.
- Distinct QS Copy ended because `Step-size less than MinStep (8.3986e-07)` after 18417.09 s; result save/normal program exit does not prove sweep completion. Final accepted voltage and failure mechanism pending.
- Team action: diagnose QS plot/log before solver alterations; full/fine reference equivalence pending.


## 2026-10-09 — QS Copy last accepted bias determined
- 작업자: 이택규. OBSERVED from user-provided `JUSUBIN_FAST_HALF_SWB_Copy/n2_des.plt` tail and `n2_des.log` grep.
- Last recorded QS pseudo-time: 6.43487876313307E-02; last anode OuterVoltage: 1.93046362893992E-02 V (0.0193046363 V; 19.3 mV, only ~6.435% of requested 0.3 V).
- Last log attempts at t=0.0643488 to 0.0643505 then terminated `Step-size less than MinStep (step-size = 8.3986e-07)`.
- QS runtime 18417.09 s but did NOT reach goal. Cannot compare as speedup to original transient that reached 0.3 V in 25019.43 s.
- Root numerical/physics trigger not yet established. Next: inspect QS log around lines 6900-7000 and `n2_des.err`; no blind MinStep or baseline modification.


## 2026-10-09 — Original transient vs QS Copy settings compared
- 작업자: 이택규; 상태: OBSERVED from user-shared original `JUSUBIN_FAST_HALF_SWB/pp2_des.cmd` grep and previous QS Copy preprocessed deck.
- Both original transient and QS Copy: `ErrRef(electron/hole)=1e4`, `RHSMin=1e-3`, `CheckRhsAfterUpdate`, startup Poisson `Coupled(Iterations=500, LineSearchDamping=1e-2)`, startup carrier `Coupled(Iterations=100)`, sweep inner `Coupled(Iterations=15)` without explicit sweep-local damping.
- Original transient: `Transient` with InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2 (actual final 0.3V result was confirmed earlier). QS Copy: `Quasistationary` InitialStep=0.03, MinStep=1e-6, MaxStep=0.15, Increment=1.5, Decrement=2.0, Goal(anode)=0.3V. Time coordinates have different meanings and cannot be compared directly as numerical step sizes.
- Correction: lack of explicit sweep-local LineSearchDamping is NOT a unique QS setting and cannot by itself explain the divergent convergence. Underlying cause still UNRESOLVED. Other Physics settings and actual complete original Goal/Decrement block not yet side-by-side audited.
- The original source header comments say 0-4.0V/4.0-5.0V, whereas current observed result was a 0.3V smoke; must read executable original Goal in `pp2_des.cmd` to resolve the potentially stale header comment.
- Next: inspect original `pp2_des.cmd` lines 583–615 for actual executable voltage Goal and step-control; preserve both results and Common Baseline. No code changes.


## 2026-10-09 — Original transient executable Goal confirmed (smoke only)
- 작업자: 이택규. OBSERVED from user terminal `../JUSUBIN_FAST_HALF_SWB/pp2_des.cmd` lines 580–615 (actual executable block): `Transient(InitialTime=0.0, FinalTime=0.06, InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Goal{Name="anode", Voltage=0.3})` and inner `Coupled(Iterations=15){Poisson Electron Hole}`, followed by `Save(FilePrefix="n2_smoke_ckpt_0p3V")`.
- Therefore full 0.3 V endpoint was explicitly intended for this short syntax/mesh/physics smoke; earlier header comments describing 0–4.0 V/4.0–5.0 V are NOT the executable sweep configuration for Node 2. Previous comment/Goal discrepancy resolved.
- Original Transient smoke successfully finished 0.3 V; does not establish 3–5 V forward I–V, IQE or half+coarse equivalence to full/fine reference. QS Copy stalled at 0.019304636 V and remains an experimental numerical branch.
- Decision: preserve both existing projects and all outputs; prioritize preparing a separate, reviewed high-bias Transient branch for actual LED operation, only after source/provenance, bias plan, solver stability and half-vs-full validation gates. Do NOT modify original 0.3 V smoke or automatically launch 5 V.


## 2026-10-09 — Half 5V test SDevice edit performed in copied SWB project
- 작업자: 이택규. OBSERVED from terminal in `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST`: user ran `cp -p sdevice_des.cmd sdevice_des_0p3V_backup.cmd`, then `sed -i` replacing `FinalTime = 0.06` with `1.0`, `Goal Voltage = 0.3` with `5.0`, and `Save FilePrefix n@node@_smoke_ckpt_0p3V` with `n@node@_5V_ckpt`.
- Follow-up `grep -nE 'FinalTime|Voltage =|FilePrefix =' sdevice_des.cmd` confirmed line 587 FinalTime=1.0, line 597 Goal Voltage=5.0, line 608 new 5V Save prefix; initial electrode Voltage=0.0 appears at lines 38 and 43.
- Code modification is OBSERVED in the user's remote copied project, NOT yet synced as full source to GitHub. Backup command executed but exact backup-byte equality not independently checked. Original `JUSUBIN_FAST_HALF_SWB` and QS Copy were not targeted.
- Numerical intent: preserve the old 5 V per time-unit voltage ramp by adjusting 0.3/0.06 to 5/1; note `Transient` time is physical simulation time and this is not a steady-state QS. Not yet validated for high-bias convergence/current/IQE. The old 0.3V smoke comment in source may remain stale.
- NEXT: in the copied SWB project select SDevice Node 2 and run Ctrl+P preprocessing only; check generated `pp2_des.cmd` for actual FinalTime=1.0, anode Goal Voltage=5.0, Save prefix and expected mesh/physics/NtSide before F7. Do NOT run 5V yet; check that copied project prep is independent from original.


## 2026-10-09 — 5V copied Half/Coarse transient backup and Grid/Trap preflight observed
- 작업자: 이택규; 상태: OBSERVED from user's terminal (archive integrity check pending; 5V run NOT YET observed).
- At `/user/semi/semi437/tmp/myproject`, user executed `tar -czf JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz JUSUBIN_FAST_HALF_5V_TEST`; `ls -lh` confirms archive 12M, timestamp Oct 9 11:25. This is an existing compressed project snapshot made *after* 5V source edits, containing copied old 0.3V outputs; not a verified successful 5V result. Archive contents/integrity have not yet been independently checked with `tar -tzf`.
- In copied project `pp2_des.cmd` grep: Grid=`n1_msh.tdr` line20; 12 displayed region-level `Conc=0` lines145–365; RHSMin=1e-3 line510; startup Coupled Iterations=500 and 100; sweep `Coupled(Iterations=15)` line600. Earlier pp2 verification showed executable Transient, FinalTime=1.0, Goal anode=5.0, Save prefix `n2_5V_ckpt`.
- Original 0.3V smoke and separate QS Copy preserved. Current blocker: archive integrity check and launching SDevice Node2 only in copied SWB; don't launch SDE or modify original. 5V high-bias numerical/physical validity, IQE, I-V, mesh/symmetry equivalence are not established. Allow initial run only as exploratory independent branch, with output/log monitoring and no runtime/accuracy promise.
- NEXT: `tar -tzf ../JUSUBIN_FAST_HALF_5V_TEST_pre5V_20261009.tar.gz > /dev/null` and `echo $status` (C-shell-compatible; 0 expected); then copied SWB Node2 SDevice Run F7 only; inspect new n2_des.log/err after startup, verify no immediate failure and logs no longer Oct 9 01:39 copied outputs.


## 2026-10-09 — 5V copied project Node2 not running; old 0.3V log confirmed
- 작업자: 이택규; OBSERVED user terminal from `JUSUBIN_FAST_HALF_5V_TEST`.
- `ps -fu semi437 | grep '[s]device'` showed ONLY two old active sdevice processes: PID 69457 running `pp6_des.cmd` since Oct04, and PID 93915 running `pp12_des.cmd` since Oct06 (both 99% CPU). No `pp2_des.cmd` SDevice process present in this observed process list. A queued SWB job, if any, was not separately checked.
- `n2_des.log` mtime Oct 9 01:39:13 +0900; its tail says the *old original 0.3V smoke* completed with `Good Bye` Oct9 01:39:13, wallclock 25019.43 s and 2.61GB peak memory. This log was inherited by directory copy and is NOT a 5V result.
- Therefore no indication 5V SDevice Node2 has launched; do NOT Clean Up Node merely to start. Existing pre5V archive readable (tar listing status 0), pp2_des.cmd preprocessed 5V parameters confirmed earlier.
- NEXT: if concurrent machine/license resources are acceptable, select **only** SDevice Node2 in the SWB copied `JUSUBIN_FAST_HALF_5V_TEST` and run F7. Avoid SDE re-run. Monitor fresh `n2_des.log` timestamp and View Output; check convergence and actual attained anode voltage. CPU contention from pp6/pp12 may prolong 5V run. Do not mark 5V started/completed before evidence.

## 2026-10-09 — 이택규 Half+Coarse 5V_TEST 5V 달성 (OBSERVED)

- OBSERVED source: user-provided terminal in `/user/semi/semi437/tmp/myproject/JUSUBIN_FAST_HALF_5V_TEST`, `tail -n 40 n2_des.log` after run. Final anode voltage `5.000E+00 V`, anode electron `2.781E-13`, hole `1.420E-11`, total current `1.448E-11` (terminal output units require current-normalization audit). `Finished, because... Curve trace finished.`, `Sentaurus Device simulation finished`, `Good Bye !` at 2026-10-09 14:29:52 KST.
- OBSERVED files written per log: `n2_5V_ckpt_des.sav`, `n2_5V_ckpt_circuit_des.sav`, `n2_des.tdr`. `wallclock=10596.76 s` (2 h 56 m 36.76 s), total CPU 30641.23 s, peak memory 2.97 GB. `ps` showed only pp6 PID 69457 and pp12 PID 93915; no active pp2 at check.
- Proven: copied **Half+Coarse NtSide=0** Transient Node2 reached 5V and terminated normally. Not proven: publication-grade/common damaged NtSide=1e18 baseline, physical I-V/current-density validity, full-vs-half equivalence, IQE/optical emission, extracted current units, or A/B improvements. Do not treat save filename alone as 5V evidence; here independently supported by final 5V terminal row + normal curve trace.
- Previous 116h extrapolated runtime and 3–7+day planning range are superseded by the **measured 10596.76 s** for this run; reason for fast runtime relative to old 0.3V smoke remains unverified. Do not infer speedup or solver equivalence without source/deck/log comparison.
- NEXT: preserve 5V outputs/checkpoints and current reference pp6/pp12 jobs; inspect `n2_des.plt` for full I-V, ensure actual postprocess unit/AreaFactor/2D symmetry normalization, compare intermediate MQW Rrad/SRH/Auger and carrier/injection with full/fine at matched bias/current; then separate nominal `NtSide=1e18` damage case after controlled preprocess/short-run gate. Project A/B production remains NO-GO pending existing audit.

## 2026-10-09 — Half+Coarse 5V_TEST PLT 1023-point I–V readout and Parameters path confirmed (OBSERVED)

- 작업자: 이택규. User ran read-only awk across `n2_des.plt` DF-ISE Data with 17 fields per record: `ROWS=1023`, `REMAINDER=0`, first anode OuterVoltage 0 V, last exactly 5.00000000000000E+00 V; last anode TotalCurrent (raw printed) 1.44801646079583E-11. This confirms a fully parsed 17-column series from 0 to 5V but not yet its physical current units or validity.
- Sampled voltage/raw total current pairs: (0 V, -9.34556980161972E-27), (0.503368865 V, 5.81275673304787E-15), (1.003368865 V, 6.13100514338505E-15), (1.503368865 V, 7.84214693612489E-15), (2.003368865 V, 1.31567117783539E-14), (2.503368865 V, 2.84645414227297E-14), (3.003368865 V, 3.17582117791696E-14), (3.503368865 V, 3.28516927136479E-14), (4.003368865 V, 3.50552134304176E-14), (4.503368865 V, 3.69335070901735E-13), (5V, 1.44801646079583E-11). Sample points show pronounced rise above ~4V, not evidence of confirmed LED emission or normal operating current; full 1023-point monotonicity not checked.
- `pp2_des.cmd` File block points to `Grid="n1_msh.tdr"`, `Parameters="FASTC1_pp6_des.par"`, `Plot="n2_des.tdr"`, `Current="n2_des.plt"`, `Output="n2_des.log"`. User `find . -maxdepth 1 -type f -name '*.par'` returned `./FASTC1_pp6_des.par`. Therefore absent `pp2_des.par` is explained by correct alternate parameter filename. Parameter *contents*, AreaFactor absence across all active sources, radiative coefficient and steady-state-vs-transient interpretation not yet verified.
- Source header comments claim staged 0–4 / 4–5V with multiple checkpoint saves, but previous actual executable Solve was a single 0–5V transient and log showed end Save only; comments cannot substitute for active code. Do not assert multi-stage operation from comments.
- NEXT: read-only inspect `FASTC1_pp6_des.par`, actual `pp2_des.cmd` Physics/Plot and any AreaFactor; establish semiconductor radiative coefficient/output fields, 2D width and current scaling; then evaluate MQW Rrad/SRH/Auger and terminal carrier-current consistency using `n2_des.tdr`. Do not modify working code, clean up, or rerun as part of audit. NtSide=0 endpoint success does not validate damaged NtSide=1e18 or final common baseline.

## 2026-10-09 — Half+Coarse 5V endpoint contact-current components and recombination declarations (OBSERVED / emission UNRESOLVED)

- 작업자: 이택규. User provided direct terminal outputs from `JUSUBIN_FAST_HALF_5V_TEST`: last DF-ISE PLT record `time=1.00000000000000E+00, V=5.00000000000000E+00`. Anode raw `DisplacementCurrent=3.29132361382365E-18`, `eCurrent=2.78143237811134E-13`, `hCurrent=1.42020180788235E-11`, `TotalCurrent=1.44801646079583E-11`. At final step, terminal displacement contribution is negligible relative to total; anode hole current dominates. This does NOT establish MQW hole injection or steady-state across complete device.
- Actual parameter linkage confirmed: `pp2_des.cmd` uses `Parameters="FASTC1_pp6_des.par"` and `find` locates that exact file. User `cat FASTC1_pp6_des.par` shows only `LatticeParameters`, `Thermionic Formula=1`, and GaN Mg active-species `Ionization`; **no explicit Radiative coefficient in this parameter file**. Material database / other effective settings may still supply parameters: do not infer radiative coefficient=0 from this absence.
- User `grep -niE 'AreaFactor|Radiative|SRH|Auger|Recombination|CurrentPlot' pp2_des.cmd FASTC1_pp6_des.par` shows SDevice Physics `Recombination(SRH(), Auger(), Radiative)` at pp2 lines ~78–84, and Plot datasets `SRHRecombination`, `RadiativeRecombination`, `AugerRecombination` ~398–408. No AreaFactor match in these two files. These are code/model/output declarations, **not proof that any MQW Rrad is positive, integrated, or emitted light**.
- Prior Synopsys T-2022.03 UG audit recorded in `LeeTaekGyu/TIMELINE.md` (2026-10-08; Device UG §16 pp.488–489) cautions non-GaAs radiative-coefficient default may be zero without override; need verify effective GaN/InGaN material coefficients instead of claiming emission. Material database not reviewed in this turn.
- Next: read-only inspect `pp2_des.cmd` Physics/Plot context and `n2_des.log` radiative/material parameter clues, then open final `n2_des.tdr` in SVisual and confirm fully visible `RadiativeRecombination` values inside `Clean_QW1`–`Clean_QW4`; compare SRH/Auger and carrier maps and, when validated, perform spatial integration. Current-density normalization/AreaFactor still unresolved; no code modified, no rerun.

## 2026-10-09 — 5V Half+Coarse SVisual RadiativeRecombination field visible, QW attribution pending (OBSERVED)

- 작업자: 이택규. User shared Sentaurus Visual T-2022.03 screenshot, project title `JUSUBIN_FAST_HALF_5V_TEST`, data `n2_des`, selected scalar `RadiativeRecombination` (not only an output-deck declaration). Colorbar displays max `7.483e+19 cm^-3*s^-1` and minimum `-7.512e-34 cm^-3*s^-1` (numerically ~0). Therefore the **displayed spatial field includes nonzero positive radiative recombination** at the plotted state. Note values are 3D volume-rate density and do not imply integrated photon rate or EQE.
- Spatial map shows high rate in several thin **top** layers and near-zero deep bulk. Individual colored layers are not yet labelled as Clean_QW1–Clean_QW4. Screenshot top Data Selection was `Lines/Particles`, not a visible region-isolation of each InGaN QW. Hence precise QW rate, total QW-integrated radiative recombination, meaningful LED optical emission, efficiency/IQE, material coefficient C, and carrier balance are **not yet verified**.
- Bottom status: `Elements=138194`, `Points=65513`, consistent with accelerated Half+Coarse SDE mesh provenance. The screenshot is direct evidence for field visualization, not a quantitative integration of MQWs or a comparison against reference Full/fine.
- NEXT: in SVisual, open `Regions` tab and identify/visually isolate `Clean_QW1`–`Clean_QW4` while keeping RadiativeRecombination selected; zoom near top quantum-well stack, verify region names and use Probe to obtain numerical QW values. After check, inspect SRH/Auger spatial distributions and integrated rates. Preserve current saved data/other active jobs; do not launch new run. Material radiative coefficient and 2D current normalization remain unresolved.

## 2026-10-09 — 5V_TEST four InGaN Clean_QW local RadiativeRecombination Probe measurements (OBSERVED; IQE NOT YET)

- 작업자: 이택규. User supplied four direct Sentaurus Visual Probe screenshots in `JUSUBIN_FAST_HALF_5V_TEST` / `n2_des`, with scalar `RadiativeRecombination`, explicit zone label, x/y coordinates and Magnitude (cm^-3 s^-1, unit grounded in preceding SVisual legend).
- `Clean_QW1(InGaN)`: x=0.169818746552, y=0.560459877538, z=0, `Rrad=1.836010164996e+13`.
- `Clean_QW2(InGaN)`: x=0.194326754006, y=0.556958733616, z=0, `Rrad=3.558921779790e+12`.
- `Clean_QW3(InGaN)`: x=0.22058533342, y=0.56571159342, z=0, `Rrad=8.395713573050e+14`.
- `Clean_QW4(InGaN)`: x=0.245093340874, y=0.58321731303, z=0, `Rrad=7.094266327897e+18`.
- Result: **each of four named InGaN QWs contains a positive local Rrad point**, beyond mere output declaration or plot-wide maximum. The QW4 sampled point exceeds sampled other QW values by several orders of magnitude. HOWEVER: points differ in both vertical and lateral coordinates (x/y), so local values are **NOT** region-integrated emission, per-well averages or a verified QW4 total-emission dominance. Do not treat local peak, photon escape, IQE or material radiative coefficient as validated.
- Remaining: check SRH and Auger at the *same probe coordinates*, map Rrad spatially through each QW and perform mesh/region correct integrals, confirm 2D current normalization, injection/current plausibility and half-vs-full correspondence; NtSide=0 branch only. No new solver or source changes.

## 2026-10-09: 이택규 5V_TEST Clean_QW4 같은 좌표 Probe. x=0.244864017914, y=0.651958341615, z=0, InGaN. Radiative 7.103015017104e18, SRH 1.681575471039e22, Auger 1.238545872618e15, Total 1.682285896396e22 (cm^-3 s^-1). Local radiative fraction about 0.0422%; NOT integrated IQE. Verify physical rates and lifetimes before baseline freeze; no code change.

## 2026-10-09 — Project A fabrication-route feasibility brainstorm (PROPOSED / NOT APPROVED / NOT RUN)

- Worker: 이택규. Request: evaluate how the Stage1 Project A localized upper-nGaN-sidewall GaN:C Cedge could be fabricated. **No process route selected, no implantation/epitaxy performed, no TCAD/SProcess code modified.** Original frozen Common Baseline, Cedge conceptual position inside existing 5nm damaged-sidewall strip under MQW, and NtSide0/1e18 comparison remain unchanged.
- Candidate POST-MESA: completed LED epitaxy → ICP mesa etch exposes nGaN sidewall → protect pGaN/MQW and all non-target surfaces with *selective vertical-height mask/spacer* → angled/rotated C-ion implantation into exposed upper-nGaN sidewall → damage-recovery/thermal-budget gate → passivation and contacts. Critical unsolved gates: selectively exposing only target nGaN sidewall without irradiating QWs; finite ion straggle/depth/dose, angular shadowing; implanted C electrical activity vs implantation-induced isolation; post-MQW anneal thermal damage risk. Without selective mask this does **not** implement the current localized nGaN-only Cedge.
- Candidate PRE-MQW: grow nGaN up to intended upper region → lithographically mask future mesa-edge ring → implant C into exposed nGaN or grow selective GaN:C → validated recovery/cleaning and epitaxial regrowth → deposit MQW/EBL/pGaN → accurately align future mesa etch to buried annulus → passivation/contact. Protects already-formed MQW from carbon implantation anneal (since it is grown later) but has severe future-mesa overlay, high-quality epitaxial regrowth, and implant-damage recovery gates. Exact 5nm Dmg in TCAD is **not** a realizable lithographic alignment tolerance specification.
- Literature DOES demonstrate related *non-carbon* isolation concepts: As sidewall implantation in InGaN microLED (Next Nanotechnology 2025 DOI 10.1016/j.nxnano.2024.100101), F-implanted p-GaN current confinement ring in 6-10um microLED (ACS Photonics 2026 DOI 10.1021/acsphotonics.5c02363). Neither verifies a C-implanted upper-nGaN sidewall ring. Earlier `Characterization of Ca and C implanted GaN` (Materials Science and Engineering B 1997 DOI 10.1016/S0921-5107(97)00144-X) documents implantation damage/incomplete anneal with C+, and a Sandia 1995 report `Role of C, O and H in III-V nitrides` reports no measurable electrical activity for implanted C under its investigated conditions. Carbon-doped GaN growth literature supports C_N deep acceptor around Ev+0.9–1.1eV, but implanted-carbon activity cannot be assumed to match as-grown GaN:C.
- InGaN MQWs have temperature-dependent degradation/intermixing sensitivity; reports show significant degradation around 930–950 C for particular structures (J Alloys Compounds 2022, DOI 10.1016/j.jallcom.2021.163519; J Crystal Growth 2005 DOI 10.1016/j.jcrysgro.2005.04.002). Do not establish a universal safe/unsafe anneal temperature or prescribe unverified implantation energy/dose/angle/temperature.
- Next research gates: 1) team decides whether target is a chemically active C_N-compensated GaN:C edge vs damage-based implantation isolation (different device physics!); 2) compare POST vs PRE-MQW process feasibility, alignment and thermal budgets; 3) obtain measured/proven C depth and lateral profile/activation data, SRIM/SProcess process profile model before claiming fabrication realism; 4) ensure experimental masked/annealed control and inert-ion damage controls to separate C compensation vs irradiation damage; 5) keep current Baseline electrical/radiative validation priority unchanged.

## 2026-10-09 — 5V SVisual Clean_QW3 Rad field integral and '+' label correction (OBSERVED / UNRESOLVED)

- Worker 이택규 supplied `Field Integration` screenshot for `JUSUBIN_FAST_HALF_5V_TEST/n2_des`: field `RadiativeRecombination`, right pane `Regions of Dimension 2` shows ONLY `Clean_QW3 (InGaN)` with `Integral = 2.657110e+02 [s^-1*um^-1]`, `Domain=5.985012e-03 [um^2]`. This is **Clean_QW3-only 2D area integral**, not full QW3 or total photon output, and NOT IQE. Left list highlights both `Clean_QW3` and `Clean_QW3+DmgL_QW3` but only Clean_QW3 appears in right output, possibly stale result until Start Integration; do not interpret highlighted items as proven integrated.
- **Correction of previous GPT claim:** `Clean_QW3+DmgL_QW3` should NOT be assumed to denote union of bulk regions or selected as sole full-well ROI. Its structure and lack of inclusion in the dimension-2 output indicate it is likely a lower-dimensional boundary/interface label. Exact T-2022.03 metadata for '+' label has not been independently inspected, so interface interpretation remains PROVISIONAL. Safest method: select standalone region `DmgL_QW3` (not '+' named item), click `Start Integration`, verify `Regions of Dimension 2: DmgL_QW3`, record its Integral/Domain, then **sum independent Clean_QW3 and DmgL_QW3** integrals for whole QW3 (or choose both standalone 2D regions and verify both appear in output). Do not double-count interface or mix old results.
- The physical measured rate is 2D area-integrated per out-of-plane unit; raw SVisual [s^-1 um^-1] is NOT absolute 3D photon rate without explicit effective thickness. Same geometric normalization cancels for recombination fraction ratios when all wells are treated consistently; continue SRH/Auger over same 2D set and four QWs before IQE.
- Source: user screenshot Oct9 and earlier GitHub `PROJECT_AB_PRE_RUN_AUDIT.md`, SVisual manual Integration Tool general region-filter procedure. No code or TCAD source modified, no new run.

## 2026-10-09 — QW3 full 2D Radiative integration obtained from separate Clean/Dmg regions (OBSERVED)

- Worker 이택규; user SVisual Field Integration screenshot of completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des`, field `RadiativeRecombination`, `Regions of Dimension 2` explicitly lists **DmgL_QW3 (InGaN)**: `Integral=5.268180e-01 [s^-1*um^-1]`, `Domain=1.500002e-05 [um^2]`.
- Previously directly observed **Clean_QW3 (InGaN)**: `Integral=2.657110e+02 [s^-1*um^-1]`, `Domain=5.985012e-03 [um^2]`.
- These are separate disjoint **2D area region** integrals, so the full QW3 half-device measured raw regional sum = **266.237818 s^-1 um^-1**; total measured 2D domain area = **0.00600001202 um^2**. Arithmetic: 265.711 + 0.526818; 0.005985012 + 0.00001500002. **Derived**, not direct SVisual combined group output.
- This supersedes earlier incorrect idea that '+' item is a merged area. The `Clean_QW3+DmgL_QW3` entry should not be used as integrated 2D union without proof (likely lower-dimensional interface). Not full device IQE/absolute 3D photon rate. At NtSide=0, parametric damaged-edge traps are off, while DmgL_QW3 geometry exists.
- NEXT READ-ONLY: Integrate `srhRecombination` for standalone Clean_QW3 and DmgL_QW3 (or both as explicitly distinct 2D regions with actual Total Integral verification), then `AugerRecombination` same region scope. Keep units and voltage fixed; after all four QWs, compute recombination-based IQE from summed Rrad/SRH/Auger integrals; confirm normalization, full-vs-half equivalence and current physics before declaring baseline.
- No TCAD source edit, no new run; original files and checkpoints retained.

## 2026-10-09 — QW3 DmgL Auger spatial integral measured (OBSERVED)

- 이택규 supplied direct SVisual Field Integration screenshot for completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des`: `AugerRecombination` `Regions of Dimension 2: DmgL_QW3 (InGaN)`; `Integral=5.774334e-02 [s^-1*um^-1]`, `Domain=1.500002e-05 [um^2]`.
- Prior directly observed same-region 2D Radiative `0.526818`, SRH `1655.249` [s^-1 um^-1] and same Domain. Therefore DmgL_QW3 has all 3 regional integrals and SRH dominates *this segment*. At `NtSide=0`, generic SRH remains active; do NOT attribute to parameterized edge traps or infer full QW/device IQE.
- The earlier request was `Clean_QW3` SRH; user instead measured DmgL_QW3 Auger, which is useful and preserved. Still missing standalone `Clean_QW3` SRH and Auger for full QW3 radiative-vs-nonradiative integration. Clean_QW3 Radiative=265.711 [s^-1 um^-1]. NEXT: switch field `srhRecombination` + select only standalone `Clean_QW3` + Start Integration, screenshot. Then `AugerRecombination` + standalone `Clean_QW3`, repeat. No code edits or rerun.

## 2026-10-09 — QW3 whole-well 2D recombination integrals and derived recombination fraction (OBSERVED + DERIVED)

- Worker: 이택규. User screenshots of Sentaurus Visual Field Integration from successful 5V `JUSUBIN_FAST_HALF_5V_TEST/n2_des`. Newly OBSERVED `Clean_QW3(InGaN)`, Region of Dimension 2: `srhRecombination Integral=5.841611e+05 [s^-1 um^-1]` and `AugerRecombination Integral=1.265704e+01 [s^-1 um^-1]`; both Domain `5.985012e-03 um^2`. Earlier standalone Clean_QW3 Rrad=265.711; DmgL_QW3 Rrad=0.526818, SRH=1655.249, Auger=0.05774334 [s^-1 um^-1], Dmg Domain=1.500002e-05 um^2.
- Independent nonoverlapping **Half-domain QW3 Clean+DmgL** 2D area integral sums [s^-1 um^-1]: Rrad=**266.237818**; SRH=**585816.349**; Auger=**12.71478334**; sum all 3=**586095.30160134**. Derived recombination-based **QW3-only, 5V, NtSide=0 ratio** = 100*266.237818/586095.30160134 = **0.0454256871%**. SRH fraction ≈99.9524049%, Auger fraction≈0.0021694054%.
- Fraction of QW3 SRH integral from Clean region = 584161.1/585816.349 ≈99.71745%; DmgL contribution ~0.28255%. This matters for Project A sidewall-loss hypothesis: high QW3 SRH is not dominated by Dmg region under NtSide=0 in this output. It does NOT diagnose causes; Clean area is also ~99.75% of total QW3 physical cross-section. Generic SRH remains active even when NtSide=0. Need verify effective SRH lifetimes, material radiative coefficients, carrier density, local recombination maps and current normalization before claiming physical LED model is valid.
- **Strict scope**: QW3 recombination-ratio from spatial integrals, NOT whole-MQW/device IQE, EQE, measured experimental light, or proof that damaged NtSide=1e18 device behaves similarly. 2D integrals are per out-of-plane micrometer per SVisual display, common thickness factors cancel in within-device ratios. Full/fine vs Half/coarse and mesh convergence still unverified.
- NEXT: integrate Rrad/SRH/Auger in standalone Clean_QW1 + DmgL_QW1, QW2, QW4; record Region Dimension 2/Domain and compute 4-QW summed IQE. In parallel physical parameter and J-normalization audit; no modifications/re-run now.

## 2026-10-09 — 이택규 QW4 Clean+DmgL 2D integrals obtained (OBSERVED + DERIVED)

- 5V_TEST NtSide=0 Half. SVisual Clean_QW4 2D integrals [s^-1 um^-1]: Rad 38746.96, SRH 35617690, Auger 1327.983, Domain 0.005985012 um². DmgL_QW4: Rad 98.768, SRH 226496.2, Auger 2.414354, Domain 0.00001500002 um². Summed QW4 Rrad 38845.728, SRH 35844186.2, Auger 1330.397354, total 35884362.325354. QW4-only recombination radiative fraction 0.1082525242%; SRH 99.8880400%. Prior QW3-only radiative fraction 0.0454256871%.
- This is NOT device IQE/EQE, and strong SRH requires effective material physics and current/injection sanity checks. QW1 and QW2 integrations pending. No source/run modifications.

## 2026-10-09 — QW2 complete 2D Clean/DmgL radiative, SRH, Auger integrals + active physics grep (OBSERVED / DERIVED)

- Worker 이택규 shared six Sentaurus Visual T-2022.03 Field Integration screenshots from the completed `JUSUBIN_FAST_HALF_5V_TEST/n2_des` dataset at 5V, NtSide=0, Half+Coarse. Right pane confirms Regions of Dimension 2 for every selected independent region/field, and common per-region 2D Domains. Units for rate area-integrals [s^-1 um^-1].
- **Clean_QW2(InGaN)** (Domain=5.984982e-03 um²): Radiative=8.331490e+01 (=83.3149), srh=5.464576e+04 (=54645.76), Auger=1.736316e+00 (=1.736316).
- **DmgL_QW2(InGaN)** (Domain=1.499994e-05 um²): Radiative=1.672872e-01 (=0.1672872), srh=1.416049e+02 (=141.6049), Auger=3.800247e-03 (=0.003800247).
- Derived nonoverlapping **full QW2 Half-domain** sums: Rrad=**83.4821872**; SRH=**54787.3649**; Auger=**1.740116247**; All=**54872.587203447** [s^-1 um^-1], Total Area=0.00599998194 um². Derived `IQE_rec,QW2=100*Rrad/(Rrad+SRH+Auger)=0.1521382378%`; SRH share=99.8446906%, Auger share=0.00317119%. IMPORTANT: **QW2-only**, not device IQE/EQE; QW1 pending and physics unvalidated. Comparators QW3=0.0454256871%, QW4=0.1082525242%, all QW-only.
- Same user terminal ran read-only `grep -niE 'Lifetime|Tau|Radiative|SRH|Auger|DefaultParametersFromFile|AreaFactor' pp2_des.cmd FASTC1_pp6_des.par | head -n 90`: `pp2_des.cmd:68 DefaultParametersFromFile`, lines 80/82/84 `SRH()`, `Auger()`, `Radiative`; lines 398–406 desired output fields; NO explicit lifetime/Tau/Radiative coefficient/AreaFactor matched in these two files. This proves model declarations and default-parameter flag but **NOT** the numerical effective lifetime/radiative coefficients; material DB and log remain to be checked. No right to conclude unphysical defaults or that Radiative coefficient is zero without material model verification.
- Next: run QW1 six standalone 2D region integrations (Clean_QW1 and DmgL_QW1, each Radiative/srh/Auger); sum four QW integrals to compute recombination-based full MQW fraction. In parallel inspect actual effective SDevice material SRH/radiative coefficients and 2D terminal J/AreaFactor; do not modify source or rerun, Common Baseline still not frozen, A/B NO-GO.
