import gdsfactory as gf

c = gf.components.compass(size=(4.0, 2.0), layer=(1, 0), port_type='electrical', port_inclusion=0.0)
c.plot()