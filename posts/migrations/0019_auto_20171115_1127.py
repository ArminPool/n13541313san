# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 07:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20171115_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='writer',
            new_name='author',
        ),
    ]
