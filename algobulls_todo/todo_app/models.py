from django.db import models

# Create your models here.
# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     complete = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
    
    
#     def __str__(self):
#         return self.title

class Task(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(max_length=1000, verbose_name='Description')
    due_date = models.DateField(blank=True, null=True, verbose_name='Due Date')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Tags')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN', verbose_name='Status')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Tag Name')

    def __str__(self):
        return self.name
