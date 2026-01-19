from __future__ import annotations # Delayed evaluation of type hints (PEP 563)

from resonitelink.models.datamodel import Worker, Reference, Field_Float3, Field_FloatQ, Field_Bool, Field_String, Field_Long
from resonitelink.json import SELF, JSONPropertyType, json_model, json_property
from dataclasses import dataclass
from typing import List

from .component import Component


@json_model() # NOT derived from Worker, it's the same in the reference C# implementation.
@dataclass(slots=True)
class Slot(Worker):
    parent : Reference = json_property("parent", Reference)
    position : Field_Float3 = json_property("position", Field_Float3)
    rotation : Field_FloatQ = json_property("rotation", Field_FloatQ)
    scale : Field_Float3 = json_property("scale", Field_Float3)
    is_active : Field_Bool = json_property("isActive", Field_Bool)
    is_persistent : Field_Bool = json_property("isPersistent", Field_Bool)
    name : Field_String = json_property("name", Field_String)
    tag : Field_String = json_property("tag", Field_String)
    order_offset : Field_Long = json_property("orderOffset", Field_Long)

    components : List[Component] = json_property("components", Component, JSONPropertyType.LIST)
    children : List[Slot] = json_property("children", SELF, JSONPropertyType.LIST)

    # Special Slot references
    Root = Reference(target_id="Root", target_type="slot")
