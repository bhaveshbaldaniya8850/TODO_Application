from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import TaskForm

# Create your views here.
# def index(request):
#     tasks = Task.objects.all()
#     context = {'tasks' : tasks}
#     return render(request, 'todo_app/list.html', context)

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_app/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Change 'task_list' to your actual task list URL
    else:
        form = TaskForm()

    return render(request, 'todo_app/task_form.html', {'form': form})

def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Change 'task_list' to your actual task list URL
    else:
        form = TaskForm(instance=task)

    return render(request, 'todo_app/task_form.html', {'form': form})

def view_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo_app/task_detail.html', {'task': task})