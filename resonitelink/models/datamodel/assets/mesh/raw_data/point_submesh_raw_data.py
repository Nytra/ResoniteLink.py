from .submesh_raw_data import SubmeshRawData
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("points", SubmeshRawData)
@dataclass(slots=True)
class PointSubmeshRawData(SubmeshRawData):
    point_count : int = json_property("pointCount", int)

    @property
    def indices_count(self) -> int:
        return self.point_count
