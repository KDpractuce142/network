from django import forms
from .models import Chat, Message


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['name', 'members']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['desk', 'created_by']

