from django.urls import path
from . import views



urlpatterns = [
    path('<int:pk>/', views.getroompage, name='roompage'),
    path('createnewroom/', views.getcreateroompage, name='createroompage')
]