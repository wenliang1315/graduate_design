# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-05-22 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoweliang', '0003_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewsid', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoweliang.House')),
            ],
        ),
    ]
