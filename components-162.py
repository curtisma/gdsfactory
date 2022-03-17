import gdsfactory as gf

c = gf.components.taper_cross_section_linear(length=10, npoints=2, linear=True)
c.plot()