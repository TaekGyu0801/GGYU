# ============================================================
# CMP_BASELINE_3.3.1_GPTD50 | SVisual map (PROPOSED/UNRUN)
# Wire SVisual2 DIRECTLY after SDevice, not after SVisual1.
# Requires n@previous@_des.tdr from the preceding SDevice.
# Actual school-final SVisual remains UNKNOWN.
# ============================================================
#setdep @previous@
set N @node@
set PREV @previous@
set ds "GPTD50_Map_$N"
set tdrfile "n${PREV}_des.tdr"
puts "GPTD50 SVisual map, node=$N, source=$tdrfile"
if {![file exists $tdrfile]} {
    error "GPTD50 SVisual2: missing TDR file $tdrfile; check preceding SDevice Plot and SWB edge"
}
load_file $tdrfile -name $ds
set p2 [create_plot -dataset $ds -name "GPTD50_2D_$N"]
select_plots $p2
puts "GPTD50 SVisual2 map dataset loaded: $ds"
