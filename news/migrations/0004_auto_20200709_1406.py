# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-09 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comment_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='username',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
    ]
