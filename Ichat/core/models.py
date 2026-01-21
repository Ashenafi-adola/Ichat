from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profiles/group/',null=True, blank=True)
    description = models.CharField(max_length=300)
    members = models.ManyToManyField(User, related_name="member")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class FriendMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reciever', null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:30]

class GroupMessage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null= True)


    def __str__(self):
        return self.body[0:30]
    
class Channel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profiles/channel/',null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    subscribers = models.ManyToManyField(User, related_name="subscribers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ChannelMessage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null= True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null= True)


    def __str__(self):
        return self.body[0:30]

class ChannelMessageComment(models.Model):
    channelmessage = models.ForeignKey(ChannelMessage, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:20]