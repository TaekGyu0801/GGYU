# AI Sync — ChatGPT ↔ Claude 전용 인수인계 공간

이 폴더는 **사람용 대시보드가 아니라 AI 간 작업 인수인계용**이다.

> 주의: 현재 GGYU 저장소가 public이므로 이 폴더는 인터넷에서 비밀인 공간은 아니다.
> 다만 대시보드에는 노출하지 않고, ChatGPT/Claude가 작업 시작 시 우선 읽는 전용 채널로 사용한다.

## AI가 작업 시작할 때

반드시 다음 순서로 읽는다.

1. `LIVE_STATE.md`
2. `LIVE_STATE.json`
3. `RELAY.md`
4. 실제 관련 코드
5. `../COMMON_BASELINE.md`
6. `../ERROR_LOG.md`

## 의미 있는 디버깅 작업 후

AI는 같은 작업에서 다음을 갱신한다.

- `LIVE_STATE.md`: 현재 문제를 사람이 읽기 쉽게 최신 상태로 덮어씀
- `LIVE_STATE.json`: 같은 내용을 기계가 읽기 쉽게 최신 상태로 덮어씀
- `RELAY.md`: 새 인수인계 메시지를 맨 위에 추가
- 실제 코드가 바뀌었으면 `../tcad/CURRENT/*`도 갱신
- 검증 결과가 바뀌었으면 `../CURRENT_STATUS.md`, `../ERROR_LOG.md`도 갱신

## 상태 규칙

- OBSERVED: 실제 로그/화면/파일에서 확인
- CONFIRMED: 반복 확인 또는 직접 결과로 확정
- PROPOSED: 아직 실행하지 않은 제안
- REJECTED: 시도했으나 폐기
- UNRESOLVED: 현재 미해결

## 절대 규칙

AI는 다른 AI가 남긴 PROPOSED 내용을 CONFIRMED처럼 취급하지 않는다.
실제 Sentaurus 로그와 현재 GitHub 코드가 가장 우선한다.


## Protocol v2

전체 AI 공용 읽기/쓰기 계약은 `../AI_SHARED_MEMORY_PROTOCOL.md`가 최상위 규칙이다.
기계가 읽을 수 있는 운영 설정은 `SYNC_STATE.json`에 있다.
