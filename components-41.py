import gdsfactory as gf

c = gf.components.coupler_adiabatic(length1=20.0, length2=50.0, length3=30.0, wg_sep=1.0, input_wg_sep=3.0, output_wg_sep=3.0, dw=0.1, port=(0, 0), direction='EAST')
c.plot()