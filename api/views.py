from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rooms.models import *
from .serializers import RoomSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_room_details(request, pk):
    """
    This api takes the pk of a room as argument and extract the details from the database.

    Requires client to me logged in / authenticated
    """
    try:
        room = Room.objects.get(id = pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    except Exception as e:
        return Response({
            "status": 404,
            "message": "Room doesn't exist"
        })
    