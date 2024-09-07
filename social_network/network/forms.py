from django import forms
from .models import Chat, Message, Publication, User, Like


class ChatForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
    queryset=User.objects.all(),
    widget=forms.CheckboxSelectMultiple, 
    )
    class Meta:
        model = Chat
        fields = ['name', 'members']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['desk', 'created_by']

class PostForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['desk']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = []


