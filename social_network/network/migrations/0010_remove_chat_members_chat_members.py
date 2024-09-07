# Generated by Django 5.1 on 2024-09-07 09:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_remove_chat_members_chat_members'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='members',
        ),
        migrations.AddField(
            model_name='chat',
            name='members',
            field=models.ManyToManyField(default='1', to=settings.AUTH_USER_MODEL),
        ),
    ]
