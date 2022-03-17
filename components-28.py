import gdsfactory as gf
from gdsfactory.components.crossing_waveguide import crossing45
from gdsfactory.components.crossing_waveguide import compensation_path

symbol_to_component =  {
      "C": gf.routing.fanout2x2(component=gf.components.coupler(), port_spacing=40.0),
      "X": crossing45(port_spacing=40.0),
      "-": compensation_path(crossing45=crossing45(port_spacing=40.0)),
}
c = gf.components.component_lattice(symbol_to_component=symbol_to_component)
c.plot()