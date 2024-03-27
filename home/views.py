from django.shortcuts import render, redirect, reverse
from rooms.models import Room, Topic
from django.contrib.auth import get_user_model

from django.db.models import Q
from django.views.generic.base import TemplateView

User = get_user_model()

def gethomepage(request):
    search = request.GET.get("search")
    search = "" if search == None else search
    rooms = None

    
    rooms = Room.objects.filter(Q(topic__topic__icontains = search) | 
                                Q(host__username__icontains = search) |
                                Q(discription__icontains = search) |
                                Q(topic__subtopic__subtopic__icontains = search)).order_by("-id")

    
    topics = Topic.objects.all()
    return render(request, 'home/home.html', {"rooms":rooms, "topics":topics})



