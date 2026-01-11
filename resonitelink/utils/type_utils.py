from resonitelink.models.datamodel.primitives import Color, ColorX, Color32
from dataclasses import dataclass
from decimal import Decimal
from typing import Type


@dataclass(slots=True)
class LibraryTypeInfo():
    type_name : str
    type : Type


type_mappings = {
    "bool": LibraryTypeInfo("Bool", bool),
    "byte": LibraryTypeInfo("Byte", int),
    "sbyte": LibraryTypeInfo("SByte", int),
    "ushort": LibraryTypeInfo("UShort", int),
    "short": LibraryTypeInfo("Short", int),
    "uint": LibraryTypeInfo("UInt", int),
    "int": LibraryTypeInfo("Int", int),
    "ulong": LibraryTypeInfo("ULong", int),
    "long": LibraryTypeInfo("Long", int),
    "float": LibraryTypeInfo("Float", float),
    "double": LibraryTypeInfo("Double", float),
    "decimal": LibraryTypeInfo("Decimal", Decimal),
    "char": LibraryTypeInfo("Char", str),
    "color": LibraryTypeInfo("Color", Color),
    "colorX": LibraryTypeInfo("ColorX", ColorX),
    "color32": LibraryTypeInfo("Color32", Color32),
    "string": LibraryTypeInfo("String", str),
    "Uri": LibraryTypeInfo("Uri", str)
}
