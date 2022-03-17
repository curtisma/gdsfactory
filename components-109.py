import gdsfactory as gf

c = gf.components.mzi_lattice(coupler_lengths=(10.0, 20.0), coupler_gaps=(0.2, 0.3), delta_lengths=(10.0,))
c.plot()