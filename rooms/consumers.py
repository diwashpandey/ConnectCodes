from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from .models import Room, Message
from channels.db import database_sync_to_async
import json


class ChatConsumers(AsyncConsumer):

    async def websocket_connect(self, event):
        self.user = self.scope["user"]
        self.room_id = self.scope["url_route"]["kwargs"]['room_id']
        self.room = await database_sync_to_async(Room.objects.get)(id = self.room_id)
        # room_members = await database_sync_to_async(room.members.all)()

        await self.channel_layer.group_add(self.room_id, self.channel_name)
        await self.send({
            "type":"websocket.accept"
        })
    
    async def websocket_receive(self, event):
        print("Messege received from client")

        data = json.dumps({
            "username":self.user.username,
            "profile_pic":self.user.profile_pic.name,
            "message":event["text"]
        })

        # await database_sync_to_async(Message.objects.create)(
        #     room = self.room,
        #     user=self.user,
        #     message=event["text"]
        #     )
        
        await self.channel_layer.group_send(self.room_id,{
            "type":"message.send",
            "text": data
        })

    async def websocket_disconnect(self, event):
        print("Disconnected from the client", event)
        await self.channel_layer.group_discard(self.room_id, self.channel_name)
        raise StopConsumer()
    
    async def message_send(self, event):
        await self.send({
            "type":"websocket.send",
            "text":event["text"]
        })