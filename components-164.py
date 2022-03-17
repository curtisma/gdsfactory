import gdsfactory as gf

c = gf.components.taper_from_csv(layer=(1, 0), layer_cladding=(111, 0), cladding_offset=3.0)
c.plot()