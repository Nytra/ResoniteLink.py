from resonitelink.models.datamodel import Component
from resonitelink.proxies import Proxy

class ComponentProxy(Proxy[Component]):
    
    async def fetch_data(self) -> Component:
        return await self.client.get_component(self.id)