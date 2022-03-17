import gdsfactory as gf

c = gf.components.switch_tree(noutputs=4, spacing=(500, 100))
c.plot()