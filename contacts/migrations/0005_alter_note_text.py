# Generated by Django 3.2.6 on 2021-08-12 01:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20210812_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(default=datetime.datetime(2021, 8, 12, 1, 20, 17, 919692, tzinfo=utc), max_length=2000),
            preserve_default=False,
        ),
    ]
