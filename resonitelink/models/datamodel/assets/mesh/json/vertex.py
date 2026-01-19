from resonitelink.models.datamodel import Float3, Color
from resonitelink.json import JSONPropertyType, json_model, json_property
from dataclasses import dataclass
from typing import List

from .uv_coordinate import UV_Coordinate
from .bone_weight import BoneWeight


@json_model("vertex")
@dataclass(slots=True)
class Vertex():
    """
    Defines a single vertex of a mesh. Position is mandatory field, but all other properties are optional.
    
    """
    # Position of the vertex.
    position : Float3 = json_property("position", Float3)
    
    # Normal vector of the vertex.
    normal : Float3 = json_property("normal", Float3)

    # Tangent vector of the vertex. The 4th component indicates direction of the binormal.
    # When specifying tangent, it's strongly recommended that normals are specified too.
    tangent : Float3 = json_property("tangent", Float3)
    
    # Color of the vertex.
    color : Color = json_property("color", Color)
    
    # UV channel coordinates.
    # Each UV channel can have 2-4 dimensions.
    # Each vertex can have multiple UV channels.
    # The number of channels and dimensions for each MUST be same across all vertices.
    uvs : List[UV_Coordinate] = json_property("uvs", UV_Coordinate, JSONPropertyType.LIST)

    # Weights that define how much this vertex is affected by specific bones for skinned meshes.
    # The weights should add up to 1 across all the weights.
    bone_weights : List[BoneWeight] = json_property("boneWeights", BoneWeight, JSONPropertyType.LIST)
