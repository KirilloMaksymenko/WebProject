# Generated by Django 4.0 on 2022-01-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_options_task_time_create_alter_task_task_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_create',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
