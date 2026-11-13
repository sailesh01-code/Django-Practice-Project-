from django.urls import path
from students import views
urlpatterns = [
# path('student/',views.student_view),
path('students/',views.students_view),
]