from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient, Float3, Field_String
import asyncio


# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient()


@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
    slot = await client.add_slot(name="Hello World Slot", position=Float3(0, 1.5, 0))
    
    # Adds a TextRenderer component to the newly created slot.
    await slot.add_component("[FrooxEngine]FrooxEngine.TextRenderer",
        # Sets the initial value of the string field 'Text' on the component.
        Text=Field_String(value="Hello, world!")
    )
    
    # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
    await client.stop()


# Asks for the current port ResoniteLink is running on.
port = int(input("ResoniteLink Port: "))


# Start the client on the specified port.
asyncio.run(client.start(port))
