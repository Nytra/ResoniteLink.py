from resonitelink.models.datamodel import Member
from resonitelink.json import MISSING, JSONProperty, JSONPropertyType, json_model
from dataclasses import dataclass
from typing import Annotated, Dict


@json_model("syncObject")
@dataclass(slots=True)
class SyncObject(Member):
    members : Annotated[Dict[str, Member], JSONProperty("members", property_type=JSONPropertyType.DICT)] = MISSING
