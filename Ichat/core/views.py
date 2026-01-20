from django.shortcuts import render, redirect
from . forms import GroupForm, ChannelForm, GroupMessageForm, FriendMessageForm, ChannelMessageForm
from . models import Group, FriendMessage, GroupMessage, ChannelMessage, Channel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

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
    return render(request, 'core/home.html', context)

@login_required(login_url='log-in')
def create_group(request):
    page = 'group'
    form = GroupForm()
    if request.method == "POST":
        form = GroupForm(request.POST, request.FILES)
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    p = request.GET.get('p') if request.GET.get('p') != None else ''
    channels = Channel.objects.filter(Q(name__icontains=q))
    groups = Group.objects.filter(name__icontains=q)
    users = User.objects.filter(username__icontains=q)

    messages = GroupMessage.objects.filter(
        Q(body__icontains = p)
    )
    
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
        'channels':channels
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    channels = Channel.objects.filter(Q(name__icontains=q))
    groups = Group.objects.filter(name__icontains=q)
    users = User.objects.filter(username__icontains=q)

    messages = FriendMessage.objects.all()
    form = FriendMessageForm()
    if request.method == "POST":
        form = FriendMessageForm(request.POST)
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
        form = ChannelForm(request.POST, request.FILES)
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
    groups = Group.objects.all()
    subscribers = channel.subscribers.all()
    form = ChannelMessageForm()

    if request.method == "POST":
        if request.POST.get('ok') == 'OK':
            channel.subscribers.add(request.user)
            return redirect(f'/channel/{pk}')
        form = ChannelMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.owner = request.user
            message.channel = channel
            message.save()
            return redirect(f'/channel/{pk}')

    context = {
        'channel':channel,
        'channels':channels,
        'messages':messages,
        'users':users,
        'groups':groups,
        'subscribers': subscribers,
        'form':form,
    }
    return render(request, 'core/channels.html', context)

def edit_channel_message(request, pk, id):
    channel = Channel.objects.get(id=id)
    channels = Channel.objects.all()
    messages = ChannelMessage.objects.all()
    users = User.objects.all()
    subscribers = channel.subscribers.all()

    message = ChannelMessage.objects.get(id=pk)
    form = ChannelMessageForm(instance=message)

    if request.method == "POST":
        form = ChannelMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect(f'/channel/{id}/')
    context = {
        'channel':channel,
        'channels':channels,
        'form':form,
        'messages':messages,
        'users':users,
        'subscribers': subscribers,
    }

    return render(request, 'core/channels.html', context)