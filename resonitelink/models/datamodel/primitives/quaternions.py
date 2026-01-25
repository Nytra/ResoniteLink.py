#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from resonitelink.json import json_model, json_element


@json_model(internal_type_name="t_floatQ")
class FloatQ():
    x : float = json_element("x", float)
    y : float = json_element("y", float)
    z : float = json_element("z", float)
    w : float = json_element("w", float)


@json_model(internal_type_name="t_doubleQ")
class DoubleQ():
    x : float = json_element("x", float)
    y : float = json_element("y", float)
    z : float = json_element("z", float)
    w : float = json_element("w", float)
