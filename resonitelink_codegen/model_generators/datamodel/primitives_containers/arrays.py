from resonitelink_codegen import CodeGenerator
from resonitelink.utils.types import type_mappings, primitive_types
from typing import Type, Generator


# NOTE: Reference output:
# from resonitelink.models.datamodel.primitives import *
# from resonitelink.models.datamodel import Member, SyncArray
# from resonitelink.json import JSONPropertyType, json_model, json_property
# from dataclasses import dataclass
# from decimal import Decimal
# from typing import List

# @json_model("bool[]", Member)
# @dataclass(slots=True)
# class Array_Bool(SyncArray):
#     values : List[bool] = json_property("values", bool, JSONPropertyType.LIST)
    
#     @property
#     def element_type(self) -> str:
#         return "bool"


class ArraysGenerator(CodeGenerator):
    """
    Generator for the arrays.py model file.
    
    """
    def __init__(self):
        super().__init__("./resonitelink/models/datamodel/primitives_containers/arrays.py")
    
    def generate(self) -> Generator[str, None, None]:
        """
        Generates the content of arrays.py

        """
        yield f"from resonitelink.models.datamodel.primitives import *\n"
        yield f"from resonitelink.models.datamodel import Member, SyncArray\n"
        yield f"from resonitelink.json import JSONPropertyType, json_model, json_property\n"
        yield f"from dataclasses import dataclass\n"
        yield f"from decimal import Decimal\n"
        yield f"from typing import List\n"
        yield f"\n\n"

        def _generate_array_class(model_name : str, class_name : str, value_type : Type, value_type_name : str):
            yield f"@json_model(\"{model_name}\", Member)\n"
            yield f"@dataclass(slots=True)\n"
            yield f"class {class_name}(SyncArray):\n"
            yield f"    values : List[{value_type.__name__}] = json_property(\"values\", {value_type.__name__}, JSONPropertyType.LIST)\n"
            yield f"    \n"
            yield f"    @property\n"
            yield f"    def element_type(self) -> str:\n"
            yield f"        return \"{value_type_name}\"\n"

        for primitive_type in primitive_types:
            type_info = type_mappings[primitive_type]

            yield from _generate_array_class(f"{primitive_type}[]", f"Array_{type_info.type_name}", type_info.type, primitive_type)
            if primitive_types.index(primitive_type) < len(primitive_types) - 1:
                yield f"\n\n"
