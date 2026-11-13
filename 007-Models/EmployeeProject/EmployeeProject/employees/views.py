# from urllib import request

# from django.shortcuts import render

# from EmployeeProject import employees

# # Create your views here.
# from .models import Employee
# def employee_view(request):
#  employees = Employee.objects.all()
#  return render(request,'employees/employees.html',{'employees':employees})

from django.shortcuts import render
from .models import Employee


def employee_view(request):
    employees = Employee.objects.all()
    return render(
        request,
        'employees/employees.html',
        {'employees': employees}
    )