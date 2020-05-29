# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-06 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0004_auto_20200403_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll', models.CharField(max_length=30, unique=True)),
                ('sname', models.CharField(max_length=64)),
                ('img', models.ImageField(upload_to='pics')),
                ('sclass', models.CharField(max_length=64)),
                ('saddr', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('fatherName', models.CharField(max_length=100)),
                ('motherName', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('enrollDate', models.DateField()),
                ('sid', models.CharField(max_length=30, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=30)),
            ],
        ),
    ]