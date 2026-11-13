from django.shortcuts import render,HttpResponse
from .forms import EmployeeForm
from .models import Employee

def employee_view(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST) # captured form data
        if form.is_valid():
            form.save() # save the data into the database table
        return render(request,'Employees/success.html')
    else:
        form=EmployeeForm() # empty form object creation
        context={
            'form':form,
        }
        return render(request,'Employees/form.html',context)

