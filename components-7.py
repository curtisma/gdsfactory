import gdsfactory as gf

c = gf.components.array_with_fanout(columns=3, pitch=150.0, waveguide_pitch=10.0, start_straight_length=5.0, end_straight_length=40.0, radius=5.0, component_port_name='e4')
c.plot()