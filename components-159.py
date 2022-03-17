import gdsfactory as gf

c = gf.components.taper(length=10.0, width1=0.5, with_cladding_box=True)
c.plot()