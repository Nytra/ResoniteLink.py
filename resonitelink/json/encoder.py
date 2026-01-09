from .models import get_model_for_data_class
from typing import Any
from json import JSONEncoder

class ResoniteLinkJSONEncoder(JSONEncoder):
    """
    Custom encoder for ResoniteLink model classes.

    """
    def default(self, o : Any):
        obj_type = type(o)
        model = get_model_for_data_class(obj_type)
            