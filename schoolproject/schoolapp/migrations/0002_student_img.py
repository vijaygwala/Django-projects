# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-03-28 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]