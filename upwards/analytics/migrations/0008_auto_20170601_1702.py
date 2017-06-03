# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-01 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0007_contactdata'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contactdata',
            unique_together=set([('customer', 'data_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='devicedata',
            unique_together=set([('customer', 'data_type', 'status', 'attribute', 'weekday_type', 'day_hour_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='fieldeventdata',
            unique_together=set([('customer', 'screen', 'field', 'mode')]),
        ),
        migrations.AlterUniqueTogether(
            name='screeneventdata',
            unique_together=set([('customer', 'screen', 'mode')]),
        ),
    ]
