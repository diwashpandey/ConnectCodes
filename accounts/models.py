from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_photo/", default="default_profile_photo.jpg")
    location = models.CharField(max_length = 256, blank=True)
    age = models.IntegerField(blank=True,  null=True)
    friends = models.ManyToManyField('self')