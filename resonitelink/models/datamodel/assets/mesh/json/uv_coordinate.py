from resonitelink.models.datamodel import Float2, Float3, Float4
from resonitelink.json import json_model, json_property
from dataclasses import dataclass
from abc import ABC


@dataclass(slots=True)
class UV_Coordinate(ABC):
    pass


@json_model("2D", UV_Coordinate)
@dataclass(slots=True)
class UV2D_Coordinate(UV_Coordinate):
    uv : Float2 = json_property("uv", Float2)


@json_model("3D", UV_Coordinate)
@dataclass(slots=True)
class UV3D_Coordinate(UV_Coordinate):
    uv : Float3 = json_property("uv", Float3)


@json_model("4D", UV_Coordinate)
@dataclass(slots=True)
class UV4D_Coordinate(UV_Coordinate):
    uv : Float4 = json_property("uv", Float4)
