# Generated by Django 5.0.6 on 2024-06-05 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanaging', '0002_rename_дата_создания_task_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_date',
            new_name='due_date_2000_12_31',
        ),
    ]
