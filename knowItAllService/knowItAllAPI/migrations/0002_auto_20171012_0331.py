# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 03:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowItAllAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('userID', 'pollChoiceID')]),
        ),
    ]
