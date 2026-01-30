"""
ASGI config for Ichat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from accounts.routing import friend_urlpatterns
from groups.routing import group_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ichat.settings')

django_asgi_app = get_asgi_application()

all_websocket_patterns = friend_urlpatterns + group_urlpatterns

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    all_websocket_patterns
                    )
                )
        ),
})
