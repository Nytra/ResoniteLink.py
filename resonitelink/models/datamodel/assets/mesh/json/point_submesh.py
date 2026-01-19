from resonitelink.json import JSONPropertyType, json_model, json_property
from dataclasses import dataclass
from typing import List

from .submesh import Submesh


@json_model("points", Submesh)
@dataclass(slots=True)
class PointSubmesh(Submesh):
    vertex_indices : List[int] = json_property("vertexIndices", int, JSONPropertyType.LIST)
