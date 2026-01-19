from resonitelink.models.datamodel import Float3
from resonitelink.json import json_model, json_property
from dataclasses import dataclass
from typing import List


@json_model()
@dataclass(slots=True)
class BlendshapeFrame():
    # Position of the frame within the blendshape animation.
    # When blendshape has only a single frame, this should be set to 1.0.
    # With multiple frames per blendshape, this determines the position at which this set of deltas is fully applied.
    position : float = json_property("position", float)

    # Delta values for vertex positions of this blendshape frame.
    # Number of deltas MUST match number of vertices.
    position_deltas : List[Float3] = json_property("positionDeltas", Float3)

    # Optional. Delta values for vertex normals of this blendshape frame.
    # Number of deltas MUST match number of vertices.
    normal_deltas : List[Float3] = json_property("normalDeltas", Float3)

    # Optional. Delta values for vertex tangents of this blendshape frame.
    # Number of deltas MUST match number of vertices.
    tangent_deltas : List[Float3] = json_property("tangentDeltas", Float3)
