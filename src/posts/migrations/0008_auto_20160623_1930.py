# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20160623_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(max_length=120, null=True),
        ),
    ]