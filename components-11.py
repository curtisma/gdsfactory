import gdsfactory as gf

c = gf.components.awg(arms=10, outputs=3, fpr_spacing=50.0)
c.plot()