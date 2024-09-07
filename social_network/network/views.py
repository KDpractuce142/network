from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Chat, Publication, Message, UserData
from .forms import *

def chat_list(request):
    chats = Chat.objects.all()
    return render(request, 'chat_list.html', {'chats': chats})

def create_chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.save()
            return redirect('chat_detail', chat_id=chat.id)
    else:
        form = ChatForm()
    
    return render(request, 'create_chat.html', {'form': form})


def like(request, post_id):
        print(post_id)
        post = get_object_or_404(Publication, id=post_id)
        like_qs = Like.objects.filter(post=post, user=request.user)
        if like_qs.exists():
            like_qs.delete()
        else:    
            if request.method == 'POST':
                form = LikeForm(request.POST)
                if form.is_valid():
                    like = form.save(commit=False)
                    like.save()
            else:
                form = LikeForm()
            return render(request, "post_list.html", {'form': form})
        

def post_detail(request, post_id):
    print(post_id)
    post = get_object_or_404(Publication, id=post_id)
    like_qs = Like.objects.filter(post=post, user=request.user)
    if like_qs.exists():
        like_qs.delete()
    else:    
        if request.method == 'POST':
            form = LikeForm(request.POST)
            if form.is_valid():
                like = form.save(commit=False)
                like.save()
        else:
            form = LikeForm()
            return render(request, "post_detail.html", {'form': form,
                                                  })

    return render(request, "post_detail.html", {'post': post,
                                                  })


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})




def chat(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.filter(chat=chat)
    form = MessageForm()

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
        'messages': messages,
        'form': form,
    })

def profile(request, user_id):
    
    user = get_object_or_404(User, id=user_id)
    userdata = UserData.objects.filter(user=user)
    user_posts = Publication.objects.filter(created_by=user)
    return render(request, 'profile.html', {
        'userdatas': userdata,
        'user_posts': user_posts,
    })




def post_list(request):
    posts = Publication.objects.all()
    print("sas")
    return render(request, 'post_list.html', {'posts': posts})
