# Generated by Django 4.0 on 2022-01-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name_plural': 'Задача'},
        ),
        migrations.AddField(
            model_name='task',
            name='time_create',
            field=models.CharField(default=1, max_length=50, verbose_name='Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.TextField(max_length=1000, verbose_name='Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
