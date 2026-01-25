from resonitelink.models.datamodel import Slot
from resonitelink.models.messages import Message
from resonitelink.json import json_model, json_element


@json_model("getSlot", Message)
class GetSlot(Message):
    slot_id : str = json_element("slotId", str)
    depth : int = json_element("depth", int)
    include_component_data : bool = json_element("includeComponentData", bool)


@json_model("addSlot", Message)
class AddSlot(Message):
    data : Slot = json_element("data", Slot)


@json_model("updateSlot", Message)
class UpdateSlot(Message):
    data : Slot = json_element("data", Slot)


@json_model("removeSlot", Message)
class RemoveSlot(Message):
    slot_id : str = json_element("slotId", str)
