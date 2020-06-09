# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-19 20:13
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations
from apps.common.model_utils.improved_django_json_encoder import ImprovedDjangoJSONEncoder


class Migration(migrations.Migration):

    dependencies = [
        ('rawdb', '0006_remove_savedfilter_filter_sql'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savedfilter',
            old_name='created_by',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='savedfilter',
            name='filter_query',
        ),
        migrations.AddField(
            model_name='savedfilter',
            name='column_filters',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=ImprovedDjangoJSONEncoder, null=True),
        ),
    ]
