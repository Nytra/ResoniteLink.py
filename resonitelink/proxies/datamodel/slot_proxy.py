from typing import Any
from resonitelink.models.datamodel import Slot, Field_String
from resonitelink.models.messages import UpdateSlot
from resonitelink.proxies import Proxy

class SlotProxy(Proxy[Slot]):
    
    async def fetch_data(self) -> Slot:
        return await self.client.fetch_slot(self.id)
    
    async def set_name(self, new_name : str):
        msg = UpdateSlot(data=Slot(id=self.id, name=Field_String(value=new_name)))
        await self.client.send_message(msg)
        self.invalidate_data()
