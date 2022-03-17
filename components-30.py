import gdsfactory as gf

c = gf.components.contact(size=(11.0, 11.0), layers=((41, 0), (45, 0), (49, 0)))
c.plot()