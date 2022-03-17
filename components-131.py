import gdsfactory as gf

c = gf.components.ring_single(gap=0.2, radius=10.0, length_x=4.0, length_y=0.6)
c.plot()