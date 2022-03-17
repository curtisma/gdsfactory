import gdsfactory as gf

c = gf.components.taper_parabolic(length=20, width1=0.5, width2=5.0, exp=0.5, npoints=100, layer=(1, 0))
c.plot()