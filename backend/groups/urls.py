from django.urls import path
from .import views

urlpatterns = [
    # Creating pages
    path('create_group/', views.CreateGroup.as_view(), name='create_group'),
    # Main pages
    path('group/<int:pk>/', views.GroupView.as_view(), name='group'),
    # Editting pages
    path('edit_group_message/<int:pk>/', views.EditGroupMessage.as_view(), name='edit_gp_message'),
    # Deleting pages
    path('delete_group_message/<int:pk>/', views.delete_group_message, name='delete_gp_message'),
    path('delete_group/<int:pk>/', views.delete_group, name='delete_gp'),
    # Profile pages
    path('group_profile/<int:pk>/', views.group_profile, name="group_profile"),
    # Show shared media
    path('shared_gp_media/<int:pk>/', views.view_group_media, name='shared_gp_media'),
]