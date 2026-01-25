from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("t_color", type_name_is_internal=True)
@dataclass(slots=True)
class Color():
    r : float = json_property("r", float)
    g : float = json_property("g", float)
    b : float = json_property("b", float)
    a : float = json_property("a", float)


@json_model("t_color32", type_name_is_internal=True)
@dataclass(slots=True)
class Color32():
    r : int = json_property("r", int)
    g : int = json_property("g", int)
    b : int = json_property("b", int)
    a : int = json_property("a", int)


@json_model("t_colorX", type_name_is_internal=True)
@dataclass(slots=True)
class ColorX():
    r : float = json_property("r", float)
    g : float = json_property("g", float)
    b : float = json_property("b", float)
    a : float = json_property("a", float)
    profile : str = json_property("profile", str)
