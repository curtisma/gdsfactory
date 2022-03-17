import gdsfactory as gf

c = gf.components.cutback_bend90(straight_length=5.0, rows=6, columns=6, spacing=5)
c.plot()