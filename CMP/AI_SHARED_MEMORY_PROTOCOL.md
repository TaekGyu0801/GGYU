# CMP AI Shared Memory Protocol v2

이 문서는 **이택규 GPT / 주수빈 GPT / Claude**가 서로 다른 채팅·노트북·계정에서 작업하더라도
GitHub를 공용 기억장치로 사용해 같은 연구 상태를 읽고 이어서 작업하기 위한 **최상위 운영 규칙**이다.

> 핵심 원칙: AI끼리 서로의 비공개 채팅을 직접 읽는다고 가정하지 않는다.
> 의미 있는 작업 결과를 GitHub에 기록하고, 다음 AI는 GitHub의 최신 기록을 읽는다.

---

## 1. 작업자 식별

새 채팅에서 사용자가 다음 중 하나로 시작하면 해당 세션의 작업자로 고정한다.

- `이택규`
- `주수빈`

사용자가 명시적으로 변경하기 전까지 작업자를 바꾸지 않는다.

---

## 2. 모든 AI의 세션 시작 절차 — READ FIRST

작업자 확인 직후, 본격 답변/코드 작성 전에 최신 GitHub 상태를 읽는다.

읽기 순서:

1. `CMP/.ai-sync/LIVE_STATE.md`
2. `CMP/.ai-sync/LIVE_STATE.json`
3. `CMP/.ai-sync/RELAY.md`
4. `CMP/CURRENT_STATUS.md`
5. `CMP/ERROR_LOG.md`
6. `CMP/NEXT_ACTIONS.md`
7. `CMP/TEAM_TIMELINE.md`
8. 현재 작업자의 개인 `TIMELINE.md`
9. GitHub LIVE LOG Issue #7 최신 comments
10. 관련 Phase Issue
11. 실제 작업 대상 `CMP/tcad/CURRENT/*` 코드

### 새 채팅 첫 답변 필수 항목

- 현재까지 팀 진행 상황
- 가장 마지막으로 실제 수행한 작업
- 현재 blocker
- 현재 작업자의 개인 최신 작업
- 바로 이어서 할 다음 작업
- CMP 대시보드: https://taekgyu0801.github.io/GGYU/

최신 정보가 충돌하면 임의로 하나를 선택하지 말고 충돌 사실을 알려준다.

---

## 3. GitHub가 장기 기억이다

정보 종류별 저장 위치:

| 정보 | 저장 위치 |
|---|---|
| 현재 한 장 요약 | `CMP/.ai-sync/LIVE_STATE.md` |
| 기계가 읽는 현재 상태 | `CMP/.ai-sync/LIVE_STATE.json` |
| AI → AI 인수인계 | `CMP/.ai-sync/RELAY.md` |
| 팀 현재 상태 | `CMP/CURRENT_STATUS.md` |
| 오류/실패/해결 이력 | `CMP/ERROR_LOG.md` |
| 다음 할 일 | `CMP/NEXT_ACTIONS.md` |
| 이택규 작업 이력 | `CMP/members/LeeTaekGyu/TIMELINE.md` |
| 주수빈 작업 이력 | `CMP/members/JuSubin/TIMELINE.md` |
| 팀 전체 주요 이력 | `CMP/TEAM_TIMELINE.md` |
| 시간순 append-only 이벤트 | GitHub Issue #7 |
| 장기 task / Phase | GitHub Issues #1~#6 및 후속 Issues |
| 현재 실제 TCAD 코드 | `CMP/tcad/CURRENT/*` |

채팅 기억보다 GitHub의 최신 실제 코드/로그/기록을 우선한다.

---

## 4. 의미 있는 작업이 발생하면 자동 WRITE

사용자가 별도로 "저장해"라고 하지 않아도 아래 사건이 생기면 같은 작업에서 GitHub를 갱신한다.

- 코드를 작성/수정함
- 새 오류가 발생함
- 오류 원인을 확인함
- 시뮬레이션 성공/실패를 확인함
- 로그/스크린샷/결과에서 새로운 사실을 확인함
- 중요한 연구 아이디어를 채택/폐기함
- Common Baseline 관련 판단이 생김
- Project A/B 설계가 바뀜
- blocker가 생기거나 해결됨
- 다음 작업이 바뀜
- 다른 연구원/AI가 이어받아야 함

단순 잡담, 일반 개념 질문, 아직 연구에 반영하지 않은 사소한 아이디어는 기록하지 않는다.

---

## 5. WRITE 순서

의미 있는 사건이 생기면 아래 순서로 기록한다.

1. **실제 코드/결과 파일** — 변경이 있을 때만
2. **현재 작업자 TIMELINE**
3. **TEAM_TIMELINE** — 팀 공통 의미가 있을 때
4. **ERROR_LOG** — 오류/실패/해결일 때
5. **CURRENT_STATUS** — 현재 상태가 바뀌었을 때
6. **NEXT_ACTIONS** — 다음 단계가 바뀌었을 때
7. **.ai-sync/LIVE_STATE.md + LIVE_STATE.json**
8. **.ai-sync/RELAY.md** — 다른 AI가 바로 이어받아야 할 때
9. **Issue #7 comment** — 의미 있는 이벤트를 시간순으로 append
10. **관련 Phase Issue** — 완료 조건/장기 task가 바뀌었을 때

모든 파일을 매번 억지로 수정하지 않는다. 실제로 바뀐 상태만 갱신한다.

---

## 6. 상태 라벨은 반드시 구분

- `PROPOSED`: AI/연구원의 제안, 아직 실행 전
- `OBSERVED`: 실제 로그/화면/파일에서 직접 확인
- `CONFIRMED`: 충분한 검증으로 확정
- `UNRESOLVED`: 아직 해결되지 않음
- `REJECTED`: 시도했으나 실패/폐기

제안한 코드를 실행된 코드처럼 기록하지 않는다.
AI 해석을 실험 결과처럼 기록하지 않는다.

---

## 7. Issue #7 공용 이벤트 형식

각 의미 있는 작업 뒤 Issue #7에 가능하면 아래 형식으로 comment를 남긴다.

```text
[YYYY-MM-DD HH:MM]
작업자: 이택규 / 주수빈
AI: ChatGPT / Claude
구분: PROGRESS / BLOCKER / FIX / RESULT / DECISION / HANDOFF
상태: PROPOSED / OBSERVED / CONFIRMED / UNRESOLVED / REJECTED

요약:
...

근거:
- 로그 / 화면 / 코드 / 결과 파일

변경:
- 바뀐 파일 또는 파라미터

다음:
...
```

Issue #7은 여러 AI가 동시에 사용하기 쉬운 append-only 공용 로그다.

---

## 8. 코드 수정 전 반드시 다시 읽기

AI가 GitHub의 코드를 수정하려면 바로 직전에 해당 파일의 최신 버전을 다시 읽는다.

규칙:
- 오래된 채팅에 있는 코드를 기준으로 덮어쓰지 않는다.
- 최신 전체 원문이 없는 SDE/SDevice 파일을 추정 생성하지 않는다.
- 최소 수정 우선.
- 변경 후 무엇을 바꿨고 왜 바꿨는지 기록.
- 실행 전이면 `PROPOSED`, 실행 결과가 있으면 근거에 맞는 상태로 기록.

---

## 9. 동시 작업 충돌 방지

다른 AI/연구원이 같은 파일을 수정했을 수 있으므로 WRITE 직전에 최신 GitHub 버전을 다시 확인한다.

만약 읽은 뒤 파일이 바뀌었다면:
1. 새 버전을 다시 읽음
2. 양쪽 변경을 보존해 병합
3. 의미 충돌은 임의 해결하지 않음
4. 충돌 내용을 `UNRESOLVED`로 기록
5. 연구자 판단이 필요하면 명확히 요청

다른 사람의 결과를 덮어써서 없애지 않는다.

---

## 10. AI 인수인계 규칙

작업이 막히거나 다른 AI가 이어받아야 할 때 `.ai-sync/RELAY.md` 최상단에 새 기록을 추가한다.

반드시 포함:
- 작업자
- 사용한 AI
- 정확한 현재 오류/문제
- 실제 확인된 근거
- 현재 관련 코드 경로
- 이미 시도한 것
- 실패한 접근
- 다음에 가장 먼저 확인할 것
- 변경하면 안 되는 baseline 조건

다음 AI는 RELAY를 읽고 이미 실패한 시도를 처음부터 반복하지 않는다.

---

## 11. Common Baseline 보호

사용자의 명시적 승인 없이 임의 변경하지 않는다.

- Kou 기반 vertical epitaxy
- representative mesa 4 µm
- sidewall damage width 5 nm
- nominal Nt / Et / sigma
- A/B 공통 contacts / physics / 비교 조건

Project A 또는 Project B에 유리하도록 Common Baseline을 변경하지 않는다.

---

## 12. 기록 실패 시 절대 성공했다고 말하지 않기

GitHub connector가 없거나 권한/도구 오류 때문에 WRITE가 실패했다면:

- "GitHub 기록 완료"라고 말하지 않는다.
- 어떤 파일/Issue가 미반영됐는지 사용자에게 알린다.
- 가능하면 같은 세션에서 다시 시도한다.

AI는 백그라운드에서 나중에 자동 저장한다고 약속하지 않는다.

---

## 13. 응답 종료 시 동기화 표시

의미 있는 작업을 수행한 답변 끝에는 짧게 현재 동기화 상태를 알린다.

예:

```text
GitHub 동기화: 완료
- JuSubin/TIMELINE.md
- LIVE_STATE.md
- Issue #7
```

실제로 갱신한 항목만 적는다.

---

## 14. 이 프로토콜의 우선순위

AI 협업 운영 규칙이 서로 충돌할 경우:

1. `CMP/AI_SHARED_MEMORY_PROTOCOL.md` (이 문서)
2. `CMP/AI_COLLAB_RULES.md`
3. `CMP/SESSION_START_PROTOCOL.md`
4. `CMP/AUTO_LOG_POLICY.md`
5. `CMP/CHAT_TO_GITHUB_PROTOCOL.md`

연구 사실/파라미터의 우선순위는 별도로 실제 코드·로그·COMMON_BASELINE을 따른다.
