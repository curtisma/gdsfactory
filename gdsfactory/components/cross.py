from typing import Optional, Tuple

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.tech import LAYER


@gf.cell
def cross(
    length: float = 10.0,
    width: float = 3.0,
    layer: Tuple[int, int] = LAYER.WG,
    port_type: Optional[str] = None,
) -> Component:
    """Returns a cross from two rectangles of length and width.

    Args:
        length: float Length of the cross from one end to the other
        width: float Width of the arms of the cross
        layer: layer for geometry
        port_type:

    """
    c = gf.Component()
    R = gf.components.rectangle(size=(width, length), layer=layer)
    r1 = c.add_ref(R).rotate(90)
    r2 = c.add_ref(R)
    r1.center = (0, 0)
    r2.center = (0, 0)

    if port_type:
        c.add_port(
            1,
            width=width,
            layer=layer,
            orientation=0,
            midpoint=(+length / 2, 0),
            port_type=port_type,
        )
        c.add_port(
            2,
            width=width,
            layer=layer,
            orientation=180,
            midpoint=(-length / 2, 0),
            port_type=port_type,
        )
        c.add_port(
            3,
            width=width,
            layer=layer,
            orientation=90,
            midpoint=(0, length / 2),
            port_type=port_type,
        )
        c.add_port(
            4,
            width=width,
            layer=layer,
            orientation=270,
            midpoint=(0, -length / 2),
            port_type=port_type,
        )
        c.auto_rename_ports()
    return c


if __name__ == "__main__":
    c = cross()
    c.show()
    # c.pprint_ports()
    # cc = gf.routing.add_fiber_array(component=c)
    # cc.show()
