from api.models import Order
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import (ObserverModelInstanceMixin, action)
from api.serializers import OrderSerializer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions

class OrderConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action()
    async def subscribe(self, **kwargs):
        await self.model_change.subscribe()

    @model_observer(Order)
    async def model_change(self, message, **kwargs):
        message["action"] = kwargs.get("action")
        await self.send_json(message)