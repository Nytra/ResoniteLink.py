from resonitelink.json import json_model, json_element, json_dict
from typing import Dict

from ..worker import Worker
from ..member import Member


@json_model() # NOT derived from Worker, it's the same in the reference C# implementation.
class Component(Worker):
    component_type : str = json_element("componentType", str)
    members : Dict[str, Member] = json_dict("members", Member)
