# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0009_auto_20171231_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='img',
            field=models.ImageField(upload_to='img'),
        ),
    ]
