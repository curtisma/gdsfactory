import gdsfactory as gf

c = gf.components.straight_rib_tapered(length=5.0, port1='o2', port2='o1', port_type='optical', centered=False)
c.plot()