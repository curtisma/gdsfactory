import gdsfactory as gf

c = gf.components.delay_snake_sbend(length=100.0, length1=0.0, length4=0.0, radius=5.0, waveguide_spacing=5.0, sbend_xsize=100.0, print_min_bend_radius=False)
c.plot()