from resonitelink.json import json_property
from dataclasses import dataclass
from abc import ABC


@dataclass(slots=False)
class Worker(ABC):
    id : str = json_property("id", str)
    is_reference_only : bool = json_property("isReferenceOnly", bool)
