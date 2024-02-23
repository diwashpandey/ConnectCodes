from django.shortcuts import render, redirect, reverse
from rooms.models import Room, Topic
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# from django.contrib.auth.models import User


User = get_user_model()
# Create your views here.


def gethomepage(request):
    rooms = Room.objects.all().order_by("-id")
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
                return redirect('loginpage')
            else:
                messages.error(request, "Password didnot match")
                
        else:
            messages.error(request, "Username already exists")
    return render(request, 'home/register.html')

def getprofilepage(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            data = request.POST
            commit = data.get("commit")
            print('This is the connit:\n\n:',commit)
            commit = commit.strip().split()

            to_do = commit[0]
            comit_to_username = commit[1]
            requested_username = request.user.username
            print(f"Request get from {requested_username} for {to_do} to {comit_to_username}")
            self_user = User.objects.get(username = requested_username)
            to_user = User.objects.get(username = comit_to_username)
            try:
                if to_do == 'follow':
                    self_user.following.add(to_user)
                elif to_do == 'unfollow':
                    self_user.following.remove(to_user)
            except:
                print("i am in except")
                return redirect("homepage")
        else:
            return redirect('loginpage')
        

    username = request.GET.get('profile')


    try:
        user = User.objects.get(username=username)
        room_count = user.room_host.all().count()

        followers = user.followers.all()
        followers_count = followers.count()
        following_count = user.following.all().count()

        already_following = False
        if user in request.user.following.all():
            already_following = True


        data = {"user" : user,
                "room_count":room_count,
                "followers":followers_count,
                "following":following_count,
                'already_following': already_following}
        
        


        return render(request, 'home/profilepage.html', data)
    except User.DoesNotExist:
        return redirect('homepage')


