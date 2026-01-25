from resonitelink.json import json_model, json_element

from .submesh_raw_data import SubmeshRawData


@json_model("points", SubmeshRawData)
class PointSubmeshRawData(SubmeshRawData):
    point_count : int = json_element("pointCount", int)

    @property
    def indices_count(self) -> int:
        return self.point_count
