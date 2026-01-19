from resonitelink.models.datamodel.assets.mesh import Bone, SubmeshRawData, BlendshapeRawData
from resonitelink.models.messages import Message, BinaryPayloadMessage
from resonitelink.json import JSONPropertyType, json_model, json_property
from dataclasses import dataclass
from typing import List


@json_model("importMeshRawData", Message)
@dataclass(slots=True)
class ImportMeshRawData(BinaryPayloadMessage):
    # Number of vertices in this mesh.
    vertex_count : int = json_property("vertexCount", int)
    
    # Do vertices have normals?
    has_normals : bool = json_property("hasNormals", int)
    
    # Do vertices have tangents?
    has_tangents : bool = json_property("hasTangents", bool)
    
    # Do vertices have colors?
    has_colors : bool = json_property("hasColors", bool)
    
    # How many bone weights does each vertex have.
    # If some vertices have fewer bone weights, use weight of 0 for remainder bindings.
    bone_weight_count : int = json_property("boneWeightCount", int)
    
    # Configuration of UV channels for this mesh.
    # Each entry represents one UV channel of the mesh.
    # Number indicates number of UV dimensions. This must be between 2 and 4 (inclusive).
    uv_channel_dimensions : List[int] = json_property("uvChannelDimensions", int, JSONPropertyType.LIST)

    # Submeshes that form this mesh. Meshes will typically have at least one submesh.
    submeshes : List[SubmeshRawData] = json_property("submeshes", SubmeshRawData, JSONPropertyType.LIST)

    # Blendshapes of this mesh.
    # These allow modifying the vertex positions, normals & tangents for animations such as facial expressions.
    blendshapes : List[BlendshapeRawData] = json_property("blendshapes", BlendshapeRawData, JSONPropertyType.LIST)

    # Bones of the mesh when data represents a skinned mesh.
    # These will be referred to by their index from vertex data.
    bones : List[Bone] = json_property("bones", Bone, JSONPropertyType.LIST)
