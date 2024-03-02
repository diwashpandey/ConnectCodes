from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer

class ChatConsumers(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connection initalized...")
        await self.send({
            "type":"websocket.accept"
        })
    
    async def websocket_receive(self, event):
        print("Messege received from client")
    
    async def websocket_disconnect(self, event):
        print("Disconnected from the client", event)
        raise StopConsumer()