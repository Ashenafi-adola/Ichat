from django.shortcuts import render, redirect
from . forms import GroupForm
from . models import Group, FriendMessage, GroupMessage, ChannalMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
            group.members.add(request.user)
            return redirect(f'/group/{group.id}')
    context = {
        'form' : form,

    }
    return render(request, 'core/create_group.html', context)    

@login_required(login_url='log-in')
def group(request, pk):
    group = Group.objects.get(id=pk)
    groups = Group.objects.all()
    messages = GroupMessage.objects.all()
    users = User.objects.all()
    members = group.members.all()
    
    if request.method == "POST":
        body = request.POST.get("message")
        message = GroupMessage(
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
        'users':users,
        'members': members,
    }
    return render(request, 'core/group.html', context)

def friend(request, pk):
    friend = User.objects.get(id = pk)

    context = {
        'friend':friend,
    }
    return render(request, 'core/friends.html', context)