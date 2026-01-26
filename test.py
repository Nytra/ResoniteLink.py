from resonitelink.utils.slot_hierarchy import SlotHierarchy
from resonitelink.models.datamodel import Member, SyncObject, SyncList
from resonitelink.json import json_model, json_element
from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient, ImportAudioClipRawData, Float3, Member, Array_Float, Array_Float3, Field_Float
from dataclasses import dataclass
from typing import List
import asyncio
import logging
from array import array

# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient(log_level=logging.DEBUG)


# @json_model("[FrooxEngine]FrooxEngine.MultiLineMesh+Line", Member)
# @dataclass(slots=True)
# class MultiLineMesh_Line(Member):
#     pass

from math import pi, sin

@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
    slot = await client.add_slot(name="Test Line Mesh Slot", position=Float3(0, 1.5, 0))

    positions : List[Float3] = []
    scales : List[float] = []

    resolution = 100
    for i in range(resolution):
        x = i / resolution
        y = sin(2 * pi * x)

        positions += [ Float3(x, 0, y) ]
        scales += [ 0.01 ]
    
    print(len(positions))

    multi_line_mesh = await client.add_component(
        slot, 
        component_type="[FrooxEngine]FrooxEngine.MultiLineMesh",
        Lines=SyncList(
            SyncObject(
                Scale=Field_Float(value=0.2),
                Positions=Array_Float3(values=positions),
                Scales=Array_Float(values=scales)
            )
        )
    )
    
    line_update_data = SyncObject(
        Scale=Field_Float(value=0.2),
        Positions=Array_Float3(values=positions),
        Scales=Array_Float(values=scales)
    )

    await client.update_component(multi_line_mesh, Lines=SyncList(line_update_data))

    # root_slot = await client.get_slot("Root", -1, False)
    # root_hierarchy = SlotHierarchy.from_slot(root_slot)
    # target_hierarchy = next(root_hierarchy.find(lambda h: h.slot.name.value == 'MultiLineMeshTest'))

    # await client.get_slot(target_hierarchy.slot, -1, True)


# Asks for the current port ResoniteLink is running on.
# port = int(input("ResoniteLink Port: "))
port = 8627

# Start the client on the specified port.
asyncio.run(client.start(port))








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




