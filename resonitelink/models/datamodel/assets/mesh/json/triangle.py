from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model()
@dataclass(slots=True)
class Triangle():
    """
    Represents a single triangle of a mesh.
    
    """
    # Index of the first vertex that forms this triangle.
    vertex_0_index : int = json_property("vertex0Index", int)

    # Index of the second vertex that forms this triangle.
    vertex_1_index : int = json_property("vertex1Index", int)

    # Index of the third vertex that forms this triangle.
    vertex_2_index : int = json_property("vertex2Index", int)
