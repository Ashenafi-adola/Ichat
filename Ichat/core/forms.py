from django.forms import ModelForm, Textarea, TextInput
from .models import Group, Channel, GroupMessage, ChannelMessage, FriendMessage


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
        fields = ['body']
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
        fields = ['body']
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
        fields = ['body']
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