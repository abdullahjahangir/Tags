# Generated by Django 4.2.11 on 2024-03-06 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0003_todo_is_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='is_completed',
            new_name='checked',
        ),
    ]
