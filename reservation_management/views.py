from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')
