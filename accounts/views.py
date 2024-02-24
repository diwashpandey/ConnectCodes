from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

@login_required(login_url="loginpage")
def getprofilepage(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            data = request.POST
            commit = data.get("commit")
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

        return render(request, 'accounts/profilepage.html', data)
    except User.DoesNotExist:
        return redirect('homepage')

@login_required(login_url='login_page')
def getedit_profilepage(request, userid):
    try:
        user = User.objects.get(username = userid)

        if request.method == "POST":
            received_data = request.POST 
            user.full_name = received_data.get("full_name")
            user.bio = received_data.get("bio")
            user.location = received_data.get("location")
            user.save()
            print(reverse('profilepage')+"?="+userid)
            return redirect(reverse('profilepage')+"?profile="+userid)

        if user == request.user:
            return render(request, 'accounts/edit_profilepage.html', {"user" : user})
        else:
            return redirect("homepage")
            
    except:
        return redirect("homepage")
