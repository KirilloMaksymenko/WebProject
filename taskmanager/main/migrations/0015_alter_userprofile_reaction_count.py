# Generated by Django 4.0 on 2022-01-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_userprofile_avatar_userprofile_avatar_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='reaction_count',
            field=models.CharField(max_length=100, verbose_name='reaction_count'),
        ),
    ]