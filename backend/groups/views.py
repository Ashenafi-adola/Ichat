from django.shortcuts import render, redirect
from . forms import GroupForm, GroupMessageForm
from . models import Group, GroupMessage
from ichat_channel.models import Channel
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.db.models import Q
import os
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='log-in'), name='dispatch')
class CreateGroup(CreateView):
    form_class = GroupForm
    template_name = 'groups/create_group.html'

    def form_valid(self, form):
        group = form.save(commit=False)
        group.owner = self.request.user
        group.save()
        group.members.add(self.request.user)
        return redirect(f'home') 

class GroupView(DetailView):
    model = Group
    template_name = 'groups/group.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["channels"] = Channel.objects.all()
        context["groups"] = Group.objects.all()
        context["form"] = GroupMessageForm()
        context["users"] = CustomUser.objects.all()
        context["messages"] = GroupMessage.objects.all()
        context["group"] = Group.objects.get(id= self.kwargs['pk'])
        context["members"] = Group.objects.get(id=self.kwargs['pk']).members.all()
        return context
    
    def post(self, request, *args, **kwargs):
        group = Group.objects.get(id=self.kwargs['pk'])
        form = GroupMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.owner = request.user
            message.group = group
            message.save()
        return redirect(f'/group/group/{group.id}/')

@method_decorator(login_required(login_url='log-in'), name='dispatch')
class EditGroupMessage(UpdateView):
    model = GroupMessage
    form_class = GroupMessageForm
    template_name = 'groups/group.html'

    def get_success_url(self):
        return f'/group/group/{self.get_context_data()['group'].id}/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = super().get_context_data()
        context["channels"] = Channel.objects.all()
        context["groups"] = Group.objects.all()
        context["users"] = CustomUser.objects.all()
        context["messages"] = GroupMessage.objects.all()
        context['message'] = GroupMessage.objects.get(id=self.kwargs['pk'])
        context["group"] = GroupMessage.objects.get(id=self.kwargs['pk']).group
        context["members"] = GroupMessage.objects.get(id=self.kwargs['pk']).group.members.all()
        return context
 
class DeleteGroupMessage(DeleteView):
    model
@login_required(login_url='log-in')
def delete_group_message(request, pk):
    delete = 'message'
    message = GroupMessage.objects.get(id=pk)
    group = message.group
    groups = Group.objects.all()
    users = CustomUser.objects.all()
    channels = Channel.objects.all()


    if request.method == "POST":
        try:
            os.remove(f'D:/Django/Ichat/Ichat{message.shared_media.url}')
        except ValueError:
            print("no file associated with it")
        message.delete()
        return redirect(f'/group/group/{group.name}')
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
    users = CustomUser.objects.all()
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
    users = CustomUser.objects.all()
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
    users = CustomUser.objects.all()
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