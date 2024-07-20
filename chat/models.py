from django.db import models


class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Message(models.Model):
    username = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE, null=True, blank=True)
    room_str = models.CharField(max_length=255, default="room1")

    def __str__(self):
        return f'{self.username}: {self.content[:20]}'
    
    class Meta:
        ordering = ['timestamp']