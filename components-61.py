import gdsfactory as gf

c = gf.components.dbr_tapered(length=10.0, period=0.85, dc=0.5, w1=0.4, w2=1.0, taper_length=20.0, fins=False, fin_size=(0.2, 0.05), port=(0, 0), direction='EAST')
c.plot()