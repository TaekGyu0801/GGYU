## 2026-10-04 — Runtime planning implication for Project A/B

- 작업자: 이택규
- 연구 판단: FAST common baseline optimization은 단순 baseline 편의가 아니라 이후 Project A/B parameter study의 총 계산시간을 줄이기 위한 필수 단계.
- Project A의 localized GaN:C high-resistance 영역은 carrier transport를 더 강하게 제한하고 수치 stiffness/cutback을 증가시킬 수 있어 baseline보다 느려질 가능성이 있음. 단, 실제 slowdown magnitude는 아직 미측정이며 추측하지 않음.
- 따라서 production A/B sweep 전에 representative single-case pilot를 먼저 실행해 runtime/convergence를 측정하고, 그 결과로 parameter grid/parallelization 계획을 확정해야 함.
- baseline C1 검증 후 동일 numerical framework를 A/B에 유지하고, physics shortcut 대신 numerical efficiency + independent parallel runs로 시간을 단축한다.

## 2026-10-04 — FAST C1 baseline acceptance sequence clarified

- 작업자: 이택규
- 연구 판단: FAST_C1은 단순히 Node 6/12가 완주했다는 이유만으로 baseline으로 확정하지 않는다.
- 최종 공통 baseline은 두 조건을 포함한다:
  - NtSide=0: defect-free control
  - NtSide=1e18: nominal sidewall-defect baseline
- acceptance sequence:
  1. FAST_C1 preprocess equivalence gate PASS.
  2. NtSide=0 B1 run: golden x8 overlap에서 accepted/rejected trajectory, Iterations=15 적용, I-V/Vf/출력 등가성 검증.
  3. NtSide=1e18 run: 동일한 C1 source/mesh/physics 유지, trap concentration만 1e18로 변경되었는지 확인하고 완주/물리 sanity 검증.
  4. 두 조건이 모두 통과하면 FAST_C1을 Project A/B 공통 baseline numerical implementation으로 freeze.
- Project A/B는 이후 이 frozen common baseline 위에서 각각 GaN:C high-resistance 영역과 AlGaN barrier를 추가한다.

## 2026-10-04 — FAST_C1 Node 6 solve accidentally launched before preprocess gate

- 작업자: 이택규
- 상태: OBSERVED / BLOCKER
- process check shows FAST_C1 Node 6 was actually launched, not preprocess-only:
  - gsub PID 69166: `-e 6 .../GaN_PiN_Diode_FAST_C1`
  - gjob PID 69396
  - sdevice PID 69457: `sdevice --max_threads 4 pp6_des.cmd`
  - start time 15:46, active at ~99% CPU.
- therefore the ~3 h delay is real SDevice solve runtime, not preprocess delay.
- since SDevice is running from `pp6_des.cmd`, preprocessing has already produced the generated deck.
- this run began before the mandatory preprocess equivalence gate, so it must not be accepted as B1 evidence unless the generated deck is validated.
- immediate action: stop only the FAST_C1 Node 6 job via Workbench (do not kill unrelated jobs), then audit `pp6_des.cmd/par` before any restart.
- the current process list showed no other user-owned x8 gsub/sdevice process; user had reported stopping other runs.

## 2026-10-04 — User reports other runs stopped for FAST_C1 work

- 작업자: 이택규
- 상태: USER-REPORTED / VERIFY NEEDED
- 사용자가 FAST_C1 작업을 위해 "나머지 다 멈춰놨어"라고 보고함.
- 어떤 기존 run들이 실제로 중지되었는지는 아직 프로세스 확인 전이므로 확정하지 않음.
- FAST_C1의 현재 단계는 solve가 아니라 Node 6 (NtSide=0) preprocess-only gate임.
- preprocess 자체는 계산 solve가 아니므로 기존 장시간 run을 멈출 필요가 없음.
- 다음: FAST_C1 Node 6 preprocess-only 수행, 필요 시 기존 run 프로세스 상태 재확인.

## 2026-10-04 — FAST_C1 copied .status ownership resolved

- 작업자: 이택규
- 상태: OBSERVED / RESOLVED
- FAST_C1 `.status`에 남아 있던 PID 78941을 `/proc/78941/cwd`와 cmdline으로 확인함.
- PID 78941의 실제 cwd와 gsub 대상은 원래 live Copy x8:
  `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_Copy_Copy_Copy_Copy_Copy_Copy_Copy_Copy`
- 따라서 FAST_C1의 `.status`는 Save As 과정에서 복사된 stale metadata이고, live process ownership은 x8에 있음.
- PID 78941은 절대 종료/수정하지 않음.
- FAST_C1 source는 exact C1 SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`.
- 다음: Workbench에서 FAST_C1 프로젝트만 열고 Node 6(NtSide=0)을 preprocess-only. SDevice solve는 시작하지 않음.

## 2026-10-04 — FAST_C1 copied .status points to live gsub PID

- 작업자: 이택규
- 상태: OBSERVED / CAUTION
- FAST_C1 `.status` contains PID 78941 on host ssudisu3.
- `ps -fp 78941` confirms PID 78941 is an active Synopsys `gsub0` process started Sep 28.
- do NOT kill or modify this process; it may belong to the live Copy x8 run.
- next: read-only inspect `/proc/78941/cwd` and cmdline to identify which project owns the process before touching FAST_C1 status metadata.

## 2026-10-04 — FAST_C1 node mapping confirmed

- 작업자: 이택규
- 상태: OBSERVED
- FAST_C1 `gtree.dat` confirms SDevice split:
  - Node 6: `NtSide=0`
  - Node 12: `NtSide=1e18`
- source remains exact C1 SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`.
- `.status` currently contains host `ssudisu3` and PID `78941`; its meaning/liveness must be checked before preprocess.
- next: read-only `ps -fp 78941`; then preprocess Node 6 only if safe.

## 2026-10-04 — FAST_C1 exact source installation PASS

- 작업자: 이택규
- 상태: OBSERVED / SOURCE-INSTALL PASS
- separate project: `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1`
- exact patch applied successfully to `sd_fdiv_des.cmd`.
- resulting SHA-256:
  `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`
- this matches the canonical Claude C1 source hash exactly.
- golden backup remains `sd_fdiv_des.cmd.golden_x8`.
- live x6/x7/x8 untouched.
- next: inspect copied Workbench node/status metadata before preprocess; do not launch SDevice yet.

## 2026-10-04 — FAST_C1 Workbench copy contents confirmed

- 작업자: 이택규
- 상태: OBSERVED
- `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1` contains the copied Copy x8 Workbench project contents (~145 MB).
- Key copied inputs are present: `sd_fdiv_des.cmd`, `n1_msh.tdr`, `pp1_dvs.cmd`, `pp6_des.cmd`, `pp6_des.par`.
- Legacy/stale execution outputs were also copied (`n6_des.out/log/plt/tdr`, intermediate TDRs, old n12 artifacts); these are not FAST C1 results and must not be interpreted as such.
- no C1 source edit or preprocess has been performed yet.
- next: read-only SHA-256 check of copied golden inputs before any cleanup/edit.

## 2026-10-04 — Separate FAST C1 directory created

- 작업자: 이택규
- 상태: OBSERVED
- separate directory exists:
  `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_FAST_C1`
- live Copy x8 remains untouched.
- directory existence alone does not yet prove the Workbench project contents were fully copied.
- next: read-only listing of the FAST_C1 directory before any cleanup/source replacement/preprocess.

## 2026-10-04 — B0 cutback-rule validation CLOSED

- 작업자: 이택규
- 상태: OBSERVED / B0 COMPLETE
- regenerated x8 CSV with the updated audit tool using explicit `Stepsize`.
- all 285 rejection/retry pairs were checked.
- `retry_dt / rejected_dt`:
  - pairs = 285
  - min = 0.499975805
  - max = 0.500023337
  - mean = 0.499999621
- interpretation: the retry timestep is effectively exactly 0.5 of the rejected timestep; remaining spread is consistent with printed Stepsize precision.
- this closes the B0 assumption that the transient cutback factor is independent of whether the rejected Newton attempt ran to 50 or is capped at 15.
- therefore C1 should preserve the x8 rejection points/accepted-step trajectory over the observed overlap; only the rejected-attempt Newton count changes 50 -> 15.
- C1 source remains unchanged: SHA-256 `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`, `Iterations=15`.
- next: separate FAST C1 Workbench project/copy -> source hash -> preprocess gate.
- live x6/x7/x8 untouched.

## 2026-10-04 — Old B0 CSV cutback-ratio spread identified as dt-rounding artifact

- 작업자: 이택규
- 상태: OBSERVED
- full old-CSV check over 285 rejection/retry pairs: min=0.47826087, max=0.52173913, mean=0.499405569.
- old CSV used dt=t1-t0 from rounded printed endpoints, so high-bias small timesteps are distorted.
- this spread is not accepted as evidence of a variable cutback factor.
- updated Claude audit tool reads explicit Stepsize from the log; regenerate CSV before judging cutback-ratio constancy.
- existing raw log examples using Stepsize are approximately 0.5.
## 2026-10-04 — Full CSV cutback-ratio check exposed old-dt rounding artifact

- 작업자: 이택규
- 상태: OBSERVED / TOOLING INTERPRETATION
- old B0 CSV ratio check across all 285 rejection/retry pairs returned:
  - pairs = 285
  - min = 0.47826087
  - max = 0.52173913
  - mean = 0.499405569
- This CSV was produced by the older audit parser whose `dt` was computed from printed `t1-t0`.
- T-2022.03 prints t0/t1 with limited decimal precision, so small high-bias timesteps are distorted when subtracting the rounded endpoints.
- Therefore the 0.478–0.522 spread is **not valid evidence that the cutback factor varies**.
- Claude's updated audit tool specifically fixes this by reading the explicit `(Stepsize: ... s)` value from each log line.
- Existing raw examples using printed Stepsize show exact/near-exact 0.5 cutback.
- Next: regenerate x8_attempts.csv with the updated audit tool and repeat the 285-pair ratio check using the explicit Stepsize-derived dt.

## 2026-10-04 — B0 CSV ratio check command quoting error under csh/tcsh

- 작업자: 이택규
- 상태: OBSERVED / RESOLVED COMMAND SYNTAX
- multiline `python3 -c '...'` command was pasted into csh/tcsh and split across prompts, causing `Unmatched '`, `Badly placed ()'s`, and globbing errors.
- no file/simulation change occurred.
- correction: use a single-line awk command for the CSV retry-dt/rejected-dt ratio check.

## 2026-10-04 — Claude B0 review package integrated

- 작업자: 이택규
- 상태: PROPOSED / REVIEWED / READY FOR PREPROCESS
- reviewed `C1_B0_review_for_GPT.zip`.
- C1 source unchanged; `Iterations=15` retained; SHA `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`.
- corrected interpretation:
  - ~4.33 V = first rejected attempt where Newton count changes 50->15, not trajectory divergence.
  - expected observed-overlap trajectory is same accepted steps + same rejection points.
- A1'/A1'' added; printed-precision identity expectation tightens A3/A4 on observed overlap.
- updated audit tool package SHA `9a935633e92bc55fa86849b6988b60a8a8ee55f637387ced62721d9f6267d281`; ChatGPT reran `--selftest` successfully.
- patch base `30f9d947...` matched current main and patch-equivalent content was committed as `ace056fcb01d2e6e785dbee08a213e1148d6be35`.
- x8 raw excerpt supports ~0.5 timestep cutback on several observed rejection/retry pairs; full CSV-wide ratio verification remains pending because the CSV was not attached to the review package.
- next: separate FAST C1 project preprocess gate, then NtSide=0 B1.
- live x6/x7/x8 untouched.

## 2026-10-04 — B0 raw x8 audit PASS for C1 Iterations=15

- 작업자: 이택규
- 상태: OBSERVED / B0 PASS TO CURRENT X8 PROGRESS
- source log: `~/CMP_B0/x8_n6_des_20261004_1335.out`
- parsed attempts: 2236
  - accepted: 1950
  - rejected: 285
  - unknown: 0
- accepted-step Newton iterations:
  - 2 iter: 1019
  - 3 iter: 778
  - 4 iter: 153
  - **accepted max = 4**
- rejected attempts: **285/285 reached 50 iterations**
- parser/raw excerpt directly confirms a rejected attempt finishing with `#iterations larger than 50.`
- `Iterations=15` predicted false rejections over the observed x8 trajectory: **0**
- first trajectory divergence under a 15-cap is predicted near anode **4.33 V**
- observed attempt wallclock sum:
  - total ≈ 495106 s = 137.5 h
  - accepted ≈ 123464 s
  - rejected ≈ 371643 s (~75.1% of attempt wallclock)
- simple uniform-per-iteration estimate for N=15: saved rejected-attempt time ≈ 260150 s (~72.3 h), corresponding to an idealized ~2.11x speedup over the observed trajectory if no additional recovery cost is introduced.
- important limitation: x8 log copy only reaches ~4.643 V; B0 does not prove behavior from 4.643→5.0 V.
- tool caveats:
  - real log `error` column is not yet parsed, so `err<1?` output is not used.
  - cutback recovery median/max from the current script is not used for acceptance because the metric is misleading under repeated ramp failures.
- decision: C1 `Iterations=15` is approved as the first PROPOSED numerical candidate for separate-project preprocess + NtSide=0 benchmark. It is not yet a CONFIRMED FAST baseline.

## 2026-10-04 — Corrected B0 parser selftest passed

- 작업자: 이택규
- 상태: OBSERVED / TOOL SELFTEST PASS
- commit-pinned parser `a0ff43f2aff4b76ed390dcd6831e3ebeba6cb366` downloaded successfully.
- `python3 ~/CMP_B0/sdevice_newton_audit.py --selftest` returned `selftest OK`.
- This version contains the regression probe for the observed x8 T-2022.03 BE-step syntax.
- next: rerun the real x8 copied-log audit and inspect accepted/rejected iteration distribution.
- C1 `Iterations=15` remains unconfirmed until the real-log audit passes.

## 2026-10-04 — Root cause of failed BE-step parser patch: regex escaping error

- 작업자: 이택규
- 상태: FIXED / B0 PENDING
- commit `c9e5804...` still failed its real-line regression selftest.
- direct source inspection found the regex contained raw-string tokens like `\\\\s` instead of `\\s`, so it searched for a literal backslash+s rather than whitespace.
- actual fix committed as:
  - `a0ff43f2aff4b76ed390dcd6831e3ebeba6cb366`
- GitHub source was reread after the write and now contains single-backslash regex tokens such as `Computing\\s+BE-step`.
- next: download commit-pinned script, run selftest, then rerun B0.
- no TCAD simulation/source deck modified.

## 2026-10-04 — Correction: previous BE-step parser patch had not changed RE_STEP; fixed at commit c9e5804

- 작업자: 이택규
- 상태: FIXED / PROPOSED TOOL
- user reran the supposed patched parser and still got attempts=0.
- direct GitHub inspection showed `RE_STEP` was still the old `Computing step from t=...` regex.
- prior statement that the BE-step parser patch was applied was incorrect.
- actual fix now committed:
  - commit `c9e5804ba0d84e424fcde6f4fd83bb4a04cd686a`
  - recognizes observed `Computing BE-step from <t0> s to <t1> s (Stepsize: <dt> s)` syntax
  - adds a regression selftest using the exact observed x8 line.
- next: download the commit-pinned script, rerun selftest and B0 audit.
- no simulation/source deck was modified.

## 2026-10-04 — Real T-2022.03 BE-step syntax identified; B0 parser patched

- 작업자: 이택규
- 상태: OBSERVED / TOOL FIXED
- real x8 log uses:
  - `Computing BE-step from <t0> s to <t1> s (Stepsize: <dt> s)`
  - `Iteration |Rhs| factor |step| error #inner #iterative time`
  - rejected attempt message: `Newton didn't converge, trying again with smaller timestep...`
  - accepted attempt message: `|RHS| less than 1.0000E-03.`
- repeated retry at the same t0 with a smaller dt is directly visible, validating the high-level accepted/rejected classification rule.
- `CMP/tcad/tools/sdevice_newton_audit.py` patched to recognize the actual T-2022.03 BE-step start format while preserving the previous synthetic format.
- B0 statistics must be rerun with the updated parser before any Iterations=15 decision.

## 2026-10-04 — B0 parser mismatch on real x8 SDevice log

- 작업자: 이택규
- 상태: OBSERVED / UNRESOLVED TOOLING
- `sdevice_newton_audit.py --selftest` passed on synthetic data.
- Real Copy x8 log audit returned:
  - attempts=0
  - no wallclock found
  - `NO "Computing step from t=... to t=..." lines found`
- Interpretation: actual T-2022.03 `n6_des.out` format does not match the parser's assumed step-start regex.
- B0 scientific conclusion is therefore still pending; no claim about accepted/rejected iteration distribution or Iterations=15 is valid yet.
- Next: inspect raw x8 log wording around "Computing", "Rhs", "step", and transient time, then patch the parser to the actual format and rerun B0.

## 2026-10-04 — B0 local audit setup

- 작업자: 이택규
- 상태: OBSERVED
- x8 n6_des.out copy succeeded to ~/CMP_B0/x8_n6_des_20261004_1335.out.
- LOG variable setup succeeded under csh/tcsh.
- audit did not start because sdevice_newton_audit.py was not yet present in ~/CMP_B0.
- no simulation/source change occurred.
- next: place the audit script in ~/CMP_B0, run selftest, then audit the copied x8 log.

## 2026-10-04 — B0 audit script missing locally

- 작업자: 이택규
- 상태: OBSERVED / RESOLVED PATH ISSUE
- x8 log copy succeeded:
  - `~/CMP_B0/x8_n6_des_20261004_1335.out`
  - size ≈ 3.4M
- csh/tcsh `LOG` variable setup succeeded.
- audit command failed only because `~/CMP_B0/sdevice_newton_audit.py` was not present:
  - `python3: can't open file ... [Errno 2] No such file or directory`
- no simulation/source modification occurred.
- next: download the GitHub tool to `~/CMP_B0/`, run `--selftest`, then execute B0 audit.

## 2026-10-04 — semi437 shell syntax mismatch during B0 log copy

- 작업자: 이택규
- 상태: OBSERVED / RESOLVED
- command `cp n6_des.out ~/CMP_B0/x8_n6_des_$(date +%Y%m%d_%H%M).out` returned `Illegal variable name.`
- interpretation: login shell behaves as csh/tcsh, where bash-style `$(...)` command substitution is invalid.
- correction: use backticks for command substitution, e.g. `x8_n6_des_`date +%Y%m%d_%H%M`.out`.
- no simulation/source files were modified; only the attempted copy command failed.
- next B0 commands should use csh/tcsh-compatible syntax.

## 2026-10-04 — B0-1: Copy x8 preprocessed Iterations check

- 작업자: 이택규
- 상태: OBSERVED
- active Copy x8 `pp6_des.cmd`에서:
  - `RHSMin = 1e-3`
  - `CheckRhsAfterUpdate`
  - `Iterations = 500` (initial Poisson)
  - `Iterations = 100` (equilibrium Coupled)
  - transient inner Coupled에 explicit `Iterations` 없음
  - `NotDamped` 없음
- 따라서 프로젝트 기록의 ~50-row/iteration failure는 preprocessed deck에 명시된 `Iterations=50` 때문이 아님.
- 다음: exact x8 `n6_des.out` raw audit으로 50의 의미를 확인하고 accepted-step iteration 분포를 측정.

## 2026-10-04 — Claude FAST C1 package reviewed by ChatGPT

- 작업자: 이택규
- 상태: PROPOSED / REVIEWED / NOT EXECUTED
- Claude package `FAST_BASELINE_C1_for_GPT.zip` 검토 완료.
- golden source SHA-256 재검증:
  - `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`
- FAST C1 source SHA-256 재검증:
  - `f62eab51816ba21a9fba6f9d26ef39606ea76b17c2a522153d4b45ed8cf27f93`
- golden 대비 executable statement 변경은 transient inner Coupled의 `Iterations=15` 한 group뿐.
- 기존 ChatGPT FAST v0.1(SHA `6ccf386c...`)과 Claude C1은 executable statement 기준 동일. 차이는 comments/formatting뿐이며 앞으로 C1을 canonical candidate로 사용.
- Claude Python tools 3개는 ChatGPT sandbox에서 `py_compile` 통과; Newton audit/PLT compare synthetic selftest 통과. 실제 semi437 SDevice log/PLT에서는 아직 미검증.
- 중요 correction:
  - Synopsys 2022 training은 Quasistationary/Transient Newton `Iterations` default=20, 보통 15–20회 제한을 권장.
  - CMP 기록의 약 50-iteration failure와 충돌하므로 effective x8 cap은 아직 UNRESOLVED.
  - B0에서 exact `pp6_des.cmd` + raw `n6_des.out`을 교차검증한 뒤 15를 확정.
- raw Claude patch의 “x7 먼저 정리” 권고는 최신 운영 결정과 충돌하여 반영하지 않음. live x6/x7/x8은 보존.
- acceptance thresholds는 PROVISIONAL engineering criteria로 기록.
- public record: `CMP/FAST_BASELINE_C1.md`
- sanitized diff: `CMP/tcad/tools/FAST_C1_vs_CopyX8.diff`

## 2026-10-04 — Claude FAST implementation prompt committed

- 작업자: 이택규
- 상태: READY FOR CLAUDE
- Claude가 GitHub만 읽어도 FAST_BASELINE 구현 맥락을 이해할 수 있도록 종합 prompt/handoff를 생성:
  - `CMP/prompts/CLAUDE_FAST_BASELINE_IMPLEMENTATION.md`
- 내용:
  - exact Copy x8 golden source filename/hash
  - generated-input hashes
  - 연구 목적 / Project A-B framing
  - 변경 금지 Common Baseline physics
  - exact current numerical settings
  - 실제 high-bias runtime bottleneck
  - historical provenance traps
  - Claude가 제출해야 할 complete code/diff/Workbench/benchmark 산출물
  - public GitHub에 proprietary source를 올리지 않는 규칙
- FAST Sentaurus 코드 작성은 Claude가 전담.
- 이전 ChatGPT `Iterations=15` 아이디어는 확정 patch가 아니라 PROPOSED 참고 후보로만 취급.
- 사용자는 Claude 채팅에 `Copy_x8_sd_fdiv_des.cmd`를 별도 첨부해야 함.

## 2026-10-04 — FAST_BASELINE v0.1 Iter15 candidate created

- 작업자: 이택규
- 상태: PROPOSED / READY FOR SHORT BENCHMARK
- 업로드된 exact Copy x8 source SHA-256가 golden hash `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`와 일치함을 확인.
- FAST v0.1은 원본 대비 numerical-only 1개 변경:
  - Transient 내부 `Coupled`에 `Iterations = 15` 명시.
- FAST v0.1 SHA-256: `6ccf386cd8959b5953c2c1b241f2c868916bf222814a03f9f774edbc82011040`
- Physics/Traps/Nt/Et/sigma/mesh intent/bias goal/step controls/ILS는 변경하지 않음.
- 목적: high-bias에서 장시간 소모 후 reject되는 Newton step을 더 일찍 cutback하도록 유도.
- 다음: live x8은 보존하고 별도 Workbench copy에서 short benchmark; accepted/rejected iteration, timestep, wallclock, I-V 및 matched-bias 결과 비교.

## 2026-10-04 — FAST workflow sequence corrected to original plan

- 작업자: 이택규
- 상태: DECISION / CORRECTION
- 사용자 지적에 따라 GitHub 기록을 재검토했고, 2026-10-03 원래 계획은 Copy x8 reference 확보 후 별도 FAST_BASELINE 코드를 바로 작성하고 Newton/cutback policy부터 short benchmark하는 순서였음을 확인.
- clean-account reproduction은 FAST 코드 작성 전 blocker가 아니라, 최종 FAST deck freeze 및 Project A/B production 전 필수 검증 gate로 위치를 복원.
- 현재 상태: Copy x8 golden hashes frozen; separate FAST code 작성 준비 완료.
- 남은 직접 blocker: 코딩 AI가 exact Copy x8 editable source 본문을 받아야 함. public CURRENT 파일은 stale이므로 사용 금지.

## 2026-10-04 — Copy x8 golden reference freeze completed

- 작업자: 이택규
- 상태: CONFIRMED
- local snapshot: `~/CMP_REFERENCE_SNAPSHOTS/Copy_x8_20261004_124024`
- exact core files and hashes:
  - `n1_msh.tdr` = `762d2d57a352a00bb030b968985cbf3b71d53118c68e5c53b7586e613f392ea3`
  - `pp1_dvs.cmd` = `5685528bc3ec338ce104040b0503be43ef032094976d69995529eb5d6fb4e658`
  - `pp6_des.cmd` = `2dfcc98effe145ec944fb8ee5d6914f5f098e54d1bf2319c69acc76afe1692e6`
  - `pp6_des.par` = `60405755de61500d9815a8e9ecca6a7a465783d77eb8e5dadf1db515aeb10039`
  - `sd_fdiv_des.cmd` = `56a8be698321e5056e33bf22d4b873063728013e8a2383f4e264a42662c4aa2c`
- 기존 blocker였던 editable SDevice source 누락은 해결됨.
- 이 snapshot/hash set을 clean-account reproduction의 golden reference로 사용.
- 다음: 이택규 clean account 새 Workbench project에서 preprocess/early-init까지만 실행 후 exact diff/hash 비교.

## 2026-10-04 — Copy x8 core files verified

- 작업자: 이택규
- 상태: OBSERVED
- active Copy x8 directory에서 핵심 파일 존재를 사용자 터미널로 확인:
  - `sd_fdiv_des.cmd`
  - `pp1_dvs.cmd`
  - `pp6_des.cmd`
  - `pp6_des.par`
  - `n1_msh.tdr`
- 기존 reference-package blocker였던 exact editable SDevice source 부재는 active x8 directory 기준으로 해소 가능.
- 다음: snapshot helper 실행 → local golden snapshot + SHA-256 manifest 생성.

## 2026-10-04 — Copy x8 exact core files verified in active directory

- 작업자: 이택규
- 상태: OBSERVED
- 사용자 터미널에서 active Copy x8 directory `/user/semi/semi437/tmp/myproject/GaN_PiN_Diode_Copy_Copy_Copy_Copy_Copy_Copy_Copy_Copy` 확인.
- 핵심 파일 존재 확인:
  - `sd_fdiv_des.cmd` 18K, Sep 28 12:17
  - `pp1_dvs.cmd` 18K, Sep 28 10:31
  - `pp6_des.cmd` 7.5K, Sep 28 18:43
  - `pp6_des.par` 283B, Sep 28 18:43
  - `n1_msh.tdr` 2.9M, Sep 28 10:31
- 따라서 기존 reference-package blocker였던 exact editable SDevice source 부재는 active x8 directory 기준으로 해소 가능.
- 다음: snapshot helper를 x8 directory에서 실행해 local golden package와 SHA-256 manifest 생성.

## 2026-10-04 — FAST baseline reproducibility gate and capture helper added

- 작업자: 이택규
- 상태: PROPOSED / TOOLING READY
- GitHub public repository의 CURRENT TCAD deck이 active Copy x8의 authoritative source가 아니라는 점을 재확인.
- 새 문서 `CMP/FAST_BASELINE_REPRO_PROTOCOL.md` 추가: Copy x8 local freeze → clean-account preprocess/hash/diff → reproducibility gate → numerical-only FAST branch 순서를 명문화.
- 새 도구 `CMP/tcad/capture_reference_snapshot.sh` 추가: project directory에서 source/preprocessed/grid/log/runtime context를 local snapshot으로 수집하고 SHA-256 manifest를 생성.
- public GitHub에는 licensed/example-derived source/output 원문을 업로드하지 않고, snapshot은 로컬에만 보존하도록 명시.
- 기존 이택규 기록상 `~/CMP_REFERENCE_20261004.tgz` 패키지는 생성되었으나 `sd_fdiv_des.cmd`가 누락된 상태이므로, 우선 exact Copy x8 source를 local reference package에 추가한 뒤 clean-account preprocess 비교로 진행.
- baseline physics/Nt/Et/sigma/5 nm damage width는 변경하지 않음.

## 2026-10-04 — Claude project instructions rebuilt for paper-grade TCAD implementation

- 작업자: 이택규
- 상태: CONFIRMED
- 새 파일 `CMP/CLAUDE_PROJECT_INSTRUCTIONS.md` 생성.
- 목적: Claude가 단순 코드 생성기가 아니라 CMP 연구 목적, Common Baseline, Project A/B mechanism, 과거 오류/provenance, runtime 병목, clean-account reproducibility, GitHub 기록 규칙을 모두 이해한 상태에서 구현하도록 함.
- 역할 분담을 명시:
  - ChatGPT: 연구 방향/검증/provenance/판단 중심
  - Claude: Sentaurus 코드 구현/디버깅/copy-paste-ready 산출물 중심
- `CMP/AGENTS.md`에도 Claude project instruction 문서 읽기 지침 추가.
- 최종 FAST_BASELINE 작업 프롬프트는 아직 작성하지 않음. 사용자 추가 요구조건을 받은 뒤 작성 예정.

## 2026-10-04 — Copy x8 reference package capture

- 작업자: 이택규
- 상태: IN PROGRESS
- Copy x8 active directory에서 reproducibility/reference package를 생성함.
- 포함: pp1_dvs.cmd, pp6_des.cmd, pp6_des.par, n1_dvs.out, n1_msh.log, n6 job/status/error, Workbench gexec/gtree/gvars/gscens, solver log snapshots, mesh hash, environment/process snapshot.
- 패키지: ~/CMP_REFERENCE_20261004.tgz
- 현재 누락: sd_fdiv_des.cmd. 터미널에서 cd 명령과 cp 명령이 붙어 실행되어 source 복사가 실패함.
- 다음: active Copy x8 directory에서 sd_fdiv_des.cmd를 추가 복사하고 SHA256SUMS 재생성 후 tgz 재패키징.

## 2026-10-03 — Copy x6 vs x7 semantic mesh identity confirmed

- 작업자: 이택규
- 상태: CONFIRMED
- Copy x6 and x7 use identical pp1_dvs.cmd, identical pp6_des.cmd, and identical pp6_des.par.
- Mesh logs show the same 138137 vertices, 274946 elements, and max connectivity 9.
- n1_msh.log differences are limited to process ID and mesh-generation timing/rate.
- Therefore x6 and x7 are semantically the same device/mesh/solver input for the active SDevice run; differing TDR binary hashes are non-physical serialization/metadata differences.
- Operational conclusion: x6 and x7 are duplicate active computations. Since x6 is farther progressed, keep x6 if one v1.1 reference is desired and stop x7 after preserving provenance.
- x8 remains the preferred latest v1.2 reference with intermediate TDR snapshots.

## 2026-10-03 — correction: Copy x6 vs x7 SDE inputs are identical

- 작업자: 이택규
- 상태: OBSERVED / CORRECTION
- Copy x6 and Copy x7 `pp1_dvs.cmd` SHA-256 are identical: `5685528bc3ec338ce104040b0503be43ef032094976d69995529eb5d6fb4e658`.
- `diff -u pp1_dvs.cmd` produced no differences.
- Therefore the SDE geometry/mesh-generation command input is byte-identical between x6 and x7.
- Previous interpretation that differing `n1_msh.tdr` hashes prove a different mesh is withdrawn. Binary TDR hash differences can reflect metadata/order/output serialization and must be verified semantically.
- Next verification: compare TDR sizes plus SDE/mesh logs and node/element statistics before declaring the meshes different.

## 2026-10-03 — active baseline lineage clarified by timestamps and diff

- 작업자: 이택규
- 상태: CONFIRMED / IMPORTANT PROVENANCE
- Copy x6 current source header = Final SDevice v1.1.
- Copy x7 current source header = Final SDevice v1.2 and differs from x6 source only by intermediate Plot snapshots block.
- However Copy x7 active pp6_des.cmd timestamp is 2026-09-28 10:31, while its sd_fdiv_des.cmd was edited later at 12:17. Therefore the already-running Copy x7 job did NOT preprocess from the later v1.2 source revision.
- Copy x8 pp6_des.cmd timestamp is 18:43 and exact diff vs Copy x7 active pp6 shows only the intermediate Plot block. Thus Copy x8 is the actual v1.2-running deck; Copy x7 active run is effectively v1.1 numerics/output behavior despite the folder's source file later being edited to v1.2.
- Copy x6 and Copy x7 active pp6_des.cmd/par hashes are identical, but their n1_msh.tdr hashes differ; therefore their active simulations are not identical because the grid input differs.
- Copy x7 and Copy x8 share identical grid hash and parameter hash, with pp6 difference only intermediate output save block.
- Preferred exact running reference: Copy x8.
- Remaining provenance task: determine why Copy x6 and x7 mesh hashes differ by comparing SDE/preprocessed mesh-generation inputs.

## 2026-10-03 — Copy x7 vs Copy x8 exact command diff confirmed

- 작업자: 이택규
- 상태: CONFIRMED
- Copy x7 and Copy x8 have identical source hash, grid hash, and pp6_des.par hash.
- Exact `diff -u pp6_des.cmd` shows the only command-file difference is an added intermediate `Plot(-Loadable FilePrefix="n6_inter" NoOverWrite Time=(0.80 ... 0.995))` block in Copy x8.
- No Physics, Math, Solve, trap, bias-ramp, or parameter differences were shown by the exact diff.
- Therefore Copy x7 and Copy x8 are the same device/physics/numerics; Copy x8 is an output-save revision only.
- Runtime implication: the multi-day slowdown is not caused by a changed physical model between x7 and x8. Intermediate TDR writes may add I/O overhead at specified save points, but the dominant observed bottleneck remains high-bias Newton nonconvergence and timestep cutback.
- Preferred future reference for analysis/manuscript workflow: Copy x8, because it preserves intermediate spatial states while retaining the same underlying device model.

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
