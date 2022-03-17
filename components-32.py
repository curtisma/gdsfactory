import gdsfactory as gf

c = gf.components.contact_slab_m3(size=(11.0, 11.0), layers=((3, 0), (41, 0), (45, 0), (49, 0)))
c.plot()