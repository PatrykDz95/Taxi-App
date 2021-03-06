# taxi/routing.py

from django.urls import path  # new
from channels.auth import AuthMiddlewareStack  # new
from channels.routing import ProtocolTypeRouter, URLRouter  # changed

from trips.consumers import TaxiConsumer

# changed
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('taxi/', TaxiConsumer),
        ])
    )
})