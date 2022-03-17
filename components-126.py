import gdsfactory as gf

c = gf.components.resistance_meander(pad_size=(50.0, 50.0), num_squares=1000, width=1.0, res_layer=(49, 0), pad_layer=(49, 0), gnd_layer=(49, 0))
c.plot()