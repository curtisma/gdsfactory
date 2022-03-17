import gdsfactory as gf
gf.config.set_plot_options(show_subports=False)

c = gf.components.crossing()
cc = gf.routing.add_fiber_array(
    component=c,
    optical_routing_type=2,
    grating_coupler=gf.components.grating_coupler_elliptical_te,
    with_loopback=False
)
cc.plot()