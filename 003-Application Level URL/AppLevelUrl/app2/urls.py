from django.urls import path
from app2 import views

urlpatterns = [
    path('morning/',views.morning_view),
    path('evening/',views.evening_view),
]
