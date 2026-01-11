from resonitelink.models.responses import Response
from resonitelink.models.datamodel import Slot
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, Any


@json_model("slotData")
@dataclass(slots=True)
class SlotData(Response):
    depth : Annotated[int, JSONProperty("depth")] = MISSING
    data : Annotated[Slot, JSONProperty("data")] = MISSING


@json_model("componentData")
@dataclass(slots=True)
class ComponentData(Response):
    data : Annotated[Any, JSONProperty("data")] = MISSING # TODO: This should be type Component


@json_model("assetData")
@dataclass(slots=True)
class AssetData(Response):
    asset_url : Annotated[str, JSONProperty("assetUrl")] = MISSING
