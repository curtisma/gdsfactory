import gdsfactory as gf

c = gf.components.bend_circular_heater(radius=10, angle=90, npoints=720, heater_to_wg_distance=1.2, heater_width=0.5, layer_heater=(47, 0))
c.plot()