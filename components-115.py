import gdsfactory as gf

c = gf.components.nxn(west=1, east=4, north=0, south=0, xsize=8.0, ysize=8.0, wg_width=0.5, layer=(1, 0), wg_margin=1.0)
c.plot()