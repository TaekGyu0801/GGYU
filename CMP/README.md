# CMP — MicroLED Sidewall TCAD Collaboration Hub

이 디렉터리는 **ChatGPT ↔ Claude ↔ 연구자**가 같은 프로젝트 상태를 공유하기 위한 단일 기준 저장소(Single Source of Truth)이다.

## 가장 먼저 읽을 파일

1. [COMMON_BASELINE.md](./COMMON_BASELINE.md) — 변하면 안 되는 Common Baseline v1
2. [CURRENT_STATUS.md](./CURRENT_STATUS.md) — 지금 실제로 어디까지 진행됐는지
3. [ERROR_LOG.md](./ERROR_LOG.md) — 현재/과거 오류와 해결 이력
4. [NEXT_ACTIONS.md](./NEXT_ACTIONS.md) — 다음에 할 일
5. [SYNC_PROTOCOL.md](./SYNC_PROTOCOL.md) — ChatGPT/Claude 공용 작업 규칙
6. [AI_HANDOFF.md](./AI_HANDOFF.md) — 최신 인수인계 요약

## TCAD 현재 코드

- `tcad/CURRENT/sdevice2_defect_on.cmd`
- `tcad/CURRENT/svisual1_iv.tcl`
- `tcad/CURRENT/svisual2_maps.tcl`

> 현재 대화에서 SDE와 SDevice1의 **완전한 최신 코드 원문은 아직 GitHub에 동기화되지 않았다.**
> 확인되지 않은 코드를 임의 생성하지 말고, 연구자가 보내는 실제 코드로 업데이트한다.

## 핵심 운영 원칙

- GitHub에 기록된 최신 상태가 ChatGPT/Claude 채팅 기억보다 우선한다.
- 코드 수정 전 반드시 `COMMON_BASELINE.md`와 `CURRENT_STATUS.md`를 읽는다.
- 해결되지 않은 오류는 `ERROR_LOG.md`에 남긴다.
- 의미 있는 변경이 끝나면 `CURRENT_STATUS.md`, `NEXT_ACTIONS.md`, `AI_HANDOFF.md`를 갱신한다.
- Common Baseline 값을 Project A/B 성능에 유리하도록 임의 변경하지 않는다.
