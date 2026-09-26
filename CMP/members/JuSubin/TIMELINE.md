# Ju Subin Timeline

## 2026-09-26 — Node12 최소 수정안 확정

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** PROPOSED FIX
- **수정:** global `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")` 제거.
- **추가:** `Clean_pGaN`, `DmgL_pGaN`, `DmgR_pGaN`에만 동일 `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")` 적용.
- **유지:** `Thermionic`, `NtSide`, trap Et/sigma, geometry, Plot, Math, Solve 전부 유지.
- **검증:** 수정 후 NtSide=0/1e18을 동일 final source/PAR revision에서 재실행.


## 2026-09-26 — Node 12 project/scheduler log interpretation

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED
- **근거:** Project Log 화면.
- **확인:** Node 12 SDevice가 실제로 시작된 뒤 약 수 초 내 `exited abnormally: exit()`로 종료하고 scheduler가 failed 처리, `gsub exits with status 1`.
- **의미:** 이 화면은 실행 실패 사실과 시점을 확인해 주지만, root-cause message 자체는 포함하지 않음.
- **진단 우선순위:** root cause는 `n12_des.log`/`n12_des.err` 및 `pp12_des.par` 내용으로 판단. 현재 가장 강한 후보는 InGaN에서 Mg incomplete-ionization parameter가 없는 상태에서 global Mg incomplete-ionization을 활성화한 material-scope mismatch.


## 2026-09-26 — 중요 정정: Node6/Node12 parameter file도 서로 다른 revision

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / COMPARISON INVALIDATED
- **근거:** 사용자 제공 성공 Node6 `pp6_des.par` 화면과 실패 Node12 `pp12_des.par` 화면 비교.
- **Node6 par:** GaN Ionization에 `PDopantActiveConcentration` (E0=0.15, g=4, Xsec=1e-12) 및 `NDopantActiveConcentration` (E0=0.05, g=2, Xsec=1e-12).
- **Node12 par:** GaN Ionization에 `pMagnesiumActiveConcentration` (E0=0.2, alpha=8e-9, g=4, Xsec=1e-14).
- **결론:** 기존 Node6와 current Node12는 command deck뿐 아니라 parameter file도 다른 revision. 따라서 Node12만 수정해서 기존 Node6와 비교하는 것은 fair NtSide-only comparison이 아님.
- **정정:** 직전 'Node12만 region-scoped Mg incomplete ionization으로 수정 후 기존 Node6와 비교' 제안은 비교 목적에는 철회.
- **올바른 방법:** 최종 baseline source + parameter file을 먼저 freeze하고, 그 동일 revision으로 NtSide=0과 1e18을 둘 다 새로 preprocess/run해야 함.
- **진단 목적:** Node12 crash를 고치기 위한 region-scoped Mg incomplete-ionization 실험은 가능하지만, 그 결과는 기존 Node6와 final quantitative comparison에 사용하지 않음.


## 2026-09-26 — pp12_des.par confirms Mg incomplete-ionization material-scope mismatch

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / PROPOSED FIX
- **근거:** 사용자가 Node 12의 전체 `pp12_des.par` 화면 제공.
- **parameter file 내용:** `Material="GaN"`의 `Ionization` block에 `Species("pMagnesiumActiveConcentration")`만 정의됨 (E_0=0.2, alpha=8e-9, g=4.0, Xsec=1e-14). InGaN/AlGaN Ionization block은 없음.
- **실패 log와 결합한 판단:** current source의 global `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`가 전체 device에 활성화된 상태에서 InGaN QW에서 Mg-related species의 ionization parameter가 없다는 메시지 직후 SDevice가 종료됨. material scope mismatch가 가장 강한 root-cause 후보.
- **최소 수정안:** global IncompleteIonization을 제거하고 Mg가 실제 p-GaN에 필요한 `Clean_pGaN`, `DmgL_pGaN`, `DmgR_pGaN`에만 region-specific으로 적용. Thermionic/trap Et/sigma/NtSide/Plot은 건드리지 않음.
- **검증:** 수정 후 Node12 재-preprocess → 초기화 통과/Poisson solve 진입 여부 확인. 통과 시 원인 확인 강화.
- **공정 비교 주의:** 최종 baseline freeze 후 NtSide=0과 1e18은 동일 final source revision으로 다시 비교해야 함.


## 2026-09-26 — Current full SDevice source inspected; stale Node 6 provenance identified

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / ROOT-CAUSE NARROWING
- **자료:** 사용자가 현재 원본 SDevice 전체 코드를 제공.
- **확인:** source에서 `@NtSide@`는 trap `Conc`에만 사용되며, `NtSide`에 따른 `#if/#else/#endif` conditional은 없음.
- **현재 source 고정 Physics:** `Thermionic`, `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`, Mg/quasi-Fermi 관련 Plot fields 포함.
- **의미:** 현재 source를 preprocess한 Node 12가 이 구성을 갖는 것은 정상. 반면 성공 Node 6 pp6에는 이 항목들이 없으므로 Node 6은 현재 source revision으로 재-preprocess된 node가 아니라 과거 source revision의 generated/output artifact일 가능성이 매우 높음.
- **따라서:** 기존 Node6(success) vs 현재 Node12(fail)는 엄밀한 same-source NtSide-only 비교가 아님.
- **현재 실패 핵심 후보:** species-selected incomplete ionization이 InGaN QW의 Mg species에 적용되면서 parameter file에 해당 ionization parameter가 없어 초기화 종료. 실제 Node12 log가 InGaN QW의 Mg incomplete-ionization parameter missing 직후 종료.
- **다음:** `pp12_des.par`에서 `Ionization`, `Magnesium`, `InGaN` block 확인. parameter definition과 doping species naming을 확인한 뒤 최소 수정 결정.


## 2026-09-26 — Node 12 단독 재실행에서도 동일 failure 재현

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / REPRODUCIBLE
- **근거:** 사용자가 Node 12만 다시 실행했으나 동일하게 failed 상태가 재현됨.
- **의미:** 일회성 queue/license/transient 환경 오류 가능성은 낮아지고, Node 12가 사용하는 현재 preprocessed input/configuration에 재현성 있는 문제가 있을 가능성이 높아짐.
- **중요 정정 유지:** 사용자는 동일 source에서 NtSide만 split했다고 확인했으므로, pp6/pp12 차이는 source를 별도로 편집했다는 뜻이 아님.
- **가장 유력한 설명 후보:** (1) source 내부 NtSide-dependent preprocessor conditional, 또는 (2) Node 6이 과거 source 버전의 stale/cached preprocess/output을 재사용하고 Node 12만 현재 source로 재-preprocess됨.
- **다음:** 원본 `sd_fdiv_des.cmd`에서 `NtSide`, `#if/#else/#endif`, `Thermionic`, `IncompleteIonization`, Mg Plot fields를 직접 확인하고, Node6/12 Job Log의 preprocess source timestamp/provenance를 비교.


## 2026-09-26 — 중요 정정: 사용자 확인상 source는 동일, NtSide만 split

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** USER-CONFIRMED / UNRESOLVED
- **사용자 확인:** Node 6과 Node 12는 원본 코드를 별도로 수정한 것이 아니라 동일한 SDevice source에서 `NtSide`만 0 / 1e18로 split하여 실행함.
- **정정:** 직전의 "Node 12 source deck drift" 해석은 확정할 수 없음. preprocessed deck 차이는 source 자체가 달랐다는 증거가 아니라, NtSide-dependent preprocessing/conditional branch 또는 node input/version/cache 차이일 수 있음.
- **중요:** 원인 확인 전 `Thermionic`, `IncompleteIonization`, Plot 항목을 임의 삭제/변경하지 않음.
- **다음:** 실제 원본 `sd_fdiv_des.cmd`에서 `@NtSide@`, `Thermionic`, `IncompleteIonization`, `Dopants`, preprocessor conditional(`#if` 등) 존재 여부 확인. Node 6/12 Job Log의 source path와 preprocessing 시각도 대조.


## 2026-09-26 — Node 6 vs Node 12 exact Physics/Plot diff identified

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED + PROPOSED FIX
- **근거:** 사용자가 성공 Node 6 및 실패 Node 12의 preprocessed Physics/Trap/Plot block을 직접 제공.
- **공통:** Temperature/Fermi/Piezoelectric/DefaultParameters/Recombination/Mobility/Aniso 및 trap Et=Ev+0.75 eV, e/h Xsection=1e-15는 동일.
- **의도된 차이:** trap `Conc=0` (Node 6) vs `Conc=1e18` (Node 12).
- **추가 비의도 차이:** Node 12에만 `Thermionic`; Node 12는 `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`, Node 6는 plain `IncompleteIonization`; Node 12 Plot에 `eQuasiFermiEnergy`, `hQuasiFermiEnergy`, `pMagnesiumActiveConcentration`, `pMagnesiumMinusConcentration` 추가.
- **판단:** 현재 Node 6/12는 NtSide만 다른 true split이 아님. 따라서 Node 12 실패를 NtSide=1e18 trap 자체의 실패로 결론낼 수 없음.
- **제안:** 원본 SDevice source를 Node 6 physics/plot과 동일하게 복구하고 trap Conc parameter만 1e18로 유지하여 Node 12를 다시 실행. `pp12_des.cmd`는 생성물이라 직접 수정하지 않음.
- **주의:** `Thermionic` 자체가 물리적으로 잘못이라는 판단은 아님. 사용하려면 0/1e18 두 branch에 동일하게 적용해 별도 baseline 재검증.


## 2026-09-26 — Failed Node 12 preprocessed Physics/Plot block captured

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **자료:** 사용자 제공 Node 12 preprocessed SDevice Physics/Plot block.
- **Node 12 global Physics:** `Thermionic` 활성, `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")` 사용.
- **Trap:** DmgL/R의 pGaN, EBL, Barrier0~4, QW1~4, nGaN 전체에 Acceptor trap `Conc=1e18`, `FromValBand EnergyMid=0.75`, `e/h Xsection=1e-15`.
- **Plot:** 기존 baseline 기록보다 확장된 trap/SRH/Mg 관련 output 항목(`eSRHRecombination`, `hSRHRecombination`, `tSRHRecombination`, `TotalTrapConcentration`, trapped charge/gap-state fields, Mg fields 등)이 포함됨.
- **중요 관찰:** GitHub에 동기화된 기존 baseline deck은 plain `IncompleteIonization`이며 `Thermionic`이 없고 Plot 항목도 더 단순함. 따라서 Node 12가 단순히 NtSide만 바뀐 deck인지 아직 보장되지 않음.
- **다음:** 성공 Node 6의 대응 `pp6_des.cmd` Physics/Trap/Plot block을 받아 exact diff. 원인 확정/수정은 diff 이후.


## 2026-09-26 — NtSide=0 성공 run 최종 확인 및 Node 12 차이점 강화

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** CONFIRMED (NtSide=0 completion) / UNRESOLVED (NtSide=1e18 failure)
- **근거:** 성공 Node 6 `n6_des.log` 마지막 화면.
- **NtSide=0 성공:** anode 5.000 V까지 도달, curve trace finished, `n6_des.tdr` 저장 완료, `Sentaurus Device simulation finished`, `Good Bye !` 확인.
- **wallclock:** 약 235312.35 s ≈ 65.4 h ≈ 2.7 days.
- **비교:** 성공 Node 6 log에는 `mMagnesiumActiveConcentration` 검색 결과가 없다고 사용자 확인. 실패 Node 12는 해당 InGaN incomplete-ionization 메시지 반복 직후 종료.
- **해석:** 해당 메시지는 강한 차이점/원인 후보가 되었으나, split deck이 NtSide 외에 달라졌을 가능성을 먼저 배제해야 함.
- **다음:** `pp6_des.cmd` vs `pp12_des.cmd`, 그리고 `pp6_des.par` vs `pp12_des.par` 비교. 의도된 차이가 trap Conc 0 ↔ 1e18뿐인지 확인.


## 2026-09-26 — GitHub 자동 미러 동기화 구축

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Collaboration infrastructure / GitHub sync
- **상태:** CONFIRMED
- **연결 계정:** `soybeanmilk0514-jpg`
- **대상 저장소:** `soybeanmilk0514-jpg/TCAD-MicroLED-Sidewall-Carrier-Confinement`
- **원본 source of truth:** `TaekGyu0801/GGYU`의 `CMP/`
- **구현:** `.github/workflows/sync-cmp.yml` 생성. GitHub Actions가 5분 주기로 원본 CMP 전체를 수빈 저장소의 `CMP/`에 `rsync --delete` 방식으로 미러링.
- **LIVE LOG:** 원본 GitHub Issue #7 comments도 `CMP/.ai-sync/LIVE_LOG_ISSUE_7_MIRROR.md`에 자동 미러링.
- **검증:** 첫 workflow run #1이 2026-09-26에 `success`로 완료됨.
- **경계:** GitHub cron 특성상 완전한 실시간 push mirror가 아니라 최대 수분 단위 동기화. CMP 외 원본 GGYU 파일은 미러링하지 않음.

# Ju Subin Timeline

## 2026-09-26 — Node 12 des.log 종료 지점 확인

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **근거:** `n12_des.log` 마지막 구간.
- **관찰:** 로그는 InGaN QW region의 `mMagnesiumActiveConcentration` incomplete-ionization parameter 메시지 반복 직후 license check-in으로 끝남. 정상 solve 시작/완료 로그는 없음.
- **해석:** 해당 메시지가 단순 warning인지 SDevice initialization을 중단시킨 configuration error인지 아직 확정 불가.
- **가장 강한 판별법:** 성공한 `NtSide=0` node의 대응 `*_des.log`에서 같은 메시지가 존재하는지 비교. 성공 node에도 동일하면 원인 가능성 낮음; failed node에만 있으면 핵심 원인 후보.
- **다음:** 성공 node log 비교 후 필요 시 `n12_des.sta` 확인.


## 2026-09-26 — Node 12 Find Error 결과: explicit fatal 없음

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **근거:** Node 12 Job Log의 `Find Error` 결과 마지막 화면.
- **관찰:** Find Error 결과는 vanOverstraetendeMan E0 anisotropy warning, InGaN QW의 Mg incomplete-ionization parameter warning들을 나열한 뒤 `**** End`로 종료.
- **판단:** 현재 error stream / Find Error 결과에는 직접적인 ERROR/FATAL root cause가 나타나지 않음.
- **다음:** Node Output Files의 `n12_des.log`를 열어 실제 SDevice simulation log의 마지막 부분 확인. 이후 필요 시 `n12_des.sta`.
- **주의:** warning만으로 trap physics 또는 incomplete-ionization을 원인으로 확정하지 않음.


## 2026-09-26 — Node 12 Job Log 확인: preprocessing 성공, SDevice exit(1)

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **근거:** Node 12 Job Log 화면.
- **관찰:** preprocessor가 `pp12_des.cmd`, `pp12_des.par`를 정상 생성했고 dependency 분석도 완료.
- **실행:** `sdevice --max_threads 4 pp12_des.cmd`로 SDevice가 실제 시작됨.
- **종료:** 10:45:47 시작 → 10:45:14? 화면상 약 수십 초 내 `sdevice exited abnormally: exit(1)` 기록. (정확 timestamp 표기는 화면 원문 우선)
- **판단:** Workbench preprocessing/dependency 오류가 아니라 SDevice가 command deck 초기화/모델 설정 단계에서 non-zero exit한 것으로 좁혀짐.
- **다음:** Job Log의 `Find Error` 기능 또는 `n12_des.err` 검색으로 최초 explicit error/fatal line 확인.


## 2026-09-26 — Node 12 local.err 확인: wrapper-level abnormal exit

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **근거:** `n12_local.err` 화면.
- **내용:** `Job failed`, `Error: Unknown error: child process exited abnormally`, `gjob exits with status 1` 확인.
- **해석:** Workbench/gjob가 SDevice child process의 비정상 종료를 감지한 것은 확인되었지만, 이 메시지만으로 원인을 특정할 수 없음.
- **다음:** Node 12 **Job Log** 하단의 command/exit 정보 확인. 필요 시 `n12_des.job` 및 `n12_des.sta` 확인.
- **보호:** 원인 확인 전 Nt/Et/sigma/geometry 변경 금지.


## 2026-09-26 — NtSide=1e18 Node 12 로그 1차 확인

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **상태:** OBSERVED / UNRESOLVED
- **근거:** Node 12 Explorer의 `n12_des.err` 및 `n12_des.out` 화면.
- **관찰:** `n12_des.err`에는 vanOverstraetendeMan E0 anisotropy 관련 warning과 InGaN 영역의 `mMagnesiumActiveConcentration` incomplete-ionization parameter warning이 반복되지만, 화면에 직접적인 fatal/error는 보이지 않음.
- **관찰:** `n12_des.out`은 reference-potential/parameter 초기화 뒤 license check-in으로 끝나며 `Sentaurus Device simulation finished` / `Good Bye !`가 없음.
- **관찰:** Node 12 Output Files 화면에 `.tdr` / `.plt` 결과 파일이 보이지 않음.
- **판단:** 현재 증거는 Newton/Transient 수렴 실패보다 Solve 본격 시작 전 초기화/프로세스 종료 가능성을 우선 시사. 정확 원인은 아직 미확인.
- **다음:** `n12_local.err` → Job Log / `n12_des.job` 순서로 process exit reason 확인.


## 2026-09-26 — Common Baseline split-run 결과 확인: NtSide=0 성공, NtSide=1e18 실패

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Common Baseline / simulation result
- **상태:** OBSERVED
- **근거:** 사용자가 학교에서 Sentaurus Workbench split-run 상태 화면을 직접 확인해 제공.
- **관찰:** `NtSide=0` 조건은 정상 완료되었고, `NtSide=1e18` 조건은 failed 상태로 확인됨.
- **현재 해석 경계:** 실패 원인은 아직 확인되지 않았으므로 convergence / trap-coupling / syntax / resource 문제 중 어느 하나로 단정하지 않음.
- **다음:** 실패한 1e18 run의 실제 SDevice `*.err` 및 `*.out` 마지막 구간을 확인해 최초 fatal/error 또는 convergence failure 지점을 식별한 뒤 최소 수정.


## 2026-09-22 — Project A/B TCAD 구현 계획 구체화

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** CES 발표 / Project A-B 연구설계
- **상태:** PROPOSED
- **배경:** 1차 발표 후 교수진이 Carbon high-resistance 영역과 AlGaN lateral barrier를 실제로 어떻게 형성/코딩하고 무엇을 볼 것인지 질문함.
- **Project A 제안:** baseline 5 nm damage는 유지하고 그 안쪽 upper n-GaN edge에 C-doped/high-resistivity guard region을 추가. C-related deep acceptor/compensation으로 current path를 중앙으로 유도하고 sidewall SRH 감소 여부를 확인.
- **Project B 제안:** baseline damage 안쪽 active-region edge에 localized AlGaN lateral heterobarrier를 추가. Al mole fraction/width를 parameter sweep하고 lateral band offset, carrier confinement, sidewall SRH 감소를 확인.
- **공통 평가:** same-current 비교, integrated sidewall SRH, MQW radiative/Auger, IQE, Vf, current crowding, lateral carrier/current maps.
- **주의:** A/B의 실제 공정 치수/농도/Al composition은 아직 freeze하지 않았으며 DOE 제안 단계.
- **산출물:** `CMP/PROJECT_AB_TCAD_IMPLEMENTATION_PLAN.md`

---

## 2026-09-22 — CES2027 선발 발표 스토리라인 설계 시작

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** 발표 / CES2027 selection
- **상태:** PROPOSED
- **목표:** 다음 주 월요일 15분 CES2027 선발 발표를 위해, 1주차 주제 소개 반복이 아니라 Common Baseline의 문헌 근거 → 구조적 검증 → Project A/B TCAD 구현 전략을 중심으로 발표 구조를 재설계.
- **핵심 메시지:** JBD application scale, Kou 2019 vertical epitaxy, Wu 2023 localized sidewall damage, Chen 2024 small-size sidewall evidence를 역할별로 분리해 baseline의 출처를 설명하고, 동일 baseline 위에서 A/B를 공정 비교하는 연구 설계를 강조.
- **주의:** 아직 완료되지 않은 장시간 SDevice 결과는 확정 결과처럼 발표하지 않으며, 구조적 검증과 전기/광학 validation 진행 상태를 구분.
- **산출물:** `CMP/CES2027_PRESENTATION_PLAN.md`

---

## 2026-09-21 — Common Baseline 코드 최종 수정 보고 / 장시간 run 전 최종 검토

- **작성자:** ChatGPT (공유 프로젝트 대화 동기화)
- **작업자:** 주수빈
- **구분:** Common Baseline 검토 / simulation 준비
- **상태:** OBSERVED — 주수빈 채팅의 사용자 보고 기준
- **작업 내용:** 주수빈이 메인 SDevice 코드를 포함해 앞서 검토된 관련 코드들을 최종 수정했다고 보고함.
- **현재 판단 요청:** Project A와 Project B 모두에 사용할 Common Baseline으로 적합한지, 장시간 simulation을 시작하기 전에 코드와 논리를 마지막으로 꼼꼼히 검토하는 단계.
- **우선 실행 계획:** 전체 Nt sweep을 바로 돌리지 않고 먼저 `NtSide=0`과 `NtSide=1e18` 두 조건을 실행해 baseline 동작을 확인할 계획.
- **비용/제약:** 주수빈 보고 기준으로 한 조건의 simulation이 약 3일 소요될 수 있어, run 전 검증을 우선함.
- **주의:** 이 동기화 시점에는 주수빈 측 최신 전체 코드 원문과 실제 simulation 결과를 GitHub에서 직접 검증하지 못했으므로 코드 정확성/실행 성공은 CONFIRMED로 기록하지 않음.
- **다음:** 주수빈 측 최신 전체 코드 동기화 → baseline 최종 정적 검토 → `NtSide=0`, `NtSide=1e18` 실행 → 결과/로그 GitHub 기록.

---

## 2026-09-22 — NtSide split 실행 중 SWB 실행 순서 점검

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Common Baseline / Workbench dependency diagnostic
- **상태:** OBSERVED + UNRESOLVED
- **관찰:** 사용자가 Sentaurus Workbench 화면에서 NtSide=0, 1e18 두 split을 준비/실행하는 과정에서 SDE보다 SDevice가 먼저 동작하는 것처럼 보인다고 보고함.
- **해석:** NtSide가 SDevice에서만 사용되고 SDE geometry/mesh가 이미 유효한 upstream 결과라면 SWB가 SDE를 재실행하지 않고 같은 SDE 결과를 재사용해 SDevice split부터 실행하는 것은 정상일 수 있음.
- **주의:** 반대로 해당 experiment에서 SDE가 한 번도 성공적으로 실행되지 않았는데 SDevice가 시작된다면 SDE→SDevice dependency 또는 SDevice File/Grid 입력 연결을 확인해야 함.
- **다음 확인:** SDevice preprocessed `pp*_des.cmd`의 `File { Grid=... }`가 실제 SDE 생성 TDR을 가리키는지, 그리고 SDE output에 해당 mesh TDR이 존재하는지 확인.

---

## 2026-09-22 — SDE→SDevice dependency 정상 확인

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Workbench dependency diagnostic
- **상태:** CONFIRMED
- **근거:** Node 6 Explorer의 preprocessed `pp6_des.cmd`에서 `File { Grid = "n1_msh.tdr" }` 확인. 동일 Node 6 output 목록에 `n6_des.tdr`, `n6_des.plt`, `n6_des.log` 존재.
- **판단:** 현재 SDevice Node 6는 SDE에서 생성된 Node 1 mesh `n1_msh.tdr`을 정상 입력으로 사용 중이며, SDevice 자체 TDR도 정상 생성하고 있음.
- **결론:** NtSide split 실행에서 SDE가 다시 돌지 않고 SDevice부터 실행되는 현상은 기존 SDE mesh를 재사용하는 정상 동작으로 판단됨. NtSide가 SDE geometry를 바꾸지 않는 한 SDE 재실행은 필수 아님.

---


## 2026-09-22 — NtSide run 장시간 실행 상태 점검

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** SDevice runtime / convergence diagnostic
- **상태:** OBSERVED
- **관찰:** 사용자가 전날 밤부터 실행해 18시간 이상 지난 Node 6 SDevice output을 공유함. 화면상 계산은 정지하지 않았고 BE step을 계속 진행 중임.
- **근거:** `n6_des.out`에 직전 step이 `|Rhs| < 1.0000E-03`로 수렴 완료된 뒤, 다음 BE step이 약 `0.0766738 → 0.0776738`, `Stepsize = 1.0000E-03`로 진행 중. 직전 step 누적 wallclock은 Assembly 약 598.77 s, Solve 약 2928.83 s, Total 약 3563.68 s로 약 59분/step 수준.
- **판단:** 현재 화면만 보면 hang/fatal error라기보다 각 BE step 계산비용이 매우 큰 장시간 run 상태. 18시간 미완료 자체는 현재 step cost와 양립함.
- **추가 관찰:** `.err`의 vanOverstraetendeMan E0 isotropic/anisotropic 값 차이 메시지는 경고로 보이며, 현재 화면에서 run 중단 원인으로 관찰되지는 않음.
- **다음:** `pp6_des.cmd`의 Solve 블록에서 현재 transient/BE 구간의 최종 목표 시간(또는 ramp 목표), InitialStep/MinStep/MaxStep/Increment 설정을 확인해 예상 총 step 수와 총 wallclock을 산정. 코드 변경 전 최신 전체 deck 동기화 필요.

---

## 2026-09-22 — 장시간 run 원인 확인: Transient MaxStep=1e-3

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** SDevice runtime / step-control diagnosis
- **상태:** CONFIRMED (현재 preprocessed deck 및 log 기준)
- **근거:** `pp6_des.cmd`의 Transient block에서 `InitialStep=1e-5`, `MinStep=1e-9`, `MaxStep=1e-3`, `Increment=1.2`, `Goal { Name="anode" Voltage=5.0 }` 확인.
- **교차확인:** 실행 로그의 pseudo-time 약 0.0766738에서 anode voltage가 약 0.3834 V이며, `5.0 × 0.0766738 ≈ 0.38337 V`로 일치. 따라서 현재 transient coordinate가 0→1 동안 anode 0→5 V ramp에 대응함을 강하게 확인.
- **의미:** `MaxStep=1e-3`이면 최대 전압 증가량은 약 5 mV/accepted step. 현재 약 0.077 지점에서 5 V 목표까지 최소 약 923~924 accepted steps가 더 필요함.
- **runtime 추정:** 최근 관찰된 약 3563.68 s/step을 단순 적용하면 남은 시간이 약 38일 규모. 실제 step cost는 bias에 따라 달라질 수 있으므로 이는 거친 추정이지만 현재 설정이 매우 장시간인 원인은 분명함.
- **다음:** `pp6_des.cmd`가 아닌 원본 SDevice deck에서 numerical step strategy를 검토. Common Baseline physics(Nt/Et/sigma/5 nm damage 등)는 변경하지 않으며, A/B 및 Nt 비교에 동일한 numerical protocol을 적용해야 함.

---

## 2026-09-22 — runtime 원인 판단 정정/정밀화

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Runtime diagnosis refinement
- **상태:** OBSERVED / UNRESOLVED
- **사용자 추가 정보:** 최종 수정 전 거의 같은 코드가 약 3일 내 완료된 이력이 있다고 보고함.
- **정정:** 따라서 현재 `MaxStep=1e-3` 자체만으로 이번 느려짐의 '새 원인'이라고 단정할 수 없음. 이전 run에도 동일하거나 유사한 step 설정이 있었다면, 3일→현재 18시간에 pseudo-time ~0.077의 차이는 **accepted step 하나당 계산비용 증가 또는 rejected/cutback 증가**를 우선 의심해야 함.
- **현재 강한 단서:** 최근 한 step의 solve time이 약 2929 s, total 약 3564 s로 매우 큼. 이는 단순 step 개수보다 선형/비선형 solve cost, mesh unknown 수, conditioning, traps/physics coupling, 또는 반복적인 cutback 여부를 비교해야 함을 의미.
- **38일 추정의 지위:** 최근 한 개의 느린 step을 전체에 선형 외삽한 거친 상한성 추정으로만 유지하며, 실제 총 runtime 예측으로 사용하지 않음.
- **다음 비교 우선순위:** (1) 이전 3일 run의 Transient 설정, (2) mesh node/element 수, (3) Physics/Traps/region 적용 차이, (4) Math solver 설정, (5) log의 failed/repeated step 및 step cutback 빈도.

---

## 2026-09-22 — 과거 3일 run 초기 solve 시간 증거 확보

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** old-vs-current runtime comparison
- **상태:** OBSERVED
- **근거:** 사용자가 과거 약 3일 내 완료된 run의 초기 `.out` 로그 화면을 공유함.
- **관찰값:** 초기 0 V coupled solve에서 Assembly 약 350.52 s, Solve 약 232.46 s, Total 약 585.81 s. Newton iteration은 화면상 50회까지 진행 후 `|RHS| < 1.0000E-03`로 수렴.
- **주의:** 이 로그는 anode=0 V 초기 구간이므로 현재 run의 약 0.38 V step(Total ~3563.68 s)과 직접 1:1 비교할 수는 없음.
- **다음:** 과거 run에서 anode 0.3~0.4 V 구간의 step 로그를 찾아 동일 bias에서 Total time / Newton iteration / retry-cutback 여부를 비교.

---

## 2026-09-22 — 과거 3일 run 0.30 V 부근 step 비용 확인

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** old-vs-current runtime comparison
- **상태:** OBSERVED
- **근거:** 과거 약 3일 내 완료된 run의 `.out`에서 anode 약 0.3034 V 및 0.3084 V 구간 로그를 확인.
- **관찰값:**
  - 약 0.3034 V step: Assembly 35.80 s, Solve 136.34 s, Total 172.57 s
  - 약 0.3084 V step: Assembly 42.71 s, Solve 78.79 s, Total 123.94 s
  - 두 step 모두 5회 Newton iteration(0~4) 후 `|RHS| < 1e-3`로 수렴
- **비교:** 현재 run의 약 0.3834 V 부근에서 Total 약 3563.68 s/step이 관찰되어, 과거 0.30 V 부근보다 한 step 계산비용이 이미 매우 크게 증가해 있음.
- **주의:** bias가 정확히 동일하지 않으므로 최종 정량 비교는 과거 run의 0.38 V 부근 로그를 추가 확인해야 함.
- **다음:** 과거 run에서 anode 약 0.38 V(대략 0.375~0.390 V) 구간의 Total time / Newton iteration / retry 여부 확인.

---

## 2026-09-22 — old/current 동일 bias 0.3834 V step 직접 비교

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Runtime root-cause comparison
- **상태:** CONFIRMED (공유된 old/current 로그 화면 기준)
- **old run (~3일 완료):** pseudo-time 0.0756738→0.0766738, accepted anode ≈0.3834 V, Assembly 64.84 s, Solve 108.74 s, Total 177.47 s.
- **current run:** 동일 accepted anode ≈0.3834 V에서 Assembly 598.77 s, Solve 2928.83 s, Total 3563.68 s.
- **비교:** 동일 bias에서 현재 accepted step의 wallclock이 old 대비 약 20.1배 증가. 따라서 이번 slowdown의 주원인은 MaxStep/step count 자체가 아니라 **step 하나를 푸는 계산비용 증가**로 확정적으로 좁혀짐.
- **다음 원인 후보:** mesh unknown 수 증가, Physics/Trap 적용 범위 변화, Math/linear solver 설정 변화, 또는 비선형/선형 반복 비용 증가. old/current startup statistics와 preprocessed deck diff가 우선.

---

## 2026-09-22 — 중요 정정: 0.30~0.38 V의 123~177 s 로그도 현재 run 내부 초기 구간

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Runtime diagnosis correction
- **상태:** CONFIRMED (스크린샷 경로/라인 기준)
- **정정:** 앞선 답변에서 0.303~0.383 V, Total 123~177 s 로그를 '과거 3일 run'으로 잘못 해석했음. 새 스크린샷 상단 경로가 현재와 동일한 `.../n6_des.out`이고 사용자가 '돌아간 것 중 초창기 부분'이라고 설명했으므로, 해당 로그는 **현재 Node 6 run의 초기 구간**임.
- **현재 run 초기 구간 실제 값:** pseudo-time 0.0746738→0.0756738에서 Total 166.16 s, 이어 0.0756738→0.0766738에서 Total 177.47 s, accepted anode ≈0.3834 V.
- **중요 모순/단서:** 같은 현재 run의 나중 화면에서는 accepted anode ≈0.3834 V 직후 Total 3563.68 s가 관찰됨. 따라서 단순 old-vs-new 비교가 아니라 **현재 한 run 안에서 동일 pseudo-time/voltage ramp가 다시 등장하거나 다른 solve stage가 존재하는지** 확인해야 함.
- **다음:** `pp6_des.cmd`에서 `Transient(` 등장 횟수를 검색하고, `n6_des.out`에서 `0.0766738` 또는 `3563.68`을 검색해 느린 구간이 어느 Solve/Transient stage에 속하는지 식별.

---

## 2026-09-22 — 재정정: 0.3834 V / 177.47 s 로그는 과거 3일 완료 run

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Runtime evidence correction
- **상태:** CONFIRMED (사용자 직접 확인)
- **사용자 확인:** 직전 스크린샷의 `n6_des.out`은 현재 실행 중인 노드가 아니라 **예전에 약 3일 만에 완료된 노드의 파일**임.
- **따라서 유효 비교:** old run anode ≈0.3834 V에서 Total 177.47 s (Assembly 64.84 s, Solve 108.74 s), current run 같은 anode ≈0.3834 V에서 Total 3563.68 s (Assembly 598.77 s, Solve 2928.83 s).
- **비율:** current accepted-step wallclock은 old 대비 약 20.1× 증가.
- **결론:** slowdown은 step count 자체보다 per-step computational cost 증가가 핵심이라는 이전 판단을 복구.
- **주의:** 파일명 `n6_des.out`은 서로 다른 프로젝트/노드 복사본에서도 반복될 수 있으므로, 앞으로는 파일명만으로 old/current를 구분하지 않고 사용자의 노드 식별과 경로 맥락을 함께 사용.

---

## 2026-09-22 — 과거 약 3일 완료 node의 full preprocessed SDevice deck 확보

- **작성자:** ChatGPT
- **작업자:** 주수빈
- **구분:** Old-vs-current runtime baseline capture
- **상태:** OBSERVED
- **자료:** 사용자가 과거 약 3일 만에 완료된 node의 `pp6_des.cmd` 전체 내용을 제공.
- **old deck 주요 설정:**
  - Grid=`n1_msh.tdr`
  - global Physics: Fermi, Piezoelectric_Polarization(strain), SRH/Auger/Radiative, Masetti + CaugheyThomas + Lombardi, IncompleteIonization, Aniso(Poisson)
  - DmgL/R의 pGaN, EBL, Barrier0~4, QW1~4, nGaN에 Acceptor trap 정의
  - **모든 trap Conc = 0**
  - trap: FromValBand, EnergyMid=0.75, e/h Xsection=1e-15
  - Math: NumberOfThreads=4, Digits=5, ErrRef(e/h)=1e4, RHSMin=1e-3, Transient=BE, ExtendedPrecision(80), TensorGridAniso(aniso), Method=Blocked, SubMethod=ILS(set=22)
  - ILS(22): gmres(100), tolrel=1e-10, tolunprec=1e-4, maxit=200, ilut(1e-8,-1)
  - Solve: Poisson-only Coupled Iterations=500 LineSearchDamping=1e-2; full Coupled Iterations=100
  - Transient: InitialStep=1e-5, MinStep=1e-9, MaxStep=1e-3, Increment=1.2, Goal anode=5.0 V
- **중요:** 현재 slow run의 Transient step-control은 이전에 확인한 값과 동일하므로 step-control 변경만으로 slowdown을 설명할 수 없음.
- **가장 먼저 검증할 것:** 현재 slow Node 6의 trap `Conc`가 0인지 1e18인지 확인. old deck은 명백히 NtSide=0 케이스이므로 current가 1e18이면 직접 runtime 비교가 공정하지 않음.
- **그 다음:** current full `pp6_des.cmd`의 Physics/Math와 old deck을 diff하고, old/current mesh statistics 비교.

---
