#==============================================================================
# CMP Common Baseline - SVisual 1
# Electrical validation / Forward I-V
#==============================================================================

#setdep @previous@

set N @node@
set dname1 n@previous@

load_file @plot@ -name $dname1

if {[lsearch [list_plots] IaVac] == -1} {

    create_plot -1d -name IaVac

    set_plot_prop \
        -plot IaVac \
        -hide_title \
        -hide_legend

    set_axis_prop \
        -plot IaVac \
        -title_font_size 20 \
        -scale_font_size 14

    set_axis_prop \
        -plot IaVac \
        -axis x \
        -title {Anode Voltage [V]}

    set_axis_prop \
        -plot IaVac \
        -axis y \
        -title {Anode TotalCurrent [raw 2D output]}

    select_plots {IaVac}
}

create_curve \
    -name IV($N) \
    -plot IaVac \
    -dataset "$dname1" \
    -axisX {anode InnerVoltage} \
    -axisY {anode TotalCurrent}

set_curve_prop \
    IV($N) \
    -plot IaVac \
    -label "Node $N"

# fit_plot intentionally not used in T-2022.03.
