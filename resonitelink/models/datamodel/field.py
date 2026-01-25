from resonitelink.json import abstract_json_model, json_element
from typing import Any
from abc import ABC, abstractmethod

from .member import Member


@abstract_json_model()
class Field(Member, ABC):
    value : Any = json_element("value", object, abstract=True)

    @property
    @abstractmethod
    def value_type_name(self) -> str:
        raise NotImplementedError()
