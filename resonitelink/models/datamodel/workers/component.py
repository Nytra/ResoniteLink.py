from resonitelink.models.datamodel import Worker, Member
from resonitelink.json import JSONPropertyType, json_model, json_property
from dataclasses import dataclass
from typing import Dict


@json_model() # NOT derived from Worker, it's the same in the reference C# implementation.
@dataclass(slots=False)
class Component(Worker):
    component_type : str = json_property("componentType", str)
    members : Dict[str, Member] = json_property("members", Member, JSONPropertyType.DICT)
