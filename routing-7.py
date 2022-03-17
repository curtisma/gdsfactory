import numpy as np
import gdsfactory as gf


@gf.cell
def test_connect_bundle_waypoints():
    """Connect bundle of ports with bundle of routes following a list of waypoints."""
    xs1 = np.arange(10) * 5 - 500.0
    N = xs1.size
    ys2 = np.array([0, 5, 10, 20, 25, 30, 40, 55, 60, 75]) + 500.0

    ports1 = [gf.Port(f"A_{i}", (xs1[i], 0), 0.5, 90) for i in range(N)]
    ports2 = [gf.Port(f"B_{i}", (0, ys2[i]), 0.5, 180) for i in range(N)]

    c = gf.Component()
    waypoints = [
        ports1[0].position + (0, 100),
        ports1[0].position + (200, 100),
        ports1[0].position + (200, -200),
        ports1[0].position + (0, -200),
        ports1[0].position + (0, -350),
        ports1[0].position + (400, -350),
        (ports1[0].x + 400, ports2[0].y),
    ]

    routes = gf.routing.get_bundle_from_waypoints(ports1, ports2, waypoints)
    for route in routes:
        c.add(route.references)

    return c

cell = test_connect_bundle_waypoints()
cell.plot()