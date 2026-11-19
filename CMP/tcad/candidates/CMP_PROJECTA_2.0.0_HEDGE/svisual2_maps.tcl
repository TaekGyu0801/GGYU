# ============================================================
# CMP_PROJECTA_2.0.0_HEDGE | SVisual map (PROPOSED/UNRUN)
# Wire SVisual2 DIRECTLY after SDevice, not after SVisual1.
# Requires n@previous@_des.tdr from the preceding SDevice.
# Actual school-final SVisual remains UNKNOWN.
# ============================================================
#setdep @previous@
set N @node@
set PREV @previous@
set ds "PROJECTA_HEDGE_Map_$N"
set tdrfile "n${PREV}_des.tdr"
puts "PROJECTA_HEDGE SVisual map, node=$N, source=$tdrfile"
if {![file exists $tdrfile]} {
    error "PROJECTA_HEDGE SVisual2: missing TDR file $tdrfile; check preceding SDevice Plot and SWB edge"
}
load_file $tdrfile -name $ds
set p2 [create_plot -dataset $ds -name "PROJECTA_HEDGE_2D_$N"]
select_plots $p2
puts "PROJECTA_HEDGE SVisual2 map dataset loaded: $ds"
