from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('tasks/',views.task_list,name='task-list'),
    path('tasks/create/', views.task_create, name='task-create'),
    path('tasks/<int:task_id>/',views.task_detail,name='task-detail'),
    path('tasks/<int:task_id>/edit/', views.task_update, name='task-update'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task-delete'),
    path('tasks/<int:task_id>/complete/', views.task_complete, name='task-complete'),
    path('tasks/<int:task_id>/undo/', views.task_undo, name='task-undo'),
    path('tasks/pending/', views.pending_tasks, name='pending-tasks'),
    path('tasks/completed/', views.completed_tasks, name='completed-tasks'),
]
