"""
ASGI config for chat_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import sys
sys.path.insert(1, '../chat_app')
from chat_app import routing

import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

application = ProtocolTypeRouter({'http': get_asgi_application(),
                                  "websocket": AuthMiddlewareStack(
                                      URLRouter(
                                          routing.websocket_urlpatterns
                                      )
                                  ),
                                  })
