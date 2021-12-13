from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from .models import Order, menuItem
from .serializers import OrderSerializer, UserSerializer, MenuItemSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@authentication_classes([BasicAuthentication, TokenAuthentication,])
@permission_classes((permissions.IsAuthenticated,))
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):

        body = request.data

        if len(body) > 0:
            query = Order.objects.filter(**body)
            serializer = self.serializer_class(query, many=True,)
        else:
            serializer = self.serializer_class(self.queryset, many=True,)
        print(len(request.data))
        return Response(serializer.data)
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@authentication_classes([BasicAuthentication, TokenAuthentication,])
@permission_classes((permissions.IsAuthenticated,))
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@authentication_classes([BasicAuthentication, TokenAuthentication,])
@permission_classes((permissions.IsAuthenticated,))
class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = menuItem.objects.all()
    serializer_class = MenuItemSerializer

@authentication_classes([BasicAuthentication,])
@permission_classes((permissions.IsAuthenticated,))
class UserAuth(APIView):
    def get(self, request, format=None):
        try:
            token = Token.objects.get(user=request.user)
        except:
            token = Token.objects.create(user=request.user)

        return Response({"token" : token.key})
