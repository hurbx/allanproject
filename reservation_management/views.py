from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from reservation_management.models import Client
from reservation_management.serializers import SerializerClient


# Create your views here.
def index(request):
    return render(request, 'index.html')


class ClientView(APIView):
    def get(self, request):
        clients = Client.client.all()
        serializer = SerializerClient(clients, many=True)
        return Response(serializer.data)
