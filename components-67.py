import gdsfactory as gf

c = gf.components.die(size=(10000.0, 10000.0), street_width=100.0, street_length=1000.0, die_name='chip99', text_size=100.0, text_location='SW', layer=(99, 0), bbox_layer=(99, 0), draw_corners=False, draw_dicing_lane=False)
c.plot()