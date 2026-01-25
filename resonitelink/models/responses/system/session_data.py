from resonitelink.models.responses import Response
from resonitelink.json import json_model, json_element


@json_model("sessionData", Response)
class SessionData(Response):
    resonite_version : str = json_element("resoniteVersion", str)
    resonite_link_version : str = json_element("resoniteLinkVersion", str)
    unique_session_id : str = json_element("uniqueSessionId", str)
