# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-01 12:10
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
from apps.common.model_utils.improved_django_json_encoder import ImprovedDjangoJSONEncoder


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document', '0055_auto_20180730_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalFieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('type_id', models.CharField(max_length=36)),
                ('field_id', models.CharField(max_length=36)),
                ('value', django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=ImprovedDjangoJSONEncoder, null=True)),
                ('sentence_text', models.TextField()),
                ('extraction_hint', models.CharField(blank=True, choices=[('TAKE_FIRST', 'TAKE_FIRST'), ('TAKE_SECOND', 'TAKE_SECOND'), ('TAKE_LAST', 'TAKE_LAST'), ('TAKE_MIN', 'TAKE_MIN'), ('TAKE_MAX', 'TAKE_MAX'), ('ORDINAL_EXTRACTION_HINTS', 'ORDINAL_EXTRACTION_HINTS')], db_index=True, default='TAKE_FIRST', max_length=30, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_externalfieldvalue_set', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_externalfieldvalue_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
