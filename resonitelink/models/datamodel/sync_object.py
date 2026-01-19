from resonitelink.models.datamodel import Member
from resonitelink.json import JSONPropertyType, json_model, json_property
from dataclasses import dataclass
from typing import Dict


@json_model("syncObject", Member)
@dataclass(slots=True)
class SyncObject(Member):
    members : Dict[str, Member] = json_property("members", Member, JSONPropertyType.DICT)
