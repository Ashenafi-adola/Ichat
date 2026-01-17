from django.shortcuts import render, redirect
from . forms import GroupForm, MessageForm
from . models import Group, Message
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    form = UserCreationForm()

    context = {
        "form":form,
    }
    return render(request, 'core/sign_in_sign_up.html', context)

def home(request):
    page = "home"
    groups = Group.objects.all()

    context = {
        'groups':groups,
        'page':page
        }
    return render(request, 'core/home.html', context)

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

def group(request, pk):
    group = Group.objects.get(id=pk)
    groups = Group.objects.all()
    messages = Message.objects.all()
    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/group/{pk}')

    context = {
        'group':group,
        'form':form,
        'groups':groups,
        'messages':messages,
    }
    return render(request, 'core/group.html', context)