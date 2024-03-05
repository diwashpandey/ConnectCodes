from django.urls import path
from rooms.consumers import ChatConsumers
from accounts.consumers import CommitConsumer

ws_patterns = [
    path("ws/chat/<str:room_id>/", ChatConsumers.as_asgi()),
    path("ws/account/commit/", CommitConsumer.as_asgi())
]