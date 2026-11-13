from django.urls import path
from students import views
urlpatterns = [
    path('home/', views.home_view),
]