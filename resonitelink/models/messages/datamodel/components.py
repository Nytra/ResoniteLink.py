from resonitelink.models.messages import BaseMessage
from resonitelink.json import MISSING, json_model, JSONProperty
from dataclasses import dataclass
from typing import Annotated, Any


@json_model("getComponent")
@dataclass(slots=True)
class GetComponent(BaseMessage):
    component_id : Annotated[str, JSONProperty("componentId")] = MISSING


@json_model("addComponent")
@dataclass(slots=True)
class AddComponent(BaseMessage):
    data : Annotated[Any, JSONProperty("data")] = MISSING # TODO: This should be of type Component
    container_slot_id : Annotated[str, JSONProperty("containerSlotId")] = MISSING


@json_model("updateComponent")
@dataclass(slots=True)
class UpdateComponent(BaseMessage):
    data : Annotated[Any, JSONProperty("data")] = MISSING # TODO: This should be of type Component


@json_model("removeComponent")
@dataclass(slots=True)
class RemoveComponent(BaseMessage):
    component_id : Annotated[str, JSONProperty("componentId")] = MISSING
