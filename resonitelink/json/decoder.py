from .models import JSONModel, JSONProperty, JSONPropertyType
from typing import Any, Dict
from json import JSONDecoder
import logging

__all__ = (
    'ResoniteLinkJSONDecoder',
)

logger = logging.getLogger("ResoniteLinkJSONDecoder")
logger.setLevel(logging.DEBUG)


class ResoniteLinkJSONDecoder(JSONDecoder):
    """
    Custom decoder for ResoniteLink model classes.

    """
    _root_model : JSONModel

    def __init__(self, *args, root_model : JSONModel, **kwargs):
        if not root_model:
            raise ValueError("No root model provided for decoder!")

        self._root_model = root_model

        super().__init__(*args, **kwargs)
    
    @staticmethod
    def _decode_element(obj : Any, prop : JSONProperty):
        """
        Processes a single element of a property (properties have multiple elements if they are List or Dicts).

        """
        if isinstance(obj, dict):
            # We assume that any JSON-Dictionary should map to a registered model
            try:
                # Check if the property is a child model.
                if '$type' in obj:
                    # Include type name, this allows resolving derived or global models by their type name.
                    child_model = JSONModel.find_model(prop.element_type, obj['$type'])
                else:
                    # Can only be exact match
                    child_model = JSONModel.find_model(prop.element_type)

            except KeyError:
                # No model found, raw dict will be kept in decoded data, log warning.
                logger.warning(f"Encountered JSON-Dictionary that didn't resolve to a registered model: {obj}")
            
            else:
                # Resolve child model recursively.
                obj = ResoniteLinkJSONDecoder._decode_model(obj, child_model)
        
        else:
            # Element is not an object and will be kept in the decoded data as-is.
            # TODO: Type validation?
            pass

        return obj
    
    @staticmethod
    def _decode_property(obj : Any, prop : JSONProperty) -> Any:
        """
        Decodes a parsed JSON object for the given property into a suitable value.

        Parameters
        ----------
        obj : Any
            The parsed JSON object to convert into a property.
        prop : JSONProperty
            The property to convert the object for.

        Returns
        -------
        A suitable value for the given property. This might be either
        - An instance of a `JSONModel`'s data class if the property defines a `model_type_name` or
        - The original object in case no further transformation is necessary.

        """
        if obj is None:
            # Object not provided, that's okay, but nothing to do!
            pass # TODO this isn't nice! We should skip the object entirely.
        
        elif prop.property_type == JSONPropertyType.ELEMENT:
            # Resolve property as single element
            obj = ResoniteLinkJSONDecoder._decode_element(obj, prop)
        
        elif prop.property_type == JSONPropertyType.LIST:
            # Resolve property as list
            if not isinstance(obj, list): 
                raise TypeError(f"Error decoding JSON-Data into {prop}: Object expected to be of type {list}, not {type(obj)}!")
            
            obj = [ ResoniteLinkJSONDecoder._decode_element(o, prop) for o in obj ]

        elif prop.property_type == JSONPropertyType.DICT:
            # Resolve property as dict
            if not isinstance(obj, dict): 
                raise TypeError(f"Error decoding JSON-Data into {prop}: Object expected to be of type {dict}, not {type(obj)}!")
            
            obj = { k: ResoniteLinkJSONDecoder._decode_element(v, prop) for k, v in obj.items() }

        else:
            raise ValueError(f"Error decoding JSON-Data into {prop}: Invalid JSONPropertyType: {prop.property_type}")

        return obj

    @staticmethod
    def _decode_model(obj : Dict[str, Any], model : JSONModel) -> Any:
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
                # NOTE: The $type property does not have to be present in JSON-Object if its type is not ambiguous.
                if value != model.type_name:
                    # Type name mismatch!
                    raise ValueError(f"Error decoding JSON-Data into {model}: Type name mismatch! JSON-Object: '{value}', Model: '{model.type_name}'")
                
                else:
                    # Type is explicitly defined and matches the model we're decoding into, all is good.
                    pass
            
            try:
                # Try to get the property key associated with the name of the JSON attribute.
                key = model.property_name_mapping[name]

            except KeyError:
                # JSON attribute isn't associated with a JSONProperty, log warning.
                logger.warning(f"Encountered unknown key while decoding JSON-Object into model '{model}': '{name}'")

            else:
                # JSON attribute is associated with a JSONProperty
                prop = model.properties[key]
                setattr(data_class, key, ResoniteLinkJSONDecoder._decode_property(value, prop))
            
        return data_class
    

    def decode(self, *args, **kwargs) -> Any:
        """
        Python's `JSONDecoder` provides the ability to define a custom `object_hook` which is invoked for every parsed JSON-Object,
        however that is unsuitable for our use-case. The reason for that is that this `object_hook` is invoked recursively from
        bottom to top. That means that elements that are nested deep in the structure are evaluated before elements higher up.
        This is unfortunately exactly the opposite of what we need. So instead, this decoder works the following way:

        1. Run the default decoder first, which decodes the JSON string / bytes into a raw python object.
        2. Take the resulting raw object and attept to recursively decode it into the decoder's root model.

        That root model is than returned.

        """
        raw_obj = super().decode(*args, **kwargs)
        model_obj = ResoniteLinkJSONDecoder._decode_model(raw_obj, self._root_model)
        return model_obj
