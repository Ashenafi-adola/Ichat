from django.shortcuts import render, redirect
from .forms import ChannelForm, ChannelMessageForm, CommentForm
from .models import ChannelMessage, Channel, ChannelMessageComment
from groups.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
import os


@login_required(login_url='log-in')
def create_channel(request):
    form = ChannelForm()
    if request.method == "POST":
        form = ChannelForm(request.POST, request.FILES)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.owner = request.user
            channel.save()
            channel.subscribers.add(request.user)
            return redirect(f'/channel/channel/{channel.id}')
        
    context = {
        'form' : form,
    }

    return render(request, 'ichat_channel/create_group_channel.html', context)

@login_required(login_url='log-in')
def channel(request, pk):
    channel = Channel.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    p = request.GET.get('p') if request.GET.get('p') != None else ''
    
    channels = Channel.objects.filter(Q(name__icontains=q))
    groups = Group.objects.filter(Q(name__icontains=q))
    users = User.objects.filter(Q(username__icontains=q))
    messages = ChannelMessage.objects.filter(channel=channel).filter(
        Q(body__icontains=p)
    )
    subscribers = channel.subscribers.all()
    form = ChannelMessageForm()

    if request.method == "POST":
        if request.POST.get('ok') == 'OK':
            channel.subscribers.add(request.user)
            return redirect(f'/channel/channel/{pk}')
        form = ChannelMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.owner = request.user
            message.channel = channel
            message.save()
            return redirect(f'/channel/channel/{pk}')

    context = {
        'channel':channel,
        'channels':channels,
        'messages':messages,
        'users':users,
        'groups':groups,
        'subscribers': subscribers,
        'form':form,
    }
    return render(request, 'ichat_channel/channels.html', context)

@login_required(login_url='log-in')
def edit_channel_message(request, pk):
    message = ChannelMessage.objects.get(id=pk)
    channel = message.channel
    channels = Channel.objects.all()
    messages = ChannelMessage.objects.filter(channel=channel)
    users = User.objects.all()
    groups = Group.objects.all()
    subscribers = channel.subscribers.all()
    form = ChannelMessageForm(instance=message)

    if request.method == "POST":
        form = ChannelMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect(f'/channel/channel/{channel.id}/')
    context = {
        'channel':channel,
        'channels':channels,
        'groups':groups,
        'form':form,
        'messages':messages,
        'users':users,
        'subscribers': subscribers,
    }

    return render(request, 'ichat_channel/channels.html', context)

@login_required(login_url='log-in')
def delete_channel_message(request, pk):
    delete = 'delete'
    message = ChannelMessage.objects.get(id=pk)
    channel = message.channel
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()

    if request.method == 'POST': 
        try:
            os.remove(f'D:/Django/Ichat/Ichat{message.shared_media.url}')
        except ValueError:
            print("no file associated with it")
        message.delete()
        return redirect(f'/channel/channel/{channel.id}/')
    context = {
        'message':message,
        'channels':channels,
        'users':users,
        'groups':groups,
        'delete': delete,
    }
    return render(request, 'ichat_channel/delete_page.html', context)

@login_required(login_url='log-in')
def leave_comment(request, pk):
    message = ChannelMessage.objects.get(id=pk)
    channel = message.channel
    comments = ChannelMessageComment.objects.filter(channelmessage=message)
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user
            comment.channelmessage = message
            comment.save()
            return redirect(f'/channel/comment/{pk}')
    
    context = {
        'comments':comments,
        'channel':channel,
        'message':message,
        'channels':channels,
        'users':users,
        'groups':groups,
        'form':form,
    }
    return render(request, 'ichat_channel/comments.html', context)

@login_required(login_url='log-in')
def edit_comment(request, pk, id):
    message = ChannelMessage.objects.get(id=pk)
    channel = message.channel
    comments = ChannelMessageComment.objects.filter(channelmessage=message)
    channels = Channel.objects.all()
    users = User.objects.all()
    comment = ChannelMessageComment.objects.get(id=id)
    groups = Group.objects.all()
    form = CommentForm(instance=comment)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user
            comment.channelmessage = message
            comment.save()
            return redirect(f'/channel/comment/{pk}')
    
    context = {
        'comments':comments,
        'channel':channel,
        'message':message,
        'channels':channels,
        'users':users,
        'groups':groups,
        'form':form,
    }
    return render(request, 'ichat_channel/comments.html', context)

@login_required(login_url='log-in')
def delete_comment(request, pk):
    delete = 'comment'
    comment = ChannelMessageComment.objects.get(id=pk)
    message = comment.channelmessage
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()

    if request.method == 'POST': 
        try:
            os.remove(f'D:/Django/Ichat/Ichat{comment.shared_media.url}')
        except ValueError:
            print("no file associated with it")
        comment.delete()
        return redirect(f'/channel/comment/{message.id}/')
    context = {
        'message':comment,
        'channels':channels,
        'users':users,
        'groups':groups,
        'delete':delete,
    }
    return render(request, 'ichat_channel/delete_page.html', context)

@login_required(login_url='log-in')
def channel_profile(request, pk):
    channel = Channel.objects.get(id=pk)
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()
    subscribers = channel.subscribers.all()
    messages = ChannelMessage.objects.filter(channel=channel)

    context = {
        'channel':channel,
        'groups':groups,
        'channels':channels,
        'users':users,
        'subscribers':subscribers,
        'messages':messages,
    }
    return render(request, 'ichat_channel/profile.html', context)

@login_required(login_url='log-in')
def view_channel_media(request, pk):
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()
    message = ChannelMessage.objects.get(id=pk)
    context = {
        'groups':groups,
        'channels':channels,
        'users':users,
        'message':message,
    }
    return render(request, 'ichat_channel/display_media.html', context)

@login_required(login_url='log-in')
def delete_channel(request,pk):
    delete = 'channel'
    channel = Channel.objects.get(id=pk)
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()
    messages = ChannelMessage.objects.filter(channel=channel)

    if request.method == "POST":
        for message in messages:
            try:
                os.remove(f'D:/Django/Ichat/Ichat{message.shared_media.url}')
            except ValueError:
                print("no file associated with it")
            message.delete()
        channel.delete()
        return redirect('home')

    context = {
        'channel':channel,
        'delete':delete,
        'groups':groups,
        'channels':channels,
        'users':users,
    }
    return render(request, 'ichat_channel/delete_page.html', context)