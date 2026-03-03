from django.urls import path
from .import views
from . views import RegisterView, Home
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Authentications
    path('sign-up/', RegisterView.as_view(), name="sign-up"),
    path('sign-in/', LoginView.as_view(template_name = 'accounts/sign_in.html'), name='log-in'),
    path('logout/', views.log_out, name='logout'),
    # Home page
    path('', Home.as_view(), name='home'),
    # Main pages
    path('friend/<str:friend_name>', views.friend, name='friend'),
    # Editting pages
    path('edit_friend_message/<int:pk>/', views.edit_friend_message, name='edit_fr_message'),
    # Deleting pages
    path('delete_friend_message/<int:pk>/', views.delete_friend_message, name='delete_fr_message'),
    # Profile pages
    path('user_profile/<int:pk>', views.user_profile, name="user_profile"),
    
    # Show shared media
    
    path('shared_fr_media/<int:pk>/', views.view_friend_media, name='shared_fr_media'),
]