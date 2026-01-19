from resonitelink.models.responses import Response
from resonitelink.models.datamodel import Slot, Component
from resonitelink.json import json_property, json_model
from dataclasses import dataclass


@json_model("slotData", Response)
@dataclass(slots=True)
class SlotData(Response):
    depth : int = json_property("depth", int)
    data : Slot = json_property("data", Slot)


@json_model("componentData", Response)
@dataclass(slots=True)
class ComponentData(Response):
    data : Component = json_property("data", Component)


@json_model("assetData", Response)
@dataclass(slots=True)
class AssetData(Response):
    asset_url : str = json_property("assetURL", str)
