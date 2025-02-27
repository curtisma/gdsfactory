import phidl.geometry as pg

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.geometry.boolean import boolean
from gdsfactory.types import Int2, Layer, Union


@gf.cell
def invert(
    elements,
    border: float = 10.0,
    precision: float = 1e-4,
    num_divisions: Union[int, Int2] = (1, 1),
    max_points: int = 4000,
    layer: Layer = (1, 0),
):
    """Creates an inverted version of the input shapes with an additional
    border around the edges. adapted from phidl.geometry.invert

    Args:
        elements : Component(/Reference), list of Component(/Reference), or Polygon
            A Component containing the polygons to invert.
        border : int or float
            Size of the border around the inverted shape (border value is the
            distance from the edges of the boundary box defining the inverted
            shape to the border, and is applied to all 4 sides of the shape).
        precision : float
            Desired precision for rounding vertex coordinates.
        num_divisions : array-like[2] of int
            The number of divisions with which the geometry is divided into
            multiple rectangular regions. This allows for each region to be
            processed sequentially, which is more computationally efficient.
        max_points : int
            The maximum number of vertices within the resulting polygon.
        layer : int, array-like[2], or set
            Specific layer(s) to put polygon geometry on.

    Returns
        D: A Component containing the inverted version of the input shape(s) and the
        corresponding border(s).
    """
    Temp = Component()
    if type(elements) is not list:
        elements = [elements]
    for e in elements:
        if isinstance(e, Component):
            Temp.add_ref(e)
        else:
            Temp.add(e)
    gds_layer, gds_datatype = pg._parse_layer(layer)

    # Build the rectangle around the Component D
    R = gf.components.rectangle(
        size=(Temp.xsize + 2 * border, Temp.ysize + 2 * border), centered=True
    )
    R.center = Temp.center
    D = boolean(
        A=R,
        B=Temp,
        operation="A-B",
        precision=precision,
        num_divisions=num_divisions,
        max_points=max_points,
        layer=layer,
    )
    return D


def test_invert():
    e1 = gf.components.ellipse(radii=(6, 6)).move((10, 10))
    c = invert(e1)
    assert int(c.area()) == 910


if __name__ == "__main__":
    e1 = gf.components.ellipse(radii=(6, 6)).move((10, 10))
    c = invert(e1)
    c.show()
