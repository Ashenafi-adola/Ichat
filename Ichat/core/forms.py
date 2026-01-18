from django.forms import ModelForm
from .models import Group, Channel


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = ['name', 'description']