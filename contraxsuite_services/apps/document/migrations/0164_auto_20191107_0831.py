# Generated by Django 2.2.4 on 2019-11-07 08:31

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations, models

from apps.common.model_utils.improved_django_json_encoder import ImprovedDjangoJSONEncoder


class Migration(migrations.Migration):
    dependencies = [
        ('document', '0163_auto_20191101_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.TextField(null=True)),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='document.Document')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata',
                 django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=ImprovedDjangoJSONEncoder)),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='document.Document')),
            ],
        ),
    ]
