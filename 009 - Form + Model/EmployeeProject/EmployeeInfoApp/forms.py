from django import forms
#define your form class here
class EmployeeForm(forms.Form):
    name=forms.CharField()
    desg=forms.CharField()
    age=forms.IntegerField()
    sal=forms.FloatField()
    address=forms.CharField()
    