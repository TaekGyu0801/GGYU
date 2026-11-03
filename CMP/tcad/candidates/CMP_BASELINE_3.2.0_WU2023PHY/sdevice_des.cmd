* ======================================================================
* CMP_BASELINE_3.2.0_WU2023PHY — PROPOSED/NOT RUN ON SCHOOL T-2022.03
* Parent original remains unchanged. Requires companion sdevice.par
* and SWB macro parameters NtSide, Vstop, TrapEt, TrapSigmaN, TrapSigmaP.
* Mg 2e19 nominal via SDE MagnesiumActiveConcentration; ionization
* calculated here. Full polarization ON; orientation in sdevice.par.
* Thermionic and PooleFrenkel are motivated numerical proxies, NOT
* independently proven to be exactly Wu's interface/trap formulation.
* All 2023-Wu-unverified pilot parameters remain explicitly tentative.
* ======================================================================
File {
  Grid="@tdr@"
  Current="@plot@"
  Plot="@tdrdat@"
  Output="@log@"
  Parameter="@parameter@"
}
Electrode {
  { Name="anode"   Voltage=0.0 }
  { Name="cathode" Voltage=0.0 }
}
Physics {
  Temperature=300.0
  DefaultParametersFromFile
  Fermi
  Mobility( DopingDependence HighFieldSaturation )
  Recombination( SRH Radiative Auger )
  Piezoelectric_Polarization( strain )
  IncompleteIonization( Dopants="MagnesiumActiveConcentration" )
  Thermionic
}
* Check pp*_des.cmd and pp*_des.par, effective GaN/InGaN parameters,
* actual Mg/Si species and crystal orientation before interpreting I-V.

Physics (Region="DmgL_pGaN") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_pGaN") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgL_Barrier0") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_Barrier0") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgL_QW1") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_QW1") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgL_Barrier1") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_Barrier1") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgL_QW2") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_QW2") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgL_Barrier2") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_Barrier2") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgL_QW3") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_QW3") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgL_Barrier3") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_Barrier3") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgL_QW4") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_QW4") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgL_Barrier4") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_Barrier4") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgL_nGaN") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
  )
}

Physics (Region="DmgR_nGaN") {
  Traps(
    (Acceptor Level FromValBand EnergyMid=@TrapEt@
      Conc=@NtSide@ eXsection=@TrapSigmaN@ hXsection=@TrapSigmaP@
      PooleFrenkel)
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
  Digits=5
  ErrRef(Electron)=1e8
  ErrRef(Hole)=1e8
  Iterations=35
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
