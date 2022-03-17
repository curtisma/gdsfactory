import gdsfactory as gf

c = gf.components.litho_calipers(notch_size=(2.0, 5.0), notch_spacing=2.0, num_notches=11, offset_per_notch=0.1, row_spacing=0.0, layer1=(1, 0), layer2=(2, 0))
c.plot()