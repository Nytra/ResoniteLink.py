from resonitelink.models.datamodel import Member
from resonitelink.json import MISSING, JSONProperty
from dataclasses import dataclass
from typing import Annotated, Any
from abc import ABC, abstractmethod


@dataclass(slots=True)
class Field(Member, ABC):
    value : Annotated[Any, JSONProperty("value", abstract=True)] = MISSING

    @property
    @abstractmethod
    def value_type_name(self) -> str:
        raise NotImplementedError()
