from django.urls import path
from app1 import views
urlpatterns = [
    path('puri/',views.puri_view),
    path('bbsr/',views.bbsr_view),
    path('cuttack/',views.cuttack_view),
]
