# Generated by Django 4.0 on 2022-01-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_userprofile_activation_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='server_board',
            name='reaction_count_in_post',
            field=models.CharField(default=0, max_length=100, null=True, verbose_name='reaction_count_in_post'),
        ),
    ]