# Generated by Django 2.0.13 on 2019-04-29 00:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20190428_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='observacao',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='rent',
            name='data_devolucao',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 0, 29, 51, 945082, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rent',
            name='data_rent',
            field=models.DateField(default=datetime.datetime(2019, 4, 29, 0, 29, 51, 945055, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rent',
            name='tipo',
            field=models.CharField(choices=[('Alugar', 'Alugar'), ('Comprar', 'Comprar')], max_length=50),
        ),
    ]
