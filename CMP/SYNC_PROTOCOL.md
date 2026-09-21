# ChatGPT ↔ Claude Live Sync Protocol

## 목적

ChatGPT와 Claude가 서로의 대화를 직접 실시간으로 읽을 수 없기 때문에, 이 GitHub 저장소를 **공용 기억장치 + 코드 기준점**으로 사용한다.

'실시간 공유'의 의미:
- 각 AI가 작업 시작 시 최신 GitHub 상태를 읽는다.
- 의미 있는 작업 직후 GitHub를 갱신한다.
- 다음 AI는 같은 파일을 읽고 바로 이어서 작업한다.

## 작업 시작 시 반드시 읽기

순서:
1. `CMP/COMMON_BASELINE.md`
2. `CMP/CURRENT_STATUS.md`
3. `CMP/ERROR_LOG.md`
4. `CMP/NEXT_ACTIONS.md`
5. 관련 `CMP/tcad/CURRENT/*` 코드
6. `CMP/AI_HANDOFF.md`

## 코드 수정 규칙

1. 먼저 실제 현재 코드를 읽는다.
2. 추측으로 전체 코드를 재작성하지 않는다.
3. 최소 수정 우선.
4. 수정 후:
   - 어떤 파일을 바꿨는지
   - 왜 바꿨는지
   - 실행 결과
   - unresolved issue
   를 GitHub에 기록한다.
5. 실행 전 제안과 실행 후 검증 결과를 구분한다.

## Common Baseline 보호

다음은 사용자가 명시적으로 baseline 재설계를 승인하지 않는 한 변경 금지:
- Kou vertical epitaxy
- mesa 4 µm representative geometry
- 5 nm sidewall damaged region
- nominal sidewall Nt/Et/sigma
- common contacts/physics/mesh comparison condition

Project A/B 개선을 위해 baseline을 유리하게 바꾸지 않는다.

## 상태 표기

각 항목은 다음 중 하나로 기록:
- CONFIRMED
- OBSERVED
- PROPOSED
- UNRESOLVED
- REJECTED

## ChatGPT/Claude가 사용자에게 답할 때

난관 질문을 받으면 먼저:
- CURRENT_STATUS
- ERROR_LOG
- 해당 CURRENT code
를 읽고 답한다.

이미 해결된 오류를 다시 처음부터 추측하지 않는다.

## 작업 종료 시 갱신 대상

의미 있는 작업이면 최소:
- `CURRENT_STATUS.md`
- `ERROR_LOG.md` (오류/해결이 있을 때)
- `NEXT_ACTIONS.md`
- `AI_HANDOFF.md`

코드가 바뀌면:
- `tcad/CURRENT/*`

## Claude 시작 프롬프트

Claude에게 다음과 같이 요청:

> GitHub repository TaekGyu0801/GGYU의 CMP 폴더를 이 프로젝트의 source of truth로 사용해. 먼저 CMP/COMMON_BASELINE.md, CURRENT_STATUS.md, ERROR_LOG.md, NEXT_ACTIONS.md, SYNC_PROTOCOL.md와 관련 tcad/CURRENT 코드를 읽고, 그 상태에서 이어서 작업해. 추측으로 baseline이나 코드를 재설계하지 말고, 작업 후에는 같은 파일들을 최신 상태로 갱신해.

## ChatGPT 시작 프롬프트

> GitHub의 TaekGyu0801/GGYU/CMP를 먼저 읽고 그 최신 상태를 기준으로 이어서 작업해. COMMON_BASELINE, CURRENT_STATUS, ERROR_LOG, NEXT_ACTIONS, SYNC_PROTOCOL, tcad/CURRENT 코드를 우선 확인하고, 의미 있는 작업 후 GitHub 상태를 갱신해.


## VCAT-style dashboard sync

공동 진행 상황은 GitHub Pages dashboard와 GitHub Issues에도 반영한다.

- Phase task 원본: GitHub Issues #1~#6
- Dashboard data: `docs/data/status.json`
- Dashboard source: `docs/index.html`, `docs/app.js`, `docs/style.css`

의미 있는 작업 후 상태가 바뀌면 AI는 다음을 함께 갱신한다.
1. `CMP/CURRENT_STATUS.md`
2. 필요한 경우 `CMP/ERROR_LOG.md`
3. `CMP/NEXT_ACTIONS.md`
4. 관련 member `TIMELINE.md`
5. `docs/data/status.json`
6. 관련 GitHub Issue 체크리스트/설명

즉 dashboard는 별도 수기 기록이 아니라 GitHub 상태를 사람이 빠르게 확인하기 위한 요약 화면으로 운용한다.
