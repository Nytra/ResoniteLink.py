from resonitelink.models.datamodel import Member
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("reference")
@dataclass(slots=True)
class Reference(Member):
    target_id : Annotated[str, JSONProperty("targetId")] = MISSING
    target_type : Annotated[str, JSONProperty("targetType")] = MISSING
