from resonitelink.models.datamodel.assets.mesh import Vertex, Submesh, Bone, Blendshape
from resonitelink.models.messages import Message
from resonitelink.json import JSONPropertyType, json_model, json_property
from dataclasses import dataclass
from typing import List


@json_model("importMeshJSON", Message)
@dataclass(slots=True)
class ImportMeshJSON(Message):
    """
    Imports a mesh asset from purely JSON definition.
    This is pretty verbose, so it's recommended only for smaller meshes, but is supported for
    convenience and ease of implementation & experimentation, at the cost of efficiency.
    If possible, it's recommended to use ImportMeshRawData for better efficiency.

    """
    #  Vertices of this mesh. These are shared across sub-meshes.
    vertices : List[Vertex] = json_property("vertices", Vertex, JSONPropertyType.LIST)
    
    # List of submeshes (points, triangles...) representing this mesh.
    # Meshes will typically have at least one submesh.
    # Each submesh uses indicies of the vertices for its primitives.
    submeshes : List[Submesh] = json_property("submeshes", Submesh, JSONPropertyType.LIST)

    # Bones of the mesh when data represents a skinned mesh.
    # These will be referred to by their index from vertex data.
    bones : List[Bone] = json_property("bones", Bone, JSONPropertyType.LIST)

    # Blendshapes of this mesh.
    # These allow modifying the vertex positions, normals & tangents for animations such as facial expressions.
    blendshapes : List[Blendshape] = json_property("blendshapes", Blendshape, JSONPropertyType.LIST)
