import gdsfactory as gf

c = gf.components.bend_circular(angle=90.0, npoints=720, with_cladding_box=True)
c.plot()