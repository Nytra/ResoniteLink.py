from resonitelink.models.datamodel import Slot
from resonitelink.models.messages import BaseMessage
from resonitelink.json import MISSING, json_model, JSONProperty
from dataclasses import dataclass
from typing import Annotated


@json_model("getSlot")
@dataclass(slots=True)
class GetSlot(BaseMessage):
    slot_id : Annotated[str, JSONProperty("slotId")] = MISSING
    depth : Annotated[int, JSONProperty("depth")] = MISSING
    include_component_data : Annotated[bool, JSONProperty("includeComponentData")] = MISSING


@json_model("addSlot")
@dataclass(slots=True)
class AddSlot(BaseMessage):
    data : Annotated[Slot, JSONProperty("data")] = MISSING


@json_model("updateSlot")
@dataclass(slots=True)
class UpdateSlot(BaseMessage):
    data : Annotated[Slot, JSONProperty("data")] = MISSING


@json_model("removeSlot")
@dataclass(slots=True)
class RemoveSlot(BaseMessage):
    slot_id : Annotated[str, JSONProperty("slotId")] = MISSING
