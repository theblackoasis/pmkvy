# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170319_1917'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login_details',
        ),
    ]
