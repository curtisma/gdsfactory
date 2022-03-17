import gdsfactory as gf

c = gf.components.crossing_arm(width=0.5, r1=3.0, r2=1.1, w=1.2, L=3.4, layer_wg=(1, 0), layer_slab=(2, 0))
c.plot()