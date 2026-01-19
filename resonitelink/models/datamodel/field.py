from resonitelink.models.datamodel import Member
from resonitelink.json import json_property
from dataclasses import dataclass
from typing import Any
from abc import ABC, abstractmethod


@dataclass(slots=True)
class Field(Member, ABC):
    value : Any = json_property("value", object, abstract=True)

    @property
    @abstractmethod
    def value_type_name(self) -> str:
        raise NotImplementedError()
