from resonitelink.models.responses import Response
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("sessionData", Response)
@dataclass(slots=True)
class SessionData(Response):
    resonite_version : str = json_property("resoniteVersion", str)
    resonite_link_version : str = json_property("resoniteLinkVersion", str)
    unique_session_id : str = json_property("uniqueSessionId", str)
