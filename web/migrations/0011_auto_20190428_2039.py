# Generated by Django 2.0.13 on 2019-04-28 23:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20190428_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='tipo',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='rent',
            name='data_devolucao',
            field=models.DateField(default=datetime.datetime(2019, 4, 28, 23, 39, 50, 889094, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rent',
            name='data_rent',
            field=models.DateField(default=datetime.datetime(2019, 4, 28, 23, 39, 50, 889066, tzinfo=utc)),
        ),
    ]
