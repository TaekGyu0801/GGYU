# 주수빈 GPT/Claude GitHub 자동 기록 설정

목표: 주수빈이 **자기 노트북 + 자기 ChatGPT/Claude 계정**으로 작업해도,
중요한 연구 진행이 자동으로 GitHub에 기록되고 이택규/ChatGPT/Claude가 같은 상태를 읽을 수 있게 한다.

## 1. 주수빈 GitHub 계정에 저장소 접근 권한 부여

저장소:
`TaekGyu0801/GGYU`

주수빈 GitHub 계정을 collaborator로 추가하고 최소 **Write** 권한을 준다.

## 2. 주수빈 ChatGPT/Claude 계정에서 GitHub 연결

각 AI 계정에서 GitHub 연결/connector를 켜고,
`TaekGyu0801/GGYU` 저장소에 **읽기 + 쓰기 권한**을 허용한다.

중요:
- 이 권한은 계정마다 따로 승인해야 한다.
- 이택규 계정의 GitHub 연결 권한이 주수빈 계정으로 자동 전달되지는 않는다.

## 3. 프로젝트 시작 지침 등록

주수빈이 쓰는 ChatGPT 프로젝트 또는 Claude 프로젝트의 시작 지침에 아래 내용을 넣는다.

```text
이 프로젝트의 작업자는 주수빈이다.

작업 시작 시 GitHub repository TaekGyu0801/GGYU의
CMP/AGENTS.md
CMP/SESSION_START_PROTOCOL.md
CMP/CHAT_TO_GITHUB_PROTOCOL.md
CMP/AUTO_LOG_POLICY.md
를 먼저 읽어라.

새 채팅에서 내가 "주수빈"이라고 입력하면,
GitHub 최신 상태를 읽고 다음을 먼저 알려줘:
1. 현재 팀 진행 상황
2. 현재 blocker
3. 주수빈 개인 최신 작업
4. 바로 이어서 할 다음 작업

작업 중 아래 사건이 생기면 내가 "저장해"라고 하지 않아도 GitHub에 즉시 기록해:
- 코드 수정
- 새 오류 발생
- 오류 원인 확인
- 시뮬레이션 결과 확인
- 중요한 설계/해석 결정
- blocker 변경
- 다음 작업 변경
- 다른 AI에게 넘길 내용 발생

기록 위치:
- CMP/members/JuSubin/TIMELINE.md
- CMP/TEAM_TIMELINE.md
- CMP/CURRENT_STATUS.md
- CMP/ERROR_LOG.md
- CMP/.ai-sync/*
- GitHub LIVE LOG Issue #7
- 필요 시 관련 Phase Issue

검증되지 않은 제안은 PROPOSED로 기록하고,
실제 로그/스크린샷/결과로 확인된 것만 OBSERVED/CONFIRMED로 기록해.
```

## 4. 첫 테스트

주수빈이 새 채팅에서:

```text
주수빈
```

이라고 입력한다.

정상이라면 AI는 추가 설명을 요구하기 전에 GitHub를 읽고:
- 팀 현재 Phase
- 현재 blocker
- 주수빈 개인 TIMELINE
- 다음 작업
을 브리핑해야 한다.

## 5. 자동 기록 테스트

그 다음 간단히 실제 연구 작업 하나를 수행한다.

예:
- 코드 한 줄 수정
- 오류 로그 확인
- Project B 아이디어 하나를 PROPOSED로 정리

그 뒤 GitHub에서 아래가 갱신됐는지 확인한다.

- `CMP/members/JuSubin/TIMELINE.md`
- Issue #7 comment
- 필요 시 `CMP/.ai-sync/LIVE_STATE.md`

## 6. 중요한 한계

"자동 기록"은 AI가 **현재 대화에서 실제 작업을 처리하는 동안** GitHub에 쓰는 방식이다.

AI가 채팅이 끝난 뒤 백그라운드에서 계속 감시하거나,
다른 계정의 비공개 대화를 몰래 읽는 방식은 아니다.

따라서 주수빈 계정의 AI가:
1. GitHub 저장소에 접근 가능하고
2. 이 프로젝트 규칙을 읽고
3. 의미 있는 작업마다 GitHub write를 실행
해야 한다.


## 같은 CMP 프로젝트 안에서 사용할 경우

주수빈이 이 ChatGPT CMP 프로젝트 안에서 새 채팅을 열어 작업한다면 설정은 더 단순하다.

새 채팅 첫 메시지로:

```text
주수빈
```

이라고 입력하면 된다.

프로젝트 공통 지침과 `SESSION_START_PROTOCOL.md`에 따라 AI는 주수빈을 현재 작업자로 유지하고,
GitHub 최신 상태를 읽은 뒤 팀 진행 상황 / 현재 blocker / 주수빈 개인 최신 기록 / 다음 작업을 브리핑한다.

이후 의미 있는 작업은 기존 자동 기록 규칙에 따라 GitHub에 반영한다.

단, 주수빈의 계정에서도 GitHub 저장소에 읽기/쓰기 접근이 가능해야 실제 자동 기록이 된다.
