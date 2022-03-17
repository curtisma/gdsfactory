import gdsfactory as gf

c = gf.components.bend_straight_bend(straight_length=10.0, angle=90, p=0.5, with_arc_floorplan=True, npoints=720, direction='ccw', with_cladding_box=True)
c.plot()