import gdsfactory as gf

c = gf.components.delay_snake(wg_width=0.5, wg_width_wide=2.0, total_length=1600.0, L0=5.0, taper_length=10.0, n=2)
c.plot()