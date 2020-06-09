# Generated by Django 2.2.10 on 2020-03-03 08:57

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
from apps.common.model_utils.improved_django_json_encoder import ImprovedDjangoJSONEncoder


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0185_auto_20200219_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentFieldMultilineRegexDetector',
            fields=[
                ('document_field', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='document.DocumentField')),
                ('csv_content', models.TextField(blank=True, help_text='CSV structure where:\n    - the first column is the detected value,\n    - the second column is the regular expression,\n    - separators are semicolon, other semicolon are escaped with \\', null=True)),
                ('csv_checksum', models.CharField(blank=True, db_index=True, help_text='The field is used for caching regular expressions between\n                                     parsing tasks. Should be rewritten upon changing csv_content.', max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='documentfield',
            name='code',
            field=models.CharField(db_index=True, help_text='Field codes must be lowercase, should start with \na Latin letter, and contain only Latin letters, digits, underscores. Field codes must be unique to every Document Type.', max_length=50),
        ),
        migrations.AlterField(
            model_name='documentfield',
            name='default_value',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=ImprovedDjangoJSONEncoder, help_text='When populated, this \n    default value is displayed in the user interface’s annotator sidebar for the associated field. If not populated, the\n     Field Value remains empty by default. Please wrap entries with quotes, example: “landlord”. This is only applicable\n      to Choice and Multichoice fields.', null=True),
        ),
        migrations.AlterField(
            model_name='documentfield',
            name='detect_limit_count',
            field=models.IntegerField(db_index=True, default=0, help_text='Specify the maximum \nrange for a bounded search. Field detection begins at the top of the document and continues until this Nth \n"Detect limit unit" element.'),
        ),
        migrations.AlterField(
            model_name='documentfield',
            name='detect_limit_unit',
            field=models.CharField(choices=[('NONE', 'No Limit'), ('UNIT', 'Limit to N documents units'), ('SENTENCE', 'Limit to N sentences'), ('PARAGRAPH', 'Limit to N paragraphs'), ('PAGE', 'Limit to N pages'), ('CHAR', 'Limit to N characters')], default='NONE', help_text='Users may limit Document Field searches by bounding the detection \nrange. Specify the type of element (a “step size”) for a bounded search. When specified, a Document Field Detector will \nonly search from the beginning of the document until it reaches the specified Nth element. Note: Cannot be used with \nthe Field Value Detection Strategy called “apply regexp field detectors to depends-on field values”.', max_length=10),
        ),
        migrations.AlterField(
            model_name='documentfield',
            name='value_detection_strategy',
            field=models.CharField(choices=[('disabled', 'Field detection disabled'), ('use_regexps_only', 'No ML. Use regexp field detectors.'), ('regexp_table', 'Use regexp pattern: value collection.'), ('use_formula_only', 'No ML. Use formula only.'), ('regexps_and_text_based_ml', 'Start with regexps, switch to text-based ML when possible.'), ('text_based_ml_only', 'Use pre-trained text-based ML only.'), ('formula_and_fields_based_ml', 'Start with formula, switch to fields-based ML when possible.'), ('fields_based_ml_only', 'Use pre-trained field-based ML only.'), ('fields_based_prob_ml_only', 'Use pre-trained field-based ML with "Unsure" category.'), ('python_coded_field', 'Use python class for value detection.'), ('field_based_regexps', 'Apply regexp field detectors to depends-on field values'), ('mlflow_model', 'Use pre-trained mlflow model to find matching text units.')], default='use_regexps_only', max_length=50),
        ),
        migrations.AlterField(
            model_name='documentfield',
            name='value_regexp',
            field=models.TextField(blank=True, help_text='This regular expression is run on the sentence \n    found by a Field Detector and extracts a specific string value from a Text Unit. The first matching group is used if\n     the regular expression returns multiple matching groups. This is only applicable to string fields.', null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='definition_words',
            field=models.TextField(blank=True, help_text='Enter words or phrases, each on a new line, that must be present \nin the Text Unit. These words must be in the Definitions List. If ContraxSuite fails to recognize these words as \ndefinitions, then the Field Detector skips and moves to the next Text Unit. If there are Include regexps, then the \nField Detector checks against those requirements. The Field Detector marks the entire Text Unit as a match. Note that \nthe Field Detector checks for definition words after filtering using the Exclude regexps.', null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='detected_value',
            field=models.CharField(blank=True, help_text='The string value written here \nwill be assigned to the field if the Field Detector positively matches a Text Unit. This is only applicable to Choice, \nMultichoice, and String fields, as their respective Field Detectors do not extract and display values from the source \ntext.', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='exclude_regexps',
            field=models.TextField(blank=True, help_text='Enter regular expressions, each on a new line, to exclude sentences \nfrom field detection. If any portion of a given Text Unit’s text matches the pattern described in one of the Exclude \nregexps, then the Field Detector skips and moves to the next Text Unit. Note that Exclude regexps are checked before \nboth definition words and Include regexps.', null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='extraction_hint',
            field=models.CharField(blank=True, choices=[('TAKE_FIRST', 'TAKE_FIRST'), ('TAKE_SECOND', 'TAKE_SECOND'), ('TAKE_LAST', 'TAKE_LAST'), ('TAKE_MIN', 'TAKE_MIN'), ('TAKE_MAX', 'TAKE_MAX')], db_index=True, default='TAKE_FIRST', help_text='Provide additional instruction on which \nspecific values should be prioritized for extraction, when multiple values of the same type \n(e.g., Company, Person, Geography) are found within the relevant detected Text Unit.', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='include_regexps',
            field=models.TextField(blank=True, help_text='Enter regular expressions, each on a new \nline, for finding a text pattern. The Field Detector attempts to match each of these regular expressions within a given \nText Unit. Avoid using “.*” and similar unlimited multipliers, as they can crash or slow ContraxSuite. Use bounded \nmultipliers for variable length matching, like “.{0,100}” or similar. Note that Include regexps are checked after both \nExclude regexps and Definition words.', null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='regexps_pre_process_lower',
            field=models.BooleanField(default=True, help_text='Convert a sentence or a paragraph’s characters to \nlowercase prior to running regular expressions for field detection.'),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='text_part',
            field=models.CharField(choices=[('FULL', 'Whole text'), ('BEFORE_REGEXP', 'Before matching substring'), ('AFTER_REGEXP', 'After matching substring'), ('INSIDE_REGEXP', 'Inside matching substring')], db_index=True, default='FULL', help_text='Defines which part of the matched Text Unit \nshould be passed to the extraction function. Example: In the string "2019-01-23 is the start date and 2019-01-24 is the \nend date," if text part = "Before matching substring" and Include regexp is "is.{0,100}start" then "2019-01-23" will be \nparsed correctly as the start date.', max_length=30),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='code',
            field=models.CharField(db_index=True, help_text='Field codes must be lowercase, should start with a Latin letter, and contain \nonly Latin letters, digits, and underscores.', max_length=50, unique=True),
        ),
    ]
