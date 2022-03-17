import gdsfactory as gf

c = gf.components.grating_coupler_array(pitch=127.0, n=6, port_name='o1', rotation=0)
c.plot()