# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-05-19 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoweliang', '0002_auto_20170518_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('price', models.CharField(max_length=128)),
                ('area', models.CharField(max_length=128)),
                ('numofman', models.CharField(max_length=128)),
                ('bedsize', models.CharField(max_length=128)),
            ],
        ),
    ]
