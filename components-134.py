import gdsfactory as gf

c = gf.components.ring_single_heater(gap=0.2, radius=10.0, length_x=4.0, length_y=0.6, port_orientation=90, contact_offset=(0, 0))
c.plot()