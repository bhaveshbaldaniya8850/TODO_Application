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
    path('public-api/', PublicApiView.as_view(), name='public_api'),
    path('private-api/', PrivateApiView.as_view(), name='private_api'),
    path('another-private-api/', AnotherPrivateApiView.as_view(), name='another_private_api'),

    # path("signup", views.handlesignup, name='handlesignup'),
    # path("login", views.handlelogin, name='login'),
    # path("logout", views.handlelogout, name='logout'),
    # path("notauthenticated", views.notauthenticated, name='notauthenticated'),
]
