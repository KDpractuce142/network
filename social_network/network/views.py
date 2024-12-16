from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Chat, Publication, Message, UserData
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login   


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем пользователя в базе данных
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} был успешно создан!')
            return redirect('login')  # Перенаправляем пользователя на страницу входа
        else:
            messages.error(request, 'Исправьте ошибки в форме регистрации.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def chat_list(request):
    """Список чатов текущего пользователя"""
    chats = request.user.chats.all()
    return render(request, 'chat_list.html', {'chats': chats})

@login_required
def chat_detail(request, chat_id):
    """Детали чата с сообщениями"""
    chat = get_object_or_404(Chat, id=chat_id)
    messages = chat.messages.all().order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.user = request.user
            message.save()
            return redirect('chat_detail', chat_id=chat.id)
    else:
        form = MessageForm()

    return render(request, 'chat_detail.html', {'chat': chat, 'messages': messages, 'form': form})


@login_required
def create_chat(request):
    """Создать новый чат"""
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.save()
            form.save_m2m()  # Сохранение ManyToMany поля
            return redirect('chat_list')
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





def logout_view(request):
    logout(request)  # Выход из системы
    messages.success(request, 'Вы успешно вышли из системы.')
    return redirect('post_list')  # Перенаправляем на страницу входа

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # Проверка пользователя
        if user is not None:
            login(request, user)  # Вход пользователя в систему
            messages.success(request, 'Вы успешно вошли в систему.')
            return redirect('post_list')  # Перенаправляем на главную страницу или другую целевую страницу
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'login.html')






def profile(request, user_id):
    
    user = get_object_or_404(User, id=user_id)
    userdata = UserData.objects.filter(user=user)
    user_posts = Publication.objects.filter(created_by=user)
    return render(request, 'profile.html', {
        'userdatas': userdata,
        'user_posts': user_posts,
    })




def post_list(request):
    posts = Publication.objects.all().order_by('-created_at')
    print("sas")
    return render(request, 'post_list.html', {'posts': posts})
