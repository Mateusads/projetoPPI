# Generated by Django 2.0.13 on 2019-04-29 01:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20190428_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='data_devolucao',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 1, 50, 32, 515085, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rent',
            name='data_rent',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 1, 50, 32, 515058, tzinfo=utc)),
        ),
    ]
