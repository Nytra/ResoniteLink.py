from resonitelink.models.datamodel import Member
from resonitelink.json import json_model
from dataclasses import dataclass


@json_model("empty")
@dataclass(slots=True)
class EmptyElement(Member):
    pass
