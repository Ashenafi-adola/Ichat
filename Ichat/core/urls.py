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
    path('channel/<int:pk>/', views.channel, name='channel')
]