import gdsfactory as gf

c = gf.components.die_bbox(street_width=100.0, street_length=1000.0, text_size=100.0, text_anchor='sw', layer=(49, 0), padding=10.0)
c.plot()