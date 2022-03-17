import gdsfactory as gf

c = gf.components.coupler_full(length=40.0, gap=0.5, dw=0.1, angle=0.5235987755982988, parity=1, port=(0, 0), direction='EAST')
c.plot()