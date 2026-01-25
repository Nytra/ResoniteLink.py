#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from resonitelink.json.models import _json_property
from resonitelink.json import json_model
from dataclasses import dataclass


@json_model("t_floatQ")
@dataclass(slots=True)
class FloatQ():
    x : float = _json_property("x", float)
    y : float = _json_property("y", float)
    z : float = _json_property("z", float)
    w : float = _json_property("w", float)


@json_model("t_doubleQ")
@dataclass(slots=True)
class DoubleQ():
    x : float = _json_property("x", float)
    y : float = _json_property("y", float)
    z : float = _json_property("z", float)
    w : float = _json_property("w", float)
