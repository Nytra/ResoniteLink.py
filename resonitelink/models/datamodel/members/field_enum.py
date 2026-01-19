from resonitelink.models.datamodel import Member, Field
from resonitelink.json import json_model, json_property
from dataclasses import dataclass
from typing import Optional


@json_model("enum", Member)
@dataclass(slots=True)
class Field_Enum(Field):
    value : str = json_property("value", str)
    enum_type : str = json_property("enumType", str)

    @property
    def value_type_name(self) -> str:
        return "enum"


@json_model("enum?", Member)
@dataclass(slots=True)
class Field_Nullable_Enum(Field):
    value : Optional[str] = json_property("value", str)
    enum_type : str = json_property("enumType", str)

    @property
    def value_type_name(self) -> str:
        return "enum?"
