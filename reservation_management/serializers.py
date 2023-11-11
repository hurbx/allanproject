from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from reservation_management.models import Client, Hotel, HotelRoom, Tour


class SerializerClient(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class SerializerHotel(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class SerializerHotelRoom(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = '__all__'


class SerializerTour(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
