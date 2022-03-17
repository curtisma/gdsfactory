import gdsfactory as gf

c = gf.components.crossing()
cc = gf.routing.add_fiber_single(
    component=c,
    optical_routing_type=0,
    grating_coupler=gf.components.grating_coupler_elliptical_te,
)
cc.plot()