from resonitelink.models.datamodel import Component
from resonitelink.models.messages import Message
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("getComponent", Message)
@dataclass(slots=True)
class GetComponent(Message):
    component_id : str = json_property("componentId", str)


@json_model("addComponent", Message)
@dataclass(slots=True)
class AddComponent(Message):
    data : Component = json_property("data", Component)
    container_slot_id : str = json_property("containerSlotId", str)


@json_model("updateComponent", Message)
@dataclass(slots=True)
class UpdateComponent(Message):
    data : Component = json_property("data", Component)


@json_model("removeComponent", Message)
@dataclass(slots=True)
class RemoveComponent(Message):
    component_id : str = json_property("componentId", str)
