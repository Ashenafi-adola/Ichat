from django.shortcuts import render, redirect
from . forms import FriendMessageForm, CustomUserCreationForm
from . models import FriendMessage
from ichat_channel.models import Channel
from groups.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.db.models import Q
import os
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/sign_up.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        form.username = user.username.lower()
        user.save()
        login(self.request, user)
        return redirect("home")

def log_out(request):
    logout(request)
    return redirect('home')

@method_decorator(login_required(login_url='log-in'), name='dispatch')
class Home(ListView):
    template_name = 'accounts/home.html'
    model = CustomUser
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channels'] = Channel.objects.all()
        context['groups'] = Group.objects.all()
        context['users'] = CustomUser.objects.all()
        return context

@method_decorator(login_required(login_url='log-in'), name='dispatch')
class Friend(DetailView, ModelFormMixin):
    model = CustomUser
    template_name = 'accounts/friends.html'
    form_class = FriendMessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channels'] = Channel.objects.all()
        context['groups'] = Group.objects.all()
        context['users'] = CustomUser.objects.all()
        context['messages'] = FriendMessage.objects.all()
        context['friend'] = CustomUser.objects.get(id=self.kwargs['pk'])

        return context 
    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.reciever = CustomUser.objects.get(id=self.kwargs['pk'])
        message.save()
        return redirect(f'/friend/{self.kwargs["pk"]}')
    def post(self, request, *args, **kwargs):
        form = FriendMessageForm(request.POST, request.FILES)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
@method_decorator(login_required(login_url='log-in'), name='dispatch')
class EditFriendMessage(UpdateView):
    model = FriendMessage
    form_class = FriendMessageForm
    template_name = 'accounts/friends.html'
    
    def get_success_url(self):
        return f'/friend/{self.get_context_data()['friend'].id}/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channels'] = Channel.objects.all()
        context['groups'] = Group.objects.all()
        context['users'] = CustomUser.objects.all()
        context['messages'] = FriendMessage.objects.all()
        context['friend'] = FriendMessage.objects.get(id=self.kwargs['pk']).reciever
        return context
    
class DeleteFriendMessage(DeleteView):
    model = FriendMessage
    template_name = 'accounts/delete_message.html'

    def get_success_url(self):
        return f'/friend/{self.get_context_data()['friend'].id}/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channels'] = Channel.objects.all()
        context['groups'] = Group.objects.all()
        context['users'] = CustomUser.objects.all()
        context['message'] = FriendMessage.objects.get(id=self.kwargs['pk'])
        context['friend'] = context['message'].reciever
        return context


@login_required(login_url='log-in')
def delete_friend_message(request, pk):
    message = FriendMessage.objects.get(id=pk)
    friend = message.reciever
    channels = Channel.objects.all()
    users = CustomUser.objects.all()
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
        'friend':friend,
    }
    return render(request, 'accounts/delete_message.html', context)

@login_required(login_url='log-in')
def user_profile(request, pk):
    profile = 'user'
    user = CustomUser.objects.get(id=pk)
    channels = Channel.objects.all()
    users = CustomUser.objects.all()
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
    users = CustomUser.objects.all()
    groups = Group.objects.all()
    message = FriendMessage.objects.get(id=pk)
    context = {
        'groups':groups,
        'channels':channels,
        'users':users,
        'message':message,
    }
    return render(request, 'accounts/display_media.html', context)