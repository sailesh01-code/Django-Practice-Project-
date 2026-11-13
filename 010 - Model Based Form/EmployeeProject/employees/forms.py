from django import forms
from .models import Employee

#define your form class here
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'desg', 'age', 'sal', 'address']
