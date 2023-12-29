# todolist/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'tags', 'status']

# class SignUp(forms.ModelForm):
#     class Meta:
#         model = signup
#         fields = ['username', 'fname', 'lname', 'email', 'phone', 'pass1', 'pass2']