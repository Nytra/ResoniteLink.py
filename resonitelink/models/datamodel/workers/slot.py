from __future__ import annotations # Delayed evaluation of type hints (PEP 563)

from resonitelink.json import SELF, json_model, json_element, json_list
from typing import List

from ..worker import Worker
from ..members import Reference
from ..primitives_containers import Field_Float3, Field_FloatQ, Field_Bool, Field_String, Field_Long
from .component import Component


@json_model() # NOT derived from Worker, it's the same in the reference C# implementation.
class Slot(Worker):
    parent : Reference = json_element("parent", Reference)
    position : Field_Float3 = json_element("position", Field_Float3)
    rotation : Field_FloatQ = json_element("rotation", Field_FloatQ)
    scale : Field_Float3 = json_element("scale", Field_Float3)
    is_active : Field_Bool = json_element("isActive", Field_Bool)
    is_persistent : Field_Bool = json_element("isPersistent", Field_Bool)
    name : Field_String = json_element("name", Field_String)
    tag : Field_String = json_element("tag", Field_String)
    order_offset : Field_Long = json_element("orderOffset", Field_Long)

    components : List[Component] = json_list("components", Component)
    children : List[Slot] = json_list("children", SELF)

    # Special Slot references
    Root = Reference(target_id="Root", target_type="[FrooxEngine]FrooxEngine.Slot")
