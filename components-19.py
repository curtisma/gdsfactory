import gdsfactory as gf

c = gf.components.bend_port(port_name='e1', port_name2='e2', angle=180)
c.plot()