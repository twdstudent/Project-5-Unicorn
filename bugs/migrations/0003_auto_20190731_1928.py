# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-31 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0002_auto_20190730_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bugs',
            old_name='description',
            new_name='content',
        ),
    ]
