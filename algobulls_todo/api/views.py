from django.shortcuts import render
from rest_framework import generics
from todo_app.models import Task
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer

# #example
@api_view(['GET'])
def getdata(request):
    dummy = {'Message' : 'Pass the api with appropriate value', 'Action':'Retry'}
    return Response(dummy)