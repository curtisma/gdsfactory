import gdsfactory as gf

c = gf.components.array_with_via(columns=3, spacing=150.0, via_spacing=10.0, straight_length=60.0, contact_dy=0, port_orientation=180)
c.plot()