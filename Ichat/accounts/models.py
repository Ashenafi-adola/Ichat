from django.db import models
from django.contrib.auth.models import User

class FriendMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reciever', null=True)
    shared_media = models.ImageField(upload_to='shared_media/friend/', null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:30]