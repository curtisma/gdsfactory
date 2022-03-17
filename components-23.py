import gdsfactory as gf

c = gf.components.cdc(length=30.0, gap=0.5, period=0.22, dc=0.5, angle=0.5235987755982988, width_top=2.0, width_bot=0.75, input_bot=False, fins=False, fin_size=(0.2, 0.05), port_midpoint=(0, 0), direction='EAST')
c.plot()