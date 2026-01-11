#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#      >==============================================================================<
from resonitelink.json import JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("bool2")
@dataclass(slots=True)
class Vector_Bool2():
    x : Annotated[bool, JSONProperty("x")]
    y : Annotated[bool, JSONProperty("y")]


@json_model("bool3")
@dataclass(slots=True)
class Vector_Bool3():
    x : Annotated[bool, JSONProperty("x")]
    y : Annotated[bool, JSONProperty("y")]
    z : Annotated[bool, JSONProperty("z")]


@json_model("bool4")
@dataclass(slots=True)
class Vector_Bool4():
    x : Annotated[bool, JSONProperty("x")]
    y : Annotated[bool, JSONProperty("y")]
    z : Annotated[bool, JSONProperty("z")]
    w : Annotated[bool, JSONProperty("w")]


@json_model("byte2")
@dataclass(slots=True)
class Vector_Byte2():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]


@json_model("byte3")
@dataclass(slots=True)
class Vector_Byte3():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]


@json_model("byte4")
@dataclass(slots=True)
class Vector_Byte4():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]
    w : Annotated[int, JSONProperty("w")]


@json_model("sbyte2")
@dataclass(slots=True)
class Vector_SByte2():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]


@json_model("sbyte3")
@dataclass(slots=True)
class Vector_SByte3():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]


@json_model("sbyte4")
@dataclass(slots=True)
class Vector_SByte4():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]
    w : Annotated[int, JSONProperty("w")]


@json_model("ushort2")
@dataclass(slots=True)
class Vector_UShort2():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]


@json_model("ushort3")
@dataclass(slots=True)
class Vector_UShort3():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]


@json_model("ushort4")
@dataclass(slots=True)
class Vector_UShort4():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]
    w : Annotated[int, JSONProperty("w")]


@json_model("short2")
@dataclass(slots=True)
class Vector_Short2():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]


@json_model("short3")
@dataclass(slots=True)
class Vector_Short3():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]


@json_model("short4")
@dataclass(slots=True)
class Vector_Short4():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]
    w : Annotated[int, JSONProperty("w")]


@json_model("uint2")
@dataclass(slots=True)
class Vector_UInt2():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]


@json_model("uint3")
@dataclass(slots=True)
class Vector_UInt3():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]


@json_model("uint4")
@dataclass(slots=True)
class Vector_UInt4():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]
    w : Annotated[int, JSONProperty("w")]


@json_model("int2")
@dataclass(slots=True)
class Vector_Int2():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]


@json_model("int3")
@dataclass(slots=True)
class Vector_Int3():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]


@json_model("int4")
@dataclass(slots=True)
class Vector_Int4():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]
    w : Annotated[int, JSONProperty("w")]


@json_model("ulong2")
@dataclass(slots=True)
class Vector_ULong2():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]


@json_model("ulong3")
@dataclass(slots=True)
class Vector_ULong3():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]


@json_model("ulong4")
@dataclass(slots=True)
class Vector_ULong4():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]
    w : Annotated[int, JSONProperty("w")]


@json_model("long2")
@dataclass(slots=True)
class Vector_Long2():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]


@json_model("long3")
@dataclass(slots=True)
class Vector_Long3():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]


@json_model("long4")
@dataclass(slots=True)
class Vector_Long4():
    x : Annotated[int, JSONProperty("x")]
    y : Annotated[int, JSONProperty("y")]
    z : Annotated[int, JSONProperty("z")]
    w : Annotated[int, JSONProperty("w")]


@json_model("float2")
@dataclass(slots=True)
class Vector_Float2():
    x : Annotated[float, JSONProperty("x")]
    y : Annotated[float, JSONProperty("y")]


@json_model("float3")
@dataclass(slots=True)
class Vector_Float3():
    x : Annotated[float, JSONProperty("x")]
    y : Annotated[float, JSONProperty("y")]
    z : Annotated[float, JSONProperty("z")]


@json_model("float4")
@dataclass(slots=True)
class Vector_Float4():
    x : Annotated[float, JSONProperty("x")]
    y : Annotated[float, JSONProperty("y")]
    z : Annotated[float, JSONProperty("z")]
    w : Annotated[float, JSONProperty("w")]


@json_model("double2")
@dataclass(slots=True)
class Vector_Double2():
    x : Annotated[float, JSONProperty("x")]
    y : Annotated[float, JSONProperty("y")]


@json_model("double3")
@dataclass(slots=True)
class Vector_Double3():
    x : Annotated[float, JSONProperty("x")]
    y : Annotated[float, JSONProperty("y")]
    z : Annotated[float, JSONProperty("z")]


@json_model("double4")
@dataclass(slots=True)
class Vector_Double4():
    x : Annotated[float, JSONProperty("x")]
    y : Annotated[float, JSONProperty("y")]
    z : Annotated[float, JSONProperty("z")]
    w : Annotated[float, JSONProperty("w")]
