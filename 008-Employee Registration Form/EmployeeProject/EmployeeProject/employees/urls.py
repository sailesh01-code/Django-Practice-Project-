from django.urls import path
from . import views

urlpatterns = [
    path('employee-form/', views.employee_form_view, name='employee_form'),
    path('success/', views.success_view, name='employee-success'),
]