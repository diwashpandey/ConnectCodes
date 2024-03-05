from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer


class CommitConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data=text_data)

    def disconnect(self):
        raise StopConsumer()
        