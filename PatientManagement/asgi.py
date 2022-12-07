"""
ASGI config for PatientManagement project.

It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
# """

# import os
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# from django.urls import path
# from notifier.consumers import NoseyConsumer

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PatientManagement.settings')

# application = get_asgi_application()

# application = ProtocolTypeRouter({
#     "websocket": URLRouter([
#         path("notifications/", NoseyConsumer),
#     ])
# })

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PatientManagement.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

from notifier.consumers import NoseyConsumer

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket chat handler
    "websocket": 
            URLRouter([
                path("notifications/", NoseyConsumer.as_asgi())
            ])
})