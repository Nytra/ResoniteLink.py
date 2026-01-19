from resonitelink.json import json_property
from dataclasses import dataclass
from abc import ABC


@dataclass(slots=True)
class Member(ABC):
    id : str = json_property("id", str)
