from django.shortcuts import render
from . forms import GroupForm
from . models import Group


def home(request):
    groups = Group.objects.all()

    return render(request, 'core/home.html', {'groups':groups})

def create_group(request):
    form = GroupForm()
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form' : form,
    }
    return render(request, 'core/create_group.html', context)    

