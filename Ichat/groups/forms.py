from django.forms import ModelForm, Textarea, TextInput,PasswordInput
from .models import Group, GroupMessage


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'profile']
        widgets = {
                'name': TextInput(attrs={
                    'class': 'form-control',
                    'rows': 2,
                    'name': 'message',
                    'data-custom': 'some-value',
                    'placeholder': "Name"
                }),
                'description': Textarea(attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': "Description"
                }),
            }


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



