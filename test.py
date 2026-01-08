from resonitelink import ResoniteLinkClient, ResoniteLinkClientEvent
import asyncio
import logging

logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)

port = int(input("ResoniteLink Port: "))

async def on_client_started(client : ResoniteLinkClient):
    logger.info("Start event invoked!")
    await client._send_message('{"$type" : "getSlot", "slotId" : "Root", "includeComponentData" : false, "depth" : 0}')

client = ResoniteLinkClient(log_level=logging.DEBUG)
client.register_event_handler(ResoniteLinkClientEvent.STARTED, on_client_started) # TODO: Decorator syntax

asyncio.run(client.start(port))