# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-16 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0005_feature_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='status',
            field=models.CharField(choices=[('todo', 'To do'), ('doing', 'Doing'), ('done', 'Done')], default='todo', max_length=5),
        ),
        migrations.AddField(
            model_name='feature',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
