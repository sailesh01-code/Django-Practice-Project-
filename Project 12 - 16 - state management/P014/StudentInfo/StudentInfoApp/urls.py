from django.urls import path
from . import views
urlpatterns = [
    path('education_info/',views.education_form_view,name='education_info'),
    path('personal_info/',views.personal_form_view,name='personal_info'),
    path('extra_info/',views.extra_cur_form_view,name='extra_cur_info'),
    path('data/',views.data_view,name='data'),
    path('all_records/',views.all_records_view,name='all_records'),
]