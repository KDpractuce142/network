from django.contrib import admin
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):  # Змінив ім'я класу
    list_display = ('desk', 'created_by', 'created_at')
    search_fields = ('created_by', 'created_at')

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):  # Змінив ім'я класу
    list_display = ('name', 'age', 'bio',)
    search_fields = ('name', 'age')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):  # Змінив ім'я класу
    list_display = ('post', 'user',)
    search_fields = ('post',)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
