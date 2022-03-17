import gdsfactory as gf

@gf.cell
def rectangle(size=(4,2), layer=0)->gf.Component:
    c = gf.Component()
    w, h = size
    points = [[w, h], [w, 0], [0, 0], [0, h]]
    c.add_polygon(points, layer=layer)
    return c

c = rectangle(layer=(1,0))
c.plot()