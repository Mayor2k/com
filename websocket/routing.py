from django.urls import path
from .consumers import OrderConsumer


websocket_urlpatterns = [
    path("orders/", OrderConsumer.as_asgi()),
]