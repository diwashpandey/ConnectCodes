from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(User):
    name = models.CharField(max_length = 50, default="ConnectCode User")
    profile_photo = models.ImageField(upload_to="profile_photo/", default='default_profile_photo.jpg')

    def __str__(self):
        return self.username