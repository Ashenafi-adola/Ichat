from django.forms import ModelForm, Textarea, TextInput,PasswordInput
from .models import Group, Channel, GroupMessage, ChannelMessage, FriendMessage, ChannelMessageComment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            'username': TextInput(attrs={
                'class':"form-control",

            }),
        }
    def save(self, commit = True):
        user = super().save(commit=True)
        return user

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'profile']

class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = ['name', 'description','profile']

class GroupMessageForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body', 'shared_media']
        widgets = {
            'body': Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'name': 'message',
                'data-custom': 'some-value',
                'placeholder': "Type message here..."
            }),
        }

class ChannelMessageForm(ModelForm):
    class Meta:
        model = ChannelMessage
        fields = ['body', 'shared_media']
        widgets = {
            'body': Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'name': 'message',
                'data-custom': 'some-value',
                'placeholder': "Type message here..."
            }),
        }

class FriendMessageForm(ModelForm):
    class Meta:
        model = FriendMessage
        fields = ['body', 'shared_media']
        widgets = {
            'body': Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'name': 'message',
                'style': "width: 100%",
                'data-custom': 'some-value',
                'placeholder': "Type message here..."
            }),
        }
class CommentForm(ModelForm):
    class Meta:
        model = ChannelMessageComment
        fields = ['body', 'shared_media']
        widgets = {
            'body': Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'name': 'message',
                'style': "width: 100%",
                'data-custom': 'some-value',
                'placeholder': "Type message here..."
            }),
        }