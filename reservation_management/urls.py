from django.urls import path
from .views import ClientView

urlpatterns = [
    path('client_list/', ClientView.as_view()),
]