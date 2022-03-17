import gdsfactory as gf

c = gf.Component('sample_connect')
mmi1 = c << gf.components.mmi1x2()
mmi2 = c << gf.components.mmi1x2()
mmi2.move((40, 20))
route = gf.routing.get_route(mmi1.ports["o2"], mmi2.ports["o1"], radius=5)
c.add(route.references)
c.plot()