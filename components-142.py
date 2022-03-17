import gdsfactory as gf

c = gf.components.splitter_tree(noutputs=4, spacing=(90.0, 50.0))
c.plot()