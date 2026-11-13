from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskUpdateViewTests(TestCase):
	def test_update_changes_existing_task_without_creating_duplicate(self):
		task = Task.objects.create(
			title='Prepare Django Notes',
			description='Complete the Django Forms chapter',
		)

		response = self.client.post(
			reverse('task-update', args=[task.id]),
			{
				'title': task.title,
				'description': 'Complete the Django Forms and ModelForm chapters',
			},
		)

		self.assertRedirects(response, reverse('task-list'))
		self.assertEqual(Task.objects.count(), 1)
		task.refresh_from_db()
		self.assertEqual(task.description, 'Complete the Django Forms and ModelForm chapters')


class TaskStatusViewTests(TestCase):
	def test_complete_marks_pending_task_as_completed(self):
		task = Task.objects.create(
			title='Prepare Django Assignment',
			description='Complete the ModelForm exercises',
		)

		response = self.client.post(reverse('task-complete', args=[task.id]))

		self.assertRedirects(response, reverse('task-list'))
		task.refresh_from_db()
		self.assertTrue(task.completed)

	def test_undo_marks_completed_task_as_pending(self):
		task = Task.objects.create(
			title='Prepare Django Assignment',
			description='Complete the ModelForm exercises',
			completed=True,
		)

		response = self.client.post(reverse('task-undo', args=[task.id]))

		self.assertRedirects(response, reverse('task-list'))
		task.refresh_from_db()
		self.assertFalse(task.completed)

	def test_get_does_not_change_task_status(self):
		task = Task.objects.create(
			title='Prepare Django Assignment',
			description='Complete the ModelForm exercises',
		)

		self.client.get(reverse('task-complete', args=[task.id]))

		task.refresh_from_db()
		self.assertFalse(task.completed)
