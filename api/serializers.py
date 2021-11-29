from rest_framework import serializers
from .models import Order, menuItem
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Order
        fields = ['id','created', 'owner', 'title', 'order','status', 'table']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = menuItem
        fields = ['id','title', 'category', 'composition','note', 'price']

class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']