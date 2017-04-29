# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 16:55
from __future__ import unicode_literals

import countries_flavor.fields
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('code', countries_flavor.fields.CodeISOField(length=2, max_length=2, primary_key=True, regex='[A-Z]', serialize=False, validators=[django.core.validators.RegexValidator(regex='^[A-Z]{2}$')], verbose_name='code')),
                ('name', models.CharField(max_length=16, verbose_name='name')),
            ],
            options={
                'verbose_name': 'continent',
                'verbose_name_plural': 'continents',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cca2', countries_flavor.fields.CodeISOField(length=2, max_length=2, primary_key=True, regex='[A-Z]', serialize=False, validators=[django.core.validators.RegexValidator(regex='^[A-Z]{2}$')], verbose_name='code ISO 3166-1 alpha-2')),
                ('cca3', countries_flavor.fields.CodeISOField(length=3, max_length=3, regex='[A-Z]', validators=[django.core.validators.RegexValidator(regex='^[A-Z]{3}$')], verbose_name='code ISO 3166-1 alpha-3')),
                ('ccn3', countries_flavor.fields.CodeISOField(length=3, max_length=3, regex='\\d', validators=[django.core.validators.RegexValidator(regex='^\\d{3}$')], verbose_name='code ISO 3166-1 numeric')),
                ('cioc', countries_flavor.fields.CodeISOField(length=3, max_length=3, regex='[A-Z]', validators=[django.core.validators.RegexValidator(regex='^[A-Z]{3}$')], verbose_name='code International Olympic Committee')),
                ('location', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('region', models.CharField(max_length=64, verbose_name='region')),
                ('region_code', countries_flavor.fields.CodeISOField(blank=True, length=3, max_length=3, regex='\\d', validators=[django.core.validators.RegexValidator(regex='^\\d{3}$')], verbose_name='region code')),
                ('subregion', models.CharField(max_length=64, verbose_name='subregion')),
                ('subregion_code', countries_flavor.fields.CodeISOField(blank=True, length=3, max_length=3, regex='\\d', validators=[django.core.validators.RegexValidator(regex='^\\d{3}$')], verbose_name='subregion code')),
                ('world_region', countries_flavor.fields.CodeISOField(blank=True, length=4, max_length=4, regex='[A-Z]', validators=[django.core.validators.RegexValidator(regex='^[A-Z]{4}$')], verbose_name='world region code')),
                ('postal_code', models.NullBooleanField()),
                ('capital', models.CharField(max_length=128, verbose_name='capital')),
                ('independent', models.CharField(blank=True, max_length=64, verbose_name='independent')),
                ('landlocked', models.BooleanField(verbose_name='landlocked status')),
                ('demonym', models.CharField(max_length=64, verbose_name='name of residents')),
                ('area', models.PositiveIntegerField(null=True, verbose_name='land area in km')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('calling_codes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(regex='^\\d+$')]), size=None, verbose_name='calling codes')),
                ('international_prefix', models.CharField(blank=True, max_length=4, verbose_name='international prefix')),
                ('national_destination_code_lengths', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), null=True, size=None, verbose_name='national destination code lengths')),
                ('national_number_lengths', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), null=True, size=None, verbose_name='national number lengths')),
                ('national_prefix', models.CharField(blank=True, max_length=4, verbose_name='national prefix')),
                ('alt_spellings', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), size=None, verbose_name='alternative spellings')),
                ('tlds', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), size=None, verbose_name='country code top-level domains')),
                ('borders', models.ManyToManyField(blank=True, related_name='_country_borders_+', to='countries_flavor.Country', verbose_name='land borders')),
                ('continent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='countries_flavor.Continent', verbose_name='continent')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'ordering': ('cca2',),
            },
        ),
        migrations.CreateModel(
            name='CountryName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common', models.CharField(max_length=128, verbose_name='common name')),
                ('official', models.CharField(max_length=128, verbose_name='official name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='countries_flavor.Country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'country name',
                'verbose_name_plural': 'country names',
                'ordering': ('country', 'language'),
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('code', countries_flavor.fields.CodeISOField(length=3, max_length=3, primary_key=True, regex='[A-Z]', serialize=False, validators=[django.core.validators.RegexValidator(regex='^[A-Z]{3}$')], verbose_name='code ISO 4217')),
                ('numeric', countries_flavor.fields.CodeISOField(blank=True, length=3, max_length=3, regex='\\d', validators=[django.core.validators.RegexValidator(regex='^\\d{3}$')], verbose_name='code ISO 4217 numeric')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('full_name', models.CharField(blank=True, max_length=64, verbose_name='full name')),
                ('minor_unit', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('symbol', models.CharField(blank=True, max_length=4, verbose_name='symbol')),
                ('unicode_hex', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=8), null=True, size=None, verbose_name='unicode hex')),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=8, verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('alt_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), size=None, verbose_name='alternative names')),
                ('location', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('poly', django.contrib.gis.db.models.fields.PolygonField(null=True, srid=4326)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisions', to='countries_flavor.Country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'division',
                'verbose_name_plural': 'divisions',
                'ordering': ('country', 'code'),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('cla3', countries_flavor.fields.CodeISOField(length=3, max_length=3, primary_key=True, regex='[a-z]', serialize=False, validators=[django.core.validators.RegexValidator(regex='^[a-z]{3}$')], verbose_name='language code ISO 639-3')),
                ('cla2', countries_flavor.fields.CodeISOField(blank=True, length=3, max_length=3, regex='[a-z]', validators=[django.core.validators.RegexValidator(regex='^[a-z]{3}$')], verbose_name='language code ISO 639-1')),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
                'ordering': ('cla3',),
            },
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('code', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='code')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='locales', to='countries_flavor.Country', verbose_name='country')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locales', to='countries_flavor.Language', verbose_name='language')),
            ],
            options={
                'verbose_name': 'locale',
                'verbose_name_plural': 'locales',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Timezone',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='name')),
            ],
            options={
                'verbose_name': 'timezone',
                'verbose_name_plural': 'timezones',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(db_index=True, max_length=64, verbose_name='content ID')),
                ('text', models.CharField(max_length=128, verbose_name='text')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content type')),
                ('locale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='countries_flavor.Locale', verbose_name='locale')),
            ],
            options={
                'verbose_name': 'translation',
                'verbose_name_plural': 'translations',
                'ordering': ('content_type', 'object_id', 'locale'),
            },
        ),
        migrations.AddField(
            model_name='countryname',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='countries_flavor.Language', verbose_name='language'),
        ),
        migrations.AddField(
            model_name='country',
            name='currencies',
            field=models.ManyToManyField(to='countries_flavor.Currency', verbose_name='currencies'),
        ),
        migrations.AddField(
            model_name='country',
            name='languages',
            field=models.ManyToManyField(to='countries_flavor.Language', verbose_name='official languages'),
        ),
        migrations.AddField(
            model_name='country',
            name='timezones',
            field=models.ManyToManyField(to='countries_flavor.Timezone', verbose_name='timezones'),
        ),
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together=set([('content_type', 'object_id', 'locale')]),
        ),
        migrations.AlterUniqueTogether(
            name='division',
            unique_together=set([('code', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='countryname',
            unique_together=set([('country', 'language')]),
        ),
    ]
