from typing import TypeVar, Generic, Type
import logging

logger = logging.getLogger("ResoniteLinkModels")
logger.setLevel(logging.DEBUG)

class JSONProperty():
    """
    Denotes a JSON property of a model data class that will be picked up by the serializer / deserializer.
    This should be added as an annotation to the members that should be JSON serialized / deserialized:
        
        @model("example")
        def ExampleModel():
            example_str : typing.Annotated[str, JsonProperty("exampleStr")]
            example_int : typing.Annotated[int, JsonProperty("exampleInt")]
    
    """
    _name : str

    def __init__(self, name : str):
        self._name = name

_models = []


D = TypeVar("D")
class Model(Generic[D]):
    """
    Base class for JSON serializable / deserializable models.
    
    WARNING
    ~~~~~~~
    Don't instantiate this directly. Use the `model` decorator on the data class instead.
    
    """
    _type_id : str
    _data_type : Type

    def __init__(self, type_id : str, data_type : Type):
        logger.debug(f"Instantiating model class for '{type_id}' with data type '{data_type}'")
        self._type_id = type_id
        self._data_type = data_type


def model(type_id : str):
    """
    Class decorator to define model classes.

    """
    logger.debug(f"Decorator for model type '{type_id}'")
    def _model_decorator(data_class : Type):
        _models.append(Model(type_id=type_id, data_type=data_class))
        return data_class

    return _model_decorator