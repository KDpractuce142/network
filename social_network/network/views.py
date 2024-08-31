from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Chat, Publication, Message
from .forms import ChatForm, MessageForm

def chat_list(request):
    chats = Chat.objects.all()
    return render(request, 'chat_list.html', {'chats': chats})

def create_chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.save()
            return redirect('chat:chat_list')  
    else:
        form = ChatForm()
    
    return render(request, 'create_chat.html', {'form': form})

def chat(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.filter(chat=chat)
    message = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.user = request.user
            message.save()
            return redirect('chat_detail', chat_id=chat.id)
    is_moderator_or_admin = False

    return render(request, 'chat_detail.html', {
        'chat': chat,
        'message': messages,
        'form': form,
    })


def post_list(request):
    posts = Publication.objects.all()
    return render(request, 'post_list.html', {'posts': posts})