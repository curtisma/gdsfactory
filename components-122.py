import gdsfactory as gf

c = gf.components.qrcode(data='mask01', psize=1, layer=(1, 0))
c.plot()