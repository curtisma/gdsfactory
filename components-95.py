import gdsfactory as gf

c = gf.components.litho_steps(line_widths=(1.0, 2.0, 4.0, 8.0, 16.0), line_spacing=10.0, height=100.0, layer=(1, 0))
c.plot()