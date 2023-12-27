from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('index', index, name='index'),
    path('', task_list, name='task_list'),
    path('task_list', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('view/<int:task_id>/', view_task, name='view_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
