from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import notes.routing

# web socket support
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            notes.routing.websocket_urlpatterns
        )
    )
})