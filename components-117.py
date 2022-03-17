import gdsfactory as gf

c = gf.components.pad_array(spacing=(150.0, 150.0), columns=6, rows=1, orientation=270)
c.plot()