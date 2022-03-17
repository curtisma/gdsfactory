import gdsfactory as gf

c = gf.components.bend_s(size=(10.0, 2.0), nb_points=99, with_cladding_box=True)
c.plot()