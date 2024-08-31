from django.db import models
from django.contrib.auth.models import User

class Publication(models.Model):
    desk=models.CharField(max_length=1000)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_by+self.created_at
    
class Chat(models.Model):
    members=models.ManyToManyField(
        'auth.Permission',
        related_name='portal_user_permissions',
        blank=True
    )
    name=models.CharField(max_length=50, default="chat")

class Message(models.Model):
    chat=models.ForeignKey(Chat, on_delete=models.CASCADE, default="1")
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    created_at=models.DateTimeField(auto_now_add=True)
    desk=models.CharField(max_length=5000)
