from django.forms import ModelForm, Textarea
from .models import  Channel, ChannelMessage,  ChannelMessageComment


class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = ['name', 'description','profile']

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