#==============================================================================
# CMP Common Baseline - SVisual 2
#
# CURRENT STATUS:
#   This script currently expects n@previous@_des.tdr.
#   As of 2026-09-21, Node 9 SDevice2 finished but that filename was not
#   visible in Node 9 Output Files. See CMP/ERROR_LOG.md before editing.
#==============================================================================

#setdep @previous@

set N @node@
set PREV @previous@
set dname2 n@previous@

set tdrfile n@previous@_des.tdr

puts "============================================================"
puts "CMP Common Baseline - SVisual2"
puts "Current SVisual node : $N"
puts "Previous SDevice node: $PREV"
puts "TDR file             : $tdrfile"
puts "============================================================"

load_file $tdrfile -name $dname2

set plot2D [create_plot \
    -dataset $dname2 \
    -name DefectON]

select_plots $plot2D
