"""When Channels accepts a WebSocket connection, it consults 
the root routing configuration to lookup a consumer, and then 
calls various functions on the consumer to handle events from the connection.

We will write a consumer that accepts WebSocket connections on the 
path /ws/chat/ROOM_NAME/ that takes any message it receives on the WebSocket."""

import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """WebSocket Consumer class"""

    async def connect(self):
        """Connect a user. 
        Сalled when the user tries to connect"""
        
        # one room and room group for all
        # self.room_name = "Test-Room"
        self.room_group_name = "Test-Room"

        # join user to the room group 
        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)
        
        # accept the user connection
        await self.accept()


    async def disconnect(self, close_code):
        """Disconnect a user.
        Сalled when the user disconect"""
        
        # leave the room group 
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_layer)
        print("Disconect. User left the room")

    async def receive(self, text_data):
        """Receive msg.
        Called when msg from client is received"""
        
        # parse received from WebSocet data
        receive_dict = json.loads(text_data)
        message = receive_dict['message']

        # for sending received info all channels connected this group
        # sends an event to a group
        # event has "type": "send_message", where send_message is 
        # function below for sending messages
        await self.channel_layer.group_send(self.room_group_name,
                                            {'type': 'send_message',
                                             'message': message
                                            })
  
    async def send_message(self, event):
        """Get data from the room group Event and send message.
        It will be invoked for consumers that receive the event,
        for channels from room group"""

        # get data from evet dict  
        message = event['message']

        # send message
        await self.send(text_data=json.dumps({'message': message
                                             }))


