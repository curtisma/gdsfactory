import gdsfactory as gf

c = gf.components.copy_layers(layers=((1, 0), (2, 0)))
c.plot()