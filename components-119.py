import gdsfactory as gf

c = gf.components.pad_gsg_short(size=(22, 7), layer_metal=(49, 0), metal_spacing=5.0, short=True, pad_spacing=150)
c.plot()