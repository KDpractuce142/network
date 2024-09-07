
from . import views
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chats/', views.chat_list, name='chat_list'),
    path('newchat/', views.create_chat, name='chatnew'),
    path('chat<int:chat_id>/', views.chat, name='chat_detail'),
    path('', views.post_list, name='post_list'),
    path('user<int:user_id>/', views.profile, name='profile'),
    path('newpost/', views.create_post, name='create_post'),
    path('post<int:post_id>/', views.post_detail, name='post'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
