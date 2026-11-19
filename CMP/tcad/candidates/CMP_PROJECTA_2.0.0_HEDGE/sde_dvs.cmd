; =====================================================================
; CMP_PROJECTA_2.0.0_HEDGE — PROPOSED / UNRUN on school (GPT independent)
; DERIVED FROM GitHub 3.2.0 PROPOSED SDE — NOT byte-verified school working source.
; PARENT: CMP_BASELINE_3.3.1_GPTD50, bilateral damage 50nm; UNRUN candidate.
; IMPORTANT: NtSide fixed means nominal integrated trap inventory x10.
; Parent CMP_BASELINE_3.0.0_WU10FULL is preserved.
; Wu 2023 DOI 10.1016/j.micrna.2023.207542:
; Wmesa10um, nGaN3.9um nSi5e18, 4x InGaN(x=0.08) 3nm QWs,
; GaN 8nm QB, core Mg2e19 and edge Mg2e16 effective,
; 50nm damaged semiconductor at sidewalls.
; Sidewall width here is a CMP stress-test hypothesis, NOT the original Wu 5nm.
; UNVERIFIED: pGaN thickness, EBL, barrier count, electrode locations,
; background QB doping, true Mg substitutional fraction.
; We map nominal Mg to active species BEFORE incomplete ionization in
; SDevice; validate actual ionized acceptors/free holes in 5V TDR.
; 2D Cartesian stripe NOT a measured 10um x 10um square.
; =====================================================================
(sde:clear)
(sdegeo:set-default-boolean "ABA")

(define Wm       10.0)
(define Wdmg      0.050)
(define WHedge    0.200)          ; lateral pGaN deactivation width per side [um]
(define tP        0.120)          ; PILOT thickness; Wu value unverified
(define tEBL      0.000)          ; NOT PROOF Wu lacks EBL; figure not available
(define xAlEBL    0.15)           ; UNUSED when tEBL=0
(define tQW       0.003)
(define tQB       0.008)
(define tN        3.900)
(define ND        5.0e18)        ; Wu n-GaN
(define PMgEdge   2.0e16)        ; effective pGaN active Mg in both edge strips
(define PMgActive 2.0e19)        ; Wu nominal Mg, substitutional mapping ASSUMED
(define NBg       1.0e15)        ; PILOT undoped-barrier background
(define xIn       0.08)

(define xNow 0.0)
(define xActiveStart (+ tP tEBL))
(define xActiveEnd (+ xActiveStart (* 5 tQB) (* 4 tQW)))

(define (seg-list)
  (list (list "DmgL" 0.0 Wdmg)
        (list "Clean" Wdmg (- Wm Wdmg))
        (list "DmgR" (- Wm Wdmg) Wm)))

(define (place-field region species value)
  (if (> value 0.0)
      (let ((tag (string-append "F." species "." region)))
        (sdedr:define-constant-profile tag species value)
        (sdedr:define-constant-profile-region
          (string-append "P." species "." region) tag region))))

; Material identity retained in DmgL/DmgR (not dielectric substitution).
(define (add-layer label material thick nval pval alloy)
  (if (> thick 0.0)
      (let ((xNext (+ xNow thick)))
        (for-each
          (lambda (seg)
            (let* ((part (car seg))
                   (ya (cadr seg))
                   (yb (caddr seg))
                   (rname (string-append part "_" label)))
              (sdegeo:create-rectangle
                (position xNow ya 0) (position xNext yb 0)
                material rname)
              (if (> nval 0.0)
                  (place-field rname "nSiliconActiveConcentration" nval))
              (if (> pval 0.0)
                  (place-field rname "MagnesiumActiveConcentration" pval))
              (if (> alloy 0.0)
                  (place-field rname "xMoleFraction" alloy))))
          (seg-list))
        (set! xNow xNext))))


; pGaN ONLY: 5 lateral segments. Original DmgL/DmgR names remain,
; preserving ALL 22 SDevice Dmg Region trap assignments.
; No explicit H atoms/diffusion; low active Mg is a screening proxy.
(define (pgan-seg-list)
  (list (list "DmgL" 0.0 Wdmg)
        (list "HEdgeL" Wdmg WHedge)
        (list "Clean" WHedge (- Wm WHedge))
        (list "HEdgeR" (- Wm WHedge) (- Wm Wdmg))
        (list "DmgR" (- Wm Wdmg) Wm)))

(define (add-pgan-with-edge-deactivation)
  (let ((xNext (+ xNow tP)))
    (for-each
      (lambda (seg)
        (let* ((part (car seg))
               (ya (cadr seg))
               (yb (caddr seg))
               (rname (string-append part "_pGaN"))
               (MgVal (if (string=? part "Clean") PMgActive PMgEdge)))
          (sdegeo:create-rectangle
            (position xNow ya 0) (position xNext yb 0)
            "GaN" rname)
          (place-field rname "MagnesiumActiveConcentration" MgVal)))
      (pgan-seg-list))
    (set! xNow xNext)))

; Stack from p-side to n-side, QW1 at p-side and QW4 at n-side.
(add-pgan-with-edge-deactivation)
(add-layer "EBL"      "AlGaN" tEBL  0.0 PMgActive xAlEBL)
(add-layer "Barrier0" "GaN"   tQB   NBg 0.0 0.0)
(add-layer "QW1"      "InGaN" tQW   0.0 0.0 xIn)
(add-layer "Barrier1" "GaN"   tQB   NBg 0.0 0.0)
(add-layer "QW2"      "InGaN" tQW   0.0 0.0 xIn)
(add-layer "Barrier2" "GaN"   tQB   NBg 0.0 0.0)
(add-layer "QW3"      "InGaN" tQW   0.0 0.0 xIn)
(add-layer "Barrier3" "GaN"   tQB   NBg 0.0 0.0)
(add-layer "QW4"      "InGaN" tQW   0.0 0.0 xIn)
(add-layer "Barrier4" "GaN"   tQB   NBg 0.0 0.0)
(add-layer "nGaN"     "GaN"   tN    ND  0.0 0.0)
(define Xend xNow)

; Boundary contacts: provisional full-width planar Ohmic geometry only!
; The original Wu electrode sizes/placements must be sourced before freeze.
(sdegeo:define-contact-set "anode"   4.0 (color:rgb 1 0 0) "##")
(sdegeo:define-contact-set "cathode" 4.0 (color:rgb 0 0 1) "##")
; Every pGaN top edge receives anode, including both new HEdge strips.
(for-each
  (lambda (seg)
    (let ((ymid (/ (+ (cadr seg) (caddr seg)) 2.0)))
      (sdegeo:set-contact
        (find-edge-id (position 0.0 ymid 0)) "anode")))
  (pgan-seg-list))
; nGaN bottom stays in the original three lateral segments.
(for-each
  (lambda (seg)
    (let ((ymid (/ (+ (cadr seg) (caddr seg)) 2.0)))
      (sdegeo:set-contact
        (find-edge-id (position Xend ymid 0)) "cathode")))
  (seg-list))

; Mesh: 50 nm Dmg strips; original 1 nm lateral edge refinement retained
; temporarily for mesh preflight (may be heavy), QWs 3nm still require fine x.
(sdedr:define-refeval-window "Win.All" "Rectangle"
  (position 0.0 0.0 0) (position Xend Wm 0))
(sdedr:define-refinement-size "Ref.All" 0.20 0.35 0.010 0.020)
(sdedr:define-refinement-placement "Place.All" "Ref.All" "Win.All")

(sdedr:define-refeval-window "Win.MQW" "Rectangle"
  (position xActiveStart 0.0 0) (position xActiveEnd Wm 0))
(sdedr:define-refinement-size "Ref.MQW" 0.0020 0.15 0.0004 0.010)
(sdedr:define-refinement-placement "Place.MQW" "Ref.MQW" "Win.MQW")

(sdedr:define-refeval-window "Win.EdgeL" "Rectangle"
  (position 0.0 0.0 0) (position Xend Wdmg 0))
(sdedr:define-refeval-window "Win.EdgeR" "Rectangle"
  (position 0.0 (- Wm Wdmg) 0) (position Xend Wm 0))
(sdedr:define-refinement-size "Ref.Edge" 0.020 0.0010 0.002 0.0005)
(sdedr:define-refinement-placement "Place.EdgeL" "Ref.Edge" "Win.EdgeL")
(sdedr:define-refinement-placement "Place.EdgeR" "Ref.Edge" "Win.EdgeR")


; Local mesh for two pGaN deactivated strips, no coarsening of
; pre-existing fine MQW or 50nm-Dmg edge mesh.
(sdedr:define-refeval-window "Win.HEdgeL" "Rectangle"
  (position 0.0 Wdmg 0) (position tP WHedge 0))
(sdedr:define-refeval-window "Win.HEdgeR" "Rectangle"
  (position 0.0 (- Wm WHedge) 0) (position tP (- Wm Wdmg) 0))
(sdedr:define-refinement-size "Ref.HEdge" 0.020 0.020 0.005 0.005)
(sdedr:define-refinement-placement "Place.HEdgeL" "Ref.HEdge" "Win.HEdgeL")
(sdedr:define-refinement-placement "Place.HEdgeR" "Ref.HEdge" "Win.HEdgeR")

; Evaluate mesh SVisual for 50nm Dmg strips, QW thicknesses, min angle and
; tiny-edge artifacts. Do NOT mark VALID before actual T-2022.03 run.
(sde:build-mesh "n@node@")
