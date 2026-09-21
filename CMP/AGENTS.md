# AI Agent Entry Point

이 CMP 프로젝트에서 작업하는 모든 AI(ChatGPT / Claude)는 **가장 먼저 `AI_SHARED_MEMORY_PROTOCOL.md`를 읽고 따른다.**

그 다음 현재 상태를 아래 순서로 읽는다.

1. `.ai-sync/LIVE_STATE.md`
2. `.ai-sync/LIVE_STATE.json`
3. `.ai-sync/RELAY.md`
4. `CURRENT_STATUS.md`
5. `ERROR_LOG.md`
6. `NEXT_ACTIONS.md`
7. `TEAM_TIMELINE.md`
8. 현재 작업자 개인 `TIMELINE.md`
9. LIVE LOG Issue #7 최신 comments
10. 관련 Issue 및 `tcad/CURRENT/*`

## 작업자

새 채팅에서 `이택규` 또는 `주수빈`이라고 입력하면 그 세션의 작업자로 고정한다.

## 필수 동작

- 세션 시작: GitHub 최신 상태 READ → 현재 진행/마지막 작업/blocker/다음 작업/대시보드 브리핑
- 의미 있는 작업: GitHub에 즉시 WRITE
- 코드 수정 전: 해당 파일 최신 버전 재확인
- 작업 막힘/AI 변경: `.ai-sync/RELAY.md`에 인수인계
- 기록 실패: 성공했다고 말하지 않음

세부 규칙과 기록 형식은 `AI_SHARED_MEMORY_PROTOCOL.md`를 최우선으로 따른다.
