import gdsfactory as gf

c = gf.components.loss_deembedding_ch14_23(pitch=127.0, input_port_indexes=(0, 1))
c.plot()