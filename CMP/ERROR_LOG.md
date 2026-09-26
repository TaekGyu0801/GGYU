## 2026-09-26 — Node 12 log terminates after incomplete-ionization messages

Observed:
- `n12_des.log` ends immediately after repeated messages that `mMagnesiumActiveConcentration` has no incomplete-ionization parameters in InGaN QW regions.
- The tool then checks licenses back in.
- No normal solver start/completion sequence is visible.

Interpretation: **UNRESOLVED**.
This message can no longer be assumed harmless solely from formatting; its causal role must be tested against the successful NtSide=0 branch.

Highest-value comparison:
- Search the successful NtSide=0 node's `*_des.log` for `mMagnesiumActiveConcentration`.
- If identical messages occur and the successful run proceeds, they are not the failure root cause.
- If absent in the successful branch, investigate parameter/material setup differences in the failed branch.

---

## 2026-09-26 — Node 12 Find Error contains warnings only

Observed:
- Workbench `Find Error` reaches `**** End`.
- Visible entries are model/material warnings only:
  - vanOverstraetendeMan E0 isotropic vs anisotropic values.
  - missing incomplete-ionization parameters for `mMagnesiumActiveConcentration` in InGaN QW regions.
- No explicit `ERROR` / `FATAL` root-cause line is visible.

Interpretation:
- These warnings are not yet proven to be the cause of `sdevice exit(1)`.
- The actual SDevice log file `n12_des.log` is now the highest-priority evidence source.

Next:
1. Open `n12_des.log`, inspect the last 50–100 lines.
2. Search there for error/fatal/abort/exception/signal.
3. If non-diagnostic, inspect `n12_des.sta`.

Status: **UNRESOLVED**

---

## 2026-09-26 — Node 12 SDevice exit(1) after successful preprocessing

Job Log evidence:
- Preprocessor successfully initialized.
- `pp12_des.cmd` and `pp12_des.par` were generated.
- Node dependency on node 1 was resolved.
- SDevice launched as:
  `sdevice --max_threads 4 pp12_des.cmd`
- SDevice then terminated with:
  `sdevice exited abnormally: exit(1)`

Interpretation:
- Workbench preprocessing/dependency failure is not the primary blocker.
- The failure occurs inside SDevice after launch, likely during deck/model/material initialization before normal solve completion.
- Exact root cause still requires the first explicit SDevice error/fatal message.

Next:
1. Use Node 12 Job Log **Find Error**.
2. Search `n12_des.err` for `Error:`, `Fatal`, `Unsupported`, `not found`, `invalid`, `cannot`.
3. If needed inspect `n12_des.sta`.

Status: **UNRESOLVED**

---

## 2026-09-26 — Node 12 gjob abnormal child exit

Observed in `n12_local.err`:
```text
Job failed
Error: Unknown error: child process exited abnormally
gjob exits with status 1
```

Meaning:
- Workbench wrapper confirms the SDevice child process exited abnormally.
- This is **not yet the root cause**; it is a generic wrapper-level failure report.

Next:
1. Inspect Node 12 Job Log bottom section.
2. Inspect `n12_des.job` if Job Log is non-diagnostic.
3. Inspect `n12_des.sta` for the last tool stage/status.
4. Search `n12_des.err` / `n12_des.out` for segmentation, killed, memory, fatal, abort, license, or signal text.

Status: **UNRESOLVED**

---

## 2026-09-26 — NtSide=1e18 Node 12 early termination evidence

Observed from Node 12:
- `n12_des.err`: E0 anisotropy and incomplete-ionization parameter warnings are visible; no explicit fatal line in the provided view.
- `n12_des.out`: output ends after material/reference-potential initialization and license check-in.
- Missing normal terminal text: `Sentaurus Device simulation finished`, `Good Bye !`.
- No visible `.tdr` / `.plt` output in the Node Output Files list.

Interpretation: **UNRESOLVED**, but the failure appears to occur before normal solve/output completion rather than as an observed late transient convergence failure.

Next evidence:
1. `n12_local.err`
2. Workbench Job Log
3. `n12_des.job` if needed
4. Search `n12_des.err` for `Error`, `Fatal`, `abort`

Do not alter Nt/Et/sigma/geometry until the process exit reason is known.

---

## 2026-09-26 — NtSide=1e18 baseline split-run failed

Observed:
- Sentaurus Workbench split run에서 `NtSide=0`은 완료.
- `NtSide=1e18`은 failed 상태.

Cause: **UNRESOLVED**

Required evidence:
1. failed 1e18 SDevice node의 `*.err`
2. 해당 `*.out` 마지막 50~100줄
3. 가능하면 failed node 번호와 preprocessed `pp*_des.cmd`

Do not change baseline trap density/energy/cross section or geometry before identifying the actual first failure message.

Status: **UNRESOLVED**

---

# Error Log

## 2026-09-21 — SVisual1 Tcl title

Error:
```text
invalid command name "v"
```

Cause:
Tcl에서 `[V]`가 command substitution으로 해석됨.

Fix:
```tcl
-title {Anode Voltage [V]}
-title {Anode TotalCurrent [raw 2D output]}
```

Status: **Resolved**

---

## 2026-09-21 — SVisual1 fit command

Error:
```text
invalid command name "fit_plot"
```

Cause:
현재 Sentaurus Visual T-2022.03 환경에서 해당 Tcl command가 유효하지 않음.

Status: **Resolved/removed from active script**

---

## 2026-09-21 — SVisual2 invalid create_plot option

Error:
```text
create_plot: "-2d" is not a valid property
```

Cause:
SVisual Tcl에 잘못된 `create_plot -2d` 사용.

Status: **Resolved by minimal dataset-based plot script**

---

## 2026-09-21 — Workbench reference macro

Error:
```text
ERROR: @node|sdevice@: tool instance 'sdevice' doesn't exist
```

Cause:
현재 Workbench flow에서 `@node|sdevice@` reference가 유효하지 않음.

Fix:
바로 앞 SDevice를 `@previous@`로 참조하도록 변경.

Status: **Resolved**

---

## 2026-09-21 — SVisual2 cannot load TDR

Current error:
```text
File 'n9_des.tdr' could not be loaded.
```

Known facts:
- Node 10 = SVisual2
- Node 9 = SDevice2
- Node 9 solver output에는 `Sentaurus Device simulation finished`, `Good Bye !`가 기록됨
- Node 9 Explorer Output Files 화면에서 `n9_des.tdr`이 확인되지 않음
- SVisual2는 현재 `n9_des.tdr`을 hard reference함

Status: **UNRESOLVED**

Next diagnostic:
1. `pp9_des.cmd`의 preprocessed `File { ... }` 블록에서 실제 `Plot = "..."` 값 확인
2. Node 9 Output Files 전체 목록에서 실제 TDR 이름 확인
3. `@tdrdat@` macro가 어떤 파일명으로 치환되는지 확인
4. 필요 시 SVisual2를 실제 output filename에 맞춤

Do not change baseline physics parameters while diagnosing this.
