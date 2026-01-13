from resonitelink.models.datamodel import Member
from resonitelink.json import MISSING, JSONProperty, JSONPropertyType, json_model
from dataclasses import dataclass
from typing import Annotated, List


@json_model("list")
@dataclass(slots=True)
class SyncList(Member):
    elements : Annotated[List[Member], JSONProperty("elements", property_type=JSONPropertyType.LIST)] = MISSING
