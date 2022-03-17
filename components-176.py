import gdsfactory as gf

c = gf.components.triangle(x=10, xtop=0, y=20, ybot=0, layer=(1, 0))
c.plot()