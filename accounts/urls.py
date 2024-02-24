from django.urls import path
from . import views

urlpatterns = [
    path('', views.getprofilepage, name='profilepage'),
    path('editprofile/<str:userid>/', views.getedit_profilepage, name="edit_profilepage")
]