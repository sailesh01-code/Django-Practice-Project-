from django.urls import path
from employees import views
urlpatterns = [
    path('employee-form/',views.employee_view,name='form'),
   
]
