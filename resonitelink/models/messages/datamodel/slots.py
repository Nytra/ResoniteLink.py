from resonitelink.models.datamodel import Slot
from resonitelink.models.messages import Message
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("getSlot", Message)
@dataclass(slots=True)
class GetSlot(Message):
    slot_id : str = json_property("slotId", str)
    depth : int = json_property("depth", int)
    include_component_data : bool = json_property("includeComponentData", bool)


@json_model("addSlot", Message)
@dataclass(slots=True)
class AddSlot(Message):
    data : Slot = json_property("data", Slot)


@json_model("updateSlot", Message)
@dataclass(slots=True)
class UpdateSlot(Message):
    data : Slot = json_property("data", Slot)


@json_model("removeSlot", Message)
@dataclass(slots=True)
class RemoveSlot(Message):
    slot_id : str = json_property("slotId", str)
