# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 22:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 8, 10, 22, 53, 32, 813543, tzinfo=utc)),
            preserve_default=False,
        ),
    ]