# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0007_userus_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='img',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]