from django.urls import path
from . import views

urlpatterns = [
    path('start_chat/', views.start_chat, name='start_chat'),
    path('<str:room_name>/', views.room, name='room'),
    path('flare/admin/', views.admin, name='admin'),
    path('flare/admin/chats/', views.admin_chat_list, name='admin_chat_list')
]