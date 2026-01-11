from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("response")
@dataclass(slots=True)
class Response():
    source_message_id : Annotated[str, JSONProperty("sourceMessageId")] = MISSING
    success : Annotated[bool, JSONProperty("success")] = MISSING
    error_info : Annotated[str, JSONProperty("errorInfo")] = MISSING
