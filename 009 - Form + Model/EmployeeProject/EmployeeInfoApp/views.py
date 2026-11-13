from django.shortcuts import render,HttpResponse
from .forms import EmployeeForm
from .models import Employee

def employee_view(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST) # captured form data
        if form.is_valid():
            employee = Employee.objects.create(**form.cleaned_data)
            context={
                'name': employee.name,
            }
            return render(request,'EmployeeInfoApp/success.html',context)
        return render(request,'EmployeeInfoApp/form.html',{'form': form})
    else:
        form=EmployeeForm() # empty form object creation
        context={
            'form':form,
        }
        return render(request,'EmployeeInfoApp/form.html',context)

def get_all_records(request):
    all_records=Employee.objects.all()
    context={
        'all_records':all_records,
    }
    return render(request,'EmployeeInfoApp/display.html',context)