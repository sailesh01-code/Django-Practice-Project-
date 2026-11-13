from django.contrib import admin  # pyright: ignore[reportMissingModuleSource]
from django.urls import path  # pyright: ignore[reportMissingModuleSource]
from App1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('wish/',views.wish_view),
]
