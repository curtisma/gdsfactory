"""Extract netlist from component port connectivity.
Assumes two ports are connected when they have same width, x, y

.. code:: yaml

    connections:
        - coupler,N0:bendLeft,W0
        - coupler,N1:bendRight,N0
        - bednLeft,N0:straight,W0
        - bendRight,N0:straight,E0

    ports:
        - coupler,E0
        - coupler,W0

"""

from typing import Tuple

import omegaconf

from gdsfactory.component import Component, ComponentReference
from gdsfactory.name import clean_name
from gdsfactory.snap import snap_to_grid
from gdsfactory.tech import LAYER


def get_instance_name(
    component: Component,
    reference: ComponentReference,
    layer_label: Tuple[int, int] = LAYER.LABEL_INSTANCE,
) -> str:
    """Returns the instance name from the label.
    If no label returns to instanceName_x_y

    Args:
        component: with labels
        reference: reference that needs naming
        layer_label: ignores layer_label[1]
    """

    x = snap_to_grid(reference.x)
    y = snap_to_grid(reference.y)
    labels = component.labels

    # default instance name follows componetName_x_y
    text = clean_name(f"{reference.parent.name}_{x}_{y}")

    # text = f"{reference.parent.name}_X{int(x)}_Y{int(y)}"
    # text = f"{reference.parent.name}_{reference.uid}"

    # try to get the instance name from a label
    for label in labels:
        xl = snap_to_grid(label.position[0])
        yl = snap_to_grid(label.position[1])
        if x == xl and y == yl and label.layer == layer_label[0]:
            # print(label.text, xl, yl, x, y)
            return label.text

    return text


def get_netlist(
    component: Component,
    layer_label: Tuple[int, int] = LAYER.LABEL_INSTANCE,
    tolerance: int = 1,
) -> omegaconf.DictConfig:
    """From a component returns instances, connections and placements dict. It
    assumes that ports with same width, x, y are connected.

     Args:
         component: to Extract netlist
         layer_label: label to read instanceNames from (if any)
         tolerance: tolerance in nm to consider two ports the same

     Returns:
         connections: Dict of Instance1Name,portName: Instace2Name,portName
         instances: Dict of instances and settings
         placements: Dict of instances and placements (x, y, rotation)
         port: Dict portName: CompoentName,port
         name: name of component

    """
    placements = {}
    instances = {}
    connections = {}
    top_ports = {}

    for reference in component.references:
        c = reference.parent
        origin = reference.origin
        x = float(snap_to_grid(origin[0]))
        y = float(snap_to_grid(origin[1]))
        reference_name = get_instance_name(
            component, reference, layer_label=layer_label
        )

        instances[reference_name] = c.metadata
        instances[reference_name]["info"] = c.info

        placements[reference_name] = dict(
            x=x,
            y=y,
            rotation=int(reference.rotation),
            mirror=reference.x_reflection,
        )

    # store where ports are located
    name2port = {}

    # Initialize a dict of port locations to Instance1Name,PortNames
    port_locations = {}

    # TOP level ports
    ports = component.get_ports(depth=0)
    top_ports_list = set()
    for port in ports:
        src = port.name
        name2port[src] = port
        top_ports_list.add(src)

    # lower level ports
    for reference in component.references:
        for port in reference.ports.values():
            reference_name = get_instance_name(
                component, reference, layer_label=layer_label
            )
            src = f"{reference_name},{port.name}"
            name2port[src] = port

    # build connectivity port_locations = Dict[Tuple(x,y,width), set of portNames]
    for name, port in name2port.items():
        xyw = tuple(
            round(1000 * v)
            for v in snap_to_grid((port.x, port.y, port.width), nm=tolerance)
        )
        if xyw not in port_locations:
            port_locations[xyw] = set()
        port_locations[xyw].add(name)

    for xyw, names_set in port_locations.items():
        if len(names_set) > 2:
            x, y, w = (v / 1000 for v in xyw)
            raise ValueError(
                f"more than 2 connections at {x, y} {list(names_set)}, width  = {w} "
            )
        if len(names_set) == 2:
            names_list = list(names_set)
            src = names_list[0]
            dst = names_list[1]
            if src in top_ports_list:
                top_ports[src] = dst
            elif dst in top_ports_list:
                top_ports[dst] = src
            else:
                src_dest = sorted([src, dst])
                connections[src_dest[0]] = src_dest[1]

    connections_sorted = {k: connections[k] for k in sorted(list(connections.keys()))}
    placements_sorted = {k: placements[k] for k in sorted(list(placements.keys()))}
    instances_sorted = {k: instances[k] for k in sorted(list(instances.keys()))}
    return omegaconf.DictConfig(
        dict(
            connections=connections_sorted,
            instances=instances_sorted,
            placements=placements_sorted,
            ports=top_ports,
            name=component.name,
        )
    )


def demo_ring_single_array() -> None:
    import gdsfactory as gf

    c = gf.components.ring_single_array()
    c.get_netlist()


def demo_mzi_lattice() -> None:
    import gdsfactory as gf

    coupler_lengths = [10, 20, 30, 40]
    coupler_gaps = [0.1, 0.2, 0.4, 0.5]
    delta_lengths = [10, 100, 200]

    c = gf.components.mzi_lattice(
        coupler_lengths=coupler_lengths,
        coupler_gaps=coupler_gaps,
        delta_lengths=delta_lengths,
    )
    c.get_netlist()
    print(c.get_netlist_yaml())


if __name__ == "__main__":
    from pprint import pprint

    from omegaconf import OmegaConf

    import gdsfactory as gf
    from gdsfactory.tests.test_component_from_yaml import sample_2x2_connections

    c = gf.read.from_yaml(sample_2x2_connections)
    c = gf.components.ring_single()
    c.show()
    pprint(c.get_netlist())

    n = c.get_netlist()
    yaml_str = OmegaConf.to_yaml(n, sort_keys=True)
    c2 = gf.read.from_yaml(yaml_str)
    gf.show(c2)
