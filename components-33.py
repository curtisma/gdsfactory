import gdsfactory as gf

c = gf.components.contact_slot(size=(11.0, 11.0), layers=((41, 0), (45, 0)), layer_offsets=(0, 1.0), enclosure=1.0, ysize=0.5, yspacing=2.0)
c.plot()