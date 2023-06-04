"""
ASGI config for VideoChatProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VideoChatProject.settings")

"""Creating a routing configuration for Channels. A Channels routing 
configuration is an ASGI application that is similar to a Django URLconf, 
in that it tells Channels what code to run when an HTTP request is 
received by the Channels server."""

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        # Just HTTP for now. (We can add other protocols later.)
    }
)
