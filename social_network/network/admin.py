from django.contrib import admin
from .models import *

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('desk', 'created_by', 'created_at', 'chat_id')
    search_fields = ('desk', 'created_by')

@admin.register(Publication)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('desk', 'created_by', 'created_at')
    search_fields = ('created_by', 'created_at')

@admin.register(UserData)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'bio',)
    search_fields = ('name', 'age')

@admin.register(Like)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('post', 'user',)
    search_fields = ('post',)

