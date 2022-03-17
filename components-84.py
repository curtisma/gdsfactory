import gdsfactory as gf

c = gf.components.grating_coupler_loss_fiber_array(pitch=127.0, input_port_indexes=(0, 1))
c.plot()