from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home_view,name='home'), 
    path('cart/',views.display_cart_view,name='cart')
]
