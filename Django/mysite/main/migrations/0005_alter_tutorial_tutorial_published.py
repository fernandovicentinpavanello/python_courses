# Generated by Django 4.0.4 on 2022-06-09 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_tutorial_tutorial_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 22, 16, 5, 146731), verbose_name='date published'),
        ),
    ]
