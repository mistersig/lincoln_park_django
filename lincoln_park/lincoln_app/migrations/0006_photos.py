# Generated by Django 2.1.2 on 2018-11-18 04:09

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lincoln_app', '0005_alllayers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('caption', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('image', models.CharField(blank=True, max_length=128, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'photos',
                'managed': False,
            },
        ),
    ]