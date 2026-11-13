from django.shortcuts import render

# def student_view(request):
    # student = {
    #     'name': 'Surendra',
    #     'course': 'Full Stack Python',
    #     'city': 'Bhubaneswar'
    # }
    
    # student = {'name':'Rahul','course':'Django','city':'Cuttack'} 
    
    # student = {'name':'Priyanka','course':'Django REST Framework','city':'Puri','email':'priyanka@gmail.com'}
    # return render(request, 'students/student.html', {'student': student})
    ######################
    
def students_view(request):
#  students = ['Surendra','Rahul','Priyanka','Zini','Anjali']
#  students = ['Surendra','Rahul','Priyanka','Zini','Anjali','Smrti','Stalina','Salina']

#  students = [
# {
# 'name': 'Surendra',
# 'course': 'Python',
# 'city': 'Bhubaneswar'
# },
# {
# 'name': 'Rahul',
# 'course': 'Django',
# 'city': 'Cuttack'
# },
# {
# 'name': 'Priyanka',
# 'course': 'DRF',
# 'city': 'Puri'
# },
# {
# 'name': 'Zini',
# 'course': 'JavaScript',
# 'city': 'Bhubaneswar',
# },
# {
# 'name':'Jack',
# 'course':'React',
# 'city':'Rourkela',
# },
# ] 
 students = [
{
'name': 'Surendra',
'course': 'Python',
'city': 'Bhubaneswar',
'email': 'surendra@gmail.com'
},
{
'name': 'Rahul',
'course': 'Django',
'city': 'Cuttack',
'email': 'rahul@gmail.com'
},
{
'name': 'Priyanka',
'course': 'DRF',
'city': 'Puri',
'email': 'priyanka@gmail.com'
},
{
'name': 'Zini',
'course': 'JavaScript',
'city': 'Bhubaneswar',
'email': 'zini@gmail.com'
},
]
 return render(request,'students/students.html',{'students':students})
