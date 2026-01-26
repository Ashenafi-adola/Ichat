from django.urls import path
from . import views

urlpatterns = [
    path('create_channel/', views.create_channel, name='create_channel'),
    # Main pages
    path('channel/<int:pk>/', views.channel, name='channel'),
    # Editting pages
    path('edit_channel_message/<int:pk>/', views.edit_channel_message, name='edit_ch_message'),
    # Deleting pages
    path('delete_channel_message/<int:pk>/', views.delete_channel_message, name='delete_ch_message'),
    path('delete_channel/<int:pk>/', views.delete_channel, name='delete_ch'),

    path('channel_profile/<int:pk>/', views.channel_profile, name="channel_profile"),
    # Commenting
    path('comment/<int:pk>/', views.leave_comment, name='comment'),
    path('edit_comment/<int:pk>/<int:id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),
    # Show shared media
    path('shared_ch_media/<int:pk>/', views.view_channel_media, name='shared_ch_media'),
]