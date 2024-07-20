from django.contrib import admin
from .models import Message, ChatRoom

class MessageAdmin(admin.ModelAdmin):
    list_display = ('username', 'content', 'timestamp', 'room_str')
    list_filter = ('room_str', 'timestamp')
    search_fields = ('username', 'content')

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ['room_str', 'timestamp']
        else:
            return ['timestamp']

admin.site.register(Message, MessageAdmin)
admin.site.register(ChatRoom)