import gdsfactory as gf

c = gf.components.grating_coupler_elliptical_tm(polarization='tm', taper_length=30, taper_angle=40.0, wavelength=1.554, fiber_angle=15.0, grating_line_width=0.707, wg_width=0.5, neff=1.8, nclad=1.443, layer=(1, 0), n_periods=16, big_last_tooth=False, layer_slab=(2, 0), slab_xmin=-2, slab_offset=2.0, fiber_marker_width=11.0, fiber_marker_layer=(204, 0), spiked=True)
c.plot()