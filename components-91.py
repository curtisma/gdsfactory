import gdsfactory as gf

c = gf.components.grating_coupler_tm(polarization='tm', fiber_marker_width=11.0, fiber_marker_layer=(204, 0), taper_length=16.6, taper_angle=30.0, trenches_extra_angle=9.0, wavelength=1.53, fiber_angle=15.0, grating_line_width=0.6, wg_width=0.5, neff=1.8, ncladding=1.443, layer=(1, 0), layer_trench=(2, 0), p_start=26, n_periods=30, end_straight_length=0.2)
c.plot()