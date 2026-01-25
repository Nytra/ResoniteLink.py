from resonitelink.json import json_model, json_element


@json_model(internal_type_name="t_color")
class Color():
    r : float = json_element("r", float)
    g : float = json_element("g", float)
    b : float = json_element("b", float)
    a : float = json_element("a", float)


@json_model(internal_type_name="t_color32")
class Color32():
    r : int = json_element("r", int)
    g : int = json_element("g", int)
    b : int = json_element("b", int)
    a : int = json_element("a", int)


@json_model(internal_type_name="t_colorX")
class ColorX():
    r : float = json_element("r", float)
    g : float = json_element("g", float)
    b : float = json_element("b", float)
    a : float = json_element("a", float)
    profile : str = json_element("profile", str)
