from .blendshape_frame import BlendshapeFrame
from resonitelink.json import JSONPropertyType, json_model, json_property
from dataclasses import dataclass
from typing import List


@json_model()
@dataclass(slots=True)
class Blendshape():
    # Name of the Blendshape.
    name : str = json_property("name", str)

    # Frames that compose this blendshape.
    # Blendshapes need at least 1 frame.
    frames : List[BlendshapeFrame] = json_property("frames", BlendshapeFrame, JSONPropertyType.LIST)
