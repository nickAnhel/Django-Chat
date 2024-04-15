from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    owner = models.ForeignKey(User, related_name="chats_created", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="chats_joined", blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
