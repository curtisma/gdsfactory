import gdsfactory as gf

c = gf.components.taper2(length=10.0, width1=0.5, width2=3, with_cladding_box=True)
c.plot()