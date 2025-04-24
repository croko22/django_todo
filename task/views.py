from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.views import View
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'task_list.html', {'tasks': tasks})

class CreateTaskView(View):
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user 
            task.save()
        return redirect('task_list')

class UpdateTaskView(View):
    def post(self, request, pk):
        if request.POST.get('_method') != 'PUT':
            return redirect('task_list')

        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('task_list')
    
class DeleteTaskView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('task_list')

    def get(self, request, task_id):
        return HttpResponseNotAllowed(['POST'])

class ToggleCompletedView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()
        return redirect('task_list')
