# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-05-22 11:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoweliang', '0008_auto_20170522_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='name',
            new_name='namer',
        ),
    ]
