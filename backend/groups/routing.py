from django.urls import re_path

from . import consumers

group_urlpatterns = [
    re_path(r"ws/group/(?P<group_name>\w+)/$", consumers.CoreConsumer.as_asgi()),
]