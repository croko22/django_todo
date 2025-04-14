from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle-completed/<int:task_id>/', views.toggle_completed, name='toggle_completed'),
    path('save/', views.save_task, name='save_task'),
]