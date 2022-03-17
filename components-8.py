import gdsfactory as gf

c = gf.components.array_with_fanout_2d(pitch=150.0, columns=3, rows=2)
c.plot()