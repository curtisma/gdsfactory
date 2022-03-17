import gdsfactory as gf

c = gf.components.L(width=1, size=(10, 20), layer=(49, 0), port_type='electrical')
c.plot()