#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from resonitelink.models.datamodel.primitives import *
from resonitelink.models.datamodel import Member, SyncArray
from resonitelink.json.models import _json_property, _JSONPropertyType
from resonitelink.json import json_model
from dataclasses import dataclass
from decimal import Decimal
from typing import List


@json_model("bool[]", Member)
@dataclass(slots=True)
class Array_Bool(SyncArray):
    values : List[bool] = _json_property("values", bool, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "bool"


@json_model("byte[]", Member)
@dataclass(slots=True)
class Array_Byte(SyncArray):
    values : List[int] = _json_property("values", int, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "byte"


@json_model("sbyte[]", Member)
@dataclass(slots=True)
class Array_SByte(SyncArray):
    values : List[int] = _json_property("values", int, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "sbyte"


@json_model("ushort[]", Member)
@dataclass(slots=True)
class Array_UShort(SyncArray):
    values : List[int] = _json_property("values", int, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "ushort"


@json_model("short[]", Member)
@dataclass(slots=True)
class Array_Short(SyncArray):
    values : List[int] = _json_property("values", int, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "short"


@json_model("uint[]", Member)
@dataclass(slots=True)
class Array_UInt(SyncArray):
    values : List[int] = _json_property("values", int, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "uint"


@json_model("int[]", Member)
@dataclass(slots=True)
class Array_Int(SyncArray):
    values : List[int] = _json_property("values", int, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "int"


@json_model("ulong[]", Member)
@dataclass(slots=True)
class Array_ULong(SyncArray):
    values : List[int] = _json_property("values", int, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "ulong"


@json_model("long[]", Member)
@dataclass(slots=True)
class Array_Long(SyncArray):
    values : List[int] = _json_property("values", int, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "long"


@json_model("float[]", Member)
@dataclass(slots=True)
class Array_Float(SyncArray):
    values : List[float] = _json_property("values", float, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "float"


@json_model("double[]", Member)
@dataclass(slots=True)
class Array_Double(SyncArray):
    values : List[float] = _json_property("values", float, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "double"


@json_model("decimal[]", Member)
@dataclass(slots=True)
class Array_Decimal(SyncArray):
    values : List[Decimal] = _json_property("values", Decimal, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "decimal"


@json_model("char[]", Member)
@dataclass(slots=True)
class Array_Char(SyncArray):
    values : List[str] = _json_property("values", str, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "char"


@json_model("string[]", Member)
@dataclass(slots=True)
class Array_String(SyncArray):
    values : List[str] = _json_property("values", str, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "string"


@json_model("Uri[]", Member)
@dataclass(slots=True)
class Array_Uri(SyncArray):
    values : List[str] = _json_property("values", str, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "Uri"


@json_model("DateTime[]", Member)
@dataclass(slots=True)
class Array_DateTime(SyncArray):
    values : List[str] = _json_property("values", str, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "DateTime"


@json_model("TimeSpan[]", Member)
@dataclass(slots=True)
class Array_TimeSpan(SyncArray):
    values : List[str] = _json_property("values", str, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "TimeSpan"


@json_model("color[]", Member)
@dataclass(slots=True)
class Array_Color(SyncArray):
    values : List[Color] = _json_property("values", Color, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "color"


@json_model("colorX[]", Member)
@dataclass(slots=True)
class Array_ColorX(SyncArray):
    values : List[ColorX] = _json_property("values", ColorX, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "colorX"


@json_model("color32[]", Member)
@dataclass(slots=True)
class Array_Color32(SyncArray):
    values : List[Color32] = _json_property("values", Color32, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "color32"


@json_model("floatQ[]", Member)
@dataclass(slots=True)
class Array_FloatQ(SyncArray):
    values : List[FloatQ] = _json_property("values", FloatQ, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "floatQ"


@json_model("doubleQ[]", Member)
@dataclass(slots=True)
class Array_DoubleQ(SyncArray):
    values : List[DoubleQ] = _json_property("values", DoubleQ, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "doubleQ"


@json_model("bool2[]", Member)
@dataclass(slots=True)
class Array_Bool2(SyncArray):
    values : List[Bool2] = _json_property("values", Bool2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "bool2"


@json_model("bool3[]", Member)
@dataclass(slots=True)
class Array_Bool3(SyncArray):
    values : List[Bool3] = _json_property("values", Bool3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "bool3"


@json_model("bool4[]", Member)
@dataclass(slots=True)
class Array_Bool4(SyncArray):
    values : List[Bool4] = _json_property("values", Bool4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "bool4"


@json_model("byte2[]", Member)
@dataclass(slots=True)
class Array_Byte2(SyncArray):
    values : List[Byte2] = _json_property("values", Byte2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "byte2"


@json_model("byte3[]", Member)
@dataclass(slots=True)
class Array_Byte3(SyncArray):
    values : List[Byte3] = _json_property("values", Byte3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "byte3"


@json_model("byte4[]", Member)
@dataclass(slots=True)
class Array_Byte4(SyncArray):
    values : List[Byte4] = _json_property("values", Byte4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "byte4"


@json_model("sbyte2[]", Member)
@dataclass(slots=True)
class Array_Sbyte2(SyncArray):
    values : List[SByte2] = _json_property("values", SByte2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "sbyte2"


@json_model("sbyte3[]", Member)
@dataclass(slots=True)
class Array_Sbyte3(SyncArray):
    values : List[SByte3] = _json_property("values", SByte3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "sbyte3"


@json_model("sbyte4[]", Member)
@dataclass(slots=True)
class Array_Sbyte4(SyncArray):
    values : List[SByte4] = _json_property("values", SByte4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "sbyte4"


@json_model("ushort2[]", Member)
@dataclass(slots=True)
class Array_Ushort2(SyncArray):
    values : List[UShort2] = _json_property("values", UShort2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "ushort2"


@json_model("ushort3[]", Member)
@dataclass(slots=True)
class Array_Ushort3(SyncArray):
    values : List[UShort3] = _json_property("values", UShort3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "ushort3"


@json_model("ushort4[]", Member)
@dataclass(slots=True)
class Array_Ushort4(SyncArray):
    values : List[UShort4] = _json_property("values", UShort4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "ushort4"


@json_model("short2[]", Member)
@dataclass(slots=True)
class Array_Short2(SyncArray):
    values : List[Short2] = _json_property("values", Short2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "short2"


@json_model("short3[]", Member)
@dataclass(slots=True)
class Array_Short3(SyncArray):
    values : List[Short3] = _json_property("values", Short3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "short3"


@json_model("short4[]", Member)
@dataclass(slots=True)
class Array_Short4(SyncArray):
    values : List[Short4] = _json_property("values", Short4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "short4"


@json_model("uint2[]", Member)
@dataclass(slots=True)
class Array_Uint2(SyncArray):
    values : List[UInt2] = _json_property("values", UInt2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "uint2"


@json_model("uint3[]", Member)
@dataclass(slots=True)
class Array_Uint3(SyncArray):
    values : List[UInt3] = _json_property("values", UInt3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "uint3"


@json_model("uint4[]", Member)
@dataclass(slots=True)
class Array_Uint4(SyncArray):
    values : List[UInt4] = _json_property("values", UInt4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "uint4"


@json_model("int2[]", Member)
@dataclass(slots=True)
class Array_Int2(SyncArray):
    values : List[Int2] = _json_property("values", Int2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "int2"


@json_model("int3[]", Member)
@dataclass(slots=True)
class Array_Int3(SyncArray):
    values : List[Int3] = _json_property("values", Int3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "int3"


@json_model("int4[]", Member)
@dataclass(slots=True)
class Array_Int4(SyncArray):
    values : List[Int4] = _json_property("values", Int4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "int4"


@json_model("ulong2[]", Member)
@dataclass(slots=True)
class Array_Ulong2(SyncArray):
    values : List[ULong2] = _json_property("values", ULong2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "ulong2"


@json_model("ulong3[]", Member)
@dataclass(slots=True)
class Array_Ulong3(SyncArray):
    values : List[ULong3] = _json_property("values", ULong3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "ulong3"


@json_model("ulong4[]", Member)
@dataclass(slots=True)
class Array_Ulong4(SyncArray):
    values : List[ULong4] = _json_property("values", ULong4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "ulong4"


@json_model("long2[]", Member)
@dataclass(slots=True)
class Array_Long2(SyncArray):
    values : List[Long2] = _json_property("values", Long2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "long2"


@json_model("long3[]", Member)
@dataclass(slots=True)
class Array_Long3(SyncArray):
    values : List[Long3] = _json_property("values", Long3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "long3"


@json_model("long4[]", Member)
@dataclass(slots=True)
class Array_Long4(SyncArray):
    values : List[Long4] = _json_property("values", Long4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "long4"


@json_model("float2[]", Member)
@dataclass(slots=True)
class Array_Float2(SyncArray):
    values : List[Float2] = _json_property("values", Float2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "float2"


@json_model("float3[]", Member)
@dataclass(slots=True)
class Array_Float3(SyncArray):
    values : List[Float3] = _json_property("values", Float3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "float3"


@json_model("float4[]", Member)
@dataclass(slots=True)
class Array_Float4(SyncArray):
    values : List[Float4] = _json_property("values", Float4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "float4"


@json_model("double2[]", Member)
@dataclass(slots=True)
class Array_Double2(SyncArray):
    values : List[Double2] = _json_property("values", Double2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "double2"


@json_model("double3[]", Member)
@dataclass(slots=True)
class Array_Double3(SyncArray):
    values : List[Double3] = _json_property("values", Double3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "double3"


@json_model("double4[]", Member)
@dataclass(slots=True)
class Array_Double4(SyncArray):
    values : List[Double4] = _json_property("values", Double4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "double4"


@json_model("float2x2[]", Member)
@dataclass(slots=True)
class Array_Float2x2(SyncArray):
    values : List[Float2x2] = _json_property("values", Float2x2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "float2x2"


@json_model("float3x3[]", Member)
@dataclass(slots=True)
class Array_Float3x3(SyncArray):
    values : List[Float3x3] = _json_property("values", Float3x3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "float3x3"


@json_model("float4x4[]", Member)
@dataclass(slots=True)
class Array_Float4x4(SyncArray):
    values : List[Float4x4] = _json_property("values", Float4x4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "float4x4"


@json_model("double2x2[]", Member)
@dataclass(slots=True)
class Array_Double2x2(SyncArray):
    values : List[Double2x2] = _json_property("values", Double2x2, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "double2x2"


@json_model("double3x3[]", Member)
@dataclass(slots=True)
class Array_Double3x3(SyncArray):
    values : List[Double3x3] = _json_property("values", Double3x3, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "double3x3"


@json_model("double4x4[]", Member)
@dataclass(slots=True)
class Array_Double4x4(SyncArray):
    values : List[Double4x4] = _json_property("values", Double4x4, _JSONPropertyType.LIST)
    
    @property
    def element_type(self) -> str:
        return "double4x4"
