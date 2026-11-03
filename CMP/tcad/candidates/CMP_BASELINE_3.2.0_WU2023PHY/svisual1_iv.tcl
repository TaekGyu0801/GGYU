#=============================================================
# CMP_BASELINE_3.2.0_WU2023PHY - SVISUAL1, 10um full 2D
# 2026-11-03 | POSTPROCESS ONLY | SWB T-2022.03
#
# SDE:  Wm = 10.0 um, 2D Cartesian stripe
# SDEV: Current = "@plot@" / anode TotalCurrent
#
# IMPORTANT PHYSICS ASSUMPTION FOR J:
#   2D terminal current reported in A/um (out-of-plane extent)
#   AreaFactor = 1, no extra electrode current scaling
#   J [A/cm2] = abs(I [A/um]) * 1e8 / Wm [um]
#   Wm = 10.0 (NOT old CMP 4.0 um)
#   Verify SDevice current units and AreaFactor before publication.
#
# Does not delete/alter low-voltage or duplicate-V data points.
# Corrected code has NOT been run in target Sentaurus by assistant.
#=============================================================

#setdep @previous@

set N @node@
set NtSide "@NtSide@"
set dname "BaselineData_$N"

# 1) Read SDevice terminal-current plot (PLT)
load_file "@plot@" -name $dname

set Vdata [get_variable_data "anode InnerVoltage" -dataset $dname]
set Idata [get_variable_data "anode TotalCurrent" -dataset $dname]

if {[llength $Vdata] == 0} {
    error "CMP_WU2023PHY SVISUAL1: no anode voltage data"
}
if {[llength $Vdata] != [llength $Idata]} {
    error "CMP_WU2023PHY SVISUAL1: voltage/current data length mismatch"
}

# 2) 10 um geometry width normalization (conditional on raw A/um)
set Wmesa 10.0
set Jdata {}
foreach I $Idata {
    set J [expr {abs(double($I)) * 1.0e8 / $Wmesa}]
    lappend Jdata $J
}
create_variable -name "J_Acm2" -dataset $dname -values $Jdata

# 3) Current vs voltage: keep signed raw current (no smoothing)
set pIV [create_plot -1d -name "WU2023PHY_IV_$N"]
set cIV [create_curve -plot $pIV -dataset $dname \
    -axisX "anode InnerVoltage" -axisY "anode TotalCurrent"]
set_curve_prop $cIV -plot $pIV -line_width 3 -label "NtSide=$NtSide"
set_axis_prop -plot $pIV -axis x -title {Anode Voltage [V]}
set_axis_prop -plot $pIV -axis y -title {Anode Current [A/um] (assumed)}
set_plot_prop -plot $pIV -show_legend -hide_title

# 4) Normalized magnitude of current density vs voltage
set pJV [create_plot -1d -name "WU2023PHY_JV_$N"]
set cJV [create_curve -plot $pJV -dataset $dname \
    -axisX "anode InnerVoltage" -axisY "J_Acm2"]
set_curve_prop $cJV -plot $pJV -line_width 3 -label "NtSide=$NtSide"
set_axis_prop -plot $pJV -axis x -title {Anode Voltage [V]}
set_axis_prop -plot $pJV -axis y -title {Width-normalized |J| [A/cm2] (assumed)}
set_plot_prop -plot $pJV -show_legend -hide_title

# 5) Export exact source data, preserving 0V spike for diagnosis
set csvFile "CMP_WU2023PHY_NtSide_${NtSide}_Node${N}_IVJV.csv"
set fp [open $csvFile w]
puts $fp "Voltage_V,Current_raw_A_per_um_assumed,J_10um_A_per_cm2_assumed"
foreach V $Vdata I $Idata J $Jdata {
    puts $fp [format "%.9g,%.12e,%.12e" $V $I $J]
}
close $fp

export_curves -plot $pIV \
    -filename "CMP_WU2023PHY_IV_Node${N}.csv" -format csv -overwrite
export_curves -plot $pJV \
    -filename "CMP_WU2023PHY_JV_Node${N}.csv" -format csv -overwrite

select_plots [list $pIV $pJV]
puts "CMP_WU10 SVISUAL1: completed plotting for NtSide=$NtSide node=$N"
puts "J normalization: Wmesa=$Wmesa um; requires A/um + AreaFactor=1 verification"
puts "CSV: $csvFile"
#=============================================================
# END
#=============================================================
