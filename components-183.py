import gdsfactory as gf

c = gf.components.viac(size=(0.7, 0.7), spacing=(2.0, 2.0), enclosure=1.0, layer=(40, 0), cladding_offset=0)
c.plot()