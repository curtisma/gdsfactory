import gdsfactory as gf

c = gf.components.spiral_external_io(N=6, x_inner_length_cutback=300.0, x_inner_offset=0.0, y_straight_inner_top=0.0, xspacing=3.0, yspacing=3.0)
c.plot()