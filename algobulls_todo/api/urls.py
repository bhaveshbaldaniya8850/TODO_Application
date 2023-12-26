# api/urls.py
from django.urls import path
from . import views
from .views import TodoListCreateView, TodoDetailView

urlpatterns = [
    path('',views.getdata),
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]
