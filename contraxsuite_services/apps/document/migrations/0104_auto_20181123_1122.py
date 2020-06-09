# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-23 11:22
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
from apps.common.model_utils.improved_django_json_encoder import ImprovedDjangoJSONEncoder


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0103_documentfield_classifier_init_script'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentfield',
            name='stop_words',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=ImprovedDjangoJSONEncoder, null=True),
        ),
        migrations.AddField(
            model_name='documentfielddetector',
            name='category',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='documentfield',
            name='type',
            field=models.CharField(choices=[('address', 'Address'), ('amount', 'Amount'), ('choice', 'Choice'), ('company', 'Company'), ('date', 'Date: Non-recurring Events'), ('date_recurring', 'Date: Recurring Events'), ('duration', 'Duration'), ('float', 'Floating Point Number'), ('geography', 'Geography'), ('int', 'Integer Number'), ('money', 'Money'), ('multi_choice', 'Multi Choice'), ('person', 'Person'), ('related_info', 'Related Info'), ('string', 'String (vectorizer uses words as tokens)'), ('string_no_word_wrap', 'String (vectorizer uses whole value as a token)'), ('text', 'Long Text')], db_index=True, default='string', max_length=30),
        ),
    ]
