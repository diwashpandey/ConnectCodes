from django.urls import path
from . import views



urlpatterns = [
    path('<int:pk>/', views.getroompage, name='roompage'),
    path('createnewroom/', views.getcreateroompage, name='createroompage'),
    path('joinroom/<str:pk>/', views.add_into_room, name='joinroom'),
    path('deleteroom/<int:pk>/', views.delete_room, name='deleteroom')
]