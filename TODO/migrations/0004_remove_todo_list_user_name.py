# Generated by Django 4.2.1 on 2023-07-27 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0003_alter_todo_list_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo_list',
            name='user_name',
        ),
    ]