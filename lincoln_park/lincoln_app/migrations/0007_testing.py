# Generated by Django 2.1.2 on 2018-11-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lincoln_app', '0006_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('person_name', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'testing',
                'managed': False,
            },
        ),
    ]