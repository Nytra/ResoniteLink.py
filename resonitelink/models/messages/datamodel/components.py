from resonitelink.json import json_model, json_element
from dataclasses import dataclass

from ...datamodel import Component
from ...messages import Message


@json_model("getComponent", Message)
@dataclass(slots=True)
class GetComponent(Message):
    component_id : str = json_element("componentId", str)


@json_model("addComponent", Message)
@dataclass(slots=True)
class AddComponent(Message):
    data : Component = json_element("data", Component)
    container_slot_id : str = json_element("containerSlotId", str)


@json_model("updateComponent", Message)
@dataclass(slots=True)
class UpdateComponent(Message):
    data : Component = json_element("data", Component)


@json_model("removeComponent", Message)
@dataclass(slots=True)
class RemoveComponent(Message):
    component_id : str = json_element("componentId", str)
