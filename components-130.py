import gdsfactory as gf

c = gf.components.ring_double_heater(gap=0.2, radius=10.0, length_x=0.01, length_y=0.01, port_orientation=90, contact_offset=(0, 0))
c.plot()