from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_view, name='employee_view'),
    path('employees/', views.employee_view, name='employees_list'),
]