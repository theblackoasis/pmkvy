# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20170320_0920'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login_details',
            new_name='AppUser',
        ),
    ]
