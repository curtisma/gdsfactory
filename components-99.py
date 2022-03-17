import gdsfactory as gf

c = gf.components.loss_deembedding_ch13_24(pitch=127.0, input_port_indexes=(0, 1))
c.plot()