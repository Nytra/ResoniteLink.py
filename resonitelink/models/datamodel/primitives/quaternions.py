#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("t_floatQ")
@dataclass(slots=True)
class FloatQ():
    x : float = json_property("x", float)
    y : float = json_property("y", float)
    z : float = json_property("z", float)
    w : float = json_property("w", float)


@json_model("t_doubleQ")
@dataclass(slots=True)
class DoubleQ():
    x : float = json_property("x", float)
    y : float = json_property("y", float)
    z : float = json_property("z", float)
    w : float = json_property("w", float)
