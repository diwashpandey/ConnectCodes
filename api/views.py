from django.shortcuts import render
from rest_framework.decorators import api_view
from rooms.models import *
from .serializers import RoomSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def get_room_details(request, pk):
    try:
        room = Room.objects.get(id = pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    except Exception as e:
        return Response({
            "status": 404,
            "message": "Room doesn't exist"
        })
    