from django.urls import path
from . import consumers

ws_patterns = [
    path("ws/chat/<str:room_id>/", consumers.ChatConsumers.as_asgi())
]