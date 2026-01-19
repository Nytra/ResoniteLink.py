from resonitelink.models.datamodel import Member
from resonitelink.json import JSONPropertyType, json_model, json_property
from dataclasses import dataclass
from typing import List


@json_model("list", Member)
@dataclass(slots=True)
class SyncList(Member):
    elements : List[Member] = json_property("elements", Member, JSONPropertyType.LIST)
