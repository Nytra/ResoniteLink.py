from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient, Float3, Field_String, UpdateComponent, ImportMeshJSON, Vertex, TriangleSubmeshFlat, AssetData, Field_Uri, Field_Float, Reference, SyncList, Triangle, TriangleSubmesh, \
    ImportMeshRawData, TriangleSubmeshRawData, Color
# from resonitelink.models.messages.assets.meshes import *
# from resonitelink.models.datamodel.assets.mesh import * 
from typing import Tuple, List, Generator, Any
from math import sin, cos, sqrt
import asyncio
import logging


# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient(log_level=logging.DEBUG)


def sub_vector3(a : Float3, b : Float3):
    return Float3(
        a.x - b.x, 
        a.y - b.y, 
        a.z - b.z
    )

def mul_vector3(a : Float3, b : Float3):
    return Float3(
        a.x * b.x,
        a.y * b.y,
        a.z * b.z
    )

def cross_vector3(a : Float3, b : Float3):
    return Float3(
        a.y * b.z - a.z * b.y,
        a.z * b.x - a.x * b.z,
        a.x * b.y - a.y * b.x
    )

def magnitude_vector3(vector : Float3):
    return sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 3)

def normalize_vector3(vector : Float3):
    l = magnitude_vector3(vector)
    return Float3(
        vector.x / l,
        vector.y / l, 
        vector.z / l
    )

def avg_vector3(*vectors : Float3):
    return Float3(
        sum( [v.x for v in vectors] ) / float(len(vectors)),
        sum( [v.y for v in vectors] ) / float(len(vectors)),
        sum( [v.z for v in vectors] ) / float(len(vectors))
    )


@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    def generate_wave_grid_points(grid_size : Tuple[int, int], wave_scale : Tuple[float, float] = (1.0, 1.0), wave_offset : Tuple[float, float] = (0.0, 0.0)) -> List[Float3]:
        def _generate() -> Generator[Float3, Any, Any]:
            for x in range(grid_size[0]):
                for z in range(grid_size[1]):
                    y = sin(x * wave_scale[0] + wave_offset[0]) * cos(z * wave_scale[1] + wave_offset[1])
                    yield Float3(x, y, z)
        
        return list(_generate())

    def generate_grid_colors(grid_size : Tuple[int, int]) -> List[Color]:
        def _generate() -> Generator[Color, Any, Any]:
            for x in  range(grid_size[0]):
                for y in range(grid_size[1]):
                    r = x / (grid_size[0] - 1)
                    g = y / (grid_size[1] - 1)
                    b = 0.0
                    a = 1.0
                    yield Color(r, g, b, a)
        
        return list(_generate())

    def triangulate_grid(grid_size : Tuple[int, int], points : List[Float3]) -> List[int]:
        if len(points) != grid_size[0] * grid_size[1]:
            raise ValueError("Invalid point count for grid size!")
        
        def _generate() -> Generator[int, Any, Any]:
            for x in range(grid_size[0] - 1):
                for y in range(grid_size[1] - 1):
                    # for each quad
                    idx_0 = (x)     + (y)     * grid_size[0]
                    idx_1 = (x + 1) + (y)     * grid_size[0]
                    idx_2 = (x)     + (y + 1) * grid_size[0]
                    idx_3 = (x + 1) + (y + 1) * grid_size[0]

                    yield idx_0
                    yield idx_1
                    yield idx_2

                    yield idx_2
                    yield idx_1
                    yield idx_3

        return list(_generate())
    
    def compute_normals(points : List[Float3], triangle_indices : List[int]) -> List[Float3]:
        if len(triangle_indices) % 3 != 0:
            raise ValueError("Length of triangles list must be a multiple of 3!")
        
        # Lists of normals of connected faces for each point
        connecting_face_normals : List[List[Float3]] = [ list() for point in points ]

        for i in range(0, len(triangle_indices), 3):
            idx0 = triangle_indices[i]
            idx1 = triangle_indices[i + 1]
            idx2 = triangle_indices[i + 2]
            
            p0 = points[idx0]
            p1 = points[idx1]
            p2 = points[idx2]

            a = sub_vector3(p1, p0)
            b = sub_vector3(p2, p0)

            n = cross_vector3(a, b)

            connecting_face_normals[idx0].append(n)
            connecting_face_normals[idx1].append(n)
            connecting_face_normals[idx2].append(n)
        
        return [ normalize_vector3(avg_vector3(*normals)) for normals in connecting_face_normals ]

    # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
    slot = await client.add_slot(name="Mesh Slot", position=Float3(0, 1.5, 0))
    
    grid_size = (64, 64)
    wave_scale = (0.33, 0.33)
    wave_offset = (0.0, 0.0)
    points = generate_wave_grid_points(grid_size, wave_scale, wave_offset)
    colors = generate_grid_colors(grid_size)
    triangle_indices = triangulate_grid(grid_size, points)
    normals = compute_normals(points, triangle_indices)
    triangle_count = int(len(triangle_indices) / 3)

    msg = ImportMeshRawData(
        init_positions=points,
        init_normals=normals,
        init_colors=colors,
        submeshes=[ TriangleSubmeshRawData(triangle_count, triangle_indices) ]
    )
    response : AssetData = await client.send_message(msg) # type: ignore

    static_mesh = await client.add_component(slot, "[FrooxEngine]FrooxEngine.StaticMesh", URL=Field_Uri(response.asset_url))
    material = await client.add_component(slot, "[FrooxEngine]FrooxEngine.PBS_VertexColorMetallic", Smoothness=Field_Float(0.0))

    mesh_renderer = await client.add_component(
        slot, 
        "[FrooxEngine]FrooxEngine.MeshRenderer", 
        Mesh=Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Mesh>", target_id=static_mesh.id),
        Materials=SyncList(Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>", target_id=material.id))
    )
    await mesh_renderer.update_members(Materials=SyncList(Reference(target_type="[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>", target_id=material.id)))

    await client.add_component(slot, "[FrooxEngine]FrooxEngine.MeshCollider")
    await client.add_component(slot, "[FrooxEngine]FrooxEngine.Grabbable")

    # while True:
    #     await asyncio.sleep(0.1)
    #     wave_offset = (wave_offset[0] + 0.1, wave_offset[1] - 0.1)

    #     points = generate_wave_grid_points(grid_size, wave_scale, wave_offset)
    #     colors = generate_grid_colors(grid_size)
    #     triangle_indices = triangulate_grid(grid_size, points)
    #     normals = compute_normals(points, triangle_indices)

    #     msg = ImportMeshRawData(
    #         init_positions=points,
    #         init_normals=normals,
    #         init_colors=colors,
    #         submeshes=[ TriangleSubmeshRawData(triangle_count, triangle_indices) ]
    #     )
    #     response : AssetData = await client.send_message(msg) # type: ignore

    #     await client.update_component(
    #         static_mesh, 
    #         URL=Field_Uri(response.asset_url)
    #     )


# Asks for the current port ResoniteLink is running on.
# port = int(input("ResoniteLink Port: "))
port = 5258


# Start the client on the specified port.
asyncio.run(client.start(port))








# from resonitelink.utils.slot_hierarchy import SlotHierarchy
# from resonitelink.models.datamodel import Member, SyncObject, SyncList
# from resonitelink.json import json_model, json_element, format_object_structure
# from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient, ImportAudioClipRawData, Float3, Member, Array_Float, Array_Float3, Field_Float
# from dataclasses import dataclass
# from typing import List
# from math import pi, sin
# import asyncio
# import logging
# from array import array


# # Creates a new client that connects to ResoniteLink via websocket.
# client = ResoniteLinkWebsocketClient(log_level=logging.DEBUG)


# @client.on_started
# async def on_client_started(client : ResoniteLinkClient):
#     """
#     This async function is called by the client at the end of its startup sequence.
#     You can use it to execute code once the client is up and running!

#     """
#     # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
#     # slot = await client.add_slot(name="Test Ref Slot", position=Float3(0, 1.5, 0))

#     # ref_slot_id = 'RLPY_47AB_01_0'
#     # ref_slot = await client.get_slot(ref_slot_id, -1, True)
#     # format_object_structure(ref_slot)

#     slot = await client.add_slot(name="", position=Float3(0, 1.5, 0))

#     positions : List[Float3] = []
#     scales : List[float] = []

#     resolution = 100
#     for i in range(resolution):
#         x = i / resolution
#         y = sin(2 * pi * x)

#         positions += [ Float3(x, 0, y) ]
#         scales += [ 0.01 ]

#     multi_line_mesh = await client.add_component(
#         slot, 
#         component_type="[FrooxEngine]FrooxEngine.MultiLineMesh",
#         Lines=SyncList(
#             SyncObject(
#                 Scale=Field_Float(value=0.2),
#                 Positions=Array_Float3(values=positions),
#                 Scales=Array_Float(values=scales)
#             )
#         )
#     )
    
#     line_update_data = SyncObject(
#         Scale=Field_Float(value=0.2),
#         Positions=Array_Float3(values=positions),
#         Scales=Array_Float(values=scales)
#     )

#     await client.update_component(multi_line_mesh, Lines=SyncList(line_update_data))

#     root_slot = await client.get_slot("Root", -1, False)
#     root_hierarchy = SlotHierarchy.from_slot(root_slot)
#     target_hierarchy = next(root_hierarchy.find(lambda h: h.slot.name.value == 'MultiLineMeshTest'))

#     await client.get_slot(target_hierarchy.slot, -1, True)


# # Asks for the current port ResoniteLink is running on.
# # port = int(input("ResoniteLink Port: "))
# port = 41634


# # Start the client on the specified port.
# asyncio.run(client.start(port))








# from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient
# from resonitelink.json import ResoniteLinkJSONEncoder, ResoniteLinkJSONDecoder, format_object_structure
# from resonitelink.models.datamodel import Slot, Component, Reference, Field, Field_String
# from resonitelink.models.messages import RemoveSlot, GetSlot, AddSlot, AddComponent, ImportTexture2DRawData, RequestSessionData
# from typing import List
# import asyncio
# import logging


# port = 49155

# logger = logging.getLogger("App")
# logger.setLevel(logging.DEBUG)


# def test_generate_image_bytes() -> bytes:
#     data : List[int] = []

#     for x in range(16):
#         for y in range(16):
#             data.append(x * 16)
#             data.append(y * 16)
#             data.append(255)
#             data.append(255)
    
#     return bytes(data)




# from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient, Float3, Field_String, UpdateComponent
# import asyncio
# import logging

# # Creates a new client that connects to ResoniteLink via websocket.
# client = ResoniteLinkWebsocketClient()

# @client.on_started
# async def on_client_started(client : ResoniteLinkClient):
#     """
#     This async function is called by the client at the end of its startup sequence.
#     You can use it to execute code once the client is up and running!

#     """
#     # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
#     slot = await client.add_slot(name="Hello World Slot", position=Float3(0, 1.5, 0))
    
#     # Adds a TextRenderer component to the newly created slot.
#     text_renderer = await client.add_component(slot, "[FrooxEngine]FrooxEngine.TextRenderer", {
#         # Sets the initial value of the string field 'Text' on the component.
#         'Text': Field_String(value="Hello, world! ")
#     })

#     while True:
#         await asyncio.sleep(0.1)
        
#         # First get the current component state
#         text_renderer_data = await client.get_component(text_renderer)
#         text_field : Field_String = text_renderer_data.members["Text"] # type: ignore
#         text_field.value = text_field.value[1:] + text_field.value[0]

#         logging.info(f"Updating text: {text_field.value}")

#         # Then update the component state
#         await client.update_component(text_renderer, {
#             'Text': text_field
#         })

# # Asks for the current port ResoniteLink is running on.
# # port = int(input("ResoniteLink Port: "))
# port = 48395

# # Start the client on the specified port.
# asyncio.run(client.start(port))




