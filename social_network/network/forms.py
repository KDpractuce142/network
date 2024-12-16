from django import forms
from .models import Chat, Message, Publication, User, Like, UserData
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ChatForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Chat
        fields = ['name', 'members']


class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Введите сообщение...'}))

    class Meta:
        model = Message
        fields = ['content']

class PostForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['desk']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = []


