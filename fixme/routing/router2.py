"""
This router could save more routing space leveraging routing with different metal layers

"""

import gdsfactory as gf
from gdsfactory.components.extend_ports_list import extend_ports_list
from gdsfactory.components.contact import contact_heater_m3
from gdsfactory.routing.sort_ports import sort_ports


if __name__ == "__main__":
    ncols = 8
    nrows = 16
    N = ncols * nrows
    with_pads = False
    with_pads = True
    pad_pitch = 150.0
    metal_width = 5.0
    metal_spacing = 10.0
    length = 200
    metal_layer = gf.LAYER.M2
    name = "problem3.gds"
    name = "solution3.gds"

    c = gf.Component(name=name)
    ps = gf.components.straight_heater_metal()
    ps_array = gf.components.array(component=ps, spacing=(0, 20), columns=1, rows=2)
    dy = 100

    splitter = gf.components.splitter_tree(noutputs=N, spacing=(80, dy))
    splitters = c.add_ref(splitter)
    splitters.movey(-30)
    splitters.xmax = 0

    extension_factory = gf.partial(
        gf.components.straight_heater_metal,
        length=length,
        port_orientation1=180,
        port_orientation2=0,
        contact=contact_heater_m3,
    )

    ps = c << extend_ports_list(
        ports=splitters.get_ports_list(orientation=0),
        extension_factory=extension_factory,
    )

    if with_pads:
        pads = c << gf.components.array_with_fanout_2d(
            columns=ncols * 2,
            rows=nrows,
            pitch=pad_pitch,
            width=metal_width,
            waveguide_pitch=metal_spacing,
            cross_section=gf.cross_section.metal2,
        )
        pads.rotate(180)
        pads.y = 15

        pads.xmax = ps.xmin - 2500

        routes_bend180 = gf.routing.get_routes_bend180(
            ports=ps.get_ports_list(port_type="electrical", orientation=0),
            radius=dy / 8,
            width=metal_width,
            layer=metal_layer,
        )
        c.add(routes_bend180.references)

        ports1 = ps.get_ports_list(port_type="electrical", orientation=180) + list(
            routes_bend180.ports
        )
        ports2 = pads.get_ports_list()
        ports1, ports2 = sort_ports(ports1, ports2)
        for i, p in enumerate(ports1):
            p.name = f"e{i+1}"
        for port1, port2 in zip(ports1, ports2):
            c.add_label(position=port1.midpoint, text=port1.name)
            c.add_label(position=port2.midpoint, text=port1.name)

        metal_routes = gf.routing.get_bundle_electrical(
            ports1,
            ports2,
            width=metal_width,
            separation=metal_spacing,
            layer=metal_layer,
        )
        if name.startswith("solution"):
            for metal_route in metal_routes:
                c.add(metal_route.references)

    c.write_gds(name)
    c.show()
