# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0002_user_current_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='current_diet',
            field=models.CharField(default=100, max_length=200),
            preserve_default=False,
        ),
    ]
