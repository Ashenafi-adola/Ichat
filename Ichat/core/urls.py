from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_group/', views.create_group, name='create_group')
]