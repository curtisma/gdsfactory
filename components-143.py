import gdsfactory as gf

c = gf.components.staircase(length_v=5.0, length_h=5.0, rows=4)
c.plot()