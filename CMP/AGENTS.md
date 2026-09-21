# AI Agent Entry Point

이 CMP 프로젝트에서 작업하는 AI는 **가장 먼저 `.ai-sync/LIVE_STATE.md`를 읽는다.**

그 다음:
1. `.ai-sync/LIVE_STATE.json`
2. `.ai-sync/RELAY.md`
3. `AI_PROJECT_GUIDE.md`
4. `COMMON_BASELINE.md`
5. `CURRENT_STATUS.md`
6. `ERROR_LOG.md`
7. `NEXT_ACTIONS.md`
8. 관련 Issue
9. 작업 대상 member의 `README.md`, `TIMELINE.md`
10. 관련 `tcad/CURRENT/*`

## AI relay rule

의미 있는 코드 디버깅/문헌 판단/연구 상태 변화가 있으면 같은 작업에서:

- `.ai-sync/LIVE_STATE.md`
- `.ai-sync/LIVE_STATE.json`
- `.ai-sync/RELAY.md`

를 최신화한다.

다른 AI가 즉시 이어서 작업할 수 있도록 **현재 blocker, 실제 관찰 로그, 현재 코드 경로, 다음 확인 항목, 바꾸면 안 되는 조건**을 남긴다.

## Member timeline rule

`CMP/members/<member>/` 아래 파일을 생성·수정·삭제·이동하면 **같은 작업에서 해당 member의 TIMELINE.md를 반드시 갱신한다.**


## 자동 기록 규칙

의미 있는 연구 작업이 발생하면 `AUTO_LOG_POLICY.md`를 따라 GitHub 상태를 함께 갱신한다.
개인 작업은 해당 연구원의 TIMELINE, 팀 공통 결정은 TEAM_TIMELINE에 기록한다.
새 blocker가 장기 작업/인수인계 대상이면 관련 GitHub Issue도 생성 또는 업데이트한다.


## 여러 계정/노트북 공동 기록

작업 시작 시 `CHAT_TO_GITHUB_PROTOCOL.md`를 읽고,
의미 있는 작업 후 LIVE LOG Issue #undefined에 comment를 남긴다.


## 세션 시작 자동 브리핑

새 채팅에서 사용자가 `이택규` 또는 `주수빈`이라고 작업자 이름을 입력하면,
`SESSION_START_PROTOCOL.md`를 실행한다.

즉, 현재 GitHub 상태를 먼저 읽고:
- 현재 팀 진행
- 현재 blocker
- 해당 작업자 개인 최신 기록
- 바로 이어서 할 다음 작업

을 첫 답변에서 요약한다.

의미 있는 작업이 발생하면 AUTO_LOG_POLICY와 CHAT_TO_GITHUB_PROTOCOL에 따라 즉시 저장한다.
