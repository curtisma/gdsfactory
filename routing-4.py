import gdsfactory as gf

c = gf.Component("get_route_from_steps_sample")
w = gf.components.straight()
left = c << w
right = c << w
right.move((100, 80))

obstacle = gf.components.rectangle(size=(100, 10), port_type=None)
obstacle1 = c << obstacle
obstacle2 = c << obstacle
obstacle1.ymin = 40
obstacle2.xmin = 25

p1 = left.ports['o2']
p2 = right.ports['o2']
route = gf.routing.get_route_from_steps(
    port1=p1,
    port2=p2,
    steps=[
        {"x": 20},
        {"y": 20},
        {"x": 120},
        {"y": 80},
    ],
)
c.add(route.references)
c.plot()
c.show()