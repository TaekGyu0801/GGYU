# Current Status

Last synchronized: 2026-09-21

## Current stage

**Common Baseline v1 validation — geometry mostly validated; SVisual2 output-file linkage currently unresolved.**

## Parallel work — Ju Subin

**Status: OBSERVED — shared project conversation / user report**

주수빈은 별도 채팅에서 Common Baseline 관련 메인 SDevice 및 앞서 검토한 관련 코드를 최종 수정했다고 보고했으며, 장시간 simulation을 시작하기 전에 Project A와 Project B 모두에 적합한 baseline인지 마지막 정적/논리 검토를 진행 중이다.

현재 계획:
- 우선 `NtSide=0`
- 우선 `NtSide=1e18`

두 조건만 먼저 실행해 baseline 동작을 확인.

주수빈 보고 기준으로 한 run이 약 3일 걸릴 수 있어 전체 sweep 전에 코드 검증을 우선한다.

**중요:** 이 기록 시점에는 주수빈 측 최신 전체 코드 원문 및 새 simulation 결과가 GitHub에서 직접 검증되지 않았다. 따라서 코드 정확성이나 실행 성공을 CONFIRMED로 간주하지 않는다.

## Confirmed

### Geometry / Regions
Sentaurus Visual에서 다음 region들이 실제로 존재함을 확인:
- Clean_Barrier0~4
- Clean_EBL
- Clean_QW1~4
- Clean_nGaN
- Clean_pGaN
- DmgL_Barrier0~4
- DmgL_EBL
- DmgL_QW1~4
- DmgL_nGaN
- DmgL_pGaN
- DmgR_Barrier0~4
- DmgR_EBL
- DmgR_QW1~4
- DmgR_nGaN
- DmgR_pGaN
- Nitride_L / Nitride_R

따라서 `DmgL | Clean | DmgR` partition은 구조적으로 구현됨.

### Doping visual check
DopingConcentration map에서:
- p-side 약 -3×10^17 cm^-3 scale
- n-GaN 약 +5×10^18 cm^-3 scale
확인됨.

### Vertical stack visual check
- MQW 층이 존재
- n-GaN 시작 위치가 p-GaN 0.120 µm + EBL 0.026 µm + MQW 0.122 µm ≈ 0.268 µm와 시각적으로 일치
- Nitride_R 폭이 약 0.1 µm scale로 보임

### SVisual1
초기 오류 수정:
1. `"Anode Voltage [V]"`의 Tcl command substitution 문제
   - 수정: `{Anode Voltage [V]}`
2. `fit_plot` unsupported
   - 수정/제거 후 실행 가능 상태 확보

### SDevice2
Node 9 `n9_des.out`에서:
- `Sentaurus Device simulation finished`
- `Good Bye !`
확인.
즉 SDevice2 solver 자체는 정상 종료한 실행 이력이 있음.

## Current blocker

SVisual2(Node 10)가 다음 파일을 읽도록 되어 있음:

```text
n9_des.tdr
```

현재 SVisual2 오류:

```text
Error: File 'n9_des.tdr' could not be loaded.
```

Node 9 Explorer의 Output Files 화면에서는 당시:
- n9_des.err
- n9_des.job
- n9_des.out
- n9_des.sta
- n9_local.err
- pp9_des.cmd
- pp9_des.par

가 보였으며 `n9_des.tdr`은 목록에서 확인되지 않았음.

따라서 현재 핵심 질문은:

**SDevice2가 실제 Plot/TDR output을 어떤 파일명으로 생성하도록 preprocessing 되었는가, 또는 왜 TDR이 생성되지 않았는가?**

## Important: do not change yet

이 blocker를 해결하기 위해 아래 baseline parameter를 바꾸지 말 것:
- Nt
- Et
- sigma_n / sigma_p
- 5 nm damage width
- Kou epitaxy
- mesa width
- doping

현재 문제는 우선 output/dependency/file-linkage 문제로 취급한다.

## Files synchronized to GitHub

- `CMP/tcad/CURRENT/sdevice2_defect_on.cmd`
- `CMP/tcad/CURRENT/svisual1_iv.tcl`
- `CMP/tcad/CURRENT/svisual2_maps.tcl`

아직 최신 전체 원문이 GitHub에 없는 것:
- SDE
- SDevice1
- 주수빈 측 최신 수정 코드 전체 원문

이들은 연구자가 실제 최신 코드를 동기화하기 전까지 추정 생성 금지.
