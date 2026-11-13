from django.urls import path
from . import views
urlpatterns = [
    path('', views.employee_view, name='employee_home'),
    path('form/', views.employee_view, name='form'),
    path('display/',views.get_all_records, name='display'),
]
