import gdsfactory as gf

c = gf.components.pad(size=(100.0, 100.0), layer=(49, 0), port_inclusion=0)
c.plot()