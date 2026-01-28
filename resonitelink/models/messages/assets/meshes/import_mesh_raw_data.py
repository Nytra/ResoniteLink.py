from resonitelink.json import MISSING, json_model, json_element, json_list
from dataclasses import InitVar, field
from typing import Optional, List
from array import array

from ....datamodel.assets.mesh import Bone, SubmeshRawData, BlendshapeRawData
from ....datamodel.primitives import Float3, Float4, Color
from ...messages import Message, BinaryPayloadMessage
from resonitelink.utils.vector_tools import pack_vectors_float3, unpack_vectors_float3, pack_vectors_color, unpack_vectors_color


import logging

@json_model("importMeshRawData", Message)
class ImportMeshRawData(BinaryPayloadMessage):
    _positions : Optional[bytes] = field(default=None, init=False) # float3
    _normals : Optional[bytes] = field(default=None, init=False) # float3
    _tangents : Optional[bytes] = field(default=None, init=False) # float4
    _colors : Optional[bytes] = field(default=None, init=False) # color (float4: rgba)
    _bone_weights : Optional[bytes] = field(default=None, init=False) # struct{ int, float } (bone_index, weight)
    _uvs : Optional[List[bytes]] = field(default=None, init=False) # float

    # Number of vertices in this mesh.
    vertex_count : int = json_element("vertexCount", int, default=MISSING)

    # Initializes the positions.
    init_positions : InitVar[Optional[List[Float3]]] = None
    
    # Do vertices have normals?
    has_normals : bool = json_element("hasNormals", bool, default=MISSING)

    # Initializes the normals.
    init_normals : InitVar[Optional[List[Float3]]] = None
    
    # Do vertices have tangents?
    has_tangents : bool = json_element("hasTangents", bool, default=MISSING)

    # Initializes the tangents.
    init_tangents : InitVar[Optional[List[Float4]]] = None
    
    # Do vertices have colors?
    has_colors : bool = json_element("hasColors", bool, default=MISSING)
    
    # Initializes the colors.
    init_colors : InitVar[Optional[List[Color]]] = None

    # How many bone weights does each vertex have.
    # If some vertices have fewer bone weights, use weight of 0 for remainder bindings.
    bone_weight_count : int = json_element("boneWeightCount", int, default=MISSING)
    
    # Configuration of UV channels for this mesh.
    # Each entry represents one UV channel of the mesh.
    # Number indicates number of UV dimensions. This must be between 2 and 4 (inclusive).
    uv_channel_dimensions : List[int] = json_list("uvChannelDimensions", int, default=MISSING)

    # Submeshes that form this mesh. Meshes will typically have at least one submesh.
    submeshes : List[SubmeshRawData] = json_list("submeshes", SubmeshRawData, default=MISSING)

    # Blendshapes of this mesh.
    # These allow modifying the vertex positions, normals & tangents for animations such as facial expressions.
    blendshapes : List[BlendshapeRawData] = json_list("blendshapes", BlendshapeRawData, default=MISSING)

    # Bones of the mesh when data represents a skinned mesh.
    # These will be referred to by their index from vertex data.
    bones : List[Bone] = json_list("bones", Bone, default=MISSING)

    def __post_init__(
        self, 
        init_positions : Optional[List[Float3]],
        init_normals : Optional[List[Float3]],
        init_tangents : Optional[List[Float4]],
        init_colors : Optional[List[Color]],
    ):
        if init_positions:
            self.vertex_count = len(init_positions)
            self.positions = init_positions
        if init_normals:
            self.has_normals = True
            # TODO: self.normsl = init_normals
        if init_tangents:
            self.has_tangents = True
            # TODO: self.tangents = init_tangents
        if init_colors:
            self.has_colors = True
            self.colors = init_colors
    
    @property
    def positions(self) -> List[Float3]:
        if not self._positions:
            raise ValueError("Positions were never provided!")
        
        arr = array("f")
        arr.frombytes(self._positions)
        return list(pack_vectors_float3(iter(arr)))
    
    @positions.setter
    def positions(self, vectors : List[Float3]):
        if len(vectors) != self.vertex_count:
            raise ValueError(f"Expected {self.vertex_count} vertex positions, but only got {len(vectors)} indices.")
        
        self._positions = array("f", unpack_vectors_float3(iter(vectors))).tobytes()

    @property
    def colors(self) -> List[Color]:
        if not self._colors:
            raise ValueError("Colors were never provided!")
        
        arr = array("f")
        arr.frombytes(self._colors)
        return list(pack_vectors_color(iter(arr)))
    
    @colors.setter
    def colors(self, colors : List[Color]):
        if len(colors) != self.vertex_count:
            raise ValueError(f"Expected {self.vertex_count} vertex colors, but only got {len(colors)} colors.")
        
        self._colors = array("f", unpack_vectors_color(iter(colors))).tobytes()

    @property
    def raw_binary_payload(self) -> bytes:
        data = bytearray()

        if self._positions:
            data.extend(self._positions)
        if self._colors:
            data.extend(self._colors)
        
        for submesh in self.submeshes:
            data.extend(submesh.raw_binary_payload)
        
        return data

    @raw_binary_payload.setter
    def raw_binary_payload(self, data : bytes):
        raise NotImplementedError()
