import gdsfactory as gf

c = gf.components.straight_pin_slot(length=500.0, contact_width=10.0, contact_spacing=3.0, contact_slab_spacing=2.0)
c.plot()