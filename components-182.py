import gdsfactory as gf

c = gf.components.via_cutback(num_vias=100.0, wire_width=10.0, via_width=5.0, via_spacing=40.0, min_pad_spacing=0.0, pad_size=(150, 150), layer1=(47, 0), layer2=(41, 0), via_layer=(40, 0), wire_pad_inclusion=12.0)
c.plot()