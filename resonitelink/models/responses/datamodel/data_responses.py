from resonitelink.json import json_model, json_element

from ...datamodel import Slot, Component
from ..response import Response


@json_model("slotData", Response)
class SlotData(Response):
    depth : int = json_element("depth", int)
    data : Slot = json_element("data", Slot)


@json_model("componentData", Response)
class ComponentData(Response):
    data : Component = json_element("data", Component)


@json_model("assetData", Response)
class AssetData(Response):
    asset_url : str = json_element("assetURL", str)
