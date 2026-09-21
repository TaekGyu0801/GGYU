# TCAD 공식 매뉴얼 / 예제 참고자료 인덱스

Last indexed: 2026-09-21

이 문서는 이택규가 업로드한 Synopsys Sentaurus T-2022.03 매뉴얼과 예제 파일을
CMP 프로젝트의 **참고자료 카탈로그**로 기록한 것이다.

> 중요: 현재 GGYU 저장소는 public이다. 업로드된 Synopsys 매뉴얼에는 proprietary/confidential notice가 있으므로
> 원본 PDF 전체나 예제 원문 전체를 이 public 저장소에 복제하지 않는다.
> 여기에는 파일 식별정보, 용도, 확인된 핵심 참고 포인트만 기록한다.

## 1. 공식 User Guide — T-2022.03

### Sentaurus Device
- 사용자 제공 파일: `sdevice_ug.pdf`
- 문서: **Sentaurus Device User Guide**
- 버전: **T-2022.03, March 2022**
- 분량: 1739 PDF pages
- 프로젝트에서 우선 참고할 항목:
  - File Section — manual TOC reference p.110
  - CurrentPlot Section — p.166
  - Plot Section — p.1190
  - 물리 모델 / Trap / Recombination / Solve / Math / File output syntax 검증
- 사용 규칙:
  - SDevice keyword를 추측으로 추가하기 전에 이 매뉴얼을 우선 확인
  - 특히 현재 SDevice2 → SVisual2 output 문제에서는 `File { Plot=... }` 의미와 실제 preprocessed output을 함께 확인

### Sentaurus Structure Editor
- 사용자 제공 파일: `sde_ug.pdf`
- 문서: **Sentaurus Structure Editor User Guide**
- 버전: **T-2022.03, March 2022**
- 분량: 861 PDF pages
- 우선 참고 항목:
  - `sde:build-mesh` — TOC reference p.438
  - `sdedr:define-refinement-size` — p.561
  - `sdegeo:create-cuboid` — p.611
  - `sdegeo:create-rectangle` — p.625
- 프로젝트 용도:
  - CMP geometry / region / contact / doping / mesh command 검증
  - DmgL | Clean | DmgR 구조를 수정할 때 Scheme syntax 확인

### Sentaurus Mesh
- 사용자 제공 파일: `smesh_ug.pdf`
- 문서: **Sentaurus Mesh User Guide**
- 버전: **T-2022.03, March 2022**
- 분량: 164 PDF pages
- 우선 참고 항목:
  - Defining Refinement Regions — p.26
  - Placing Refinement Regions — p.38
  - Doping and Refinement Examples — p.96
  - Regionwise / Materialwise Refinement — p.100
  - Interface Refinement — p.115
- 프로젝트 용도:
  - 5 nm sidewall damage mesh
  - MQW / heterointerface mesh
  - mesh convergence 조건 검증

### Sentaurus Visual
- 사용자 제공 파일: `svisual_ug.pdf`
- 문서: **Sentaurus Visual User Guide**
- 버전: **T-2022.03, March 2022**
- 분량: 583 PDF pages
- 우선 참고 항목:
  - `create_plot` — p.231
  - `load_file` — p.318
  - `zoom_plot` — p.386
- 프로젝트 용도:
  - SVisual Tcl syntax 검증
  - dataset/plot 생성
  - TDR/PLT load
  - scalar/field 확인
- 이미 프로젝트에서 확인된 교훈:
  - 현재 환경에서 `create_plot -2d`는 invalid
  - 2D dataset은 `create_plot -dataset <dataset>` 형태를 우선 확인

---

## 2. 업로드된 Sentaurus 예제

### A. Device Variability — Metal Workfunction variation
- 가이드: `greadme.pdf`
- 제목: **Device Variability Simulation**
- companion file: `sdevice.par`
- 확인된 내용:
  - Metal work function 예시
  - `WorkFunction = 4.205 eV`
  - `MetalWorkFunction(Randomize(...))` 개념 소개
- CMP 직접 관련도: 낮음
- 활용 가능성: parameter file / stochastic variation syntax 참고

### B. Textured Silicon Solar Cell — Raytracer
- 가이드: `greadme (1).pdf`
- 제목: **EQE and I–V Curve Calculation of a Textured Silicon Solar Cell Using the Raytracer**
- companion files:
  - `sdevice_des.cmd`
  - `sde_dvs.cmd`
  - `sdevice (2).par`
- duplicate files:
  - `sdevice_des (3).cmd` = `sdevice_des.cmd`와 SHA-256 동일
  - `sde_dvs (4).cmd` = `sde_dvs.cmd`와 SHA-256 동일
- 공식 example path가 파일 header에서 확인됨:
  - `examples/opto/solarcell/si/textured/sc-texture-opto-3d/`
- CMP에 특히 중요한 확인 포인트:
  - SDevice `File` block에서 Workbench macro를 사용해
    - grid → `@tdr@`
    - current → `@plot@`
    - output → `@log@`
    - plot → `@tdrdat@`
    - parameter → `@parameter@`
    로 연결하는 공식 예제 패턴이 존재
  - 따라서 현재 Node 9 문제에서는 **원본 command의 macro 자체를 추측으로 바꾸기보다 pp9_des.cmd에서 실제 치환 결과를 확인**하는 것이 우선
  - Plot / CurrentPlot / Physics / optical solver 구성의 실제 예제 참고 가능
- CMP 직접 관련도: **높음 — File/Plot output linkage 및 Workbench preprocessing 참고**

### C. SRAM Statistical Variability — IFM
- 가이드: `greadme (5).pdf`
- 제목: **Modeling Statistical Variability of Static Noise Margins of SRAM Cells Using the Statistical Impedance Field Method**
- 내용:
  - statistical IFM
  - 3D FinFET SRAM / 2D mixed-mode SRAM
  - random dopant / oxide roughness / metal workfunction / interface trap variability
- CMP 직접 관련도: 중간~낮음
- 활용 가능성:
  - 향후 statistical sensitivity / variability study 방법론 참고

### D. provenance 미확정 parameter snippets
- `sdevice (6).par`
  - Silicon / PolySi / SiGe / Oxide / HfO2 parameter include 구조
- `sdevice (7).par`
  - HeavyIon recombination/generation parameter block
- 현재 업로드된 greadme들과 직접 어떤 example set에 속하는지는 **확인되지 않음**
- 상태: `UNRESOLVED provenance`
- 규칙: 출처를 추정해서 특정 예제에 연결하지 않는다.

---

## 3. Readme.txt에 기록된 추가 탐색 후보

사용자 제공 `Readme.txt`에는 MobaXterm/Applications_Library에서 추가로 참고할 후보가 기록되어 있음.

### FinFET
- `examples/Applications_Library/FinFET/FinFET_7nm/`
- `examples/Applications_Library/FinFET/FinFET_10nm/`
- `examples/Applications_Library/FinFET/FinFET_14nm/`
- `examples/Applications_Library/FinFET/FinFET_22nm/`

### AdvancedTransport
- `examples/Applications_Library/AdvancedTransport/NSFET_SdeviceSBTE_3nm/`
- `examples/Applications_Library/AdvancedTransport/Nanowire_Si_QTX_SBTE_5nm/`
- `examples/Applications_Library/AdvancedTransport/Nanowire_Si_QTX_NEGF_5nm/`

### Memory
- `examples/Applications_Library/Memory/SRAM_FinFET_25nm/`
- `examples/Applications_Library/Memory/DRAM-Access_VerticalPillar/`
- `examples/Applications_Library/Memory/NAND_VerticalGate_PolyGrain/`

이 경로들은 **향후 실제 설치환경에서 파일을 확인한 뒤** 프로젝트 참고자료로 추가한다.

---

## 4. AI 사용 규칙

ChatGPT / Claude가 Sentaurus syntax 또는 지원 keyword를 확신하지 못하면:

1. 현재 실제 project code 확인
2. 이 Reference Index 확인
3. 해당 T-2022.03 User Guide 확인
4. 업로드된 공식 example pattern 확인
5. 그래도 불명확하면 `PROPOSED`로만 제안

공식 매뉴얼/예제와 현재 설치환경의 실제 실행 결과가 충돌하면
**현재 T-2022.03 실행 로그와 preprocessed file을 최종 근거로 우선**한다.

특히 이미 실패한 임의 keyword 추가를 반복하지 않는다.
