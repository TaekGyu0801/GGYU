# CMP AI 공동작업 규칙

이 문서는 **이택규 GPT / 주수빈 GPT / Claude**가 같은 CMP 프로젝트에서 협업할 때 따르는 공통 규칙이다.

## 1. 작업자 확인

새 채팅의 첫 메시지가 아래 이름이면 해당 세션 작업자로 고정한다.

- `이택규`
- `주수빈`

사용자가 명시적으로 바꾸기 전까지 작업자를 변경하지 않는다.

## 2. 세션 시작 시 반드시 GitHub에서 읽기

작업자 확인 직후 다음 순서로 최신 상태를 읽는다.

1. `CMP/.ai-sync/LIVE_STATE.md`
2. `CMP/.ai-sync/RELAY.md`
3. `CMP/CURRENT_STATUS.md`
4. `CMP/ERROR_LOG.md`
5. `CMP/TEAM_TIMELINE.md`
6. 해당 작업자 `TIMELINE.md`
7. GitHub LIVE LOG Issue #7 최신 comments
8. 관련 `CMP/tcad/CURRENT/*` 코드

첫 답변에는:
- 현재 팀 진행
- 현재 blocker
- 해당 작업자 최신 작업
- 바로 이어서 할 다음 작업

을 요약한다.

## 3. 작업자별 기록 위치

### 이택규
`CMP/members/LeeTaekGyu/TIMELINE.md`

### 주수빈
`CMP/members/JuSubin/TIMELINE.md`

### 팀 공통
`CMP/TEAM_TIMELINE.md`

개인 작업을 팀 전체 확정사항처럼 기록하지 않는다.

## 4. 자동 기록 조건

다음이 발생하면 사용자가 따로 "저장해"라고 말하지 않아도 GitHub에 기록한다.

- 코드 수정
- 새 오류 발생
- 오류 원인 확인
- 시뮬레이션 성공/실패 확인
- 중요한 연구 판단
- baseline 관련 결정
- blocker 변경
- 다음 작업 변경
- 다른 AI/연구원에게 인수인계할 내용 발생

필요에 따라 함께 갱신:
- 개인 TIMELINE
- TEAM_TIMELINE
- CURRENT_STATUS
- ERROR_LOG
- NEXT_ACTIONS
- `.ai-sync/LIVE_STATE.md`
- `.ai-sync/RELAY.md`
- LIVE LOG Issue #7
- 관련 Phase Issue

## 5. 상태 표기

- `PROPOSED`: 실행 전 제안
- `OBSERVED`: 실제 화면/로그/파일에서 확인
- `CONFIRMED`: 충분히 검증됨
- `UNRESOLVED`: 미해결
- `REJECTED`: 시도했지만 폐기

AI의 아이디어를 실제 연구 결과처럼 기록하지 않는다.

## 6. 코드 수정 규칙

- 항상 현재 GitHub의 실제 코드를 먼저 읽는다.
- 최신 원본이 없는 파일은 추정으로 전체 재작성하지 않는다.
- 가능한 한 최소 수정한다.
- 사용자가 전체 코드를 요청하면 수정된 전체 블록을 제공한다.
- 코드 변경 후 변경 이유와 검증 상태를 기록한다.
- 실행하지 않은 코드는 `PROPOSED`로 남긴다.

## 7. Common Baseline 보호

사용자가 명시적으로 재설계를 승인하지 않는 한 아래 공통 기준을 임의 변경하지 않는다.

- Kou 기반 vertical epitaxy
- representative mesa 4 µm
- 5 nm sidewall damaged region
- nominal Nt / Et / sigma
- A/B 공통 contacts / physics / 비교 조건

Project A 또는 B 성능에 유리하도록 baseline을 바꾸지 않는다.

## 8. 동시 작업 / 충돌 방지

- 다른 연구원이 이미 수정한 파일을 덮어쓰기 전에 최신 GitHub 버전을 다시 읽는다.
- 서로 다른 연구원의 결과가 충돌하면 한쪽을 임의 선택하지 않는다.
- 각 결과와 근거를 따로 기록하고 `UNRESOLVED`로 남긴다.
- 같은 blocker를 두 AI가 다룰 경우 `.ai-sync/RELAY.md`에서 마지막 시도와 실패 원인을 먼저 확인한다.

## 9. AI 간 인수인계

작업이 막히거나 다른 AI로 넘길 때 `.ai-sync`에 반드시 남긴다.

최소 포함:
- 정확한 오류
- 실제 확인 근거
- 현재 코드 경로
- 이미 시도한 것
- 다음 확인 항목
- 건드리면 안 되는 조건

## 10. GitHub를 공용 기억으로 사용

GPT 계정끼리 비공개 채팅을 직접 읽는다고 가정하지 않는다.

장기 기억은 GitHub에 저장한다.

- 개인 진행 → 개인 TIMELINE
- 팀 진행 → TEAM_TIMELINE
- 현재 상태 → CURRENT_STATUS
- 오류/실패 → ERROR_LOG
- AI 인수인계 → .ai-sync
- 시간순 이벤트 → Issue #7
- 장기 task → Phase Issue

## 11. 사람 우선

AI는 최종 연구 판단을 임의로 확정하지 않는다.
baseline 변경, Project A/B 핵심 설계 변경, 논문/발표에 들어갈 최종 해석은 연구자 확인 후 확정한다.


## 12. 새 채팅 첫 답변 필수 항목

새 채팅에서 사용자가 `이택규` 또는 `주수빈`이라고 시작하면,
GitHub 최신 상태를 읽은 뒤 첫 답변에 반드시 다음을 포함한다.

- 현재까지 진행 상황
- 가장 마지막으로 한 작업
- 현재 blocker
- 다음 작업
- CMP 대시보드 링크: https://taekgyu0801.github.io/GGYU/

"가장 마지막으로 한 작업"은 TEAM_TIMELINE, 개인 TIMELINE, LIVE LOG의 최신 실제 기록을 기준으로 한다.
