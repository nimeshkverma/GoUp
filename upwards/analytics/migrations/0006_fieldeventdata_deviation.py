# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-27 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_fieldeventdata_screeneventdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldeventdata',
            name='deviation',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
