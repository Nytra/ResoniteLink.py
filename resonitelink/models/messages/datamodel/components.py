from resonitelink.json import json_model, json_element

from ...datamodel import Component
from ...messages import Message


@json_model("getComponent", Message)
class GetComponent(Message):
    component_id : str = json_element("componentId", str)


@json_model("addComponent", Message)
class AddComponent(Message):
    data : Component = json_element("data", Component)
    container_slot_id : str = json_element("containerSlotId", str)


@json_model("updateComponent", Message)
class UpdateComponent(Message):
    data : Component = json_element("data", Component)


@json_model("removeComponent", Message)
class RemoveComponent(Message):
    component_id : str = json_element("componentId", str)
