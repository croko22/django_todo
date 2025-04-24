from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at', 'user')
    search_fields = ['title']
    list_filter = ['completed']
    ordering = ['-created_at']

