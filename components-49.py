import gdsfactory as gf

c = gf.components.crossing45(port_spacing=40.0, alpha=0.08, npoints=101)
c.plot()