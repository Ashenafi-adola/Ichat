from django.shortcuts import render, redirect
from . forms import GroupForm
from . models import Group, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def sign_up(request):
    page = 'signup'
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
    context = {
        "form":form,
        "page":page,
    }
    return render(request, 'core/sign_in_sign_up.html', context)

def log_out(request):
    logout(request)
    return redirect('home')
    
def log_in(request):
    page = 'signin'
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username= username, password=password)
        if user != None:
            login(request, user)
            return redirect("home")
    context = {
        "page":page,
    }
    return render(request, 'core/sign_in_sign_up.html', context)

@login_required(login_url='log-in')
def home(request):
    page = "home"
    groups = Group.objects.all()

    context = {
        'groups':groups,
        'page':page
        }
    return render(request, 'core/home.html', context)

@login_required(login_url='log-in')
def create_group(request):
    form = GroupForm()
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.owner = request.user
            group.save()
            return redirect(f'/group/{group.id}')
    context = {
        'form' : form,
    }
    return render(request, 'core/create_group.html', context)    

@login_required(login_url='log-in')
def group(request, pk):
    group = Group.objects.get(id=pk)
    groups = Group.objects.all()
    messages = Message.objects.all()
    
    
    if request.method == "POST":
        body = request.POST.get("message")
        message = Message(
            owner = request.user,
            group= group,
            body= body
        )
        message.save()
        return redirect(f'/group/{pk}')

    context = {
        'group':group,
        'groups':groups,
        'messages':messages,
    }
    return render(request, 'core/group.html', context)

def create_channel(request):

    return render(request, '')