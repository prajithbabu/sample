# Generated by Django 3.2.4 on 2021-06-17 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
