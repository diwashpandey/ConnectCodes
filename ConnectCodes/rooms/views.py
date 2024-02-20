from django.shortcuts import render, redirect
from .models import Message, Room, Topic
# Create your views here.

def getroompage(request, pk):
    key = int(pk)

    if request.method == 'POST':
        message = request.POST.get('message')
        room = Room.objects.get(id=key)
        Message.objects.create(room = room, user = request.user, message = message)
    
    room = Room.objects.get(id=key)
    room_members = room.members.all()
    messages = Message.objects.filter(room__id = key)

    return render(request, "rooms/room.html", {'messages': messages, 'room' : room, 'room_members': room_members})


def getcreateroompage(request):
    if request.method == "POST":
        data = request.POST

        selected_topic = data.get('topic')
        description = data.get('description')

        topic = Topic.objects.get(topic = selected_topic)
        room = Room.objects.create(topic = topic, discription = description, host=request.user)
        room.members.add(request.user)
        return redirect('homepage')
    
    topics = Topic.objects.all()
    return render(request, 'rooms/createroom.html',{'topics':topics})