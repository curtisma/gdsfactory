import gdsfactory as gf

c = gf.components.cutback_component(cols=4, rows=5, radius=5.0, port1='o1', port2='o2', mirror=False)
c.plot()