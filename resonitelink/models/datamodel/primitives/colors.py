from resonitelink.json import JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("color")
@dataclass(slots=True)
class Color():
    r : Annotated[float, JSONProperty("r")]
    g : Annotated[float, JSONProperty("g")]
    b : Annotated[float, JSONProperty("b")]
    a : Annotated[float, JSONProperty("a")]


@json_model("colorX")
@dataclass(slots=True)
class ColorX():
    r : Annotated[float, JSONProperty("r")]
    g : Annotated[float, JSONProperty("g")]
    b : Annotated[float, JSONProperty("b")]
    a : Annotated[float, JSONProperty("a")]
    profile : Annotated[str, JSONProperty("profile")]


@json_model("color32")
@dataclass(slots=True)
class Color32():
    r : Annotated[int, JSONProperty("r")]
    g : Annotated[int, JSONProperty("g")]
    b : Annotated[int, JSONProperty("b")]
    a : Annotated[int, JSONProperty("a")]
