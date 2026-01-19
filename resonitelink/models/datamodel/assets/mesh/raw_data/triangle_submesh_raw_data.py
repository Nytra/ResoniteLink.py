from .submesh_raw_data import SubmeshRawData
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("triangles", SubmeshRawData)
@dataclass(slots=True)
class TriangleSubmeshRawData(SubmeshRawData):
    triangle_count : int = json_property("triangleCount", int)

    @property
    def indices_count(self) -> int:
        return self.triangle_count * 3
