import gdsfactory as gf

c = gf.components.ring(radius=10.0, width=0.5, angle_resolution=2.5, layer=(1, 0))
c.plot()