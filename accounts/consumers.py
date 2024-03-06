from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from channels.db import database_sync_to_async
import json
from .models import UserAccount


class CommitConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        if self.scope["user"].is_authenticated:
            data = json.loads(text_data)
            username = data["username"]
            commit = data["commit"]

            await self.send(text_data=text_data)

    async def disconnect(self):
        raise StopConsumer()
    
    
    
        