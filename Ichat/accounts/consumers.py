from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import FriendMessage
import json

class CoreConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['friend_name']
        self.room_group_name = f'friend_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        print(self.room_name)
        await self.accept()




        print("accepted")
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = self.scope['user'].username
        user_id = self.scope['user'].id

        await self.save_message(message)
        print(message)

        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                "type": "group_message", 
                "message": message,
                "username": username,
                "user_id": user_id,
                "updated_at": str(await self.get_current_timestamp())
            }
        )

    async def group_message(self, event):
        message = event["message"]
        username = event["username"]
        user_id = event["user_id"]
        updated_at = event["updated_at"]

        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
            "user_id": user_id,
            "updated_at": updated_at,
            }))

    @database_sync_to_async
    def save_message(self, message): 
        friend = User.objects.get(username=self.room_name)
        user = User.objects.get(id=self.scope['user'].id)
        FriendMessage.objects.create(
            sender=user,
            reciever=friend,
            body=message,
        )
    
    @database_sync_to_async
    def get_current_timestamp(self):
        from django.utils import timezone
        return timezone.now()
