from resonitelink.json import json_model, json_dict
from typing import Dict

from .member import Member


@json_model("syncObject", Member)
class SyncObject(Member):
    members : Dict[str, Member] = json_dict("members", Member)
