import gdsfactory as gf

c = gf.components.text_rectangular_multi_layer(text='abcd', layers=((1, 0), (41, 0), (45, 0), (49, 0)))
c.plot()