from django.shortcuts import redirect
from . forms import FriendMessageForm, CustomUserCreationForm
from . models import FriendMessage
from ichat_channel.models import Channel
from groups.models import Group
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
from django.utils.decorators import method_decorator

from rest_framework.permissions import AllowAny
from rest_framework import status, generics, viewsets
from . serializers import FriendMessageSerialize

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
    
@method_decorator(login_required(login_url='log-in'), name='dispatch')
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

class UserProfile(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channels'] = Channel.objects.all()
        context['groups'] = Group.objects.all()
        context['users'] = CustomUser.objects.all()
        context['user'] = CustomUser.objects.get(id=self.kwargs['pk'])
        return context
    
class ViewSharedMedia(ListView):
    model = FriendMessage
    template_name = 'accounts/shared_media.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channels'] = Channel.objects.all()
        context['groups'] = Group.objects.all()
        context['users'] = CustomUser.objects.all()
        context['friend'] = CustomUser.objects.get(id=self.kwargs['pk'])
        context['messages'] = FriendMessage.objects.filter(
            Q(sender=self.request.user, reciever=context['friend']) | Q(sender=context['friend'], reciever=self.request.user),
            Q(image__isnull=False) | Q(video__isnull=False)
        ).order_by('-created_at')
        return context

class MessageApiView(viewsets.ModelViewSet):
    queryset = FriendMessage.objects.all()
    serializer_class = FriendMessageSerialize
    permission_classes = [AllowAny]
