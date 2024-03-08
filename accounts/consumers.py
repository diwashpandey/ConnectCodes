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

            try:
                # Get the full object of a authenticated user 
                requested_user = await database_sync_to_async(UserAccount.objects.get)(username = self.scope["user"].username)

                # Get the full object of a user-to-commit
                user_to_commit = await database_sync_to_async(UserAccount.objects.get)(username=username)
                
                if commit == "Unfollow":
                    # Remove the requested_user's foreignkey from the user_to_commit 
                    await database_sync_to_async(requested_user.following.remove)(user_to_commit)
                    text_data = json.dumps(
                        {
                            "new_commit":"Follow",
                            "username":user_to_commit.username
                        }
                    )
                    await self.send(text_data=text_data)
                    
                elif commit == "Follow":
                    # Add the requested_user's foreignkey to the user_to_commit 
                    await database_sync_to_async(requested_user.following.add)(user_to_commit)
                    text_data = json.dumps(
                        {
                            "new_commit":"Unfollow",
                            "username":user_to_commit.username
                        }
                    )
                    await self.send(text_data=text_data)
            except Exception as E:
                text_data = "Something error happened"

            self.send(text_data=text_data)

    async def disconnect(self, code):
        raise StopConsumer()
    
    
    
        