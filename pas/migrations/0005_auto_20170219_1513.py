# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-19 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0004_auto_20170219_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='current_diet',
            field=models.FloatField(null=True),
        ),
    ]
