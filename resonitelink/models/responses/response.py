from resonitelink.json import abstract_json_model, json_model, json_element
from abc import ABC


@abstract_json_model()
class Response(ABC):
    source_message_id : str = json_element("sourceMessageId", str)
    success : bool = json_element("success", bool)
    error_info : str = json_element("errorInfo", str)


@json_model("response", derived_from=Response)
class GenericResponse(Response):
    pass
