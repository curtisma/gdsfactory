import gdsfactory as gf

c = gf.components.add_frame(width=10.0, spacing=10.0, layer=(1, 0))
c.plot()