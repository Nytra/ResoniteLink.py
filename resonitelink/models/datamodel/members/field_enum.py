from resonitelink.models.datamodel import Field
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("enum", Field)
@dataclass(slots=True)
class Field_Enum(Field):
    value : str = json_property("value", str)
    enum_type : str = json_property("enumType", str)

    @property
    def value_type_name(self) -> str:
        return "enum"


@json_model("enum?", Field)
@dataclass(slots=True)
class Field_Nullable_Enum(Field):
    value : str = json_property("value", str) # TODO: This is optional. Is that a problem?
    enum_type : str = json_property("enumType", str)

    @property
    def value_type_name(self) -> str:
        return "enum?"