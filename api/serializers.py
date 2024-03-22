from rest_framework import serializers
from rooms.models import Room, Topic, Message
from django.contrib.auth import get_user_model

User = get_user_model()

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['topic']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Message
        fields = ['user', 'message']

class RoomSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()
    host = UserSerializer()
    members = UserSerializer(many=True)
    messages = serializers.SerializerMethodField()

    def get_messages(self, obj):
        messages = Message.objects.filter(room=obj)[:10]  # Fetching latest 10 messages
        return MessageSerializer(messages, many=True).data

    class Meta:
        model = Room
        fields = ['id', 'topic', 'host', 'discription', 'members', 'messages']
