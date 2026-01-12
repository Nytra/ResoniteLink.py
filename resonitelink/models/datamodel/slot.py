from resonitelink.models.datamodel import Worker, Reference, Field_Float3, Field_FloatQ, Field_Bool, Field_String, Field_Long
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, Any


@json_model("slot")
@dataclass(slots=False)
class Slot(Worker):
    parent : Annotated[Reference, JSONProperty("parent", model_type_name="reference")] = MISSING
    position : Annotated[Field_Float3, JSONProperty("position", model_type_name="field_float3")] = MISSING
    rotation : Annotated[Field_FloatQ, JSONProperty("rotation", model_type_name="field_floatQ")] = MISSING
    scale : Annotated[Field_Float3, JSONProperty("scale", model_type_name="field_float3")] = MISSING
    is_active : Annotated[Field_Bool, JSONProperty("isActive", model_type_name="field_bool")] = MISSING
    is_persistent : Annotated[Field_Bool, JSONProperty("isPersistent", model_type_name="field_bool")] = MISSING
    name : Annotated[Field_String, JSONProperty("name", model_type_name="field_string")] = MISSING
    tag : Annotated[Field_String, JSONProperty("tag", model_type_name="field_string")] = MISSING
    order_offset : Annotated[Field_Long, JSONProperty("orderOffset", model_type_name="field_long")] = MISSING

    components : Annotated[Any, JSONProperty("components")] = MISSING # TODO: Should be List[Component]
    children : Annotated[Any, JSONProperty("children")] = MISSING # TODO: Should be List[Slot]

    # Special Slot references
    Root = Reference(target_id="Root", target_type="slot")
