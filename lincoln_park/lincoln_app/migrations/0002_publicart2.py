# Generated by Django 2.1.2 on 2018-11-07 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lincoln_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicArt2',
            fields=[
                ('geoid', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('park_name', models.CharField(blank=True, max_length=128, null=True)),
                ('park_number', models.SmallIntegerField(blank=True, null=True)),
                ('art_name', models.CharField(blank=True, max_length=128, null=True)),
                ('artist_name', models.CharField(blank=True, max_length=128, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'public_art2',
                'managed': False,
            },
        ),
    ]
