import gdsfactory as gf

c = gf.components.coupler_symmetric(gap=0.234, dy=5.0, dx=10.0)
c.plot()