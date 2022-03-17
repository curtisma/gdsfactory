import gdsfactory as gf

bend180 = gf.components.bend_circular180()
wg_pin = gf.components.straight_pin(length=40)
wg = gf.components.straight()

# Define a map between symbols and (component, input port, output port)
symbol_to_component = {
    "A": (bend180, 'o1', 'o2'),
    "B": (bend180, 'o2', 'o1'),
    "H": (wg_pin, 'o1', 'o2'),
    "-": (wg, 'o1', 'o2'),
}

# Each character in the sequence represents a component
s = "AB-H-H-H-H-BA"
c = gf.components.component_sequence(sequence=s, symbol_to_component=symbol_to_component)
c.plot()