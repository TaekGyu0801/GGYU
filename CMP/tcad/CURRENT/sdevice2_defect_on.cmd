#==============================================================================
# CMP Common Baseline - SDevice 2
# SIDEWALL DEFECT ON
#==============================================================================

File {
  Grid       = "@tdr@"
  Parameters = "@parameter@"
  Plot       = "@tdrdat@"
  Current    = "@plot@"
  Output     = "@log@"
}

Electrode {
  { Name = "anode"   Voltage = 0.0 }
  { Name = "cathode" Voltage = 0.0 }
}

Physics {
  Temperature = 300.0
  Fermi
  Piezoelectric_Polarization(strain)
  DefaultParametersFromFile

  EffectiveIntrinsicDensity(
    NoBandgapNarrowing
  )

  Recombination (
    SRH()
    Auger()
    Radiative
  )

  Mobility (
    DopingDependence(
      Masetti
    )
    HighFieldSaturation(
      CaugheyThomas
    )
    Enormal(
      Lombardi
    )
  )

  IncompleteIonization

  Aniso (
    Poisson
    direction(SimulationSystem) = (1 0 0)
  )
}

#==============================================================================
# SIDEWALL DEFECT MODEL
# Nt = 1e18 cm^-3
# Et = Ev + 0.75 eV
# sigma_n = sigma_p = 1e-15 cm^2
#==============================================================================

Physics (Region="DmgL_pGaN") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_pGaN") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_EBL") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_EBL") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_Barrier0") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_Barrier0") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_QW1") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_QW1") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_Barrier1") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_Barrier1") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_QW2") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_QW2") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_Barrier2") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_Barrier2") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_QW3") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_QW3") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_Barrier3") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_Barrier3") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_QW4") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_QW4") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_Barrier4") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_Barrier4") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

Physics (Region="DmgL_nGaN") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}
Physics (Region="DmgR_nGaN") {
  Traps ((
    Acceptor
    Conc = 1e18
    Level
    FromValBand
    EnergyMid = 0.75
    eXsection = 1e-15
    hXsection = 1e-15
  ))
}

#==============================================================================
# OUTPUT VARIABLES
# NOTE:
# SRHRecombination is present in this deck, but it did not appear in one
# observed SVisual scalar list. Do not rename output keywords by guess.
#==============================================================================

Plot {
  Potential
  eQuasiFermi
  hQuasiFermi
  eDensity
  hDensity
  SpaceCharge

  SRHRecombination
  RadiativeRecombination
  AugerRecombination
  TotalRecombination

  Current
  eCurrent
  hCurrent
  CurrentPotential

  ElectricField
  SemiconductorElectricField
  InsulatorElectricField

  eMobility
  hMobility
  eVelocity
  hVelocity

  Doping
  DonorConcentration
  AcceptorConcentration

  PE_Polarization/vector
  PE_Charge
  PiezoCharge

  ConductionBandEnergy
  ValenceBandEnergy
  ElectronAffinity
  BandGap
  EffectiveBandGap
  BandGapNarrowing
  QCEffectiveBandGap

  xMolefraction
  yMolefraction
}

Math {
  NumberOfThreads = 4
  ParallelLicense(Wait)
  Wallclock

  Digits = 5
  ErrRef(electron) = 1.0e4
  ErrRef(hole) = 1.0e4
  RHSMin = 1e-3
  CheckRhsAfterUpdate

  Transient = BE
  ExtendedPrecision(80)
  TensorGridAniso(aniso)

  ComputeDopingConcentration

  Method = Blocked
  SubMethod = ILS(set=22)

  ILSrc = "
    set(22) {
      iterative(
        gmres(100),
        tolrel=1e-10,
        tolunprec=1e-4,
        maxit=200
      );
      preconditioning(
        ilut(1e-08,-1),
        left
      );
      ordering(
        symmetric=nd,
        nonsymmetric=mpsilst
      );
      options(
        verbose=0,
        refineresidual=10
      );
    };
  "
}

Solve {
  Coupled(
    Iterations = 500
    LineSearchDamping = 1e-2
  ) {
    Poisson
  }

  Coupled(
    Iterations = 100
  ) {
    Poisson
    Electron
    Hole
  }

  Transient(
    InitialStep = 1e-5
    MinStep = 1e-9
    MaxStep = 1e-3
    Increment = 1.2

    Goal {
      Name = "anode"
      Voltage = 5.0
    }
  ) {
    Coupled {
      Poisson
      Electron
      Hole
    }
  }
}
