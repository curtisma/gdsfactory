import gdsfactory as gf

c = gf.components.spiral_circular(length=1000.0, wg_width=0.5, spacing=3.0, min_bend_radius=5.0, points=1000, layer=(1, 0))
c.plot()