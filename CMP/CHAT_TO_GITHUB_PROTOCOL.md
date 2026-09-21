# Chat → GitHub 공동 기록 프로토콜

## 목적

이택규와 주수빈이 **각자 다른 노트북, 다른 ChatGPT 계정, Claude 계정**을 사용해도,
각 채팅에서 발생한 중요한 연구 진행을 GitHub에 남겨서 다른 사람/AI가 즉시 이어서 작업할 수 있게 한다.

## 핵심 원리

채팅 전체를 GitHub에 저장하지 않는다.

대신 의미 있는 사건만 구조화해서 저장한다.

```text
각자 GPT/Claude 채팅
       ↓
중요한 사건 감지
       ↓
GitHub LIVE LOG Issue comment
       ↓
필요 시:
CURRENT_STATUS
ERROR_LOG
개인 TIMELINE
.ai-sync
       ↓
다른 GPT/Claude가 읽고 이어서 작업
```

## 작업 시작 시

각 AI는 먼저 다음을 읽는다.

1. `CMP/.ai-sync/LIVE_STATE.md`
2. `CMP/CURRENT_STATUS.md`
3. `CMP/TEAM_TIMELINE.md`
4. GitHub Issue #undefined 최신 comments
5. 해당 연구원 `members/<name>/TIMELINE.md`
6. 관련 현재 코드

## 작업 종료 시 자동 기록

다음 중 하나라도 발생하면 LIVE LOG에 comment를 추가한다.

- 코드가 바뀜
- 오류가 새로 생김
- 오류 원인을 찾음
- 시뮬레이션 결과를 확인함
- 중요한 설계/해석 결정을 함
- 현재 blocker가 바뀜
- 다음 액션이 바뀜
- 다른 AI에게 넘길 필요가 있음

## 분류

- PROGRESS: 진행
- BLOCKER: 막힘
- FIX: 수정
- RESULT: 결과
- DECISION: 결정
- HANDOFF: AI/연구원 간 인수인계

## 상태

- OBSERVED: 실제 화면/로그/파일에서 봄
- CONFIRMED: 충분히 확인됨
- PROPOSED: 아직 실행 전 제안
- UNRESOLVED: 미해결
- REJECTED: 시도했지만 폐기

## 역할별 기록

- 이택규 작업 → `members/LeeTaekGyu/TIMELINE.md`
- 주수빈 작업 → `members/JuSubin/TIMELINE.md`
- 팀 공통 → `TEAM_TIMELINE.md`
- 최신 한 줄 상태 → `.ai-sync/LIVE_STATE.md`
- 오류 이력 → `ERROR_LOG.md`
- 장기 blocker/task → 별도 GitHub Issue
- 시간순 공용 이벤트 → LIVE LOG Issue #undefined

## 중요한 제한

ChatGPT나 Claude가 다른 계정의 채팅 내용을 직접 읽는 것은 아니다.
공유는 GitHub에 기록된 내용을 통해 이루어진다.

따라서 각 계정의 AI가 이 프로토콜을 따르고 GitHub 접근 권한을 가지고 있어야 한다.


## 새 채팅 시작 규칙

첫 메시지가 `이택규` 또는 `주수빈`이면 `SESSION_START_PROTOCOL.md`를 따른다.

이름 확인 후 바로 GitHub 최신 상태를 읽고 브리핑한다.
작업 중 의미 있는 사건은 사용자가 따로 저장 요청을 하지 않아도 즉시 GitHub에 반영한다.
