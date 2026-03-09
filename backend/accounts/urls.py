from django.urls import path
from .import views
from . views import (RegisterView,
                    Home,
                    Friend, 
                    EditFriendMessage, 
                    DeleteFriendMessage,
                    UserProfile,ViewSharedMedia,
                    MessageApiView
                    )
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Authentications
    path('sign-up/', RegisterView.as_view(), name="sign-up"),
    path('sign-in/', LoginView.as_view(template_name = 'accounts/sign_in.html'), name='log-in'),
    path('logout/', views.log_out, name='logout'),
    # Home page
    path('', Home.as_view(), name='home'),
    # Main pages
    path('friend/<int:pk>/', Friend.as_view(), name='friend'),
    # Editting pages
    path('edit_friend_message/<int:pk>/', EditFriendMessage.as_view(), name='edit_fr_message'),
    # Deleting pages
    path('delete_friend_message/<int:pk>/', DeleteFriendMessage.as_view(), name='delete_fr_message'),
    # Profile pages
    path('user_profile/<int:pk>', UserProfile.as_view(), name="user_profile"),
    
    # Show shared media
    path('shared_fr_media/<int:pk>/', ViewSharedMedia.as_view(), name='shared_fr_media'),
]