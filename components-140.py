import gdsfactory as gf

c = gf.components.spiral_inner_io_fiber_single(x_straight_inner_right=40.0, x_straight_inner_left=75.0, y_straight_inner_top=10.0, y_straight_inner_bottom=0.0, grating_spacing=200.0)
c.plot()