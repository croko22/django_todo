from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseNotAllowed
from .models import Task

def task_list(request): 
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def save_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        title = request.POST.get('title')
        description = request.POST.get('description')

        if task_id:
            task = Task.objects.get(id=task_id)
            task.title = title
            task.description = description
            task.save()
            return redirect('task_list')
        else:
            Task.objects.create(title=title, description=description)
            return redirect('task_list')


def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('task_list')  
    else:
        return HttpResponseNotAllowed(['POST']) 
    
def toggle_completed(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()
    return redirect('task_list')