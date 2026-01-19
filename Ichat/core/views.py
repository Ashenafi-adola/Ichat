from django.shortcuts import render, redirect
from . forms import GroupForm, ChannelForm, GroupMessageForm, FriendMessageForm
from . models import Group, FriendMessage, GroupMessage, ChannelMessage, Channel
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
    channels = Channel.objects.all()
    groups = Group.objects.all()
    users = User.objects.all()
    context = {
        'channels':channels,
        'groups':groups,
        'page':page,
        'users':users,
        }
    return render(request, 'core/home.html', context)

@login_required(login_url='log-in')
def create_group(request):
    page = 'group'
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
        'page' : page,
    }
    return render(request, 'core/create_group_channel.html', context)    

@login_required(login_url='log-in')
def group(request, pk):
    group = Group.objects.get(id=pk)
    groups = Group.objects.all()
    messages = GroupMessage.objects.all()
    users = User.objects.all()
    members = group.members.all()
    
    form = GroupMessageForm()
    if request.method == "POST":
        if request.POST.get('ok') == 'OK':
            group.members.add(request.user)
            return redirect(f'/group/{pk}')
        form = GroupMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.owner = request.user
            message.group = group
            message.save()
        return redirect(f'/group/{pk}')

    context = {
        'group':group,
        'groups':groups,
        'form':form,
        'messages':messages,
        'users':users,
        'members': members,
    }
    return render(request, 'core/group.html', context)

def edit_group_message(request, pk, id):
    group = Group.objects.get(id=id)
    groups = Group.objects.all()
    messages = GroupMessage.objects.all()
    users = User.objects.all()
    members = group.members.all()

    message = GroupMessage.objects.get(id=pk)
    form = GroupMessageForm(instance=message)

    if request.method == "POST":
        form = GroupMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect(f'/group/{id}/')
    context = {
        'group':group,
        'groups':groups,
        'form':form,
        'messages':messages,
        'users':users,
        'members': members,
    }

    return render(request, 'core/group.html', context)

def friend(request, pk):
    friend = User.objects.get(id = pk)
    users = User.objects.all()
    groups = Group.objects.all()
    messages = FriendMessage.objects.all()
    form = FriendMessageForm()
    if request.method == "POST":
        form = FriendMessageForm(request.POST)
        if form.is_valid():
            message = form(commit=False)
            message.owner = request.user
            message.save()
            return redirect(f'/friend/{pk}')
    context = {
        'form':form,
        'groups':groups,
        'friend':friend,
        'users':users,
        'messages':messages,
    }
    return render(request, 'core/friends.html', context)

def edit_friend_message(request, pk, id):
    friend = User.objects.get(id = id)
    users = User.objects.all()
    groups = Group.objects.all()
    messages = FriendMessage.objects.all()

    message = FriendMessage.objects.get(id=pk)
    form = FriendMessageForm(instance=message)

    if request.method == "POST":
        form = FriendMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect(f'/friend/{id}')
    context = {
        'form':form,
        'groups':groups,
        'friend':friend,
        'users':users,
        'messages':messages,
    }
    return render(request, 'core/friends.html', context)

def create_channel(request):
    page = 'channel'
    form = ChannelForm()
    if request.method == "POST":
        form = ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.owner = request.user
            channel.save()
            channel.subscribers.add(request.user)
            return redirect(f'/channel/{channel.id}')
        
    context = {
        'form' : form,
        'page' : page,
    }

    return render(request, 'core/create_group_channel.html', context)

def channel(request, pk):
    channel = Channel.objects.get(id=pk)
    channels = Channel.objects.all()
    messages = ChannelMessage.objects.all()
    users = User.objects.all()
    subscribers = channel.subscribers.all()
    
    if request.method == "POST":
        if request.POST.get('ok') == 'OK':
            channel.subscribers.add(request.user)
            return redirect(f'/channel/{pk}')
        body = request.POST.get("message")
        message = ChannelMessage(
            owner = request.user,
            channel= channel,
            body= body
        )
        message.save()
        return redirect(f'/channel/{pk}')

    context = {
        'channel':channel,
        'channels':channels,
        'messages':messages,
        'users':users,
        'subscribers': subscribers,
    }
    return render(request, 'core/channels.html', context)

