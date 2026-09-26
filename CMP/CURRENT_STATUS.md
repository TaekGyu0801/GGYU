# Current Status

## 2026-09-26 — Full source resolves the Node 6/12 preprocessing discrepancy

The current full SDevice source contains no NtSide-dependent conditional preprocessing. `@NtSide@` appears in trap concentration only. The current source always includes `Thermionic`, species-selected Mg incomplete ionization, and the expanded Mg/quasi-Fermi Plot fields.

Therefore the successful Node 6 generated deck (which lacked these lines) is almost certainly from an earlier source revision and was not regenerated when Node 12 was rerun. Existing Node 6 output remains a valid result for its historical deck, but it is not a clean same-source control for the current Node 12.

The current Node 12 initialization failure remains strongly correlated with Mg incomplete-ionization setup in InGaN. Next evidence required: `pp12_des.par` Ionization/Magnesium/InGaN definitions.


## 2026-09-26 — Node 12 failure reproducible on rerun

The NtSide=1e18 Node 12 was rerun alone and failed again in the same manner. This makes a transient scheduler/license glitch less likely and points to a reproducible input/configuration problem for Node 12.

Because the user confirms a single source with only NtSide split, the observed pp6/pp12 differences most plausibly come from either:
1. NtSide-dependent preprocessing in the source, or
2. stale/cached Node 6 generated files from an earlier source revision while Node 12 was re-preprocessed from the current source.

No physics change should be made until the original source conditional logic/provenance is checked.


## 2026-09-26 — Correction: Node 6/12 came from the same source split

User explicitly confirmed that Node 6 and Node 12 were generated from the same SDevice source and only `NtSide` was split (0 vs 1e18).

Therefore the observed pp6/pp12 differences must not be interpreted as proven manual/source-deck drift. Plausible mechanisms now include:
- NtSide-dependent preprocessor conditionals in the source,
- parameter-dependent macro expansion,
- or node/input version/cache differences.

No physics/model line should be removed yet. The next diagnostic is to inspect the original `sd_fdiv_des.cmd` around NtSide and any conditional preprocessing.


## 2026-09-26 — Ju Subin Node 6/12 deck diff resolved a major confounder

Direct comparison of the successful Node 6 and failed Node 12 preprocessed Physics/Plot blocks confirms that the two runs differ by more than NtSide:

- Node 6: no `Thermionic`; plain `IncompleteIonization`; no Mg-specific/quasi-Fermi-energy Plot fields.
- Node 12: `Thermionic`; `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`; extra `eQuasiFermiEnergy`, `hQuasiFermiEnergy`, `pMagnesiumActiveConcentration`, `pMagnesiumMinusConcentration` Plot fields.
- Trap concentration: 0 vs 1e18 as intended.

Therefore the failed Node 12 is **not a clean NtSide-only comparison**. The immediate recovery plan is to restore the successful Node 6 Physics/Plot configuration in the original SDevice source and vary only the trap concentration for the 1e18 rerun. No claim is made yet that Thermionic or species-selected incomplete ionization is intrinsically invalid.


## 2026-09-26 — Failed Node 12 preprocessed deck differs from synchronized baseline

User supplied the failed Node 12 preprocessed Physics/Plot section. It contains:
- `Thermionic`
- `IncompleteIonization(Dopants="pMagnesiumActiveConcentration")`
- sidewall trap Conc=1e18 in DmgL/R pGaN, EBL, Barrier0~4, QW1~4, nGaN
- expanded Plot keywords for SRH subcomponents, trap fields, and Mg species

The synchronized baseline deck currently in GitHub has plain `IncompleteIonization`, no `Thermionic`, and a simpler Plot list. Therefore the failed Node 12 cannot yet be treated as a proven NtSide-only split until it is directly diffed against successful Node 6.


## 2026-09-26 — Ju Subin baseline result strengthened

**CONFIRMED:** successful `NtSide=0` Node 6 reached 5.0 V, finished the curve trace, wrote `n6_des.tdr`, and ended with normal SDevice completion text. Wallclock ≈235312 s (~65.4 h, ~2.7 days).

**FAILED:** `NtSide=1e18` Node 12 exits during initialization with SDevice `exit(1)`, before normal solve/output completion.

Key branch difference observed in logs:
- Node 6 success: no `mMagnesiumActiveConcentration` message found by user search.
- Node 12 fail: repeated InGaN incomplete-ionization parameter messages immediately before termination.

This is a strong diagnostic difference but not yet sufficient to change physics. First verify preprocessed CMD/PAR files differ only by intended NtSide trap concentration.


## 2026-09-26 — Ju Subin baseline split-run result

**OBSERVED:** 주수빈이 학교에서 이전에 실행해 둔 Common Baseline split run을 확인함.

- `NtSide=0`: 정상 완료
- `NtSide=1e18`: failed

현재는 1e18 실패 원인이 아직 식별되지 않았다. 0 조건이 완료됐다는 사실은 동일 flow가 최소한 trap-off 조건에서 실행 가능함을 보여주지만, 이것만으로 1e18 실패가 trap physics 자체 때문이라고 확정할 수는 없다.

**Immediate diagnostic:** 실패한 1e18 node의 `*.err` 전체와 `*.out` 마지막 50~100줄에서 최초 error/fatal/convergence failure를 확인한다. 원인 확인 전 Common Baseline의 Nt/Et/sigma/5 nm damage width/epitaxy를 변경하지 않는다.


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


## Parallel blocker update — Ju Subin runtime

**OBSERVED 2026-09-22:** Node 6 SDevice는 18시간 이상 실행 중이지만 현재 출력상 멈춘 것이 아니라 BE stepping을 계속 수행하고 있다. 공유 화면에서 직전 step은 수렴 완료됐고 총 wallclock 약 3563.68 s(약 59분), 다음 step은 `0.0766738 → 0.0776738` with `Stepsize=1e-3`로 진행 중이다.

현재 주수빈 트랙의 즉시 blocker는 **실패가 아니라 과도한 per-step runtime / 총 run time 불확실성**이다. 다음 판단에는 `pp6_des.cmd` Solve block의 최종 목표와 step-control 값 확인이 필요하다. Baseline physics parameter는 이 진단 때문에 임의 변경하지 않는다.


## Ju Subin runtime blocker — cause identified

**CONFIRMED 2026-09-22:** Node 6의 장시간 실행은 현재 `Transient` bias ramp의 매우 작은 `MaxStep=1e-3`와 큰 per-step solve cost가 결합된 결과다. Goal은 anode 5.0 V이며, 로그의 pseudo-time 0.0766738에서 anode ≈0.3834 V가 `5×time`과 일치한다. 따라서 MaxStep 1e-3은 약 5 mV/bias step에 해당하며 5 V까지 약 1000 accepted steps 규모가 필요하다. 현재 지점에서만 최소 약 923~924 steps가 남는다.

최근 약 3564 s/step을 그대로 외삽하면 남은 시간이 약 38일 수준이 될 수 있으므로, 현재 blocker는 **numerical step strategy / computational cost**로 갱신한다. 물리 baseline parameter는 이 문제 해결을 위해 변경하지 않는다.


## Ju Subin runtime diagnosis refinement

사용자가 **최종 수정 전 거의 같은 deck이 약 3일 내 완료**되었다고 보고했다. 따라서 현재 확인된 `MaxStep=1e-3`은 긴 총 step 수를 설명하지만, **이번 run이 과거보다 느려진 원인을 단독으로 설명하지는 못한다.** 이전 run과 step-control이 같았다면 핵심 차이는 per-step 계산비용 또는 step rejection/cutback 증가다.

현재 우선 비교 대상은 old vs current의 mesh 규모, Physics/Trap 적용 범위, Math/linear solver 설정, 그리고 n*_des.out의 rejected/repeated step 이력이다. 최근 3564 s 한 step으로 산출한 ~38일 값은 실제 총시간 예측이 아니라 단순 외삽 참고치로 강등한다.


## Ju Subin runtime evidence — old run around 0.30 V

과거 약 3일 내 완료된 run에서 anode 약 0.3034 V step의 Total time은 172.57 s, 약 0.3084 V step은 123.94 s였고 각각 5 Newton iterations로 수렴했다. 현재 run의 약 0.3834 V step은 Total 약 3563.68 s가 관찰됐다. bias가 완전히 같지는 않지만, **현재 run의 accepted step 비용이 과거 run보다 크게 증가한 정황이 강해졌다.** 최종 비교를 위해 과거 0.38 V 부근 로그 확인이 필요하다.


## Ju Subin runtime root cause narrowed at identical bias

Old/current를 **동일 accepted anode ≈0.3834 V**에서 직접 비교했다. old run은 Total 177.47 s (Assembly 64.84 s, Solve 108.74 s), current run은 Total 3563.68 s (Assembly 598.77 s, Solve 2928.83 s)였다. 현재 step은 old 대비 약 **20.1× 느림**. 따라서 현재 장시간 문제는 MaxStep/step 개수보다 per-step computational cost 증가가 핵심이다.


## Correction — Ju Subin runtime interpretation (2026-09-22)

앞서 'old run 0.3834 V = 177.47 s vs current = 3563.68 s'로 기록한 비교는 **무효**다. 177.47 s 로그도 현재 Node 6의 동일 `n6_des.out` 초기 구간임이 확인됐다.

현재 확인된 사실:
- 현재 run 초기 구간: 0.0756738→0.0766738, accepted anode ≈0.3834 V, Total 177.47 s.
- 같은 현재 run의 더 뒤쪽 화면: accepted anode ≈0.3834 V 직후 Total 3563.68 s.
- 따라서 현재 핵심 질문은 **한 run 안에서 같은 ramp coordinate가 왜 다시 나타나는지 / 서로 다른 Transient or Solve stage인지**이다.

old-vs-current 20.1× slowdown 결론은 철회하고, stage identification 전까지 원인을 mesh/physics/solver 변화로 확정하지 않는다.


## Re-correction — old/current runtime comparison restored

사용자가 직전 스크린샷이 **예전에 약 3일 만에 완료된 노드의 `n6_des.out`**이라고 명확히 확인했다. 따라서 앞서 추가한 "같은 current run 내부 초기 구간" 해석은 철회한다.

유효한 동일-bias 비교:
- old run, anode ≈0.3834 V: Assembly 64.84 s, Solve 108.74 s, Total 177.47 s
- current run, anode ≈0.3834 V: Assembly 598.77 s, Solve 2928.83 s, Total 3563.68 s
- current/old Total ≈ 20.1×

따라서 현재 장시간 문제는 **per-step solve cost 증가**가 핵심이며, old/current deck 차이 비교가 우선이다.


## Ju Subin old 3-day deck captured

과거 약 3일 완료된 preprocessed SDevice deck의 전체 설정을 확보했다. 이 old deck은 모든 sidewall damage trap의 `Conc=0`인 **NtSide=0 케이스**다. 또한 Transient 설정은 `1e-5 / 1e-9 / 1e-3 / Increment 1.2 / Goal 5 V`로 현재 slow run에서 확인한 step-control과 동일하다.

따라서 다음 판정의 핵심은 현재 slow Node 6도 `Conc=0`인지 여부다. current가 1e18이면 old 0과 runtime을 직접 비교하면 안 된다. current도 0이면 Math/Physics/mesh 차이로 바로 좁힌다.
