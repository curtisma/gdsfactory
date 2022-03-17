import gdsfactory as gf

c = gf.components.array_with_via_2d(spacing=(150.0, 150.0), columns=3, rows=2)
c.plot()