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
