from django.shortcuts import render, redirect
from . forms import FriendMessageForm, CustomUserCreationForm
from . models import FriendMessage
from channels.models import Channel
from groups.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
import os

def sign_up(request):
    page = 'signup'
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
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
    return render(request, 'accounts/sign_in_sign_up.html', context)

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
    return render(request, 'accounts/sign_in_sign_up.html', context)

@login_required(login_url='log-in')
def home(request):
    page = "home"
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    channels = Channel.objects.filter(Q(name__icontains=q))
    groups = Group.objects.filter(name__icontains=q)
    users = User.objects.filter(username__icontains=q)
    context = {
        'channels':channels,
        'groups':groups,
        'page':page,
        'users':users,
        }
    return render(request, 'accounts/home.html', context)

@login_required(login_url='log-in')
def friend(request, pk):
    friend = User.objects.get(id = pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    channels = Channel.objects.filter(Q(name__icontains=q))
    groups = Group.objects.filter(name__icontains=q)
    users = User.objects.filter(username__icontains=q)

    p = request.GET.get('p') if request.GET.get('p') != None else ''
    messages = FriendMessage.objects.filter(
            Q(body__icontains = p)
        )
    form = FriendMessageForm()
    if request.method == "POST":
        form = FriendMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.reciever = friend
            message.save()
            return redirect(f'/friend/{pk}')
    context = {
        'form':form,
        'groups':groups,
        'friend':friend,
        'users':users,
        'messages':messages,
        'channels':channels,
    }
    return render(request, 'accounts/friends.html', context)

@login_required(login_url='log-in')
def edit_friend_message(request, pk):
    users = User.objects.all()
    groups = Group.objects.all()
    messages = FriendMessage.objects.all()
    channels = Channel.objects.all()

    message = FriendMessage.objects.get(id=pk)
    friend = message.reciever
    form = FriendMessageForm(instance=message)

    if request.method == "POST":
        form = FriendMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect(f'/friend/{friend.id}')
    context = {
        'form':form,
        'groups':groups,
        'friend':friend,
        'users':users,
        'messages':messages,
        'channels': channels,
    }
    return render(request, 'accounts/friends.html', context)

@login_required(login_url='log-in')
def delete_friend_message(request, pk):
    message = FriendMessage.objects.get(id=pk)
    friend = message.reciever
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()

    if request.method == 'POST':
        try:
            os.remove(f'D:/Django/Ichat/Ichat{message.shared_media.url}')
        except ValueError:
            print("no file associated with it")        
        message.delete()
        return redirect(f'/friend/{friend.id}')
    context = {
        'message':message,
        'channels':channels,
        'users':users,
        'groups':groups,

    }
    return render(request, 'accounts/delete_message.html', context)

@login_required(login_url='log-in')
def user_profile(request, pk):
    profile = 'user'
    user = User.objects.get(id=pk)
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()
    messages = FriendMessage.objects.all()

    context = {
        'profile':profile,
        'user':user,
        'groups':groups,
        'channels':channels,
        'users':users,
        'messages':messages,
    }
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='log-in')
def view_friend_media(request, pk):
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()
    message = FriendMessage.objects.get(id=pk)
    context = {
        'groups':groups,
        'channels':channels,
        'users':users,
        'message':message,
    }
    return render(request, 'accounts/display_media.html', context)