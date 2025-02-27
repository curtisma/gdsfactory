import pathlib
from typing import Any, Callable, Dict, Optional, Tuple

import pydantic
from pydantic import BaseModel

module_path = pathlib.Path(__file__).parent.absolute()
Layer = Tuple[int, int]


def make_empty_dict() -> Dict[str, Callable]:
    return {}


@pydantic.dataclasses.dataclass(frozen=True)
class LayerMap:
    """Generic layermap based on Textbook:
    Lukas Chrostowski, Michael Hochberg, "Silicon Photonics Design",
    Cambridge University Press 2015, page 353

    You will need to create a new LayerMap with your specific foundry layers.
    """

    WG: Layer = (1, 0)
    WGCLAD: Layer = (111, 0)
    SLAB150: Layer = (2, 0)
    SLAB90: Layer = (3, 0)
    DEEPTRENCH: Layer = (4, 0)
    GE: Layer = (5, 0)
    WGN: Layer = (34, 0)
    WGN_CLAD: Layer = (36, 0)

    N: Layer = (20, 0)
    NP: Layer = (22, 0)
    NPP: Layer = (24, 0)
    P: Layer = (21, 0)
    PP: Layer = (23, 0)
    PPP: Layer = (25, 0)
    GEN: Layer = (26, 0)
    GEP: Layer = (27, 0)

    HEATER: Layer = (47, 0)
    M1: Layer = (41, 0)
    M2: Layer = (45, 0)
    M3: Layer = (49, 0)
    VIAC: Layer = (40, 0)
    VIA1: Layer = (44, 0)
    VIA2: Layer = (43, 0)
    PADOPEN: Layer = (46, 0)

    NO_TILE_SI: Layer = (71, 0)
    PADDING: Layer = (67, 0)
    DEVREC: Layer = (68, 0)
    FLOORPLAN: Layer = (99, 0)
    TEXT: Layer = (66, 0)
    PORT: Layer = (1, 10)
    PORTE: Layer = (1, 11)
    PORTH: Layer = (70, 0)
    LABEL: Layer = (201, 0)
    LABEL_SETTINGS: Layer = (202, 0)
    TE: Layer = (203, 0)
    TM: Layer = (204, 0)
    DRC_MARKER: Layer = (205, 0)
    LABEL_INSTANCE: Layer = (206, 0)
    ERROR_MARKER: Layer = (207, 0)
    ERROR_PATH: Layer = (208, 0)


LAYER = LayerMap()
PORT_MARKER_LAYER_TO_TYPE = {
    LAYER.PORT: "optical",
    LAYER.PORTE: "dc",
    LAYER.TE: "vertical_te",
    LAYER.TM: "vertical_tm",
}

PORT_LAYER_TO_TYPE = {
    LAYER.WG: "optical",
    LAYER.WGN: "optical",
    LAYER.SLAB150: "optical",
    LAYER.M1: "dc",
    LAYER.M2: "dc",
    LAYER.M3: "dc",
    LAYER.TE: "vertical_te",
    LAYER.TM: "vertical_tm",
}

PORT_TYPE_TO_MARKER_LAYER = {v: k for k, v in PORT_MARKER_LAYER_TO_TYPE.items()}


class LayerLevel(BaseModel):
    """Layer For 3D LayerStack.

    Args:
        layer: (GDSII Layer number, GDSII datatype)
        thickness: layer thickness
        zmin: height position where material starts
        material: material name
        sidewall_angle: in degrees with respect to normal
    """

    layer: Tuple[int, int]
    thickness: Optional[float] = None
    zmin: Optional[float] = None
    material: Optional[str] = None
    sidewall_angle: float = 0


class LayerStack(dict):
    """For simulation and trimesh 3D rendering"""

    def get_layer_to_thickness(self) -> Dict[Tuple[int, int], float]:
        """Returns layer tuple to thickness (um)."""
        return {
            level.layer: level.thickness for level in self.values() if level.thickness
        }

    def get_layer_to_zmin(self) -> Dict[Tuple[int, int], float]:
        """Returns layer tuple to z min position (um)."""
        return {level.layer: level.zmin for level in self.values() if level.thickness}

    def get_layer_to_material(self) -> Dict[Tuple[int, int], str]:
        """Returns layer tuple to material name."""
        return {
            level.layer: level.material for level in self.values() if level.thickness
        }

    def get_layer_to_sidewall_angle(self) -> Dict[Tuple[int, int], str]:
        """Returns layer tuple to material name."""
        return {
            level.layer: level.sidewall_angle
            for level in self.values()
            if level.thickness
        }

    def to_dict(self) -> Dict[str, Dict[str, Any]]:
        return {level_name: dict(level) for level_name, level in self.items()}


def get_layer_stack_generic(thickness_silicon_core: float = 220e-3) -> LayerStack:
    """Returns generic LayerStack.
    based on paper https://www.degruyter.com/document/doi/10.1515/nanoph-2013-0034/html
    """
    layer_stack = LayerStack(
        core=LayerLevel(
            layer=LAYER.WG,
            thickness=thickness_silicon_core,
            zmin=0.0,
            material="si",
        ),
        clad=LayerLevel(
            layer=LAYER.WGCLAD,
            zmin=0.0,
            material="sio2",
        ),
        slab150=LayerLevel(
            layer=LAYER.SLAB150,
            thickness=150e-3,
            zmin=0,
            material="si",
        ),
        slab90=LayerLevel(
            layer=LAYER.SLAB90,
            thickness=90e-3,
            zmin=0.0,
            material="si",
        ),
        nitride=LayerLevel(
            layer=LAYER.WGN,
            thickness=350e-3,
            zmin=220e-3 + 100e-3,
            material="sin",
        ),
        ge=LayerLevel(
            layer=LAYER.GE,
            thickness=500e-3,
            zmin=220e-3,
            material="ge",
        ),
        via_contact=LayerLevel(
            layer=LAYER.VIAC,
            thickness=1100e-3,
            zmin=90e-3,
            material="Aluminum",
        ),
        metal1=LayerLevel(
            layer=LAYER.M1,
            thickness=750e-3,
            zmin=220e-3 + 1100e-3,
            material="Aluminum",
        ),
        heater=LayerLevel(
            layer=LAYER.HEATER,
            thickness=750e-3,
            zmin=220e-3 + 1100e-3,
            material="TiN",
        ),
        viac=LayerLevel(
            layer=LAYER.VIA1,
            thickness=1500e-3,
            zmin=220e-3 + 1100e-3 + 750e-3,
            material="Aluminum",
        ),
        metal2=LayerLevel(
            layer=LAYER.M2,
            thickness=2000e-3,
            zmin=220e-3 + 1100e-3 + 750e-3 + 1.5,
            material="Aluminum",
        ),
    )
    return layer_stack


LAYER_STACK = get_layer_stack_generic()


class Section(BaseModel):
    """

    Args:
        width: of the section (um)
        offset: center offset
        layer:
        ports: Optional port names
        name: Optional Section name
        port_types: optical, electrical, ...

    .. code::

          0   offset
          |<-------------->|
          |              _____
          |             |     |
          |             |layer|
          |             |_____|
          |              <---->
                         width

    """

    width: float
    offset: float = 0
    layer: Layer = (1, 0)
    ports: Tuple[Optional[str], Optional[str]] = (None, None)
    name: Optional[str] = None
    port_types: Tuple[str, str] = ("optical", "optical")

    def __repr__(self):
        return "_".join(
            [
                f"{i}"
                for i in [
                    self.name,
                    int(self.width * 1e3),
                    self.layer[0],
                    self.layer[1],
                    self.ports[0],
                    self.ports[1],
                    self.port_types[0],
                    self.port_types[1],
                ]
                if i is not None
            ]
        )


class SimulationSettings(BaseModel):
    """Lumerical FDTD simulation_settings

    Args:
        background_material: for the background
        port_margin: on both sides of the port width (um)
        port_height: port height (um)
        port_extension: port extension (um)
        mesh_accuracy: 2 (1: coarse, 2: fine, 3: superfine)
        zmargin: for the FDTD region (um)
        ymargin: for the FDTD region (um)
        xmargin: for the FDTD region (um)
        wavelength_start: 1.2 (um)
        wavelength_stop: 1.6 (um)
        wavelength_points: 500
        simulation_time: (s) related to max path length 3e8/2.4*10e-12*1e6 = 1.25mm
        simulation_temperature: in kelvin (default = 300)
        frequency_dependent_profile: computes mode profiles for different wavelengths
        field_profile_samples: number of wavelengths to compute field profile

    """

    background_material: str = "sio2"
    port_margin: float = 1.5
    port_extension: float = 5.0
    mesh_accuracy: int = 2
    zmargin: float = 1.0
    ymargin: float = 3.0
    xmargin: float = 3.0
    wavelength_start: float = 1.2
    wavelength_stop: float = 1.6
    wavelength_points: int = 500
    simulation_time: float = 10e-12
    simulation_temperature: float = 300
    frequency_dependent_profile: bool = True
    field_profile_samples: int = 15
    distance_source_to_monitors: float = 0.2
    material_name_to_lumerical = {
        "si": "Si (Silicon) - Palik",
        "sio2": "SiO2 (Glass) - Palik",
        "sin": "Si3N4 (Silicon Nitride) - Phillip",
    }


SIMULATION_SETTINGS = SimulationSettings()


def assert_callable(function):
    if not callable(function):
        raise ValueError(
            f"Error: function = {function} with type {type(function)} is not callable"
        )


class Tech(BaseModel):
    name: str = "generic"
    layer: LayerMap = LAYER

    fiber_spacing: float = 50.0
    fiber_array_spacing: float = 127.0
    fiber_input_to_output_spacing: float = 200.0
    layer_label: Layer = LAYER.LABEL
    metal_spacing: float = 10.0


TECH = Tech()

if __name__ == "__main__":
    import gdsfactory as gf
    from gdsfactory.component import clean_value_json

    d = clean_value_json(SIMULATION_SETTINGS)

    def mmi1x2_longer(length_mmi: float = 25.0, **kwargs):
        return gf.components.mmi1x2(length_mmi=length_mmi, **kwargs)

    def mzi_longer(**kwargs):
        return gf.components.mzi(splitter=mmi1x2_longer, **kwargs)

    ls = LAYER_STACK
    # print(ls.get_layer_to_material())
    # print(ls.get_layer_to_thickness())

    # s = Section(width=1, layer=(1, 0))
    # print(s)
