from django.urls import re_path

from . import consumers

friend_urlpatterns = [
    re_path(r"ws/friend/(?P<friend_name>\w+)/$", consumers.CoreConsumer.as_asgi()),
]