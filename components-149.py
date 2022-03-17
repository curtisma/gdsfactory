import gdsfactory as gf

c = gf.components.straight_heater_metal(length=320.0, length_undercut_spacing=6.0, length_undercut=30.0, length_straight_input=15.0, heater_width=2.5, with_undercut=False, port_orientation1=180, port_orientation2=0, heater_taper_length=5.0)
c.plot()