import gdsfactory as gf

c = gf.components.fiber_array(n=8, pitch=127.0, core_diameter=10, cladding_diameter=125, layer_core=(1, 0), layer_cladding=(111, 0))
c.plot()