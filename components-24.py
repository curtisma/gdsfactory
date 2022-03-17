import gdsfactory as gf

c = gf.components.cdsem_all(widths=(0.4, 0.45, 0.5, 0.6, 0.8, 1.0), dense_lines_width=0.3, dense_lines_width_difference=0.02, dense_lines_gap=0.3, dense_lines_labels=('DL', 'DM', 'DH'))
c.plot()