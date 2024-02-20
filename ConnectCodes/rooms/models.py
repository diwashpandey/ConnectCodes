from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    topic = models.CharField(max_length = 40)

    def __str__(self):
        return self.topic

class Room(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    host = models.ForeignKey(User, on_delete = models.CASCADE, related_name="room_host")
    discription = models.TextField()
    members = models.ManyToManyField(User, related_name="room_members", null=True, blank = True)

    def __str__(self):
        return self.discription[:20]
    
class Message(models.Model): 
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()

    def __str__(self):
        return self.message[:20]
