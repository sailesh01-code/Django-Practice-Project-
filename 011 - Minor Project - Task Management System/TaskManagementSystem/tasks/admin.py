from django.contrib import admin

# Register your models here.
# from .models import Task
# admin.site.register(Task)

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'title', 'completed', 'created_at']
    list_filter = ['completed']
    search_fields = ['title']

    @admin.display(description='Sl. No.')
    def serial_number(self, obj):
        return obj.id