import gdsfactory as gf

c = gf.components.straight_heater_doped_strip(length=320.0, nsections=3, contact_metal_size=(10.0, 10.0), contact_size=(10.0, 10.0), with_taper1=True, with_taper2=True, heater_width=2.0, heater_gap=0.8, contact_gap=0.0, width=0.5, with_top_contact=True, with_bot_contact=True)
c.plot()