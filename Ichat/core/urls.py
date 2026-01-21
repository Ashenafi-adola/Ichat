from django.urls import path
from .import views

urlpatterns = [
    # Authentications
    path('sign-up/', views.sign_up, name="sign-up"),
    path('sign-in/', views.log_in, name='log-in'),
    path('logout/', views.log_out, name='logout'),
    # Home page
    path('', views.home, name='home'),
    # Creating pages
    path('create_group/', views.create_group, name='create_group'),
    path('create_channel/', views.create_channel, name='create_channel'),
    # Main pages
    path('group/<int:pk>/', views.group, name='group'),
    path('friend/<int:pk>', views.friend, name='friend'),
    path('channel/<int:pk>/', views.channel, name='channel'),
    # Editting pages
    path('edit_group_message/<int:pk>/', views.edit_group_message, name='edit_gp_message'),
    path('edit_channel_message/<int:pk>/', views.edit_channel_message, name='edit_ch_message'),
    path('edit_friend_message/<int:pk>/', views.edit_friend_message, name='edit_fr_message'),
    # Deleting pages
    path('delete_channel_message/<int:pk>/', views.delete_channel_message, name='delete_ch_message'),
    path('delete_group_message/<int:pk>/', views.delete_group_message, name='delete_gp_message'),
    path('delete_friend_message/<int:pk>/', views.delete_friend_message, name='delete_fr_message'),
    # Profile pages
    path('user_profile/<int:pk>', views.user_profile, name="user_profile"),
    path('group_profile/<int:pk>/', views.group_profile, name="group_profile"),
    path('channel_profile/<int:pk>/', views.channel_profile, name="channel_profile"),
    # Commenting
    path('comment/<int:pk>/', views.leave_comment, name='comment'),
]