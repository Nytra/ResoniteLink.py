from resonitelink.json import json_model, json_element

from ..member import Member


@json_model("reference", Member)
class Reference(Member):
    target_id : str = json_element("targetId", str)
    target_type : str = json_element("targetType", str)
