import gdsfactory as gf

c = gf.components.pads_shorted(columns=8, pad_spacing=150.0, layer_metal=(49, 0), metal_width=10)
c.plot()