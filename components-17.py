import gdsfactory as gf

c = gf.components.bend_euler180(angle=180, p=0.5, with_arc_floorplan=True, npoints=720, direction='ccw', with_cladding_box=True)
c.plot()