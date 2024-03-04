from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer

class ChatConsumers(AsyncConsumer):

    room_id:str = None

    async def websocket_connect(self, event):
        print("Connection initalized...")

        print(self.scope)
        self.room_id = self.scope["url_route"]["kwargs"]['room_id']
        await self.channel_layer.group_add(self.room_id, self.channel_name)
        await self.send({
            "type":"websocket.accept"
        })
    
    async def websocket_receive(self, event):
        print("Messege received from client")

        await self.channel_layer.group_send(self.room_id,{
            "type":"message.send",
            "text":event["text"]
        })

    async def websocket_disconnect(self, event):
        print("Disconnected from the client", event)
        await self.channel_layer.group_discard(self.room_id, self.channel_layer)
        raise StopConsumer()
    
    async def message_send(self, event):
        await self.send({
            "type":"websocket.send",
            "text":event["text"]
        })