# Generated by Django 2.2.6 on 2019-10-27 18:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies_api', '0005_auto_20191027_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='add_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 27, 18, 41, 32, 147544, tzinfo=utc)),
        ),
    ]
