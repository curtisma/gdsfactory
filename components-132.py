import gdsfactory as gf

c = gf.components.ring_single_array(spacing=5.0, list_of_dicts=({'length_x': 10.0, 'radius': 5.0}, {'length_x': 20.0, 'radius': 10.0}))
c.plot()