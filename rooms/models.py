from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Topic(models.Model):
    topic = models.CharField(max_length = 40)

    def __str__(self):
        return self.topic
    
class SubTopic(models.Model):
    subtopic = models.CharField(max_length = 40)
    main_topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    def __str__(self):
        return self.subtopic

class Room(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    subtopic = models.ForeignKey(SubTopic, on_delete = models.CASCADE)
    host = models.ForeignKey(User, on_delete = models.CASCADE, related_name="room_host")
    discription = models.TextField()
    members = models.ManyToManyField(User, related_name="room_members")
    
    def __str__(self):
        return self.discription[:20]
    
class Message(models.Model): 
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()

    def __str__(self):
        return self.message[:20]
