# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toutiaoio', '0002_auto_20160718_2209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toutiaoitem',
            old_name='commend',
            new_name='comment',
        ),
    ]
