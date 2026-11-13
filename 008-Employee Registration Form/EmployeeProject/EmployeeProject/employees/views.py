from django.shortcuts import redirect, render

from .forms import EmployeeForm



# def employee_form_view(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         print(request.POST)
#     else:
#         form = EmployeeForm()
#     return render(request, 'employees/employee-form.html', {'form': form})


def employee_form_view(request):
	initial = {
		'name': 'Ram',
		'department': 'development',
		'salary': 45000,
		'email': 'Ram@gmail.com',
	}

	if request.method == 'POST':
		form = EmployeeForm(request.POST, request.FILES)
		if form.is_valid():
			resumes = request.FILES.getlist('resume')
			for resume in resumes:
				print(resume.name)
			return redirect('employee-success')
	else:
		form = EmployeeForm(initial=initial)

	return render(request, 'employees/employee-form.html', {'form': form})


def success_view(request):
	return render(request, 'employees/success.html')