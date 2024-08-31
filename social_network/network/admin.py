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
