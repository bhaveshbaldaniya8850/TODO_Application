# Generated by Django 5.0 on 2023-12-26 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_todo_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
