# Generated by Django 3.0.7 on 2020-06-30 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200630_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='user',
        ),
    ]
