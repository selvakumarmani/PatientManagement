from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NoseyConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("file_notification", self.channel_name)
        print(f"Added {self.channel_name} channel to file Notification")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("file_notification", self.channel_name)
        print(f"Removed {self.channel_name} channel to to file Notification")

    async def user_file_notification(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")
