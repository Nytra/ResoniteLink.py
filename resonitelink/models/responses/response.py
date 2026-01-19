from resonitelink.json import json_model, json_property
from dataclasses import dataclass
from abc import ABC


@dataclass(slots=True)
class Response(ABC):
    source_message_id : str = json_property("sourceMessageId", str)
    success : bool = json_property("success", bool)
    error_info : str = json_property("errorInfo", str)


@json_model("response", derived_from=Response)
@dataclass(slots=True)
class GenericResponse(Response):
    pass
