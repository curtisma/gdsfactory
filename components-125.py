import gdsfactory as gf

c = gf.components.rectangle_with_slits(size=(100.0, 200.0), layer=(1, 0), layer_slit=(2, 0), centered=False, slit_size=(1.0, 1.0), slit_spacing=(20, 20), slit_enclosure=10)
c.plot()