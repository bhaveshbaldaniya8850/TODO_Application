from django.db import models

# Create your models here.


# class Task(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     due_date = models.DateField(blank=True, null=True)
#     tags = models.ManyToManyField('Tag', blank=True)
#     status = models.CharField(max_length=10, default='OPEN')

#     def __str__(self):
#         return self.title

# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name
