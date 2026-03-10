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
        context = super().get_context_data(**kwargs)
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
        context["channels"] = Channel.objects.all()
        context["groups"] = Group.objects.all()
        context["users"] = CustomUser.objects.all()
        context["messages"] = GroupMessage.objects.all()
        context['message'] = GroupMessage.objects.get(id=self.kwargs['pk'])
        context["group"] = GroupMessage.objects.get(id=self.kwargs['pk']).group
        context["members"] = GroupMessage.objects.get(id=self.kwargs['pk']).group.members.all()
        return context
 
@method_decorator(login_required(login_url='log-in'), name='dispatch')
class DeleteGroupMessage(DeleteView):
    model = GroupMessage
    template_name = 'groups/delete_page.html'

    def get_success_url(self):
        return f'/group/group/{self.get_context_data()['group'].id}/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete'] = 'message'
        context["channels"] = Channel.objects.all()
        context["groups"] = Group.objects.all()
        context["users"] = CustomUser.objects.all()
        context['message'] = GroupMessage.objects.get(id=self.kwargs['pk'])
        context["group"] = GroupMessage.objects.get(id=self.kwargs['pk']).group
        return context
 
@method_decorator(login_required(login_url='log-in'), name='dispatch')
class GroupProfile(DetailView):
    model = Group
    template_name = 'groups/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = 'group'
        context["channels"] = Channel.objects.all()
        context["groups"] = Group.objects.all()
        context["form"] = GroupMessageForm()
        context["users"] = CustomUser.objects.all()
        context["messages"] = GroupMessage.objects.filter(group=Group.objects.get(id= self.kwargs['pk']))
        context["group"] = Group.objects.get(id= self.kwargs['pk'])
        context["members"] = Group.objects.get(id=self.kwargs['pk']).members.all()
        return context
  
@method_decorator(login_required(login_url='log-in'), name='dispatch')
class ViewGroupMedia(DetailView):
    model = GroupMessage
    template_name = 'groups/display_media.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["channels"] = Channel.objects.all()
        context["groups"] = Group.objects.all()
        context["users"] = CustomUser.objects.all()
        context['message'] = GroupMessage.objects.get(id=self.kwargs['pk'])
        return context

@method_decorator(login_required(login_url='log-in'), name='dispatch')
class DeleteGroup(DeleteView):
    model = Group
    template_name = "groups/delete_page.html"

    def get_success_url(self):
        return f'home'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete'] = 'group'
        context["channels"] = Channel.objects.all()
        context["groups"] = Group.objects.all()
        context["users"] = CustomUser.objects.all()
        context["group"] = Group.objects.get(id=self.kwargs['pk'])
        return context    
