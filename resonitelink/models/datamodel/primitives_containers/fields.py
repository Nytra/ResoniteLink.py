#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from resonitelink.models.datamodel.primitives import *
from resonitelink.models.datamodel import Member, Field
from resonitelink.json import json_model, json_property
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@json_model("bool", Member)
@dataclass(slots=True)
class Field_Bool(Field):
    value : bool = json_property("value", bool)
    
    @property
    def value_type_name(self) -> str:
        return "bool"


@json_model("bool?", Member)
@dataclass(slots=True)
class Field_Nullable_Bool(Field):
    value : Optional[bool] = json_property("value", bool)
    
    @property
    def value_type_name(self) -> str:
        return "bool?"


@json_model("byte", Member)
@dataclass(slots=True)
class Field_Byte(Field):
    value : int = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "byte"


@json_model("byte?", Member)
@dataclass(slots=True)
class Field_Nullable_Byte(Field):
    value : Optional[int] = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "byte?"


@json_model("sbyte", Member)
@dataclass(slots=True)
class Field_SByte(Field):
    value : int = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte"


@json_model("sbyte?", Member)
@dataclass(slots=True)
class Field_Nullable_SByte(Field):
    value : Optional[int] = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte?"


@json_model("ushort", Member)
@dataclass(slots=True)
class Field_UShort(Field):
    value : int = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "ushort"


@json_model("ushort?", Member)
@dataclass(slots=True)
class Field_Nullable_UShort(Field):
    value : Optional[int] = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "ushort?"


@json_model("short", Member)
@dataclass(slots=True)
class Field_Short(Field):
    value : int = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "short"


@json_model("short?", Member)
@dataclass(slots=True)
class Field_Nullable_Short(Field):
    value : Optional[int] = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "short?"


@json_model("uint", Member)
@dataclass(slots=True)
class Field_UInt(Field):
    value : int = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "uint"


@json_model("uint?", Member)
@dataclass(slots=True)
class Field_Nullable_UInt(Field):
    value : Optional[int] = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "uint?"


@json_model("int", Member)
@dataclass(slots=True)
class Field_Int(Field):
    value : int = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "int"


@json_model("int?", Member)
@dataclass(slots=True)
class Field_Nullable_Int(Field):
    value : Optional[int] = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "int?"


@json_model("ulong", Member)
@dataclass(slots=True)
class Field_ULong(Field):
    value : int = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "ulong"


@json_model("ulong?", Member)
@dataclass(slots=True)
class Field_Nullable_ULong(Field):
    value : Optional[int] = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "ulong?"


@json_model("long", Member)
@dataclass(slots=True)
class Field_Long(Field):
    value : int = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "long"


@json_model("long?", Member)
@dataclass(slots=True)
class Field_Nullable_Long(Field):
    value : Optional[int] = json_property("value", int)
    
    @property
    def value_type_name(self) -> str:
        return "long?"


@json_model("float", Member)
@dataclass(slots=True)
class Field_Float(Field):
    value : float = json_property("value", float)
    
    @property
    def value_type_name(self) -> str:
        return "float"


@json_model("float?", Member)
@dataclass(slots=True)
class Field_Nullable_Float(Field):
    value : Optional[float] = json_property("value", float)
    
    @property
    def value_type_name(self) -> str:
        return "float?"


@json_model("double", Member)
@dataclass(slots=True)
class Field_Double(Field):
    value : float = json_property("value", float)
    
    @property
    def value_type_name(self) -> str:
        return "double"


@json_model("double?", Member)
@dataclass(slots=True)
class Field_Nullable_Double(Field):
    value : Optional[float] = json_property("value", float)
    
    @property
    def value_type_name(self) -> str:
        return "double?"


@json_model("decimal", Member)
@dataclass(slots=True)
class Field_Decimal(Field):
    value : Decimal = json_property("value", Decimal)
    
    @property
    def value_type_name(self) -> str:
        return "decimal"


@json_model("decimal?", Member)
@dataclass(slots=True)
class Field_Nullable_Decimal(Field):
    value : Optional[Decimal] = json_property("value", Decimal)
    
    @property
    def value_type_name(self) -> str:
        return "decimal?"


@json_model("char", Member)
@dataclass(slots=True)
class Field_Char(Field):
    value : str = json_property("value", str)
    
    @property
    def value_type_name(self) -> str:
        return "char"


@json_model("char?", Member)
@dataclass(slots=True)
class Field_Nullable_Char(Field):
    value : Optional[str] = json_property("value", str)
    
    @property
    def value_type_name(self) -> str:
        return "char?"


@json_model("string", Member)
@dataclass(slots=True)
class Field_String(Field):
    value : str = json_property("value", str)
    
    @property
    def value_type_name(self) -> str:
        return "string"




@json_model("Uri", Member)
@dataclass(slots=True)
class Field_Uri(Field):
    value : str = json_property("value", str)
    
    @property
    def value_type_name(self) -> str:
        return "Uri"




@json_model("DateTime", Member)
@dataclass(slots=True)
class Field_DateTime(Field):
    value : str = json_property("value", str)
    
    @property
    def value_type_name(self) -> str:
        return "DateTime"


@json_model("DateTime?", Member)
@dataclass(slots=True)
class Field_Nullable_DateTime(Field):
    value : Optional[str] = json_property("value", str)
    
    @property
    def value_type_name(self) -> str:
        return "DateTime?"


@json_model("TimeSpan", Member)
@dataclass(slots=True)
class Field_TimeSpan(Field):
    value : str = json_property("value", str)
    
    @property
    def value_type_name(self) -> str:
        return "TimeSpan"


@json_model("TimeSpan?", Member)
@dataclass(slots=True)
class Field_Nullable_TimeSpan(Field):
    value : Optional[str] = json_property("value", str)
    
    @property
    def value_type_name(self) -> str:
        return "TimeSpan?"


@json_model("color", Member)
@dataclass(slots=True)
class Field_Color(Field):
    value : Color = json_property("value", Color)
    
    @property
    def value_type_name(self) -> str:
        return "color"


@json_model("color?", Member)
@dataclass(slots=True)
class Field_Nullable_Color(Field):
    value : Optional[Color] = json_property("value", Color)
    
    @property
    def value_type_name(self) -> str:
        return "color?"


@json_model("colorX", Member)
@dataclass(slots=True)
class Field_ColorX(Field):
    value : ColorX = json_property("value", ColorX)
    
    @property
    def value_type_name(self) -> str:
        return "colorX"


@json_model("colorX?", Member)
@dataclass(slots=True)
class Field_Nullable_ColorX(Field):
    value : Optional[ColorX] = json_property("value", ColorX)
    
    @property
    def value_type_name(self) -> str:
        return "colorX?"


@json_model("color32", Member)
@dataclass(slots=True)
class Field_Color32(Field):
    value : Color32 = json_property("value", Color32)
    
    @property
    def value_type_name(self) -> str:
        return "color32"


@json_model("color32?", Member)
@dataclass(slots=True)
class Field_Nullable_Color32(Field):
    value : Optional[Color32] = json_property("value", Color32)
    
    @property
    def value_type_name(self) -> str:
        return "color32?"


@json_model("floatQ", Member)
@dataclass(slots=True)
class Field_FloatQ(Field):
    value : FloatQ = json_property("value", FloatQ)
    
    @property
    def value_type_name(self) -> str:
        return "floatQ"


@json_model("floatQ?", Member)
@dataclass(slots=True)
class Field_Nullable_FloatQ(Field):
    value : Optional[FloatQ] = json_property("value", FloatQ)
    
    @property
    def value_type_name(self) -> str:
        return "floatQ?"


@json_model("doubleQ", Member)
@dataclass(slots=True)
class Field_DoubleQ(Field):
    value : DoubleQ = json_property("value", DoubleQ)
    
    @property
    def value_type_name(self) -> str:
        return "doubleQ"


@json_model("doubleQ?", Member)
@dataclass(slots=True)
class Field_Nullable_DoubleQ(Field):
    value : Optional[DoubleQ] = json_property("value", DoubleQ)
    
    @property
    def value_type_name(self) -> str:
        return "doubleQ?"


@json_model("bool2", Member)
@dataclass(slots=True)
class Field_Bool2(Field):
    value : Bool2 = json_property("value", Bool2)
    
    @property
    def value_type_name(self) -> str:
        return "bool2"


@json_model("bool2?", Member)
@dataclass(slots=True)
class Field_Nullable_Bool2(Field):
    value : Optional[Bool2] = json_property("value", Bool2)
    
    @property
    def value_type_name(self) -> str:
        return "bool2?"


@json_model("bool3", Member)
@dataclass(slots=True)
class Field_Bool3(Field):
    value : Bool3 = json_property("value", Bool3)
    
    @property
    def value_type_name(self) -> str:
        return "bool3"


@json_model("bool3?", Member)
@dataclass(slots=True)
class Field_Nullable_Bool3(Field):
    value : Optional[Bool3] = json_property("value", Bool3)
    
    @property
    def value_type_name(self) -> str:
        return "bool3?"


@json_model("bool4", Member)
@dataclass(slots=True)
class Field_Bool4(Field):
    value : Bool4 = json_property("value", Bool4)
    
    @property
    def value_type_name(self) -> str:
        return "bool4"


@json_model("bool4?", Member)
@dataclass(slots=True)
class Field_Nullable_Bool4(Field):
    value : Optional[Bool4] = json_property("value", Bool4)
    
    @property
    def value_type_name(self) -> str:
        return "bool4?"


@json_model("byte2", Member)
@dataclass(slots=True)
class Field_Byte2(Field):
    value : Byte2 = json_property("value", Byte2)
    
    @property
    def value_type_name(self) -> str:
        return "byte2"


@json_model("byte2?", Member)
@dataclass(slots=True)
class Field_Nullable_Byte2(Field):
    value : Optional[Byte2] = json_property("value", Byte2)
    
    @property
    def value_type_name(self) -> str:
        return "byte2?"


@json_model("byte3", Member)
@dataclass(slots=True)
class Field_Byte3(Field):
    value : Byte3 = json_property("value", Byte3)
    
    @property
    def value_type_name(self) -> str:
        return "byte3"


@json_model("byte3?", Member)
@dataclass(slots=True)
class Field_Nullable_Byte3(Field):
    value : Optional[Byte3] = json_property("value", Byte3)
    
    @property
    def value_type_name(self) -> str:
        return "byte3?"


@json_model("byte4", Member)
@dataclass(slots=True)
class Field_Byte4(Field):
    value : Byte4 = json_property("value", Byte4)
    
    @property
    def value_type_name(self) -> str:
        return "byte4"


@json_model("byte4?", Member)
@dataclass(slots=True)
class Field_Nullable_Byte4(Field):
    value : Optional[Byte4] = json_property("value", Byte4)
    
    @property
    def value_type_name(self) -> str:
        return "byte4?"


@json_model("sbyte2", Member)
@dataclass(slots=True)
class Field_Sbyte2(Field):
    value : SByte2 = json_property("value", SByte2)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte2"


@json_model("sbyte2?", Member)
@dataclass(slots=True)
class Field_Nullable_Sbyte2(Field):
    value : Optional[SByte2] = json_property("value", SByte2)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte2?"


@json_model("sbyte3", Member)
@dataclass(slots=True)
class Field_Sbyte3(Field):
    value : SByte3 = json_property("value", SByte3)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte3"


@json_model("sbyte3?", Member)
@dataclass(slots=True)
class Field_Nullable_Sbyte3(Field):
    value : Optional[SByte3] = json_property("value", SByte3)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte3?"


@json_model("sbyte4", Member)
@dataclass(slots=True)
class Field_Sbyte4(Field):
    value : SByte4 = json_property("value", SByte4)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte4"


@json_model("sbyte4?", Member)
@dataclass(slots=True)
class Field_Nullable_Sbyte4(Field):
    value : Optional[SByte4] = json_property("value", SByte4)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte4?"


@json_model("ushort2", Member)
@dataclass(slots=True)
class Field_Ushort2(Field):
    value : UShort2 = json_property("value", UShort2)
    
    @property
    def value_type_name(self) -> str:
        return "ushort2"


@json_model("ushort2?", Member)
@dataclass(slots=True)
class Field_Nullable_Ushort2(Field):
    value : Optional[UShort2] = json_property("value", UShort2)
    
    @property
    def value_type_name(self) -> str:
        return "ushort2?"


@json_model("ushort3", Member)
@dataclass(slots=True)
class Field_Ushort3(Field):
    value : UShort3 = json_property("value", UShort3)
    
    @property
    def value_type_name(self) -> str:
        return "ushort3"


@json_model("ushort3?", Member)
@dataclass(slots=True)
class Field_Nullable_Ushort3(Field):
    value : Optional[UShort3] = json_property("value", UShort3)
    
    @property
    def value_type_name(self) -> str:
        return "ushort3?"


@json_model("ushort4", Member)
@dataclass(slots=True)
class Field_Ushort4(Field):
    value : UShort4 = json_property("value", UShort4)
    
    @property
    def value_type_name(self) -> str:
        return "ushort4"


@json_model("ushort4?", Member)
@dataclass(slots=True)
class Field_Nullable_Ushort4(Field):
    value : Optional[UShort4] = json_property("value", UShort4)
    
    @property
    def value_type_name(self) -> str:
        return "ushort4?"


@json_model("short2", Member)
@dataclass(slots=True)
class Field_Short2(Field):
    value : Short2 = json_property("value", Short2)
    
    @property
    def value_type_name(self) -> str:
        return "short2"


@json_model("short2?", Member)
@dataclass(slots=True)
class Field_Nullable_Short2(Field):
    value : Optional[Short2] = json_property("value", Short2)
    
    @property
    def value_type_name(self) -> str:
        return "short2?"


@json_model("short3", Member)
@dataclass(slots=True)
class Field_Short3(Field):
    value : Short3 = json_property("value", Short3)
    
    @property
    def value_type_name(self) -> str:
        return "short3"


@json_model("short3?", Member)
@dataclass(slots=True)
class Field_Nullable_Short3(Field):
    value : Optional[Short3] = json_property("value", Short3)
    
    @property
    def value_type_name(self) -> str:
        return "short3?"


@json_model("short4", Member)
@dataclass(slots=True)
class Field_Short4(Field):
    value : Short4 = json_property("value", Short4)
    
    @property
    def value_type_name(self) -> str:
        return "short4"


@json_model("short4?", Member)
@dataclass(slots=True)
class Field_Nullable_Short4(Field):
    value : Optional[Short4] = json_property("value", Short4)
    
    @property
    def value_type_name(self) -> str:
        return "short4?"


@json_model("uint2", Member)
@dataclass(slots=True)
class Field_Uint2(Field):
    value : UInt2 = json_property("value", UInt2)
    
    @property
    def value_type_name(self) -> str:
        return "uint2"


@json_model("uint2?", Member)
@dataclass(slots=True)
class Field_Nullable_Uint2(Field):
    value : Optional[UInt2] = json_property("value", UInt2)
    
    @property
    def value_type_name(self) -> str:
        return "uint2?"


@json_model("uint3", Member)
@dataclass(slots=True)
class Field_Uint3(Field):
    value : UInt3 = json_property("value", UInt3)
    
    @property
    def value_type_name(self) -> str:
        return "uint3"


@json_model("uint3?", Member)
@dataclass(slots=True)
class Field_Nullable_Uint3(Field):
    value : Optional[UInt3] = json_property("value", UInt3)
    
    @property
    def value_type_name(self) -> str:
        return "uint3?"


@json_model("uint4", Member)
@dataclass(slots=True)
class Field_Uint4(Field):
    value : UInt4 = json_property("value", UInt4)
    
    @property
    def value_type_name(self) -> str:
        return "uint4"


@json_model("uint4?", Member)
@dataclass(slots=True)
class Field_Nullable_Uint4(Field):
    value : Optional[UInt4] = json_property("value", UInt4)
    
    @property
    def value_type_name(self) -> str:
        return "uint4?"


@json_model("int2", Member)
@dataclass(slots=True)
class Field_Int2(Field):
    value : Int2 = json_property("value", Int2)
    
    @property
    def value_type_name(self) -> str:
        return "int2"


@json_model("int2?", Member)
@dataclass(slots=True)
class Field_Nullable_Int2(Field):
    value : Optional[Int2] = json_property("value", Int2)
    
    @property
    def value_type_name(self) -> str:
        return "int2?"


@json_model("int3", Member)
@dataclass(slots=True)
class Field_Int3(Field):
    value : Int3 = json_property("value", Int3)
    
    @property
    def value_type_name(self) -> str:
        return "int3"


@json_model("int3?", Member)
@dataclass(slots=True)
class Field_Nullable_Int3(Field):
    value : Optional[Int3] = json_property("value", Int3)
    
    @property
    def value_type_name(self) -> str:
        return "int3?"


@json_model("int4", Member)
@dataclass(slots=True)
class Field_Int4(Field):
    value : Int4 = json_property("value", Int4)
    
    @property
    def value_type_name(self) -> str:
        return "int4"


@json_model("int4?", Member)
@dataclass(slots=True)
class Field_Nullable_Int4(Field):
    value : Optional[Int4] = json_property("value", Int4)
    
    @property
    def value_type_name(self) -> str:
        return "int4?"


@json_model("ulong2", Member)
@dataclass(slots=True)
class Field_Ulong2(Field):
    value : ULong2 = json_property("value", ULong2)
    
    @property
    def value_type_name(self) -> str:
        return "ulong2"


@json_model("ulong2?", Member)
@dataclass(slots=True)
class Field_Nullable_Ulong2(Field):
    value : Optional[ULong2] = json_property("value", ULong2)
    
    @property
    def value_type_name(self) -> str:
        return "ulong2?"


@json_model("ulong3", Member)
@dataclass(slots=True)
class Field_Ulong3(Field):
    value : ULong3 = json_property("value", ULong3)
    
    @property
    def value_type_name(self) -> str:
        return "ulong3"


@json_model("ulong3?", Member)
@dataclass(slots=True)
class Field_Nullable_Ulong3(Field):
    value : Optional[ULong3] = json_property("value", ULong3)
    
    @property
    def value_type_name(self) -> str:
        return "ulong3?"


@json_model("ulong4", Member)
@dataclass(slots=True)
class Field_Ulong4(Field):
    value : ULong4 = json_property("value", ULong4)
    
    @property
    def value_type_name(self) -> str:
        return "ulong4"


@json_model("ulong4?", Member)
@dataclass(slots=True)
class Field_Nullable_Ulong4(Field):
    value : Optional[ULong4] = json_property("value", ULong4)
    
    @property
    def value_type_name(self) -> str:
        return "ulong4?"


@json_model("long2", Member)
@dataclass(slots=True)
class Field_Long2(Field):
    value : Long2 = json_property("value", Long2)
    
    @property
    def value_type_name(self) -> str:
        return "long2"


@json_model("long2?", Member)
@dataclass(slots=True)
class Field_Nullable_Long2(Field):
    value : Optional[Long2] = json_property("value", Long2)
    
    @property
    def value_type_name(self) -> str:
        return "long2?"


@json_model("long3", Member)
@dataclass(slots=True)
class Field_Long3(Field):
    value : Long3 = json_property("value", Long3)
    
    @property
    def value_type_name(self) -> str:
        return "long3"


@json_model("long3?", Member)
@dataclass(slots=True)
class Field_Nullable_Long3(Field):
    value : Optional[Long3] = json_property("value", Long3)
    
    @property
    def value_type_name(self) -> str:
        return "long3?"


@json_model("long4", Member)
@dataclass(slots=True)
class Field_Long4(Field):
    value : Long4 = json_property("value", Long4)
    
    @property
    def value_type_name(self) -> str:
        return "long4"


@json_model("long4?", Member)
@dataclass(slots=True)
class Field_Nullable_Long4(Field):
    value : Optional[Long4] = json_property("value", Long4)
    
    @property
    def value_type_name(self) -> str:
        return "long4?"


@json_model("float2", Member)
@dataclass(slots=True)
class Field_Float2(Field):
    value : Float2 = json_property("value", Float2)
    
    @property
    def value_type_name(self) -> str:
        return "float2"


@json_model("float2?", Member)
@dataclass(slots=True)
class Field_Nullable_Float2(Field):
    value : Optional[Float2] = json_property("value", Float2)
    
    @property
    def value_type_name(self) -> str:
        return "float2?"


@json_model("float3", Member)
@dataclass(slots=True)
class Field_Float3(Field):
    value : Float3 = json_property("value", Float3)
    
    @property
    def value_type_name(self) -> str:
        return "float3"


@json_model("float3?", Member)
@dataclass(slots=True)
class Field_Nullable_Float3(Field):
    value : Optional[Float3] = json_property("value", Float3)
    
    @property
    def value_type_name(self) -> str:
        return "float3?"


@json_model("float4", Member)
@dataclass(slots=True)
class Field_Float4(Field):
    value : Float4 = json_property("value", Float4)
    
    @property
    def value_type_name(self) -> str:
        return "float4"


@json_model("float4?", Member)
@dataclass(slots=True)
class Field_Nullable_Float4(Field):
    value : Optional[Float4] = json_property("value", Float4)
    
    @property
    def value_type_name(self) -> str:
        return "float4?"


@json_model("double2", Member)
@dataclass(slots=True)
class Field_Double2(Field):
    value : Double2 = json_property("value", Double2)
    
    @property
    def value_type_name(self) -> str:
        return "double2"


@json_model("double2?", Member)
@dataclass(slots=True)
class Field_Nullable_Double2(Field):
    value : Optional[Double2] = json_property("value", Double2)
    
    @property
    def value_type_name(self) -> str:
        return "double2?"


@json_model("double3", Member)
@dataclass(slots=True)
class Field_Double3(Field):
    value : Double3 = json_property("value", Double3)
    
    @property
    def value_type_name(self) -> str:
        return "double3"


@json_model("double3?", Member)
@dataclass(slots=True)
class Field_Nullable_Double3(Field):
    value : Optional[Double3] = json_property("value", Double3)
    
    @property
    def value_type_name(self) -> str:
        return "double3?"


@json_model("double4", Member)
@dataclass(slots=True)
class Field_Double4(Field):
    value : Double4 = json_property("value", Double4)
    
    @property
    def value_type_name(self) -> str:
        return "double4"


@json_model("double4?", Member)
@dataclass(slots=True)
class Field_Nullable_Double4(Field):
    value : Optional[Double4] = json_property("value", Double4)
    
    @property
    def value_type_name(self) -> str:
        return "double4?"


@json_model("float2x2", Member)
@dataclass(slots=True)
class Field_Float2x2(Field):
    value : Float2x2 = json_property("value", Float2x2)
    
    @property
    def value_type_name(self) -> str:
        return "float2x2"


@json_model("float2x2?", Member)
@dataclass(slots=True)
class Field_Nullable_Float2x2(Field):
    value : Optional[Float2x2] = json_property("value", Float2x2)
    
    @property
    def value_type_name(self) -> str:
        return "float2x2?"


@json_model("float3x3", Member)
@dataclass(slots=True)
class Field_Float3x3(Field):
    value : Float3x3 = json_property("value", Float3x3)
    
    @property
    def value_type_name(self) -> str:
        return "float3x3"


@json_model("float3x3?", Member)
@dataclass(slots=True)
class Field_Nullable_Float3x3(Field):
    value : Optional[Float3x3] = json_property("value", Float3x3)
    
    @property
    def value_type_name(self) -> str:
        return "float3x3?"


@json_model("float4x4", Member)
@dataclass(slots=True)
class Field_Float4x4(Field):
    value : Float4x4 = json_property("value", Float4x4)
    
    @property
    def value_type_name(self) -> str:
        return "float4x4"


@json_model("float4x4?", Member)
@dataclass(slots=True)
class Field_Nullable_Float4x4(Field):
    value : Optional[Float4x4] = json_property("value", Float4x4)
    
    @property
    def value_type_name(self) -> str:
        return "float4x4?"


@json_model("double2x2", Member)
@dataclass(slots=True)
class Field_Double2x2(Field):
    value : Double2x2 = json_property("value", Double2x2)
    
    @property
    def value_type_name(self) -> str:
        return "double2x2"


@json_model("double2x2?", Member)
@dataclass(slots=True)
class Field_Nullable_Double2x2(Field):
    value : Optional[Double2x2] = json_property("value", Double2x2)
    
    @property
    def value_type_name(self) -> str:
        return "double2x2?"


@json_model("double3x3", Member)
@dataclass(slots=True)
class Field_Double3x3(Field):
    value : Double3x3 = json_property("value", Double3x3)
    
    @property
    def value_type_name(self) -> str:
        return "double3x3"


@json_model("double3x3?", Member)
@dataclass(slots=True)
class Field_Nullable_Double3x3(Field):
    value : Optional[Double3x3] = json_property("value", Double3x3)
    
    @property
    def value_type_name(self) -> str:
        return "double3x3?"


@json_model("double4x4", Member)
@dataclass(slots=True)
class Field_Double4x4(Field):
    value : Double4x4 = json_property("value", Double4x4)
    
    @property
    def value_type_name(self) -> str:
        return "double4x4"


@json_model("double4x4?", Member)
@dataclass(slots=True)
class Field_Nullable_Double4x4(Field):
    value : Optional[Double4x4] = json_property("value", Double4x4)
    
    @property
    def value_type_name(self) -> str:
        return "double4x4?"
