from django.urls import path
from .import views

urlpatterns = [
    path('sign-up/', views.sign_up, name="sign-up"),
    path('home/', views.home, name='home'),
    path('create_group/', views.create_group, name='create_group'),
    path('group/<int:pk>/', views.group, name='group'),
]