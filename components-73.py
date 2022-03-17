import gdsfactory as gf

c = gf.components.extend_ports(length=5.0, port_type='optical', centered=False)
c.plot()