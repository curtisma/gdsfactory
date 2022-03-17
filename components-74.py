import gdsfactory as gf

c = gf.components.fiber(core_diameter=10, cladding_diameter=125, layer_core=(1, 0), layer_cladding=(111, 0))
c.plot()