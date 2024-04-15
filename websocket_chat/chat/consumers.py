import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.chat_group_name = f"chat_{self.chat_id}"
        async_to_sync(self.channel_layer.group_add)(  # type: ignore
            self.chat_group_name,
            self.channel_name,
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(  # type: ignore
            self.chat_group_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)  # type: ignore
        message = text_data_json["message"]
        async_to_sync(self.channel_layer.group_send)(  # type: ignore
            self.chat_group_name,
            {
                "type": "chat_message",
                "message": message,
            },
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))
