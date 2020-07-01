# Generated by Django 3.0.7 on 2020-06-29 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20200629_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_seeker',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='id_employer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Employer'),
        ),
    ]
