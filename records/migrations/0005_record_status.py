# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-12 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20171112_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'Processing'), (3, 'Finished')], default=1, verbose_name='Status'),
        ),
    ]
