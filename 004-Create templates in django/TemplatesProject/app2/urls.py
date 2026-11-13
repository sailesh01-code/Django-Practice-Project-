from django.urls import path # type: ignore[import-not-found]
from app2 import views
urlpatterns = [
    path('puri/', views.puri_view),
    path('bbsr/',views.bbsr_view),
]
