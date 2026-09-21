# CMP MicroLED TCAD — AI Project Guide

이 저장소는 연구자 **이택규 / 주수빈**과 **ChatGPT / Claude**가 같은 상태를 공유하며 연구하기 위한 공동 작업 공간이다.

## Start order

작업 시작 전에 반드시 다음 순서로 읽는다.

1. `CMP/COMMON_BASELINE.md`
2. `CMP/CURRENT_STATUS.md`
3. `CMP/ERROR_LOG.md`
4. `CMP/NEXT_ACTIONS.md`
5. 관련 GitHub Issue
6. 작업 대상 `CMP/members/<name>/README.md`와 `TIMELINE.md`
7. 관련 `CMP/tcad/CURRENT/*`

## Truth hierarchy

충돌 시 우선순위:
1. 실제 코드 / 실행 로그 / 결과 파일
2. COMMON_BASELINE.md
3. CURRENT_STATUS.md
4. 최신 GitHub Issue
5. ERROR_LOG.md / NEXT_ACTIONS.md
6. 개인 README / TIMELINE
7. 과거 AI 채팅 내용

## Absolute rules

- 검증되지 않은 결과를 성공으로 기록하지 않는다.
- 같은 physical parameter에 충돌하는 문헌값을 근거 없이 혼합하지 않는다.
- JBD 4 µm pitch를 actual mesa width로 해석하지 않는다.
- Calibration parameter를 direct literature value처럼 쓰지 않는다.
- Common Baseline을 Project A/B 성능에 유리하도록 변경하지 않는다.
- 코드 수정 시 먼저 현재 실제 코드를 읽는다.
- 개인 폴더를 수정하면 같은 작업에서 TIMELINE.md도 갱신한다.

## Roles

- Common Baseline: 팀 공통
- Project A: Carbon-Induced High-Resistivity Edge
- Project B: Localized AlGaN Lateral Heterobarrier
- ChatGPT / Claude: 코드 리뷰, 오류 분석, 문헌 정리, 상태 동기화 보조
