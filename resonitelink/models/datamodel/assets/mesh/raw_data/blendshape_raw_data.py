from resonitelink.json import JSONPropertyType, json_model, json_property
from dataclasses import dataclass
from typing import List

from .blendshape_frame_raw_data import BlendshapeFrameRawData


@json_model()
@dataclass(slots=True)
class BlendshapeRawData():
    # Name of the blendshape.
    name : str = json_property("name", str)

    # Indicates if this blenshape has normal datas.
    has_normal_deltas : bool = json_property("hasNormalDeltas", bool)

    # Indicates if this blendshape has tangent deltas.
    has_tangent_deltas : bool = json_property("hasTangentDeltas", bool)

    # Frames that compose this blendshape.
    # Blendshapes need at least 1 frame.
    frames : List[BlendshapeFrameRawData] = json_property("frames", BlendshapeFrameRawData, JSONPropertyType.LIST)
