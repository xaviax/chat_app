from django.shortcuts import render
from .models import ChatRoom,ChatMessage
# Create your views here.

def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request,'myapp/index.html',{'chatrooms':chatrooms})

def chatroom(request, slug):
    chat_room = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chat_room)
    return render(request,'myapp/room.html',{'chat_room':chat_room, 'messages':messages})