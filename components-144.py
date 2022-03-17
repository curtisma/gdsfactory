import gdsfactory as gf

c = gf.components.straight(length=10.0, npoints=2, with_cladding_box=True)
c.plot()