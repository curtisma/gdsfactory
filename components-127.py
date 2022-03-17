import gdsfactory as gf

c = gf.components.resistance_sheet(width=10, layers=((3, 0), (24, 0)), layer_offsets=(0, 0.2), pad_pitch=100.0)
c.plot()