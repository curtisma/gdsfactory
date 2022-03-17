import gdsfactory as gf

c = gf.components.cutback_bend180(straight_length=5.0, rows=6, columns=6, spacing=3)
c.plot()