from django.urls import path
from . import views


urlpatterns = [
    path("room-details/<int:pk>", views.get_room_details),
    # path("user-detail/<int:pk>", views.get_user_details)
]