import gdsfactory as gf

c = gf.components.disk(radius=10.0, gap=0.2, wrap_angle_deg=180.0, parity=1, port=(0, 0), direction='EAST')
c.plot()