# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 15:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('synaptogram', '0002_auto_20170614_1751'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]