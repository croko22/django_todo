from django.urls import path
from .views import TaskListView, CreateTaskView, UpdateTaskView, DeleteTaskView, ToggleCompletedView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('update/<int:pk>/', UpdateTaskView.as_view(), name='update_task'),
    path('delete/<int:task_id>/', DeleteTaskView.as_view(), name='delete_task'),
    path('toggle-completed/<int:task_id>/', ToggleCompletedView.as_view(), name='toggle_completed'),
]
