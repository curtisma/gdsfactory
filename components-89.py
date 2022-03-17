import gdsfactory as gf

c = gf.components.grating_coupler_rectangular_arbitrary_slab(gaps=(0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2), widths=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5), wg_width=0.5, width_grating=11.0, length_taper=150.0, layer=(1, 0), polarization='te', wavelength=1.55, layer_slab=(2, 0), slab_offset=2.0)
c.plot()