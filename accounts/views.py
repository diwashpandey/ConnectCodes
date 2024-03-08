from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

@login_required(login_url="loginpage")
def getprofilepage(request):
    
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
            profile_pic = request.FILES.get("profile_pic")

            if profile_pic is not None:
                user.profile_pic = profile_pic
            user.save()
            return redirect(reverse('profilepage')+"?profile="+userid)

        if user == request.user:
            return render(request, 'accounts/edit_profilepage.html', {"user" : user})
        else:
            return redirect("homepage")
            
    except Exception as e:
        print("An error occurred:", e)
