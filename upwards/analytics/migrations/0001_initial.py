# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-12 20:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algo360',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('imei', models.CharField(blank=True, editable=False, max_length=16, validators=[django.core.validators.RegexValidator(message='Data must be entered in Digits only.', regex='[0-9]+')])),
                ('monthly_average_balance_lifetime', models.CharField(blank=True, max_length=100)),
                ('monthly_average_balance_12', models.CharField(blank=True, max_length=100)),
                ('monthly_average_balance_6', models.CharField(blank=True, max_length=100)),
                ('monthly_average_balance_3', models.CharField(blank=True, max_length=100)),
                ('monthly_average_balance_1', models.CharField(blank=True, max_length=100)),
                ('number_of_cheque_bounce_1', models.CharField(blank=True, max_length=100)),
                ('number_of_cheque_bounce_3', models.CharField(blank=True, max_length=100)),
                ('is_credit_card_overlimited', models.CharField(default=True, max_length=100)),
                ('credit_card_last_payment_due', models.CharField(blank=True, max_length=100)),
                ('salary', models.CharField(blank=True, max_length=100)),
                ('algo360_data', models.TextField(blank=True, editable=False)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
            options={
                'db_table': 'analytics_algo360',
            },
        ),
        migrations.CreateModel(
            name='DataLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('log_type', models.CharField(choices=[('Call', 'Call'), ('SMS', 'SMS'), ('Data Usage', 'Data Usage')], default='SMS', max_length=50)),
                ('log_data', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
            options={
                'db_table': 'data_log',
            },
        ),
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('data_type', models.CharField(choices=[('Call', 'Call'), ('SMS', 'SMS'), ('Internet', 'Internet')], default='Call', max_length=50)),
                ('status', models.CharField(choices=[('Incomming', 'Incomming'), ('Outgoing', 'Outgoing'), ('Missed', 'Missed')], default='Incomming', max_length=50)),
                ('attribute', models.CharField(choices=[('Count', 'Count'), ('Duration', 'Duration'), ('Ratio', 'Ratio')], default='Count', max_length=50)),
                ('value', models.DecimalField(decimal_places=4, max_digits=10)),
                ('weekday_type', models.CharField(choices=[('Weekday', 'Weekday'), ('Weekend', 'Weekend')], default='Weekday', max_length=50)),
                ('day_hour_type', models.CharField(choices=[('Morning', 'Morning'), ('Office Hours', 'Office Hours'), ('Evening', 'Evening'), ('Late Night', 'Late Night'), ('All', 'All')], default='All', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
