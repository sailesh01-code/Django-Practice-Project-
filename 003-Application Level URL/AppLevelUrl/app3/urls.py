from django.urls import path
from app3 import views

urlpatterns = [
    path('btech/',views.btech_view),
    path('mca/',views.mca_view),
    path('mba/',views.mba_view),
    path('mtech/',views.mtech_view),

]
