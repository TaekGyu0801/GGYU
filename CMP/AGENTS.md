# AI Agent Entry Point

이 CMP 프로젝트에서 작업하는 모든 AI(ChatGPT / Claude)는 **가장 먼저 `AI_SHARED_MEMORY_PROTOCOL.md`를 읽고 따른다.**

그 다음 Claude를 포함한 구현 AI는 `CLAUDE_PROJECT_INSTRUCTIONS.md`에서 연구 목적·baseline 보호·재현성·코딩 역할을 확인하고, 현재 상태를 아래 순서로 읽는다.

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

## TCAD 프로젝트 명명 규칙 (2026-10-09 확정)

새 CMP Baseline/Project A/Project B SWB 프로젝트를 생성하거나 이름을 제안하기 전에 `PROJECT_NAMING_CONVENTION.md`를 읽는다.

형식: `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>`. 현재 준비 중인 신규 후보는 `CMP_BASELINE_1.2.0_CAL`이고 기존 완성 프로젝트 `JUSUBIN_FAST_HALF_5V_TEST`와는 별도이다. 정확한 부모 코드·물성/mesh 버전과 실험 파라미터를 기록하고, 실제 결과 없이 후보를 검증 완료라고 부르지 않는다.

### 공동 적용 범위 — 이택규 / 주수빈 모두 필수 (2026-10-10 재확인)

- 이택규와 주수빈이 **각자의 별도 채팅/Claude에서 새 CMP SWB 프로젝트 또는 배포용 작업 결과물**을 만들 때 동일한 `CMP_<TYPE>_<MAJOR.MINOR.PATCH>_<TAG>` 규칙을 적용한다. 작업자가 주수빈이라고 예외가 생기지 않는다.
- 새 소자 명명 전에 `PROJECT_NAMING_CONVENTION.md`를 읽고, 부모 버전과 주요 변경을 문서화한다. 기존 프로젝트는 소급해서 이름을 바꾸지 않는다.
- **SWB 실행에 필요한 내부 파일명/생성 파일명은 임의로 바꾸지 않는다**. 버전은 프로젝트와 별도 배포 산출물에 적용한다.
- 현재 이택규 CAL 소자는 기존 custom `.par` 방식으로 실행 중이라고 사용자가 보고했다. 차기 신규 소자에서 교수님이 재현하기 쉬운 SWB-native 명령/파라미터 편집 방식을 검토한다.
