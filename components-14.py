import gdsfactory as gf

c = gf.components.bend_circular180(angle=180, npoints=720, with_cladding_box=True)
c.plot()