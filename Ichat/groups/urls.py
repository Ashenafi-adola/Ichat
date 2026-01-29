from django.urls import path
from .import views

urlpatterns = [
    # Creating pages
    path('create_group/', views.create_group, name='create_group'),
    # Main pages
    path('group/<str:group_name>/', views.group, name='group'),
    # Editting pages
    path('edit_group_message/<int:pk>/', views.edit_group_message, name='edit_gp_message'),
    # Deleting pages
    path('delete_group_message/<int:pk>/', views.delete_group_message, name='delete_gp_message'),
    path('delete_group/<int:pk>/', views.delete_group, name='delete_gp'),
    # Profile pages
    path('group_profile/<int:pk>/', views.group_profile, name="group_profile"),
    # Show shared media
    path('shared_gp_media/<int:pk>/', views.view_group_media, name='shared_gp_media'),
]