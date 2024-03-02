from django.urls import path
from . import consumers

ws_patterns = [
    path("ws/chat/", consumers.ChatConsumers.as_asgi())
]