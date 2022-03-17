import gdsfactory as gf

c = gf.components.straight_heater_metal_90_90(length=320.0, length_undercut_spacing=6.0, length_undercut=30.0, length_straight_input=15.0, heater_width=2.5, with_undercut=False, port_orientation1=90, port_orientation2=90, heater_taper_length=5.0)
c.plot()