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
