from django.urls import path
from .import views

urlpatterns = [
    # Authentications
    path('sign-up/', views.sign_up, name="sign-up"),
    path('sign-in/', views.log_in, name='log-in'),
    path('logout/', views.log_out, name='logout'),
    # Home page
    path('', views.home, name='home'),
    # Main pages
    path('friend/<int:pk>', views.friend, name='friend'),
    # Editting pages
    path('edit_friend_message/<int:pk>/', views.edit_friend_message, name='edit_fr_message'),
    # Deleting pages
    path('delete_friend_message/<int:pk>/', views.delete_friend_message, name='delete_fr_message'),
    # Profile pages
    path('user_profile/<int:pk>', views.user_profile, name="user_profile"),
    
    # Show shared media
    
    path('shared_fr_media/<int:pk>/', views.view_friend_media, name='shared_fr_media'),
]