# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toutiaoio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toutiaoitem',
            name='commend',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='toutiaoitem',
            name='source',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toutiaoitem',
            name='subjectname',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toutiaoitem',
            name='subjecturl',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toutiaoitem',
            name='title',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toutiaoitem',
            name='url',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toutiaoitem',
            name='username',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toutiaoitem',
            name='userurl',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]