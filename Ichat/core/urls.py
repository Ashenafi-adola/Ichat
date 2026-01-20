from django.urls import path
from .import views

urlpatterns = [
    path('sign-up/', views.sign_up, name="sign-up"),
    path('sign-in/', views.log_in, name='log-in'),
    path('logout/', views.log_out, name='logout'),
    path('', views.home, name='home'),
    path('create_group/', views.create_group, name='create_group'),
    path('create_channel/', views.create_channel, name='create_channel'),
    path('group/<int:pk>/', views.group, name='group'),
    path('friend/<int:pk>', views.friend, name='friend'),
    path('channel/<int:pk>/', views.channel, name='channel'),
    path('edit_group_message/<int:pk>/<int:id>/', views.edit_group_message, name='edit_gp_message'),
    path('edit_channel_message/<int:pk>/<int:id>/', views.edit_channel_message, name='edit_ch_message'),
    path('edit_friend_message/<int:pk>/<int:id>/', views.edit_friend_message, name='edit_fr_message'),
    path('user_profile/', views.user_profile, name="user_profile"),
    path('group_profile/<int:pk>/', views.group_profile, name="group_profile"),
    path('channel_profile/', views.channel_profile, name="channel_profile"),
]