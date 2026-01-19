from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("response")
@dataclass(slots=True)
class Response():
    source_message_id : str = json_property("sourceMessageId", str)
    success : bool = json_property("success", bool)
    error_info : str = json_property("errorInfo", str)
