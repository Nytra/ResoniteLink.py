from resonitelink.models.assets.mesh import TriangleSubmeshRawData 
from resonitelink.models.datamodel import Float3, Color, Reference, SyncList, Field_Enum, Field_Float, Field_Uri
from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient
from typing import Tuple, List, Generator, Any
from math import sin, cos, sqrt
import asyncio
import logging


import time

def timeit(f):

    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        
        return result

    return timed


# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient(log_level=logging.INFO)



@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    ts = time.time()

    parent = await client.add_slot("Root", name="Lib Perf Test")

    for i in range(1000):
        child = await client.add_slot(parent, name=f"Child {i}")
        component = await child.add_component("[FrooxEngine]FrooxEngine.ValueField<bool>")
        await client.get_component(component)

    te = time.time()

    logging.warning(f"Operation took {(te - ts)}s")

    # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
    await client.stop()

# Asks for the current port ResoniteLink is running on.
# port = int(input("ResoniteLink Port: "))
port = 11960


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
