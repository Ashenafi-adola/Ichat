from django.shortcuts import render, redirect
from . forms import GroupForm, GroupMessageForm
from . models import Group, GroupMessage
from channels.models import Channel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
import os

@login_required(login_url='log-in')
def create_group(request):
    form = GroupForm()
    if request.method == "POST":
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            group.owner = request.user
            group.save()
            group.members.add(request.user)
            return redirect(f'home')
    context = {
        'form' : form,
    }
    return render(request, 'groups/create_group_channel.html', context)    

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
            return redirect(f'/group/group/{pk}')
        form = GroupMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.owner = request.user
            message.group = group
            message.save()
        return redirect(f'/group/group/{pk}')

    context = {
        'group':group,
        'groups':groups,
        'form':form,
        'messages':messages,
        'users':users,
        'members': members,
        'channels':channels
    }
    return render(request, 'groups/group.html', context)

@login_required(login_url='log-in')
def edit_group_message(request, pk):
    groups = Group.objects.all()
    messages = GroupMessage.objects.all()
    users = User.objects.all()
    message = GroupMessage.objects.get(id=pk)
    group = message.group
    members = group.members.all()
    channels = Channel.objects.all()

    form = GroupMessageForm(instance=message)

    if request.method == "POST":
        form = GroupMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect(f'/group/group/{group.id}/')
    context = {
        'group':group,
        'groups':groups,
        'form':form,
        'messages':messages,
        'users':users,
        'members': members,
        'channels': channels
    }

    return render(request, 'groups/group.html', context)

@login_required(login_url='log-in')
def delete_group_message(request, pk):
    delete = 'message'
    message = GroupMessage.objects.get(id=pk)
    group = message.group
    groups = Group.objects.all()
    users = User.objects.all()
    channels = Channel.objects.all()


    if request.method == "POST":
        try:
            os.remove(f'D:/Django/Ichat/Ichat{message.shared_media.url}')
        except ValueError:
            print("no file associated with it")
        message.delete()
        return redirect(f'/group/group/{group.id}')
    context = {
        'message':message,
        'group':group,
        'groups':groups,
        'users':users,
        'channels': channels,
        'delete': delete,
    }
    return  render(request, 'groups/delete_page.html', context)

@login_required(login_url='log-in')
def group_profile(request, pk):
    profile = 'group'
    group = Group.objects.get(id=pk)
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()
    members = group.members.all()
    messages = GroupMessage.objects.filter(group=group)

    
    context = {
        'profile':profile,
        'group':group,
        'groups':groups,
        'channels':channels,
        'users':users,
        'members':members,
        'messages':messages,
    }
    return render(request, 'groups/profile.html', context)

@login_required(login_url='log-in')
def view_group_media(request, pk):
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()
    message = GroupMessage.objects.get(id=pk)
    context = {
        'groups':groups,
        'channels':channels,
        'users':users,
        'message':message,
    }
    return render(request, 'groups/display_media.html', context)

@login_required(login_url='log-in')
def delete_group(request,pk):
    delete = 'group'
    group = Group.objects.get(id=pk)
    channels = Channel.objects.all()
    users = User.objects.all()
    groups = Group.objects.all()
    messages = GroupMessage.objects.filter(group=group)

    if request.method == "POST":
        for message in messages:
            try:
                os.remove(f'D:/Django/Ichat/Ichat{message.shared_media.url}')
            except ValueError:
                print("no file associated with it")
            message.delete()
        group.delete()
        return redirect('home')

    context = {
        'group':group,
        'delete':delete,
        'groups':groups,
        'channels':channels,
        'users':users,
    }
    return render(request, 'groups/delete_page.html', context)