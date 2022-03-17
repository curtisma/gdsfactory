import gdsfactory as gf

c = gf.components.bbox(bbox=((-1.0, -1.0), (3.0, 4.0)), layer=(1, 0), top=0, bottom=0, left=0, right=0)
c.plot()