# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20171029_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='path_to_file',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Record'),
        ),
    ]