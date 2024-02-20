from django.urls import path
from . import views

urlpatterns = [
    path('', views.gethomepage, name='homepage'),
    path('login/', views.getloginpage, name='loginpage'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('register/', views.getregisterpage, name='registerpage'),
    path('profilepage/', views.getprofilepage)
]