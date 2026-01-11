from .models import get_model_for_data_class
from typing import Any, List


class _MissingSentinel:
    """
    Sentinel class used to represent missing values.

    Note
    ----
    Missing values are NOT `null`, they are *missing* (i.e. they won't be included in JSON objects)!

    """
    __slots__ = ()

    def __eq__(self, other) -> bool:
        return False

    def __bool__(self) -> bool:
        return False

    def __hash__(self) -> int:
        return 0

    def __repr__(self):
        return '...'


MISSING: Any = _MissingSentinel()


def is_missing(value : Any) -> bool:
    """
    Checks wether the specified value is "missing" (i.e. is of type `_MissingSentinel`).

    Parameters
    ----------
    value : Any
        The value to check.

    Returns
    -------
    `True` if the provided value has the `_MissingSentinel` type. 

    """
    return type(value) is _MissingSentinel


def get_object_structure_str(obj : Any, print_missing : bool = False, prefix : str = "| ") -> str:
    """
    Produces a string for the given object that represents that object's structure.
    If that object is an instance of a registered model's data class, it will be resolved recursively.
    This is mainly intended for debugging purposes.

    Parameters
    ----------
    obj : Any
        The object to analyze.
    print_missing : bool
        Wether to list missing property members when resolving model structure.
    prefix : str
        String to prefix before message. Each recursion level pads this with leading spaces.
    
    Returns
    -------
    A string representing the object's structure.

    """
    structure_str : str
    try:
        # Attempt to 
        model = get_model_for_data_class(type(obj))
    
    except KeyError:
        # Not a model
        structure_str = f"Type {type(obj)}: {obj}"
    
    else:
        # Model class, resolve children
        property_lines : List[str] = []
        for key, json_property in model.properties.items():
            if hasattr(obj, key):
                # Value for key present
                property_lines.append(f"- {key}: {get_object_structure_str(getattr(obj, key), prefix=f"{prefix}  ")}")
            
            elif print_missing:
                # Value for key missing & missing values should be printed
                property_lines.append(f"{key}: MISSING")
        
        structure_str = f"Type {type(obj)} (Data class for model '{model.type_name}'):\n{prefix}{f'\n{prefix}'.join(property_lines)}"

    return structure_str
