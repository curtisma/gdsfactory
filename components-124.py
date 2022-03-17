import gdsfactory as gf

c = gf.components.rectangle(size=(4.0, 2.0), layer=(1, 0), centered=False, port_type='electrical')
c.plot()