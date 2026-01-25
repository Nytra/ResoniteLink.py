from resonitelink_codegen import CodeGenerator
from resonitelink.utils.types import type_mappings, quaternion_types
from typing import Type, Generator


# NOTE: Reference output:
# from resonitelink.json import json_model, json_property
# from dataclasses import dataclass

# @json_model("floatQ")
# @dataclass(slots=True)
# class Quaternion_Float():
#     x : float = json_property("x", float)
#     y : float = json_property("y", float)
#     z : float = json_property("z", float)
#     w : float = json_property("w", float)


class QuaternionsGenerator(CodeGenerator):
    """
    Generator for the quaternions.py model file.
    
    """
    def __init__(self):
        super().__init__("./resonitelink/models/datamodel/primitives/quaternions.py")
    
    def generate(self) -> Generator[str, None, None]:
        """
        Generates the content of quaternions.py

        """
        yield f"from resonitelink.json import json_model, json_element\n"
        yield f"\n\n"

        def _generate_quaternion_class(model_name : str, class_name : str, element_type : Type):
            yield f"@json_model(internal_type_name=\"t_{model_name}\")\n"
            yield f"class {class_name}():\n"
            yield f"    x : {element_type.__name__} = json_element(\"x\", {element_type.__name__})\n"
            yield f"    y : {element_type.__name__} = json_element(\"y\", {element_type.__name__})\n"
            yield f"    z : {element_type.__name__} = json_element(\"z\", {element_type.__name__})\n"
            yield f"    w : {element_type.__name__} = json_element(\"w\", {element_type.__name__})\n"

        for quaternion_type in quaternion_types:
            type_info = type_mappings[quaternion_type]

            yield from _generate_quaternion_class(f"{quaternion_type}Q", f"{type_info.type_name}Q", type_info.type)
            if quaternion_types.index(quaternion_type) < len(quaternion_types) - 1:
                yield f"\n\n"
