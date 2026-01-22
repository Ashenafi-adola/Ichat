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

class GroupMessage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    shared_media = models.ImageField(upload_to='shared_media/group/', null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null= True)


    def __str__(self):
        return self.body[0:30]
    