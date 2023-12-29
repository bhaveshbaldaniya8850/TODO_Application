from django.test import TestCase
from todo_app.models import Task
from .serializers import TodoSerializer

class TodoModelTest(TestCase):
    def test_todo_creation(self):
        todo = Task.objects.create(title='Test Todo', description='Test description')
        self.assertEqual(todo.title, 'Test Todo')
        self.assertEqual(todo.description, 'Test description')

class TodoSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        valid_data = {'title': 'Test Todo', 'description': 'Test description'}
        serializer = TodoSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data(self):
        invalid_data = {'title': '', 'description': 'Test description'}
        serializer = TodoSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())