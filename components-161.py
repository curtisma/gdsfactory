import gdsfactory as gf

c = gf.components.taper_0p5_to_3_l36(layer=(1, 0), layer_cladding=(111, 0), cladding_offset=3.0)
c.plot()