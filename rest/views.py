from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, Item
from .serializers import OrderSerializer, ItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer