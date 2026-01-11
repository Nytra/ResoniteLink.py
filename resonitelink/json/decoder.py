from .models import JSONModel, JSONProperty, get_model_for_type_name
from typing import Any, Dict
from json import JSONDecoder
import logging


logger = logging.getLogger("ResoniteLinkJSONDecoder")
logger.setLevel(logging.DEBUG)


class ResoniteLinkJSONDecoder(JSONDecoder):
    """
    Custom decoder for ResoniteLink model classes.

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, object_hook=self._object_hook, **kwargs)
    
    @staticmethod
    def _decode_property(obj : Any, json_property : JSONProperty) -> Any:
        """
        Decodes a parsed JSON object for the given property into a suitable value.

        Parameters
        ----------
        obj : Any
            The parsed JSON object to convert into a property.
        json_property : JSONProperty
            The property to convert the object for.

        Returns
        -------
        A suitable value for the given property. This might be either
        - An instance of a `JSONModel`'s data class if the property defines a `model_type_name` or
        - The original object in case no further transformation is necessary.

        """
        model_type_name = json_property.model_type_name
        if model_type_name:
            # Property is associated with a model, ensure the value is decoded into the child model's data class.
            # This is required because the decoder processes JSON data recursively from bottom-to-top.
            # Any anonymous models (without explicit `$type` argument) will not be recognized at first, 
            # and converted to a normal `dict` by the default decoding behavior.
            # In those cases we'll have to backtrace a bit to transform those dicts into proper instances of the 
            # corresponding model's data class.
            try:
                # Attempt to find the model for the given model_type_name
                child_model = get_model_for_type_name(model_type_name)
            
            except KeyError:
                # Not found! This code is only invoked for explicit type names, so this indicates something is wrong.
                logger.warning(f"Unknown child model type name '{model_type_name}': '{obj}'")
            
            else:
                # Model exists!
                if isinstance(obj, child_model.data_class):
                    # Already the target type, nothing to do!
                    pass
                
                elif isinstance(obj, dict):
                    # Decoder produced dict, which can be replaced with the target object
                    obj = ResoniteLinkJSONDecoder._decode_model(obj, child_model)

                else:
                    # Was decoded into a non-dict type, this shouldn't happen.
                    raise TypeError(f"Expected object to transform into data class '{model_type_name}' to be of type `{type(dict)}`, not `{type(obj)}`: {obj}")
        
        # TODO: Type validation?

        return obj

    @staticmethod
    def _decode_model(obj : Any, model : JSONModel) -> Any:
        """
        Decodes a parsed JSON object for the given model into that model's data class.

        Parameters
        ----------
        obj : Any
            The parsed JSON object to be decoded.
        model : JSONModel
            The model to decode the object into.
        
        Returns
        -------
        An instance of the model's data class populated from the parsed JSON object.

        """
        data_class : Any = model.data_class()
        for name, value in obj.items():
            if name == "$type":
                # Skip the '$type' entry as we already know it
                continue
            
            try:
                # Try to get the property key associated with the name of the JSON attribute
                key = model.property_name_mapping[name]

            except KeyError:
                # JSON attribute isn't associated with a JSONProperty, log warning
                logger.warning(f"Attribute '{name}' in JSON object isn't associated with a JSONProperty of model '{model}': {obj}")

            else:
                # JSON attribute is associated with a JSONProperty
                json_property = model.properties[key]
                setattr(data_class, key, ResoniteLinkJSONDecoder._decode_property(value, json_property))
            
        return data_class

    def _object_hook(self, obj : Dict[str, Any]) -> Any:
        """
        Decoding logic to decode custom model structure.

        If the JSON object to decode specifies the type name of a registered JSONModel via $type:
        - A new instance of the model's data class is created.
        - All parameters that map to existing fields in the data class are carried over into the data class instance.
        - The data class instance is returned in place of the input object.

        Any other objects will be returned the way they were deserialized by the base class (`json.JSONDecoder`).
        This naturally supports decoding nested models due to how JSONDecoder is implemented.

        Parameters
        ----------
        obj : Dict[str, Any]
            The deserialized JSON object that was produced by the base class.
        
        Returns
        -------
        A new instance of the model's data class if the input object was identified as a registered JSONModel, or
        the unmodified input object as produced by the base class if it wasn't.

        """
        type_name : Any = obj.get('$type', None)
        if type_name is not None:
            try:
                # Try retrieving a model to check if the JSON object's $type corresponds to a registered model
                model = get_model_for_type_name(type_name)
            
            except KeyError:
                # Object has $type, but no model for that type name is registered, log warning
                logger.warning(f"Encountered JSON object with unknown type name '{type_name}': {obj}")

            else:
                # Model found, JSON object will be decoded into an instance of the model's data class
                obj = ResoniteLinkJSONDecoder._decode_model(obj, model)

        return obj
