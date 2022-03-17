import gdsfactory as gf

c = gf.components.verniers(widths=(0.1, 0.2, 0.3, 0.4, 0.5), gap=0.1, xsize=100, layer_label=(201, 0))
c.plot()