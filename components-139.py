import gdsfactory as gf

c = gf.components.spiral_inner_io(N=6, x_straight_inner_right=150.0, x_straight_inner_left=50.0, y_straight_inner_top=50.0, y_straight_inner_bottom=10.0, grating_spacing=127.0, waveguide_spacing=3.0)
c.plot()