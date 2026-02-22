from django.db import models
from django.contrib.auth.models import User, AbstractUser

class CustomUser(AbstractUser):
    profile = models.ImageField(upload_to='profiles/users', blank=True, null=True)


class FriendMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reciever = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='reciever', null=True)
    shared_media = models.ImageField(upload_to='shared_media/friend/', null=True, blank=True)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:30]