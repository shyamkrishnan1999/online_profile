# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-11 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='account',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='online_portal.TimeStampedModel')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('dob', models.DateTimeField()),
                ('blood', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
            bases=('online_portal.timestampedmodel',),
        ),
    ]
