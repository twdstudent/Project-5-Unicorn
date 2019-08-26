# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-26 18:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feature', '0004_auto_20190731_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='feature', to=settings.AUTH_USER_MODEL),
        ),
    ]