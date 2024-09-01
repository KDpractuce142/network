
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chats/', views.chat_list, name='chat_list'),
    path('newchat/', views.create_chat, name='chatnew'),
    path('<int:chat_id>/', views.chat, name='chat_detail'),
    path('', views.post_list, name='post_list'),
]
