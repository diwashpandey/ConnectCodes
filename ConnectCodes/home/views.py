from django.shortcuts import render, redirect
from rooms.models import Room, Topic
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def gethomepage(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    return render(request, 'home/home.html', {"rooms":rooms, "topics":topics})


def getloginpage(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                messages.error(request, "Username or password didn't match")
        else:
            messages.error(request, "Username didn't found")

    return render(request, "home/login.html")

def logoutuser(request):
    
    logout(request)
    return redirect('loginpage')

def getregisterpage(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        repassword = data.get('repassword')

        check_user = User.objects.filter(username = username)
        if not check_user.exists():
            if password == repassword:
                user = User.objects.create(username = username)
                user.set_password(password)
                user.save()
            else:
                messages.error(request, "Password didnot match")
                
        else:
            messages.error(request, "Username already exists")
    return render(request, 'home/register.html')