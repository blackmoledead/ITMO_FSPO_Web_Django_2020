# Generated by Django 3.0.7 on 2020-06-29 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_auto_20200629_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='user',
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
