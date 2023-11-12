from django.urls import path
from .views import ClientView, TourView

urlpatterns = [
    path('client_list/', ClientView.as_view()),
    path('tour_list', TourView.as_view()),
]