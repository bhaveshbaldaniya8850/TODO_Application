from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from todo_app.models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TodoAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token, _ = Token.objects.get_or_create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        self.todo_data = {'title': 'Test Todo', 'description': 'Test description'}
        self.todo = Task.objects.create(**self.todo_data)
        
    def test_get_todo_list(self):
        url = reverse('todo-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_todo(self):
        url = reverse('todo-list-create')
        response = self.client.post(url, data=self.todo_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_todo_detail(self):
        url = reverse('todo-detail', args=[self.todo.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.todo_data['title'])


    def test_update_todo(self):
        updated_data = {'title': 'Updated Todo', 'description': 'Updated description'}
        url = reverse('task-detail', args=[self.todo.id])
        response = self.client.put(url, data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Todo')


    def test_delete_todo(self):
        url = reverse('todo-detail', args=[self.todo.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)