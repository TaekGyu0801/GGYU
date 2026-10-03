## 2026-10-03 — active run identity correction after grid/source hashes

- 작업자: 이택규
- 상태: OBSERVED / CORRECTION
- 추가 터미널 검증 결과:
  - Copy x6 path: n1_msh.tdr SHA256 = 716df696..., sd_fdiv_des.cmd SHA256 = ee13bea5...
  - Copy x7 path: n1_msh.tdr SHA256 = 762d2d57..., sd_fdiv_des.cmd SHA256 = 56a8be69...
  - Copy x8 path: n1_msh.tdr SHA256 = 762d2d57..., sd_fdiv_des.cmd SHA256 = 56a8be69...
- 따라서 Copy x7과 Copy x8은 source + generated mesh가 byte-identical.
- Copy x6과 Copy x7은 pp6_des.cmd/par은 동일했지만 source/grid가 다르므로 전체 simulation input이 동일하다고 볼 수 없음.
- Copy x8은 Copy x7과 same source/grid/par이지만 pp6_des.cmd hash가 다르며 intermediate TDR files가 존재. Exact diff로 output-save-only revision인지 확인 필요.
- 다음: Copy x7 vs x8 pp6_des.cmd diff, Copy x6 vs x7 source diff 확인.

## 2026-10-03 — active run comparison from terminal

- 작업자: 이택규
- 상태: OBSERVED
- semi437의 세 SDevice run을 직접 비교함.
- 첫 번째와 두 번째 run은 pp6_des.cmd와 pp6_des.par SHA-256이 각각 동일하여 preprocessed SDevice command/parameter가 동일함.
- 첫 번째 진행: pseudo-time 약 0.94147, anode 약 4.707 V.
- 두 번째 진행: pseudo-time 약 0.92964, anode 약 4.648 V.
- 세 번째 run은 pp6_des.par은 동일하지만 pp6_des.cmd 해시가 다르고 intermediate TDR 파일들이 존재함. 진행은 pseudo-time 약 0.92647, anode 약 4.632 V.
- 세 run 모두 고전압 구간에서 Newton iteration 정체와 timestep cutback이 runtime 병목으로 관찰됨.
- 다음: 첫 번째와 세 번째 pp6_des.cmd exact diff, grid input hash 확인.

## 2026-10-03 — semi437 3 active baseline runs: exact pp6 hash/progress comparison

- **작성자:** ChatGPT
- **작업자:** 이택규
- **상태:** OBSERVED
- **근거:** semi437 터미널에서 세 active project directory의 file list, SHA-256, n6_des.out tail 직접 확인.
- **Run A:** `...Copy_Copy_Copy_Copy_Copy_Copy` (Sep26 start)
  - pp6_des.cmd SHA256 = `928613d261c0265b8ac44acb97ed6d80867557dd2910f2648abcc477f60440c3`
  - pp6_des.par SHA256 = `60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039`
  - latest visible pseudo-time ≈0.94147, anode ≈4.707 V
  - repeated high-bias Newton stalls; a failed step exceeded 50 iterations and cost ~1073 s before timestep cutback.
- **Run B:** `...Copy_Copy_Copy_Copy_Copy_Copy_Copy` (Sep28 start)
  - pp6_des.cmd SHA256 identical to Run A
  - pp6_des.par SHA256 identical to Run A
  - latest visible pseudo-time ≈0.92964, anode ≈4.648 V
  - same high-bias convergence pattern.
  - Therefore SDevice preprocessed command/parameter are byte-identical to Run A.
- **Run C:** `...Copy_Copy_Copy_Copy_Copy_Copy_Copy_Copy` (Sep28 start)
  - pp6_des.cmd SHA256 = `2dfcc98effe145ec944fb8ee5d6914f5f098e54d1bf2319c69acc76afe1692e6` (different)
  - pp6_des.par SHA256 identical to A/B
  - latest visible pseudo-time ≈0.92647, anode ≈4.632 V
  - intermediate TDRs `n6_inter_0000..0003_des.tdr` exist, consistent with a revised output-save workflow.
- **Interpretation:** A and B are duplicate SDevice decks at cmd/par level; C is a different command revision with the same parameter file. Exact command-line differences between A/B and C are not yet inspected.
- **Next:** run `diff -u` between A and C pp6_des.cmd, hash the grid input(s), and inspect Solve/Math blocks before deciding whether any duplicate run should be stopped.

## 2026-10-03 — semi437 active TCAD process inventory 확인

- **작성자:** ChatGPT
- **작업자:** 이택규
- **구분:** runtime evidence
- **상태:** OBSERVED
- **직접 확인:** 2026-10-03 22:31:57 KST 터미널 `ps -ef` 출력에서 semi437 계정의 active SDevice가 3개 확인됨.
  1. PID 61681 — started Sep26 — `.../GaN_PiN_Diode_Copy_Copy_Copy_Copy_Copy_Copy` — `sdevice --max_threads 4 pp6_des.cmd`
  2. PID 42738 — started Sep28 — `.../GaN_PiN_Diode_Copy_Copy_Copy_Copy_Copy_Copy_Copy` — `sdevice --max_threads 4 pp6_des.cmd`
  3. PID 79167 — started Sep28 — `.../GaN_PiN_Diode_Copy_Copy_Copy_Copy_Copy_Copy_Copy_Copy` — `sdevice --max_threads 4 pp6_des.cmd`
- **사용자 설명:** 세 작업 중 두 개는 같은 조건이며, 사용자가 Workbench에서 부르는 Copy 6 / Copy 7이 같은 소자라고 설명.
- **주의:** 폴더명의 Copy 반복 횟수와 사용자가 부르는 Workbench Copy 번호의 정확한 대응은 아직 확정하지 않음.
- **다음:** 각 3개 작업 디렉터리에서 `pp6_des.cmd`, `pp6_des.par`, `n6_des.out` tail을 직접 수집해 동일/상이 조건을 확정.

## 2026-10-03 — 7-day baseline runtime concern / numerics optimization direction

- **작성자:** ChatGPT
- **작업자:** 이택규
- **구분:** runtime diagnosis / proposed numerical optimization
- **상태:** USER-REPORTED + PROPOSED
- **사용자 보고:** 주수빈이 실행한 기준소자가 약 7일간 계산 중인 것으로 보임. 현재 세션에서 최신 solver output으로 7일 연속 progress 여부는 직접 검증하지 못함.
- **확인된 기존 병목:** 2026-09-29 Node 6은 ~4.66 V 부근에서 Newton failure 후 timestep이 ~8.67e-6까지 cutback됨.
- **numerics 관찰:** GitHub CURRENT의 stale deck 기준 Transient MaxStep=1e-3이면 0→5 V ramp에서 최대 전압 increment가 5 mV이므로 cutback이 없어도 최소 약 1000 accepted steps가 필요함.
- **제안:** baseline physics/Nt/Et/sigma/geometry는 유지하고, exact running v1.1/v1.2 source를 먼저 회수한 뒤 numerical-only optimization branch를 만들어 step control, Newton iteration policy, ErrRef, mesh node count를 benchmark. Quasistationary는 transient 대비 별도 controlled comparison으로만 시험.
- **주의:** GitHub CURRENT SDevice가 실제 Final v1.2와 불일치하므로 stale 파일을 바로 수정하지 않음.

## 2026-10-03 — 논문화 전략 / novelty framing 제안

- **작성자:** ChatGPT
- **작업자:** 이택규
- **구분:** manuscript strategy / research framing
- **상태:** PROPOSED
- **핵심:** 동일한 5 nm damaged-sidewall Common Baseline에서 Project A(GaN:C resistive blocking)와 Project B(localized AlGaN heterobarrier blocking)를 같은 injected current 기준으로 직접 비교하는 논문 구조를 제안.
- **노벨티 경계:** generic current confinement 자체가 아니라, 동일 defect physics를 보존한 채 resistive vs band-offset edge engineering을 mechanism-resolved 비교하는 것이 핵심. Carbon-localized edge는 잠재적으로 강한 차별점, AlGaN은 기존 lateral-confinement 문헌이 있어 geometry/use-case/comparison level로 claim 제한.
- **필수 결과:** edge carrier access 감소 → integrated sidewall SRH 감소 → MQW radiative/IQE 보존/증가의 causal chain과, Vf/current-crowding/Auger tradeoff 및 optimum design window를 제시.
- **산출물:** `CMP/PAPER_MANUSCRIPT_STRATEGY_PROPOSED.md`

# Lee Taek Gyu Timeline

## 2026-09-28 — NtSide=1e18 근거 수준 재검증 / 발표용 연구노트

- **작성자:** ChatGPT
- **작업자:** 이택규
- **구분:** literature evidence / baseline parameter provenance
- **상태:** CONFIRMED BOUNDARY
- **확인:** Wu et al. (Micro and Nanostructures 177, 207542, 2023)는 양쪽 sidewall edge 5 nm 이내 acceptor-like trap 및 trap-density/energy-level sweep 방법을 직접 지지.
- **중요 경계:** 현재 확인 가능한 근거만으로 Wu 논문이 NtSide=1e18 cm^-3를 보편적/직접 측정 정답값으로 확정했다고 주장하면 안 됨.
- **해석:** CMP의 NtSide=1e18 cm^-3는 nominal Defect-ON calibration/sensitivity starting value로 유지. 다른 III-nitride MicroLED 수치 모델에서 1e18 cm^-3 규모 sidewall trap 사용 사례가 있어 order-of-magnitude plausibility는 있음.
- **발표 표현:** "문헌 기반 plausible nominal calibration value이며 최종 결론은 NtSide sweep으로 검증한다."
- **산출물:** 발표/Q&A용 paper-style PDF 연구노트 생성.


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
