import gdsfactory as gf

@gf.cell
def test_north_to_south():
    dy = 200.0
    xs1 = [-500, -300, -100, -90, -80, -55, -35, 200, 210, 240, 500, 650]

    pitch = 10.0
    N = len(xs1)
    xs2 = [-20 + i * pitch for i in range(N // 2)]
    xs2 += [400 + i * pitch for i in range(N // 2)]

    a1 = 90
    a2 = a1 + 180

    ports1 = [gf.Port("top_{}".format(i), (xs1[i], 0), 0.5, a1) for i in range(N)]
    ports2 = [gf.Port("bottom_{}".format(i), (xs2[i], dy), 0.5, a2) for i in range(N)]

    c = gf.Component()
    routes = gf.routing.get_bundle(ports1, ports2)
    for route in routes:
        c.add(route.references)

    return c


c = test_north_to_south()
c.show()
c.plot()