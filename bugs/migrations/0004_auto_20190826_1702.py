# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-26 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0003_auto_20190731_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('todo', 'To do'), ('doing', 'Doing'), ('done', 'Done')], default='todo', max_length=5),
        ),
        migrations.AddField(
            model_name='bugs',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]