import gdsfactory as gf

c = gf.components.text_rectangular(text='abcd', size=10.0, position=(0.0, 0.0), justify='left', layer=(1, 0))
c.plot()