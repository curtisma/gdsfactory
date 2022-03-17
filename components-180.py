import gdsfactory as gf

c = gf.components.via1(size=(0.7, 0.7), spacing=(2.0, 2.0), enclosure=2, layer=(44, 0), cladding_offset=0)
c.plot()