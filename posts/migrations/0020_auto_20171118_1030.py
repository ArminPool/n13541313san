# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20171115_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(),
        ),
    ]
