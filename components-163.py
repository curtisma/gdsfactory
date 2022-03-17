import gdsfactory as gf

c = gf.components.taper_cross_section_sine(length=10, npoints=101, linear=False)
c.plot()