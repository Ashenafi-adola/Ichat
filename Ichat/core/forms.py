from django.forms import ModelForm
from .models import Group, Message


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'