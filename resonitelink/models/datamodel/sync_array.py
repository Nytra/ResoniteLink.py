from resonitelink.models.datamodel import Member
from resonitelink.json import JSONPropertyType, json_property
from dataclasses import dataclass
from typing import List, Any
from abc import ABC, abstractmethod


@dataclass(slots=True)
class SyncArray(Member, ABC):
    values : List[Any] = json_property("values", object, JSONPropertyType.LIST, abstract=True)

    @property
    @abstractmethod
    def element_type(self) -> str:
        raise NotImplementedError()
