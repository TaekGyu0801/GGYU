# 세션 시작 자동 인수인계 규칙

이 파일은 이택규 / 주수빈이 **각자 다른 노트북·다른 ChatGPT 계정·Claude 계정**으로 작업할 때,
새 채팅 시작 즉시 현재 연구 상태를 복원하기 위한 규칙이다.

## 1. 작업자 이름으로 시작하는 경우

새 채팅의 첫 사용자 메시지가 아래 이름 중 하나면 해당 세션의 작업자로 고정한다.

- `이택규`
- `주수빈`

사용자가 명시적으로 바꾸기 전까지 작업자를 변경하지 않는다.

## 2. 이름을 받으면 바로 해야 할 일

작업자 이름을 확인한 직후, 추가 설명을 요구하기 전에 GitHub 최신 상태를 읽는다.

읽기 순서:

1. `CMP/.ai-sync/LIVE_STATE.md`
2. `CMP/.ai-sync/LIVE_STATE.json`
3. `CMP/.ai-sync/RELAY.md`
4. `CMP/CURRENT_STATUS.md`
5. `CMP/ERROR_LOG.md`
6. `CMP/TEAM_TIMELINE.md`
7. 해당 작업자의 `CMP/members/<name>/TIMELINE.md`
8. GitHub LIVE LOG Issue #7의 최신 comments
9. 필요 시 관련 `CMP/tcad/CURRENT/*` 코드

## 3. 시작 브리핑 형식

작업자 이름을 받은 뒤 첫 답변에는 최소 다음을 포함한다.

### 현재 팀 진행
현재 Phase와 전체 진행 상황.

### 현재 blocker
지금 해결되지 않은 문제.

### 작업자 개인 최신 기록
해당 연구원이 직전에 무엇을 했는지.

### 바로 이어서 할 수 있는 다음 작업
GitHub 기록 기준으로 가장 가까운 다음 액션.

확인되지 않은 내용을 추측하지 않는다.

## 4. 작업 중 자동 기록

채팅 도중 아래 사건이 발생하면 사용자가 따로 "저장해"라고 하지 않아도 GitHub에 기록한다.

- 코드 수정
- 새 오류 발생
- 오류 원인 확인
- 시뮬레이션 결과 확인
- 중요한 연구 판단
- blocker 변경
- 다음 작업 확정
- 다른 AI에게 넘길 내용 발생

갱신 대상:

- 작업자 개인 `TIMELINE.md`
- 필요 시 `TEAM_TIMELINE.md`
- 필요 시 `CURRENT_STATUS.md`
- 필요 시 `ERROR_LOG.md`
- `CMP/.ai-sync/LIVE_STATE.md`
- `CMP/.ai-sync/LIVE_STATE.json`
- `CMP/.ai-sync/RELAY.md`
- LIVE LOG Issue #7 comment
- 장기 task면 관련 GitHub Issue

## 5. 저장 타이밍

"채팅 종료"를 감지하려고 기다리지 않는다.
의미 있는 사건이 발생한 직후 기록한다.

이렇게 해야 다른 GPT/Claude가 같은 날 바로 이어서 작업할 수 있다.

## 6. 중요한 제한

AI는 다른 GPT 계정의 비공개 채팅을 직접 읽을 수 없다.
공유되는 기억은 **GitHub에 기록된 내용**이다.

따라서 모든 참여 AI는 이 저장소를 읽고 쓸 수 있어야 한다.

## 7. 예시

사용자:
`주수빈`

AI 시작 응답 예시:

> 주수빈 작업으로 시작할게.
> 현재 팀은 Common Baseline validation 단계이고, 현재 blocker는 SDevice2→SVisual2 TDR linkage 문제야.
> 이택규 쪽에서는 Node 9 SDevice2가 solver 종료까지 갔지만 n9_des.tdr이 보이지 않는 상태까지 확인했어.
> 주수빈 개인 TIMELINE의 최신 기록도 확인해서 이어서 정리할게.
> 지금 바로 이어서 할 수 있는 작업은 ...

그 뒤 주수빈이 Project B 코드를 수정하면 그 결과를 주수빈 TIMELINE과 AI sync에 자동 기록한다.
