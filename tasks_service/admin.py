from django.contrib import admin
from .models import Task

#admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Custom admin for Task model to display important fields in the admin panel.
    """
    list_display = ('id','title', 'status', 'due_date', 'assigned_to', 'created_at',)
    search_fields = ('title', 'description')
    list_filter = ('status', 'due_date')
    ordering = ('due_date',)
