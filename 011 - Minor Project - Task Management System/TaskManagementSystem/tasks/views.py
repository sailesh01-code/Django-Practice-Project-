from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task

def home(request):
	return render(request, "tasks/home.html")

def dashboard(request):
	total_tasks = Task.objects.count()
	completed_tasks = Task.objects.filter(completed=True).count()
	pending_tasks = Task.objects.filter(completed=False).count()
	recent_tasks = Task.objects.order_by('-created_at')[:5]
	completion_percentage = 0
	if total_tasks:
		completion_percentage = round((completed_tasks / total_tasks) * 100)
	return render(request, 'tasks/dashboard.html', {
		'total_tasks': total_tasks,
		'completed_tasks': completed_tasks,
		'pending_tasks': pending_tasks,
		'completion_percentage': completion_percentage,
		'recent_tasks': recent_tasks,
	})

def task_list(request):
	
	# tasks = Task.objects.all().order_by('-created_at')
	search = request.GET.get('search', '')
	status = request.GET.get('status', 'all')
	tasks = Task.objects.all().order_by('-created_at')

	if search:
		tasks = tasks.filter(title__icontains=search)

	if status == 'pending':
		tasks = tasks.filter(completed=False)
	elif status == 'completed':
		tasks = tasks.filter(completed=True)

	return render(request, 'tasks/task-list.html', {
		'tasks': tasks,
		'search': search,
		'status': status,
		'total_tasks': tasks.count(),
		'completed_tasks': tasks.filter(completed=True).count(),
		'pending_tasks': tasks.filter(completed=False).count(),
	})

def task_detail(request, task_id):
	task = get_object_or_404(Task, id=task_id)
	return render(request, 'tasks/task-detail.html', {'task': task})

def task_create(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			# Old code:
			# return redirect('task-list')
			messages.success(request, 'Task added successfully.')
			return redirect('task-list')
	else:
		form = TaskForm()
	return render(request, 'tasks/task-form.html', {'form': form})

def task_update(request, task_id):
	task = get_object_or_404(Task, id=task_id)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			# Old code:
			# return redirect('task-list')
			messages.success(request, 'Task updated successfully.')
			return redirect('task-list')
	else:
		form = TaskForm(instance=task)
	return render(request, 'tasks/task-form.html', {'form': form, 'task': task})

def task_delete(request, task_id):
	task = get_object_or_404(Task, id=task_id)
	if request.method == 'POST':
		task.delete()
		# Old code:
		# return redirect('task-list')
		messages.success(request, 'Task deleted successfully.')
		return redirect('task-list')
	return render(request, 'tasks/task-confirm-delete.html', {'task': task})

def task_complete(request, task_id):
	task = get_object_or_404(Task, id=task_id)
	if request.method == 'POST':
		task.completed = True
		task.save()
		# Old code:
		# return redirect('task-list')
		messages.success(request, 'Task marked as completed.')
		return redirect('task-list')
	return redirect('task-list')

def task_undo(request, task_id):
	task = get_object_or_404(Task, id=task_id)
	if request.method == 'POST':
		task.completed = False
		task.save()
		
		# return redirect('task-list')
		messages.info(request, 'Task moved back to pending.')
		return redirect('task-list')
	return redirect('task-list')

def pending_tasks(request):
	tasks = Task.objects.filter(completed=False).order_by('-created_at')
	return render(request, 'tasks/task-list.html', {'tasks': tasks})

def completed_tasks(request):
	tasks = Task.objects.filter(completed=True).order_by('-created_at')
	return render(request, 'tasks/task-list.html', {'tasks': tasks})
