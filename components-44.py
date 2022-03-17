import gdsfactory as gf

c = gf.components.coupler_ring(gap=0.2, radius=5.0, length_x=4.0)
c.plot()