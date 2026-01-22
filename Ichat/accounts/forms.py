from django.forms import ModelForm, Textarea, TextInput
from .models import FriendMessage
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
