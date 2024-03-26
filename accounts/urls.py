from django.urls import path
from . import views

urlpatterns = [
    path('', views.getprofilepage, name='profilepage'),
    path('editprofile/<str:userid>/', views.getedit_profilepage, name="edit_profilepage"),
    path('register/', views.GetRegisterPage.as_view(), name='registerpage'),
    path('login/', views.GetLoginPage.as_view(), name='loginpage'),
    path('logout/', views.logoutuser, name='logoutuser'),
]