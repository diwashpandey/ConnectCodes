from django.shortcuts import render, redirect
from .models import Message, Room
# Create your views here.

def getroompage(request, pk):
    key = int(pk)
    if request.method == 'POST':
        message = request.POST.get('message')
        room = Room.objects.get(id=key)
        Message.objects.create(room = room, user = request.user, message = message)
    
    room = Room.objects.get(id=key)
    messages = Message.objects.filter(room__id = key)
    
    return render(request, "rooms/room.html", {'messages': messages, 'room' : room})