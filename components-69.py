import gdsfactory as gf

c = gf.components.die_bbox_frame(bbox=((-1.0, -1.0), (3.0, 4.0)), street_width=100.0, street_length=1000.0, text_size=100.0, text_anchor='sw', layer=(49, 0), padding=10.0)
c.plot()