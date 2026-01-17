from django.forms import ModelForm
from .models import Group, Message


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
