* ======================================================================
* CMP_BASELINE_3.0.0_WU10FULL - UNTESTED SWB SDEVICE PILOT ONLY
* This is a parameterized MODEL CONSTRUCTION/SMOKE CANDIDATE, NOT the
* validated Wu 2023 physics. Check T-2022.03 actual PP/PAR first.
* SWB node parameters REQUIRED: NtSide, PolAct, Vstop.
* Example smoke: NtSide=0, PolAct=0, Vstop=0.1 (do not infer LED valid).
* Later diagnostics: single-variable OFF/ON, physical polarization and
* validated Mg incomplete-ionization after MaterialDB/species audit.
* Trap energy/conc/sigma are CMP PILOT assumptions, NOT Wu direct values.
* ======================================================================
File {
  Grid="@tdr@"
  Current="@plot@"
  Plot="@tdrdat@"
  Output="@log@"
}
Electrode {
  { Name="anode"   Voltage=0.0 }
  { Name="cathode" Voltage=0.0 }
}
Physics {
  DefaultParametersFromFile
  Fermi
  Mobility( DopingDependence HighFieldSaturation )
  Recombination( SRH Radiative Auger )
  Piezoelectric_Polarization( strain Activation=@PolAct@ )
}
* Bypass IncompleteIonization ONLY for the initial parsing/smoke stage.
* Wu chemical Mg2e19 has NOT yet been converted to a justified active
* density; true Wu-model Mg/ionization is a mandatory next validation.

Physics (Region="DmgL_pGaN") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_pGaN") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgL_Barrier0") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_Barrier0") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgL_QW1") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_QW1") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgL_Barrier1") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_Barrier1") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgL_QW2") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_QW2") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgL_Barrier2") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_Barrier2") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgL_QW3") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_QW3") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgL_Barrier3") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_Barrier3") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgL_QW4") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_QW4") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgL_Barrier4") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_Barrier4") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgL_nGaN") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Physics (Region="DmgR_nGaN") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=0.75
      Conc=@NtSide@ eXsection=1e-15 hXsection=1e-15)
  )
}

Plot {
  eDensity hDensity
  Potential SpaceCharge ElectricField/Vector
  eCurrentDensity/Vector hCurrentDensity/Vector
  eQuasiFermiEnergy hQuasiFermiEnergy
  ConductionBandEnergy ValenceBandEnergy
  Doping DonorConcentration AcceptorConcentration
  RadiativeRecombination SRHRecombination AugerRecombination
  eGapStatesRecombination eTrappedCharge TotalTrapConcentration
}
Math {
  Extrapolate
  Derivatives
  RelErrControl
  Digits=4
  Iterations=25
  NotDamped=100
}
Solve {
  Coupled(Iterations=150) { Poisson }
  Coupled(Iterations=150) { Poisson Electron Hole }
  Quasistationary(
    InitialStep=1e-4 MinStep=1e-10 MaxStep=0.02
    Increment=1.25 Decrement=2.0
    Goal { Name="anode" Voltage=@Vstop@ }
  ) { Coupled { Poisson Electron Hole } }
}
