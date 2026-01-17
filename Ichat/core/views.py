from django.shortcuts import render
from . forms import GroupForm
def home(request):
    form = GroupForm()
    return render(request, 'core/home.html', {'form':form})