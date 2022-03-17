import gdsfactory as gf

c = gf.components.mmi2x2(width=0.5, width_taper=1.0, length_taper=10.0, length_mmi=5.5, width_mmi=2.5, gap_mmi=0.25)
c.plot()