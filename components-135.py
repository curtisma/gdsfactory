import gdsfactory as gf

c = gf.components.seal_ring(bbox=((-1.0, -1.0), (3.0, 4.0)), width=10, padding=10.0, with_north=True, with_south=True, with_east=True, with_west=True)
c.plot()