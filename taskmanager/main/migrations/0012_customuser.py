# Generated by Django 4.0 on 2022-01-08 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0011_task_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('date_create_user', models.DateTimeField(auto_now_add=True)),
                ('avatar_url', models.CharField(default='https://i.imgur.com/BoZwIXW.png', max_length=100, verbose_name='avatar_url')),
                ('about_me', models.TextField(max_length=200, verbose_name='about')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
