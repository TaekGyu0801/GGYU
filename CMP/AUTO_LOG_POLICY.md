# AI 자동 기록 규칙

이 프로젝트에서 ChatGPT / Claude는 단순 답변만 하는 것이 아니라, **의미 있는 연구 작업이 발생하면 GitHub 상태도 함께 갱신**한다.

## 언제 자동 기록하는가

다음 중 하나가 발생하면 기록한다.

- 새 코드 작성 또는 기존 코드 수정
- Sentaurus 오류 발생
- 오류 원인 확인
- 시뮬레이션 결과 확인
- 새로운 연구 아이디어 채택/폐기
- Common Baseline 관련 결정
- Project A/B 설계 변경
- 새로운 blocker 발생
- blocker 해결
- 다음 작업이 명확해짐
- 다른 AI에게 넘겨야 할 상황

## 누구의 기록으로 남기는가

현재 채팅 작업자 기준:

- 이택규 → `members/LeeTaekGyu/TIMELINE.md`
- 주수빈 → `members/JuSubin/TIMELINE.md`
- 팀 공통 결정 → `TEAM_TIMELINE.md`

현재 작업자가 명확하지 않으면 먼저 작업자를 확인한다.

## 함께 갱신할 파일

의미 있는 작업 후 필요에 따라:

1. 개인 `TIMELINE.md`
2. `TEAM_TIMELINE.md`
3. `CURRENT_STATUS.md`
4. `ERROR_LOG.md`
5. `NEXT_ACTIONS.md`
6. `.ai-sync/LIVE_STATE.md`
7. `.ai-sync/LIVE_STATE.json`
8. `.ai-sync/RELAY.md`
9. 관련 GitHub Issue

## GitHub Issue 생성 기준

모든 사소한 대화를 Issue로 만들지 않는다.

Issue를 만들거나 업데이트하는 경우:
- 하루 이상 이어질 수 있는 blocker
- 다른 연구원이 이어받아야 하는 문제
- 독립적인 검증 task
- Phase 완료 조건과 직접 연결된 작업
- 코드/결과 검토가 필요한 연구 항목

짧은 디버깅 시도는 ERROR_LOG와 TIMELINE에 기록하고, 필요하면 기존 Phase Issue에 반영한다.

## 사실성 규칙

- 사용자가 실제 실행하지 않은 코드는 "PROPOSED"
- 스크린샷/로그에서 확인된 내용은 "OBSERVED"
- 반복 검증된 내용은 "CONFIRMED"
- 실패한 접근은 "REJECTED"
- 해결되지 않은 문제는 "UNRESOLVED"

AI가 제안한 내용을 실제 연구 결과처럼 기록하지 않는다.

## AI 간 인수인계

ChatGPT/Claude가 작업을 끝내거나 막히면 반드시 `.ai-sync`를 최신화한다.

다음 AI는 대화 기록보다 GitHub의 최신 상태를 우선한다.
