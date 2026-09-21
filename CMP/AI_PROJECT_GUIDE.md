# CMP MicroLED TCAD — AI Project Guide

이 저장소는 연구자 **이택규 / 주수빈**과 **ChatGPT / Claude**가 같은 상태를 공유하며 연구하기 위한 공동 작업 공간이다.

## Start order

작업 시작 전에 반드시 다음 순서로 읽는다.

1. `CMP/.ai-sync/LIVE_STATE.md`
2. `CMP/.ai-sync/LIVE_STATE.json`
3. `CMP/.ai-sync/RELAY.md`
4. `CMP/COMMON_BASELINE.md`
5. `CMP/CURRENT_STATUS.md`
6. `CMP/ERROR_LOG.md`
7. `CMP/NEXT_ACTIONS.md`
8. 관련 GitHub Issue
9. 작업 대상 `CMP/members/<name>/README.md`와 `TIMELINE.md`
10. 관련 `CMP/tcad/CURRENT/*`

## Why .ai-sync exists

ChatGPT와 Claude는 서로의 채팅 내용을 직접 읽지 못한다.
따라서 `CMP/.ai-sync/`를 **AI 간 실시간에 가까운 인수인계 채널**로 사용한다.

- `LIVE_STATE.md`: 현재 상황 한 장 요약
- `LIVE_STATE.json`: 기계가 읽기 쉬운 상태
- `RELAY.md`: AI → AI 인수인계 메시지

사람용 대시보드와 분리해서 운영하며, 작업 시작 시 AI가 우선 읽는다.

## Truth hierarchy

충돌 시 우선순위:
1. 실제 코드 / 실행 로그 / 결과 파일
2. `.ai-sync/LIVE_STATE.md`의 최신 OBSERVED/CONFIRMED 기록
3. COMMON_BASELINE.md
4. CURRENT_STATUS.md
5. 최신 GitHub Issue
6. ERROR_LOG.md / NEXT_ACTIONS.md
7. 개인 README / TIMELINE
8. 과거 AI 채팅 내용

## Absolute rules

- 검증되지 않은 결과를 성공으로 기록하지 않는다.
- 같은 physical parameter에 충돌하는 문헌값을 근거 없이 혼합하지 않는다.
- JBD 4 µm pitch를 actual mesa width로 해석하지 않는다.
- Calibration parameter를 direct literature value처럼 쓰지 않는다.
- Common Baseline을 Project A/B 성능에 유리하도록 변경하지 않는다.
- 코드 수정 시 먼저 현재 실제 코드를 읽는다.
- 개인 폴더를 수정하면 같은 작업에서 TIMELINE.md도 갱신한다.
- PROPOSED fix를 실행 결과 없이 CONFIRMED로 승격하지 않는다.
- 다른 AI가 이미 시도해 실패한 접근을 RELAY 확인 없이 반복하지 않는다.

## Roles

- Common Baseline: 팀 공통
- Project A: Carbon-Induced High-Resistivity Edge
- Project B: Localized AlGaN Lateral Heterobarrier
- ChatGPT / Claude: 코드 리뷰, 오류 분석, 문헌 정리, 상태 동기화 보조
