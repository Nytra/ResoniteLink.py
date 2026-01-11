from resonitelink.models.messages import Message
from resonitelink.json import MISSING, json_model, JSONProperty
from dataclasses import dataclass
from typing import Annotated, Any


@json_model("getComponent")
@dataclass(slots=True)
class GetComponent(Message):
    component_id : Annotated[str, JSONProperty("componentId")] = MISSING


@json_model("addComponent")
@dataclass(slots=True)
class AddComponent(Message):
    data : Annotated[Any, JSONProperty("data")] = MISSING # TODO: This should be of type Component
    container_slot_id : Annotated[str, JSONProperty("containerSlotId")] = MISSING


@json_model("updateComponent")
@dataclass(slots=True)
class UpdateComponent(Message):
    data : Annotated[Any, JSONProperty("data")] = MISSING # TODO: This should be of type Component


@json_model("removeComponent")
@dataclass(slots=True)
class RemoveComponent(Message):
    component_id : Annotated[str, JSONProperty("componentId")] = MISSING
