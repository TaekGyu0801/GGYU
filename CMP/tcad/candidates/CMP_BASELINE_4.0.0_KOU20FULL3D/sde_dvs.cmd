; CMP_BASELINE_4.0.0_KOU20FULL3D - SDE T-2022.03 PROPOSED / NOT RUN
; Kou et al., Optics Express 27 A643 (2019), sec.2 / Fig.1.
; Full 3D 20x20um2 square; 4um damage ring on all four sides.
; x = vertical p-to-n, y and z = lateral (all lengths in um).
; Source-supported: nGaN 4um Si5e18, 4 In0.15 QWs 3nm, QB22nm,
; pAl0.15GaN EBL26nm, pGaN120nm, top heavily doped pGaN20nm.
; 5 barriers assumed for 4 QWs; exact stack order must be checked.
; PILOT, NOT PAPER: MgActive assigned as hole-density proxy 3e17;
; top p+ MgActive=1e19; full top/bottom Ohmic contacts.
; Damage geometry ONLY; traps/SRH require a separate Kou SDevice.
(sde:clear)
(sdegeo:set-default-boolean "ABA")

(define Wm 20.0)
(define Wdamage 4.0)
(define tPplus 0.020)
(define tP 0.120)
(define tEBL 0.026)
(define tQW 0.003)
(define tQB 0.022)
(define tN 4.000)
(define xIn 0.15)
(define xAlEBL 0.15)
(define nDonor 5.0e18)
(define pActiveApprox 3.0e17)
(define pPlusPilot 1.0e19)

(define xNow 0.0)
(define xActiveBegin (+ tPplus tP tEBL))
(define xActiveFinish (+ xActiveBegin (* 5 tQB) (* 4 tQW)))
(define ticks (list 0.0 Wdamage (- Wm Wdamage) Wm))

(define (apply-region-profile region species value)
  (if (> value 0.0)
    (let ((tag (string-append "F_" region "_" species)))
      (sdedr:define-constant-profile tag species value)
      (sdedr:define-constant-profile-region
        (string-append "P_" region "_" species) tag region))))

; Each epitaxial layer uses 3x3 lateral tiles: eight damaged, one clean.
; This preserves (20-2*4)^2 / 20^2 = 36% clean planar area.
(define (add-layer label material thickness donor acceptor alloy)
  (if (> thickness 0.0)
    (let ((xNext (+ xNow thickness)))
      (do ((iy 0 (+ iy 1))) ((= iy 3))
        (do ((iz 0 (+ iz 1))) ((= iz 3))
          (let* ((ya (list-ref ticks iy))
                 (yb (list-ref ticks (+ iy 1)))
                 (za (list-ref ticks iz))
                 (zb (list-ref ticks (+ iz 1)))
                 (prefix (if (and (= iy 1) (= iz 1)) "Clean_" "Dmg_"))
                 (region (string-append prefix
                          (number->string iy) (number->string iz)
                          "_" label)))
            (sdegeo:create-cuboid (position xNow ya za)
                                   (position xNext yb zb)
                                   material region)
            (apply-region-profile region "SiliconActiveConcentration" donor)
            (apply-region-profile region "MagnesiumActiveConcentration" acceptor)
            (apply-region-profile region "xMoleFraction" alloy))))
      (set! xNow xNext))))

; x=0 p-contact side. QW1 is the p-side well and QW4 n-side.
(add-layer "pPlusGaN" "GaN" tPplus 0.0 pPlusPilot 0.0)
(add-layer "pGaN" "GaN" tP 0.0 pActiveApprox 0.0)
(add-layer "EBL" "AlGaN" tEBL 0.0 pActiveApprox xAlEBL)
(add-layer "Barrier0" "GaN" tQB 0.0 0.0 0.0)
(add-layer "QW1" "InGaN" tQW 0.0 0.0 xIn)
(add-layer "Barrier1" "GaN" tQB 0.0 0.0 0.0)
(add-layer "QW2" "InGaN" tQW 0.0 0.0 xIn)
(add-layer "Barrier2" "GaN" tQB 0.0 0.0 0.0)
(add-layer "QW3" "InGaN" tQW 0.0 0.0 xIn)
(add-layer "Barrier3" "GaN" tQB 0.0 0.0 0.0)
(add-layer "QW4" "InGaN" tQW 0.0 0.0 xIn)
(add-layer "Barrier4" "GaN" tQB 0.0 0.0 0.0)
(add-layer "nGaN" "GaN" tN nDonor 0.0 0.0)
(define Xend xNow)

; PILOT top/bottom full-surface contacts. Kou Fig.7 p-contact is
; 4um wide; original placement is NOT implemented or validated here.
(sdegeo:define-contact-set "anode" 4.0 (color:rgb 1 0 0) "##")
(sdegeo:define-contact-set "cathode" 4.0 (color:rgb 0 0 1) "##")
(do ((iy 0 (+ iy 1))) ((= iy 3))
  (do ((iz 0 (+ iz 1))) ((= iz 3))
    (let ((ym (/ (+ (list-ref ticks iy) (list-ref ticks (+ iy 1))) 2.0))
          (zm (/ (+ (list-ref ticks iz) (list-ref ticks (+ iz 1))) 2.0)))
      (sdegeo:set-contact
        (find-face-id (position 0.0 ym zm)) "anode")
      (sdegeo:set-contact
        (find-face-id (position Xend ym zm)) "cathode"))))

; Tentative 3D mesh. Inspect elements and quality before SDevice.
(sdedr:define-refeval-window "Win_All" "Cuboid"
  (position 0 0 0) (position Xend Wm Wm))
(sdedr:define-refinement-size "Ref_All"
  0.40 1.50 1.50 0.010 0.30 0.30)
(sdedr:define-refinement-placement "Place_All" "Ref_All" "Win_All")
(sdedr:define-refeval-window "Win_MQW" "Cuboid"
  (position xActiveBegin 0 0) (position xActiveFinish Wm Wm))
(sdedr:define-refinement-size "Ref_MQW"
  0.0015 1.50 1.50 0.0005 0.20 0.20)
(sdedr:define-refinement-placement "Place_MQW" "Ref_MQW" "Win_MQW")
(sdedr:define-refeval-window "Win_Ymin" "Cuboid"
  (position 0 0 0) (position Xend Wdamage Wm))
(sdedr:define-refeval-window "Win_Ymax" "Cuboid"
  (position 0 (- Wm Wdamage) 0) (position Xend Wm Wm))
(sdedr:define-refeval-window "Win_Zmin" "Cuboid"
  (position 0 0 0) (position Xend Wm Wdamage))
(sdedr:define-refeval-window "Win_Zmax" "Cuboid"
  (position 0 0 (- Wm Wdamage)) (position Xend Wm Wm))
(sdedr:define-refinement-size "Ref_Edge"
  0.30 0.80 0.80 0.010 0.20 0.20)
(sdedr:define-refinement-placement "Place_Ymin" "Ref_Edge" "Win_Ymin")
(sdedr:define-refinement-placement "Place_Ymax" "Ref_Edge" "Win_Ymax")
(sdedr:define-refinement-placement "Place_Zmin" "Ref_Edge" "Win_Zmin")
(sdedr:define-refinement-placement "Place_Zmax" "Ref_Edge" "Win_Zmax")
(sde:build-mesh "n@node@")
