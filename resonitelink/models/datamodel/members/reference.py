from resonitelink.models.datamodel import Member
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("reference", Member)
@dataclass(slots=True)
class Reference(Member):
    target_id : str = json_property("targetId", str)
    target_type : str = json_property("targetType", str)
