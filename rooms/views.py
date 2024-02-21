from django.shortcuts import render, redirect
from .models import Message, Room, Topic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def getroompage(request, pk):
    key = int(pk)

    # this receives the messege that user has sent
    if request.method == 'POST':
        message = request.POST.get('message')
        room = Room.objects.get(id=key)
        Message.objects.create(room = room, user = request.user, message = message)
    
    

    room = Room.objects.get(id=key)
    room_members = room.members.all()
    messages = Message.objects.filter(room__id = key)
    is_member = False
    if request.user in room_members:
        is_member = True
    print("Is member:", is_member)
    return render(request, "rooms/room.html", {'messages': messages, 'room' : room, 'room_members': room_members, "is_member": is_member})

@login_required(login_url = "loginpage")
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

@login_required(login_url = "loginpage")
def add_into_room(request, pk):
    user = request.user
    room = Room.objects.get(id = pk)
    room.members.add(user)
    return redirect('roompage', pk=pk)
