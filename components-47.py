import gdsfactory as gf

c = gf.components.cross(length=10.0, width=3.0, layer=(1, 0))
c.plot()