from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import TaskForm
import requests, json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import date
import json
import requests

username = "admin"
password = "superuser@admin"

def task_list(request):
    # Make a GET request to your API endpoint to fetch todo items
    api_url = 'http://localhost:8000/api/todos/'   
    # response = requests.get(api_url)
    response = requests.get(api_url, auth=(username, password))
    print(response)

    if response.status_code == 200:
        tasks = response.json()
    else:
        tasks = []

    return render(request, 'todo_app/task_list.html', {'tasks': tasks})

# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'todo_app/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Validate the form and retrieve cleaned data
            cleaned_data = form.cleaned_data
            tags_list = list(cleaned_data['tags'].values())
            due_date = cleaned_data['due_date'].isoformat()

            # Make a POST request to create a new task through the API
            api_url = 'http://localhost:8000/api/todos/'   
            data = {
                'title': cleaned_data['title'],
                'description': cleaned_data['description'],
                'due_date': due_date,
                'tags': tags_list,
                'status': cleaned_data.get('status', 'OPEN'),
            }
            response = requests.post(api_url,auth=(username, password), json= data)

            if response.status_code == 201:
                # Task created successfully, redirect to the task list
                return redirect('task_list')
            else:
                # error Handling
                pass
    else:
        form = TaskForm()

    return render(request, 'todo_app/task_form.html', {'form': form})


# def create_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()

#     return render(request, 'todo_app/task_form.html', {'form': form})

def update_task(request, task_id):
    # Get the task from the API
    api_url = f'http://localhost:8000/api/todos/{task_id}/'   
    response = requests.get(api_url,auth=(username, password))

    if response.status_code == 200:
        task_data = response.json()
    else:
        # error Handling
        task_data = {}

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Validate the form and retrieve cleaned data
            cleaned_data = form.cleaned_data

            # Convert queryset to a list of dictionaries
            tags_list = list(cleaned_data['tags'].values())
            due_date = cleaned_data['due_date'].isoformat()
            
            # Make a PUT request to update the task through the API
            update_data = {
                'title': cleaned_data['title'],
                'description': cleaned_data['description'],
                'due_date': due_date,
                'tags': tags_list,
                'status': cleaned_data.get('status', 'OPEN'),
            }
            update_response = requests.put(api_url,auth=(username, password), json=update_data)

            if update_response.status_code == 200:
                # Task updated successfully, redirect to the task list
                return redirect('task_list')
            else:
                # error Handling
                pass
    else:
        form = TaskForm(initial=task_data)

    return render(request, 'todo_app/task_form.html', {'form': form})

# def update_task(request, task_id):
#     task = Task.objects.get(pk=task_id)

#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm(instance=task)

#     return render(request, 'todo_app/task_form.html', {'form': form})


def view_task(request, task_id):
    # Make a GET request to fetch task details from the API
    api_url = f'http://localhost:8000/api/todos/{task_id}/'   
    response = requests.get(api_url,auth=(username, password))

    if response.status_code == 200:
        task = response.json()
    else:
        # error Handling
        task = {}

    # Render the task_detail.html template with the task data
    return render(request, 'todo_app/task_detail.html', {'task': task})


# def view_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#     return render(request, 'todo_app/task_detail.html', {'task': task})


def delete_task(request, task_id):
    # Make a GET request to fetch task details from the API
    api_url = f'http://localhost:8000/api/todos/{task_id}/'  # Replace with your actual API URL
    response = requests.get(api_url,auth=(username, password))

    if response.status_code == 200:
        task_data = response.json()
    else:
        # error Handling
        task_data = {}

    delete_response = requests.delete(api_url,auth=(username, password))

    if delete_response.status_code == 204:
        # Task deleted successfully, redirect to the task list
        return redirect('task_list')
    else:
        # error Handling
        pass

    return render(request, 'todo_app/task_list.html', {'task': task_data})

class PublicApiView(APIView):
    """
    An example of a public API view that doesn't require authentication.
    """
    def get(self, request):
        return Response({"message": "This is a public API."})


class PrivateApiView(APIView):
    """
    An example of a private API view that requires Basic Authentication.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}! This is a private API."})


class AnotherPrivateApiView(APIView):
    """
    Another example of a private API view with Basic Authentication.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Welcome, {request.user.username}! This is another private API."})