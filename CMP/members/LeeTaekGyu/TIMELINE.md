# Lee Taek Gyu Timeline

## 2026-09-28 — JuSubin/GitHub/Gmail sync audit

- **작성자:** ChatGPT
- **작업자:** 이택규
- **구분:** collaboration sync audit / blocker discovery
- **상태:** OBSERVED + UNRESOLVED
- **확인:** Gmail의 최신 CMP 메일은 JuSubin이 GitHub Issue #7에 남긴 진행 기록 알림이며, Issue 내용과 일치.
- **중요 발견:** 실제 `CMP/tcad/CURRENT/sdevice2_defect_on.cmd`는 Final SDevice v1.2로 업데이트되지 않았고 오래된 deck이 남아 있음.
- **의미:** 진행상황 로그는 동기화됐지만 실행 코드 source-of-truth는 동기화되지 않음.
- **다음:** exact Final SDevice v1.1/v1.2 전체 원문을 JuSubin 사용자 제공 파일에서 회수한 뒤 CURRENT에 반영. 원문 없이 Issue 요약으로 재구성 금지.



## 2026-09-21 — Common Baseline / AI collaboration workspace

- **작성자:** ChatGPT
- **Phase / Issue:** Phase 0 / #1
- **변경 유형:** 기록 / 인수인계
- **작업 내용:** Common Baseline v1의 source philosophy, 현재 TCAD 상태, 오류 이력, ChatGPT↔Claude 공유 구조를 GitHub에 정리.
- **결과 및 검증:** DmgL/Clean/DmgR region family와 p/n doping scale을 Sentaurus Visual에서 확인. SDevice2→SVisual2 TDR linkage는 미해결.
- **남은 일:** pp9_des.cmd File block과 실제 Node 9 TDR filename 확인.
