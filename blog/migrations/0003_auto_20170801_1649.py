# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170729_0949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time']},
        ),
    ]
