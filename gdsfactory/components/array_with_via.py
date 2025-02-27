from typing import Optional

import numpy as np

from gdsfactory.cell import cell
from gdsfactory.component import Component
from gdsfactory.components.array_component import array
from gdsfactory.components.contact import contact as contact_factory
from gdsfactory.components.pad import pad
from gdsfactory.components.straight import straight
from gdsfactory.cross_section import metal2
from gdsfactory.types import (
    ComponentFactory,
    ComponentOrFactory,
    CrossSectionFactory,
    Float2,
)


@cell
def array_with_via(
    component: ComponentOrFactory = pad,
    columns: int = 3,
    spacing: float = 150.0,
    via_spacing: float = 10.0,
    straight_length: float = 60.0,
    cross_section: Optional[CrossSectionFactory] = metal2,
    contact: ComponentFactory = contact_factory,
    contact_dy: float = 0,
    port_orientation: float = 180,
    port_offset: Optional[Float2] = None,
    **kwargs,
) -> Component:
    """Returns an array of components in X axis
    with fanout waveguides facing west

    Args:
        component: to replicate in the array
        columns: number of components
        spacing: for the array
        via_spacing: for fanout
        straight_length: lenght of the straight at the end
        waveguide: waveguide definition
        cross_section:
        contact:
        contact_dy: contact offset
        port_orientation: 180: facing west
        port_offset: Optional port movement
        kwargs: cross_section settings
    """

    c = Component()
    component = component() if callable(component) else component
    contact = contact()

    for col in range(columns):
        ref = component.ref()
        ref.x = col * spacing
        c.add(ref)

        if port_orientation == 180:
            xlength = col * spacing + straight_length
        elif port_orientation == 0:
            xlength = columns * spacing - (col * spacing) + straight_length
        elif port_orientation == 270:
            xlength = col * via_spacing + straight_length

        elif port_orientation == 90:
            xlength = columns * via_spacing - (col * via_spacing) + straight_length

        else:
            raise ValueError(
                f"Invalid port_orientation = {port_orientation}",
                "180: west, 0: east, 90: north, 270: south",
            )

        contact_ref = c << contact
        contact_ref.x = col * spacing
        contact_ref.y = col * via_spacing + contact_dy

        if cross_section:
            port_name = f"e{col}"
            straightx_ref = c << straight(
                length=xlength, cross_section=cross_section, **kwargs
            )
            straightx_ref.connect(
                "e2", contact_ref.get_ports_list(orientation=port_orientation)[0]
            )
            c.add_port(port_name, port=straightx_ref.ports["e1"])
            if port_offset:
                c.ports[port_name].move(np.array(port_offset) * col)
    return c


@cell
def array_with_via_2d(
    spacing: Float2 = (150.0, 150.0),
    columns: int = 3,
    rows: int = 2,
    **kwargs,
) -> Component:
    """Returns 2D array with fanout waveguides facing west.

    Args:
        spacing: 2D spacing
        columns:
        rows:
        kwargs:
            component: to replicate
            columns: number of components
            spacing: float
            via_spacing: for fanout
            straight_length: lenght of the straight at the end
            contact_port_name:
            **kwargs
    """
    row = array_with_via(columns=columns, spacing=spacing[0], **kwargs)
    return array(component=row, rows=rows, columns=1, spacing=(0, spacing[1]))


if __name__ == "__main__":
    import gdsfactory as gf

    contact_big = gf.partial(contact_factory, size=(30, 20))
    # c = array_with_via(columns=3, width=10, via_spacing=20, port_orientation=90)
    c = array_with_via_2d(
        columns=2,
        rows=3,
        via_spacing=27.3,
        spacing=(150, 218),
        port_orientation=270,
        straight_length=0,
        contact=contact_big,
        contact_dy=-50 + 10,
        port_offset=(0, 10),
    )
    # c.auto_rename_ports()
    c.show()
