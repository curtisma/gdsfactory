import gdsfactory as gf

c = gf.components.mzi_pads_center(length_x=500, length_y=40, mzi_sig_top='e3', mzi_gnd_top='e2', mzi_sig_bot='e1', mzi_gnd_bot='e4', pad_sig_bot='e1_1_1', pad_sig_top='e3_1_3', pad_gnd_bot='e4_1_2', pad_gnd_top='e2_1_2', delta_length=40.0, end_straight_length=5, start_straight_length=5, metal_route_width=10)
c.plot()