# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-25 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20200625_0645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='accounts.UserProfile', verbose_name='Your username:'),
        ),
    ]
