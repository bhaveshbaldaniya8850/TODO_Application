from django.shortcuts import render
from rest_framework import generics
from todo_app.models import Task
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics, authentication, permissions
from .serializers import TodoSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    #  Uncomment while undergoing the integrstion test
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer

# #example
@api_view(['GET'])
def getdata(request):
    dummy = {'Message' : 'Pass the api with appropriate value', 'Action':'Retry'}
    return Response(dummy)