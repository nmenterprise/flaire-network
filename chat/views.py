from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .models import ChatRoom

def room(request, room_name):
    if room_name != "favicon.ico":
        ChatRoom.objects.get_or_create(name=room_name)
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def admin(request):
    return render(request, 'chat/admin.html')

def start_chat(request):
    if request.method == 'POST':
        username = request.POST['username']
        room_name = get_random_string(12)  # Generate a unique room name
        return redirect('room', room_name=room_name)
    return render(request, 'chat/start.html')

def admin_chat_list(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chat/admin_chat_list.html', {'chat_rooms': chat_rooms})