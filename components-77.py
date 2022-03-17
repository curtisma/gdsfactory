import gdsfactory as gf

c = gf.components.grating_coupler_circular(taper_angle=30.0, taper_length=10.0, length=30.0, period=1.0, fill_factor=0.7, n_periods=30, bias_gap=0, port=(0.0, 0.0), layer=(1, 0), layer_cladding=(111, 0), direction='EAST', polarization='te', wavelength=1.55, fiber_marker_width=11.0, fiber_marker_layer=(203, 0), wg_width=0.5, cladding_offset=2.0)
c.plot()