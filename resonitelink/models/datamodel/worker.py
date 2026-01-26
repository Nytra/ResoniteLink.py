from resonitelink.json import abstract_json_model, json_element, MISSING
from abc import ABC


@abstract_json_model()
class Worker(ABC):
    id : str = json_element("id", str, default=MISSING)
    is_reference_only : bool = json_element("isReferenceOnly", bool, default=MISSING)
