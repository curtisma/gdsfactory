import gdsfactory as gf

c = gf.components.wire_straight(length=10.0, npoints=2, with_cladding_box=False)
c.plot()